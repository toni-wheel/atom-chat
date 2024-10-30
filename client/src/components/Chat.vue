<template>
  <div class="chat">
    <div class="channels">
      <span
        v-for="channel in channels"
        :key="channel.id"
        :class="{ active: channel.id === currentChannelId }"
        @click="selectChannel(channel.id)"
        class="channel"
      >
        {{ channel.name }}
      </span>
    </div>

    <div class="messages">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <span class="username"
          >{{ userStore.getUserById(message.user_id).username }}:</span
        >
        <span class="text">{{ message.content }}</span>
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
import { useChannelStore } from "../store/channelStore.js"; // Подключаем хранилище каналов

const userStore = useUserStore();
const messageStore = useMessageStore();
const channelStore = useChannelStore();

const newMessage = ref("");
const channels = ref([]);
const messages = ref([]);
const currentChannelId = ref(1); // Изначально выбран первый канал

// Загружаем список каналов
const loadChannels = async () => {
  try {
    channels.value = await channelStore.fetchChannels(
      10,
      0,
      userStore.getAccessToken,
      userStore.user.is_moderator,
      userStore.user.id
    );
  } catch (error) {
    console.error("Ошибка загрузки каналов:", error);
  }
};

// Загружаем сообщения для выбранного канала
const loadMessages = async () => {
  try {
    messages.value = await messageStore.getMessagesByChannel(
      currentChannelId.value
    );
  } catch (error) {
    console.error("Ошибка загрузки сообщений:", error);
  }
};

// Вызываем при монтировании компонента
onMounted(async () => {
  await loadChannels();
  await loadMessages();
  console.log(userStore.getUserById(1));
});

// Обработчик выбора канала
const selectChannel = async (channelId) => {
  currentChannelId.value = channelId;
  await loadMessages();
};

// Отправка сообщения
const sendMessage = async () => {
  if (newMessage.value.trim() !== "") {
    try {
      await messageStore.createMessage({
        channel_id: currentChannelId.value,
        user_id: userStore.getUser.id,
        content: newMessage.value,
      });
      await loadMessages(); // Обновляем список сообщений после отправки нового
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

.channels {
  display: flex;
  gap: 8px;
  padding: 8px;
  background-color: #e0e0e0;
  border-bottom: 1px solid #ccc;
}

.channel {
  padding: 8px 12px;
  cursor: pointer;
  color: #007bff;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.channel.active {
  background-color: #007bff;
  color: white;
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
