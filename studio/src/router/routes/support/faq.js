export default [
    {
        path: '/support/faq',
        name: 'support-faq',
        component: () => import('@/views/support/faq/Faq.vue'),
        meta: {
            pageTitle: 'FAQ',
            breadcrumb: [
                {
                    text: 'Support',
                },
                {
                    text: 'FAQ',
                    active: true,
                },
            ],
        },
    },
]
