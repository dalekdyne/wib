<template>
  <b-link to="/">
    <b-img style="width: 40px; height: 40px" :src="appLogoImage" alt="logo" />
  </b-link>
</template>

<script>
import { BLink, BImg } from "bootstrap-vue";
import { $themeConfig } from "@themeConfig";

export default {
  components: {
    BLink,
    BImg,
  },
  setup() {
    // App Name
    const { appLogoImage } = $themeConfig.app;
    return {
      appLogoImage,
    };
  },
};
</script>

<style>
</style>
