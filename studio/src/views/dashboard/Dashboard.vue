<template>
  <section id="dashboard-analytics">
    <b-row class="match-height">
      <b-col lg="6" md="12">
        <dashboard-congratulation :data="data.congratulations" />
      </b-col>
      <b-col lg="3" sm="6">
        <statistic-card-with-area-chart
          v-if="data.subscribersGained"
          icon="HeadphonesIcon"
          :statistic="
            kFormatter(data.subscribersGained.analyticsData.subscribers)
          "
          :statistic-title="$t('Total Streams')"
          :chart-data="data.subscribersGained.series"
        />
      </b-col>
      <b-col lg="3" sm="6">
        <statistic-card-with-area-chart
          v-if="data.ordersRecevied"
          icon="UsersIcon"
          color="warning"
          :statistic="kFormatter(data.ordersRecevied.analyticsData.orders)"
          :statistic-title="$t('Total Listeners')"
          :chart-data="data.ordersRecevied.series"
        />
      </b-col>
    </b-row>

    <b-row class="match-height">
      <b-col lg="4">
        <dashboard-timeline :data="data.timeline" />
      </b-col>
      <b-col lg="8">
        <dashboard-twitter-feed :data="data.twitterFeeds" />
      </b-col>
    </b-row>
  </section>
</template>

<script>
import { BRow, BCol } from "bootstrap-vue";

import StatisticCardWithAreaChart from "@core/components/statistics-cards/StatisticCardWithAreaChart.vue";
import { kFormatter } from "@core/utils/filter";
import DashboardCongratulation from "./DashboardCongratulation.vue";
import DashboardTimeline from "./DashboardTimeline.vue";
import DashboardTwitterFeed from "./DashboardTwitterFeed.vue";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BRow,
    BCol,
    StatisticCardWithAreaChart,
    DashboardCongratulation,
    DashboardTimeline,
    DashboardTwitterFeed,
  },
  data() {
    return {
      data: {},
    };
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  created() {
    // data
    this.$http.get("/analytics/data").then((response) => {
      this.data = response.data;
    });
  },
  methods: {
    kFormatter,
  },
};
</script>
