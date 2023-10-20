<template>
  <div>
    <b-row class="d-xl-none">
      <b-col>
        <episodes-cards :items="this.items" />
      </b-col>
    </b-row>
    <b-row class="d-none d-xl-block">
      <b-col>
        <episodes-table :items="this.items" />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import EpisodesTable from "../list/EpisodesTable.vue";
import EpisodesCards from "../list/EpisodesCards.vue";

import { BCol, BRow } from "bootstrap-vue";

export default {
  components: {
    EpisodesTable,
    EpisodesCards,
    BCol,
    BRow,
  },
  data() {
    return {
      items: [
        {
          id: 1,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/300/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 2,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 3,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 671,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 4,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 5,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 6,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Published",
        },
        {
          id: 7,
          name: "John is a very long name",
          description: "John is a very long name",
          coverArtUrl: "https://picsum.photos/200/300",
          length: 670,
          streams: 1000,
          date: "2019-01-01",
          type: "Video",
          status: "Draft",
        },
      ],
    };
  },
};
</script>