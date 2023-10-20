<template>
  <b-card>
    <!-- Title -->
    <div>
      <b-card-title>{{ t("Podcast details") }}</b-card-title>
    </div>
    <b-row>
      <b-col>
        <b-form-group
          :label="$t('Podcast category')"
          label-for="podcastCategory"
        >
          <b-form-select
            id="podcastCategory"
            v-model="podcastCategory"
            :options="podcastCategories"
          />
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col>
        <b-form-group
          :label="$t('Podcast language')"
          label-for="podcastLanguage"
        >
          <b-form-select
            id="podcastLanguage"
            v-model="podcastLanguage"
            :options="languages"
          />
        </b-form-group>
      </b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col>
        <b-form-group :label="$t('Podcast creator')" label-for="podcastCreator">
          <b-form-input
            id="podcastCreator"
            v-model="podcastCreator"
            :placeholder="
              $t('The name of the studio or person who creates the podcast')
            "
          />
        </b-form-group>
      </b-col>
    </b-row>
  </b-card>
</template>
  
  <script>
import { useUtils as useI18nUtils } from "@core/libs/i18n";
import {
  getAllLanguages,
  getLanguageCode,
  getLanguageName,
} from "@/libs/helpers/languages";
import { categories } from "@/libs/helpers/podcastCategories";

import {
  BButton,
  BForm,
  BFormText,
  BFormSelect,
  BFormGroup,
  BFormInput,
  BRow,
  BCol,
  BCard,
  BCardTitle,
  BInputGroup,
  BInputGroupAppend,
} from "bootstrap-vue";

export default {
  components: {
    categories,
    BButton,
    BForm,
    BFormText,
    BFormSelect,
    BFormGroup,
    BFormInput,
    BRow,
    BCol,
    BCard,
    BCardTitle,
    BInputGroup,
    BInputGroupAppend,
  },
  data() {
    return {
      podcastCategory: "",
      podcastLanguage: "",
      podcastCreator: "",
    };
  },
  setup() {
    const { t } = useI18nUtils();
    const languages = getAllLanguages();
    const podcastCategories = categories;

    return {
      podcastCategories,
      languages,
      getAllLanguages,
      getLanguageCode,
      getLanguageName,
      t,
    };
  },
  computed: {
    isFormValid() {
      return (
        this.podcastCategory &&
        this.podcastLanguage &&
        this.podcastCreator !== ""
      );
    },
  },
  methods: {
  },
};
</script>


  <style lang="scss">
</style>
  