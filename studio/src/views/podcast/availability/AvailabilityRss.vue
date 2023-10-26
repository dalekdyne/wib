<template>
  <b-card>
    <b-form>
      <!-- Title -->
      <div>
        <b-card-title class="platform-card">
          <b-img class="platform-logo" src="@/assets/images/svg/rss.svg" />
          <div class="platform-name">RSS Distribution</div>
        </b-card-title>
      </div>
      <b-row>
        <b-col md="12" xl="12" class="mb-1">
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text"
                ><feather-icon icon="LinkIcon" size="12"
              /></span>
            </b-input-group-prepend>
            <b-form-input id="rssUrl" v-model="rssUrl" readonly></b-form-input>
          </b-input-group>
          <b-button
            variant="primary"
            class="mt-2"
            @click="copyToClipboard(rssUrl)"
          >
            Copy to clipboard
          </b-button>
        </b-col>
      </b-row>
    </b-form>
  </b-card>
</template>

<script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";

import {
  BImg,
  BButton,
  BForm,
  BFormText,
  BFormInput,
  BFormGroup,
  BInputGroup,
  BInputGroupPrepend,
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
    BFormInput,
    BFormGroup,
    BInputGroup,
    BInputGroupPrepend,
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
      rssUrl:
        "https://rss.Wib.com/feeds/5f9b5b5b-8b8a-4b8a-8b5b-5b5b5b5b5b5b.xml",
    };
  },
  methods: {
    copyToClipboard(target) {
      navigator.clipboard.writeText(target);
    },
  },
};
</script>

<style lang="scss">
.platform-card {
  display: flex;
}
.platform-logo {
  width: 30px;
  height: 30px;
}
.platform-name {
  margin-left: 10px;
}
</style>