import mock from '@/@fake-db/mock'
/* eslint-disable global-require */
const data = {
  faqData: {
    // payment
    payment: {
      icon: 'CreditCardIcon',
      title: 'Payment',
      subtitle: 'Which plan is best for me?',
      qandA: [
        {
          question: 'Does my subscription automatically renew?',
          ans:
            'Yes, your subscription will automatically renew at the end of your billing cycle. You can cancel your subscription at any time.',
        },
        {
          question: 'How do I cancel my subscription?',
          ans:
            'You can cancel your subscription at any time. To cancel your subscription, go to your account settings and click on the “Cancel Subscription” button.',
        },
        {
          question: 'How do I change my payment method?',
          ans:
            'You can change your payment method at any time. To change your payment method, go to pricing settings and click on the “Change Payment Method” button.',
        },
        {
          question: 'Can I get a refund?',
          ans:
            'You can send an email to payments@podbeam.io and let us know the reason for your refund request. We will review your request and get back to you within 24 hours.',
        },
      ],
    },
    // account
    account: {
      icon: 'UserIcon',
      title: 'Account',
      subtitle: 'How do I manage my account?',
      qandA: [
        {
          question: 'How do I change my password?',
          ans:
            'You can change your password at any time. To change your password, go to your account settings and click on the “Change Password” button.',
        },
        {
          question:
            'How do I change the email address associated with my account?',
          ans:
            'You can change the email address associated with your account at any time. To change your email address, go to your account settings and click on the “Change Email Address” button.',
        },
        {
          question: 'How do I delete my account?',
          ans:
            'You can delete your account at any time. To delete your account, go to your account settings and click on the “Delete Account” button. This is a permanent action and cannot be undone.',
        },
      ],
    },
    // recording
    recording: {
      icon: 'MicIcon',
      title: 'Recording',
      subtitle: 'How do I record a podcast?',
      qandA: [
        {
          question: 'How do I record a podcast?',
          ans:
            'You start by either scheduling a recording session or starting a recording session immediately. You can schedule a recording session by clicking on the “Schedule podcast” button on the "Calendar" page under "Studio". You can start a recording session immediately by clicking on "Start instant recording" button on the "Create" page under "Studio".',
        },
        {
          question: 'Does the recording session automatically record the audio and video of all participants?',
          ans:
            'Yes, the recording session automatically records the audio and video of all participants.',
        },
        {
          question: 'Why doesn\’t the recording session show up when I end the session?',
          ans:
            'It takes a few minutes for the recording session to show up on the "Episodes" page under "Podcast" as a "Draft" episode.',
        },
        {
          question: 'How do I edit the recording session?',
          ans:
            'You can download the recording session from the "Episodes" page under "Podcast" and edit it on your computer. You can then upload the edited recording session to the "Episodes" page under "Podcast" to publish it. You can also include options as fade-in or fade-out, change the background image or add an intro and outro to the recording session in the "Configuration" page under "Studio". ',
        },
      ],
    },
    // publishing
    publishing: {
      icon: 'GlobeIcon',
      title: 'Publishing',
      subtitle: 'How do I publish a podcast?',
      qandA: [
        {
          question: 'How do I publish a podcast?',
          ans:
            'You can either publish a podcast immediately or schedule a podcast to be published at a later date. You can publish a podcast immediately by clicking on the "Publish" button on the "Edit Episode" page under "Podcast". You can schedule a podcast to be published at a later date by clicking on the "Schedule" button on the "Edit episode" page under "Podcast".',
        },
        {
          question: 'Where will my podcast be published?',
          ans:
            'Your podcast will be published on all major podcast platforms such as Apple Podcasts, Google Podcasts, Spotify, and more. You can see all the integrations on the "Availability" page under "Podcast".',
        },
        {
          question: 'Will you publish the video of the podcast episode on YouTube?',
          ans:
            'Yes, we will publish the video of the podcast episode on YouTube if you have enabled the integration. You can see the YouTube channel on the "Availability" page under "Podcast". We will publish the audio version of your podcast on platforms that don\’t support video.',
        }
      ],
    },
    // product and services
    product: {
      icon: 'PackageIcon',
      title: 'Product',
      subtitle: 'What is Podbeam?',
      qandA: [
        {
          question: 'What is Podbeam?',
          ans:
            'Podbeam is a video podcasting platform that allows you to record, edit, and publish your podcast. You can also manage your podcast and your audience on Podbeam.',
        },
        {
          question: 'What is a video podcast?',
          ans:
            'A video podcast is a podcast that includes video. You can record a video podcast on Podbeam and publish it on all major podcast platforms such as Apple Podcasts, Google Podcasts, Spotify, and more.',
        },
      ],
    },
  },
}

mock.onGet('/faq/data').reply(config => {
  const { q = '' } = config.params
  const queryLowered = q.toLowerCase()

  const filteredData = {}

  Object.entries(data.faqData).forEach(entry => {
    const [categoryName, categoryObj] = entry
    // eslint-disable-next-line arrow-body-style
    const filteredQAndAOfCategory = categoryObj.qandA.filter(qAndAObj => {
      return qAndAObj.question.toLowerCase().includes(queryLowered)
    })
    if (filteredQAndAOfCategory.length) {
      filteredData[categoryName] = { ...categoryObj, qandA: filteredQAndAOfCategory }
    }
  })

  return [200, filteredData]
})
