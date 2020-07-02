import axios from 'axios'

export const writer = {
  namespaced: true,
  state: {
    writers: {},
  },
  mutations: {
    addWriter (state, data) {
      state.writers[data.id] = data.content
    },
  },
  actions: {
    async fetchSingleWriter ({ commit }, url) {
      const { data } = await axios(`http://127.0.0.1:8000/api/author/${url}`)

      commit('addWriter', {
        id: data.id,
        content: data
      })
    }
  },
  getters: {
    isWritterAvailable: (state) => (id) => {
      return !!state.writers[id]
    }
  }
}
