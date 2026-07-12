---
title: "Misc Gists"
url: "https://freemius.com/help/documentation/wordpress-sdk/gists/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 1553
---

## Adding new permission to the opt-in[​](#adding-new-permission-to-the-opt-in "Direct link to Adding new permission to the opt-in")

```php
<?php
  function add_helpscount_permission( $permissions ) {
    $permissions['helpscout'] = array(
      'id'          => 'helpscout', // Unique permission id.
      'icon-class'  => 'dashicons <yourIconClass>',
      'label'       => __( 'Help Scout', 'my_plugin_slug' ),
      'tooltip'     => __( 'Get easy access to our support via Help Scout Beacon.', 'my_plugin_slug' ),  // Optional tooltip.
      'desc'        => __( 'Rendering Help Scout\'s beacon for easy support access', 'my_plugin_slug' ),
      'priority'    => 16,
      /**
       * The permission layer is currently only persistent with built-in permissions.
       * So if you make this permission optional, you won't be able to determine if the user switched it on or off.
       */
      'is_optional' => false,
      'default'     => true,
    );

    return $permissions;
  }

  my_fs()->add_filter( 'permission_list', 'add_helpscount_permission' );
```

```php
<?php
  if (
    // Checks if user opted-in (or activated a license).
    my_fs()->is_registered() &&
    // Checks if user didn't opt out from tracking.
    my_fs()->is_tracking_allowed()
  ) {
    // Render Help Scout Beacon.
    require_once( '../path/to/help-scout-beacon.php' );
  }
```

## Customizing the support forum URL for the premium code version[​](#customizing-the-support-forum-url-for-the-premium-code-version "Direct link to Customizing the support forum URL for the premium code version")

```php
<?php
  function my_premium_support_forum_url( $wp_org_support_forum_url ) {
    return 'https://my-awesome-site.com/forum/';
  }

  if ( my_fs()->is_premium() ) {
    my_fs()->add_filter( 'support_forum_url', 'my_premium_support_forum_url' );
  }
```

## Show the contact submenu item only when the user have a valid non-expired license[​](#show-the-contact-submenu-item-only-when-the-user-have-a-valid-non-expired-license "Direct link to Show the contact submenu item only when the user have a valid non-expired license")

```php
<?php
  /**
   * Show the contact submenu item only when the user have a valid non-expired license.
   *
   * @param $is_visible The filtered value. Whether the submenu item should be visible or not.
   * @param $menu_id    The ID of the submenu item.
   *
   * @return bool If true, the menu item should be visible.
   */
  function my_custom_is_submenu_visible( $is_visible, $menu_id ) {
    if ( 'contact' != $menu_id ) {
      return $is_visible;
    }

    return my_fs()->can_use_premium_code();
  }

  my_fs()->add_filter( 'is_submenu_visible', 'my_custom_is_submenu_visible', 10, 2 );

```

## Add permission for adding Help Scout Beacon[​](#add-permission-for-adding-help-scout-beacon "Direct link to Add permission for adding Help Scout Beacon")

```php
<?php
  function add_helpscount_permission( $permissions ) {
    $permissions['helpscout'] = array(
      'id'          => 'helpscout', // Unique permission id.
      'icon-class'  => 'dashicons <yourIconClass>',
      'label'       => __( 'Help Scout', 'my_plugin_slug' ),
      'tooltip'     => __( 'Get easy access to our support via Help Scout Beacon.', 'my_plugin_slug' ),  // Optional tooltip.
      'desc'        => __( 'Rendering Help Scout\'s beacon for easy support access', 'my_plugin_slug' ),
      'priority'    => 16,
      /**
       * The permission layer is currently only persistent with built-in permissions.
       * So if you make this permission optional, you won't be able to determine if the user switched it on or off.
       */
      'is_optional' => false,
      'default'     => true,
    );

    return $permissions;
  }

  my_fs()->add_filter( 'permission_list', 'add_helpscount_permission' );
```

```php
<?php
  if (
    // Checks if user opted-in (or activated a license).
    my_fs()->is_registered() &&
    // Checks if user didn't opt out from tracking.
    my_fs()->is_tracking_allowed()
  ) {
    // Render Help Scout Beacon.
    require_once( '../path/to/help-scout-beacon.php' );
  }
```

## Controlling the in-dashboard trial promotion in the Freemius WordPress SDK[​](#controlling-the-in-dashboard-trial-promotion-in-the-freemius-wordpress-sdk "Direct link to Controlling the in-dashboard trial promotion in the Freemius WordPress SDK")

