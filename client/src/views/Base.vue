<template>
  <Navbar></Navbar>
  <Header></Header>
  <Main>
    <slot></slot>
  </Main>
  <Footer></Footer>
</template>

<script setup>
import Navbar from "../components/Navbar.vue";
import Header from "../components/Header.vue";
import Main from "../components/Main.vue";
import Footer from "../components/Footer.vue";
</script>

<style scoped lang="scss"></style>
