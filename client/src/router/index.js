import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Dashboard from "../views/Dashboard.vue";

import { useUserStore } from "../store/userStore.js";

const routes = [
  {
    path: "/",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  },
  {
    path: "/dashboard",
    component: Dashboard,
    meta: { requiresAuth: true }, // Маршрут, требующий авторизации
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// Проверка при загрузке страницы
router.beforeEach((to, from, next) => {
  const userStore = useUserStore();

  // Устанавливаем статус авторизации на основе токена в localStorage
  if (userStore.accessToken && !userStore.isAuthenticated) {
    userStore.isUserAuthenticated = true;
  }

  if (to.meta.requiresAuth && !userStore.isUserAuthenticated) {
    next("/"); // Перенаправляем на страницу входа, если пользователь не авторизован
  } else {
    next();
  }
});

export default router;
