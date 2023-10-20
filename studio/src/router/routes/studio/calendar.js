export default [
    {
        path: '/studio/calendar',
        name: 'studio-calendar',
        component: () => import('@/views/studio/calendar/Calendar.vue'),
        meta: {
            pageTitle: 'Studio Calendar',
            breadcrumb: [
                {
                    text: 'Studio',
                },
                {
                    text: 'Calendar',
                    active: true,
                },
            ],
        },
    },
]
