<template>
  <div class="dashboard">
    <div class="sidebar">
      <Chat />
    </div>
    <AdminPanel />
  </div>
</template>

<script setup>
import Chat from "../components/Chat.vue";
import AdminPanel from "../components/AdminPanel.vue";
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
</style>
