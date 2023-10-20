<template>
  <b-row class="match-height">
    <b-col
      v-for="item in items"
      v-bind:data="item"
      v-bind:key="item.id"
      md="6"
      lg="4"
    >
      <b-card
        :key="item.id"
        :title="item.name"
        :sub-title="item.status == 'Published' ? 'Published on ' + item.date : 'Draft'"
      >
        <div class="mb-2" style="transform: rotate(0)">
          <a @click="previewEpisode(item)" class="stretched-link" />
          <b-img :src="item.coverArtUrl" class="mb-2 cover" />
          <b-card-text>{{ item.description }}</b-card-text>
        </div>
        <b-button
          variant="outline-primary"
          size="sm"
          @click="editEpisode(item)"
        >
          <feather-icon icon="EditIcon" />
        </b-button>
        <b-button
          :id="'deleteBtn-' + item.id"
          class="ml-1"
          variant="outline-danger"
          size="sm"
          @click="showPopover('deleteBtn-' + tem.id)"
        >
          <feather-icon icon="TrashIcon" />
        </b-button>
        <b-popover
          variant="danger"
          :target="'deleteBtn-' + item.id"
          placement="top"
          triggers="click blur"
        >
          <template #title> Are you sure? </template>
          <div class="episodeDeletePopover">
            <span>You're about to delete this episode forever!</span>
            <div class="flex">
              <b-button
                variant="danger"
                size="sm"
                class="mt-1"
                @click="deleteEpisode(item)"
              >
                {{ t("Delete") }}
              </b-button>
            </div>
          </div>
        </b-popover>
        <b-button
          :id="'downloadBtn-' + item.id"
          class="ml-1"
          variant="outline-success"
          size="sm"
          @click="downloadEpisode(item.id)"
        >
          <feather-icon icon="DownloadIcon" />
        </b-button>
        <b-popover
          variant="success"
          :target="'downloadBtn-' + item.id"
          placement="top"
          triggers="click blur"
        >
          <template #title> Which version do you want?</template>
          <div class="episodeDeletePopover">
            <span
              >You can click to download either the audio or the video version
              of the podcast.</span
            >
            <div class="flex">
              <b-button
                variant="info"
                size="sm"
                class="mt-1"
                @click="deleteEpisode(item, 'video')"
              >
                {{ t("Video") }}
              </b-button>
              <b-button
                variant="outline-secondary"
                size="sm"
                class="mt-1 ml-1"
                @click="downloadEpisode(item.id, 'audio')"
              >
                {{ t("Audio") }}
              </b-button>
            </div>
          </div>
        </b-popover>
      </b-card>
    </b-col>
  </b-row>
</template>

<script>
import {
  BRow,
  BCol,
  BCard,
  BCardGroup,
  BPopover,
  BButton,
  BImg,
  BCardText,
  BLink,
  BAspect,
} from "bootstrap-vue";
import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BAspect,
    BRow,
    BCol,
    BCard,
    BCardGroup,
    BPopover,
    BButton,
    BImg,
    BCardText,
    BLink,
  },
  methods: {
    previewEpisode(episode) {
      this.$router.push({
        name: "podcast-episodes-id",
        params: { id: episode.id },
      });
    },
    editEpisode(episode) {
      this.$router.push({
        name: "podcast-episodes-id-edit",
        params: { id: episode.id },
      });
    },
    deleteEpisode(episode) {
      console.log(episode);
    },
    downloadEpisode(episodeId) {
      console.log(episodeId);
    },
    showPopover(target) {
      this.$root.$emit("bv::show::popover", target);
    },
    hidePopover(target) {
      this.$root.$emit("bv::hide::popover", target);
    },
  },
  setup() {
    const { t } = useI18nUtils();
    return { t };
  },
  props: {
    items: {
      type: Array,
      default: () => [],
      required: true,
    },
  },
};
</script>

<style lang="scss">
.cover {
  object-fit: cover;
  width: 100%;
  height: 300px;
}
</style>