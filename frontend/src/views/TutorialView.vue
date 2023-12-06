<script>

import Selector from "@/components/Selector.vue";

export default {
  data: function () {
    return {
      camel_test: Object,
      kebab_test: Object,
      completed_camel: false,
      completed_kebab: false,

      counter: null,
      current_camel: true,
    }
  },
  components: {Selector},
  async mounted() {
    await this.$store.dispatch('fetchTest')
    this.camel_test = this.$store.state.camel_tests[0]
    this.kebab_test = this.$store.state.kebab_tests[0]
  },
  watch: {
    completed_camel: {
      immediate: false,
      deep: true,
      handler: function (val) {
        if (val) {
          this.completed_camel = true
        }
      }
    },
  },
  methods: {
    changeTest() {
      this.current_camel = !this.current_camel
    },
    goToExperiment() {
      let countdown_value = 3
      this.counter = countdown_value
      let countdown = setInterval(() => {
        if (countdown_value === 0) {
          clearInterval(countdown)
          this.$router.push('experiment')
        }
        countdown_value -= 1
        this.counter = countdown_value
      }, 1000)

    }
  }
}
</script>

<template>
  <h1> This is a Warm Up! </h1>
  <h2> Try out the selection process as long as you wish</h2>

  <Selector :test="camel_test" :tutorial="true" v-if="current_camel"/>
  <Selector :test="kebab_test" :tutorial="true" v-else/>

  <button @click="changeTest">Switch to <span v-if="current_camel">kebab</span><span v-else>camel</span> case</button>

  <h3> When you are ready, press here to start the experiment </h3>
  <button @click="goToExperiment"> Go To Experiment </button>
  <h3 v-if="counter !== null">{{counter}}</h3>
</template>

<style>

</style>