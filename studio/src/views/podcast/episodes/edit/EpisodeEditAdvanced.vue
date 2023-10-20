<template>
  <b-card>
    <b-card-title>
      {{ t("Customize this episode") }}
    </b-card-title>
    <b-row>
      <b-col sm="12" xs="12" md="6" lg="6" xl="6">
        <b-table
          thead-class="hidden-header"
          class="optionsTable"
          responsive="sm"
          :fields="fields"
          :items="customizeOptions"
        >
          <template #cell(value)="data">
            <b-form-input
              type="number"
              v-model="seasonNumber"
              style="width: 150px"
              :placeholder="t('Season number')"
              :hidden="data.value != 1"
            ></b-form-input>
            <b-form-input
              type="number"
              v-model="episodeNumber"
              style="width: 150px"
              :placeholder="t('Episode number')"
              :hidden="data.value != 2"
            ></b-form-input>
            <b-form-select
              :options="episodeTypeOptions"
              v-model="episodeType"
              style="width: 150px"
              :hidden="data.value != 3"
            ></b-form-select>
            <b-form-select
              :options="episodeContentOptions"
              v-model="episodeContent"
              style="width: 150px"
              :hidden="data.value != 4"
            ></b-form-select>
          </template>
        </b-table>
      </b-col>
      <b-col sm="12" xs="12" md="6" lg="6" xl="6">
        <div class="coverArt">
          <b-img
            src="https://picsum.photos/300/300"
            fluid
            rounded
            alt="Image"
          />
          <b-button variant="outline-primary" class="mt-2">
            {{ t("Upload cover art") }}
          </b-button>
        </div>
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
  BFormSelect,
  BImg,
  BTable,
} from "bootstrap-vue";

export default {
  components: {
    BButton,
    BRow,
    BCol,
    BFormGroup,
    BFormInput,
    BForm,
    BFormSelect,
    BCard,
    BCardTitle,
    BImg,
    BTable,
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  data() {
    return {
      fields: [{ key: "index" }, { key: "option" }, { key: "value" }],
      customizeOptions: [
        {
          index: 1,
          option: "Season number",
          value: 1,
        },
        {
          index: 2,
          option: "Episode number",
          value: 2,
        },
        {
          index: 3,
          option: "Episode type",
          value: 3,
        },
        {
          index: 4,
          option: "Content",
          value: 4,
        },
      ],
      seasonNumber: "",
      episodeNumber: "",
      episodeType: "",
      episodeContent: "",
      episodeTypeOptions: [
        { text: "Full", value: "full" },
        { text: "Trailer", value: "trailer" },
        { text: "Bonus", value: "bonus" },
      ],
      episodeContentOptions: [
        { text: "Clean", value: "clean" },
        { text: "Explicit", value: "explicit" },
      ],
    };
  },
};
</script>

<style lang="scss">
.infoline {
  display: flex;
}
.coverArt {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.optionsTable {
  line-height: 5;
}
.hidden-header {
  display: none;
}
</style>