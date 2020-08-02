<template>
  <div v-if="writerData && postData">
    <full-writer-info :data="writerData"/>

    <h2 class="text-center text-2xl mb-4">
      Writer posts
    </h2>

    <loader v-if="isFetching" />

    <template v-if="!isFetchingError.status">
      <div class="flex flex-wrap mx-auto">
        <post-item
          v-for="(item, index) in postData.results"
          :key="index"
          :data="item"
        />
      </div>

      <div class="flex justify-center my-8">
        <button
          v-if="postData.previous"
          class="link relative uppercase border-2 p-2 mx-4"
          @click="fetchPostPage(pageNumber - 1)"
        >
          Previous page
        </button>

        <button
          v-if="postData.next"
          class="link relative uppercase border-2 p-2 mx-4"
          @click="fetchPostPage(pageNumber + 1)"
        >
          Next page
        </button>
      </div>
    </template>
  </div>
  <error-component v-else>
    Problem with fetching data from api
  </error-component>
</template>

<script>
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
      postData: null,
      pageNumber: 1,
      isFetching: false,
      isFetchingError: {
        status: false,
        message: null
      }
    }
  },
  async mounted() {
    const writerData = await axios(
      `http://127.0.0.1:8000/api/author/${this.$route.params.id}/?format=json`
    )
    await this.fetchPostPage(1)

    this.writerData = writerData.data
  },
  methods: {
    async fetchPostPage(pageNumber) {
      try {
        this.isFetching = true

        const postData = await axios(
          `http://127.0.0.1:8000/api/post/?ormat=json&writer_id=${this.$route.params.id}&page=${pageNumber}`
        )

        this.pageNumber = pageNumber
        this.postData = postData.data
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
