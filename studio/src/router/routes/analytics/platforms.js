export default [
    {
        path: '/analytics/platforms',
        name: 'analytics-platforms',
        component: () => import('@/views/analytics/platforms/Platforms.vue'),
        meta: {
            pageTitle: 'Platform Analytics',
            breadcrumb: [
                {
                    text: 'Analytics',
                },
                {
                    text: 'Platforms',
                    active: true,
                },
            ],
        },
    },
]
