<script>
export default {
  data: function () {
    return {
      completed: false,
    }
  },
  mounted() {
    this.startTime = performance.now()
  },
  props: {
    completed: Boolean,
    test: Object,
    tutorial: Boolean
  },
  watch: {
    experiment: {
      immediate: false,
      deep: false,
    }
  },
  methods: {
    async sendResult() {
      if (this.tutorial) {
        return
      }
      await this.$store.dispatch('sendResult', test_result)
    },
    async selectResponse(event) {
      let endTime = performance.now()

      if (this.completed)
        return

      let target = event.target
      let target_content = target.innerHTML
      if (this.tutorial) {
        if (target_content === this.test.case_answer) {
          target.style.backgroundColor = 'green'
        } else {
          target.style.backgroundColor = 'red'
        }
        this.completed = true
        return
      }
      let result = {
        id: this.$store.state.test_id,
        age: this.$store.state.age,
        gender: this.$store.state.gender,
        experience: this.$store.state.experience,
        case_type: this.test.case_type,
        is_correct_answer: target_content === this.test.case_answer,
        time: endTime - this.startTime,
      }
      await this.$store.dispatch('saveResult', result)
      this.completed = true
    }
  }
}

</script>

<template>
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

<style scoped>
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