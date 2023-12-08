<script>
export default {
  data() {
    return {
      selectedDevice: 'Mouse',
      otherDeviceDetails: ''
    };
  },
  methods: {
    goToTutorial() {
      const selectedDevice = this.selectedDevice;
      const details = (selectedDevice === 'Other') ? this.otherDeviceDetails : '';
      this.$store.dispatch('setDevice', { selectedDevice, details });

      this.$router.push('tutorial')
    }
  }
}

</script>

<template>
  <h3> Get ready for a series of questions where you'll need to pick the correct answer  as quickly as possible. </h3>
  <h3> Options can appear in two styles: camelCase or kebab-case. </h3>
  <h3> Here's what's in store:</h3>
  <div>
  <ul>
    <li> You'll face 20 questions in total — 10 for each type of identifier. </li>
    <li> You'll begin with a random selection between camelCase or kebab-case. </li>
    <li> Once started, you'll complete all 10 tests in a row for the chosen style before moving on to the other 10 tests
      in the opposite identifier style. </li>
  </ul>
  </div>
  <h4> Please select the input device you'll be using to participate in the experiment and follow the tutorial to
    familiarize yourself with the answer selection process. </h4>


  <form @submit.prevent="goToTutorial">
    <label for="deviceType">Select your device type:</label>
    <select v-model="selectedDevice" id="deviceType" name="deviceType">
      <option value="Mouse">Mouse</option>
      <option value="Trackpad">Trackpad</option>
      <option value="Other">Other</option>
    </select>
    <br>
    <div v-if="selectedDevice === 'Other'">
      <label for="otherDetails">Please specify:</label>
      <input type="text" v-model="otherDeviceDetails" id="otherDetails" name="otherDetails" required>
    </div>
    <br>
    <button type="submit"> Go To Tutorial </button>
  </form>

</template>

<style scoped>

h3, h4 {
  margin-block: 20px;
}
ul {
  list-style-type: none;
  text-align: center;
}
li {
  margin-block: 10px;
}
div {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>