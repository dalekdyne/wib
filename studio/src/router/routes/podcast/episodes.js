export default [
    {
        path: '/podcast/episodes',
        name: 'podcast-episodes',
        component: () => import('@/views/podcast/episodes/list/Episodes.vue'),
        meta: {
            pageTitle: 'Podcast Episodes',
            breadcrumb: [
                {
                    text: 'Podcast',
                },
                {
                    text: 'Episodes',
                    active: true,
                },
            ],
        },
    },
    {
        path: '/podcast/episodes/:id',
        name: 'podcast-episodes-id',
        component: () => import('@/views/podcast/episodes/single/EpisodeSingle.vue'),
        meta: {
            pageTitle: 'Podcast Episode',
            breadcrumb: [
                {
                    text: 'Podcast',
                },
                {
                    text: 'Episode',
                    active: true,
                },
            ],
        },
    },
    {
        path: '/podcast/episodes/:id/edit',
        name: 'podcast-episodes-id-edit',
        component: () => import('@/views/podcast/episodes/edit/EpisodeEdit.vue'),
        meta: {
            pageTitle: 'Edit Episode',
            breadcrumb: [
                {
                    text: 'Episode',
                },
                {
                    text: 'Edit',
                    active: true,
                },
            ],
        },
    }

]
