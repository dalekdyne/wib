export default [
    {
        path: '/analytics/overview',
        name: 'analytics-overview',
        component: () => import('@/views/analytics/overview/Overview.vue'),
        meta: {
            pageTitle: 'Analytics Overview',
            breadcrumb: [
                {
                    text: 'Analytics',
                },
                {
                    text: 'Overview',
                    active: true,
                },
            ],
        },
    },
]
