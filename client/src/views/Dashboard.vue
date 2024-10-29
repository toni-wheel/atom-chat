<template>
  <div class="dashboard">
    <div class="sidebar">
      <Chat />
    </div>
    <div class="admin">
      <div class="header">
        <h1>Добро пожаловать, {{ userStore.getUsername }}!</h1>
        <button @click="logoutUser" class="logout-button">Выйти</button>
      </div>

      <div v-if="userStore.getUser.is_moderator" class="user-list">
        <h2>Список пользователей</h2>
        <table>
          <thead>
            <tr>
              <th>Имя пользователя</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td :class="{ blocked: !user.is_active }">{{ user.username }}</td>
              <td>
                <button @click="blockUser(user)" :disabled="!user.is_active">
                  {{ !user.is_active ? "Заблокирован" : "Заблокировать" }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import Chat from "./Chat.vue";
import { useUserStore } from "../store/userStore.js";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const userStore = useUserStore();
const users = ref([]);
const router = useRouter();

// Загружаем пользователей при монтировании компонента
onMounted(async () => {
  await userStore.fetchUsers();
  users.value = userStore.users;
});

// Функция блокировки пользователя
const blockUser = async (user) => {
  try {
    await userStore.blockUser(user.id, userStore.accessToken);
    user.isBlocked = true;
  } catch (error) {
    console.error("Ошибка при блокировке пользователя:", error.message);
  }
};

// Функция выхода из системы
const logoutUser = async () => {
  userStore.logoutUser();
  await router.push("/"); // Перенаправляем на страницу входа после выхода
};
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

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.admin h1 {
  margin: 0;
}

.logout-button {
  padding: 6px 12px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.logout-button:hover {
  background-color: #c82333;
}

.user-list {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: left;
}

button {
  padding: 6px 12px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:disabled {
  background-color: #bbb;
  cursor: not-allowed;
}

button:hover:not(:disabled) {
  background-color: #0056b3;
}

.blocked {
  color: #888;
  text-decoration: line-through;
}
</style>
