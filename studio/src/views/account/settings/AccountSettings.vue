<template>
  <b-tabs
    vertical
    content-class="col-12 col-md-9 mt-1 mt-md-0"
    pills
    nav-wrapper-class="col-md-3 col-12"
    nav-class="nav-left"
  >
    <!-- general tab -->
    <b-tab active>
      <!-- title -->
      <template #title>
        <feather-icon icon="UserIcon" size="18" class="mr-50" />
        <span class="font-weight-bold"> {{ t("General") }}</span>
      </template>

      <account-settings-general
        v-if="options.general"
        :general-data="options.general"
      />
    </b-tab>
    <!--/ general tab -->

    <!-- change password tab -->
    <b-tab>
      <!-- title -->
      <template #title>
        <feather-icon icon="LockIcon" size="18" class="mr-50" />
        <span class="font-weight-bold">{{ t("Change Password") }}</span>
      </template>

      <account-settings-password />
    </b-tab>
    <!--/ change password tab -->

    <!-- notification -->
    <b-tab>
      <!-- title -->
      <template #title>
        <feather-icon icon="BellIcon" size="18" class="mr-50" />
        <span class="font-weight-bold">{{ t("Notifications") }}</span>
      </template>

      <account-settings-notification
        v-if="options.notification"
        :notification-data="options.notification"
      />
    </b-tab>

    <!-- userdata -->
    <b-tab>
      <template #title>
        <feather-icon icon="HardDriveIcon" size="18" class="mr-50" />
        <span class="font-weight-bold">{{ t("User Data") }}</span>
      </template>

      <account-settings-userdata
        v-if="options.userdata"
        :userdata-data="options.userdata"
      />
    </b-tab>

    <!-- danger zone -->
    <b-tab>
      <template #title>
        <feather-icon icon="AlertTriangleIcon" size="18" class="mr-50" />
        <span class="font-weight-bold">{{ t("Danger zone") }}</span>
      </template>

      <account-settings-dangerzone
        v-if="options.dangerZone"
        :userdata-data="options.dangerZone"
      />
    </b-tab>
  </b-tabs>
</template>

<script>
import { BTabs, BTab } from "bootstrap-vue";
import AccountSettingsGeneral from "./AccountSettingsGeneral.vue";
import AccountSettingsPassword from "./AccountSettingsPassword.vue";
import AccountSettingsNotification from "./AccountSettingsNotification.vue";
import AccountSettingsUserdata from "./AccountSettingsUserdata.vue";
import AccountSettingsDangerzone from "./AccountSettingsDangerzone.vue";


import { useUtils as useI18nUtils } from "@core/libs/i18n";

export default {
  components: {
    BTabs,
    BTab,
    AccountSettingsGeneral,
    AccountSettingsPassword,
    AccountSettingsNotification,
    AccountSettingsUserdata,
    AccountSettingsDangerzone,
  },
  data() {
    return {
      options: {},
    };
  },
  setup() {
    const { t } = useI18nUtils();

    return {
      t,
    };
  },
  beforeCreate() {
    this.$http.get("/user").then((res) => {
      this.options = res.data;
    });
  },
};
</script>
