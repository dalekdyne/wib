<template>
  <b-card v-if="data" no-body>
    <b-card-header>
      <b-card-title class="ml-25">
        {{ t("Podcast timeline") }}
      </b-card-title>
    </b-card-header>

    <!-- timeline -->
    <b-card-body>
      <app-timeline>
        <app-timeline-item
          v-bind:data="item"
          v-bind:key="item.id"
          v-for="item in data"
          variant="primary"
        >
          <a @click="previewEpisode(item)" class="stretched-link" />
          <div
            class="
              d-flex
              justify-content-between
              flex-sm-row flex-column
              mb-sm-0 mb-1
            "
          >
            <h6>{{ item.title }}</h6>
          </div>
          <p>{{ item.description }}</p>
          <b-badge
            pill
            :variant="item.status == 'Published' ? 'success' : 'warning'"
            >{{ item.status }}</b-badge
          >
        </app-timeline-item>
      </app-timeline>
      <!--/ timeline -->
    </b-card-body>
  </b-card>
</template>

<script>
import {
  BBadge,
  BCard,
  BCardBody,
  BCardHeader,
  BCardTitle,
  BImg,
  BMedia,
  BMediaBody,
  BMediaAside,
  BAvatar,
  BAvatarGroup,
  VBTooltip,
} from "bootstrap-vue";
import AppTimeline from "@core/components/app-timeline/AppTimeline.vue";
import AppTimelineItem from "@core/components/app-timeline/AppTimelineItem.vue";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

/* eslint-disable global-require */
export default {
  components: {
    BBadge,
    BCard,
    BImg,
    BCardBody,
    BCardHeader,
    BCardTitle,
    AppTimeline,
    AppTimelineItem,
    BMedia,
    BAvatar,
    BMediaBody,
    BMediaAside,
    BAvatarGroup,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  directives: {
    "b-tooltip": VBTooltip,
  },
  props: {
    data: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    previewEpisode(episode) {
      this.$router.push({
        name: "podcast-episodes-id",
        params: { id: episode.id },
      });
    },
  },
};
</script>
