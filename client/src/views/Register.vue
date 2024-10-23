<template>
  <AuthForm
    title="Создайте аккаунт"
    subtitle="Введите имя пользователя, почту и пароль для регистрации"
    buttonText="Зарегистрироваться"
    :isLogin="false"
    :logo="atomLogo"
    :onSubmit="onRegister"
  />
</template>

<script setup>
import AuthForm from "./AuthForm.vue";
import atomLogo from "../images/atom-logo.png";

// Получаем доступ к userStore
import { useUserStore } from "../store/userStore.js";
const userStore = useUserStore();

const onRegister = async (data) => {
  console.log("Данные при регистрации:", data.username, data.password);

  try {
    // Вызываем метод для регистрации
    await userStore.registerUser({
      username: data.username,
      password: data.password,
    });
  } catch (error) {
    console.error("Ошибка регистрации:", error.message);
    // Здесь можно обработать ошибку, например, показать уведомление
  }
};
</script>
