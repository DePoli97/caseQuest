<script>
export default {
  data: function () {
    return {
      completed: false,
      last_selection: null
    }
  },
  mounted() {
    this.startTime = performance.now()
  },
  props: {
    completedObj: Object,
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
    async selectResponse(event) {
      if (this.last_selection) {
        this.last_selection.style.backgroundColor = '';
      }

      let target = event.target
      this.last_selection = target
      let target_content = target.innerHTML
      if (this.tutorial) {
        if (target_content === this.test.case_answer) {
          target.style.backgroundColor = 'green'
        } else {
          target.style.backgroundColor = 'red'
        }
        this.completed = true
      }
    }
  }
}

</script>

<template>
  <div class="grid-container" v-if="test.sentence">
    <div id="sentence" class="big-grid-item">{{test.answer}}</div>
    <div id="ArrowUp" class="grid-item" @click="selectResponse($event)">{{test.sentence[0]}}</div>
    <div id="ArrowLeft" class="grid-item" @click="selectResponse($event)">{{ test.sentence[1] }}</div>
    <div id="ArrowRight" class="grid-item" @click="selectResponse($event)">{{ test.sentence[2] }}</div>
    <div id="ArrowDown" class="grid-item" @click="selectResponse($event)">{{ test.sentence[3] }}</div>
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