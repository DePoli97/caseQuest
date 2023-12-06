<script>

import {defineComponent} from "vue";
import Selector from "@/components/Selector.vue";

export default defineComponent({
  components: {Selector},
  data: function () {
    return {
      camel_test: Object,
      kebab_test: Object,
      test: Object,
      index: 0,
      completed_camel : false,
      startTime: 0,
    }
  },
  async mounted() {
    await this.$store.dispatch('updateLastTestId')
    await this.$store.dispatch('getLastTestId')

    await this.$store.dispatch('fetchTest')
    this.camel_test = this.$store.state.camel_tests
    this.kebab_test = this.$store.state.kebab_tests

    this.test = this.camel_test[0]
  },
  methods: {
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
        is_correct_answer: target_content === this.test.case_answer,
        time: endTime - this.startTime,
      }
      this.startTime = performance.now()
      await this.$store.dispatch('saveResult', result)
      this.index += 1
      if (this.index === this.camel_test.length-1 && !this.completed_camel) {
        this.test = this.kebab_test[0]
        this.index = 0
        this.completed_camel = true
      } else if (!this.completed_camel) {
        this.test = this.camel_test[this.index]
      } else {
        this.test = this.kebab_test[this.index]
      }
    }
  },
})
</script>

<template>
<!--  <Selector :test="test" :tutorial="false" :completedObj="completedObj" v-if="!completedObj.completed"/>-->
  <div class="grid-container" v-if="test.sentence">
    <div></div>
    <div id="ArrowUp" class="grid-item" @click="selectResponse($event)">{{test.sentence[0]}}</div>
    <div></div>
    <div id="ArrowLeft" class="grid-item" @click="selectResponse($event)">{{ test.sentence[1] }}</div>

    <div id="sentence" class="grid-item">{{test.answer}}</div>

    <div id="ArrowRight" class="grid-item" @click="selectResponse($event)">{{ test.sentence[2] }}</div>
    <div></div>
    <div id="ArrowDown" class="grid-item" @click="selectResponse($event)">{{ test.sentence[3] }}</div>
    <div></div>
  </div>
  <p id="time"></p>
</template>

<style>
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
  align-items: center;
  justify-content: center;
  width: 70%;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px; /* Adjust the gap as needed */
}

.grid-item {
  text-align: center;
  border: 1px solid #ccc;
  padding: 20px;
  cursor: pointer ;
}

div {
  color: #181818;
}
</style>