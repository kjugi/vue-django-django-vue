<template>
  <router-link
    :to="`/post/${data.id}`"
    class="
      item
      relative
      p-4
      m-4
      bg-white
      border-2
      border-gray-500
      text-left
      text-gray-700
      no-underline
      hover:border-gray-800
      hover:text-gray-800
      transition
      duration-200
      ease-in-out
    "
  >
    <img
      v-if="imageHasError"
      :src="data.featureImage"
      class="max-w-full"
      @error="imageHasError = true"
    />

    <h3 class="title relative inline-block bg-white text-2xl px-2">
      {{ data.title }}
    </h3>

    <p class="mb-4 pb-2 border-b-2">
      {{ data.content.substr(0, 20) }}...
    </p>

    <div
      v-if="data.categories"
      class="mb-2 pb-2"
    >
      <div
        v-for="(item, index) in data.categories"
        :key="index"
      >
        {{ data.text }}
      </div>
    </div>

    <div class="text-sm text-right uppercase">
      Author: {{ data.writer.name }}
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      imageHasError: false
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  top: -30px;
}

.item {
  @apply w-full;

  @media (min-width: 768px) {
    width: calc(50% - 2rem);
  }

  &:after {
    content: '';
    @apply absolute;
    bottom: 0;
    right: 0;
    @apply w-full;
    background: rgb(0,108,255);
    background: linear-gradient(90deg, rgba(0,108,255,1) 0%, rgba(83,172,255,1) 60%, rgba(0,113,255,1) 100%);
    background-size: 400% 100%;
    height: 80%;
    z-index: -1;
    @apply transition-all;
    @apply duration-300;
    @apply ease-in-out;
    animation: backgroundAnimation 4s infinite;
  }

  &:hover {
    &:after {
      bottom: -10px;
      right: -10px;
    }
  }
}

@keyframes backgroundAnimation {
  0% {
		background-position: 0% 0%;
	}
	50% {
		background-position: 100% 0%;
	}
	100% {
		background-position: 0% 0%;
	}
}
</style>
