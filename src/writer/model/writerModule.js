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
      const { data } = await axios(url)

      commit('addWriter', {
        id: data.id,
        content: data
      })
    }
  }
}
