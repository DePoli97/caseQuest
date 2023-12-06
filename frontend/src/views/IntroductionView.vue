<script>
export default {
  methods: {
    goToTutorial() {
      this.$router.push('tutorial')
    }
  }
}

</script>

<template>

  <h1> We have to write an explanation page about the experiment</h1>
  <h2> Maybe add form to ask if the user is going to use a mouse</h2>
  <button @click="goToTutorial"> Go To Tutorial </button>
</template>

<style scoped>

</style>