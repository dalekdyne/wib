<template>
  <b-row class="match-height">
    <b-col sm="12" md="12" xl="6" lg="6">
      <audience-geographic />
    </b-col>
    <b-col sm="12" md="12" xl="6" lg="6">
      <audience-platforms />
    </b-col>
    <b-col cols="12">
      <audience-devices />
    </b-col>
    <b-col cols="12">
      <audience-streaming />
    </b-col>
  </b-row>
</template>
  
  <script>
import { BRow, BCol } from "bootstrap-vue";

import AudienceDevices from "./AudienceDevices.vue";
import AudienceGeographic from "./AudienceGeographic.vue";
import AudiencePlatforms from "./AudiencePlatforms.vue";
import AudienceStreaming from "./AudienceStreaming.vue";

export default {
  components: {
    AudienceDevices,
    AudienceGeographic,
    AudiencePlatforms,
    AudienceStreaming,
    BRow,
    BCol,
  },
  data() {
    return {};
  },
  computed: {},
};
</script>
  
  <style lang="scss">
@import "@core/scss/vue/libs/chart-apex.scss";
</style>
  