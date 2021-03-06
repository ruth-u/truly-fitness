import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/home/HomePage.vue"),
  },
  {
    path: "/sing-up",
    name: "Form",
    component: () => import("@/pages/sing-up/SingUpPage.vue"),
  },

  {
    path: "/training_plan",
    name: "Plan",
    component: () => import("@/pages/training_plan/TrainingPlanPage.vue"),
  },
  {
    path: "/exercises/:id",
    name: "Detail",
    component: () => import("@/pages/exercise-detail/TrainingDetailPage.vue"),
  },
  {
    path: "/http://foo.com/bar.html#disqus_thread",
    name: "Info",
    component: () => import("@/pages/info/InfoPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
