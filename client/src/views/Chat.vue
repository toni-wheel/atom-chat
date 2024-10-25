<template>
  <div class="chat">
    <div class="messages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <span class="username">{{ message.username }}:</span>
        <span class="text">{{ message.text }}</span>
      </div>
    </div>
    <div class="chat-input">
      <input
        v-model="newMessage"
        @keyup.enter="sendMessage"
        type="text"
        placeholder="Введите сообщение"
      />
      <button @click="sendMessage">Отправить</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const messages = ref([
  { username: "Пользователь 1", text: "Привет!" },
  { username: "Пользователь 2", text: "Привет, как дела?" },
]);

const newMessage = ref("");

const sendMessage = () => {
  if (newMessage.value.trim() !== "") {
    messages.value.push({ username: "Вы", text: newMessage.value });
    newMessage.value = "";
  }
};
</script>

<style lang="scss" scoped>
.chat {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  border-bottom: 1px solid #ccc;
}

.message {
  margin-bottom: 8px;
}

.username {
  font-weight: bold;
}

.chat-input {
  display: flex;
  padding: 16px;
  background-color: #f5f5f5;
}

input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-left: 8px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