```php
<?php
my_fs()->override_i18n( array(
    'hey'                                        => 'Hey',
    'trial-x-promotion-message'                  => 'Thank you so much for using %s!',
    'already-opted-in-to-product-usage-tracking' => 'How do you like %s so far? Test all our %s premium features with a %d-day free trial.',
    'start-free-trial'                           => 'Start free trial',
    // Trial with a payment method required.
    'no-commitment-for-x-days'                   => 'No commitment for %s days - cancel anytime!',
    // Trial without a payment method.
    'no-cc-required'                             => 'No credit card required',
) );

#----------------------------------------------------------------------------------
#region Show the 1st trial promotion after 7 days instead of 24 hours.
#----------------------------------------------------------------------------------

function my_show_first_trial_after_7_days( $day_in_sec ) {
    // 7 days in sec.
    return 7 * 24 * 60 * 60;
}

my_fs()->add_filter( 'show_first_trial_after_n_sec', 'my_show_first_trial_after_7_days' );

#endregion

#----------------------------------------------------------------------------------
#region Re-show the trial promotional offer after every 60 days instead of 30 days.
#----------------------------------------------------------------------------------

function my_reshow_trial_after_every_60_days( $thirty_days_in_sec ) {
    // 60 days in sec.
    return 60 * 24 * 60 * 60;
}

my_fs()->add_filter( 'reshow_trial_after_every_n_sec', 'my_reshow_trial_after_every_60_days' );

#endregion

#----------------------------------------------------------------------------------
#region Add custom action after trial start/expiration
#----------------------------------------------------------------------------------

function my_after_license_change_handler( $plan_change_desc, FS_Plugin_Plan $plan) {
    $plan_name = $plan->name;

    switch( $plan_change_desc ) {
        case 'trial_started':
            // Do something immediately after a trial is started.
            break;
        case 'trial_expired':
            // Do something immediately after a trial expiration.
            break;
    }
}

my_fs()->add_action( 'after_license_change', 'my_after_license_change_handler', 10, 2);

#endregion
```

## EDD to Freemius Pricing Page Override based on URLs / Href[​](#edd-to-freemius-pricing-page-override-based-on-urls--href "Direct link to EDD to Freemius Pricing Page Override based on URLs / Href")

```html
<script src="https://checkout.freemius.com/checkout.min.js"></script>
<script>
  (function ($) {
    $(document).ready(function () {
      var handler = FS.Checkout.configure({
        plugin_id: '<product_id>',
        plan_id: '<plan_id>',
        public_key: '<product_public_key>',
      });

      $('.purchase a').on('click', function (e) {
        debugger;
        var $this = $(this),
          href = $this.attr('href'),
          price_id = parseInt(href.substr(-1), 10),
          licenses = 1,
          billing_cycle = 'annual';

        switch (price_id) {
          case 2:
            licenses = 3;
            break;
          case 3:
            licenses = 25;
            break;
          case 4:
            licenses = 25;
            billing_cycle = 'lifetime';
            break;
          case 1:
          default:
            licenses = 1;
            break;
        }

        handler.open({
          licenses: licenses,
          billing_cycle: billing_cycle,
        });

        e.preventDefault();

        return false;
      });
    });
  })(jQuery);
</script>
```

## Freemius submenu items visibility filter[​](#freemius-submenu-items-visibility-filter "Direct link to Freemius submenu items visibility filter")

```php
<?php
function my_is_submenu_visible($is_visible, $submenu_id){
    return $is_visible;
}

my_fs()->add_filter( 'is_submenu_visible', 'my_is_submenu_visible', 10, 2 );
```

## Freemius Purchase Completion JavaScript Callback Filter[​](#freemius-purchase-completion-javascript-callback-filter "Direct link to Freemius Purchase Completion JavaScript Callback Filter")

```php
<?php
    // Add GA tracking only if user opted-in OR if non-WP.org compliant product.
    function my_after_purchase_js( $js_function ) {
        return 'function ( response ) {
            /**
             * Since the user just entered their personal & billing information, agreed to the TOS & privacy,
             * know they are running within a secure iframe from an external domain, they implicitly permit tracking
             * this purchase. So initizlizing GA here (after the purchase), is legitimate.
             */
            ga('create', 'UA-XXXXXXX', 'auto');

            console.log("checkout", "purchaseCompleted");
        }';
    }

    function my_checkout_enrich ( $html ) {
        return '<script type="text/javascript">
            (function() {
                if ( null == ga ) {
                    // Add code to include GA.
                }
            })();
        </script>' . $html;
    }

    my_fs()->add_filter('checkout/purchaseCompleted', 'my_after_purchase_js');
    my_fs()->add_filter('templates/checkout.php', 'my_checkout_enrich');
```

## Freemius Buy Button Code for a Multi-Plans Table[​](#freemius-buy-button-code-for-a-multi-plans-table "Direct link to Freemius Buy Button Code for a Multi-Plans Table")

