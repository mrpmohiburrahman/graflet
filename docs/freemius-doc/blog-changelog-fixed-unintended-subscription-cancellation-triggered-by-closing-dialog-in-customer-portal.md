[Changelog](https://freemius.com/changelog/) / Fixed: Unintended Subscription Cancellation Triggered by Closing Dialog in Customer Portal

We discovered an edge case bug where closing the subscription cancellation dialog in the [Customer Portal](help-documentation-users-account-management.md) could incorrectly trigger the cancellation API call.

[![Cancel Subscription from Freemius Customer Portal](https://freemius.com/blog/wp-content/uploads/2025/07/customer-portal-subscription-cancellation-1024x733.png)](https://freemius.com/blog/wp-content/uploads/2025/07/customer-portal-subscription-cancellation.png)

We have identified the root cause and have issued a fix. Now, simply closing the dialog will not result in any unwanted cancellation actions.