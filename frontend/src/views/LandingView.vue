<script>
export default {
  data: function () {
    return {
      age: 0,
      gender: '',
      experience: 0,
    }
  },
  methods: {
    saveResult(event) {
      event.preventDefault()
      let info = {
        gender: this.gender,
        age: this.age,
        experience: this.experience,
        id: this.$store.state.test_id,
      }
      console.log(info)
      this.$store.dispatch('setInfo', info)
      this.$router.push('introduction')
    }
  }
}

</script>

<template>
  <h1>Code Reading Experiment</h1>
  <p>Welcome to our experiment on code identifier readability!</p>
  <p>In this study, we aim to investigate whether reading speed is affected by the style of composed identifiers.</p>
  <p>The experiment will take around 6 minutes</p>
  <p>Please take a moment to provide some demographic information before starting the experiment.</p>

  <form method="get" @submit.prevent="saveResult">
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" required min="1" max="100" v-model="age" placeholder="1">

    <label for="gender">Gender:</label>
    <select id="gender" name="gender" required v-model="gender">
      <option value="male">Male</option>
      <option value="female">Female</option>
      <option value="other">Other</option>
    </select>

    <label for="experience">Coding Experience (years):</label>
    <input type="number" id="experience" name="experience" required v-model="experience" placeholder="0" min="0">

    <button type="submit">Start Experiment</button>
  </form>

  <p id="timer" style="color: red"></p>
</template>

<style>

</style>
