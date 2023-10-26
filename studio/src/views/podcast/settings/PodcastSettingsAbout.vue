<template>
  <b-card>
    <!-- Title -->
    <div>
      <b-card-title>{{ t("About your podcast") }}</b-card-title>
    </div>

    <b-row>
      <b-col md="12" xl="12" class="mb-1">
        <!-- textarea -->
        <b-form-group :label="$t('Podcast name')" label-for="podcastName">
          <b-form-textarea
            rows="3"
            max-rows="6"
            id="podcastName"
            :placeholder="
              $t(
                'Your podcast name is how people will find your podcast, both on Wib and on other platforms.'
              )
            "
            v-model="podcastName"
            v-on:keyup="podcastNameRemaining = countChar(podcastName, 100, 100)"
          ></b-form-textarea>
          <b-form-text
            >{{ this.podcastNameRemaining }}
            {{ $t("characters remaining") }}</b-form-text
          >
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="12" xl="12" class="mb-1">
        <!-- textarea -->
        <b-form-group
          :label="$t('Podcast description')"
          label-for="podcastDescription"
        >
          <b-form-textarea
            id="podcastDescription"
            :placeholder="
              $t(
                'Tell people what your podcast is about. You can always change this later.'
              )
            "
            rows="6"
            max-rows="10"
            v-model="podcastDescription"
            v-on:keyup="
              podcastDescriptionRemaining = countChar(
                podcastDescription,
                600,
                600
              )
            "
          ></b-form-textarea>
          <b-form-text
            >{{ this.podcastDescriptionRemaining }}
            {{ $t("characters remaining") }}</b-form-text
          >
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
  BFormText,
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
    BButton,
    BForm,
    BFormText,
    BFormGroup,
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
      podcastName: "",
      podcastDescription: "",
      podcastNameRemaining: 100,
      podcastDescriptionRemaining: 600,
    };
  },
  computed: {
    isFormValid() {
      // verify that podcastName and podcastDescription are not empty and are different that the current values
      return (
        this.podcastName.length > 0 &&
        this.podcastDescription.length > 0 &&
        this.podcastName !== this.$store.state.podcast.podcastName &&
        this.podcastDescription !== this.$store.state.podcast.podcastDescription
      );
    },
  },
  methods: {
    countChar(val, limit, remaining) {
      remaining = limit - val.length;
      return remaining;
    },
  },
};
</script>
  
  <style lang="scss" scoped>
</style>
  