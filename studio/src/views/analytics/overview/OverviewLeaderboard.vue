<template>
  <b-card>
    <b-card-header>
      <!-- title and subtitle -->
      <div>
        <b-card-title class="font-weight-bolder">
          Episodes leaderboard
        </b-card-title>
      </div>
    </b-card-header>
    <!--/ title and subtitle -->
    <div class="paginationContainer">
      <b-table
        id="leaderboardTable"
        :per-page="perPage"
        :current-page="currentPage"
        class="leaderboardTable"
        responsive="xl"
        :fields="fields"
        :items="items"
        hover
        @row-clicked="previewEpisode($event)"
      >
        <template #cell(streams)="data">
          <vue-apex-charts
            class="streams-chart"
            :options="chartOptions"
            :series="data.value"
            type="bar"
            height="100%"
            width="100%"
          />
          <div class="streams-text">{{ data.value[0].data[0] }}</div>
        </template>
        <template #cell(index)="data">
          <b-badge pill variant="primary">{{ data.index + 1 }}</b-badge>
        </template>
      </b-table>
      <b-pagination
        class="paginationController"
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
      />
    </div>
  </b-card>
</template>
      
      <script>
import {
  BTable,
  BCard,
  BCardTitle,
  BCardHeader,
  BPagination,
  BButton,
  BBadge,
  BPopover,
} from "bootstrap-vue";
import { useUtils as useI18nUtils } from "@core/libs/i18n";
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    VueApexCharts,
    BPopover,
    BBadge,
    BButton,
    BPagination,
    BTable,
    BCard,
    BCardHeader,
    BCardTitle,
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "bar",
          height: 350,
          toolbar: {
            show: true,
            tools: {
              download: false,
            },
          },
        },
        plotOptions: {
          bar: {
            borderRadius: 1,
            horizontal: true,
          },
        },
        dataLabels: {
          enabled: false,
        },
        xaxis: {
          categories: [""],
        },
        yaxis: {
          max: 2000,
          // We need to make this dynamic
        },
      },
      perPage: 10,
      currentPage: 1,
      totalRows: 10,
      fields: [
        { key: "index", label: "Place", sortable: true },
        { key: "name", label: "Name" },
        { key: "streams", label: "Streams" },
      ],
      items: [
        {
          id: 1,
          index: 1,
          name: "Episode 1",
          streams: [{ data: [534] }],
        },
        {
          id: 2,
          index: 2,
          name: "Episode 2",
          streams: [{ data: [156] }],
        },
        {
          id: 3,
          index: 3,
          name: "Episode 3",
          streams: [{ data: [1231] }],
        },
        {
          id: 4,
          index: 5,
          name: "Episode 3",
          streams: [{ data: [121] }],
        },
        {
          id: 5,
          index: 7,
          name: "Episode 3",
          streams: [{ data: [1241] }],
        },
        {
          id: 6,
          index: 4,
          name: "Episode 3",
          streams: [{ data: [1131] }],
        },
        {
          id: 7,
          index: 6,
          name: "Episode 3",
          streams: [{ data: [3123] }],
        },
        {
          id: 8,
          index: 8,
          name: "Episode 3",
          streams: [{ data: [1233] }],
        },
      ],
    };
  },
  setup() {
    const { t } = useI18nUtils();
    return {
      t,
    };
  },
  computed: {},
  methods: {
    previewEpisode(episode) {
      this.$router.push({
        name: "podcast-episodes-id",
        params: { id: episode.id },
      });
    },
  },
  filters: {},
};
</script>
      
      <style lang="scss">
.paginationContainer {
  display: flex;
  flex-direction: column;
}
.paginationController {
  margin-top: 1rem;
  margin-left: auto;
}
.leaderboardTable td:first-child {
  text-align: left;
}
.leaderboardTable th:first-child {
  text-align: left;
}
.leaderboardTable th:nth-child(3) {
  @media screen and (max-width: 768px) {
    text-align: left;
  }
  @media screen and (min-width: 768px) {
    text-align: center;
  }
}
.leaderboardTable th:nth-child(2) {
  text-align: left;
}
.streams-text {
  @media screen and (min-width: 768px) {
    display: none;
  }
}
.streams-chart {
  @media screen and (max-width: 768px) {
    display: none;
  }
}
</style>
      