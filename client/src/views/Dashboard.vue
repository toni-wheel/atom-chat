<template>
  <div class="dashboard">
    <div class="sidebar">
      <Chat />
    </div>
    <div class="admin">
      <h1>Добро пожаловать, {{ userStore.getUser.username }}!</h1>
    </div>
  </div>
</template>

<script setup>
import Chat from "./Chat.vue";
import { useUserStore } from "../store/userStore.js";
const userStore = useUserStore();
</script>

<style lang="scss" scoped>
.dashboard {
  display: flex;
  height: 100vh;
}

.sidebar {
  flex: 1;
  border-right: 1px solid #ccc;
  padding: 16px;
}

.admin {
  flex: 2;
  padding: 16px;
}

.admin h1 {
  margin: 0; /* Убираем отступы для заголовка */
}
</style>
