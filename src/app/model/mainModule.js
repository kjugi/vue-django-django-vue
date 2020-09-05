import axios from 'axios'

export const main = {
  namespaced: true,
  state: {
    posts: null,
    postCount: 0,
    pagination: {
      prev: null,
      next: null
    }
  },
  mutations: {
    addPosts (state, data) {
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
    async fetchBlogEndpoint ({ commit }, params) {
      try {
        const { data } = await axios('http://127.0.0.1:8000/api/post/', {
          params: {
            format: 'json',
            ...params
          }
        })

        commit('addPosts', data.results)
        commit('updateCount', data.count)
        commit('updatePagination', {
          prev: data.previous,
          next: data.next
        })
      } catch (error) {
        commit('addPosts', null)
        commit('updateCount', 0)
        commit('updatePagination', {
          prev: null,
          next: null
        })
      }
    }
  }
}
