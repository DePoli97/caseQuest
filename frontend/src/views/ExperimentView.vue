<script>

import {defineComponent} from "vue";
import Selector from "@/components/Selector.vue";

export default defineComponent({
  components: {Selector},
  data: function () {
    return {
      camel_test: Object,
      kebab_test: Object,
      starting_test: Object,
      other_test: Object,
      test: Object,
      index: 0,
      completed_starting : false,
      startTime: 0,
    }
  },
  async mounted() {
    this.startTime = performance.now()
    await this.$store.dispatch('updateLastTestId')
    await this.$store.dispatch('getLastTestId')

    await this.$store.dispatch('fetchTest')
    this.camel_test = this.$store.state.camel_tests
    this.kebab_test = this.shuffleArray(this.$store.state.kebab_tests)
    for (let i = 0; i < this.camel_test.length; i++) {
      this.camel_test[i].sentence = this.shuffleArray(this.camel_test[i].sentence)
    }
    for (let i = 0; i < this.kebab_test.length; i++) {
      this.kebab_test[i].sentence = this.shuffleArray(this.kebab_test[i].sentence)
    }

    let choice = Math.floor(Math.random() * 2)
    if (choice === 0) {
      this.starting_test = this.camel_test
      this.other_test = this.kebab_test
    } else {
      this.starting_test = this.kebab_test
      this.other_test = this.camel_test
    }

    this.test = this.starting_test[0]
  },
  methods: {
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
      return array
    },
    async selectResponse(event) {
      let endTime = performance.now()

      if (this.completed)
        return

      let target = event.target
      let target_content = target.innerHTML
      let result = {
        id: this.$store.state.test_id,
        age: this.$store.state.age,
        gender: this.$store.state.gender,
        experience: this.$store.state.experience,
        case_type: this.test.case_type,
        question_number: this.test.question_number,
        n_words: this.test.n_words,
        is_correct_answer: target_content === this.test.case_answer,
        time: endTime - this.startTime,
        device: this.$store.state.device,
      }
      this.startTime = performance.now()
      await this.$store.dispatch('saveResult', result)
      this.index += 1
      if (this.index === this.starting_test.length && !this.completed_starting) {
        this.test = this.other_test[0]
        this.index = 0
        this.completed_starting = true
      } else if (this.index === this.starting_test.length && this.completed_starting) {
        this.$router.push('end')
      }
      else if (!this.completed_starting) {
        this.test = this.starting_test[this.index]
        this.test.sentence = this.shuffleArray(this.test.sentence)
      } else {
        this.test = this.other_test[this.index]
        this.test.sentence = this.shuffleArray(this.test.sentence)
      }
    }
  },
})
</script>

<template>
<!--  <Selector :test="test" :tutorial="false" :completedObj="completedObj" v-if="!completedObj.completed"/>-->
  <div class="centered-selector">
    <div class="grid-container" v-if="test.sentence">
      <div id="sentence" class="big-grid-item">{{test.answer}}</div>
      <div id="ArrowUp" class="grid-item" @click="selectResponse($event)">{{test.sentence[0]}}</div>
      <div id="ArrowLeft" class="grid-item" @click="selectResponse($event)">{{ test.sentence[1] }}</div>
      <div id="ArrowRight" class="grid-item" @click="selectResponse($event)">{{ test.sentence[2] }}</div>
      <div id="ArrowDown" class="grid-item" @click="selectResponse($event)">{{ test.sentence[3] }}</div>
    </div>
  </div>
  <p id="time"></p>
</template>

<style>

.centered-selector {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-bottom: 20px; /* Adjust as needed */
}

body {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}

.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 10px;
}

.grid-item {
  padding: 20px;
  text-align: center;
  cursor: pointer;
  font-size: 2em;
}

.big-grid-item {
  padding: 20px;
  text-align: center;
  grid-column: 1 / span 2;
  font-size: 3em;
}

div {
  color: #181818;
}

</style>