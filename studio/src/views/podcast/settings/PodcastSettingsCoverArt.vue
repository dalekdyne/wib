<template>
  <b-card>
    <!-- Title -->
    <div>
      <b-card-title>{{ t("Podcast cover art") }}</b-card-title>
    </div>
    <b-row>
      <b-col md="4" xl="4" class="mb-1 coverArtUploadImg">
        <b-img src="https://picsum.photos/300/300" fluid rounded alt="Image" />
      </b-col>
      <b-col md="8" xl="8" class="mb-1">
        <b-form-group>
          <div class="coverArtUploadArea">
            <h6 class="coverArtUploadText">
              {{
                t(
                  "Choose an image for cover art that best represents your podcast."
                )
              }}
            </h6>
            <!-- Upload area for cover art -->
            <input id="podcastCoverArt" type="file" accept="image/*" hidden />
            <b-button variant="primary" @click="uploadCoverArt">{{
              t("Upload cover art")
            }}</b-button>
          </div>
        </b-form-group>
      </b-col>
    </b-row>
  </b-card>
</template>
  
  <script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";

import {
  BImg,
  BButton,
  BForm,
  BFormText,
  BFormFile,
  BFormTextarea,
  BFormGroup,
  BRow,
  BCol,
  BCard,
  BCardText,
  BCardTitle,
} from "bootstrap-vue";

export default {
  components: {
    BImg,
    BButton,
    BForm,
    BFormText,
    BFormGroup,
    BFormFile,
    BFormTextarea,
    BRow,
    BCol,
    BCard,
    BCardText,
    BCardTitle,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  data() {
    return {
      podcastCoverArt: null,
    };
  },
  computed: {},
  methods: {
    uploadCoverArt() {
      document.getElementById("podcastCoverArt").click();
    },
  },
};
</script>
  
  <style lang="scss">
.coverArtUploadArea {
  align-items: center;
  display: flex;
  flex-direction: column;
}
@media screen and (max-width: 768px) {
  .coverArtUploadImg {
    align-items: center;
    display: flex;
    flex-direction: column;
  }
}
.coverArtUploadText {
  margin-top: 7rem;
  text-align: center;
  margin-bottom: 1rem;
}
</style>
  