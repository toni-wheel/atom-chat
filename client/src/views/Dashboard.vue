<template>
  <div class="dashboard">
    <div class="sidebar">
      <Chat />
    </div>
    <div class="chat-list">
      <!-- Здесь может быть список чатов -->
      <ul>
        <li v-for="(chat, index) in chats" :key="index">
          {{ chat.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Chat from "./Chat.vue";

const chats = ref([{ name: "Чат 1" }, { name: "Чат 2" }, { name: "Чат 3" }]);
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

.chat-list {
  flex: 2;
  padding: 16px;
}
</style>
