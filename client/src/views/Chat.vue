<template>
  <div class="chat">
    <div class="messages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <span class="username">{{ message.user_id }}:</span>
        <span class="text">{{ message.content }}</span>
        <!-- Замените text на content, если используется это поле -->
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
import { ref, onMounted } from "vue";
import { useUserStore } from "../store/userStore.js";
import { useMessageStore } from "../store/messageStore.js";

const userStore = useUserStore();
const messageStore = useMessageStore();

const newMessage = ref("");

// Загружаем сообщения из первого канала при монтировании компонента
const messages = ref([]);
const loadMessages = async () => {
  try {
    messages.value = await messageStore.getMessagesByChannel(1); // Загружаем сообщения для channel_id 1
  } catch (error) {
    console.error("Ошибка загрузки сообщений:", error);
  }
};

onMounted(loadMessages);

const sendMessage = async () => {
  if (newMessage.value.trim() !== "") {
    try {
      await messageStore.createMessage({
        channel_id: 1,
        user_id: userStore.getUser.id, // Предполагается, что у пользователя есть id
        content: newMessage.value,
      });
      // Обновляем список сообщений после отправки нового
      await loadMessages();
      newMessage.value = "";
    } catch (error) {
      console.error("Ошибка отправки сообщения:", error);
    }
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
  margin-right: 5px;
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
