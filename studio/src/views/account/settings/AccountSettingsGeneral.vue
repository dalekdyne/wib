<template>
  <b-card>
    <!-- media -->
    <b-media no-body>
      <b-media-aside>
        <b-link>
          <b-img
            ref="previewEl"
            rounded
            :src="optionsLocal.avatar"
            height="80"
          />
        </b-link>
        <!--/ avatar -->
      </b-media-aside>

      <b-media-body class="mt-75 ml-75">
        <!-- upload button -->
        <b-button
          v-ripple.400="'rgba(255, 255, 255, 0.15)'"
          variant="primary"
          size="sm"
          class="mb-75 mr-75"
          @click="$refs.refInputEl.$el.click()"
        >
          {{ t("Upload") }}
        </b-button>
        <b-form-file
          ref="refInputEl"
          v-model="profileFile"
          accept=".jpg, .png, .gif"
          :hidden="true"
          plain
          @input="inputImageRenderer"
        />
        <!--/ upload button -->

        <!-- reset -->
        <b-button
          v-ripple.400="'rgba(186, 191, 199, 0.15)'"
          variant="outline-secondary"
          size="sm"
          class="mb-75 mr-75"
        >
          {{ t("Reset") }}
        </b-button>
        <!--/ reset -->
        <b-card-text>{{ t("Allowed JPG, GIF or PNG.") }}</b-card-text>
      </b-media-body>
    </b-media>
    <!--/ media -->

    <!-- form -->
    <b-form class="mt-2">
      <b-row>
        <b-col sm="6">
          <b-form-group :label="$t('Username')" label-for="account-username">
            <b-form-input
              v-model="optionsLocal.username"
              :placeholder="$t('Username')"
              name="username"
            />
          </b-form-group>
        </b-col>
        <b-col sm="6">
          <b-form-group :label="t('Name')" label-for="account-name">
            <b-form-input
              v-model="optionsLocal.fullName"
              name="name"
              :placeholder="$t('Name')"
            />
          </b-form-group>
        </b-col>
        <b-col sm="6">
          <b-form-group :label="$t('E-mail')" label-for="account-e-mail">
            <b-form-input
              v-model="optionsLocal.email"
              name="email"
              :placeholder="$t('Email')"
            />
          </b-form-group>
        </b-col>

        <!-- alert -->
        <!-- this is important to have to avoid podcast takeover attacks -->
        <b-col cols="12" class="mt-75">
          <b-alert show variant="warning" class="mb-50">
            <h4 class="alert-heading">
              {{ t("Your email is not confirmed. Please check your inbox.") }}
            </h4>
            <br />
            <div class="alert-body">
              <b-link class="alert-link">
                {{ t("Resend confirmation.") }}
              </b-link>
            </div>
          </b-alert>
        </b-col>
        <!--/ alert -->

        <b-col cols="12">
          <b-button
            v-ripple.400="'rgba(255, 255, 255, 0.15)'"
            variant="primary"
            class="mt-2 mr-1"
          >
            {{ t("Save Changes") }}
          </b-button>
          <b-button
            v-ripple.400="'rgba(186, 191, 199, 0.15)'"
            variant="outline-secondary"
            type="reset"
            class="mt-2"
            @click.prevent="resetForm"
          >
            {{ t("Reset") }}
          </b-button>
        </b-col>
      </b-row>
    </b-form>
  </b-card>
</template>

<script>
import {
  BFormFile,
  BButton,
  BForm,
  BFormGroup,
  BFormInput,
  BRow,
  BCol,
  BAlert,
  BCard,
  BCardText,
  BMedia,
  BMediaAside,
  BMediaBody,
  BLink,
  BImg,
} from "bootstrap-vue";
import Ripple from "vue-ripple-directive";
import { useInputImageRenderer } from "@core/comp-functions/forms/form-utils";
import { ref } from "@vue/composition-api";

import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BButton,
    BForm,
    BImg,
    BFormFile,
    BFormGroup,
    BFormInput,
    BRow,
    BCol,
    BAlert,
    BCard,
    BCardText,
    BMedia,
    BMediaAside,
    BMediaBody,
    BLink,
  },
  directives: {
    Ripple,
  },
  props: {
    generalData: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      optionsLocal: JSON.parse(JSON.stringify(this.generalData)),
      profileFile: null,
    };
  },
  methods: {
    resetForm() {
      this.optionsLocal = JSON.parse(JSON.stringify(this.generalData));
    },
  },
  setup() {
    const refInputEl = ref(null);
    const previewEl = ref(null);
    const { t } = useI18nUtils();

    const { inputImageRenderer } = useInputImageRenderer(refInputEl, previewEl);

    return {
      refInputEl,
      previewEl,
      inputImageRenderer,
      t,
    };
  },
};
</script>
