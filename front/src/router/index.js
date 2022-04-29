import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/pages/home/HomePage.vue"),
  },
  {
    path: "/form",
    name: "Form",
    component: () => import("@/pages/form/FormPage.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
