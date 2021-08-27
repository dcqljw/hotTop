import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import installElementPlus from './plugins/element'
import axios from "axios";

const app = createApp(App)
installElementPlus(app)
app.use(router, axios).mount("#app")