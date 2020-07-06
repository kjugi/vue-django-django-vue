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

      <div class="flex justify-center my-8">
        <router-link
          v-if="pagination.prev"
          :to="`/blog/${pageNumber-1}`"
          class="link relative uppercase border-2 p-2"
        >
          Previous page
        </router-link>

        <router-link
          v-if="pagination.next"
          :to="`/blog/${pageNumber+1}`"
          class="link relative uppercase border-2 p-2"
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

<style lang="scss" scoped>
.link {
  @apply border-black;
  @apply text-white;
  @apply transition-all;
  @apply duration-500;

  &:after {
    content: '';
    @apply absolute;
    top: -10px;
    left: -10px;
    width: 110%;
    @apply h-full;
    background: rgb(0,108,255);
    transition: height 0.4s ease-in, top 0.3s ease;
    z-index: -1;
  }

  &:hover {
    @apply text-black;

    &:after {
      top: 25px;
      @apply h-0;
    }
  }
}
</style>
