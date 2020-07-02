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

      // TODO: Check store for writer or fetch from API by url
      this.data = data
    } catch (error) {
      this.data = false
    }
  }
}
</script>
