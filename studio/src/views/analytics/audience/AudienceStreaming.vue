<template>
  <b-card no-body>
    <b-card-header>
        <div>
        <b-card-title class="mb-1"> Streaming platforms </b-card-title>
        <b-card-sub-title
          >What steraming services your listeners prefer</b-card-sub-title
        >
      </div>
    </b-card-header>

    <!-- chart -->
    <b-card-body>
      <chartjs-component-polar-area-chart
        :height="350"
        :data="polarChart.data"
        :options="polarChart.options"
      />
    </b-card-body>
  </b-card>
</template>
  
  <script>
import {
  BCard,
  BCardTitle,
  BCardSubTitle,
  BCardBody,
  BCardHeader,
  BDropdown,
  BDropdownItem,
} from "bootstrap-vue";
import ChartjsComponentPolarAreaChart from "./charts-components/ChartjsComponentPolarAreaChart.vue";
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
    ChartjsComponentPolarAreaChart,
    BCard,
    BCardTitle,
    BCardSubTitle,
    BCardBody,
    BCardHeader,
    BDropdown,
    BDropdownItem,
  },
  data() {
    return {
      polarChart: {
        options: {
          responsive: true,
          maintainAspectRatio: false,
          responsiveAnimationDuration: 500,
          legend: {
            position: "right",
            labels: {
              usePointStyle: true,
              padding: 25,
              boxWidth: 10,
              fontColor: chartColors.labelColor,
            },
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
          scale: {
            scaleShowLine: true,
            scaleLineWidth: 1,
            ticks: {
              display: false,
              fontColor: chartColors.labelColor,
            },
            reverse: false,
            gridLines: {
              display: false,
            },
          },
          animation: {
            animateRotate: false,
          },
        },
        data: {
          labels: [
            "Spotify",
            "YouTube",
            "Apple Podcasts",
            "Google Podcasts",
            "SoundCloud",
            "Other",
          ],
          datasets: [
            {
              label: "Population (millions)",
              backgroundColor: [
                chartColors.primaryColorShade,
                chartColors.warningColorShade,
                $themeColors.primary,
                chartColors.infoColorShade,
                chartColors.greyColor,
                chartColors.successColorShade,
              ],
              data: [19, 17.5, 15, 13.5, 11, 9],
              borderWidth: 0,
            },
          ],
        },
      },
    };
  },
};
</script>
  