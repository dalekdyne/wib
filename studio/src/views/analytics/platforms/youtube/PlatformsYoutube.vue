<template>
    <div>
      <b-row>
        <b-col sm="12" md="12" xl="6" lg="6">
          <platforms-youtube-views />
        </b-col>
        <b-col sm="12" md="12" xl="6" lg="6">
          <platforms-youtube-subscribers />
        </b-col>
        <b-col>
          <platforms-youtube-demographics />
        </b-col>
      </b-row>
      <div class="youtube-logo-ctn">
        <div class="youtube-logo">
          <h5>
            analytics fetched from
            <b-img
              src="@/assets/images/svg/youtube.svg"
              style="width: 30px; height: 20px"
            />
            YouTube
          </h5>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { BRow, BCol, BImg } from "bootstrap-vue";
  import PlatformsYoutubeViews from "./PlatformsYoutubeViews.vue";
  import PlatformsYoutubeSubscribers from "./PlatformsYoutubeSubscribers.vue";
  import PlatformsYoutubeDemographics from "./PlatformsYoutubeDemographics.vue";
  
  export default {
    components: {
      PlatformsYoutubeViews,
      PlatformsYoutubeSubscribers,
      PlatformsYoutubeDemographics,
      BRow,
      BCol,
      BImg,
    },
  };
  </script>
  
  <style>
  .youtube-logo-ctn {
    display: flex;
    margin-top: -20px;
    margin-bottom: 20px;
  }
  .youtube-logo {
    margin-left: auto;
  }
  </style>