Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up-to-date on what’s new. Here’s what we launched between August 2017 and March 2018.

We didn’t get lost on a tropical island since August, in fact, we’ve been working so hard on the product side that we didn’t even have time to publish these release notes. There are a lot of amazing new capabilities that we’ve shipped during the past six months, probably more than 30 different features, so I’m not going to cover all of it, just the biggest releases.

Ready, set, go…

The ability to sell bundles was on our TODOs list for over 2 years, so we’re extremely psyched to get this out and looking forward to see how it will help you increase your customers’ LTV (lifetime value).

The bundles solution is quite flexible, allowing you to sell any combination of products: themes, plugins, and add-ons. All under a single license and a single subscription (or a single purchase with a lifetime plan).

I’d like to highlight that we have put a lot of planning into the design of the bundles, consulting with successful business owners who have been selling bundles for years, to build an outstanding solution and avoid common flaws from other systems in the market. For example, one of the things that we’ve learned during the design was the importance of having a single license key per bundle. Imagine a bundle of 20 add-ons. Competing sales platforms will generate 20 different license keys for every purchase of the bundle. Besides the fact that this is a waste of storage resources. It also clutters the licenses management dashboard and adds a huge hassle for the customer when they need to activate their license keys. Instead of copying one license and then pasting it across all add-ons – the customer will need to switch their browser tab 40 times! Switch tab, copy license, switch tab to WP, paste license… and again and again… Imagine how annoying would the user-experience be in that case. Some bundles can have even more products packed inside them.

