import mock from '@/@fake-db/mock'
/* eslint-disable global-require */
const data = {
  accountSetting: {
    general: {
      avatar: require('@/assets/images/portrait/small/avatar-s-11.jpg'),
      username: 'johndoe',
      fullName: 'John Doe',
      email: 'granger007@hogward.com',
    },
    notification: {
      upcomingInterview: true,
      scheduledPodcastPublished: true,
      deletedCalendarEvent: true,
    },
    userdata: {
      enabled: true,
    },
    dangerZone: {
      enabled: true,
    },
  },
}
/* eslint-disable global-require */
mock.onGet('/user').reply(() => [200, data.accountSetting])
