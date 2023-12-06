import {createRouter, createWebHistory} from 'vue-router'
import LandingView from "@/views/LandingView.vue";
import TutorialView from "@/views/TutorialView.vue";
import IntroductionView from "@/views/IntroductionView.vue";
import ExperimentView from "@/views/ExperimentView.vue";

const routes = [
    { path: '/', component: LandingView},
    { path: '/introduction', component: IntroductionView},
    { path: '/tutorial', component: TutorialView},
    { path: '/experiment', component: ExperimentView}

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;