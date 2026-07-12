---
title: "API and Configuration for Freemius Checkout"
url: "https://freemius.com/help/documentation/checkout/integration/freemius-checkout-buy-button/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:38+06:00"
word_count: 2963
---

The Freemius Checkout is highly customizable to fit your product and business needs. You'll find various configuration options to customize the checkout experience, as well as callbacks to handle different events during the checkout process.

If you're using the JavaScript-based [Overlay Checkout](help-documentation-checkout-integration-overlay-checkout.md), you can directly pass the configuration options and callbacks using the `FS.Checkout` constructor and its `open()` method.

```js
const checkout = new FS.Checkout({
  product_id: '<productID>',
  plan_id: '<planID>',
  // ... Other options
});

checkout.open({
  licenses: 10,
  // ... Other options and callbacks
  success: function (purchaseData) {
    console.log('Purchase completed!', purchaseData);
  },
});
```

If you're using the [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md), you can pass all the configuration options as URL parameters (except the callbacks). Learn more about it [here](help-documentation-checkout-integration-hosted-checkout.md#programmatically-generating-checkout-links).

Below, we'll go over all arguments you can pass to the `FS.Checkout` constructor and the `open()` method. We've divided them into two categories: [options](#checkout-options) and [callbacks](#callbacks).

## Checkout Options[​](#checkout-options "Direct link to Checkout Options")

`product_id`[](#product_id "Direct link to product_id")

number|string

REQUIRED

Required product ID (whether it's a plugin, theme, add-on, bundle, or SaaS).

`id`[](#id "Direct link to id")

string

An optional ID to set the `id` attribute of the checkout's `<body>` HTML element. This argument is particularly useful if you have multiple checkout instances that need a slightly different design or visibility of UI components. You can assign a unique ID for each instance and customize it differently using the CSS stylesheet that you can attach through the *Plans -&gt; Customization* in the Developer Dashboard.

`title`[](#title "Direct link to title")

string

OPTIONAL

Default: `{{ productTitle }} {{ planTitle }}`

An optional string to override the checkout’s title when buying a new license.

`image`[](#image "Direct link to image")

string

OPTIONAL

Default: `The product’s title set within the Freemius dashboard.`

An optional icon that loads in the checkout and will override the product's icon uploaded to the Freemius Dashboard. **Use a secure path to the image over HTTPS.** While the checkout will remain PCI compliant, credit-card automatic prefill by the browser will not work.

`plan_id`[](#plan_id "Direct link to plan_id")

number

OPTIONAL

Default: `The cheapest visible plan.`

The ID of the plan that will load with the checkout. When selling multiple plans, you can set the param when calling the `open()` method.

`licenses`[](#licenses "Direct link to licenses")

number

OPTIONAL

Default: `1`

The multi-site `licenses` pricing that will load immediately with the checkout. A developer-friendly param that can be used instead of the `pricing_id`. To specify **unlimited** licenses pricing, use one of the following values: `0`, `null`, or `'unlimited'`.

`disable_licenses_selector`[](#disable_licenses_selector "Direct link to disable_licenses_selector")

boolean

OPTIONAL

Default: `false`

Set this param to `true` if you would like to disable the licenses selector when the product is sold with multiple license activation options.

`hide_licenses`[](#hide_licenses "Direct link to hide_licenses")

boolean

OPTIONAL

Default: `false`

Set this param to `true` if you would like to entirely hide the 3rd row in the header with the license selector.

`pricing_id`[](#pricing_id "Direct link to pricing_id")

number

OPTIONAL

Default: `The plan’s single-site prices ID.`

**Use the [licenses](#licenses) param instead.**  
An optional ID of the exact multi-site license prices that will load once the checkout is opened.

`billing_cycle`[](#billing_cycle "Direct link to billing_cycle")

string

OPTIONAL

Default: `'annual'`

Allowed Values: `'monthly'` | `'annual'` | `'lifetime'`

An optional billing cycle that will be auto-selected when the checkout is opened.

`currency`[](#currency "Direct link to currency")

string

OPTIONAL

Allowed Values: `'usd'` | `'eur'` | `'gbp'` | `'auto'`

`auto` lets the checkout automatically choose the currency based on the geolocation of the user. With the `auto` option, you may also want to dynamically show the prices on your pricing page according to the user’s geo. Therefore, we created the [Checkout Geo API](help-documentation-checkout-features-local-languages-currencies.md#checkout-geo-api) to allow you to identify the browser's geolocation and currency that the checkout will use by default.

`default_currency`[](#default_currency "Direct link to default_currency")

string

OPTIONAL

Default: `usd`

You could use this when the `currency` param is set to `auto`. In this case, if the auto-detected currency is not associated with any pricing, this will be the fallback currency. To set the default currency of the pricing page and checkout within the WP Admin dashboard, use the [default\_currency](help-documentation-wordpress-sdk-filters-actions-hooks.md#default_currency) filter.

`coupon`[](#coupon "Direct link to coupon")

string

OPTIONAL

An optional coupon code to be automatically applied to the checkout immediately when opened.

See demo [preloading the checkout with a coupon](help-documentation-checkout-features-coupons.md#preload-the-checkout-with-coupon).

`hide_coupon`[](#hide_coupon "Direct link to hide_coupon")

boolean

OPTIONAL

Default: `false`

Set this param to `true` if you prepopulate a coupon and would like to hide the coupon code and coupon input field from the user.

See demo [preloading the checkout with a hidden coupon](help-documentation-checkout-features-coupons.md#preload-the-checkout-with-hidden-coupon).

`maximize_discounts`[](#maximize_discounts "Direct link to maximize_discounts")

boolean

OPTIONAL

DEPRECATED

Default: `true`

*This has been deprecated in favor of [bundle\_discount](#bundle_discount).*

Set this param to `false` when selling a bundle and you want the discounts to be based on the closest licenses quota and billing cycle from the child products. Unlike the default discounts calculation which is maximized by basing the discounts on the child products single-site prices.

Learn [how the automatic discounts work](help-documentation-checkout-features-automatic-discounts-in-checkout.md#annual_discount)

`trial`[](#trial "Direct link to trial")

boolean|string

OPTIONAL

Default: `false`

Allowed Values: `true` | `false` | `'free'` | `'paid'`

When set to `true`, it will open the checkout in trial mode, and the trial type (free vs. paid) will be based on the plan's configuration. This will only work if you've activated the [Free Trial functionality](help-documentation-selling-with-freemius-set-up-trials.md) in the plan configuration.

If you configured the plan to support a trial that doesn't require a payment method, you can also open the checkout in trial mode that requires a payment method by setting the value to `'paid'`.

`license_key`[](#license_key "Direct link to license_key")

string

OPTIONAL

An optional param to pre-populate a license key for license renewal, license extension and more.

`hide_license_key`[](#hide_license_key "Direct link to hide_license_key")

boolean

OPTIONAL

Default: `false`

Set this param to `true` if you would like to hide the option to manually enter a license key during checkout for existing license renewal.

`is_payment_method_update`[](#is_payment_method_update "Direct link to is_payment_method_update")

boolean

OPTIONAL

Default: `false`

An optional param to load the checkout for a payment method update. When set to `true`, the `license_key` params must be set and associated with a non-canceled subscription.

Generating Payment Method Update Flow from the API

Instead of generating the configuration manually you can check our [API documentation](https://docs.freemius.com/api/licenses/generate-upgrade-link) or [JS SDK documentation](help-documentation-saas-sdk-js-sdk-checkout.md#handling-upgrade-flow) to automate the flow.

`user_email`[](#user_email "Direct link to user_email")

string

OPTIONAL

An optional string to prefill the buyer’s email address.

`user_firstname`[](#user_firstname "Direct link to user_firstname")

string

OPTIONAL

An optional string to prefill the buyer’s first name.

`user_lastname`[](#user_lastname "Direct link to user_lastname")

string

OPTIONAL

An optional string to prefill the buyer’s last name.

`readonly_user`[](#readonly_user "Direct link to readonly_user")

boolean

OPTIONAL

Set this parameter to `true` to make the user details (name and email) readonly. This is useful for SaaS integration where you are loading the user email and their first and last name from your own DB.

`affiliate_user_id`[](#affiliate_user_id "Direct link to affiliate_user_id")

number

OPTIONAL

An optional user ID to associate purchases generated through the checkout with their affiliate account.

`language | locale`[](#language%20%7C%20locale "Direct link to language | locale")

string

OPTIONAL

If given the Checkout will load in the selected language and would also show an UI for the user to switch language. The value of the `language` or `locale` parameter could be one of the followings:

- **locale**: It can be a fully qualified locale code, for example: `en_US`, `de_DE` etc.
- **language**: It can be just the language code, for example: `en`, `de` or `fr` etc. If we have more than two locales available for a language, then we have a system in place where we define the preferred language by popularity. If you are unsure about it, then please use the fully qualified locale code instead.
- **auto** (recommended): The system will try to guess the language of your user by looking into the browser and then the geo-location respectively. However, this won’t select languages that are marked as AI-translated or beta for the time being. If we identify a locale that we don’t support right now, we’ll keep showing the English language. However we will still show the language selector UI.
- **auto-beta**: Same as above, but will also select a language marked as beta. When a language marked as beta is selected, the UI will also show a “BETA” tag near it.

tip

Our Checkout will always display the language selector UI to the buyer. If you wish to automatically load the Checkout in the buyer’s preferred language, please use the `auto` value.

`user_token`[](#user_token "Direct link to user_token")

string

OPTIONAL

An optional token which, if present, would pre-populate the checkout with the user's personal and billing data (for example, the name, email, country, VAT ID, etc.). [Learn more…](help-documentation-checkout-features-pre-populate-user-info.md#generating-user-tokens)

`layout`[](#layout "Direct link to layout")

string

OPTIONAL

Default: `null`

Allowed Values: `'vertical'` | `'horizontal'` | `'null'`

Specify the layout of the form on a larger screen. This cannot be horizontal in cases like payment method updates or free plans. If set to `null` the system will automatically choose the best default for the current checkout mode.

`form_position`[](#form_position "Direct link to form_position")

string

OPTIONAL

Default: `left`

Allowed Values: `'left'` | `'right'`

Specifies the position of the form in horizontal layout.

`fullscreen`[](#fullscreen "Direct link to fullscreen")

boolean

OPTIONAL

Default: `false`

If set to `true`, the Checkout dialog will take the entire screen when opened.

`show_upsells`[](#show_upsells "Direct link to show_upsells")

boolean

OPTIONAL

Default: `false`

Whether or not to show the upsell toggles.

`show_reviews`[](#show_reviews "Direct link to show_reviews")

boolean

OPTIONAL

Default: `false`

Whether or not to show the featured reviews in the checkout. By default, it will be shown if the checkout page is loaded directly, without any JS snippet (iFrame) integration call.

`review_id`[](#review_id "Direct link to review_id")

number

OPTIONAL

When showing the review UI in the checkout, you can specify which review you want to show with its ID. By default the latest featured review will be shown.

`show_refund_badge`[](#show_refund_badge "Direct link to show_refund_badge")

boolean

OPTIONAL

Default: `false`

Whether or not to show the Refund Policy UI in the checkout. By default, it will be shown if the checkout page is loaded directly, without any JS snippet (iFrame) integration call.

`refund_policy_position`[](#refund_policy_position "Direct link to refund_policy_position")

string

OPTIONAL

Default: `dynamic`

Allowed Values: `'below_form'` | `'below_breakdown'` | `'dynamic'`

Use the parameter to position the refund policy badge when showing the form in horizontal layout. By default with the `'dynamic'` value, it will be positioned either below the form or the breakdown column.

`annual_discount`[](#annual_discount "Direct link to annual_discount")

boolean

OPTIONAL

Default: `true`

Determines whether the annual discount will be shown in the checkout. Learn [how the automatic discounts work](help-documentation-checkout-features-automatic-discounts-in-checkout.md)

`show_monthly`[](#show_monthly "Direct link to show_monthly")

boolean

OPTIONAL

Default: `false`

Switching to the monthly billing cycle is disabled when the Checkout is loaded with an annual billing cycle. Use this parameter to show it.

- Setting the value to `true` may not display the upsell toggle UI. It will show up only if the annual pricing has some discount associated with it. In case your single unit pricing doesn't have a monthly price set, you would need to disable the multisite discount by using `multisite_discount=false` for the system to calculate the annual discount from the currently selected license units instead of the single license unit.
- If you are using the `billing_cycle_selector` UI, then `show_monthy` will always display the monthly option regardless of any discount associated with it.

Learn [how the automatic discounts work](help-documentation-checkout-features-automatic-discounts-in-checkout.md)

`multisite_discount`[](#multisite_discount "Direct link to multisite_discount")

boolean|string

OPTIONAL

Default: `'auto'`

Allowed Values: `true` | `false` | `'auto'`

Determines whether the multi-site discount will be shown. When the value is `'auto'`, the discount will only be shown if the single license pricing difference does not exceed 10 times more than the current pricing.

Learn [how the automatic discounts work](help-documentation-checkout-features-automatic-discounts-in-checkout.md#multi_unit_discount)

`bundle_discount`[](#bundle_discount "Direct link to bundle_discount")

boolean|string

OPTIONAL

Default: `'maximize'`

Allowed Values: `true` | `false` | `'maximize'`

Determines whether the bundle discount will be shown. The bundle discount itself depends on the compound price of its children. By default with maximize, we try to take the compound price from the lowest billing cycle and license. But with the value of true, we take it from the closest billing cycle and licenses.

Learn [how the automatic discounts work](help-documentation-checkout-features-automatic-discounts-in-checkout.md#bundle_discount)

`show_inline_currency_selector`[](#show_inline_currency_selector "Direct link to show_inline_currency_selector")

boolean

OPTIONAL

Default: `true`

Set it to `false` to hide the inline currency selector from the "Today’s Total" line.

`cancel_url`[](#cancel_url "Direct link to cancel_url")

string

OPTIONAL

When the checkout is loaded in `page`, you can specify a cancel URL to be used for the back button. By default, if you link Freemius Checkout from your website, it will be picked up from the `Referer` header (if present). Using this option, you can override the URL as needed.

`cancel_icon`[](#cancel_icon "Direct link to cancel_icon")

string

OPTIONAL

By default, the website icon (also known as favicon) will be rendered alongside the cancel button. If you want to use any other icon image, please specify the link to the icon using this parameter.

`always_show_renewals_amount`[](#always_show_renewals_amount "Direct link to always_show_renewals_amount")

boolean

OPTIONAL

Default: `false`

When set to `true`, a small line mentioning the total renewal price per billing cycle will be shown below the total. By default, it only shows up when there is a renewal discount involved.

`is_bundle_collapsed`[](#is_bundle_collapsed "Direct link to is_bundle_collapsed")

boolean

OPTIONAL

Default: `true`

Determines whether the products in a bundle appear hidden by default. Is applicable only to bundles.

`billing_cycle_selector`[](#billing_cycle_selector "Direct link to billing_cycle_selector")

string

OPTIONAL

Default: `null`

Allowed Values: `'list'` | `'responsive_list'` | `'dropdown'`

If present, it will show the billing cycle selector UI in the Checkout. Read more about it [here](help-documentation-checkout-features-billing-cycle-selector-ui.md).

`show_confirmation_dialog`[](#show_confirmation_dialog "Direct link to show_confirmation_dialog")

boolean

OPTIONAL

Default: `true`

Determines whether or not to show the confirmation dialog after a successful purchase. Learn more about it [here](help-documentation-checkout-customization-customizing-confirmation-dialog.md).

`sandbox`[](#sandbox "Direct link to sandbox")

{token: string; ctx: string;}

OPTIONAL

Default: `1`

If you want to test the checkout in the sandbox environment, you need to provide a `sandbox` object with the `token` and `ctx` values. You can generate these values from the Freemius Dashboard. Learn more about it [here](help-documentation-saas-sdk-checkout-js-sdk-usage.md#sandbox-testing).

`gdpr`[](#gdpr "Direct link to gdpr")

string

OPTIONAL

Default: `default`

Allowed Values: `'default'` | `'opt_out'` | `'hidden'`

Determines whether to show the marketing consent UI in the checkout and, if shown, its default state. Learn more [here](help-documentation-checkout-features-gdpr.md).

`cart`[](#cart "Direct link to cart")

boolean

OPTIONAL

Default: `true`

When set to `false`, this parameter disables the [cart abandonment recovery](help-documentation-marketing-automation-cart-abandonment-recovery.md) mechanism.

A common use case for setting this parameter to `false` is during short-term promotional campaigns lasting less than 24 hours. In such cases, sending a cart recovery reminder 24 hours after an incomplete purchase may no longer be relevant once the promotion has ended.

As a general best practice, this parameter should remain set to `true` to maximize cart recovery opportunities. This parameter is GDPR-compliant.

tip

All the parameters can be preset when creating the checkout using `new FS.Checkout({ /* options */ })`. If you need to set different param values based on the user's selection, you can set all the params except `product_id` when executing the `checkout.open()` method.

## Callbacks[​](#callbacks "Direct link to Callbacks")

`cancel`[](#cancel "Direct link to cancel")

callable

OPTIONAL

A callback handler that will execute when a user closes the checkout by clicking the close icon. This handler only executes when the checkout is running in `dialog` mode.

`purchaseCompleted`[](#purchaseCompleted "Direct link to purchaseCompleted")

callable(data: Object)

OPTIONAL

A callback handler executed after successful purchase/subscription completion. The structure of the argument is detailed [here](#user--purchase-data-in-callbacks).

note

When the user subscribes to a recurring billing plan, this method will execute upon successful subscription creation. It doesn't guarantee that the subscription's initial payment was processed successfully as well. If you'd like to use this method for the in-dashboard/WP-Admin checkout, you'll need to use a special filter named [`checkout/purchasedCompleted`](help-documentation-wordpress-sdk-filters-actions-hooks.md#checkoutpurchasedcompleted).

`success`[](#success "Direct link to success")

callable(data: Object)

OPTIONAL

An optional callback handler, similar to `purchaseCompleted` but only triggered after the [confirmation dialog](help-documentation-checkout-customization-customizing-confirmation-dialog.md) is closed.

The structure of the argument is detailed [here](#user_purchase_data_in_callbacks). The main difference is that this callback will only execute after the user clicks the **"Got It"** button that appears in the post-purchase screen as a declaration that they successfully received the post-purchase email. This callback is obsolete when the checkout is running in `dashboard` mode.

`track`[](#track "Direct link to track")

callable(event: String, data: Object)

OPTIONAL

An optional callback handler for advanced tracking, which will be called on multiple checkout events such as updates in the currency, billing cycle, licenses #, etc.

## User & Purchase Data in Callbacks[​](#user--purchase-data-in-callbacks "Direct link to User & Purchase Data in Callbacks")

If you're hooking into the `success` or `purchaseCompleted` callbacks for advanced integrations, you can retrieve purchase and user information from the first argument passed to your callback. For example:

```javascript
checkout.open({
  success(data) {
    // Get the user
    console.log(data.user);
    // Get the purchase
    console.log(data.purchase);
    // Get the free trial
    console.log(data.trial);
  },
});
```

### The `user` Object[​](#the-user-object "Direct link to the-user-object")

Contains details about the user who completed the purchase:

- `email`: Buyer's email address
- `first`: First name
- `last`: Last name
- `id`: Freemius user ID

### The `purchase` Object[​](#the-purchase-object "Direct link to the-purchase-object")

The `purchase` object differs depending on whether the transaction is a subscription or a one-off payment. Key properties include:

- `plan_id`: ID of the purchased plan
- `license_id`: ID of the license created or updated
- `subscription_id`: ID of the subscription (only present for subscriptions)
- `billing_cycle`: Subscription billing frequency (only present for subscriptions)

TypeScript Intellisense

The full structure is documented in our [repository](https://github.com/Freemius/freemius-checkout-js/blob/main/src/lib/contracts/CheckoutResponse.ts). If you're using the [@freemius/checkout](help-documentation-saas-sdk-checkout-js-sdk.md) package, you'll get full IDE type intellisense support.

### The `trial` Object[​](#the-trial-object "Direct link to the-trial-object")

The `trial` object is only present if the purchase includes a free trial. It contains the following important properties:

- `license_id`: The ID of the license associated with the trial
- `trial_ends_at`: The date-time indicating when the trial period ends

Just like the `purchase` object, the full structure of the `trial` object is documented in our [repository](https://github.com/Freemius/freemius-checkout-js/blob/main/src/lib/contracts/CheckoutResponse.ts).