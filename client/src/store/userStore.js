import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import { useToast } from "vue-toast-notification";

const toast = useToast();
const API_URL = "http://localhost:8000/user"; // Общий URL бэкенда для авторизации и регистрации

export const useUserStore = defineStore("userStore", {
  state: () => ({
    user: useStorage("user", null), // сохраняем информацию о пользователе
    accessToken: useStorage("accessToken", null), // сохраняем токен доступа
    isAuthenticated: useStorage("isAuthenticated", false), // флаг авторизации
    isLoading: false, // флаг загрузки
  }),

  getters: {
    // Геттер для получения информации о пользователе
    getUser(state) {
      return state.user;
    },

    // Геттер для получения статуса авторизации
    isUserAuthenticated(state) {
      return state.isAuthenticated;
    },

    // Геттер для получения токена доступа
    getAccessToken(state) {
      return state.accessToken;
    },

    // Дополнительный геттер для получения имени пользователя
    getUsername(state) {
      return state.user ? state.user.username : null; // Возвращаем имя пользователя или null, если пользователь не авторизован
    },
  },

  actions: {
    // Функция для отправки запросов к API
    async apiRequest(endpoint, credentials) {
      const { username, password } = credentials;

      // Выводим данные в консоль перед отправкой
      console.log(`Отправка данных для ${endpoint}:`, { username, password });

      // Формируем URL с параметрами
      const params = new URLSearchParams({
        username,
        password,
      }).toString();

      const response = await fetch(`${API_URL}/${endpoint}?${params}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `Ошибка при ${endpoint}`);
      }

      return await response.json();
    },

    // Функция для авторизации
    async loginUser(credentials) {
      this.isLoading = true;
      try {
        const userData = await this.apiRequest("login", credentials);

        // Сохраняем данные пользователя и токен
        this.user = userData.user; // сохраняем данные пользователя
        this.accessToken = userData.access_token; // сохраняем токен доступа
        this.isAuthenticated = true; // отмечаем, что пользователь авторизован
        toast.success("Авторизация успешна!");
      } catch (error) {
        toast.error(error.message || "Ошибка при авторизации");
        throw error; // пробрасываем ошибку дальше для обработки в компоненте
      } finally {
        this.isLoading = false;
      }
    },

    // Функция для регистрации
    async registerUser(credentials) {
      this.isLoading = true;
      try {
        const userData = await this.apiRequest("register", credentials);
        this.user = userData.user; // сохраняем данные пользователя
        this.accessToken = userData.access_token; // сохраняем токен доступа
        this.isAuthenticated = true; // отмечаем, что пользователь авторизован
        toast.success("Регистрация успешна!");
      } catch (error) {
        toast.error(error.message || "Ошибка при регистрации");
        throw error; // пробрасываем ошибку дальше для обработки в компоненте
      } finally {
        this.isLoading = false;
      }
    },

    // Функция для выхода пользователя
    logoutUser() {
      this.user = null;
      this.accessToken = null; // очищаем токен доступа
      this.isAuthenticated = false;
      useStorage("user", null); // очищаем хранилище
      useStorage("accessToken", null); // очищаем токен в хранилище
      toast.success("Вы успешно вышли из системы!");
    },
  },
});
