import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router/index.js";
import ToastPlugin from "vue-toast-notification";

import "vue-toast-notification/dist/theme-bootstrap.css";

import App from "./App.vue";

import "./styles/reset.scss";
import "./styles/font.scss";
import "./styles/base.scss";

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(ToastPlugin, {
  // Можно указать глобальные параметры здесь
  position: "bottom-right",
  duration: 3000,
});

app.mount("#app");
