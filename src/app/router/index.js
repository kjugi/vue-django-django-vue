import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/homepage/ui/Home.vue'
import BlogPost from '@/blog/ui/_slug.vue'
import Blog from '@/blog/ui/index.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/about/ui/About.vue')
  },
  {
    path: '/blog',
    component: Blog
  },
  {
    path: '/blog/:id',
    component: Blog
  },
  {
    path: '/blog/:slug',
    name: 'post',
    component: BlogPost
  }
]

const router = new VueRouter({
  routes
})

export default router
