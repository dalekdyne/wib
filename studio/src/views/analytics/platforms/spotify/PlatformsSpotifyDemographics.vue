<template>
  <b-row>
    <b-col sm="12" md="12" xl="6" lg="6">
      <spotify-age />
    </b-col>
    <b-col sm="12" md="12" xl="6" lg="6">
      <spotify-gender />
    </b-col>
  </b-row>
</template>

<script>
import { BRow, BCol } from "bootstrap-vue";

import SpotifyAge from "./spotify-demographics/SpotifyAge.vue";
import SpotifyGender from "./spotify-demographics/SpotifyGender.vue";

export default {
  components: {
    BRow,
    BCol,
    SpotifyAge,
    SpotifyGender,
  },
};
</script>

<style>
</style>