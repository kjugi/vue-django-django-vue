<template>
  <div class="p-8 border-b-2 border-gray-700">
    <router-link
      to="/"
      class="link"
    >
      Home
    </router-link>

    <router-link
      to="/about"
      class="link"
    >
      About
    </router-link>

    <router-link
      to="/blog"
      class="link"
    >
      Blog
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
.link {
  @apply relative;
  @apply px-2;
  @apply mx-2;
  @apply bg-white;
  @apply border-2;
  @apply border-green-400;
  @apply font-bold;
  @apply transition;
  @apply duration-100;

  &:after {
    content: '';
    @apply absolute;
    top: 0;
    left: 0;
    width: 115%;
    height: 130%;
    background: linear-gradient(to right, #c6ffdd, #fbd786, #f7797d, #fbd786, #c6ffdd);
    background-size: 400% 100%;
    z-index: -1;
    @apply transition-all;
    @apply duration-300;
    @apply ease-in-out;
  }

  &:hover {
    @apply bg-transparent;

    &:after {
      animation: backgroundAnimation 2s infinite;
    }
  }
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
