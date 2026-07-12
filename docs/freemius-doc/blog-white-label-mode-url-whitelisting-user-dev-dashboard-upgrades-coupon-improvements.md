Release Notes include our periodic updates that highlight the recent product improvements we’ve made, so you can easily stay up-to-date on what’s new. We’ve had some major updates and bug fixes to make selling your plugins and themes way easier! Here’s what we worked on between June – Sept 2019:

- White Label mode and URL whitelisting.
- Major improvements to coupons
- Strong Customer Authentication (SCA) is fully supported in the Freemius checkout
- A ton of UX improvements related to checkout, transactional emails, and the Customer Portal
- An upgrade to our Help Scout App that will help you organize your support tickets.

### License Security

One of the most useful things that came out of [OceanWP’s migration to Freemius](https://oceanwp.org/blog/oceanwp-freemius-perfect-match/) was that we discovered some exciting needs for Agency customers. We’ve added 2 new capabilities into the Customer Portal to allow for greater protection of the license purchased by an Agency, including White Label Mode and URL Whitelisting.

From a marketing/sales point of view, these features make your products much more compelling for that special segment of users that are building sites for clients.

Both features are available in a new LICENSE SECURITY section shown when managing licenses:

![License Security on Freemius](https://freemius.com/blog/wp-content/uploads/2019/10/license-security-on-freemius.png)

#### White Label Mode

Agencies and freelancers who work on client projects can hide confidential information about their account and license by flagging a license as White Labeled:  
![License Security & URL Whitelisting](https://freemius.com/blog/wp-content/uploads/2019/10/license-security-and-url-whitelisting.png)

This means that Account details normally shown in the Account tab in the WP Admin will **not** appear when Users check the box that says “This license is activated on my client(s) site(s)”. This addition to the [Customer Portal](wordpress-user-dashboard.md) is great for anyone who uses your product as part of their own services. Here’s everything that will be hidden when a license is set as white-labeled:

- User information
- Billing details and invoices
- License key
- Pricing page
- Add-on prices (if you sell add-ons)
- Contact Us page

**Important:** This feature will only work with the newly released SDK (and all future release). So if this feature is essential for your product, make sure to update the SDK to the latest release.

#### URL Whitelisting

With the new URL whitelisting capability, customers can also control the URLs that can activate their license or continue receiving updates.

![URL Whitelisting](https://freemius.com/blog/wp-content/uploads/2019/10/url-whitelisting.png)

### Serviceware Plugins Support

If you’re running a SaaS that uses a free plugin or theme to connect to your users’ WordPress websites, your users can download the product from the Customer Portal.

Servicware plugins don’t go through the typical license activation process, so we customized it to go through the plugins.php page:

![Serviceware License Protected Plugin](https://freemius.com/blog/wp-content/uploads/2019/10/serviceware-license-protected-plugin.png)

### Free Bundled Products Support

If a bundle contains free WordPress.org products, they will be shown in the downloads section. The download confirmation dialog has been adjusted accordingly:

### ![WordPress.org product reference in User Dashboard](https://freemius.com/blog/wp-content/uploads/2019/10/wordpress-org-product-reference-in-user-dashboard.png)

### PayPal Subscription Cancellation

Since it can take up to 24 hours before an initial payment for a PayPal recurring profile is processed, the cancel subscription option will no longer be visible for PayPal subscriptions that haven’t yet received any payments.

## Coupons

Coupons are much more flexible! You can create multiple coupons with the exact same code based on different criteria. The checkout engine automatically applies the coupon that matches the criteria.

Usage example:

You can create two [Black-Friday/Cyber-Monday](https://freemius.com/blog/black-friday-cyber-monday-wordpress/) coupons with the same code “BFCM”. One coupon can apply 20% off an annual 5-site license, and a larger 40% discount for any lifetime plan. You don’t need two separate coupon codes.

It also means that if you previously created a “BFCM” coupon that has expired, you can create another one with the same code for the recurring promotions.

### Coupon Indicator

If a purchase is associated with a Coupon, the gross payment amount shows an icon next to it (both for payments and subscriptions) in the Developer Dashboard. This helps you easily identify payments that were discounted with a coupon and allows you to easily navigate to the associated coupon.

![Coupon Indicator](https://freemius.com/blog/wp-content/uploads/2019/10/coupon-indicator.png)

### Down to the Cent

You can now set coupon amounts down to cents for more specific use cases – like $10.37 instead of just $10 or $11.

### Redemption Counter

Coupons have a clickable “redemption counter” that links to a list of payments that are associated with that coupon. This saves all the time in helping you find all the purchase history associated with a coupon.

![Coupon Redemption Counter](https://freemius.com/blog/wp-content/uploads/2019/10/coupon-redemption-counter.png)

## Cloned Environment – Finally Fixed!

If you’ve been using Freemius for a while, there’s a good chance you already stumbled across the dreaded fatal PHP error: `Argument 1 passed to Freemius::get_api_user_scope_by_user() must be an instance of FS_User`.

This error has been “haunting” our support for a while, but we’ve never managed to reproduce it on our end. After months of troubleshooting and research, we identified the problem:

The symptom of the error was due to inconsistency in the serialized object types stored in the Database. For some reason, instances of our custom classes, such as the `FS_User`, were converted into instances of the generic `stdClass` class.  
The error was typically happening after some sort of website cloning (e.g. website migration, staging to production replication, etc.).  
The environment was running PHP 7.2 and higher.

With the help of several kind buyers, we got screen recordings of their cloning process, which helped us to reproduce the issue and pinpoint the exact code that was causing the issue (this is one example from BackupBuddy):

```
  if ( is_a( $data, '__PHP_Incomplete_Class' ) ) {
      $serialized_object = serialize( $data );
      $std_class_object  = preg_replace( '/^O:\d+:"[^"]++"/', 'O:' . strlen( 'stdClass' ) . ':"stdClass"', $serialized_object );
      $data              = unserialize( $std_class_object );
  }
  
```

Due to the way those cloning solutions work the plugins are not included in the cloning execution process, therefore when the options are unserialized and replicated, PHP 7.2+ considers those object instances as `__PHP_Incomplete_Class`, which is then converted to `stdClass` and stored incorrectly in the Database.

To make a long story short, we created a workaround by wrapping all the logic that is expected to load instances of our classes from the storage with a helper function that will convert those instances to their corresponding classes in case they are serialized incorrectly as `stdClass`.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Tabs for Plugin/Theme settings!

With the new SDK release, developers can choose to include Freemius pages in the WP Admin within tabs of plugin or theme settings instead of menu items on the WP side menu. To activate the “tabs” view please include the following line in your [WordPress SDK](https://github.com/Freemius/wordpress-sdk) integration snippet:

`'navigation' => 'tabs',`

## Strong Customer Authentication

We made our checkout fully compatible with upcoming regulations for the upcoming European payment regulations around the 2nd Payment Services Directive (PSD2) and [Strong Customer Authentication](blog-strong-customer-authentication.md) (SCA) for accepting payments online. There’s nothing our plugin and theme selling partners need to do to prepare for SCA – we’ve minimized the risk of losing subscription payments and improved our checkout UX.

## Developer Dashboard

### Licenses

There’s a new filter available in the LICENSES section to filter by Plan, making it much easier for you to see who has purchased what plan, and organized your licenses more effectively.

### ![Licenses Plans Filter - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2019/10/licenses-plans-filter-freemius-developer-dashboard.png)

### Payment Refunds

If you need to refund a purchase of your plugin or theme, the refund dialog box shows an option to set a license as expired or canceled

![Payment Refunds - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2019/10/payment-refunds-freemius-developer-dashboard.png)

Choosing “Expire license” will set the license’s expiration date based on the date of the last payment, which is when the license would normally expire if the user stopped paying for it. The customer will still be allowed to activate and use the license if it is not blocking.

Choosing “Cancel license” will immediately cancel the license and block the product’s premium functionality that you wrapped with the [Freemius WordPress SDK’s licensing](help-documentation-wordpress-sdk-software-licensing.md) methods.

## Checkout

### Renewals Discount

We’ve migrated tons of plugin and theme shops to Freemius, and when we do the migrations they have a lot of complex pricing options set up, including things like lifetime coupons for discounts on renewals.

For these migrated licenses, we took an extra step to make sure all the discounts were brought over from the old system too, so if annual renewals take place after you migrate, all your customers will have the right price.

The extra peace of mind and hassle taken out of one step of the migration process.

### Payment Method Update

We’ve improved the process for Payment Method updates. Users will be presented with a form that only requests payment details and does not display unnecessary information about their subscription, pricing, etc. The reason this information was appearing before is that we had to basically re-create a subscription when users would change their payment methods. With the new update, users “really” update their payment method without changing anything about the subscription itself.

![Payment method updating - Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2019/10/payment-method-updating-freemius-checkout.png)

## Cart Abandonment Recovery

Automated [Cart Abandonment Recovery](wordpress-cart-abandonment-recovery.md) emails have been updated to display renewal discounts more precisely. If users activated a valid coupon during their abandoned checkout, the automated emails will include the discounted price. Your missed customers will now have a consistent experience when you’ve offered them a coupon for your product.

![Cart Abandonment Recovery Email With Renewals Discount](https://freemius.com/blog/wp-content/uploads/2019/10/cart-abandonment-recovery-email-with-renewals-discount.png)

We also updated the recovery emails so that If a customer starts to checkout and there’s already an existing cart that they completed in the last 48 hours, the cart recovery mechanism won’t be activated anymore, as it’s not likely that the customer would be trying to purchase another license.

## Customer Purchase Confirmation Emails

We added a disclaimer to all customer purchase confirmation emails about the statement descriptor they may see on their statements. This will help to reduce disputes if customers don’t recognize the charge.

While the main payment gateway we use, Stripe, does support a soft descriptor, allowing us to custom set the payment descriptor that appears on customers’ bank statements, it isn’t supported by all banks. Sometimes this leads to customer confusion about unrecognized transactions.

This issue also applies to PayPal payments, which always show “Freemius, Inc.” on the PayPal statement as their current soft descriptor doesn’t really work, even though they do have technical documentation on it.

![Freemius Statement Descriptor in Customer Purchase Confirmation Emails](https://freemius.com/blog/wp-content/uploads/2019/10/freemius-statement-descriptor-in-customer-purchase-confirmation-emails.png)

## Help Scout Integration

Freemius’ [Help Scout App](help-documentation-integrations-help-scout.md) now loads information from all emails that are associated with a ticket or customer (there’s an option to attach multiple emails to a single customer). This can save a lot of time when handling tickets where users activated products on multiple sites with different email addresses, but they’re the same person or business.

## Other Awesome Stuff

Translations added to the WordPress SDK

- 100% Translated to Tamil – big thanks to Sankar Srinivasan!
- 76% Translated to Czech – big thanks to [Karolína Vyskočilová](https://twitter.com/vyskoczilova)!

### Bug Fixes

- After users updated a premium version of a theme from the Updates page in the WP-Admin, it was still showing as if the theme was running a previous version even though the update was successful. This was all due to a cached layer, and the issue is resolved. Thanks to Jesse and [Yuli](https://twitter.com/YuliYang_Ching) from [REI Conversion](https://reiconversion.com/) for bringing it to our attention and helping us test!
- The Weekly Report email was showing sandbox payments-related data. That was fixed and now only real production purchases and subscriptions are taken into consideration.

## Keep Up to Date

You can stay up to date by subscribing to our blog, and you can also check out some of our [previous release notes](blog-category-release-notes.md) so you can see progress on different Freemius features.