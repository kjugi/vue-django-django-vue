<template>
  <div class="post-item">
    <router-link
      :to="`/blog/${data.id}`"
      class="post-item__link"
    >
      <img
        :src="data.featureImage || '../images/placeholder-image.png'"
        class="post-item__image"
      />

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

<style>
.post-item {
  width: calc(50% - 32px);
  border: 1px solid #393E41;
  padding: 12px;
  margin: 0 12px 12px 0;
  text-align: left;
}

.post-item:nth-child(2n) {
  margin-right: 0;
}

.post-item__link {
  color: #2c3e50;
  text-decoration: none;
}

.post-item__link:hover,
.post-item__link:focus {
  cursor: pointer;
}
</style>
