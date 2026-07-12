[Changelog](https://freemius.com/changelog/) / Changelog summary 29th August, 2023

### Freemius Checkout

We noticed that in the Brave browser, the credit card field of our checkout app would become hidden due to configuration. We pushed a fix and the checkout app will now work on the Brave browser regardless of the browser’s configuration.

### Improvements to the user email verification event

Your product will now receive the relevant `user.email.verified` event when a user verifies their email. You can process this event for marketing purposes.