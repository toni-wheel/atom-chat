import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import { useToast } from "vue-toast-notification";
import router from "../router/index.js";

const toast = useToast();

const API_URL = "http://localhost:8000/user";

export const useUserStore = defineStore("userStore", {
  state: () => ({
    user: JSON.parse(localStorage.getItem("user")) || null, // Получаем user из localStorage
    accessToken: useStorage("accessToken", null),
    isAuthenticated: useStorage("isAuthenticated", false),
    isLoading: false,
    users: useStorage("users", []), // Сохраняем состояние пользователей в localStorage
  }),

  getters: {
    getUser(state) {
      return state.user;
    },
    isUserAuthenticated(state) {
      return state.isAuthenticated;
    },
    getAccessToken(state) {
      return state.accessToken;
    },
    getUsername(state) {
      return state.user ? state.user.username : null;
    },
    getUsers(state) {
      return state.users;
    },
    // Новый геттер для поиска пользователя по ID
    getUserById: (state) => (user_id) => {
      return state.users.find((user) => user.id === user_id) || null;
    },
  },

  actions: {
    async apiRequest(endpoint, credentials = {}) {
      const { username, password } = credentials;

      console.log(`Отправка данных для ${endpoint}:`, { username, password });

      const params = new URLSearchParams({ username, password }).toString();

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

    async loginUser(credentials) {
      this.isLoading = true;
      try {
        const userData = await this.apiRequest("login", credentials);

        this.user = userData.user;
        this.accessToken = userData.access_token;
        this.isAuthenticated = true;
        localStorage.setItem("user", JSON.stringify(this.user)); // Сохраняем user в localStorage
        toast.success("Авторизация успешна!");

        // Перенаправляем пользователя на страницу dashboard
        router.push("/dashboard");
      } catch (error) {
        toast.error(error.message || "Ошибка при авторизации");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    async registerUser(credentials) {
      this.isLoading = true;
      try {
        const userData = await this.apiRequest("register", credentials);
        this.user = userData.user;
        this.accessToken = userData.access_token;
        this.isAuthenticated = true;
        localStorage.setItem("user", JSON.stringify(this.user)); // Сохраняем user в localStorage
        toast.success("Регистрация успешна!");
      } catch (error) {
        toast.error(error.message || "Ошибка при регистрации");
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    logoutUser() {
      this.user = null;
      this.accessToken = null;
      this.isAuthenticated = false;
      localStorage.removeItem("user"); // Удаляем user из localStorage
      localStorage.removeItem("accessToken"); // Удаляем accessToken из localStorage
      toast.success("Вы успешно вышли из системы!");
    },

    // Функция для получения всех пользователей
    async fetchUsers(limit = 10, offset = 0) {
      this.isLoading = true;
      try {
        const response = await fetch(
          `${API_URL}/?limit=${limit}&offset=${offset}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${this.accessToken}`, // передаем токен доступа
            },
          }
        );

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(
            errorData.detail || "Ошибка при получении списка пользователей"
          );
        }

        this.users = await response.json();
      } catch (error) {
        toast.error(
          error.message || "Ошибка при получении списка пользователей"
        );
        throw error;
      } finally {
        this.isLoading = false;
      }
    },

    // Функция для блокировки пользователя
    async blockUser(user_id, token) {
      try {
        const response = await fetch(
          `http://localhost:8000/user/block/${user_id}?token=${token}`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(
            errorData.detail || "Ошибка при блокировке пользователя"
          );
        }

        // Обновляем статус блокировки в локальном состоянии
        const userIndex = this.users.findIndex((user) => user.id === user_id);
        if (userIndex !== -1) {
          this.users[userIndex].isBlocked = true;
        }

        toast.success("Пользователь успешно заблокирован!");
      } catch (error) {
        toast.error(error.message || "Ошибка при блокировке пользователя");
        throw error;
      }
    },
  },
});
