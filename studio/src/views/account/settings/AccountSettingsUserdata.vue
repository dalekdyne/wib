<template>
  <b-card>
    <b-row>
      <h6 class="section-label mx-1 mb-2">{{ t("Your data") }}</h6>
    </b-row>
    <b-col cols="12" class="mb-2">
      <b-card-text>
        {{ t("You can download all your media by clicking the button below.") }}
      </b-card-text>
      <b-button
        v-ripple.400="'rgba(255, 255, 255, 0.15)'"
        variant="primary"
        class="mr-1 mt-1"
        :disabled="requestedDownload"
        @click="downloadMedia"
      >
        {{ requestedDownload ? t("Gathering your data...") : t("Download") }}
      </b-button>
    </b-col>
    <b-col cols="12" class="mb-2">
      <b-form-text v-if="requestedDownload">
        {{ t("We will send you an email when you're data is ready to download.") }}
      </b-form-text>
    </b-col>
  </b-card>
</template>

<script>
import {
  BCard,
  BCardText,
  BRow,
  BCol,
  BFormText,
  BButton,
} from "bootstrap-vue";
import Ripple from "vue-ripple-directive";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BCard,
    BCardText,
    BButton,
    BRow,
    BCol,
    BFormText,
  },
  directives: {
    Ripple,
  },
  props: {
    userdata: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      requestedDownload: false,
    };
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  methods: {
    downloadMedia() {
      this.requestedDownload = true;
      this.$store.dispatch("account/download-media");
    },
  },
};
</script>
