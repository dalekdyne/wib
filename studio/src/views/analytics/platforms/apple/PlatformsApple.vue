<template>
  <div>
    <b-row>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-apple-streams />
      </b-col>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-apple-listeners />
      </b-col>
    </b-row>
    <div class="apple-logo-ctn">
      <div class="apple-logo">
        <h5>
          analytics fetched from
          <b-img
            src="@/assets/images/svg/apple.svg"
            style="width: 30px; height: 30px"
          />
          Apple Podcasts
        </h5>
      </div>
    </div>
  </div>
</template>
  
  <script>
import { BRow, BCol, BImg } from "bootstrap-vue";
import PlatformsAppleListeners from "./PlatformsAppleListeners.vue";
import PlatformsAppleStreams from "./PlatformsAppleStreams.vue";

export default {
  components: {
    PlatformsAppleListeners,
    PlatformsAppleStreams,
    BRow,
    BCol,
    BImg,
  },
};
</script>
  
  <style>
.apple-logo-ctn {
  display: flex;
  margin-top: -20px;
  margin-bottom: 20px;
}
.apple-logo {
  margin-left: auto;
}
</style>