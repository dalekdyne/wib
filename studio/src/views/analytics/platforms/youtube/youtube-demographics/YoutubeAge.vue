<template>
    <b-card no-body>
      <b-card-header>
        <b-card-title>Age</b-card-title>
        <!-- datepicker -->
        <div class="d-flex align-items-center">
          <feather-icon icon="CalendarIcon" size="16" />
          <flat-pickr
            v-model="rangePicker"
            :config="{ mode: 'range' }"
            class="form-control flat-picker bg-transparent border-0 shadow-none"
            placeholder="YYYY-MM-DD"
          />
        </div>
        <!-- datepicker -->
      </b-card-header>
  
      <!-- chart -->
      <b-card-body>
        <chartjs-component-bar-chart
          :height="400"
          :data="latestBarChart.data"
          :options="latestBarChart.options"
        />
      </b-card-body>
    </b-card>
  </template>
      
      <script>
  import { BCard, BCardHeader, BCardBody, BCardTitle } from "bootstrap-vue";
  import flatPickr from "vue-flatpickr-component";
  import ChartjsComponentBarChart from "../charts-components/ChartjsComponentBarChart.vue";
  import { $themeColors } from "@themeConfig";
  
  const chartColors = {
    primaryColorShade: "#836AF9",
    yellowColor: "#ffe800",
    successColorShade: "#28dac6",
    warningColorShade: "#ffe802",
    warningLightColor: "#FDAC34",
    infoColorShade: "#299AFF",
    greyColor: "#4F5D70",
    blueColor: "#2c9aff",
    blueLightColor: "#84D0FF",
    greyLightColor: "#EDF1F4",
    tooltipShadow: "rgba(0, 0, 0, 0.25)",
    lineChartPrimary: "#666ee8",
    lineChartDanger: "#ff4961",
    labelColor: "#6e6b7b",
    grid_line_color: "rgba(200, 200, 200, 0.2)",
  };
  
  export default {
    components: {
      BCard,
      BCardHeader,
      BCardBody,
      BCardTitle,
      flatPickr,
      ChartjsComponentBarChart,
    },
    data() {
      return {
        latestBarChart: {
          data: {
            labels: [
              "7/12",
              "8/12",
              "9/12",
              "10/12",
              "11/12",
              "12/12",
              "13/12",
              "14/12",
              "15/12",
              "16/12",
              "17/12",
            ],
            datasets: [
              {
                data: [
                  275, 90, 190, 205, 125, 85, 55, 87, 127, 150, 230, 280, 190,
                ],
                backgroundColor: chartColors.successColorShade,
                borderColor: "transparent",
              },
            ],
          },
          options: {
            elements: {
              rectangle: {
                borderWidth: 2,
                borderSkipped: "bottom",
              },
            },
            responsive: true,
            maintainAspectRatio: false,
            responsiveAnimationDuration: 500,
            legend: {
              display: false,
            },
            tooltips: {
              // Updated default tooltip UI
              shadowOffsetX: 1,
              shadowOffsetY: 1,
              shadowBlur: 8,
              shadowColor: chartColors.tooltipShadow,
              backgroundColor: $themeColors.light,
              titleFontColor: $themeColors.dark,
              bodyFontColor: $themeColors.dark,
            },
            scales: {
              xAxes: [
                {
                  display: true,
                  gridLines: {
                    display: true,
                    color: chartColors.grid_line_color,
                    zeroLineColor: chartColors.grid_line_color,
                  },
                  scaleLabel: {
                    display: false,
                  },
                  ticks: {
                    fontColor: chartColors.labelColor,
                  },
                },
              ],
              yAxes: [
                {
                  display: true,
                  gridLines: {
                    color: chartColors.grid_line_color,
                    zeroLineColor: chartColors.grid_line_color,
                  },
                  ticks: {
                    stepSize: 100,
                    min: 0,
                    max: 400,
                    fontColor: chartColors.labelColor,
                  },
                },
              ],
            },
          },
        },
        rangePicker: ["2019-05-01", "2019-05-10"],
      };
    },
  };
  </script>
      
      <style lang="scss">
  @import "@core/scss/vue/libs/vue-flatpicker.scss";
  </style>
      