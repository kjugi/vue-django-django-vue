<template>
  <div>
    <loader v-if="isFetching" />

    <h1 class="text-center text-3xl mb-4">
      Blog page
    </h1>

    <template v-if="postCount > 0">
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
          class="link relative uppercase border-2 p-2 mx-4"
        >
          Previous page
        </router-link>

        <router-link
          v-if="pagination.next"
          :to="`/blog/${pageNumber+1}`"
          class="link relative uppercase border-2 p-2 mx-4"
        >
          Next page
        </router-link>
      </div>
    </template>
    <p
      v-else-if="posts && postCount === 0"
      class="text-center text-2xl mb-4"
    >
      Writer don't have any posts yet.
    </p>
    <error-component v-else>
      Problem with fetching data from api: {{ isFetchingError }}
    </error-component>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

import PostItem from '@/app/ui/PostItem.vue'
import Loader from '@/app/ui/Loader.vue'
import ErrorComponent from '@/app/connector/Error.vue'

export default {
  components: {
    PostItem,
    Loader,
    ErrorComponent
  },
  async mounted() {
    await this.handleFetching()
  },
  data () {
    return {
      isFetching: false,
      isFetchingError: null
    }
  },
  computed: {
    ...mapState('main', [
      'posts',
      'postCount',
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
    ...mapActions('main', [
      'fetchBlogEndpoint'
    ]),
    async handleFetching () {
      try {
        this.isFetching = true

        // Get post for page
        await this.fetchBlogEndpoint({
          page: this.$route.params.id || 1
        })
      } catch (error) {
        this.isFetchingError = error.message
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
