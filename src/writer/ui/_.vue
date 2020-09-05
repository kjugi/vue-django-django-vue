<template>
  <div>
    <loader v-if="isFetching" />

    <full-writer-info
      v-if="writerData"
      :data="writerData"
    />

    <template v-if="postCount > 0">
      <h2 class="text-center text-2xl mb-4">
        Writer posts
      </h2>

      <div class="flex flex-wrap mx-auto">
        <post-item
          v-for="(item, index) in posts"
          :key="index"
          :data="item"
        />
      </div>

      <div class="flex justify-center my-8">
        <button
          v-if="pagination.prev"
          class="link relative uppercase border-2 p-2 mx-4"
          @click="fetchPostPage(pageNumber - 1)"
        >
          Previous page
        </button>

        <button
          v-if="pagination.next"
          class="link relative uppercase border-2 p-2 mx-4"
          @click="fetchPostPage(pageNumber + 1)"
        >
          Next page
        </button>
      </div>
    </template>
    <p
      v-else-if="posts && postCount === 0"
      class="text-center text-2xl mb-4"
    >
      Writer don't have any posts yet.
    </p>

    <error-component v-if="(!writerData || !posts) && !isFetching">
      Problem with fetching data from api
    </error-component>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import axios from 'axios'

import FullWriterInfo from './FullWriterInfo.vue'
import Loader from '@/app/ui/Loader.vue'
import PostItem from '@/app/ui/PostItem.vue'
import ErrorComponent from '@/app/connector/Error.vue'

export default {
  components: {
    FullWriterInfo,
    Loader,
    PostItem,
    ErrorComponent
  },
  data () {
    return {
      writerData: null,
      pageNumber: 1,
      isFetching: true
    }
  },
  computed: {
    ...mapState('main', [
      'posts',
      'postCount',
      'pagination'
    ])
  },
  async mounted() {
    try {
      const writerData = await axios(
        `http://127.0.0.1:8000/api/author/${this.$route.params.id}/?format=json`
      )

      this.writerData = writerData.data

      await this.fetchPostPage(1)
    } catch (err) {
      this.writerData = false
    } finally {
      this.isFetching = false
    }
  },
  watch: {
    $route() {
      this.fetchPostPage(1)
    }
  },
  methods: {
    ...mapActions('main', [
      'fetchBlogEndpoint'
    ]),
    async fetchPostPage(pageNumber) {
      if (!this.isFetching) {
        this.isFetching = true
      }

      await this.fetchBlogEndpoint({
        page: pageNumber,
        'writer_id': this.$route.params.id
      })

      this.pageNumber = pageNumber
      this.isFetching = false
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
