<template>
  <b-card>
    <div class="paginationContainer">
      <b-table
        id="episodesTable"
        :per-page="perPage"
        :current-page="currentPage"
        class="episodesTable"
        responsive="xl"
        :fields="fields"
        :items="items"
        hover
        @row-clicked="previewEpisode($event)"
      >
        <template #cell(length)="data">
          <!-- convert seconds to minutes -->
          <span
            >{{ data.item.length | secondsToMinutes }}:{{
              data.item.length | leftSeconds
            }}
          </span>
        </template>
        <template #cell(status)="data">
          <b-badge
            pill
            :variant="data.value == 'Published' ? 'success' : 'warning'"
          >
            {{ data.value }}
          </b-badge>
        </template>
        <template #cell(actions)="data">
          <b-button
            variant="outline-primary"
            size="sm"
            @click="editEpisode(data.item)"
          >
            <feather-icon icon="EditIcon" />
          </b-button>
          <b-button
            :id="'deleteBtn-' + data.item.id"
            class="ml-1"
            variant="outline-danger"
            size="sm"
            @click="showPopover('deleteBtn-' + data.item.id)"
          >
            <feather-icon icon="TrashIcon" />
          </b-button>
          <b-popover
            variant="danger"
            :target="'deleteBtn-' + data.item.id"
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
                  @click="deleteEpisode(data.item)"
                >
                  {{ t("Delete") }}
                </b-button>
              </div>
            </div>
          </b-popover>
          <b-button
            :id="'downloadBtn-' + data.item.id"
            class="ml-1"
            variant="outline-success"
            size="sm"
            @click="downloadEpisode(data.item.id)"
          >
            <feather-icon icon="DownloadIcon" />
          </b-button>
          <b-popover
            variant="success"
            :target="'downloadBtn-' + data.item.id"
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
                  @click="deleteEpisode(data.item, 'video')"
                >
                  {{ t("Video") }}
                </b-button>
                <b-button
                  variant="outline-secondary"
                  size="sm"
                  class="mt-1 ml-1"
                  @click="downloadEpisode(data.item.id, 'audio')"
                >
                  {{ t("Audio") }}
                </b-button>
              </div>
            </div>
          </b-popover>
        </template>
      </b-table>
      <b-pagination
        class="paginationController"
        v-model="currentPage"
        :total-rows="totalRows"
        :per-page="perPage"
      />
    </div>
  </b-card>
</template>
    
    <script>
import {
  BTable,
  BCard,
  BPagination,
  BButton,
  BBadge,
  BPopover,
} from "bootstrap-vue";
import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BPopover,
    BBadge,
    BButton,
    BPagination,
    BTable,
    BCard,
  },
  data() {
    return {
      perPage: 15,
      currentPage: 1,
      totalRows: 10,
      fields: [
        { key: "name", label: "Name" },
        { key: "length", label: "Length" },
        { key: "streams", label: "Streams" },
        { key: "date", label: "Date" },
        { key: "type", label: "Type" },
        { key: "status", label: "Status" },
        { key: "actions", label: "" },
      ],
    };
  },
  setup() {
    const { t } = useI18nUtils();
    return {
      t,
    };
  },
  computed: {},
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
  filters: {
    secondsToMinutes(value) {
      return Math.floor(value / 60);
    },
    leftSeconds(value) {
      return value % 60;
    },
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
.paginationContainer {
  display: flex;
  flex-direction: column;
}
.paginationController {
  margin-top: 1rem;
  margin-left: auto;
}
.episodesTable {
  line-height: 5;
  text-align: center;
}
.episodesTable td:first-child {
  text-align: left;
}
.episodesTable th:first-child {
  text-align: left;
}
.episodesTable th {
  border-top: none;
}
.episodeDeletePopover {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
    