<template>
  <div>
    <b-row class="match-height">
      <b-col cols="12">
        <availability-overview />
      </b-col>
      <b-col xl="6" md="6" sm="12" xs="12">
        <availability-rss />
      </b-col>
      <b-col xl="6" md="6" sm="12" xs="12">
        <availability-faq />
      </b-col>
      <b-col cols="12">
        <availability-options />
      </b-col>
    </b-row>
  </div>
</template>
  
  <script>
import {
  BCol,
  BRow,
  BTable,
  BCard,
  BPagination,
  BButton,
  BBadge,
  BPopover,
} from "bootstrap-vue";

import AvailabilityOverview from "./AvailabilityOverview.vue";
import AvailabilityFaq from "./AvailabilityFaq.vue";
import AvailabilityOptions from "./AvailabilityOptions.vue";
import AvailabilityRss from "./AvailabilityRss.vue";

export default {
  components: {
    BCol,
    BRow,
    BTable,
    BCard,
    BPagination,
    BButton,
    BBadge,
    BPopover,
    AvailabilityOverview,
    AvailabilityFaq,
    AvailabilityOptions,
    AvailabilityRss,
  },
  data() {
    return {};
  },
  setup() {},
  computed: {},
};
</script>
  
  <style lang="scss">
</style>
  