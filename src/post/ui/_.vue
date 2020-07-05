<template>
  <div
    v-if="data"
    class='post'
  >
    <h3 class="post__title">
      {{ data.title }}
    </h3>

    <p class="post__content">
      {{ data.content }}
    </p>

    <div
      v-if="data.categories"
      class="post__categories"
    >
      <div
        v-for="(item, index) in data.categories"
        :key="index"
        class="post__category"
      >
        {{ data.text }}
      </div>
    </div>

    <div class="author relative border-gray-700 border-2 p-4 mt-4">
      <h4 class="post__author-name">
        Name: {{ data.writer.name }}
      </h4>

      <p
        v-if="data.writer.bio"
        class="post__author-bio"
      >
        {{ data.writer.bio }}
      </p>
    </div>
  </div>
  <p v-else>
    Problem with fetching data from api
  </p>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      data: null
    }
  },
  async mounted() {
    try {
      const { data } = await axios(
        `http://127.0.0.1:8000/api/post/${this.$route.params.id}/?format=json`
      )

      this.data = data
    } catch (error) {
      this.data = false
    }
  }
}
</script>

<style lang="scss">
.author:before {
  content: 'Author bio';
  @apply absolute;
  left: 16px;
  top: -10px;
  @apply text-base;
  @apply bg-white;
  @apply px-2;
}
</style>
