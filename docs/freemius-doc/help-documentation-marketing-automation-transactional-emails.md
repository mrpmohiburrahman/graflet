This guide provides an overview of all the automated transactional and marketing emails that Freemius sends on behalf of your product to your customers.

This guide covers:

- The [types of transactional emails](#types-of-transactional-emails).
- How to [view email history and content](#view-email-history).
- How to [customize the notifications](#email-notification-customization).

## Types of Transactional Emails[​](#types-of-transactional-emails "Direct link to Types of Transactional Emails")

### Purchase, Payment, and Subscription Emails[​](#purchase-payment-and-subscription-emails "Direct link to Purchase, Payment, and Subscription Emails")

- After subscription / purchase confirmation
- Payment
- Refund
- Subscription cancellation
- Annual subscription renewal reminder (30 days before an upcoming renewal)

### Trial Emails[​](#trial-emails "Direct link to Trial Emails")

- Trial started
- Trial about to expire (sent 2 days before expiration)
- Trial expired
- Trial canceled

## Marketing Automation Emails[​](#marketing-automation-emails "Direct link to Marketing Automation Emails")

- [Cart abandonment recovery - 3 emails](help-documentation-marketing-automation-cart-abandonment-recovery.md).
- [Manual license renewal - 4 emails](help-documentation-selling-with-freemius-license-renewals-mechanism.md) (if license was [migrated](help-documentation-migration.md) from another platform or subscription was canceled).
- [Dunning - 4 emails](help-documentation-marketing-automation-dunning-failed-payments.md).
- Immediate uninstall feedback (if user opted-in and then uninstalled in less than 60 min without providing an uninstall reason).
- [Review request](help-documentation-marketing-automation-reviews.md#verified-buyer-reviews) - sent to customers a week after the purchase.

## Other Automation Emails[​](#other-automation-emails "Direct link to Other Automation Emails")

- Email confirmation after a user opts-in.
- Installation ownership change.

## View Email History[​](#view-email-history "Direct link to View Email History")

This feature is a great way to verify that the emails Freemius sends on your behalf are being delivered as expected and to review their content.

To view a specific email:

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com).
2. Navigate to the ***Emails*** page.
3. Then open the **Email History** tab.
4. In the list of emails Freemius has sent on behalf of your product, click to select any row to view the details of that email. This will open up a modal with the email details, email content in either HTML or plain text format which can be reviewed.

Email Content Availability

Email content is available for 7 days after the email is sent. After that, only the email metadata will be available in the email history.

## Email Notification Customization[​](#email-notification-customization "Direct link to Email Notification Customization")

While many of the email notifications are mandatory to inform the product owners and customers about purchases and deductions made to customers' cards and bank accounts, several notifications can be enabled or disabled by toggling a checkbox.

These notifications are related to:

- [Affiliate program](help-documentation-affiliate-platform.md)
- [Trial subscriptions](help-documentation-wordpress-free-trials.md)
- [Ratings & reviews](help-documentation-marketing-automation-reviews.md)
- [Earnings & Payouts](help-documentation-selling-with-freemius-your-earnings.md#how-freemius-notifies-you-about-payouts)
- Weekly reports and many more options.

To access the controls to enable/disable the notifications:

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Click the profile icon in the top-right corner of the screen.
3. Select **Notifications** from the dropdown options.
4. Toggle the checkbox to disable or enable sending optional notifications.

Custom Notifications

If you wish to use your own email service providers, then you can use our [events and webhooks](help-documentation-saas-events-webhooks.md) system to trigger the custom notifications and disable the configurations from Freemius.

## Further Customization Options[​](#further-customization-options "Direct link to Further Customization Options")

- You can add [custom content](https://freemius.com/help/documentation/emails/email-content-customization/) in your transactional emails, such as a custom message, links to your support and documentation, and more.
- You can set up [Sender and reply-to email addresses](https://freemius.com/help/documentation/emails/email-settings/) to reflect your brand.
- To improve email deliverability you can configure [SPF and/or DKIM records](https://freemius.com/help/documentation/emails/email-deliverability/) for your domain.