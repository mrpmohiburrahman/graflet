[Changelog](https://freemius.com/changelog/) / CCing payment emails to user billing address

Freemius sends various payment-related emails to the users. For example

- When a new subscription is made.
- When a renewal of a subscription happens.
- When a refund is issued.

We have been sending the emails to the primary address of the user.

The users can also have a different “Billing Address” defined through the [Customer Portal](help-documentation-users-account-management.md).

[![](https://freemius.com/blog/wp-content/uploads/2024/09/user-billing-freemius-user-dashboard-1024x451.png)](https://freemius.com/blog/wp-content/uploads/2024/09/user-billing-freemius-user-dashboard.png)

To make the user experience better, we are now CCing such emails to the billing email too. For example, if the address of the user is `[email protected]` and the billing email is set as `[email protected]`, Freemius will now send payment-related emails to both addresses.