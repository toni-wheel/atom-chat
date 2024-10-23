<template>
  <section class="auth">
    <div class="auth-container">
      <div class="auth-header">
        <img :src="logo" alt="Logo" class="logo" />

        <div class="header-buttons">
          <router-link to="/" class="auth-btn" :class="{ active: isLogin }"
            >Войти</router-link
          >
          <router-link
            to="/register"
            class="auth-btn"
            :class="{ active: !isLogin }"
            >Регистрация</router-link
          >
        </div>
      </div>

      <div class="auth-form">
        <h2>{{ title }}</h2>
        <p>{{ subtitle }}</p>

        <form @submit.prevent="handleSubmit">
          <!-- Поле для имени пользователя, отображается всегда -->
          <div class="form-group">
            <input
              type="text"
              v-model="username"
              placeholder="Имя пользователя"
              required
            />
          </div>

          <!-- Поле для пароля отображается всегда -->
          <div class="form-group">
            <input
              type="password"
              v-model="password"
              placeholder="Пароль"
              required
            />
          </div>

          <!-- Если это регистрация, показываем поле для подтверждения пароля -->
          <div v-if="!isLogin" class="form-group">
            <input
              type="password"
              v-model="confirmPassword"
              placeholder="Подтвердите пароль"
              required
            />
          </div>

          <button type="submit" class="submit-btn">{{ buttonText }}</button>
        </form>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const props = defineProps({
  title: String,
  subtitle: String,
  buttonText: String,
  isLogin: Boolean,
  logo: String,
  onSubmit: Function,
});

const username = ref("");
const password = ref("");
const confirmPassword = ref("");

// Обработка отправки формы
const handleSubmit = () => {
  // Проверка совпадения паролей при регистрации
  if (!props.isLogin && password.value !== confirmPassword.value) {
    alert("Пароли не совпадают!");
    return;
  }

  // Для регистрации отправляем имя пользователя и пароль
  if (!props.isLogin) {
    props.onSubmit({
      username: username.value,
      password: password.value,
    });
  }
  // Для входа отправляем имя пользователя и пароль
  else {
    props.onSubmit({ username: username.value, password: password.value });
  }
};
</script>

<style lang="scss" scoped>
.auth {
  display: flex;
  align-items: center;
  height: 100%;
}
.auth-container {
  width: 100%;
  max-width: 600px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  margin: 0 auto;
}

.auth-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 30px;

  .logo {
    width: 60px;
  }

  .header-buttons {
    display: flex;
    gap: 10px;
  }
}

.auth-btn {
  background-color: transparent;
  border: 1px solid #007bff;
  color: #007bff;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;

  &.active {
    background-color: #007bff;
    color: white;
  }

  &:hover {
    background-color: #0056b3;
    color: white;
  }
}

.auth-form {
  width: 100%;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;

  h2 {
    margin-bottom: 10px;
    font-size: 24px;
    color: #333;
  }

  p {
    margin-bottom: 20px;
    color: #666;
  }

  .form-group {
    margin-bottom: 15px;

    input {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      text-align: center;
    }
  }

  .submit-btn {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    border: none;
    color: white;
    font-size: 16px;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;

    &:hover {
      background-color: #0056b3;
    }
  }
}
</style>
