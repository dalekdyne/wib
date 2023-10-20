<template>
  <div>
    <b-row>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-soundcloud-streams />
      </b-col>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-soundcloud-listeners />
      </b-col>
    </b-row>
    <div class="soundcloud-logo-ctn">
      <div class="soundcloud-logo">
        <h5>
          analytics fetched from
          <b-img
            src="@/assets/images/svg/soundcloud.svg"
            style="width: 30px; height: 30px"
          />
          Soundcloud
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
import { BRow, BCol, BImg } from "bootstrap-vue";
import PlatformsSoundcloudStreams from "./PlatformsSoundcloudStreams.vue";
import PlatformsSoundcloudListeners from "./PlatformsSoundcloudListeners.vue";

export default {
  components: {
    PlatformsSoundcloudStreams,
    PlatformsSoundcloudListeners,
    BRow,
    BCol,
    BImg,
  },
};
</script>

<style>
.soundcloud-logo-ctn {
  display: flex;
  margin-top: -20px;
  margin-bottom: 20px;
}
.soundcloud-logo {
  margin-left: auto;
}
</style>