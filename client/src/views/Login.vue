<template>
  <AuthForm
    title="Добро пожаловать!"
    subtitle="Введите имя пользователя и пароль для входа"
    buttonText="Войти"
    :isLogin="true"
    :logo="atomLogo"
    :onSubmit="onLogin"
  />
</template>

<script setup>
import { ref } from "vue";

import AuthForm from "./AuthForm.vue";
import atomLogo from "../images/atom-logo.png";

import { useUserStore } from "../store/userStore.js";

import router from "../router/index.js";

const userStore = useUserStore(); // Создаем экземпляр стора

const errorMessage = ref(""); // Определяем переменную errorMessage

const onLogin = async (data) => {
  console.log("Данные при входе:", data.username, data.password);

  try {
    await userStore.loginUser({
      username: data.username,
      password: data.password,
    });
    router.push("/dashboard"); // перенаправление после успешного входа
  } catch (error) {
    errorMessage.value = error.message;
  }
};
</script>
