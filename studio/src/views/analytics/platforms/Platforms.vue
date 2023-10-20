<template>
  <b-row class="match-height">
    <b-col cols="12">
      <platforms-soundcloud />
    </b-col>
    <b-col cols="12">
      <platforms-spotify />
    </b-col>
    <b-col cols="12">
      <platforms-youtube />
    </b-col>
    <b-col cols="12">
        <platforms-apple />
    </b-col>
  </b-row>
</template>
    
    <script>
import { BRow, BCol, BImg } from "bootstrap-vue";
import PlatformsSoundcloud from "./soundcloud/PlatformsSoundcloud.vue";
import PlatformsSpotify from "./spotify/PlatformsSpotify.vue";
import PlatformsYoutube from "./youtube/PlatformsYoutube.vue";
import PlatformsApple from "./apple/PlatformsApple.vue";

export default {
  components: {
    PlatformsSoundcloud,
    PlatformsSpotify,
    PlatformsYoutube,
    PlatformsApple,
    BRow,
    BCol,
    BImg,
  },
  data() {
    return {};
  },
  computed: {},
  created() {},
};
</script>
  