<template>
  <div class="blog">
    Blog page

    <template v-if="!isFetchingError.status">
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
    </template>
    <p v-else>
      Problem with fetching data from api: {{ isFetchingError.message }}
    </p>
  </div>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'

import PostItem from './PostItem.vue'

export default {
  components: {
    PostItem
  },
  async mounted() {
    await this.handleFetching()
  },
  data () {
    return {
      // TODO: Get page number from url and put it into url
      pageNumber: 1,
      isFetchingError: {
        status: false,
        message: null
      }
    }
  },
  computed: {
    ...mapState('blog', [
      'posts',
      'pagination'
    ]),
    ...mapGetters('writer', [
      'isWritterAvailable'
    ])
  },
  methods: {
    ...mapActions('blog', [
      'fetchPosts'
    ]),
    ...mapActions('writer', [
      'fetchSingleWriter'
    ]),
    async handleFetching () {
      try {
        // Get post for page
        await this.fetchPosts(this.pageNumber)

        // Fetch post authors
        this.posts.map(async (post) => {
          if (!this.isWritterAvailable(post.writer)) {
            await this.fetchSingleWriter(post.writer)
          }
        })
      } catch (error) {
        this.isFetchingError = {
          status: true,
          message: error.message
        }
      }
    },
    async getPage (newPageNumber) {
      this.pageNumber = newPageNumber
      await this.handleFetching()
    }
  }
}
</script>

<style>
.blog__wrapper {
  display: flex;
  flex-wrap: wrap;
  max-width: 800px;
  margin: 0px auto;
}
</style>
