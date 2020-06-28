import Vue from 'vue'
import Vuex from 'vuex'

import blogModule from '@/blog/model/blogModule.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    blogModule
  },
  state: {
    globalError: {
      status: false,
      message: null
    }
  },
  mutations: {
    updateError (state, data) {
      state.globalError = data
    }
  }
})
