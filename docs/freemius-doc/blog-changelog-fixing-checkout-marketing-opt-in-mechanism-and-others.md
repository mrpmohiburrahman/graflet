[Changelog](https://freemius.com/changelog/) / Fixing checkout marketing opt-in mechanism and others

## Marketing Opt-In UI in the checkout

We noticed in some cases the marketing UI was defaulting to “No” instead of asking the user about their choice.

[![Freemius Checkout Marketing Opt-In UI](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-marketing-opt-in-ui.png)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-marketing-opt-in-ui.png)

We fixed this regression. Now the UI will be in an indeterminate state, making the customer choose their preference.

[![Freemius Checkout Marketing Opt-In Indeterminate UI](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-marketing-opt-in-indeterminate-ui.png)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-checkout-marketing-opt-in-indeterminate-ui.png)

## Fixing `user.created` event

We noticed in some edge cases the event was not fired. We figured out the root cause and have pushed a fix.

## Regression in subscription cancellation email

We noticed some regression in the [modification](blog-changelog-fixed-user-notes-in-the-developer-dashboard-and-misc-improvements.md) we made in the subscription cancellation email to have its `replyTo` set to the user instead of Freemius. We have reverted the change for the time being. We will investigate the issue and fix it in the near future.