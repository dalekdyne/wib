<template>
  <div class="accordion" role="tablist">
    <b-card no-body>
      <b-card-header
        header-tag="header"
        class="p-1 accordion-header"
        role="tab"
      >
        <div class="platform-header">
          <b-img class="platform-logo" src="@/assets/images/svg/apple.svg" />
          <h6 class="ml-1 platform-name">Apple Podcasts</h6>
        </div>
        <b-button
          variant="light"
          class="accordion-button"
          v-b-toggle.accordion-1
        >
          <feather-icon icon="ChevronDownIcon" size="16" />
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text"
                ><feather-icon icon="LinkIcon" size="12"
              /></span>
            </b-input-group-prepend>
            <b-form-input
              id="appleUrl"
              v-model="appleUrl"
              readonly
            ></b-form-input>
          </b-input-group>
          <b-button
            @click="
              appleUrl == ''
                ? enableIntegration('apple')
                : copyToClipboard(appleUrl)
            "
            variant="primary"
            class="mt-2"
            >{{ appleUrl != "" ? "Copy" : "Enable" }}</b-button
          >
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body>
      <b-card-header header-tag="header" class="p-1 accordion-header" role="tab"
        ><div class="platform-header">
          <b-img class="platform-logo" src="@/assets/images/svg/youtube.svg" />
          <h6 class="ml-1 platform-name">YouTube</h6>
        </div>
        <b-button
          variant="light"
          class="accordion-button"
          v-b-toggle.accordion-2
        >
          <feather-icon icon="ChevronDownIcon" size="16" />
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text"
                ><feather-icon icon="LinkIcon" size="12"
              /></span>
            </b-input-group-prepend>
            <b-form-input
              id="youtubeUrl"
              v-model="youtubeUrl"
              readonly
            ></b-form-input>
          </b-input-group>
          <b-button
            @click="
              youtubeUrl == ''
                ? enableIntegration('youtube')
                : copyToClipboard(youtubeUrl)
            "
            variant="primary"
            class="mt-2"
            >{{ youtubeUrl != "" ? "Copy" : "Enable" }}</b-button
          >
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body>
      <b-card-header
        header-tag="header"
        class="p-1 accordion-header"
        role="tab"
      >
        <div class="platform-header">
          <b-img
            class="platform-logo"
            src="@/assets/images/svg/soundcloud.svg"
          />
          <h6 class="ml-1 platform-name">SoundCloud</h6>
        </div>
        <b-button
          variant="light"
          class="accordion-button"
          v-b-toggle.accordion-3
        >
          <feather-icon icon="ChevronDownIcon" size="16" />
        </b-button>
      </b-card-header>
      <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <b-input-group>
            <b-input-group-prepend>
              <span class="input-group-text"
                ><feather-icon icon="LinkIcon" size="12"
              /></span>
            </b-input-group-prepend>
            <b-form-input
              id="soundcloudUrl"
              v-model="soundcloudUrl"
              readonly
            ></b-form-input>
          </b-input-group>
          <b-button
            @click="
              soundcloudUrl == ''
                ? enableIntegration('soundcloud')
                : copyToClipboard(soundcloudUrl)
            "
            variant="primary"
            class="mt-2"
            >{{ soundcloudUrl != "" ? "Copy" : "Enable" }}</b-button
          >
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>
  
  <script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";

import { VBToggle } from "bootstrap-vue";
import Vue from "vue";

Vue.directive("b-toggle", VBToggle);

import {
  BInputGroup,
  BFormInput,
  BInputGroupPrepend,
  BImg,
  BButton,
  BForm,
  BRow,
  BCol,
  BCollapse,
  BCard,
  BCardHeader,
  BCardBody,
  BCardText,
  BCardTitle,
} from "bootstrap-vue";

export default {
  components: {
    BInputGroup,
    BFormInput,
    BInputGroupPrepend,
    BImg,
    BButton,
    BForm,
    BCollapse,
    BRow,
    BCol,
    BCard,
    BCardBody,
    BCardHeader,
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
      appleUrl:
        "https://podcasts.apple.com/us/podcast/5f9b5b5b-8b8a-4b8a-8b5b-5b5b5b5b5b5b",
      youtubeUrl: "https://www.youtube.com/watch?v=5b5b5b5b5b5b",
      soundcloudUrl: "https://soundcloud.com/5b5b5b5b5b5b",
    };
  },
  methods: {
    copyToClipboard(target) {
      navigator.clipboard.writeText(target);
    },
    enableIntegration(service) {
      console.log("enable integration" + service);
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
.accordion-header {
  display: flex;
}
.accordion-button {
  margin-left: auto;
}
.platform-logo {
  width: 30px;
  height: 30px;
  float: left;
}
.platform-name {
  margin-top: 6px;
  float: left;
}
.platform-header {
  display: flex;
}
</style>