<template>
  <b-card>
    <div class="overview-card-title">
      <b-card-title>{{ t("Details") }}</b-card-title>
    </div>
    <b-row>
      <b-col md="12" xl="12" class="mb-1">
        <!-- textarea -->
        <b-form-group :label="$t('Episode title')" label-for="episodeTitle">
          <b-form-input
            rows="1"
            max-rows="6"
            id="episodeTitle"
            :placeholder="$t('What do you want to call this episode?')"
            v-model="episodeTitle"
            v-on:keyup="
              episodeTitleRemaining = countChar(episodeTitle, 200, 200)
            "
          ></b-form-input>
          <b-form-text
            >{{ this.episodeTitleRemaining }}
            {{ $t("characters remaining") }}</b-form-text
          >
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col md="12" xl="12" class="mb-1">
        <!-- textarea -->
        <b-form-group
          :label="$t('Episode description')"
          label-for="episodeDescription"
        >
          <b-form-textarea
            id="episodeDescription"
            :placeholder="$t('What else do you want your listeners to know?')"
            rows="6"
            max-rows="10"
            v-model="episodeDescription"
            v-on:keyup="
              episodeDescriptionRemaining = countChar(
                episodeDescription,
                4000,
                4000
              )
            "
          ></b-form-textarea>
          <b-form-text
            >{{ this.episodeDescriptionRemaining }}
            {{ $t("characters remaining") }}</b-form-text
          >
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col xl="2" md="2" lg="2" sm="4" xs="4">
        <b-form-group :label="$t('Publish date')" label-for="publishDate">
          <flat-pickr
            v-model="publishDate"
            class="form-control"
            :config="{
              enableTime: true,
              dateFormat: 'Y-m-d H:i',
              time_24hr: true,
              disable: [disableDates],
            }"
          />
        </b-form-group>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";
import {
  BRow,
  BForm,
  BCol,
  BCard,
  BCardTitle,
  BButton,
  BFormGroup,
  BFormInput,
  BFormDatepicker,
  BFormTimepicker,
  BFormText,
  BFormTextarea,
} from "bootstrap-vue";

import flatPickr from "vue-flatpickr-component";

export default {
  components: {
    flatPickr,
    BButton,
    BRow,
    BCol,
    BFormGroup,
    BFormInput,
    BForm,
    BFormDatepicker,
    BFormTimepicker,
    BFormText,
    BFormTextarea,
    BCard,
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
      disableDates: {
        from: "1980-01-01",
        to: new Date() - 1,
      },
      publishDate: new Date(),
      episodeTitle: "",
      episodeDescription: "",
      episodeTitleRemaining: 100,
      episodeDescriptionRemaining: 4000,
    };
  },
  computed: {},
  methods: {
    countChar(val, limit, remaining) {
      remaining = limit - val.length;
      return remaining;
    },
    disabledDatesPast(date) {
      return date < new Date();
    },
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
@import "@core/scss/vue/libs/vue-flatpicker.scss";
</style>