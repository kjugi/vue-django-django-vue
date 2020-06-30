import Vue from 'vue'
import Vuex from 'vuex'

import { blog } from '@/blog/model/blogModule.js'
import { mainModule } from './mainModule.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    mainModule,
    blogModule
    blog
  }
})
