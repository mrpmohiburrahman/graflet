[Changelog](https://freemius.com/changelog/) / Customize Key Transactional Emails with Custom Content

This week we are releasing a feature requested by many of our makers. Freemius sends various [transactional emails](help-documentation-marketing-automation-transactional-emails.md#purchase-payment-and-subscription-emails) to your customers. For example, when someone purchases a subscription (or lifetime access), they receive an email with all the plan and pricing details. Similarly, customers are notified when subscriptions are renewed.

So far, all these emails were fully controlled by Freemius. While they are already fine-tuned and optimized for your buyers, we understood that having some level of customization can significantly improve your software integration and onboarding experience. For example:

1. A [SaaS or App](help-documentation-saas.md) product can include a short introduction and links to help users get started immediately.
2. A [WordPress](help-documentation-wordpress.md) product may include or link to usage instructions or next steps after activation.

With this in mind, we are deploying a feature this week that lets you do exactly that. You can now add a custom section to the following emails:

1. New Subscription Email
2. New Lifetime Purchase Email
3. Subscription Renewal Email

### Adding Custom Content to the Emails

Simply go to **Emails** → **Customization**, where you will find a new section named **Specific Email Customization**.

[![Freemius Developer Dashboard for Email Customization](https://freemius.com/blog/wp-content/uploads/2026/02/email-customization-freemius-developer-dashboard-1024x925.png)](https://freemius.com/blog/wp-content/uploads/2026/02/email-customization-freemius-developer-dashboard.png)

From there, select the email you want to customize and add a new section by defining its title and content.

The content area supports Markdown for basic formatting, and you can include custom links as needed. A live preview of the email is available below the form so you can verify exactly how it will appear to your buyers.

[![Email Preview with Custom Section](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-new-subscription-email-with-custom-section-1024x625.png)](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-new-subscription-email-with-custom-section.png)

We believe this will help you better align transactional emails with your product’s onboarding and user journey. If you have any feedback, please let us know via the [feature request](https://freemius.nolt.io/) board.