<template>
  <b-card>
    <!-- Title -->
    <div>
      <b-card-title>{{ t("Advanced options") }}</b-card-title>
    </div>
    <b-row>
      <b-col>
        <div class="explicitContent">
          <h6 class="mt-2">{{ t("Content") }}</h6>
          <div class="explicitContentCheckbox">
            <b-card-text class="mb-0"> {{ t("Explicit") }} </b-card-text>
            <b-form-checkbox
              class="custom-control-danger mt-1"
              checked="false"
              name="contentWarning"
              switch
            />
          </div>
        </div>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col>
        <b-form-group :label="$t('Podcast website')" label-for="podcastWebsite">
          <b-form-input
            id="podcastWebsite"
            v-model="podcastWebsite"
            :placeholder="
              $t('A link to your podcast website - if you have one')
            "
          />
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col>
        <b-form-group :label="$t('Donations link')" label-for="donationsLink">
          <b-form-input
            id="donationsLink"
            v-model="donationsLink"
            :placeholder="$t('Where listeners can donate to your podcast')"
          />
        </b-form-group>
      </b-col>
    </b-row>
  </b-card>
</template>
    
    <script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";

import {
  BButton,
  BForm,
  BFormCheckbox,
  BFormGroup,
  BFormInput,
  BRow,
  BCol,
  BCard,
  BCardText,
  BCardTitle,
  BInputGroup,
  BInputGroupAppend,
} from "bootstrap-vue";

export default {
  components: {
    BButton,
    BForm,
    BFormCheckbox,
    BFormGroup,
    BFormInput,
    BRow,
    BCol,
    BCard,
    BCardTitle,
    BCardText,
    BInputGroup,
    BInputGroupAppend,
  },
  data() {
    return {
      podcastWebsite: "",
      donationsLink: "",
    };
  },
  setup() {
    const { t } = useI18nUtils();
    return {
      t,
    };
  },
  computed: {
    isFormValid() {
      // Check if podcastWebsite and donationsLink are not the same as the current values
      //   if (
      //     this.podcastWebsite !== this.$store.state.podcast.podcastWebsite ||
      //     this.donationsLink !== this.$store.state.podcast.donationsLink
      //   ) {
      //     return true;
      //   }
    },
  },
  methods: {
  },
};
</script>
  
  
    <style lang="scss">
.explicitContent {
  display: flex;
  justify-content: space-between;
}
.explicitContentCheckbox {
  margin-left: auto;
}
</style>
    