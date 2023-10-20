<template>
  <b-form>
    <b-row>
      <div class="overview-card-button mb-2 mr-1 desktop-btn">
        <b-button
          variant="outline-primary"
          class="mr-2"
          @click="editMedia(episode.id)"
          >{{ t("Unpublish") }}</b-button
        >
        <b-button variant="primary" @click="editMedia(episode.id)">{{
          t("Update episode")
        }}</b-button>
      </div>

      <b-col cols="12">
        <episode-edit-overview :episode="episode" />
      </b-col>
      <b-col cols="12">
        <episode-edit-advanced :episode="episode" />
      </b-col>
      <b-col cols="12">
        <episode-edit-media :episode="episode" />
      </b-col>
    </b-row>
    <div class="mobile-btn-ctn">
      <div class="overview-card-button mb-2 ml-auto mobile-btn">
        <b-button
          variant="outline-primary"
          class="mr-2"
          @click="editMedia(episode.id)"
          >{{ t("Unpublish") }}</b-button
        >
        <b-button variant="primary" @click="editMedia(episode.id)">{{
          t("Update episode")
        }}</b-button>
      </div>
    </div>
  </b-form>
</template>

<script>
import EpisodeEditAdvanced from "./EpisodeEditAdvanced.vue";
import EpisodeEditOverview from "./EpisodeEditOverview.vue";
import EpisodeEditMedia from "./EpisodeEditMedia.vue";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

import { BCol, BRow, BButton, BForm } from "bootstrap-vue";
export default {
  components: {
    EpisodeEditAdvanced,
    EpisodeEditOverview,
    EpisodeEditMedia,
    BCol,
    BRow,
    BButton,
    BForm,
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
        status: "Published",
      },
    };
  },
  setup() {
    const { t } = useI18nUtils();
    return {
      t,
    };
  },
};
</script>
<style lang="scss">
.overview-card-title {
  display: flex;
}
.overview-card-button {
  margin-left: auto;
}
.mobile-btn-ctn {
  display: flex;
}
@media screen and (min-width: 768px) {
  .mobile-btn {
    display: none;
  }
  .desktop-btn {
    display: block;
  }
}
@media screen and (max-width: 768px) {
  .mobile-btn {
    display: block;
  }
  .desktop-btn {
    display: none;
  }
}
</style>
