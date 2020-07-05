<template>
  <div class="
    fixed
    top-0
    left-0
    w-full
    h-full
    flex
    justify-center
    items-center
    bg-white
    bg-opacity-75
    z-10
  ">
    <div class="flex justify-center flex-wrap w-full">
      <p class="w-full text-base text-center">
        Loading...
      </p>

      <div class="
        relative
        w-48
        max-w-3/4
        h-4
        rounded-full
        bg-white border-2
        border-gray-700
        overflow-hidden
      ">
        <span class="
          progress
          block
          w-48
          h-3
          rounded-full
          bg-green-600
          -translate-x-full
        "></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style>
.progress {
  animation: scroll 2s infinite;
}

@keyframes scroll {
  0% {
    transform: translateX(-100%);
  }
  50% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(100%);
  }
}
</style>
