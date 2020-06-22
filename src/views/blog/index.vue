<template>
  <div>
    Blog page

    <div
      v-for="(item, index) in posts"
      :key="index"
    >
      {{ item }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  async mounted() {
    try {
      const { data } = await axios('http://127.0.0.1:8000/api/post/?format=json')

      this.posts = data
    } catch (error) {
      console.error(error)
    }
  },
  data () {
    return {
      posts: []
    }
  }
}
</script>
