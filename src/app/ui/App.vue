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

<style lang="scss">
a.router-link-exact-active {
  @apply text-green-400;
}

.error {
  @apply p-2;
  @apply text-center;
  @apply text-xl;
  @apply text-white;
  background: linear-gradient(90deg, rgba(204,0,20,1) 0%, rgba(255,73,92,1) 60%, rgba(204,0,20,1) 100%);
}
</style>
