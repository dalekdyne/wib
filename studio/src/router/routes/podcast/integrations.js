export default [
    {
        path: '/podcast/availability',
        name: 'podcast-availability',
        component: () => import('@/views/podcast/availability/Availability.vue'),
        meta: {
            pageTitle: 'Podcast Availability',
            breadcrumb: [
                {
                    text: 'Podcast',
                },
                {
                    text: 'Availability',
                    active: true,
                },
            ],
        },
    },
]
