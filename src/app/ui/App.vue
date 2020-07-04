<template>
  <div class="m-0 font-display">
    <div class="p-8">
      <router-link
        to="/"
        class="font-bold text-green-400"
      >
        Home
      </router-link>

      <router-link
        to="/about"
        class="font-bold text-green-400"
      >
        About
      </router-link>

      <router-link
        to="/blog"
        class="font-bold text-green-400"
      >
        Blog
      </router-link>
    </div>

    <router-view/>
  </div>
</template>

<style src="../assets/tailwind.css"></style>

<style lang="scss">
a.router-link-exact-active {
  @apply text-gray-600;
}
</style>
