<template>
  <b-card>
    <b-row>
      <h6 class="section-label mx-1 mb-2">{{ t("Danger zone") }}</h6>
    </b-row>
    <b-col cols="12" class="mb-2">
      <b-card-text>
        {{ t("You can delete your account by clicking the button below. This is a permanent action.") }}
      </b-card-text>
      <b-button
        v-ripple.400="'rgba(255, 255, 255, 0.15)'"
        variant="danger"
        class="mr-1 mt-1"
        :disabled="requestedDelete"
        @click="deleteAccount"
      >
        {{ requestedDelete ? t("Deleting your account...") : t("Delete") }}
      </b-button>
    </b-col>
    <b-col cols="12" class="mb-2">
      <b-form-text v-if="requestedDelete">
        {{ t("We will delete your account in the next 15 minutes. Logging you out...") }}
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
    dangerZone: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      requestedDelete: false,
    };
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  methods: {
    deleteAccount() {
      this.requestedDelete = true;
      this.$store.dispatch("account/delete");
    },
  },
};
</script>
