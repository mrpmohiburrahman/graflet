[Changelog](https://freemius.com/changelog/) / Deployment summary: 30 April, 2023

### Backend Changes

- Following a suggestion from a maker, we’re now logging a new event called `user.billing.tax_id.updated`. This event is logged when either the developer or the user changes the tax ID associated with the user’s billing. If you need to sync your own system with the changes in the tax ID of a user, you [can hook into this event](help-documentation-marketing-automation-events-webhooks.md) from the [Developer Dashboard](https://dashboard.freemius.com/).
- We fixed some SEO-related issues in our blog.

### User Dashboard Changes

Following user complaints, we’ve added a password visibility button in the User Dashboard’s ‘login’ form and the ‘change password’ form.

[![](https://freemius.com/blog/wp-content/uploads/2023/04/password-visibility-toggle-ui.jpg)](https://freemius.com/blog/wp-content/uploads/2023/04/password-visibility-toggle-ui.jpg)

This helps our users determine if the password is correct when trying to log in.