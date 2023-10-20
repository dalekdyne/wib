import mock from './mock'

/* eslint-disable import/extensions */

// JWT
import './jwt'

// Table
import './data/card/card-statistics'
import './data/card/card-analytics'

// Apps
import './data/apps/calendar'

// dashboard
import './data/dashboard/analytics'
import './data/dashboard/ecommerce'

// pages
import './data/pages/faq-data'
import './data/pages/pricing-data'
import './data/pages/users'
/* eslint-enable import/extensions */

mock.onAny().passThrough() // forwards the matched request over network
