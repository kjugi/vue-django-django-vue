import axios from 'axios'

const blogModule = {
  state: {
    posts: {},
    postCount: 0,
    pagination: {
      prev: null,
      next: null
    }
  },
  mutations: {
    addPosts (state, data) {
      // TODO: push to array with page number key to not fetch from api each time
      state.posts = data
    },
    updateCount (state, count) {
      state.postCount = count
    },
    updatePagination (state, data) {
      state.pagination = data
    },
    updateError (state, data) {
      state.globalError = data
    }
  },
  actions: {
    async fetchPosts ({ commit }, pageNumber) {
      try {
        const { data } = await axios(`http://127.0.0.1:8000/api/post/?format=json&page=${pageNumber}`)

        commit('addPosts', data.results)
        commit('updateCount', data.count)
        commit('updatePagination', {
          prev: data.previous,
          next: data.next
        })
      } catch (error) {
        // TODO: Some global error handling in module
        commit('updateError', {
          status: true,
          message: error.message
        })
        console.error(error)
      }
    },
    // TODO: split into modules
    // TODO: fetch writters
  }
}

export default blogModule
