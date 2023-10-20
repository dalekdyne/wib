import mock from '@/@fake-db/mock'
/* eslint-disable global-require */
const data = {
  congratulations: {
    name: 'John',
    saleToday: '57.6',
  },
  subscribersGained: {
    series: [
      {
        name: 'Subscribers',
        data: [28, 40, 36, 52, 38, 60, 55],
      },
    ],
    analyticsData: {
      subscribers: 92600,
    },
  },
  ordersRecevied: {
    series: [
      {
        name: 'Orders',
        data: [10, 15, 8, 15, 7, 12, 8],
      },
    ],
    analyticsData: {
      orders: 38400,
    },
  },
  avgSessions: {
    sessions: 2700,
    lastDays: ['Last 28 Days', 'Last Month', 'Last Year'],
    growth: '+5.2%',
    goal: 100000,
    users: 100000,
    retention: 90,
    duration: 1,
    salesBar: {
      series: [
        {
          name: 'Sessions',
          data: [75, 125, 225, 175, 125, 75, 25],
        },
      ],
    },
  },
  supportTracker: {
    title: 'Support Tracker',
    lastDays: ['Last 28 Days', 'Last Month', 'Last Year'],
    totalTicket: 163,
    newTicket: 29,
    openTicket: 63,
    responseTime: 1,
    supportTrackerRadialBar: {
      series: [83],
    },
  },
  timeline: [
    {
      id: 1,
      title: 'Interview with John',
      description: 'Invoices have been paid to the company.',
      status: "Scheduled",
      date: "2020-01-01",
    },
    {
      id: 2,
      title: 'Interview with John',
      description: 'Invoices have been paid to the company.',
      status: "Published",
      date: "2020-01-01",
    },
    {
      id: 3,
      title: 'Interview with John',
      description: 'Invoices have been paid to the company.',
      status: "Published",
      date: "2020-01-01",
    },
    {
      id: 4,
      title: 'Interview with John',
      description: 'Invoices have been paid to the company.',
      status: "Scheduled",
      date: "2020-01-01",
    },
  ],
  salesChart: {
    series: [
      {
        name: 'Sales',
        data: [90, 50, 86, 40, 100, 20],
      },
      {
        name: 'Visit',
        data: [70, 75, 70, 76, 20, 85],
      },
    ],
  },
  appDesign: {
    date: '03 Sep, 20',
    title: 'App design',
    subtitle: 'You can Find Only Post and Quotes Related to IOS like ipad app design, iphone app design',
    teams: [
      { name: 'Figma', color: 'light-warning' },
      { name: 'Wireframe', color: 'light-primary' },
    ],
    members: [
      { img: require('@/assets/images/portrait/small/avatar-s-9.jpg'), color: 'primary' },
      { text: 'PI', color: 'light-danger' },
      { img: require('@/assets/images/portrait/small/avatar-s-14.jpg'), color: 'primary' },
      { img: require('@/assets/images/portrait/small/avatar-s-7.jpg'), color: 'primary' },
      { text: 'AL', color: 'light-secondary' },
    ],
    planing: [
      { title: 'Due Date', subtitle: '12 Apr, 21' },
      { title: 'Budget', subtitle: '$49251.91' },
      { title: 'Cost', subtitle: '$840.99' },
    ],
  },
}
/* eslint-disable global-require */
mock.onGet('/analytics/data').reply(() => [200, data])
