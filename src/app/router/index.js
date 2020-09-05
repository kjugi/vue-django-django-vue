import Vue from 'vue'
import VueRouter from 'vue-router'
import BlogPost from '@/blog/ui/_slug.vue'
import Blog from '@/blog/ui/index.vue'
import Writer from '@/writer/ui/_.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Blog',
    component: Blog
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
    path: '/post/:slug',
    name: 'post',
    component: BlogPost
  },
  {
    path: '/writer/:id',
    component: Writer
  }
]

const router = new VueRouter({
  routes
})

export default router
