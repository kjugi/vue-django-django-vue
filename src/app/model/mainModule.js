export const mainModule = {
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
}
