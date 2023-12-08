<script>
export default {
  data: function () {
    return {
      age: 0,
      gender: '',
      experience: '',
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
  <p>We aim to investigate whether reading speed is affected by the style of composed identifiers.</p>
  <p>The experiment will take about 5 minutes</p>
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

    <label for="experience">Coding Experience:</label>
    <select v-model="experience" id="experience" name="experience" required>
      <option value="No">No experience</option>
      <option value="1-3">1-3 years</option>
      <option value="3+">3+ years</option>
    </select>

    <button type="submit">Start Experiment</button>
  </form>

  <p id="timer" style="color: red"></p>
</template>

<style>

</style>
