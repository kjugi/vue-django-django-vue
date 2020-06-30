import Vue from 'vue'
import Vuex from 'vuex'

import { blog } from '@/blog/model/blogModule.js'
import { writer } from '@/writer/model/writerModule.js'
import { mainModule } from './mainModule.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    mainModule,
    writer,
    blog
  }
})
