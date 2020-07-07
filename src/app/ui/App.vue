<template>
  <div class="m-0 font-display">
    <navigation />

    <router-view class="container mx-auto py-4" />
  </div>
</template>

<script>
import Navigation from './Navigation.vue'

export default {
  components: {
    Navigation
  }
}
</script>

<style src="../assets/tailwind.css"></style>
