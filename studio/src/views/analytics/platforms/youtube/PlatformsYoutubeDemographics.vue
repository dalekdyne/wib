<template>
  <b-row>
    <b-col sm="12" md="12" xl="6" lg="6">
      <youtube-age />
    </b-col>
    <b-col sm="12" md="12" xl="6" lg="6">
      <youtube-gender />
    </b-col>
  </b-row>
</template>
  
  <script>
import { BRow, BCol } from "bootstrap-vue";

import YoutubeAge from "./youtube-demographics/YoutubeAge.vue";
import YoutubeGender from "./youtube-demographics/YoutubeGender.vue";

export default {
  components: {
    BRow,
    BCol,
    YoutubeAge,
    YoutubeGender,
  },
};
</script>