```html
<script src="https://checkout.freemius.com/checkout.min.js"></script>
<select id="starter-licenses">
  <option value="1" selected="selected">Single Site License</option>
  <option value="5">5-Site License</option>
  <option value="25">25-Site License</option>
  <option value="unlimited">Unlimited Sites License</option>
</select>
<button id="starter-purchase">Buy Starter</button>

<select id="pro-licenses">
  <option value="1" selected="selected">Single Site License</option>
  <option value="5">5-Site License</option>
  <option value="25">25-Site License</option>
  <option value="unlimited">Unlimited Sites License</option>
</select>
<button id="pro-purchase">Buy Professional</button>

<select id="bus-licenses">
  <option value="1" selected="selected">Single Site License</option>
  <option value="5">5-Site License</option>
  <option value="25">25-Site License</option>
  <option value="unlimited">Unlimited Sites License</option>
</select>
<button id="bus-purchase">Buy Professional</button>

<script type="text/javascript">
  (function () {
    var freemiusHandler = FS.Checkout.configure({
      name: '<pluginTitle>',
      plugin_id: '<pluginID>',
      public_key: '<publicKey>',
    });

    var plans = {
      starter: '<starterPlanID>',
      pro: '<proPlanID>',
      bus: '<busPlanID>',
    };

    var addBuyHandler = function (plan, planID) {
      $('#' + plan + '-purchase').on('click', function (e) {
        freemiusHandler.open({
          plan_id: planID,
          licenses: $('#' + plan + '-licenses').val(),
          // You can consume the response for after purchase logic.
          success: function (response) {
            // alert(response.user.email);
          },
        });

        e.preventDefault();
      });
    };

    for (var plan in plans) {
      if (!plans.hasOwnProperty(plan)) continue;

      addBuyHandler(plan, plans[plan]);
    }
  })();
</script>
```

## Controlling the visibility of admin notices added by the Freemius SDK[​](#controlling-the-visibility-of-admin-notices-added-by-the-freemius-sdk "Direct link to Controlling the visibility of admin notices added by the Freemius SDK")

```php
<?php
  /**
   * @param bool  $show
   * @param array $msg {
   *     @var string $message The actual message.
   *     @var string $title An optional message title.
   *     @var string $type The type of the message ('success', 'update', 'warning', 'promotion').
   *     @var string $id The unique identifier of the message.
   *     @var string $manager_id The unique identifier of the notices manager. For plugins it would be the plugin's slug, for themes - `<slug>-theme`.
   *     @var string $plugin The product's title.
   *     @var string $wp_user_id An optional WP user ID that this admin notice is for.
   * }
   * @return bool
   */
  function my_custom_show_admin_notice( $show, $msg ) {
      if ('trial_promotion' == $msg['id']) {
          // Don't show the trial promotional admin notice.
          return false;
      }

      return $show;
  }

  my_fs()->add_filter( 'show_admin_notice', 'my_custom_show_admin_notice', 10, 2 );
```

## Merging different free and premium product versions into one with Freemius[​](#merging-different-free-and-premium-product-versions-into-one-with-freemius "Direct link to Merging different free and premium product versions into one with Freemius")

```php
<?php
  /**
   * Plugin Name: ...
   * Plugin URI:  ...
   * ...
   *
   * @fs_premium_only /path/to/premium/folder/
   */
  // Freemius Init SDK code
  function my_fs() {
      global $my_fs;

      if ( ! isset( $my_fs ) ) {
          // Include Freemius SDK.
          require_once dirname(__FILE__) . '/freemius/start.php';

          $my_fs = fs_dynamic_init( array(
            ...
          ) );
      }

      return $my_fs;
  }

  if ( ! my_fs()->is_premium() ) {
    require_once dirname(__FILE__) . 'path/to/free/loader.php';
  }
  if ( my_fs()->is__premium only() ) {
    if ( my_fs()->can_use_premium_code() ) {
      require_once dirname(__FILE__) . 'path/to/premium/loader.php';
    }
  }
```

## Disable deactivation feedback form[​](#disable-deactivation-feedback-form "Direct link to Disable deactivation feedback form")

```php
<?php
  my_fs()->add_filter( 'show_deactivation_feedback_form', '__return_false' );
```

## Disable after deactivation subscription cancellation window[​](#disable-after-deactivation-subscription-cancellation-window "Direct link to Disable after deactivation subscription cancellation window")

warning

A subscription cancellation window will only show up when deactivating a product associated with a license that is only activated on the current site. Over the years, we learned that some users assume a product deactivation is also a cancelation of its subscription, which may cause an unexpected charge that can lead to a dispute. Therefore, we generally recommend keeping the default behavior as it reduces payment reversals and dispute fees.

```php
<?php
  my_fs()->add_filter( 'show_deactivation_subscription_cancellation', '__return_false' );
```