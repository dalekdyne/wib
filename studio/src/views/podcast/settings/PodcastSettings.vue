<template>
  <b-form>
    <b-row class="match-height">
      <div class="overview-card-button mb-2 mr-1 desktop-btn">
        <b-button
          variant="outline-primary"
          class="mr-2"
          @click="resetChanges()"
          >{{ t("Reset") }}</b-button
        >
        <b-button variant="primary" @click="savePodcastChanges(episode.id)">{{
          t("Save changes")
        }}</b-button>
      </div>
      <b-col cols="12">
        <podcast-settings-about />
      </b-col>
      <b-col cols="12">
        <podcast-settings-cover-art />
      </b-col>
      <b-col md="6" xl="6" sm="12" xs="12">
        <podcast-settings-details />
      </b-col>
      <b-col md="6" xl="6" sm="12" xs="12">
        <podcast-settings-advanced-options />
      </b-col>
    </b-row>
    <div class="mobile-btn-ctn">
    <div class="overview-card-button mb-2 ml-auto mobile-btn">
        <b-button
          variant="outline-primary"
          class="mr-2"
          @click="resetChanges()"
          >{{ t("Reset") }}</b-button
        >
        <b-button variant="primary" @click="savePodcastChanges(episode.id)">{{
          t("Save changes")
        }}</b-button>
      </div>
    </div>
  </b-form>
</template>
  
  <script>
/* eslint-disable global-require */

import { BRow, BCol, BForm, BButton } from "bootstrap-vue";

import PodcastSettingsAbout from "./PodcastSettingsAbout.vue";
import PodcastSettingsDetails from "./PodcastSettingsDetails.vue";
import PodcastSettingsCoverArt from "./PodcastSettingsCoverArt.vue";
import PodcastSettingsAdvancedOptions from "./PodcastSettingsAdvancedOptions.vue";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BForm,
    BRow,
    BCol,
    BButton,
    PodcastSettingsAbout,
    PodcastSettingsDetails,
    PodcastSettingsCoverArt,
    PodcastSettingsAdvancedOptions,
  },
  setup() {
    const { t } = useI18nUtils();
    return {
      t,
    };
  },
  methods: {
    resetChanges() {
      console.log("reset changes");
    },
    savePodcastChanges() {
      this.$store.dispatch("podcast/saveChanges");
    },
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
