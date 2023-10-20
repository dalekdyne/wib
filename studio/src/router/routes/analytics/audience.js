export default [
    {
        path: '/analytics/audience',
        name: 'analytics-audience',
        component: () => import('@/views/analytics/audience/Audience.vue'),
        meta: {
            pageTitle: 'Analytics Audience',
            breadcrumb: [
                {
                    text: 'Analytics',
                },
                {
                    text: 'Audience',
                    active: true,
                },
            ],
        },
    },
]
