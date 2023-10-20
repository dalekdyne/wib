<template>
  <div>
    <b-row>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-spotify-streams />
      </b-col>
      <b-col sm="12" md="12" xl="6" lg="6">
        <platforms-spotify-listeners />
      </b-col>
      <b-col>
        <platforms-spotify-demographics />
      </b-col>
    </b-row>
    <div class="spotify-logo-ctn">
      <div class="spotify-logo">
        <h5>
          analytics fetched from
          <b-img
            src="@/assets/images/svg/spotify.svg"
            style="width: 30px; height: 30px"
          />
          Spotify
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
import { BRow, BCol, BImg } from "bootstrap-vue";
import PlatformsSpotifyStreams from "./PlatformsSpotifyStreams.vue";
import PlatformsSpotifyListeners from "./PlatformsSpotifyListeners.vue";
import PlatformsSpotifyDemographics from "./PlatformsSpotifyDemographics.vue";

export default {
  components: {
    PlatformsSpotifyStreams,
    PlatformsSpotifyListeners,
    PlatformsSpotifyDemographics,
    BRow,
    BCol,
    BImg,
  },
};
</script>

<style>
.spotify-logo-ctn {
  display: flex;
  margin-top: -20px;
  margin-bottom: 20px;
}
.spotify-logo {
  margin-left: auto;
}
</style>