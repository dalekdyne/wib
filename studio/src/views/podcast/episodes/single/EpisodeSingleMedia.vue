<template>
  <b-card>
    <div class="media-card-title">
      <b-card-title>{{ t("Episode media") }}</b-card-title>
      <b-button
        variant="primary"
        class="media-card-button"
        @click="editMedia(episode.id)"
        >{{ t("Edit media") }}</b-button
      >
    </div>
    <b-card-body>
      <div class="video-mask">
        <video width="100%" height="100%" controls>
          <source
            src="https://download.samplelib.com/mp4/sample-30s.mp4"
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
      </div>
    </b-card-body>
  </b-card>
</template>
  
  <script>
import {
  BButton,
  BCol,
  BRow,
  BCard,
  BCardBody,
  BCardTitle,
  BCardHeader,
} from "bootstrap-vue";
import { useUtils as useI18nUtils } from "@core/libs/i18n";


export default {
  components: {
    BButton,
    BCol,
    BRow,
    BCard,
    BCardBody,
    BCardTitle,
    BCardHeader,
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
};
</script>
  
<style lang="scss">
.media-card-title {
  display: flex;
}
.media-card-button {
  margin-left: auto;
}
.video-mask {
  border-radius: 10px;
  overflow: hidden;
}
</style>
