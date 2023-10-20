export default [
    {
        path: '/studio/create',
        name: 'studio-create',
        component: () => import('@/views/studio/create/Create.vue'),
        meta: {
            pageTitle: 'Create',
            breadcrumb: [
                {
                    text: 'Studio',
                },
                {
                    text: 'Create',
                    active: true,
                },
            ],
        },
    },
]
