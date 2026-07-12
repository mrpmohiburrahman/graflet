Release Notes include our periodic updates that highlight the recent product improvements we’ve made, so you can easily stay up-to-date on what’s new. Here’s what we launched between December 2018 and June 2019 (a LOT!).

During the past six months we released LOTs of new exciting features. Here are some of the notable ones:

- Multi-Currency Pricing & Support
- Release Cycle Management – Beta Program
- New EULA (End User License Agreement)
- Login as Customer
- Checkout Optimizations
- Major enhancements around bundles & add-ons

## Multi-Currency Transaction Support (A big one!)

We are super excited to share that Freemius now fully supports [multi-currency pricing and transactions](help-documentation-selling-with-freemius-multi-currency.md), recently adding *€-Euros* and *£-Brithish Pounds*, in addition to *$-U.S Dollars*, which we supported from the get go.

You may be wondering, what’s with all the excitement around multi-currency? I mean, both Stripe and PayPal (the gateways we use under the hood) support multi-currency transactions out of the box, so what’s all the fuss about?

Due to various financial regulations and interests from payment gateway companies, as a U.S. company, even if we accept non-USD with our U.S. PayPal/Stripe accounts, there’s no way for us to withdraw the funds in their original currency. The payment gateway companies first convert the money to USD with a healthy 2-4% FX (Foreign Exchange) conversion fee. It was clear to us that deducting an additional % from our sellers community is a big no-no, so we had to figure out a way to solve that without the additional fee. After doing some research and having discussions both with Stripe & PayPal, we ended up opening European accounts, which are now used for transacting EUR (*€-Euros*) and GBP (*£-Brithish Pounds*).

