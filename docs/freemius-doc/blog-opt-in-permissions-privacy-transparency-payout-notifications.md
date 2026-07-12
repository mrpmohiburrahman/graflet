We’re excited to share our latest WordPress SDK and platform upgrades with the community! Of particular note is that we’ve taken significant steps in being more flexible and transparent about data collection, including changes to the Freemius “opt-in” mechanism. We also added the ability to easily transfer account ownership, improved the checkout functionality, and added more features for your users in the Customer Portal.

For easy reading, here’s a clickable list 😉

- [WordPress SDK 2.3.2](#sdk)
- [Pending Affiliate Payouts Notifications](#affiliate)
- [Payout Notifications](#payout)
- [Checkout](#checkout)
- [Customer Portal](#userdashboard)
- [Deployment](#deployment)
- [Developer Dashboard](#dashboard)

### Opt-in Permission Enhancements

In the past year, we received a healthy amount of criticism accusing Freemius of being some sort of spyware. The ironic thing about this is that competing eCommerce products collect almost the same data that Freemius does after activating a license key. Even more ironic is that we have the most transparent opt-in and license activation forms that explain exactly what is collected, when, and how, so it’s naturally much easier to criticize what can be seen 🙂

The WordPress ecosystem is a “wild-west” when it comes to data collection and opt-in permissions. Competing solutions don’t have a consistent approach for developers to obtain legal approval for data sharing of their user information. With our opt-in process, we’re increasing transparency and privacy controls, so, if you know or use Freemius, you already know that all of these allegations have nothing to do with reality. Regardless, since this is a recurring issue, we’ve decided to make some changes to address the concerns raised by some community members.

#### Opting out from data collection in paid product versions

One of the main concerns raised by users is that there’s no option to opt-out from data tracking when using paid products integrated with Freemius. That was indeed the case by design. We believe that receiving update notifications and the ability to upgrade a plugin/theme version directly through the WP Admin are essential capabilities. If a user misses a security update, their site can be at risk. Regardless of our explanation, some users don’t seem to agree with us, so we decided to end this fiasco and expose the opt-out option in paid products. We made sure to add a clear warning explaining why ongoing connectivity with the licensing and updates engine is essential, leaving the decision up to the user:

![Freemius WordPress SDK - Out Out Dialog](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-wordpress-sdk-out-out-dialog.png)

#### Opting in/out from tracking installed plugins and themes

A while ago, we enriched the SDK to track basic info about installed plugins and themes for opted-in users. The goal was to also enrich the Developer Dashboard with insights about plugins and themes that are commonly used with your product to empower you with data to help you make sure your product is compatible with the top plugins/themes it’s commonly used with. This would have multiple benefits, including helping you in handling support more efficiently (e.g if you know your product is not working with one of the user’s installed products, you can respond more effectively to the ticket), and for other business reasons like establishing [collaborations and partnerships](blog-recommending-bundling-plugins-themes.md). Unfortunately, we never had the chance to complete the indexing and visualization of this data as we kept prioritizing other features, so it does not yet appear in the Developer Dashboard.

In the last few months, we’ve received numerous support requests from users and developers asking for a way to disable this type of data collection. Once we realized that tracking plugins and themes can be problematic for some users, we quickly introduced a workaround with two special defines (\`WP\_FS\_\_TRACK\_PLUGINS\` and \`WP\_FS\_\_TRACK\_THEMES\`), allowing admins to turn the plugin and theme tracking off by setting the defines to \`false\` in the \`wp-config.php\` or \`functions.php\` files. That solved the problem for some time, but wasn’t good enough.

I’m excited to share that the new SDK release comes with enriched opt-in and license activation forms that easily allow users to control the tracking of plugins and themes. Plugin & theme tracking has been moved to a standalone permission that can now be selectively enabled/disabled during opt-in and license activation:

![Freemius WordPress SDK - Opt-In Permissions](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-wordpress-sdk-opt-in-permissions.png)

The opt-out dialog has also been enriched, so users that already opted-in will be able to disable plugin & theme tracking without completely opting out.

#### Collaborative Privacy Document

We have compiled and thoroughly addressed all the privacy and data tracking concerns we’ve heard about Freemius over the years into a [single document](https://github.com/Freemius/data-concerns-faq) on Github. The goal is to have a public document that you’ll be able to reference when any of your users have privacy concerns related to Freemius. We are going to maintain the document “source” on GitHub, making it collaborative and keeping the editing process and versioning transparent to show we have nothing to hide. By leveraging the power of our entire network, we’ll be able to enrich and craft a much more accurate document that addresses everyone’s concerns. You’ll also be able to submit PRs with questions and concerns that we may have missed or issues that may be raised in the future.

If you’d like to help us resharp the document, please check it out [here](https://github.com/Freemius/data-concerns-faq).

You are welcome to branch it and submit a PR with your suggestions.

### Account User Change

In previous versions of the SDK, when a user-activated a license key for a freemium product after they had previously opted into usage-tracking in the free version, the Account page in the WP Admin would remain associated with the information of the user that opted into the free version, regardless whether or not the license belonged to the same user or if it was a “foreign license” that was purchased under a different account. This logic was created by design, allowing larger organizations to keep billing issues separate from their development teams.

Following the recent migration of OceanWP to Freemius, we had the opportunity to work with a very large customer base of agencies and freelancers – people who are building websites for clients. In many cases, agencies will buy paid plugins and themes needed for a project and will continue maintaining the website for some period after it’s completed. So, if the client installed the free plugin/theme version and opted into its usage-tracking, the client’s account remained associated with the installation and the agency couldn’t see nor maintain the website from their Customer Portal, even if they purchased the license for the paid product version. We discovered that users find this behavior confusing, leading to support tickets asking us to switch the user associated with the installation to the license owner.

We solved this problem by adding a special mechanism where users can now easily transfer the ownership of the Account and the product install to the license owner.

When a “foreign license” is activated, you’ll notice a new ***Change User*** button next to the ***User ID***. Clicking it will open a dialog box that shows a list of masked email addresses associated with the account. You can now simply choose the email associated with the user you want to transfer the ownership of the account to and click the ***I Agree – Change User*** button to complete the transfer:

![Freemius WordPress SDK - Account User Change](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-wordpress-sdk-account-user-change.gif)

In the case of a product with add-ons, there could be multiple email addresses displayed when there are multiple add-ons that were activated with licenses that belong to different owners.

We also enriched the license change/update dialog box so that when entering a license key that is associated with a different owner, a new checkbox will be dynamically displayed allowing you to associate the account with the license owner:

![Freemius WordPress SDK - Associate Account with License Owner](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-wordpress-sdk-associate-account-with-license-owner.png)

Please note: Due to the complexity of the logic to support this capability, the initial release does not support changing the user on the network-level Account page for multisite networks. That use-case will be supported at a later stage.

## Pending Affiliate Payouts Notifications

If you are using Freemius Affiliate Platform, previously you had to remember to login to the dashboard and check if there are any pending payouts on the 10th of the month. We introduce a new email that will notify you proactively about pending payouts.

**Tip:** If they want to rely on those emails, make sure you whitelist emails coming from “\*@freemius.com” to skip spam.

![pending affiliate payout email notification](https://freemius.com/blog/wp-content/uploads/2020/03/word-image.png)

## Payout Notifications

Another super-helpful email that many of you have been asking for, and we are excited to deliver! Once we process a payout, you will now receive a complete breakdown of the payout covering your net, our rev-share, the gateway fees, EU VAT, and more:

![sample payout breakdown from Freemius](https://freemius.com/blog/wp-content/uploads/2020/03/word-image-1.png)

## Checkout

### Attributing Sales to Affiliates Without Affiliate Links

Freemius Checkout has a new `affiliate_user_id` parameter that allows you to bind the Buy Button to specific affiliates. This means you can now partner with affiliates to sell your products directly through their site without using an affiliate link.

### Checkout Performance Optimization

We’ve optimized the Checkout’s performance by reducing load speed by an avg. of 1.5 sec. Since we are dealing with eCommerce, it’s vital that all the loaded resources are up to date, bypassing any potential caching layers on the way (CDN, ISP, browser caching). We discovered how we can optimize that mechanism to force the Checkout to only call new files when we release updates, so now we are leveraging different layers of caching to serve the checkout’s static files.

### Checkout Optional Phone Number

Following requests from some of our makers, we introduced an optional phone number field. We designed it to display reactively after users enter their email and name along with the email confirmation field:

![Freemius Checkout - Phone number field](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-checkout-phone-number-field.gif)

We’ll keep tracking the impact of the additional field on the conversion rate and may adjust it to not load by default.

### Checkout Payment Method Update

We introduced a new `is_payment_method_update` parameter. When it’s set to `true` and provided with a context `license_key`, the checkout will be loaded in a special mode for allowing customers to update the payment method associated with their subscription. Here’s how an update link can look like:

`https://checkout.freemius.com/mode/dialog/plugin/123/plan/456/?is_payment_method_update=true&license_key=urlEncodedLicenseKey`

## Customer Portal

If you previously migrated your platform from a self-hosted solution like WooCommerce or Easy Digital Downloads, users that wanted to cancel their subscription could cancel using the Freemius Customer Portal – but this wouldn’t actually cancel the subscription at the previously used payment gateway. Now, we’ve updated Freemius to show a corresponding message to contact support:![Freemius User Dashboard - Migrated subscription cancelation](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-user-dashboard-migrated-subscription-cancelation.png)  
Following feedback from the community, we discovered that the “Whitelist site” button was a bit confusing, as some users thought that the license would not be functional until sites were whitelisted. Therefore, we added a clarification message and changed the button label to “Restrict Sites”, and updated its color to make it clear that it’s a “dangerous” action:

![Freemius User Dashboard - Restricted Sites](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-user-dashboard-restricted-sites.png)

Additionally, we learned that the new license white-labeling option led to some confusion for some users that checked the box, yet didn’t see an immediate change on their site. This is because the SDK is currently syncing the license data once a day:

![Tickbox for activating the license on the client site](https://freemius.com/blog/wp-content/uploads/2020/03/word-image-2.png)

To make things more clear, we introduced a new dialog box letting the user know that it can take up to 24 hours until the update is propagated to the website, (with a tip on how to expedite it):

![Freemius User Dashboard - White-labeling Sync Notice](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-user-dashboard-white-labeling-sync-notice.png)

We are considering enriching the SDK with a secure endpoint to have the ability to remotely trigger syncing so updates like this will happen immediately.

### Website Deletion

Previously, if a user deleted a product via FTP, SSH, or by using any other method that was not using the “Uninstall” option in the WP Admin dashboard, Freemius would not get notified about the state change. This led to a situation where the product displayed as “installed” in the Customer Portal.

We found that this led to confusion among users and sometimes triggered support tickets asking to resolve the situation. Moreover, with some use-cases, like Docker-based local testing, a complete website can be trashed with a single line of code. These use-cases can generate “ghost” websites in the Customer Portal, an even more confusing scenario.

We are excited to announce that users can now self-declare a website deletion, which will automatically execute uninstall logic on the Freemius platform and show the product as “uninstalled” in the Customer Portal:

![User Dashboard - Website Deletion](https://freemius.com/blog/wp-content/uploads/2020/03/user-dashboard-website-deletion.gif)

This is useful for situations where an original website is deleted without uninstalling the plugins manually, such as a dev or testing site.

Alternatively, if only a single product was uninstalled incorrectly, they can also set the state of any product on a given website to Uninstalled:

![User Dashboard - Setting Product to Uninstalled](https://freemius.com/blog/wp-content/uploads/2020/03/user-dashboard-setting-product-to-uninstalled.gif)

Since the default filtration of the *Websites* section in the Customer Portal is *Installed*, deleted websites and products won’t show up in the default view.

## Deployment

The deployment process now preserves the End of Line (EOL) formatting of modified files. Our Deployment PHP Pre-processor was using Linux EOL formatting when rebuilding code after making required changes, which caused it to leave inconsistent EOL formatting in some cases.

## Developer Dashboard

### Payments Distribution: Lifetime vs. New Subscriptions vs. Renewals

We added a chart to help you better understand payment distributions. Now, you can compare where your revenue actually comes from. Are your lifetime, new subscriptions, or renewal payments contributing most to your gross revenue? The Payments Gross Distribution chart will help answer that question.

![Freemius Developer Dashboard - Payments Distribution](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-payments-distribution.png)

### GBP Currency

All products can now have plans available in GBP (British pounds) currency.

## Assets Ownership Transfer By Changing The Email Address

This one is huge and we hope that it will save all of us a bunch of time. Previously, if you were trying to update a user’s email address to an address that already belongs to another user in the system (even if it’s actually the same person), you would have to contact our support team and we were transferring the assets from one user to another.

This is no longer needed!

Transferring ownership of assets is now possible just by changing the user’s email address in the Developer Dashboard. Here’s the process and dialog box that pops up when trying to update a user’s email address to an email of an already existing user:

![Freemius Developer Dashboard - Assets Ownership Transfer](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-assets-ownership-transfer.gif)

Additionally, if an older version of the product is being used and is not using the latest SDK, we added a notification so you’re aware that ownership may not properly happen until the product is updated.

### ![Freemius Developer Dashboard - Assets Ownership Transfer Error](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-assets-ownership-transfer-error.png)

### Setting Payout Methods

You can now set and update the payout method for each currency you are selling with in the My Profile section:

![Freemius Developer Dashboard - Setting Payout Methods](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-setting-payout-methods.png)

### Payment Type Indicators

We’ve added new “payment type” indicators – a play button for initial payments, arrows for subscription renewals, and a lifering for lifetime payments.

![Freemius Developer Dashboard - Payment Type Indicators](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-payment-type-indicators.png)

### Re-Syncing License Activations

In some edge cases, license activations would get out of sync, which is quite rare but can happen in some edge cases for the sake of improved performance. You can now easily sync the license activations with the exact number of product installations using that license without the need to change the quota of the license:

![Freemius Developer Dashboard - Syncing License Activations](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-syncing-license-activations.jpeg)

### Coupons Timezone

When creating new coupons, the start date is now based on the GMT timezone and not on the geolocation of the developer. This caused issues when sending coupons for people to use immediately when the developer and the person that is intended to use the coupon are located in different timezones:

![Freemius Developer Dashboard - Effective Date Range for Coupons](https://freemius.com/blog/wp-content/uploads/2020/03/freemius-developer-dashboard-effective-date-range-for-coupons.png)

### Team Member Details

When adding team members to help manage your business, product owners and admins can now see the email addresses of the product’s team, instead of just the developer ID and their name.

## Thanks for Reading

If you made it this far, you must be interested in other features!

Please feel free to add your feature requests or suggestions to our [Trello board](https://trello.com/b/I6o3BZOo/freemius-features-requests) and let us know what else you’re interested in. We’ll do our best to include your requests if/when possible in one of our future updates.