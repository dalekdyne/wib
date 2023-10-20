<template>
  <b-card v-if="data" text-variant="center" class="card card-congratulations">
    <!-- images -->
    <b-img
      :src="require('@/assets/images/elements/decore-left.png')"
      class="congratulations-img-left"
    />
    <b-img
      :src="require('@/assets/images/elements/decore-right.png')"
      class="congratulations-img-right"
    />
    <!--/ images -->

    <b-avatar variant="primary" size="70" class="shadow mb-2">
      <feather-icon size="28" icon="AwardIcon" />
    </b-avatar>
    <h1 class="mb-1 mt-50 text-white">
      {{ t("Congratulations") }} {{ data.name }},
    </h1>
    <b-card-text class="m-auto w-75">
      {{ t("Your podcast streamed") }} <strong>{{ data.saleToday }}</strong>
      {{ t("times today") }}!
    </b-card-text>
  </b-card>
</template>

<script>
import { BCard, BImg, BAvatar, BCardText } from "bootstrap-vue";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BCard,
    BAvatar,
    BImg,
    BCardText,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
};
</script>
