<template>
  <b-card>
    <b-card-title>
      {{ t("Media") }}
    </b-card-title>
    <b-row>
      <b-col sm="12" xs="12" md="6" lg="6" xl="6">
        <div class="dropzone-ctn">
          <vue-dropzone
            class="dropzone"
            ref="episodeMediaDropzone"
            id="episodeMediaDropzone"
            :options="dropzoneOptions"
          ></vue-dropzone>
        </div>
      </b-col>
      <b-col class="dropzone-row" sm="12" xs="12" md="6" lg="6" xl="6">
        <div class="coverArt">
          <div class="video-mask">
            <video width="100%" height="100%" controls>
              <source
                src="https://download.samplelib.com/mp4/sample-30s.mp4"
                type="video/mp4"
              />
              Your browser does not support the video tag.
            </video>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";
import vue2Dropzone from "vue2-dropzone";

import {
  BRow,
  BForm,
  BCol,
  BCard,
  BCardTitle,
  BButton,
  BFormGroup,
  BFormInput,
  BFormSelect,
  BImg,
  BTable,
} from "bootstrap-vue";

export default {
  components: {
    vueDropzone: vue2Dropzone,
    BButton,
    BRow,
    BCol,
    BFormGroup,
    BFormInput,
    BForm,
    BFormSelect,
    BCard,
    BCardTitle,
    BImg,
    BTable,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  data() {
    return {
      // https://rowanwins.github.io/vue-dropzone/docs/dist/#/aws-s3-upload
      dropzoneOptions: {
        url: "https://httpbin.org/post",
        thumbnailWidth: 150,
        addRemoveLinks: true,
        maxFilesize: 12000,
        acceptedFiles: "video/*",
        dictDefaultMessage:
          "<i class='fa-3x fa fa-cloud-upload'></i><br /><h3>Drop file here to replace the current media</h3>",
      },
      fields: [{ key: "index" }, { key: "option" }, { key: "value" }],
      customizeOptions: [
        {
          index: 1,
          option: "Season number",
          value: 1,
        },
        {
          index: 2,
          option: "Episode number",
          value: 2,
        },
        {
          index: 3,
          option: "Episode type",
          value: 3,
        },
        {
          index: 4,
          option: "Content",
          value: 4,
        },
      ],
      seasonNumber: "",
      episodeNumber: "",
      episodeType: "",
      episodeContent: "",
      episodeTypeOptions: [
        { text: "Full", value: "full" },
        { text: "Trailer", value: "trailer" },
        { text: "Bonus", value: "bonus" },
      ],
      episodeContentOptions: [
        { text: "Clean", value: "clean" },
        { text: "Explicit", value: "explicit" },
      ],
    };
  },
};
</script>

<style lang="scss">
@import url("~vue2-dropzone/dist/vue2Dropzone.min.css");
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");

.coverArt {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.video-mask {
  border-radius: 10px;
  overflow: hidden;
}
.dropzone-ctn {
  display: table;
  width: 100%;
  height: 100%;
}
.dropzone {
  border: 2px dashed #0087f7;
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}
@media screen and (max-width: 768px) {
  .dropzone-row {
    margin-top: 20px;
  }
}
</style>