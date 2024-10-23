import { createRouter, createMemoryHistory } from "vue-router";

import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

const routes = [
  {
    path: "/",
    component: Login,
  },
  {
    path: "/register",
    component: Register,
  },
];

const router = createRouter({
  history: createMemoryHistory(),
  routes,
});

export default router;
