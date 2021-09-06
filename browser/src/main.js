import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import axios from "axios";
import md5 from "js-md5"

const app = createApp(App)
installElementPlus(app)
app.use(router, axios, md5).mount("#app")