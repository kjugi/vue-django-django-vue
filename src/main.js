import Vue from 'vue'
import App from './app/ui/App.vue'
import './registerServiceWorker'
import router from './app/router'
import store from './app/model/store'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
