import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Post from '../views/blog/_.vue'
import Blog from '../views/blog/index.vue'

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
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/blog',
    component: Blog
  },
  {
    path: '/blog/:id',
    component: Post,
    children: [
      { path: '', component: Blog }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
