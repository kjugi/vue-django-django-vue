<template>
  <router-link
    :to="`/post/${data.id}`"
    class="item p-4 m-4 border-2 border-gray-500 text-left text-gray-700 no-underline"
  >
    <img
      v-if="imageHasError"
      :src="data.featureImage"
      class="max-w-full"
      @error="imageHasError = true"
    />

    <h3 class="post-item__title">
      {{ data.title }}
    </h3>

    <p class="post-item__content">
      {{ data.content.substr(0, 20) }}...
    </p>

    <div
      v-if="data.categories"
      class="post-item__categories"
    >
      <div
        v-for="(item, index) in data.categories"
        :key="index"
        class="post-item__category"
      >
        {{ data.text }}
      </div>
    </div>

    <div class="post-item__author">
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

<style>
.item {
  width: calc(50% - 2rem);
}
</style>
