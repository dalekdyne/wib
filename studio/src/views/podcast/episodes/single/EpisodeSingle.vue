<template>
    <div>
        <b-row>
            <b-col cols="12">
                <episode-single-overview :episode="episode" />
            </b-col>
            <b-col cols="12">
                <episode-single-analytics :episode="episode" />
            </b-col>
            <b-col cols="12">
                <episode-single-media :episode="episode" />
            </b-col>
        </b-row>
    </div>
  
</template>

<script>
import EpisodeSingleOverview from "./EpisodeSingleOverview.vue";
import EpisodeSingleAnalytics from "./EpisodeSingleAnalytics.vue";
import EpisodeSingleMedia from "./EpisodeSingleMedia.vue";

import { BCol, BRow } from "bootstrap-vue";

export default {
    components: {
        BCol,
        BRow,
        EpisodeSingleOverview,
        EpisodeSingleAnalytics,
        EpisodeSingleMedia,
    },
    data() {
          return {
              episode: {
                id: 1,
                title: "Episode 1",
                description: "This is the description of episode 1",
                length: 100,
                coverArtUrl: "https://picsum.photos/600/600",
                streams: 1000,
                date: "2019-01-01",
                type: "Video",
                status: "Published"
              }
          };
      },
}
</script>

<style>

</style>