While there are a LOT of changes that we incorporated into the monetization engine to make it all work, we kept the frontend user-experience simple and intuitive. You can [start selling bundles of your existing products in literally less than 2 minutes](https://freemius.com/help/documentation/selling-with-freemius/selling-bundles-and-memberships/).

I’d like to showcase [Iconic’s bundle pricing](https://iconicwp.com/bundles/), which is an excellent example of a clean and elegant way to sell bundles:  
![Iconic Bundle Pricing](https://freemius.com/blog/wp-content/uploads/2018/04/iconic-bundle-pricing.png)

## Selling Memberships

When speaking of online/website memberships, it usually means subscribing to restricted content which you wouldn’t have access to otherwise. In our context, a membership license to a plugins business or a theme shop, means a customer can subscribe for a membership to access a subset, or all the current and future coming products of the shop. If you think about it, there’s almost no difference between a bundle and a membership when the membership in context relates to WordPress plugins and themes. It’s just a matter of terminology. When we realized that during the design process of the bundles, we decided to “kill” those two birds with one stone (we love animals, btw). Therefore, when setting up your bundle’s plan we added an option for you to include all future products as part of the plan, turning it into a classic plugins/themes membership:  
![Freemius Dashboard Membership Plan](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-membership-plan.png)

As mentioned, you can sell any combination of products in a bundle, so if you have a theme shop you can start selling a membership to all your themes. If you have a plugin business you can sell a bundled access to all of your plugins. And lastly, if you sell both plugins and themes you can sell access to all of your products combined 🙂

## An Affiliate Platform

We announced the release of the [Freemius Affiliate Platform](help-documentation-affiliate-platform.md) back in November when we released a [huge guide on starting an affiliate program for your WordPress products](blog-affiliate-program-wordpress-plugins-themes.md), but, since we haven’t published any release notes from back then, I wanted to mention it here again. In a few words, Freemius now includes a complete and secure affiliate solution so you can start onboarding affiliate marketers to promote your products in return for a commission.

To activate the affiliate program, navigate to the Freemius Dashboard and click on AFFILIATION. There, switch the “Activate Affiliation Program” on:  
![Freemius Activate Affiliate Program Switch](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-activate-affiliate-program-switch.png)

Currently, you can either add affiliates manually, via the dashboard, or let affiliates apply to your program directly, via their WP Admin dashboard:  
![Freemius WP Admin Affiliate Program Application Form](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-wp-admin-affiliate-program-form.png)

To include the affiliation application to your product, go to the SDK INTEGRATION page and tick the new Affiliation checkbox:  
![Freemius SDK Integration Affiliate Form Activation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-sdk-integration-affiliate-form-activation.png)

This will update the integration snippet, so you’ll need to deploy a new version with the updated code.

### What’s next for the affiliate solution?

There are still two missing components on our TODOs for the affiliation:

1. At the moment, we do not offer an application form that you can use for your site. Yes, you can leverage our [API](https://freemius.docs.apiary.io/) to build the form, but we would like to offer something out-of-the-box.
2. The 2nd thing is the affiliate program legal agreement. Our plan is to work with our legal firm to generate a reusable agreement, which you’ll be able to use on your site. At this point in time though, this is something that you have to take care of yourself.

## Upgrades and Downgrades Proration

Up until now, customers didn’t really have a way to upgrade/downgrade their licenses. A customer could update their plan, but behind the scenes, the engine would generate a new license and subscription, ignoring the previous set up. This generated 2 issues:

**Problem #1 – No Automated Proration**  
Imagine the following use-case: A freelancer purchased a single-site annual license for your WordPress theme. After only a few weeks, they fall in love with your theme and realize that they want to subscribe to the annual unlimited-site license and use your theme in all their projects. Awesome, right? Previously, the freelancer would then go to upgrade to the new site limit and pay the full price, even though they have only recently purchased the single site license. The same customer would most likely contact support, angrily demanding a refund for the 1st payment. Other customers that noticed it in advance would contact your support prior to upgrading, again, not so happy. Our workaround for that case was telling sellers to issue a one-time coupon for the prorated price. Not anymore! [Proration is now fully supported](help-documentation-selling-with-freemius-proration.md) and works like a charm.

**Problem #2 – No License Updates**  
Another use-case that the proration solves is:  
Let’s say that you are selling a premium-only plugin with two plans: Pro and Pro+. A customer subscribes to your 5-site annual Pro package and activates the license on all of their 5 sites. Then, after a short period, they realize that they actually need the Pro+ license. In the previous set up, the customer would go to your website to upgrade to the Pro+, but since there was no way to specify that it’s an upgrade of an existing license in the Freemius Checkout, they would pay the full Pro+ amount, even though they have only recently paid for the Pro plan. Moreover, they would have received a new license key and would need to activate the new license on all of those 5 sites again. Not so user-friendly 🙂 With the new release customers can add a license to the Checkout context:  
![Freemius Checkout License Renewal Input](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-checkout-license-renewal-input.png)

The new proration mechanism solves both of the mentioned issues: customers get a proration discount (when applicable), and their license is automatically updated so they don’t need to do anything else to enable the Pro+ license features on sites that already have an activated license.

## Deployment & PHP Pre-processor

Our PHP Preprocessor now supports PHP7 syntax, in addition to the PHP5 syntax, which we exclusively supported before.  
![PHP Mascot](https://freemius.com/blog/wp-content/uploads/2018/04/php-mascot.png)  
Another small, but important update that we’ve made is not adding a “ (Premium)” suffix to the plugin/theme name when the product is premium-only (with no free version). The idea behind the suffix is to help customers easily identify the premium plugin version when they have both the free and the premium products installed on their WordPress environment. But this is obviously not required when there’s only one code version for the product.

## MailChimp Integration

If you’re a MailChimp user selling with Freemius – we have got some awesome news for you:

### Plan-based Segmentation

Our MailChimp integration now automatically adds a custom merge field to store your customers’ plan name:  
![Freemius MailChimp Plan Merge Field](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-mailchimp-plan-merge-field.png)

To leverage that capability you’ll need to set up at least one rule that is associated with payments, subscriptions, or licenses. For example, when a `license.created` event is triggered, add the user to “My Customers” list. Once you have it set up, you’ll be able to create a plan-based segmentation of your users and customers and target different marketing campaigns, based on the customers’ plans:  
![Freemius MailChimp Plan Based Segmentation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-mailchimp-plan-based-segmentation.gif)

### Geolocation Based Segmentation

We are now also including the user’s country code with the MailChimp API calls, so you can create location-based segmentation as well:  
![Freemius MailChimp Location-Based Segmentation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-mailchimp-location-based-segmentation.png)

**Important:** These features will not apply retroactively and will only work for new subscribers.

## Reviews & Help Scout App Update

In an effort to help you get more reviews and testimonials from verified buyers we have added a button to the user profile page which retrieves a direct link to leave a review of the purchased product:  
![Freemius Dashboard User Profile Review Link](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-user-profile-review-link.png)

This is particularly handy for your support team. If you’ve just helped a customer – send them the direct link to review your product, while they’re appreciative.  
If you’re using Help Scout for your support ticketing system, we’ve enriched our Help Scout App by including the review link right in the Help Scout sidenav:  
![Freemius Help Scout App Review Link](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-helpscout-app-review-link.png)

If the user has already reviewed the product, instead of showing the link, the app will show the rating they had provided:  
![Freemius Help Scout App Customer Review Rate](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-helpscout-app-customer-review-rate.png)

Another helpful enhancement to the Help Scout App that we made is fetch the user’s profile, based on all the email addresses that are associated with the user on Help Scout, instead of the main one:  
![Help Scout User Profile Emails](https://freemius.com/blog/wp-content/uploads/2018/04/helpscout-user-profile-emails.png)

## Weekly Revenue Reports

We know how important it is for you to stay on top of your business growth. To facilitate that we initiated a weekly revenues report which lets you to review a beautiful breakdown of your weekly performance:  
![Freemius Weekly Revenues Report Email](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-weekly-revenues-report.png)

Showing your recurring revenues, new sales, renewals, and downgrades.

The email template was inspired by BillGuard’s weekly credit-card expense reports and as you can see it’s mobile first, so you can easily consume it via any device.

One downside is that if you have many products, you’ll receive a weekly report for every product which can be overwhelming. We do plan to introduce the concept of a “Store” in the future to aggregate the weekly reports among other things into a single view.

## Freemius Checkout Enhancements

First of all, we’ve finally [documented Freemius Checkout JavaScript API](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md)!

### Loading Freemius Checkout with A Coupon

We’ve actually announced this feature in our closed Slack group back on November, just before the [BFCM (Black-Friday / Cyber-Monday)](https://freemius.com/blog/black-friday-cyber-monday-wordpress/) period. You can now easily assign a coupon to the checkout, so when a user clicks the buy button it will preload the checkout with the coupon. This is particularly useful when you’re running periodic promotions. For instance, if you market a winter 50% sale with a header bar, you can add a buy button that will automatically load the checkout with the 50% discount coupon (already applied), saving the prospect the hassle of manually entering the coupon code.

### “Buying” The Free Plan

Not all of your free users are going to opt-in or upgrade to your product’s paid plan, but this new feature enables you to obtain your free users’ lead details and leverage that to convert them into paying users in the future. Instead of just handing out the ZIP file, you can now “sell” the free plan right from your website:  
![Freemius Checkout Selling Free Plans](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-checkout-selling-free-plan.png)

### Multi-site License Selection

If you’re offering multiple license levels for a plan, users can now modify the license level right in the checkout:  
![Freemius Checkout Dynamic Multisite License Selection](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-checkout-dynamic-multisite-license-selection.gif)

This offers more flexibility to you and to your potential customers. Also, as a data-driven company, we have started to track the impact of the licenses level-selection and so far 59.5% of the completed checkout sessions stepped-up the license level. We still don’t have enough data to draw final conclusions from this, but our goal is to make sure that it increases sales and not shoot ourselves in the foot. If we spot an overall reduction of the CLTV we may reconsider this enhancement.

### Cross-Browser Compatibility

Thanks to our new sellers from [WP Royal](https://wp-royal.com/), who are crazy for perfection and cross-browser compatibility (in a good way), we’ve fixed a few client-side related bugs in Safari, Edge, and IE11. So now the checkout is working perfectly across all browsers (modern and legacy).

### Flexible Pricing

#### Flexible Billing Cycles

Our checkout can now deal with inconsistent billing cycles across your plan’s pricing, giving you more flexibility. For example, look at the pricing setup below:  
![Freemius Dashboard Plan Flexible Billing Cycles](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-plan-flexible-billing-cycles.png)

As you can see, the single-site monthly price and unlimited-sites lifetime price were left blank. The checkout will now automatically adjust the available billing cycles, based on the site license level selection as follows:  
![Freemius Checkout Dynamic Billing Cycles](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-checkout-dynamic-billing-cycles.gif)

**Notice:** At the moment, the in-dashboard auto-generated pricing page for freemium plugins and themes will only show billing cycles that are available across all plans and all multi-site license levels.

### Flexible Multi-Site License Levels

We’ve introduced the ability to hide a plan’s multi-site price levels:  
![Freemius Dashboard Hide Price Level](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-hide-price-level.png)

This feature is great when you have customers with special bulk license needs. For example, let’s say that you’re selling single-site, 3-site, and 5-site licenses. An agency contacts you asking a quote for a 100-sites license. Once you agree on the price, you can simply add a 100-sites license pricing level and choose to hide it. Then, send a direct checkout link to the user keeping everything streamlined with the system, without over bloating (or exposing) your pricing for the rest of the customers.

## Licensing Engine Enhancement

So far, our plan configuration offered two options in regard to license generation:

1. A *Blocking License*: Once a license expires, the premium logic becomes inaccessible.
2. A *Non-blocking License*: Once a license expires, the premium logic remains active but product updates and support are disabled.

The configuration was across all billing cycles. If you’re following our progress and blog, you already know that we encourage developers to build [sustainable, SaaS-like businesses](blog-why-wordpress-plugin-developers-have-to-start-thinking-saas.md), which also means selling monthly plans when it’s a good fit. When selling monthly, one of the main ways to avoid abuse of that billing cycle is to configure the plans to use *Blocking Licenses*. That said, in today’s WordPress ecosystem, customers expect that if they buy an annual plan for a plugin or a theme they would be able to keep using the features, even after license expiration. Thus, we introduced a 3rd option for the license generation:  
![Freemius Dashboard Plan License Type Selection](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-plan-license-type.png)

With this option you get the best of both worlds: you can continue selling annual plans and offer *Non-blocking Licenses*, but also start selling monthly *Blocking Licenses*. So the generated license type will be different based on the billing cycle. We hope that this addition will encourage more developers to introduce monthly plans!

## Custom Product Icon Upload

You can now upload your product’s icon right in the dashboard. Besides the fact that it’s cool, it’s also very helpful when you have multiple products on Freemius:  
![Freemius Dashboard Product Icon Upload](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-product-icon-upload.gif)

## Profile Picture Upload

You can now upload your profile picture in the profile section:  
![](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-developer-profile-picture-upload.png)

## Branded Invoices

All new invoices are now branded with your product’s featured icon:  
![Freemius Invoice Branded Icon Example](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-invoice-branded-icon.png)

In addition, we’re now including a thank you note with your configured support email address making it easier for customers to find your support channel:  
![Freemius Invoice Vendor Support Email](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-invoice-vendor-support-email.png)

## Auto-Generated EULA for Dispute Evidence Submission

Since we are the ones that currently handle disputes we are constantly looking for ways of making the process easier for us, as well as increase our chances of winning them for you. We have been pretty successful in winning PayPal disputes, but when it comes to credit cards, since the final decision is made by the customer’s bank, unless the counter evidence are really strong the banks are usually biased towards their customers. One of the things that we’ve recently added is an auto-generated EULA (End User License Agreement) out of your selected configuration and settings. The EULA is now added under the main CTA (call-to-action) purchase button as a “terms of license” link:  
![Freemius Checkout Terms of License Link](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-checkout-terms-of-license-link.png)

The EULA is focused on the refunds policy explanation about subscriptions and automatic renewals, cancellation, software updates, etc. and we include that link as part of the dispute evidence submission.

**Important:** This EULA is not a replacement to your agreement. You should have your own EULA on your site, covering things that are related to your plugins and themes specifics.

If you would like to check your EULA you can access it via:  
`https://freemius.com/terms/{id}/{slug}/`

We plan to include the EULA in the after purchase emails as well, making our evidence submission case even stronger.

## WordPress SDK 2.0.1 is OUT!

Since the [last Release Notes post](blog-cart-abandonment-recovery-themes-monetization.md), we’ve released 3 official versions of the SDK ([1.2.2.9](https://github.com/Freemius/wordpress-sdk/releases/tag/1.2.2.9), [1.2.3](https://github.com/Freemius/wordpress-sdk/releases/tag/1.2.3), [1.2.4](https://github.com/Freemius/wordpress-sdk/releases/tag/1.2.4)). Today we’re excited to [release version 2.0.1](https://github.com/Freemius/wordpress-sdk/releases/tag/2.0.1). The reason for the bump in the major version number is that we spend about 4 of the last months on integrating the SDK with WordPress multisite networks. We had to make major design changes of the storage model to offer a seamless experience in multi-site environments.

### Multisite Network-Level Integration

Just to clarify, the WordPress SDK was working fine with multi-sites before, but the UX wasn’t optimized. Your users had to opt-in or skip the activation for each site, and your customers had to activate their license key for every sub-site in the network. For instance, when a super-admin with a 20 sites network purchased a 25-site license for your product, they had to activate the license 20 times. Not very user-friendly 🙂 Even frustrating.

With the new integration, super-admins can now opt-in/skip/activate-license on the network level, making the UX way better. I can confidently say that this is the best multisite network-level integration on the market today! We made an elegant and seamless UX, while also very flexible when needed (keeping agencies in mind).

The special integration will only work for network activated plugins.

#### Network-Level Opt-In

When a user activates your plugin on a multisite network they will see the following opt-in screen:  
![Freemius Network-Level Opt-In](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-network-level-opt-in.png)

There are 2 new elements:

1. The “Apply on all sites in the network” checkbox.
2. The “Delegate to Site Admins” action link.

You’re probably asking yourself “what is the site-admins delegation option?” So let’s start with that. One of the use-cases for running a multisite network is hosting (e.g. WordPress.com is actually the largest WordPress multisite network). Consider the following scenario where a hosting provider would like to activate an “essential” plugin across their entire network, but doesn’t want to make the decision regarding the usage-tracking or licensing for the hosted sites. Robert Abela, who is a new Freemius partner (plugin seller), started to sell [WP Security Audit Log](https://www.wpsecurityauditlog.com/) with Freemius and is an excellent example for that use-case. They offer a plugin for audit log tracking, which is quite an essential product for every website to have. So when a small hosting company wishes to offer Robert’s plugin to their entire network they can easily do that, while delegating the management of the plugin to the site admins, without taking any actions in their behalf.

Now that we’re clear on the delegation part, let’s explore the new checkbox. When the checkbox is selected, the action that the super-admin will take will affect all of the sites on the network (including new ones that will be created). In case the super-admin would like to take different actions for different subsites they can uncheck the box and easily choose which action to take, per site:  
![Freemius Network-Level Opt-In Sites Selection](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-network-level-opt-in-sites-selection.png)

#### Network-Level License Activation

In a very similar manner, super-admins can activate a license across their entire network, delegate the license activation to site admins, or handpick which subsites to activate the license for:  
![Freemius Network-Level License Activation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-network-level-license-activation.png)

#### Network-Level Management

Super admins that didn’t delegate the activation to the site admins will now have an Account page on the network Admin, allowing them to manage the plugin on the network level without the need to open the Account for every subsite:  
![Freemius SDK Network Account Management](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-sdk-network-account-management.png)

Additionally, the Account page will not be shown on the site level at all.

#### How to Activate The Multisite Network Integration?

To activate the network-level integration you’ll need to update to the new SDK, but also make a small adjustment to the integration code. Go to your SDK INTEGRATION page in the Freemius Dashboard, where you’ll notice a new checkbox which will activate the network integration:  
![Freemius Dashboard Multisite-Network Integration Activation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-multisite-network-integration-activation.png)

### SDK Add-Ons Enhancements

If you’re selling freemium add-ons with a WordPress.org free version, the add-ons information dialog box now shows a new button to install the free WordPress.org add-on version:  
![Product description with cta button for free version and 7 day trial](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-sdk-freemium-addon-dialog.png)

A small but important addition is a new license activation button next to the installed add-ons in the Account page, allowing an easy way to activate a license:  
![Freemius WordPress SDK Add-on License Activation](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-sdk-addon-license-activation.png)

### SDK Localization Logic

We are excited to share that we have revamped our localization mechanism to avoid loading all of the SDK’s translatable strings into the memory on every request. This significantly reduces the memory consumption – only the used strings are now loaded into the memory.

**Important:** Please note that we’re deprecating the localization method `__fs()` since PHP7 throws a warning if there are functions/methods starting with two underscores. Please check your plugin/theme code and if you’re using this function replace it with the WP core `__()` method instead.

### WordPress SDK Bug Fixes

- The new SDK comes with a bunch of fixes related to the “\_\_clone exception” when cloning environments (staging/production). The SDK is now bulletproof against filesystem changes (changes in folder names) and symlink changes.
- Also, we add a recovery mechanism for cases when the user’s data disappears from the local storage. This is a major enhancement that should eliminate data corruption edge-cases.
- All paths are now stored as relative paths and not absolute, making sure migrations between environments work smoothly without triggering any “file not found” exceptions.
- Since shifting to SSLv3 we noticed that some outdated environments with old cURL and/or OpenSSL versions fail to properly handshake with our API server. Since it will take a while until all hosting providers will be ready for SSLv3 we added a fallback mechanism to HTTP for those outdated environments.

## Improved User & Developer Emails

### Refund Emails

Processing a refund will now trigger emails both for the refunded user, as well as for the product owner and admins. The email that you’ll receive upon a refund will also include the name of the person who processed the refund:  
![Freemius Developers Refund Email](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-developers-refund-email.png)

This is especially handy when you have a support team and like to know who’s processing refunds. To make it even more powerful, we plan to require a refund processing reason where the person that is processing the refund will need to provide an explanation for the refund. This is great for the sake of records, but also great for management to keep track of the refunds and know why a refund was processed.

### Enhanced PayPal After Subscription Emails

Since this is a recurring issue and we get support questions about this all the time, PayPal’s recurring profiles mechanism can take up to 24 hours until the initial payment is processed. If the customer cancels the profile before the payment was processed, the license is automatically expired after 24 hours and the user will not be able to use the paid features or the whole premium product. Therefore, we’ve added a new notice that is attached to the email sent to the customer after subscribing with PayPal, letting them know about it:  
![Freemius PayPal Subscription Email Initial Payment Notice](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-paypal-subscription-email-initial-payment-notice.png)

### Subscription Cancellation Emails

One of the common scenarios we identified is when customers contact your support and ask to cancel their subscription. While for some customers a response like “I just canceled your subscription, have a great day!” would be enough, many others would like to get some official confirmation of the cancellation. Therefore, we’ve added a subscription cancellation email that will automatically be sent to the customer upon cancellation.

### Billing Related Emails

From now on only the owner and the product admins will receive billing related emails about new subscriptions, payments, refunds, renewals, etc.

## Miscellaneous

Here’s a collection of additional things that are worth mentioning:

- Team members with a support role can now manage coupons. This was a good feedback that we’ve received from the FooPlugins team.
- After receiving feedback from one of our sellers informing us that their colorblind support rep can’t see a selected of an item in the table we modified the selected item’s color, making it more accessible for colorblind folks:  
  ![Freemius Dashboard Record Selection](https://freemius.com/blog/wp-content/uploads/2018/04/freemius-dashboard-record-selection.png)
- One of the common questions we’re getting from sellers and from buyers alike is what are considered to be localhost/development/staging addresses. We’ve finally documented it here:  
  [https://freemius.com/help/documentation/selling-with-freemius/license-utilization/](https://freemius.com/help/documentation/selling-with-freemius/license-utilization/) This list is a work-in-progress and based on your feedback and demand we’ll be adding more “localhost” domains to the list.
- The “Active” users filter in the USERS section of the Freemius Dashboard was finally implemented, so you can easily filter and download a CSV list of your currently active users. This is particularly useful for email campaigns.

## What’s next?

While we are big believers in keeping things right within the comfort zone of the WP Admin, during the past 3 years we learned that there are many use-cases that require a place where users and customers can access and control their data externally. Therefore, our next BIG project is an Embeddable Membership Area that you’ll be able to include right in your website or use as a standalone dashboard for your customers. We know that many of you are anxiously waiting for this so we will do our best to deliver it as soon as possible. We’ve already spent time talking with our sellers’ community and finalized the design, based on the feedback we received and the principals we’ve learned over the years, making sure we cover all use-cases.

**That’s it, hope you’re excited about all the new features (we know there are many of them) – let us know if you have any cool ideas for future features.**