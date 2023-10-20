<template>
  <b-card>
    <b-form>
      <!-- Title -->
      <div>
        <b-card-title>
          <div>FAQs</div>
        </b-card-title>
      </div>
      <b-row>
        <b-col md="12" xl="12" class="mb-1">
          <div>
            <h6>What does my RSS feed do?</h6>
            <p>
              Your RSS feed allows your podcast to appear in other podcast apps,
              in some cases automatically. This feed is public and contains your
              email address.
            </p>
          </div>
          <div class="mt-2">
            <h6>How do I distribute my podcast elsewhere?</h6>
            <p>
              You can distribute your podcast to other podcast apps by
              submitting your RSS feed to them. You can find a list of podcast
              apps that accept RSS feeds
              <a
                href="https://podnews.net/article/podcast-apps-that-accept-rss-feeds"
                target="_blank"
                >here</a
              >.
            </p>
          </div>
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
        "https://rss.podbeam.com/feeds/5f9b5b5b-8b8a-4b8a-8b5b-5b5b5b5b5b5b.xml",
    };
  },
  methods: {},
};
</script>
  
  <style lang="scss">
</style>