<template>
  <b-card>
    <b-row>
      <h6 class="section-label mx-1 mb-2">{{ t("Activity") }}</h6>
      <b-col cols="12" class="mb-2">
        <b-form-checkbox
          id="accountSwitch1"
          :checked="localOptions.upcomingInterview"
          name="check-button"
          switch
          inline
        >
          <span>
            {{ t("Email me when I have an interview session upcoming") }}</span
          >
      </b-form-checkbox>
      </b-col>
      <b-col cols="12" class="mb-2">
        <b-form-checkbox
          id="accountSwitch2"
          :checked="localOptions.scheduledPodcastPublished"
          name="check-button"
          switch
          inline
        >
          <span>{{ t("Email me when a scheduled podcast is published") }}</span>
        </b-form-checkbox>
      </b-col>
      <b-col cols="12" class="mb-2">
        <b-form-checkbox
          id="accountSwitch3"
          :checked="localOptions.deletedCalendarEvent"
          name="check-button"
          switch
          inline
        >
          <span>{{ t("Email me when I delete a calendar event") }}</span>
        </b-form-checkbox>
      </b-col>

      <!-- buttons -->
      <b-col cols="12">
        <b-button
          v-ripple.400="'rgba(255, 255, 255, 0.15)'"
          variant="primary"
          class="mr-1 mt-1"
        >
          {{ t("Save Changes") }}
        </b-button>
        <b-button
          v-ripple.400="'rgba(186, 191, 199, 0.15)'"
          type="reset"
          class="mt-1"
          variant="outline-secondary"
        >
          {{ t("Reset") }}
        </b-button>
      </b-col>
      <!--/ buttons -->
    </b-row>
  </b-card>
</template>

<script>
import { BButton, BRow, BCol, BCard, BFormCheckbox } from "bootstrap-vue";
import Ripple from "vue-ripple-directive";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BButton,
    BRow,
    BCol,
    BCard,
    BFormCheckbox,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  directives: {
    Ripple,
  },
  props: {
    notificationData: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      localOptions: JSON.parse(JSON.stringify(this.notificationData)),
    };
  },
};
</script>
