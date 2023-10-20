<template>
  <div>
    <b-sidebar
      id="sidebar-add-new-event"
      sidebar-class="sidebar-lg"
      :visible="isEventHandlerSidebarActive"
      bg-variant="white"
      shadow
      backdrop
      no-header
      right
      @change="(val) => $emit('update:is-event-handler-sidebar-active', val)"
    >
      <template #default="{ hide }">
        <!-- Header -->
        <div
          class="
            d-flex
            justify-content-between
            align-items-center
            content-sidebar-header
            px-2
            py-1
          "
        >
          <h5 class="mb-0">{{ eventLocal.id ? "Update" : "Add" }} Event</h5>
          <div>
            <feather-icon
              v-if="eventLocal.id"
              icon="TrashIcon"
              class="cursor-pointer"
              @click="
                $emit('remove-event');
                hide();
              "
            />
            <feather-icon
              class="ml-1 cursor-pointer"
              icon="XIcon"
              size="16"
              @click="hide"
            />
          </div>
        </div>

        <!-- Body -->
        <validation-observer #default="{ handleSubmit }" ref="refFormObserver">
          <!-- Form -->
          <b-form
            class="p-2"
            @submit.prevent="handleSubmit(onSubmit)"
            @reset.prevent="resetForm"
          >
            <!-- Title -->
            <validation-provider
              #default="validationContext"
              name="Title"
              rules="required"
            >
              <b-form-group label="Title" label-for="event-title">
                <b-form-input
                  id="event-title"
                  v-model="eventLocal.title"
                  autofocus
                  :state="getValidationState(validationContext)"
                  trim
                  placeholder="Event Title"
                />

                <b-form-invalid-feedback>
                  {{ validationContext.errors[0] }}
                </b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <!-- Recording Date -->
            <validation-provider
              #default="validationContext"
              name="Recording Date"
              rules="required"
            >
              <b-form-group
                label="Recording Date"
                label-for="recording-date"
                :state="getValidationState(validationContext)"
              >
                <flat-pickr
                  v-model="eventLocal.start"
                  class="form-control"
                  :config="{
                    enableTime: true,
                    dateFormat: 'Y-m-d H:i',
                    time_24hr: true,
                    disable: [disableDates],
                  }"
                />
                <b-form-invalid-feedback
                  :state="getValidationState(validationContext)"
                >
                  {{ validationContext.errors[0] }}
                </b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <!-- Event URL -->
            <validation-provider
              #default="validationContext"
              name="Event URL"
              rules="url"
            >
              <b-form-group label="Event URL" label-for="event-url">
                <b-form-input
                  id="event-url"
                  v-model="eventLocal.eventUrl"
                  type="url"
                  :state="getValidationState(validationContext)"
                  placeholder="htttps://podbeam.io/studio/session/123"
                  trim
                  readonly
                />
                <b-form-invalid-feedback
                  :state="getValidationState(validationContext)"
                >
                  {{ validationContext.errors[0] }}
                </b-form-invalid-feedback>
              </b-form-group>
            </validation-provider>

            <!-- Guests -->
            <b-form-group label="Add Guests" label-for="add-guests">
              <div class="guest-list-ctn">
                <b-form-input
                  id="add-guests"
                  v-model="eventLocal.guest"
                  type="text"
                  placeholder="Add Guests"
                  :state="isValidEmail(eventLocal.guest)"
                />
                <b-button
                  variant="outline-primary"
                  class="ml-1"
                  size="sm"
                  @click="addGuest(eventLocal.guest, eventLocal.extendedProps.guests); eventLocal.guest = ''"
                  :disabled="!isValidEmail(eventLocal.guest)"
                  >Add</b-button
                >
              </div>
            </b-form-group>
            <b-form-group>
              <b-list-group>
                <b-list-group-item
                  v-for="guest in eventLocal.extendedProps.guests"
                  :key="guest"
                  class="d-flex justify-content-between align-items-center"
                >
                  {{ guest }}
                  <feather-icon
                    icon="TrashIcon"
                    class="cursor-pointer"
                    @click="removeGuest(eventLocal.guest, eventLocal.extendedProps.guests)"
                  />
                </b-list-group-item>
              </b-list-group>
            </b-form-group>

            <!-- Textarea -->
            <b-form-group label="Description" label-for="event-description">
              <b-form-textarea
                placeholder="A note that will be shared with all participants"
                id="event-description"
                v-model="eventLocal.extendedProps.description"
              />
            </b-form-group>

            <!-- Form Actions -->
            <div class="d-flex mt-2">
              <b-button
                v-ripple.400="'rgba(255, 255, 255, 0.15)'"
                variant="primary"
                class="mr-2"
                type="submit"
                :disabled="eventLocal.title === '' || eventLocal.start === ''"
              >
                {{ eventLocal.id ? "Update" : "Add " }}
              </b-button>
              <b-button
                v-ripple.400="'rgba(186, 191, 199, 0.15)'"
                type="reset"
                variant="outline-secondary"
              >
                Reset
              </b-button>
            </div>
          </b-form>
        </validation-observer>
      </template>
    </b-sidebar>
  </div>
