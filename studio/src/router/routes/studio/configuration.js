export default [
    {
        path: '/studio/configuration',
        name: 'studio-configuration',
        component: () => import('@/views/studio/configuration/Configuration.vue'),
        meta: {
            pageTitle: 'Studio Configuration',
            breadcrumb: [
                {
                    text: 'Studio',
                },
                {
                    text: 'Configuration',
                    active: true,
                },
            ],
        },
    },
]
