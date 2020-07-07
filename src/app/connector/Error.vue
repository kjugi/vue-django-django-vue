<template>
  <div class="error">
    <slot />
  </div>
</template>

<style lang="scss">
.error {
  @apply p-2;
  @apply text-center;
  @apply text-xl;
  @apply text-white;
  background: linear-gradient(90deg, rgba(204,0,20,1) 0%, rgba(255,73,92,1) 60%, rgba(204,0,20,1) 100%);
}
</style>
