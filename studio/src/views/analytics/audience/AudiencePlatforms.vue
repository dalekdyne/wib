<template>
  <b-card>
    <b-card-title class="mb-1"> Platforms </b-card-title>
    <b-card-sub-title class="mb-2">
      What device your audience is listening on
    </b-card-sub-title>

    <vue-apex-charts
      type="donut"
      height="350"
      :options="donutChart.chartOptions"
      :series="donutChart.series"
    />
  </b-card>
</template>
  
  <script>
import { BCard, BCardTitle, BCardSubTitle } from "bootstrap-vue";
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    VueApexCharts,
    BCard,
    BCardTitle,
    BCardSubTitle,
  },
  data() {
    return {
      donutChart: {
        series: [85, 16, 50, 50],
        chartOptions: {
          legend: {
            show: true,
            position: "bottom",
            fontSize: "14px",
            fontFamily: "Montserrat",
          },
          colors: ["#ffe700", "#00d4bd", "#826bf8", "#2b9bf4", "#FFA1A1"],
          dataLabels: {
            enabled: true,
            formatter(val) {
              // eslint-disable-next-line radix
              return `${parseInt(val)}%`;
            },
          },
          plotOptions: {
            pie: {
              donut: {
                labels: {
                  show: true,
                  name: {
                    fontSize: "2rem",
                    fontFamily: "Montserrat",
                  },
                  value: {
                    fontSize: "1rem",
                    fontFamily: "Montserrat",
                    formatter(val) {
                      // eslint-disable-next-line radix
                      return `${parseInt(val)}%`;
                    },
                  },
                },
              },
            },
          },
          labels: ["Windows", "Android", "MacOS", "iOS"],
          responsive: [
            {
              breakpoint: 992,
              options: {
                chart: {
                  height: 380,
                },
                legend: {
                  position: "bottom",
                },
              },
            },
            {
              breakpoint: 576,
              options: {
                chart: {
                  height: 320,
                },
                plotOptions: {
                  pie: {
                    donut: {
                      labels: {
                        show: true,
                        name: {
                          fontSize: "1.5rem",
                        },
                        value: {
                          fontSize: "1rem",
                        },
                        total: {
                          fontSize: "1.5rem",
                        },
                      },
                    },
                  },
                },
                legend: {
                  show: true,
                },
              },
            },
          ],
        },
      },
    };
  },
};
</script>
  