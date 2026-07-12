---
title: "Filters & Actions Hooks"
url: "https://freemius.com/help/documentation/wordpress-sdk/filters-actions-hooks/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 1909
---

The Freemius WordPress SDK provides a collection of filters and actions that allow developers to customize and extend the functionality of their WordPress plugins or themes.

The concept is similar to WordPress’ own filters and actions also known as [hooks](https://developer.wordpress.org/plugins/hooks/).

## Using Freemius Hooks[​](#using-freemius-hooks "Direct link to Using Freemius Hooks")

Using the Freemius hooks requires access to the Freemius instance, which is typically available in the main plugin file or wherever the SDK is initialized.

### Direct Usage[​](#direct-usage "Direct link to Direct Usage")

In your theme or plugin, you can use the standard `add_action()` or `add_filter()` functions via the Freemius instance, namely;

- `my_fs()->add_action()`
- `my_fs()->add_filter()`

An example using the direct method.

```php
my_fs()->add_action( 'after_license_activation', 'my_fs_after_license_activation' );

function my_fs_after_license_activation() {
    // Handle successful activation.
}

```

note

Ensure to change `my_fs()` to your actual Freemius instance prefix.

### Unique Hook Names[​](#unique-hook-names "Direct link to Unique Hook Names")

Similar to WordPress hooks, you can use a unique hook name for your product to avoid conflicts with other plugins or themes that might be using the same hook name.

The naming convention for creating unique hook names is as follows:

- The hook starts with `fs_` to identify it as a Freemius SDK hook.
- Second, include the action name, e.g., `after_license_change`.
- Finally, add the product slug at the end.
  
  - For plugins, add `my-plugin-slug`. Replace `my-plugin-slug` with the actual plugin slug.
  - For themes, add `my-theme-slug-theme`. Replace `my-theme-slug` with the actual theme slug before the suffix `-theme`.

Example: A product with the slug `awesome-plugin` using `playground_anonymous_mode` filter hook.

```php
add_filter( 'fs_playground_anonymous_mode-awesome-plugin', '__return_false' );
```

tip

The hook priorities and accepted arguments work the same way as in WordPress core e.g., see the [`is_submenu_visible`](#is_submenu_visible) filter hook.

## Filters Hooks[​](#filters-hooks "Direct link to Filters Hooks")

Filters allow developers to modify specific data or behavior within the Freemius SDK. To add a filter, use the following method from the Freemius instance:

```php
my_fs()->add_filter(
  string $tag,
  callable $callback,
  $priority = 10,
  $accepted_args = 1
);
```

The method signature is the same as WordPress' [add\_filter](https://developer.wordpress.org/reference/functions/add_filter/) function. The following filters are available:

### `default_currency`[​](#default_currency "Direct link to default_currency")

Set the default currency of the pricing page and checkout within the WP Admin dashboard.

```php
function my_fs_default_currency( $currency ) {
     return 'eur';
}

my_fs()->add_filter( 'default_currency', 'my_fs_default_currency' );
```

### `connect_url`[​](#connect_url "Direct link to connect_url")

Modifies the URL used for the activation screen.

### `trial_promotion_message`[​](#trial_promotion_message "Direct link to trial_promotion_message")

Customizes the message in the admin notice promoting trial usage to users.

### `is_long_term_user`[​](#is_long_term_user "Direct link to is_long_term_user")

Determines if a user is considered long-term based on custom criteria. The uninstall reasons shown in the deactivation feedback dialog are determined based on this user type.

### `uninstall_reasons`[​](#uninstall_reasons "Direct link to uninstall_reasons")

Defines the reasons presented to users in the deactivation feedback dialog during product deactivation.

### `is_plugin_update`[​](#is_plugin_update "Direct link to is_plugin_update")

Checks if Freemius was first added in a product update.

### `api_domains`[​](#api_domains "Direct link to api_domains")

Specifies API domains to include in an activation error message about domains that need to be whitelisted.

### `support_forum_submenu`[​](#support_forum_submenu "Direct link to support_forum_submenu")

Manages the visibility of the support forum submenu.

### `support_forum_url`[​](#support_forum_url "Direct link to support_forum_url")

Sets the URL for the support forum link for the product.

```php
my_fs()->add_filter( 'support_forum_url', function ( $url ) {
    return 'https://awesome-plugin.com/support-forum/';
});
```

### `pricing_url`[​](#pricing_url "Direct link to pricing_url")

Override the default Freemius WordPress SDK pricing page. The \`$url\` parameter can be set to any other link e.g. website.

```php
my_fs()->add_filter( 'pricing_url', function ( $url ) {
    return 'https://awesome-plugin.com/pricing/';
});
```

### `connect_message`[​](#connect_message "Direct link to connect_message")

Customizes the message displayed during the activation process.

### `connect_message_on_update`[​](#connect_message_on_update "Direct link to connect_message_on_update")

Adjusts the connection message shown during the activation process when Freemius was first added in a product update.

### `show_deactivation_subscription_cancellation`[​](#show_deactivation_subscription_cancellation "Direct link to show_deactivation_subscription_cancellation")

Disable the subscription cancellation prompt when deactivating the plugin.

```php
my_fs()->add_filter( 'show_deactivation_subscription_cancellation', '__return_false' );
```

### `uninstall_confirmation_message`[​](#uninstall_confirmation_message "Direct link to uninstall_confirmation_message")

Customizes the confirmation message to show in an additional panel within the deactivation feedback dialog before the panel with the deactivation reasons is shown.

### `pending_activation_message`[​](#pending_activation_message "Direct link to pending_activation_message")

Customizes the message shown when activation is pending (when it requires completion by clicking an activation link sent via email).

### `is_submenu_visible`[​](#is_submenu_visible "Direct link to is_submenu_visible")

Controls the visibility of specific submenus for the product. Here is an example to conditionally show the contact submenu item for customers with a trial or are paying.

```php
function my_fs_submenu_visibility_handler( $is_visible, $id ) {
    if ( 'contact' === $id ) {
        $is_visible = my_fs()->is_paying_or_trial();
    }

    return $is_visible;
}

my_fs()->add_filter( 'is_submenu_visible', 'my_fs_submenu_visibility_handler', 10, 2 );
```

### `plugin_icon`[​](#plugin_icon "Direct link to plugin_icon")

Sets the icon displayed for the product. This affects the icon on the activation page, pricing page, and the updates section.

### `show_trial`[​](#show_trial "Direct link to show_trial")

Helps determine whether the Free Trial tab or the trial promotion admin notice should be shown.

### `is_pricing_page_visible`[​](#is_pricing_page_visible "Direct link to is_pricing_page_visible")

Controls the visibility of the pricing link for the product.

### `pricing/show_annual_in_monthly`[​](#pricingshow_annual_in_monthly "Direct link to pricingshow_annual_in_monthly")

By default, the pricing page shows monthly prices.

However, this behavior can be changed in the pricing page by including this single line of code in your SDK integration code and the pricing app will show the actual annual amounts.

```php
my_fs()->add_filter( 'pricing/show_annual_in_monthly', '__return_false' );
```

### `checkout/parameters`[​](#checkoutparameters "Direct link to checkoutparameters")

Allows you to customize the Checkout with a subset of the options available in the [Checkout JS API](help-documentation-checkout-integration-freemius-checkout-buy-button.md). For example, the snippet below enables the refund badge and reviews, and sets the billing cycle selector to a dropdown (bypassing the upsells UI).

**Example**

```php
my_fs()->add_filter( 'checkout/parameters', function ( $existing_params ) {
    // You can use the $existing_params to check how the checkout is currently configured.
    // Everything you return from this callback will override the existing parameters.
    return [
        'show_refund_badge' => true,
        'show_reviews' => true,
        'billing_cycle_selector' => 'dropdown',
    ];
} );
```

To ensure the core checkout logic is not broken, only a specific set of keys is supported.

- [currency](help-documentation-checkout-integration-freemius-checkout-buy-button.md#currency)
- [default\_currency](help-documentation-checkout-integration-freemius-checkout-buy-button.md#default_currency)
- [always\_show\_renewals\_amount](help-documentation-checkout-integration-freemius-checkout-buy-button.md#always_show_renewals_amount)
- [annual\_discount](help-documentation-checkout-integration-freemius-checkout-buy-button.md#annual_discount)
- [billing\_cycle](help-documentation-checkout-integration-freemius-checkout-buy-button.md#billing_cycle)
- [billing\_cycle\_selector](help-documentation-checkout-integration-freemius-checkout-buy-button.md#billing_cycle_selector)
- [bundle\_discount](help-documentation-checkout-integration-freemius-checkout-buy-button.md#bundle_discount)
- [maximize\_discounts](help-documentation-checkout-integration-freemius-checkout-buy-button.md#maximize_discounts)
- [multisite\_discount](help-documentation-checkout-integration-freemius-checkout-buy-button.md#multisite_discount)
- [show\_inline\_currency\_selector](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_inline_currency_selector)

<!--THE END-->

- [form\_position](help-documentation-checkout-integration-freemius-checkout-buy-button.md#form_position)
- [is\_bundle\_collapsed](help-documentation-checkout-integration-freemius-checkout-buy-button.md#is_bundle_collapsed)
- [layout](help-documentation-checkout-integration-freemius-checkout-buy-button.md#layout)
- [refund\_policy\_position](help-documentation-checkout-integration-freemius-checkout-buy-button.md#refund_policy_position)
- [show\_refund\_badge](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_refund_badge)
- [show\_reviews](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_reviews)
- [title](help-documentation-checkout-integration-freemius-checkout-buy-button.md#title)
- [show\_monthly](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_monthly)
- [show\_upsells](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_upsells)

### `checkout/purchasedCompleted`[​](#checkoutpurchasedcompleted "Direct link to checkoutpurchasedcompleted")

Add custom JavaScript code to run after the user has successfully made a purchase. For example

```php
my_fs()->add_filter('checkout/purchaseCompleted', function () {
    return <<<JS
function (data) {
    return fetch(myPlugin.ajaxUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            action: 'my_plugin_purchase_completed',
            data: data,
            nonce: myPlugin.nonce,
        }),
    });
}
JS;
```

You can return a [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) from the JS callback function and the UI will wait for the promise to resolve until the page is redirected. However for a seamless experience, we suggest to send a [beacon request](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon). Here is an [example to track Google Analytics](https://gist.github.com/vovafeldman/a19a6c92838dcaa416ec7063a01dc6c9).

### `playground_anonymous_mode`[​](#playground_anonymous_mode "Direct link to playground_anonymous_mode")

On [sandbox/playground sites](https://github.com/Freemius/wordpress-sdk/blob/master/includes/entities/class-fs-site.php#L219), the opt-in process is skipped by default to allow for easier testing. This filter disables the playground anonymous mode, so the opt-in process is enabled when using the product on the playground sites.

```php
add_filter( 'fs_playground_anonymous_mode-awesome-plugin-slug', '__return_false' );
```

### `show_customizer_upsell`[​](#show_customizer_upsell "Direct link to show_customizer_upsell")

Deactivate/remove the customizer upsell in the wordpress theme customizer.

```php
add_filter( 'fs_show_customizer_upsell-awesome-theme-slug-theme', '__return_false' );
```

## Actions Hooks[​](#actions-hooks "Direct link to Actions Hooks")

Actions enable developers to execute custom code at specific points during the product’s execution. To add an action, use the following method from the Freemius instance:

```php
my_fs()->add_action( string $tag, callable $function_to_add, $priority = 10, $accepted_args = 1 );
```

This method signature is similar to WordPress' [add\_action](https://developer.wordpress.org/reference/functions/add_action/) function. The following actions are available:

### `after_license_change`[​](#after_license_change "Direct link to after_license_change")

Executed after a license change occurs.

```php
my_fs()->add_action( 'after_license_change', 'my_fs_log_after_license_change', 10, 2 );

function my_fs_log_after_license_change( $status, $plan ) {
    error_log( print_r( 'License status: ' . $status, true ) );
    error_log( print_r( 'Plan:', true ) );
    error_log( print_r( $plan, true ) );
}
```

### `after_license_activation`[​](#after_license_activation "Direct link to after_license_activation")

Executed after a license activation occurs. Example:

```php
my_fs()->add_action( 'after_license_activation', 'my_fs_after_license_activation' );

function my_fs_after_license_activation() {
    // Handle successful activation.
}
```

On execution, this hook returns two arguments:

- The status as a string, depending on the license change type (e.g., `changed`).
- The plan object with a schema similar to the [retrieve a plan](https://docs.freemius.com/api/plans/retrieve) API endpoint.

### `after_license_deactivation`[​](#after_license_deactivation "Direct link to after_license_deactivation")

Executed after a license deactivation occurs. Example:

```php
my_fs()->add_action( 'after_license_deactivation', 'my_fs_after_license_deactivation' );

function my_fs_after_license_deactivation( $license ) {
    if ( ! empty( $license->id ) ) {
        // Success, do something with the license.
    } else {
        // Failure, handle the error.
        // echo $license->error->code;
        // echo $license->error->message;
    }
}
```

On execution, the hook provides a license object with a schema similar to the [retrieve a license](https://docs.freemius.com/api/licenses/retrieve) API endpoint.

### `after_plans_sync`[​](#after_plans_sync "Direct link to after_plans_sync")

Runs after the product's plans are synchronized with Freemius.

### `after_account_details`[​](#after_account_details "Direct link to after_account_details")

Triggered after account details on the “Account” page are outputted (before the billing and payments sections).

### `after_account_user_sync`[​](#after_account_user_sync "Direct link to after_account_user_sync")

Executed after user account synchronization.

### `after_account_plan_sync`[​](#after_account_plan_sync "Direct link to after_account_plan_sync")

Runs after account plan synchronization.

### `before_account_load`[​](#before_account_load "Direct link to before_account_load")

Triggered before an account is loaded.

### `after_account_connection`[​](#after_account_connection "Direct link to after_account_connection")

Executed after a successful activation connection (when an account is successfully created).

### `account_email_verified`[​](#account_email_verified "Direct link to account_email_verified")

Triggered when an account email address is verified.

### `account_page_load_before_departure`[​](#account_page_load_before_departure "Direct link to account_page_load_before_departure")

Executed before finishing the loading of the Account page.

### `before_account_delete`[​](#before_account_delete "Direct link to before_account_delete")

Runs before an account is deleted.

### `after_account_delete`[​](#after_account_delete "Direct link to after_account_delete")

Executed after an account is deleted.

### `sdk_version_update`[​](#sdk_version_update "Direct link to sdk_version_update")

Triggered after the SDK version is updated.

### `plugin_version_update`[​](#plugin_version_update "Direct link to plugin_version_update")

Executed after the product version is updated.

### `initiated`[​](#initiated "Direct link to initiated")

Runs after the Freemius SDK is initialized.

### `after_init_plugin_registered`[​](#after_init_plugin_registered "Direct link to after_init_plugin_registered")

Runs after the Freemius SDK is initialized and the user is registered.

### `after_init_plugin_anonymous`[​](#after_init_plugin_anonymous "Direct link to after_init_plugin_anonymous")

Runs after the Freemius SDK is initialized and the user is anonymous.

### `after_init_plugin_pending_activations`[​](#after_init_plugin_pending_activations "Direct link to after_init_plugin_pending_activations")

Runs after the Freemius SDK is initialized and the user’s activation is pending confirmation.

### `after_init_addon_registered`[​](#after_init_addon_registered "Direct link to after_init_addon_registered")

Runs after the Freemius SDK is initialized for an add-on and the user is registered.

### `after_init_addon_anonymous`[​](#after_init_addon_anonymous "Direct link to after_init_addon_anonymous")

Runs after the Freemius SDK is initialized for an add-on and the user is anonymous.

### `after_init_addon_pending_activations`[​](#after_init_addon_pending_activations "Direct link to after_init_addon_pending_activations")

Runs after the Freemius SDK is initialized for an add-on and the user’s activation is pending confirmation.

### `after_premium_version_activation`[​](#after_premium_version_activation "Direct link to after_premium_version_activation")

Triggered after a premium version of the product is activated.

### `after_free_version_reactivation`[​](#after_free_version_reactivation "Direct link to after_free_version_reactivation")

Executed after reactivating the free version of the product.

### `after_uninstall`[​](#after_uninstall "Direct link to after_uninstall")

Runs after the product is uninstalled.

### `before_admin_menu_init`[​](#before_admin_menu_init "Direct link to before_admin_menu_init")

Runs before the product’s menu and submenus are added.

## More action hooks[​](#more-action-hooks "Direct link to More action hooks")

We have more action hooks related to the:

- [Opt-In Screen](help-documentation-wordpress-sdk-opt-in-message.md#advanced-opt-in-customization-actions)

## Checking if a hook is registered[​](#checking-if-a-hook-is-registered "Direct link to Checking if a hook is registered")

Just like in WordPress core, the Freemius SDK instance provides a `has_filter()` method, which you can use to check whether a specific hook has been registered. This works for both actions and filters. The method signature is:

```php
my_fs()->has_filter( string $tag, callable|bool $function_to_check );
```

You can omit the second parameter to check for any registered filter or action.