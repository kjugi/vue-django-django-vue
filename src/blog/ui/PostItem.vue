<template>
  <div class="post-item">
    <router-link
      :to="`/blog/${data.id}`"
      class="post-item__link"
    >
      <h3 class="post-item__title">
        {{ data.title }}
      </h3>

      <p class="post-item__content">
        {{ data.content.substr(0, 20) }}...
      </p>

      <div
        v-if="data.categories"
        class="post-item__categories"
      >
        <div
          v-for="(item, index) in data.categories"
          :key="index"
          class="post-item__category"
        >
          {{ data.text }}
        </div>
      </div>
    </router-link>
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