</template>

<script>
import {
  BSidebar,
  BForm,
  BFormGroup,
  BFormInput,
  BFormCheckbox,
  BAvatar,
  BFormTextarea,
  BButton,
  BListGroup,
  BListGroupItem,
  BFormInvalidFeedback,
} from "bootstrap-vue";
import vSelect from "vue-select";
import flatPickr from "vue-flatpickr-component";
import Ripple from "vue-ripple-directive";
import { ValidationProvider, ValidationObserver } from "vee-validate";
import { required, email, url } from "@validations";
import formValidation from "@core/comp-functions/forms/form-validation";
import { ref, toRefs } from "@vue/composition-api";
import useCalendarEventHandler from "./useCalendarEventHandler";

export default {
  components: {
    BButton,
    BSidebar,
    BForm,
    BFormGroup,
    BFormInput,
    BFormCheckbox,
    BFormTextarea,
    BAvatar,
    vSelect,
    flatPickr,
    ValidationProvider,
    BFormInvalidFeedback,
    BListGroup,
    BListGroupItem,
    ValidationObserver,
  },
  directives: {
    Ripple,
  },
  model: {
    prop: "isEventHandlerSidebarActive",
    event: "update:is-event-handler-sidebar-active",
  },
  props: {
    isEventHandlerSidebarActive: {
      type: Boolean,
      required: true,
    },
    event: {
      type: Object,
      required: true,
    },
    clearEventData: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      disableDates: {
        from: "1980-01-01",
        to: new Date() - 1,
      },
      required,
      email,
      url,
    };
  },
  methods: {
    addGuest(email, guestsList) {
      if (email) {
        guestsList.push(email);
        email = "";
      }
    },
    removeGuest(email, guestsList) {
      guestsList.splice(guestsList.indexOf(email), 1);
    },
    isValidEmail(email) {
      let emailRegex =
        /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
      return emailRegex.test(email);
    },
  },
  setup(props, { emit }) {
    /*
     ? This is handled quite differently in SFC due to deadlock of `useFormValidation` and this composition function.
     ? If we don't handle it the way it is being handled then either of two composition function used by this SFC get undefined as one of it's argument.
     * The Trick:

     * We created reactive property `clearFormData` and set to null so we can get `resetEventLocal` from `useCalendarEventHandler` composition function.
     * Once we get `resetEventLocal` function which is required by `useFormValidation` we will pass it to `useFormValidation` and in return we will get `clearForm` function which shall be original value of `clearFormData`.
     * Later we just assign `clearForm` to `clearFormData` and can resolve the deadlock. 😎

     ? Behind The Scene
     ? When we passed it to `useCalendarEventHandler` for first time it will be null but right after it we are getting correct value (which is `clearForm`) and assigning that correct value.
     ? As `clearFormData` is reactive it is being changed from `null` to corrent value and thanks to reactivity it is also update in `useCalendarEventHandler` composition function and it is getting correct value in second time and can work w/o any issues.
    */
    const clearFormData = ref(null);

    const {
      eventLocal,
      resetEventLocal,
      calendarOptions,

      // UI
      onSubmit,
    } = useCalendarEventHandler(toRefs(props), clearFormData, emit);

    const { refFormObserver, getValidationState, resetForm, clearForm } =
      formValidation(resetEventLocal, props.clearEventData);

    clearFormData.value = clearForm;

    return {
      // Add New Event
      eventLocal,
      calendarOptions,
      onSubmit,

      // Form Validation
      resetForm,
      refFormObserver,
      getValidationState,
    };
  },
};
</script>

<style lang="scss">
@import "@core/scss/vue/libs/vue-select.scss";
@import "@core/scss/vue/libs/vue-flatpicker.scss";

.guest-list-ctn {
  display: flex;
}
</style>
