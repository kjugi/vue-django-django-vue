<template>
  <div class="blog">
    Blog page

    <div class="blog__wrapper">
      <post-item
        v-for="(item, index) in posts"
        :key="index"
        :data="item"
      />
    </div>

    <div class="blog__pagination">
      <button
        v-if="pagination.prev"
        type="button"
        @click="getPage(pageNumber-1)"
      >
        Previous page
      </button>

      <button
        v-if="pagination.next"
        type="button"
        @click="getPage(pageNumber+1)"
      >
        Next page
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import PostItem from '@/components/PostItem.vue'

export default {
  components: {
    PostItem
  },
  async mounted() {
    await this.fetchPosts(this.pageNumber)
  },
  data () {
    return {
      // TODO: Get page number from url and put it into url
      pageNumber: 1
    }
  },
  computed: {
    ...mapState([
      'posts',
      'pagination'
    ])
  },
  methods: {
    ...mapActions([
      'fetchPosts'
    ]),
    async getPage (newPageNumber) {
      this.pageNumber = newPageNumber
      await this.fetchPosts(this.pageNumber)
    }
  }
}
</script>
