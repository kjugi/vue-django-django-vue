<template>
  <div class="
    item
    relative
    p-4
    m-4
    bg-white
    border-2
    border-gray-500
    text-left
    text-gray-700
  ">
    <h1 class="title relative inline-block bg-white text-2xl px-2">
      Writer info
    </h1>

    <p class="mb-4">
      <span class="border-b-2 border-black font-bold">
        Name:
      </span>

      {{ data.name }}
    </p>

    <p
      class="mb-4"
      v-if="data.bio"
    >
      <span class="border-b-2 border-black font-bold">
        Bio:
      </span>

      {{ data.bio }}
    </p>

    <p
      class="mb-4"
      v-if="data.email"
    >
      <span class="border-b-2 border-black font-bold">
        email:
      </span>

      <a :href="`mailto:${data.email}`" target="_blank">
        {{ data.email }}
      </a>
    </p>

    <ul>
      <li
        v-for="(link, key) in data.socialLinks"
        :key="key"
      >
        <router-link
          :to="link.url"
          class="border-b-2 border-black font-bold"
        >
          link.title
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: true
    }
  }
}
</script>

<style lang="scss" scoped>
.title {
  top: -30px;
}

</style>
