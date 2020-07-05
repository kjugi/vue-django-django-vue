<template>
  <div>
    <h1 class="text-center text-3xl mb-4">
      Blog page
    </h1>

    <loader v-if="isFetching" />

    <template v-if="!isFetchingError.status">
      <div class="flex flex-wrap mx-auto">
        <post-item
          v-for="(item, index) in posts"
          :key="index"
          :data="item"
        />
      </div>

      <div class="flex justify-center">
        <router-link
          v-if="pagination.prev"
          :to="`/blog/${pageNumber-1}`"
        >
          Previous page
        </router-link>

        <router-link
          v-if="pagination.next"
          :to="`/blog/${pageNumber+1}`"
        >
          Next page
        </router-link>
      </div>
    </template>
    <p v-else>
      Problem with fetching data from api: {{ isFetchingError.message }}
    </p>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import PostItem from './PostItem.vue'
import Loader from '@/app/ui/Loader.vue'

export default {
  components: {
    PostItem,
    Loader
  },
  async mounted() {
    await this.handleFetching()
  },
  data () {
    return {
      isFetching: false,
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
    pageNumber () {
      return Number(this.$route.params?.id || 1)
    }
  },
  watch: {
    $route(to, from) {
      // Don't need to reload page when entering same page blog number
      if (
        to.params.id === '1' && !from.params.id ||
        !to.params.id && from.params.id === '1'
      ) {
        return
      }

      this.handleFetching()
    }
  },
  methods: {
    ...mapActions('blog', [
      'fetchPosts'
    ]),
    async handleFetching () {
      try {
        this.isFetching = true

        // Get post for page
        await this.fetchPosts(this.$route.params.id || 1)
      } catch (error) {
        this.isFetchingError = {
          status: true,
          message: error.message
        }
      } finally {
        this.isFetching = false
      }
    }
  }
}
</script>
