---
title: "Handling Licensing"
url: "https://freemius.com/help/documentation/wordpress-sdk/software-licensing/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 1772
---

It’s quite easy to be able to have your product support a licensing mechanism with Freemius. All you need to do is add some logic that will help Freemius understand which parts (code blocks) of your product belong to which of your payment plans. Once you have that logic in place Freemius will automatically use it to determine which of your product’s capabilities should be included or excluded on each plan.

## Plan vs. Code Type[​](#plan-vs-code-type "Direct link to Plan vs. Code Type")

Before jumping into the code, it's important to understand the difference between a **Plan** and a **Code Type**.

### Plan[​](#plan "Direct link to Plan")

Every product on Freemius can have as many plans as you wish. A plan is a set of features or services. Multi-site license offers not considered as additional plans.

### Code Type[​](#code-type "Direct link to Code Type")

Every plugin, theme, or add-on on Freemius can have two code types at most: *Free Version* and *Premium Version*. The *Free Version* is the product's code version stripped from ANY of the product's paid features. On the other hand, the *Premium Version* is the product's code version including ALL of the product's code. It doesn't necessarily mean that all the code will be available for use, it just means that all the code included in the *Premium Version*.

## License Related Methods[​](#license-related-methods "Direct link to License Related Methods")

`can_use_premium_code()`[](#can_use_premium_code "Direct link to can_use_premium_code")

Check if a user is on a trial or has an activated license that enables premium features.

`is_free_plan()`[](#is_free_plan "Direct link to is_free_plan")

Check if the user is on the free plan of the product.

`is_plan($plan, $exact = false)`[](#is_plan "Direct link to is_plan")

Check if the user is on a specified plan. If the user is on a trial of that plan the result will be `false`.

`is_trial()`[](#is_trial "Direct link to is_trial")

Check if the user is on a trial.

`is_trial_plan($plan, $exact = false)`[](#is_trial_plan "Direct link to is_trial_plan")

Check if the user is on a specific trial plan.

`is_plan_or_trial($plan, $exact = false)`[](#is_plan_or_trial "Direct link to is_plan_or_trial")

Check if the user is on a specific plan or on that plan's trial.

`is_paying()`[](#is_paying "Direct link to is_paying")

Check if the user owns an activated and valid (paid) license.

`is_not_paying()`[](#is_not_paying "Direct link to is_not_paying")

Check if the user has an activated non-expired license that was purchased. Manually issued licenses will return `false`.

`is_paying_or_trial()`[](#is_paying_or_trial "Direct link to is_paying_or_trial")

Check if the user is paying or on a trial.

`is_premium()`[](#is_premium "Direct link to is_premium")

Check if user is running the product's *Premium Version*.

`is_trial_utilized()`[](#is_trial_utilized "Direct link to is_trial_utilized")

Check if the trial has already been used.

`is_payments_sandbox()`[](#is_payments_sandbox "Direct link to is_payments_sandbox")

Check if user is running payments in sandbox mode.

The SDK also comes with several handy license-related methods that in addition to performing their logic, all the logic that will be included within their `if` scope will be automatically stripped from the *Free Version* after the deployment process (by the Freemius' PHP preprocessor).

`is__premium_only()`[](#is__premium_only "Direct link to is__premium_only")

Check if user is only running the product's *Premium Version* code.

`is_paying__premium_only()`[](#is_paying__premium_only "Direct link to is_paying__premium_only")

Check if user is on a trial or on the free plan (not paying).

`can_use_premium_code__premium_only()`[](#can_use_premium_code__premium_only "Direct link to can_use_premium_code__premium_only")

Check if a user is on a trial or has an activated license that enables premium features.

`is_plan__premium_only($plan, $exact = false)`[](#is_plan__premium_only "Direct link to is_plan__premium_only")

Check if the user is on a specified plan. If the user is on a trial of that plan the result will be `false`.

`is_plan_or_trial__premium_only($plan, $exact = false)`[](#is_plan_or_trial__premium_only "Direct link to is_plan_or_trial__premium_only")

Check if the user is on a specific plan or on that plan's trial.

`is_paying_or_trial__premium_only()`[](#is_paying_or_trial__premium_only "Direct link to is_paying_or_trial__premium_only")

Check if the user is paying or on a trial.

### Recommended Methods[​](#recommended-methods "Direct link to Recommended Methods")

If your product only has a single paid plan, the primary methods that you'll be using are:

- `can_use_premium_code()`
- `is__premium_only()`
- `can_use_premium_code__premium_only()`

If your product has multiple paid plans, the recommended methods to start with are:

- `is_plan_or_trial()`
- `is__premium_only()`
- `is_plan_or_trial__premium_only()`

### Examples[​](#examples "Direct link to Examples")

Here are some concrete examples to help clarify this better:

warning

Note that in the following examples the product's shortcode is referred to as `my_fs` and the paid plan’s name is **professional**. It will obviously be different for you when you come to customize it.

To check if a website is eligible to use any of the premium defined logic (if the user is either currently in a trial period or simply owns a valid license), simply use:

```php
 // This IF block will be auto removed from the Free version.
 if ( my_fs()->is__premium_only() ) {
    // This IF will be executed only if the user in a trial mode or have a valid license.
    if ( my_fs()->can_use_premium_code() ) {
        // ... premium only logic ...
    }
}
```

Alternatively, you can use the following code which is equivalent:

```php
// This IF block will be auto removed from the Free Version and will only get executed if the user on a trial or have a valid license.
if ( my_fs()->can_use_premium_code__premium_only() ) {
    // ... premium only logic ...
}
```

Here’s how you can add customized **marketing content** to encourage your users to upgrade from your **free** to your your **paid** version:

```php
 if ( my_fs()->is_not_paying() ) {
    echo '<section><h1>' . esc_html__('Awesome Professional Features', 'my-text-domain') . '</h1>';
    echo '<a href="' . esc_url(my_fs()->get_upgrade_url()) . '">' . esc_html__('Upgrade Now!', 'my-text-domain') . '</a>';
    echo '</section>';
}
```

Here’s an easy way for you to add logic which will only be available in your premium plugin version:

```php
// This "if" block will be auto removed from the Free version.
if ( my_fs()->is__premium_only() ) {
    // ... premium only logic ...
}
```

To add a function which will only be available in your premium plugin version, simply add ***premium\_only*** as a suffix to the function’s name. Make sure that all lines that call that method either directly, or by using hooks, are also wrapped in the **premium only** logic:

```php
class My_Plugin {
    function init() {
        ...

        // This "if" block will be auto removed from the free version.
        if ( my_fs()->is__premium_only() ) {
            // Init premium version.
            $this->admin_init__premium_only();

            add_action( 'admin_init', array( &$this, 'admin_init_hook__premium_only' );
        }

        ...
    }

    // This method will be only included in the premium version.
    function admin_init__premium_only() {
        ...
    }

    // This method will be only included in the premium version.
    function admin_init_hook__premium_only() {
        ...
    }
}
```

Here’s how you can add logic which will only be executed for customers on one of your paid plans. Simply switch the string `professional` with whatever name you gave the plan you wish to apply this logic to:

```php
if ( my_fs()->is_plan('professional', true ) ) {
    // .. logic related to professional plan only ...
}
```

Add logic which will only be executed for customers on a specific plan you choose, OR any **higher tier**. Simply switch the string `professional` with whatever name you gave your plan:

```php
if ( my_fs()->is_plan('professional') ) {
    // ... logic related to professional plan and higher plans ...
}
```

Add logic which will only be executed for customers on a specific plan you choose, AND any **higher tier**. Simply switch the string `professional` with whatever name you gave your plan:

```php
// This "if" block will be auto removed from the Free version.
if ( my_fs()->is_plan('professional') ) {
    // ... logic related to professional plan and higher plans ...
}
```

Add logic which will only be executed for customers on a specific plan you choose, AND any **higher tier**. Simply switch the string `professional` with whatever name you gave your plan:

```php
// This "if" block will be auto removed from the Free version.
if ( my_fs()->is_plan__premium_only('professional') ) {
    // ... logic related to professional plan and higher plans ...
}
```

Add logic only for users in a **trial period:**

```php
if ( my_fs()->is_trial() ) {
    // ... logic for users in trial ...
}
```

Add logic for any specified paid plan. Simply switch the word `professional` with whatever name you gave your plan:

```php
// This "if" block will be auto removed from the Free version.
if ( my_fs()->is__premium_only() ) {
    if ( my_fs()->is_plan( 'professional', true ) ) {
        // ... logic related to professional plan only ...
    } else if ( my_fs()->is_plan( 'business' ) ) {
        // ... logic related to Business plan and higher plans ...
    }
}
```

## Excluding files and folders from the free plugin version:[​](#excluding-files-and-folders-from-the-free-plugin-version "Direct link to Excluding files and folders from the free plugin version:")

There are two ways to exclude files from your **free version**:

1. Add ***premium\_only*** just before the file extension. For example: **functions\_\_premium\_only.php** will be only included in the premium plugin version. *This works for all type of files, not only PHP.*
2. Add `@fs_premium_only`, a special meta tag, to the plugin's main PHP file header. Example:

```php
/**
 * Plugin Name: My Very Awesome Plugin
 * Plugin URI:  http://my-awesome-plugin.com
 * Description: Create and manage Awesomeness right in WordPress.
 * Version:     1.0.0
 * Author:      Awesomattic
 * Author URI:  http://my-awesome-plugin.com/me/
 * License:     GPLv2
 * Text Domain: myplugin
 * Domain Path: /langs
 *
 * @fs_premium_only /lib/functions.php, /premium-files/
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// ... my code ...
```

The file `/lib/functions.php` and the directory `/premium-files/` will be removed from the free plugin version.

## WordPress.org Compliance[​](#wordpressorg-compliance "Direct link to WordPress.org Compliance")

FInally, regarding **WordPress.org Compliance:**

Based on [WordPress.org Guidelines](https://wordpress.org/plugins/about/guidelines/) you are not allowed to submit a plugin that has premium code in it:

> "All code hosted by WordPress.org servers must be free and fully-functional. If you want to sell advanced features for a plugin (such as a "pro" version), then you must sell and serve that code from your own site, we will not host it on our servers."

Therefore, if you want to deploy your free plugin's version to WordPress.org, make sure you wrap all your premium code with an `if` statement like so:

```php
if ( my_fs()->is__premium_only() ) {
    // ... my premium only logic ...
}
```

or use the other methods provided to exclude premium features & files from the free version.

## Handling Licensing in JavaScript[​](#handling-licensing-in-javascript "Direct link to Handling Licensing in JavaScript")

If you need to control licensing in your JavaScript files, you can easily do that by applying the following approach:

```php
<?php
function my_module_add_licensing_helper() {
?>
  <script type="javascript/text">
      (function(){
          window.my_module.can_use_premium_code = <?php json_encode( my_fs()->can_use_premium_code() ) ?>;
      })();
  </script>
<?php
}

add_action('wp_head', 'my_module_add_licensing_helper');
```

```javascript
if ( window.my_module.can_use_premium_code ) {
    // ... premium only code ...
}
```