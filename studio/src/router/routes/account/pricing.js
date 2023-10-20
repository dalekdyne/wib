export default [
  {
    path: '/account/pricing',
    name: 'account-pricing',
    component: () => import('@/views/account/pricing/Pricing.vue'),
    meta: {
      pageTitle: 'Account Pricing',
      breadcrumb: [
        {
          text: 'Account',
        },
        {
          text: 'Pricing',
          active: true,
        },
      ],
    },
  },
]
