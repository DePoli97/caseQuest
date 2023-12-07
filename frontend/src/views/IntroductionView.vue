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

  <h1> We have to write an explanation page about the experiment</h1>
  <h2> Maybe add form to ask if the user is going to use a mouse</h2>


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

</style>