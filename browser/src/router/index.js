import {createRouter, createWebHashHistory} from 'vue-router'
import Index from '@/views/Index.vue'
import Hot from '@/views/Hot.vue'

const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index
    },
    {
        path: '/hot',
        name: 'Hot',
        component: Hot
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
