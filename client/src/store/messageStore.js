import { defineStore } from "pinia";
import { useToast } from "vue-toast-notification";

const toast = useToast();
const API_URL = "http://localhost:8000/messages"; // URL для работы с API сообщений

export const useMessageStore = defineStore("messageStore", {
  state: () => ({
    messages: {}, // Словарь для хранения сообщений по channel_id
    isLoading: false, // флаг загрузки
  }),

  actions: {
    // Универсальная функция для выполнения запросов к API
    async apiRequest(endpoint, method = "GET", body = null) {
      const options = {
        method,
        headers: {
          "Content-Type": "application/json",
        },
        body: body ? JSON.stringify(body) : null,
      };

      const response = await fetch(`${API_URL}/${endpoint}`, options);

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(
          errorData.detail || "Ошибка при запросе к API сообщений"
        );
      }

      return await response.json();
    },

    // Получение сообщений из API по channel_id с поддержкой пагинации
    async fetchMessagesByChannel(channel_id, limit = 5, offset = 0) {
      this.isLoading = true;
      try {
        const messagesData = await this.apiRequest(
          `channel/${channel_id}?limit=${limit}&offset=${offset}`
        );
        this.messages[channel_id] = messagesData; // Обновляем сообщения для канала в локальном хранилище
        toast.success(`Сообщения для канала ${channel_id} успешно загружены!`);
        return messagesData; // Возвращаем свежие данные
      } catch (error) {
        toast.error(error.message || "Ошибка при загрузке сообщений");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Получение сообщений для конкретного канала
    async getMessagesByChannel(channel_id, limit = 5, offset = 0) {
      // Загружаем и возвращаем сообщения из API каждый раз при обращении к этому методу
      return await this.fetchMessagesByChannel(channel_id, limit, offset);
    },

    // Создание нового сообщения с учетом channel_id, user_id и content
    async createMessage({ channel_id, user_id, content }) {
      this.isLoading = true;
      try {
        // Формируем URL с параметрами для запроса
        const endpoint = `?content=${encodeURIComponent(
          content
        )}&channel_id=${channel_id}&user_id=${user_id}`;

        // Выполняем запрос с GET методом и пустым телом
        const createdMessage = await this.apiRequest(endpoint, "POST");

        // Проверка на существование массива сообщений для канала
        if (!this.messages[channel_id]) {
          this.messages[channel_id] = [];
        }

        // Добавляем новое сообщение в массив сообщений для указанного канала
        this.messages[channel_id].push(createdMessage);
        toast.success("Сообщение успешно создано!");
      } catch (error) {
        toast.error(error.message || "Ошибка при создании сообщения");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Обновление сообщения по его ID
    async updateMessage(messageId, updatedField, channel_id) {
      this.isLoading = true;
      try {
        const updatedMessage = await this.apiRequest(
          `${messageId}`,
          "PATCH",
          updatedField
        );
        const index = this.messages[channel_id]?.findIndex(
          (msg) => msg.id === messageId
        );
        if (index !== -1) {
          this.messages[channel_id][index] = updatedMessage;
        }
        toast.success("Сообщение успешно обновлено!");
      } catch (error) {
        toast.error(error.message || "Ошибка при обновлении сообщения");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Удаление сообщения по его ID
    async deleteMessage(messageId, channel_id) {
      this.isLoading = true;
      try {
        await this.apiRequest(`${messageId}`, "DELETE");
        this.messages[channel_id] = this.messages[channel_id].filter(
          (msg) => msg.id !== messageId
        );
        toast.success("Сообщение успешно удалено!");
      } catch (error) {
        toast.error(error.message || "Ошибка при удалении сообщения");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Удаление всех сообщений для указанного channel_id
    async deleteAllMessages(channel_id) {
      this.isLoading = true;
      try {
        await this.apiRequest(`channel/${channel_id}`, "DELETE");
        delete this.messages[channel_id];
        toast.success(
          `Все сообщения для канала ${channel_id} успешно удалены!`
        );
      } catch (error) {
        toast.error(error.message || "Ошибка при удалении всех сообщений");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },
  },
});
