import { defineStore } from "pinia";
import { useToast } from "vue-toast-notification";
import { ref } from "vue";
import { useStorage } from "@vueuse/core"; // Импортируем useStorage

const toast = useToast();
let API_URL = "http://localhost:8000"; // URL для работы с API каналов

export const useChannelStore = defineStore("channelStore", () => {
  const channels = useStorage("channels", []); // Список каналов
  const isLoading = ref(false); // Флаг загрузки

  // Универсальная функция для выполнения запросов к API
  const apiRequest = async (endpoint, method = "GET", body = null) => {
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
      throw new Error(errorData.detail || "Ошибка при запросе к API каналов");
    }

    return await response.json();
  };

  // Получение всех каналов с поддержкой пагинации
  const fetchChannels = async (
    limit = 5,
    offset = 0,
    token,
    isModerator,
    userId
  ) => {
    isLoading.value = true;
    try {
      let request = ``;
      if (isModerator) {
        request = `channels?limit=${limit}&offset=${offset}&token=${token}`;
      } else {
        request = `memberships/user/${userId}/channels?limit=${limit}&offset=${offset}`;
      }
      const channelsData = await apiRequest(request);
      channels.value = channelsData;
      return channelsData;
      toast.success("Каналы успешно загружены!");
    } catch (error) {
      toast.error(error.message || "Ошибка при загрузке каналов");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  // Получение канала по ID
  const fetchChannelById = async (channelId) => {
    isLoading.value = true;
    try {
      const channelData = await apiRequest(`${channelId}`);
      return channelData;
    } catch (error) {
      toast.error(error.message || "Ошибка при загрузке канала");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  // Создание нового канала
  const createChannel = async (channel) => {
    isLoading.value = true;
    try {
      const newChannel = await apiRequest("", "POST", channel);
      channels.value.push(newChannel);
      toast.success("Канал успешно создан!");
    } catch (error) {
      toast.error(error.message || "Ошибка при создании канала");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  // Обновление канала по ID
  const updateChannel = async (channelId, field) => {
    isLoading.value = true;
    try {
      const updatedChannel = await apiRequest(`${channelId}`, "PATCH", field);
      const index = channels.value.findIndex((ch) => ch.id === channelId);
      if (index !== -1) {
        channels.value[index] = updatedChannel;
      }
      toast.success("Канал успешно обновлен!");
    } catch (error) {
      toast.error(error.message || "Ошибка при обновлении канала");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  // Удаление канала по ID
  const deleteChannel = async (channelId) => {
    isLoading.value = true;
    try {
      await apiRequest(`${channelId}`, "DELETE");
      channels.value = channels.value.filter((ch) => ch.id !== channelId);
      toast.success("Канал успешно удален!");
    } catch (error) {
      toast.error(error.message || "Ошибка при удалении канала");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  // Удаление всех каналов
  const deleteAllChannels = async () => {
    isLoading.value = true;
    try {
      await apiRequest("", "DELETE");
      channels.value = [];
      toast.success("Все каналы успешно удалены!");
    } catch (error) {
      toast.error(error.message || "Ошибка при удалении всех каналов");
      throw error;
    } finally {
      isLoading.value = false;
    }
  };

  return {
    channels,
    isLoading,
    fetchChannels,
    fetchChannelById,
    createChannel,
    updateChannel,
    deleteChannel,
    deleteAllChannels,
  };
});
