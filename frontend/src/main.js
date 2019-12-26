import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import PaperDashboard from "./plugins/paperDashboard";
import "vue-notifyjs/themes/default.css";

//These imports are for nice icons
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { faRss } from '@fortawesome/free-solid-svg-icons'
import { faSearch } from '@fortawesome/free-solid-svg-icons'
import { faSignInAlt } from '@fortawesome/free-solid-svg-icons'
import { faBookReader } from '@fortawesome/free-solid-svg-icons'
import { faUserPlus } from '@fortawesome/free-solid-svg-icons'
import { faHeart } from '@fortawesome/free-solid-svg-icons'
import { faHeartBroken } from '@fortawesome/free-solid-svg-icons'
import { faNewspaper } from '@fortawesome/free-regular-svg-icons'
import { faIdCard } from '@fortawesome/free-regular-svg-icons'
import {faBan} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import {faList} from '@fortawesome/free-solid-svg-icons'
import {faTh} from '@fortawesome/free-solid-svg-icons'
import {faSmileBeam} from '@fortawesome/free-solid-svg-icons'
import {faSignOutAlt} from '@fortawesome/free-solid-svg-icons'

//Add icons to the app so you can use them in code
library.add(faUserSecret)
library.add(faNewspaper)
library.add(faRss)
library.add(faIdCard)
library.add(faSearch)
library.add(faSignInAlt)
library.add(faUserPlus)
library.add(faHeart)
library.add(faHeartBroken)
library.add(faBookReader)
library.add(faBan)
library.add(faList)
library.add(faTh)
library.add(faSmileBeam)
library.add(faSignOutAlt)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.use(PaperDashboard);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
