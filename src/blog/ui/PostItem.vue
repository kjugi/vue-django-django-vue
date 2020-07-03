<template>
  <router-link
    :to="`/blog/${data.id}`"
    class="post-item"
  >
    <img
      v-if="imageHasError"
      :src="data.featureImage"
      class="post-item__image"
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
.post-item {
  width: calc(50% - 32px);
  border: 1px solid #393E41;
  padding: 12px;
  margin: 0 12px 12px 0;
  color: #2c3e50;
  text-align: left;
  text-decoration: none;
}

.post-item:hover,
.post-item:focus {
  cursor: pointer;
}

.post-item:nth-child(2n) {
  margin-right: 0;
}

.post-item__image {
  max-width: 100%;
}
</style>
