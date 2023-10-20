<template>
  <div class="navbar-container d-flex content align-items-center">
    <!-- Nav Menu Toggler -->
    <ul class="nav navbar-nav d-xl-none">
      <li class="nav-item">
        <b-link class="nav-link" @click="toggleVerticalMenuActive">
          <feather-icon icon="MenuIcon" size="21" />
        </b-link>
      </li>
    </ul>
    <ul class="mobile-logo align-items-center ml-auto d-xl-none">
      <app-navbar-horizontal-layout-brand-mobile />
    </ul>
    <!-- Right Col -->
    <b-navbar-nav class="nav align-items-center ml-auto">
      <locale class="d-none d-lg-block d-xl-block"/>
      <dark-Toggler class="d-none d-lg-block" />
      <user-dropdown />
    </b-navbar-nav>
  </div>
</template>

<script>
import { BLink, BNavbarNav } from "bootstrap-vue";
import Bookmarks from "./components/Bookmarks.vue";
import Locale from "./components/Locale.vue";
import DarkToggler from "./components/DarkToggler.vue";
import SearchBar from "./components/SearchBar.vue";
import NotificationDropdown from "./components/NotificationDropdown.vue";
import UserDropdown from "./components/UserDropdown.vue";
import AppNavbarHorizontalLayoutBrandMobile from "./AppNavbarHorizontalLayoutBrandMobile.vue";

export default {
  components: {
    BLink,

    // Navbar Components
    AppNavbarHorizontalLayoutBrandMobile,
    BNavbarNav,
    Bookmarks,
    Locale,
    DarkToggler,
    SearchBar,
    NotificationDropdown,
    UserDropdown,
  },
  props: {
    toggleVerticalMenuActive: {
      type: Function,
      default: () => {},
    },
  },
};
</script>
<style lang="scss">
@media screen and (max-width: 575px) {
  .mobile-logo {
    margin: 0;
    padding-left: 20px;
  }
}
@media screen and (min-width: 576px) and (max-width: 991px) {
  .mobile-logo {
    margin: 0;
    padding-left: 150px;
  }
}
@media screen and (min-width: 992px) and (max-width: 1200px) {
  .mobile-logo {
    margin: 0;
    padding-left: 240px;
  }
}
</style>
