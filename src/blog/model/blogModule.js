import axios from 'axios'

export const blog = {
  namespaced: true,
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
    }
  },
  actions: {
    async fetchPosts ({ commit, dispatch }, pageNumber) {
      const { data } = await axios(`http://127.0.0.1:8000/api/post/?format=json&page=${pageNumber}`)

      commit('addPosts', data.results)
      commit('updateCount', data.count)
      commit('updatePagination', {
        prev: data.previous,
        next: data.next
      })

      // Get only unique writers
      data.results.map(async el => {
        // TODO: Searching for existing writer by getter to not request multiple times
        await dispatch('writer/fetchSingleWriter', el.writer, { root: true })
      })
    }
  }
}
