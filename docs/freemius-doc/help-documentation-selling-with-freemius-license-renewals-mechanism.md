# The License Renewals Mechanism

All Freemius subscriptions are automatically renewed. When a renewal payment is successfully processed, the associated license will automatically be extended, based on the billing cycle. In case there's a delay with the renewal payment processing the license will be set to `Expired` mode until the renewal is processed.

When there's an issue processing the renewal payment, an [Automated Emails Dunning Campaign](https://freemius.com/help/help/documentation/marketing-automation/dunning-failed-payments/.md) will be triggered in order to recover the failed payment.

If the subscription is canceled prior to the automatic renewal, an automated emails campaign will be triggered, before the license expiration, using the following schedule:

* 30 days before license expiration
* 7 days before license expiration
* 2 days before license expiration
* 1 day after license expiration

Each email contains a secure direct link to renew the license.

If the customer renews the license prior to the expiration date, the license will be extended for an additional 30 or 365 days (based on their selected billing period). For example, if the license was renewed 5 days prior to the expiration, and the customer has chosen an annual billing cycle, the license will expire 370 days after the renewal date (5 days + 365 days).

## Manual License Renewal[​](#manual-license-renewal "Direct link to Manual License Renewal")

There's also an option to send a license renewal email manually from within the Freemius Developer dashboard. This can be done in two ways:

### Sending renewal email from Freemius[​](#sending-renewal-email-from-freemius "Direct link to Sending renewal email from Freemius")

* Go to the ***Licenses*** in the Developer Dashboard.
* Change the filter from *Active* to *All*.
  <!--$-->
  [](/help/videos/freemius-developer-dashboard-license-change-active-to-all.mp4)
  <!--/$-->
* Search for the relevant license key (using the license key or ID).
* Scroll horizontally to the preferred license and click the option icon (3 vertical dots) to get the options dropdown.
* Click the **Resend renewal email**. The process will be initiated to send the email to the customer from Freemius.
  <!--$-->
  [](/help/videos/freemius-developer-dashboard-license-send-manual-renewal.mp4)
  <!--/$-->

note

We only allow sending email for licenses:

* which are about to expire in 30 days and are associated with a subscription
* for expired licenses (These licenses must not be canceled i.e. the subscription is still active)
* for expired licenses with an active subscription.

This can happen if the payment method for the subscription has failed.

### Manually share renewal link[​](#manually-share-renewal-link "Direct link to Manually share renewal link")

Instead of the option above,

* Choose the **Copy renewal link** text to get the renewal URL into your clipboard.

  ![Freemius Developer Dashboard - Copy license renewal link](/help/assets/ideal-img/freemius-developer-dashboard-copy-license-renewal-link.b6d354e.480.png)
* Paste the renewal link on your preferred communication platform, then send the license owner for renewal.
