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
      }
      console.log(info)
      this.$store.dispatch('setInfo', info)
    }
  }
}

</script>

<template>
  <h1>Code Reading Experiment</h1>
  <p>Welcome to our experiment on code identifier readability!</p>
  <p>In this study, we aim to investigate whether reading speed is affected by the style of composed identifiers.</p>
  <p>Please take a moment to provide some demographic information before starting the experiment.</p>

  <form method="get" @submit.prevent="saveResult">
    <label for="age">Age:</label>
    <input type="number" id="age" name="age" required max="100" v-model="age">

    <label for="gender">Gender:</label>
    <select id="gender" name="gender" required v-model="gender">
      <option value="male">Male</option>
      <option value="female">Female</option>
      <option value="other">Other</option>
    </select>

    <label for="experience">Coding Experience (years):</label>
    <input type="number" id="experience" name="experience" required v-model="experience">

    <button type="submit">Start Experiment</button>
  </form>

  <p id="timer" style="color: red"></p>
</template>

<style>
body {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
  background-color: #f4f4f4;
}

h1 {
  color: #333;
}

p {
  color: #555;
  margin-bottom: 20px;
}

form {
  max-width: 400px;
  margin: 0 auto;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

label {
  display: block;
  margin-bottom: 10px;
  text-align: left;
  color: #333;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

select {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
  color: white;
  padding: 15px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
