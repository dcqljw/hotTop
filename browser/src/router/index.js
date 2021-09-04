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
    },
    {
        path: "/test",
        name: "Test",
        component: () => import("@/views/test.vue")
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
