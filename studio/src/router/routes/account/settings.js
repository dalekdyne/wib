export default [
  {
    path: '/account/settings',
    name: 'account-settings',
    component: () => import('@/views/account/settings/AccountSettings.vue'),
    meta: {
      pageTitle: 'Account Settings',
      breadcrumb: [
        {
          text: 'Account',
        },
        {
          text: 'Settings',
          active: true,
        },
      ],
    },
  },
]