An added benefit from that move is that [Stripe’s fees for European account holders](https://stripe.com/de/pricing) for European cards are 50% cheaper than Stripe’s US account fees. So, the gateway fee for a EUR transaction with a European card is now only 1.4% + €0.25, instead of the 2.9% + $0.3 with the U.S account.

Another added benefit is that our platform now supports a rule based gateway selection, allowing us to not only add new gateways into the system relatively easily, but also set up custom rules to determine which gateway will transact a specific payment based on criteria such as: geolocation, currency, credit card type, transaction amount, and more. That capability gives us a LOT of flexibility to help our developers’ community minimize transaction costs. For example, if a payment gateway is competitively priced for transacting VISA debit cards in Canada, leaving the legal & logistical aspects aside, we can integrate that gateway and selectively use it *only* for transactions involving Canadian VISA debit cards. While Stripe is a robust payment gateway and using Stripe for credit card processing was the right decision for us to begin with, our newfound deeper knowledge and understanding about the underlying costs of credit card processing allows us to factually say that other top-tier payment gateways offer much more competitive prices, without lacking on features or support.

Implementing additional gateways in this dynamic way will not happen overnight, as we have many higher priorities at the moment. However, the point is that even though our pricing model doesn’t cover gateway fees and theoretically we could just forward the fees to our sellers without looking into it more deeply, we genuinely care about our selling makers, and we are constantly enhancing our system to help you maximize your bottom line. So, if you are choosing to sell with Freemius, rest assured that for the long-term, the cost of gateway fees will significantly go down and you won’t have to do anything to make it happen.

You can learn more about Freemius multi-currency, what plugin and theme businesses we recommend it for, and how to activate it [here](help-documentation-selling-with-freemius-multi-currency.md).

## Release Cycle Management – Beta Program

The whole release cycle in the world of WordPress plugins and themes is lacking compared to the robust CI/CD workflows in the “real world”. If you have a plugin/theme with tens of thousands of active installs, every release becomes risky. At the least, it can negatively affect your business agility and puts your users’ and customers’ websites at risk. There are various practices to mitigate that risk, and one of the more popular ones is building a group of [beta testers](https://freemius.com/blog/wordpress-plugin-beta-testing/): People that love getting early access to your products – and giving them a spin before anyone else in exchange for feedback.

So… we are pleased to announce that you can now systematically onboard beta testers with Freemius and release beta versions only to those users that opted-in to the beta program!

Users can opt-in to the beta program directly from their Account page by simply checking a box and agreeing to the disclaimer prompt:

![Join the Beta Program](https://freemius.com/blog/wp-content/uploads/2019/06/join-the-beta-program-1.png)

Alternatively, you can add a user to the beta program directly from the user’s profile in the *Developer Dashboard* (don’t forget to click the UPDATE button to save):

![User Beta Program Activation](https://freemius.com/blog/wp-content/uploads/2019/06/user-beta-program-activation-1.gif)

Ready to release a beta version? Not a problem! Just upload it to the DEPLOYMENT section and flag it as a *Beta release*. When you’re ready to make the beta release public for everyone, simply switch the version to *Released* – it’s that easy!

![Version Deployment Includes Beta Releases](https://freemius.com/blog/wp-content/uploads/2019/06/version-deployment-includes-beta-releases-1.gif)

Beta releases will be flagged in the WP Admin with a *Beta* label, making it clear to users that they are currently using a beta version of the product:

![Beta label on WP Admin Plugin List](https://freemius.com/blog/wp-content/uploads/2019/06/beta-label-on-wp-admin-plugin-list-1.png)

![Beta Label on WP Admin Theme List](https://freemius.com/blog/wp-content/uploads/2019/06/beta-label-on-wp-admin-theme-list-1.png)

We hope that by empowering you with the ability to easily start beta programs it will create a safer product environment for the whole WordPress community, and of course, for your customers. Now you can test releases on a small subset of users who willingly opted-in to test your versions before making them public for all.

**Notice:** The initial version of the *Beta Program* feature can only be activated for users that are running a paid version of your plugin/theme. Also, it is not yet supported for add-ons.

## Freemius Checkout

### New Checkout JavaScript API Options

In addition to the new `currency` parameter added to control the currency that the checkout will be opened with, you can now pre-populate a license key with the `license_key` param:

```

license_key: ‘&lt;key&gt;’,

```

And if you are running a periodic promotion and want to automatically apply a coupon but not reveal it to your users, you can now include the following in the checkout’s config:

```

coupon: ‘&lt;COUPON_CODE&gt;’,
hide_coupon: true,

```

You can check the full list of checkout options here:

[https://freemius.com/help/documentation/selling-with-freemius/freemius-checkout-buy-button/](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md)

### Checkout Session

We introduced a new 60 min session “memory”, to increase conversion rates and make it easier to purchase multiple products from the same store. Basically, if a customer purchases a product on your site and then opens the checkout for another product within 60 min of the previous purchase, the buyers name and email will automatically get pre-filled when the checkout is opened. This session is automatically renewed on every purchase, allowing a customer to purchase multiple products without the need to enter their personal contact info over and over again.

Since Freemius doesn’t have a “cart” concept, and we don’t believe we should due to the extremely low number of multi-product purchases in the plugin and theme space, the checkout session memory feature is a good compromise between the “best of both worlds”.

### Renewals Discount

If a product has an annual renewal discount set, the checkout now makes it clearer that the initial payment is higher than the ongoing renewals:

![Renewals Discount on Checkout](https://freemius.com/blog/wp-content/uploads/2019/06/renewals-discount-on-checkout-1.png)

### PayPal Checkout

PayPal introduced an option to dynamically include a header image in the checkout page. We decided to integrate that option, so the checkout is branded with your product’s icon:

![Freemius - PayPal Express Checkout - Product Icon](https://freemius.com/blog/wp-content/uploads/2019/06/freemius-paypal-express-checkout-product-icon-1.jpeg)

### Checkout for Bundles

A lot of work was put into the checkout in relation to selling bundles. The checkout now shows a rich list of bundled products, including the undiscounted standalone price of each product, as well as the discount amount saved by purchasing a bundle:

![Selling Bundles via Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2019/06/selling-bundles-via-freemius-checkout-1.png)

There’s a lot of complex calculations happening behind the scenes to properly calculate all the discounts and prices based on your plans configuration. All those discounts are CRO boosters – their purpose is to show the customer how much money they are saving.

### Bug Fix

Due to our implementation of Stripe, a customer that subscribed with a credit card for a trial of a product that has a renewal discount was charged the difference between the renewal amount and the initial payment amount upon trial cancellation. That issue is fixed and no more unexpected charges should happen upon cancellation.

## User Dashboard

### Browser Compatibility

The *User Dashboard* now works on Internet Explorer 11 and higher.

### Websites Section

A new filter was added to the websites section for users to more easily filter the websites where at least one of your store’s products has been activated, installed, or deactivated. The websites section now by default displays websites where the product is installed.

![User Dashboard Websites Filter](https://freemius.com/blog/wp-content/uploads/2019/06/user-dashboard-websites-filter-1.gif)

Before that, we were showing users all the websites that ever had a product from your store installed (if they opted-in), which was leading to some confusion when, for example, a customer had previously uninstalled the product from the website or maybe even deleted the website as a whole.

### Download Upsell Enhancement

A major enhancement was introduced to the download upsell dialog box. When a user tries to download a product for which the license expired, they can now choose whether to renew the existing license or purchase a new one. Moreover, if the context license was purchased as part of a bundle, another option will show up to renew the bundle’s license:

**![Download Button Offers Renew/Purchase Option](https://freemius.com/blog/wp-content/uploads/2019/06/download-button-offers-renewithpurchase-option-1.gif)**

## Developer Dashboard

### Sticky Headers

All tables now have sticky headers – a small, yet powerful, UI/UX improvement. Please note that while most popular browsers support this CSS rule, IE and Opera Mini do not:

![Sticky Headers in the Freemius UI/UX](https://freemius.com/blog/wp-content/uploads/2019/06/sticky-headers-in-the-freemius-ui-ux-1.gif)

### Bundle Products

The PRODUCTS section of the *Developer Dashboard* now visually displays bundled product types and icons, making it much easier to identify a product within a bundle than before:

![Icons for Bundled Products](https://freemius.com/blog/wp-content/uploads/2019/06/icons-for-bundled-products-1.png)

### Emailing Manually Created Licenses

There are multiple use-cases in which developers may need to manually create licenses; here are a few:

- Paid reviews – reviewers need to test your product
- Giveaways – winners need to access the product
- YouTube promotions – affiliates need to access paid product features

Previously, you could easily create a license for those use-cases, but then you had to manually email the license to that person. That sounds easy, right? But, how do you email the download link securely? What about install instructions? There are many ways to handle it – they all require a bunch of steps – and such a process can take 10-15 min – that’s a lot of wasted time!

Based on your feedback, we introduced a new capability to the manual license creation dialog box allowing you to automatically email the license key, product download link, and installation instructions by simply checking a box:

**![Email the License Key and Download Link to the User](https://freemius.com/blog/wp-content/uploads/2019/06/email-the-license-key-and-download-link-to-the-user-1.png)**

### Login as Customer (aka impersonation)

As part of our efforts to empower you with tools to better serve your customers and reduce your support load, now you can easily log in to any of your customers’ *User Dashboards* to see exactly what they see when they are logged-in. Simply open the relevant user profile in the *Developer Dashboard* and click \*LOGIN AS USER\*:

![Login as User](https://freemius.com/blog/wp-content/uploads/2019/06/login-as-user-1.png)

This will open the *User Dashboard* and will automatically pre-populate all the input fields – all that is left to do is click the sign in button and you are in!

![Pre-populated Fields for Logging in as User](https://freemius.com/blog/wp-content/uploads/2019/06/pre-populated-fields-for-logging-in-as-user-1.png)

For security reasons, your team members will only be able to login to the user’s account when they have access to all the store’s products. I.e., if you are the seller of 3 different plugins and you’d like your support rep to have impersonation capabilities, you’ll need to add the support rep as a team member to all 3 products.

This awesome feature (and a few others) came from the [Tickera](https://tickera.com/blog/we-are-switching-to-freemius/) migration to Freemius (thank you!).

### Contact Us Styling

You can now add a custom CSS stylesheet that will be added to the in-dashboard contact us form:

**![Custom CSS for WP Admin Contact Form](https://freemius.com/blog/wp-content/uploads/2019/06/custom-css-for-wp-admin-contact-form-1.png)**

### Coupons New Default Order

The default order of coupons listed in the *Developer Dashboard* is now showing the “freshest” coupons first. You can now expect to see the coupons sorted based on these criteria:

1. Active coupons – active will appear before inactive
2. Promotion end date – a coupon that expires in 7 days will appear before a coupon that expires in 2 days
3. Promotion start date – a coupon that its validity started 3 days ago will appear before a coupon that its validity started 7 days ago

For example, if there are 2 active coupons that are valid until Jan 1, 2020, the coupon that expires later will appear before the other one.

### Bug Fixes

- Adding a webhook for add-ons is now fixed.
- The DASHBOARD’s “Upgrades” counter was showing the number of licenses created during the selected period, and after receiving a report from one of our makers, we realized that the counter was confusing because it also incorporated manually created licenses. We’ve updated the counter to only include upgrades that are associated with actual purchases and subscriptions (trials are counted too).

![Upgrades Counter](https://freemius.com/blog/wp-content/uploads/2019/06/upgrades-counter-1.png)

## Team Management & Permissions

### Team Membership Bulk Editing

If you are managing multiple products with Freemius and have a team of people working with you, you have probably already noticed that the experience of adding/removing team members is cumbersome. You had to repeat the same process over and over again for every single product. As an example, if you have 20+ add-ons, you’ll need to add every new team member 20+ times.

No more!

From now, when you add/edit/remove a team member of a product with add-ons, you can easily apply the exact same permissions for all its add-ons:

![Add Team Member to All Add-ons](https://freemius.com/blog/wp-content/uploads/2019/06/add-team-member-to-all-add-ons.png)

The same logic also applies for bundles. You can now manage team permissions for a bundle, which will apply the same team membership permissions across all the bundled products.

### Team Permissions Update

We audited the role permissions and made sure that data is properly protected and only accessible to the relevant roles. For example, `Support`reps will no longer be able to access the product’s stats page nor secret key.

Also, we introduced a new `Developer` role that, unlike the `Support` role, permits deploying and managing product releases:

![Add Developer as Team Member ](https://freemius.com/blog/wp-content/uploads/2019/06/add-developer-as-team-member.png)

## New EULA

After months of ongoing work with our legal firm, we released a new EULA (End User License Agreement) that is dynamically adjusted based on your product’s configuration. The purpose of the EULA is to protect YOU and us from legal actions that can come from customers.

As a reminder, if you’d like to check your EULA, you can access it via the following link:

[https://freemius.com/terms/&lt;productID&gt;/&lt;productSlug&gt;/](https://freemius.com/product/56/rating-widget/legal/eula/)

We also spent some time styling the EULA, giving it a nice legal agreement look, branded with your product’s icon, and an easy option to print it:

![New End User License Agreement (EULA)](https://freemius.com/blog/wp-content/uploads/2019/06/new-end-user-license-agreement-eula.jpeg)

To make things easier, we have also included a few “shortcuts”, allowing you to link directly to specific sections in the EULA:

- Subscriptions terms summary: `https://freemius.com/terms/<productID>/<productSlug>/#subscriptions_summary`
- Refund policy summary: `https://freemius.com/terms/<productID>/<productSlug>/#refund_policy_summary`
- Full refund policy: `https://freemius.com/terms/<productID>/<productSlug>/#refund_policy`

For example, if a customer contacts you asking to refund a renewal, you can tell them that they agreed to the EULA when purchasing the product and renewal refunds are not covered, while linking directly to the subscriptions terms summary:

`https://freemius.com/terms/<productID>/<productSlug>/#subscriptions_summary`

## Help Scout Integration

A little handy addition to our [Help Scout app](help-documentation-integrations-help-scout.md) is that you can now see the site owner’s origin country, and for your added convenience in scheduling with your customers, the country name links directly to the customer’s time zone information on timeanddate.com.

![Help Scout Integration Country Listing](https://freemius.com/blog/wp-content/uploads/2019/06/help-scout-integration-country-listing.png)

## Affiliate Platform

### Affiliate Coupons

We can now link a coupon to an affiliate to attribute all sales with the coupon to a particular affiliate, regardless if an affiliate link is clicked or not. Affiliates with a linked coupon will be awarded with a referral every time the coupon is redeemed as if the customer had used a valid referral URL.

This is particularly useful if you work with affiliate marketers that mainly focus on video promotions. Since the CTR (click-through-rate) of YouTube footnote links is pretty low, offering an exclusive coupon – even if it’s a symbolic 5% discount – is a great way to overcome that barrier and still be able to attribute sales to the affiliate.

**Note:** This capability is still not available in the *Developer Dashboard* so you’ll need to contact our support if you’d like to use it.

### Affiliate UTM Tags

While we do offer affiliate link tracking in the dashboard, many people prefer to manage all their tracking with GA (Google Analytics). Due to browser security restrictions and HTML attributes such as rel=”noreferrer”, there are many cases in which GA won’t be able to determine the source of the referral, and those clicks will just be counted as direct traffic. Now, all affiliate links automatically include UTM tags to easily identify the source of traffic. For example, let’s assume that a user clicks on an affiliate link that links to my-awesome-product.com from awesome-affiliate.com. The affiliate link, which looks like https://r.freemius.com/123/456/, will redirect to:

`https://my-awesome-product.com?utm_source=awesome-affiliate.com&utm_medium=website&utm_campaign=fs_aff`

Here’s the URL structure:

`https://my-awesome-product.com?utm_source={affiliate_main_domain}_{referrer_domain}&utm_medium={‘direct’|’website’|’social’}&utm_campaign=fs_aff`

## Cart Abandonment Recovery

Since our [*Cart Abandonment Recovery*](help-documentation-marketing-automation-cart-abandonment-recovery.md) mechanism works silently in the background, we discovered that some of you were not even aware it’s there 🙂 To improve communication and make it easier for you to track recovered carts, you’ll now get a notification upon successful cart recoveries:

![Successfully Recovered Cart Emails](https://freemius.com/blog/wp-content/uploads/2019/06/successfully-recovered-cart-emails.png)

## Dispute Handling

Although this was mentioned in previous release notes, we want to remind you that our end goal is to integrate with payment gateways’ dispute APIs and introduce a whole semi-automated disputes management system for our sellers, giving you the freedom and control to manage disputed payments of your products. Since this is a huge project, we are going to implement it incrementally, starting with PayPal disputes. Starting a few months ago, when a PayPal payment is disputed, we store the full dispute details in a structured table on our backend and notify developers about the disputed payment with guidance on what can be done. If you do not agree with the buyer’s claim, we ask you to reply to that email with additional information, which we later use for the evidence submission process:

![Paypal Dispute Process](https://freemius.com/blog/wp-content/uploads/2019/06/paypal-dispute-process.jpeg)

As you can see above, the email we send to *Sellers* comes with the full context of the case, including any messages sent by the buyer, whether the paid product was downloaded or not, a summary of the product’s refund policy, the reported reason for the dispute, the response due date, and much more. Our goal is to empower you with *all* the contextual information and links that you need to make a decision without the need to dig and collect all that data yourself.

Keep on the lookout for further updates on dispute handling in the next release notes!

## WordPress SDK v.2.3.0

### Bundles

If your main business model is offering a free core plugin/theme and then selling bundles, we have some exciting news for you! You can now render the bundle’s pricing inside the WP Admin instead of showing the plugin/theme’s pricing. To activate that option all you need to do is add a `‘bundle_id’ => ‘<YOUR_BUNDLE_ID>’,` setting to your integration snippet – it’s that easy!

Moreover, when activating a paid plugin or add-on, if the opted-in user obtained a bundle license that includes that paid plugin/add-on, the license will now be automatically activated upon the activation of the product. In a multi-site network environment, the license will only get activated if the license’ activations have enough unallocated licenses to activate the license for all of the subsites in the multi-site network.

### Multisite Network

When we originally enhanced the SDK to include a proper multisite network integration, due to the complexity in the storage data model, we decided to ignore the scenario of a plugin activation being switched from the network level to the site-level, and vice versa. I.e., network activation of a plugin, and then later on, deactivation and activation of the same plugin on the site-level.

The new SDK version is backward compatible and now fully supports the handling of those use-cases. It may seem simple, but there’s a lot of thinking that had to go into the logic behind it. For example, if a paid network-integrated plugin is site-level activated on 3 out of 10 subsites in a multi-site network, and the super-admin activated a license on all those 3 sites, if the plugin will be shifted to network activation, the super-admin is automatically redirected to the license activation screen, but only required to activate a license on the 7 out of the 10 sites remaining which never had that plugin activated before.

Just to give you some numbers, there are about 40 different use-cases involved in that transition, and we handled all of them! (hope we didn’t miss any)

In addition, for plugins that have different WP Admin menu settings on the site level vs. the network level, you can now specify the network level menu settings by setting the new `’menu_network’ => array( … ),` option in the SDK integration snippet.

### Auto-Install – Disabled

Unfortunately, after ongoing discussions with the WordPress.org plugin review team, we had to disable the auto-install capability, which we introduced back in March 2017 after [Jetpack started to support installation of non-wp.org themes](https://make.wordpress.org/plugins/2017/03/16/clarification-of-guideline-8-executable-code-and-installs/). I’m not going to start #WPDrama because indeed our implementation was not exactly the same as Jetpack’s. It’s just a shame that creativity and UX are being blocked in some cases like these and for no good reason.

Since we are a data-driven company, when we released the auto-install feature, we wanted to validate our assumption that the auto-install experience is actually better for users. So, every user that selected the auto-install option during checkout was sent an email with a simple Google Form survey to rank the install experience from 1 to 5 and provide additional feedback. Out of 686 responses, 83% ranked it as excellent, another 10.5% ranked it as great:

![User Feedback on Auto Installation Process](https://freemius.com/blog/wp-content/uploads/2019/06/user-feedback-on-auto-installation-process.png)

We clearly see the need for simplifying the whole upgrade experience, and we’ll get back to tackling this problem from a different angle in the future, while making sure to comply with wp.org guidelines.

### Support Forum Link

If you don’t have a free version of your product on WordPress.org (and therefore no free support forum) or just want to link the *Support Forum* menu item added by the SDK to another support page, we introduced a new filter to override the URL. You can implement it as follows:

```

&lt;?php
function set_my_custom_support_url( $wp_org_support_url ) {
	return ‘https://my-awesome-product.com/support/forum/’;
}

my_fs()-&gt;add_filters( 'support_forum_url', ‘set_my_custom_support_url’ );
?&gt;

  
```

### Account Billing & Invoices

As part of our ongoing efforts to make it easier for customers to access their billing information and invoices, we introduced a little link in the upper area of the Account page:  
![Billing & Invoices Link Added to Account Details](https://freemius.com/blog/wp-content/uploads/2019/06/billing-and-invoices-link-added-to-account-details.png)  
Even though the billing & invoices can be found on the lower part of the same page, some buyers were still missing it, so we added this simple anchor link.

### Download/Install Add-Ons from WP Admin

Back in 2017 when I attended [PressNomics](https://pressnomics.com/) 5, I had a chat with my friend [Matt Cromewall](https://www.mattcromwell.com/). Among many different things we discussed, Matt mentioned [Crate](https://cratewp.com/) (which was never released btw) as an example of a great UX for managing and installing add-ons from right within the WP Admin, without the need for customers to go through the standard, tedious installation process normally offered by WP plugins and themes:

![Create Demo](https://freemius.com/blog/wp-content/uploads/2019/06/create-demo.gif)

\[Crate early prototype from cratewp.com]

This feature has been on our list for more than 2 years, and we’ve finally managed to prioritize it! This is particularly useful if you sell a lot of add-ons. Now your customers can easily download or activate your add-ons directly from the WP Admin.

So how does it work?

If the customer has a valid license for an add-on and they are running the free wp.org version of your core plugin/theme, they will now be able to ***download*** the add-on directly from within the WP Admin, in addition to viewing the add-on’s details:

![Download Add-Ons from WP Admin ](https://freemius.com/blog/wp-content/uploads/2019/06/download-add-ons-from-wp-admin.gif)

***Installing*** the add-on directly within the WP Admin from wp.org compliant products is not allowed, therefore, the install option will only be available when the installed & activated core plugin/theme version is paid or explicitly flagged as non-WP.org compliant. This is how it will look in that case:

![Install Add-Ons from WP Admin ](https://freemius.com/blog/wp-content/uploads/2019/06/install-add-ons-from-wp-admin.gif)

We’ve made another UX improvement to the WP Admin add-ons section: Installed add-ons are now shown with an *INSTALLED* label, making it easier for admins to know if an add-on is already installed on the website or not:

![Installed Add-Ons labeled in WP Admin ](https://freemius.com/blog/wp-content/uploads/2019/06/installed-add-ons-labeled-in-wp-admin.png)

### Compatibility with ManageWP, MainWP, InfiniteWP, and Jetpack

The [*Freemius WordPress SDK*](https://github.com/freemius/wordpress-sdk) incorporates a mechanism that automatically identifies a plugin or theme’s main file. That mechanism relies on `debug_backtrace()` and assumed that WP core is responsible for originally including that main file. After several related GitHub issues in which the SDK was failing to properly get the product’s title and version, we did some troubleshooting of the problem and found that it was related to the use-case of 3rd party plugins being responsible for inclusion/execution and not the WP core. ManageWP, MainWP, InfiniteWP, and Jetpack all have capabilities to remotely install and activate plugins and themes. The inclusion of products via those services is processed differently and the code of the managed products is directly included by the corresponding services’ *“agent”* plugins.

Long story short, we addressed that use-case and the logic now properly identifies the product’s main file also when the product is managed by one of those 3rd party plugins (and not WP core).

## What’s next?

I like ending the release notes with some insights into our short-term roadmap. While priorities can easily change and an agile startup like Freemius needs to maintain that flexibility, here are some of the upcoming things we *plan* to develop in the near future.

### Multi-Store & Store-level Management

Our *Developer Dashboard* was initially designed to manage single products. Back in November 2018, we introduced a concept of *stores* together with the release of the [*User Dashboard*](blog-users-management-dashboard-premium-readme-custom-premium-slug-free-trials.md). Each developer was automatically allocated their own store, and every product they created was linked to it.

Since that release, we identified a growing demand from makers selling multiple products to have a store-level dashboard to track the whole store’s sales performance, support store-level affiliate links, manage the team for the whole store, and more.

Additionally, some of our makers have multiple stores & brands, and there’s currently no UI for managing multiple stores under the same account.

That’s something we would really like to tackle in the near future.

### WordPress SDK Sanitization & Escaping

One of the core functions of the WordPress SDK is [`fs_request_get()`](https://github.com/Freemius/wordpress-sdk/blob/master/includes/fs-core-functions.php#L128-L164). This helper function is used for accessing GET/POST params received from the client side, with an optional default value when the parameter is missing. The actual sanitization of the input is done in the scope of the function’s usage.

The WordPress.org plugin & theme review teams keep falsely flagging that SDK helper function since it doesn’t incorporate sanitization of the data. It’s a combination of automated testing tools that are limited in “seeing” the full scope of the code, as well as false-positives raised by reviewers that are browsing the code looking for issues. I can’t blame them – reviewing a whole product’s code can consume a lot of time – it’s just not feasible with a volunteer-powered review process.

In summation, we don’t like the negative impression developers just joining Freemius can have from the rejection experience with wp.org, regardless if it’s our fault or not. Therefore, with the current review process structure and human resources available, we are going to address the issue and sanitize that input data inline. While it will increase the code size (we’ll have to duplicate some redundant code) and affect the performance a bit, we are confident it’s the best decision going forward as we strongly believe in the wp.org ecosystem and want to ensure our SDK meets the repository’s guidelines properly.

### Revamped In-Dashboard Pricing

If you are selling freemium products with Freemius, you should be familiar with the SDK’s in-dashboard pricing page. The page was initially developed back in 2015 using old front-end technologies, and is also very structured and relies on several assumptions that helped us expedite development back then. Obviously, the page has undergone extensive development as we’ve added many features throughout the years. Due to the outdated technology it uses, the maintenance, bug fixing, and new features development, became slower and slower. Also, after seeing so many pricing structures, we have a much better understanding of the limitations of that page. Lastly, we want to give you complete flexibility to modify the pricing page template, something that is currently impossible since it’s running remotely from our end.

The plan is to rebuild the pricing page from scratch using React and ship the code as part of the SDK. In fact, we already started working on it and hope to include it in the next major SDK release.

### Checkout Localization

I mentioned this last year, although we still haven’t managed to prioritize this one. Basically, we want to make the checkout accessible for non-English buyers by introducing multilingual capabilities.

## See you at WCEU 2019!

That’s all for this update folks 🙂 If you are attending WordCamp Europe this week, don’t be a stranger, come by and say hello! Both [Brandon](https://twitter.com/brand_on_fire) and [I (Vova)](https://twitter.com/vovafeldman) will be there – feel free to DM us on Twitter and let’s catch up.