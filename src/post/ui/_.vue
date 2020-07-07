<template>
  <div v-if="data">
    <h3 class="title relative text-2xl p-4 mb-8 border-2 border-black text-black">
      {{ data.title }}
    </h3>

    <p class="text-justify max-w-screen-md mx-auto">
      {{ data.content }}
    </p>

    <div
      v-if="data.categories"
      class="mt-8"
    >
      <div
        v-for="(item, index) in data.categories"
        :key="index"
      >
        {{ data.text }}
      </div>
    </div>

    <div class="author relative border-gray-700 border-2 p-4 mt-8">
      <h4 class="mb-4">
        <span class="border-b-2 border-black font-bold">
          Name:
        </span>

        {{ data.writer.name }}
      </h4>

      <p v-if="data.writer.bio">
        <span class="border-b-2 border-black font-bold">
          Bio:
        </span>

        {{ data.writer.bio }}
      </p>
    </div>
  </div>
  <error-component v-else>
    Problem with fetching data from api
  </error-component>
</template>

<script>
import axios from 'axios'

import ErrorComponent from '@/app/connector/Error.vue'

export default {
  components: {
    ErrorComponent
  },
  data () {
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

<style lang="scss" scoped>
.author:before {
  content: 'Author bio';
  @apply absolute;
  left: 16px;
  top: -10px;
  @apply text-base;
  @apply bg-white;
  @apply px-2;
}

.title:before {
  content: '';
  @apply absolute;
  background: #3DDC97;
  background: linear-gradient(90deg, #3ddc97 0%, #75e6b5 60%, #23be7b 100%);
  background-size: 400% 100%;
  width: 90%;
  height: 90%;
  top: -10px;
  left: -5%;
  z-index: -1;
  @apply transition-all;
  @apply duration-300;
  @apply ease-in-out;
  animation: backgroundAnimation 15s infinite;
}

@keyframes backgroundAnimation {
  0% {
		background-position: 0% 0%;
	}
	50% {
		background-position: 100% 0%;
	}
	100% {
		background-position: 0% 0%;
	}
}
</style>
