Welcome to the last part of our planned run of four release notes 💃 Let’s face it, page builders and Gutenberg are the future of WordPress site-building, and I’m pleased to announce that we’re expanding our offering to help makers build momentum in that growing market\*.

*\*Keep your eyes peeled for an exciting article about template kits soon.*

We’ve also upgraded the deployment/PHP pre-processor. It now supports stripping comments with exclamation marks, the automatic removal of \*.po translation files, and Semantic Versioning 2.0! What’s more, we’ve introduced a special mechanism to notify you about email deliverability issues directly. Did I mention that one of our makers has found a clever way to boost 5-star WordPress.org reviews?

Let’s unpack the new features 💥

## Selling Static Products — Widgets, Templates, and Kits

The themes market is already shifting towards templates/kits, which are a combination of static assets and JSON config files. As a result, selling static software is growing in demand.

I’m excited to share you can now use Freemius to sell static software such as templates, widgets, kits, JavaScript libraries, etc. When you add a new product, you’ll notice two new product types that you can choose from:

![Creating Static Products - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2022/09/creating-static-products-freemius-developer-dashboard.png)

Static software is different from plugins and themes. There’s no SDK integration, and no ‘opt-in’ or usage tracking (no **Sites** section). While we still issue licenses, we don’t show license keys via email. Finally, as different types of static software have different install/setup/config instructions, we’ve introduced a new **INSTALL INSTRUCTIONS** tab under the **Emails** section to let you define the instructions that will appear in the after-purchase email and the User Dashboard.

![Email Installation Instruction Settings - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2022/09/email-installation-instruction-settings-freemius-developer-dashboard.png)

## Deployment/PHP Pre-processor

### Stripping Comments with Exclamation Marks

We learned that many JS and CSS minifiers and obfuscators will use the exclamation mark as a quick directive to skip stripping comments. To make it easier to retain comments before deploying to Freemius, we now also support stripping comments with an exclamation mark:

`/*! <fs_premium_only> */`

`//! <fs_premium_only>`

In addition, we removed the replacement comment `/* Premium Code Stripped by Freemius */` to keep your CSS/JS tidy.

### Removing \*.po Translation Files

If you are adding the SDK with composer, or other methods that don’t strip the \*.po translation files from the WordPress SDK, the deployment process now automatically removes these source files. This significantly reduces the size of your source code by ~2MB (~0.5MB from ZIP).

### Semantic Versioning 2.0 Support

I am super excited to share that Freemius supports [Semantic Versioning 2.0](help-documentation-release-management.md) for releases 🥳️ It’s been a long wait, and pretty challenging to tackle efficiently, but we finally made it happen 🤓

You can now start tagging your releases with alpha, beta, rc, and much more! View the full documentation [here](help-documentation-release-management.md).

## Emails Deliverability

Freemius uses SendGrid for sending transactional emails to users and customers. While their deliverability performance is outstanding, emails may not be delivered to your users’ mailboxes from time to time. When it comes to mission-critical emails, like a MAP email (Mail After Purchase), this can lead to legitimate frustration at best, a refund request, or — worst-case scenario — a chargeback.

To battle this, we’ve integrated with SendGrid’s webhooks mechanism to notify your support mailbox in the event that an email bounces, defers, or drops. The email will include the error message returned from the email server and a copy of the original message that was sent:

![Freemius Deliverability Issue Email Notification](https://freemius.com/blog/wp-content/uploads/2022/09/freemius-deliverability-issue-email-notification.png)

This allows you to proactively and easily contact the customer with all the necessary details by simply forwarding them the email. And even if you don’t offer the necessary support for handling the issue, at least they’ll be aware of it.

To reflect the deliverability status of a customer, a warning icon will appear in the **Users** table next to users with deliverability issues:

![User Deliverability Status Icon - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2022/09/user-deliverability-status-icon-freemius-developer-dashboard.png)

If you don’t have the capacity to handle these emails or don’t want to receive these messages for whatever reason, you can turn them off in your **Notification** center in the Developer Dashboard:

[![Email-Deliverability-Notification-Center-Freemius-Developer-Dashboard](https://freemius.com/blog/wp-content/uploads/2022/09/Email-Deliverability-Notification-Center-Freemius-Developer-Dashboard.png)](https://freemius.com/blog/wp-content/uploads/2022/09/Email-Deliverability-Notification-Center-Freemius-Developer-Dashboard.png)

## Boost WordPress.org 5-Star Reviews

To help you boost reviews on WordPress.org, an automated personal “thank you” email will now be sent to customers 15–30 minutes after leaving a 5-star [review through Freemius](help-documentation-marketing-automation-reviews.md). This email will ask them to submit the same review on WordPress.org:

![WordPress.org Review Request Email Example](https://freemius.com/blog/wp-content/uploads/2022/09/wordpress-org-review-request-email-example.png)

**Note:** This is only applicable for freemium plugins/themes that have a free version on WordPress.org.

Thanks [Brandon](https://twitter.com/brand_on_fire) for the feature suggestion!

If for some reason you don’t like 5-star reviews 😉 and wish to disable them, you can do that in the **Notifications** center.

![WordPress.org Review Notification - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2022/09/wordpress-org-review-notification-freemius-developer-dashboard.png)

## What’s next?

Phew 😅 We’ve covered a lot of new things in the last eight months and there are many new features coming soon, including:

- Taking the Multi-store Developer Dashboard out of Beta with our shiny new analytics.
- Major improvements in the WordPress SDK’s UI and UX.
- Searching affiliates in the Developer Dashboard.
- Custom Terms & Conditions.
- Protection against overriding releases.

There are exciting times ahead — see you soon!