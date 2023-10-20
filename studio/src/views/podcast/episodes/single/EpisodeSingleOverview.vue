<template>
  <b-card>
    <b-row class="mb-n4">
      <b-col md="4" sm="4" lg="4" xl="2" class="coverArtUploadImg text-center">
        <b-img :src="this.episode.coverArtUrl" fluid rounded alt="Image" />
        <statistic-card-vertical
          icon="HeadphonesIcon"
          :statistic="this.episode.streams"
          statistic-title="Streams"
          color="info"
        />
      </b-col>
      <b-col md="8" sm="8" lg="8" xl="8">
        <div class="header">
          <h1 style="font-weight: 800">{{ episode.title }}</h1>
          <b-button
            class="editBtn"
            variant="outline-primary"
            size="sm"
            @click="editEpisode(episode)"
            ><feather-icon icon="EditIcon" />
          </b-button>
        </div>

        <span
          >{{ episode.date }} | {{ episode.length | secondsToMinutes }}:{{
            episode.length | leftSeconds
          }}</span
        >
        <br />
        <span>
          {{
            episode.status == "Published"
              ? t(
                  "This episode has been published and can be heard everywhere your podcast is available."
                )
              : t("This episode is a draft.")
          }}
        </span>
        <b-form-textarea
          debounce="500"
          rows="1"
          max-rows="5"
          class="mt-2 mb-4"
          style="font-weight: 600"
          plaintext
          :value="episode.description"
        ></b-form-textarea>
      </b-col>
      <b-col class="d-none d-xl-block text-center">
        <div class="mt-2">
          <h2 style="font-weight: 600">Share</h2>
          <div class="mt-2">
            <b-button
              variant="outline-primary"
              size="sm"
              class="mt-1"
              @click="copyLink(episode.id)"
            >
              <feather-icon icon="CopyIcon" />
            </b-button>
            <br />
            <b-button
              variant="outline-primary"
              size="sm"
              class="mt-1"
              @click="shareOnTwitter(episode.id)"
            >
              <feather-icon icon="TwitterIcon" />
            </b-button>
            <br />
            <b-button
              variant="outline-primary"
              size="sm"
              class="mt-1"
              @click="shareOnFacebook(episode.id)"
            >
              <feather-icon icon="FacebookIcon" />
            </b-button>
            <br />
            <b-button
              variant="outline-primary"
              size="sm"
              class="mt-1"
              @click="shareOnLinkedIn(episode.id)"
            >
              <feather-icon icon="LinkedinIcon" />
            </b-button>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
import {
  BButton,
  BCol,
  BRow,
  BCard,
  BCardTitle,
  BCardHeader,
  BFormTextarea,
  BImg,
} from "bootstrap-vue";
import { useUtils as useI18nUtils } from "@core/libs/i18n";

import StatisticCardVertical from "@core/components/statistics-cards/StatisticCardVertical.vue";

export default {
  components: {
    BButton,
    BImg,
    BCol,
    BRow,
    BCard,
    BCardTitle,
    BCardHeader,
    BFormTextarea,
    StatisticCardVertical,
  },
  setup() {
    const { t } = useI18nUtils();
    return { t };
  },
  props: {
    episode: {
      type: Object,
      required: true,
    },
  },
  filters: {
    secondsToMinutes(value) {
      return Math.floor(value / 60);
    },
    leftSeconds(value) {
      return value % 60;
    },
  },
  methods: {
    editEpisode(episode) {
      this.$router.push({
        name: "podcast-episodes-id-edit",
        params: { id: episode.id },
      });
    },
    copyLink(id) {
      navigator.clipboard.writeText(
        `${window.location.origin}/podcast/episode/${id}`
      );
    },
    shareOnTwitter(id) {
      window.open(
        `https://twitter.com/intent/tweet?url=${window.location.origin}/podcast/episode/${id}`,
        "_blank"
      );
    },
    shareOnFacebook(id) {
      window.open(
        `https://www.facebook.com/sharer/sharer.php?u=${window.location.origin}/podcast/episode/${id}`,
        "_blank"
      );
    },
    shareOnLinkedIn(id) {
      window.open(
        `https://www.linkedin.com/shareArticle?mini=true&url=${window.location.origin}/podcast/episode/${id}`,
        "_blank"
      );
    },
  },
  props: {
    episode: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style lang="scss">
@media screen and (max-width: 768px) {
  .coverArtUploadImg {
    align-items: center;
  }
}
.header {
  display: flex;
}
.editBtn {
  margin-left: auto;
}
</style>