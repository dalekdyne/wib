<template>
  <b-row class="match-height">
    <b-col cols="12">
      <overview-performance />
    </b-col>
    <b-col xl="6" lg="6" md="6" sm="12">
      <overview-chart
        icon="UserCheckIcon"
        color="success"
        statistic="659.8k"
        statistic-title="Podcast Listeners"
        :chart-data="podcastListeners.series"
      />
    </b-col>
    <b-col xl="6" lg="6" md="6" sm="12">
      <overview-chart
        icon="ActivityIcon"
        color="info"
        statistic="659.8k"
        statistic-title="Podcast Streams"
        :chart-data="podcastStreams.series"
      />
    </b-col>
    <b-col cols="12">
      <overview-leaderboard />
    </b-col>
  </b-row>
</template>
  
  <script>
import { BRow, BCol } from "bootstrap-vue";
import OverviewPerformance from "./OverviewPerformance.vue";
import OverviewChart from "./OverviewChart.vue";
import OverviewLeaderboard from "./OverviewLeaderboard.vue";

export default {
  components: {
    OverviewPerformance,
    OverviewChart,
    OverviewLeaderboard,
    BRow,
    BCol,
  },
  data() {
    return {
      podcastStreams: {},
      podcastListeners: {},
    };
  },
  computed: {},
  created() {
    // Active Users
    this.$http.get("/card/card-statistics/active-users").then((response) => {
      this.podcastListeners = response.data;
    });
    // Active Users
    this.$http.get("/card/card-statistics/active-users").then((response) => {
      this.podcastStreams = response.data;
    });
  },
};
</script>
