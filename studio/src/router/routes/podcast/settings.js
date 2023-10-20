export default [
    {
        path: '/podcast/settings',
        name: 'podcast-settings',
        component: () => import('@/views/podcast/settings/PodcastSettings.vue'),
        meta: {
            pageTitle: 'Podcast Settings',
            breadcrumb: [
                {
                    text: 'Podcast',
                },
                {
                    text: 'Settings',
                    active: true,
                },
            ],
        },
    },
]
