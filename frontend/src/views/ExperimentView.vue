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
    }
  },
  async mounted() {
    await this.$store.dispatch('updateLastTestId')
    await this.$store.dispatch('getLastTestId')

    await this.$store.dispatch('fetchTest')
    this.camel_test = this.$store.state.camel_tests[0]
    this.kebab_test = this.$store.state.kebab_tests[0]

    this.test = this.camel_test
  },
})
</script>

<template>
  <Selector :test="test" :tutorial="false"/>
</template>

<style scoped>

</style>