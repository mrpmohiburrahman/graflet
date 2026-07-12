The Freemius WordPress SDK contains an impressive [set of features](https://freemius.com/help/documentation/wordpress-sdk/features/) like the In-Dashboard upgrade/pricing page, account management, license handling, and more to help you sell your WordPress plugins, themes, blocks, widgets, etc.

To complete the integration process:

1. Add the [core Freemius WordPress SDK](#add-the-core-freemius-wordpress-sdk) into your product.
2. Fill out the [SDK Integration Form](#fill-out-the-sdk-integration-form) via the Freemius Developer Dashboard.
3. Insert the [auto-generated SDK integration snippet](#insert-the-auto-generated-sdk-integration-snippet) into your product.
4. Wrap your [product's premium code with Freemius logic](#designate-your-premium-only-code).

For license management, in-dashboard purchase, and other features to work, you need to add the Freemius WordPress SDK to your product's codebase for your premium product version.

tip

If you are adding a premium version to an existing free product, we recommend adding the SDK to the free version as well to allow you to use the SDK features in the free version, such as the In-Dashboard upgrade/pricing page, which can help increase conversions.

The SDK can be added to your product in two ways: manually or via Composer.

### Manual Installation[​](#manual-installation "Direct link to Manual Installation")

- Download the newest version of the [WordPress SDK](https://github.com/Freemius/wordpress-sdk/archive/master.zip) and extract the ZIP file.
- Rename the extracted `wordpress-sdk-master` folder to `freemius`.
- In the root directory of your WordPress theme or plugin, create a new directory called `vendor` (if it does not exist).
- Move the renamed `freemius` folder as-is into the `vendor` folder.

### Composer Installation[​](#composer-installation "Direct link to Composer Installation")

If you prefer, the process above can be [automated with Composer](https://packagist.org/packages/freemius/wordpress-sdk) using this command:

```
composer require freemius/wordpress-sdk
```

This will add the Freemius WordPress SDK as a dependency in your project and automatically place it in the `vendor` directory.

SDK Files Placement

The `vendor` folder is the recommended location for the SDK by the WordPress plugin and theme development standards. Adding the SDK to the `vendor` folder will be required when you submit your product's free version to the public repository.

## Fill out the SDK Integration Form[​](#fill-out-the-sdk-integration-form "Direct link to Fill out the SDK Integration Form")

This step helps generate the [SDK integration snippet](#insert-the-auto-generated-sdk-integration-snippet), which initializes the Freemius SDK using an array of key/value pairs that contain specific information about your Freemius product and unlocks the full range of features available.

To fill out the SDK integration form:

1. Log into the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the ***SDK Integration*** page.
3. Scroll down to the **Init SDK** section, then fill out all the necessary form fields.
   
   **Any** changes made to the SDK integration page are auto-saved when any field is edited.
   
   The SDK integration page screenshot above is for a plugin and is very similar to the one for the theme below:

note

At any time, if any of the [fields in the SDK integration form](#fill-out-the-sdk-integration-form) are changed via the Developer Dashboard, the SDK Integration code snippet with need an update. Find the details on [updating the snippet](https://freemius.com/help/documentation/wordpress-sdk/integration/integration-snippet/#updating-the-sdk-integration-snippet).

## Insert the Auto-Generated SDK Integration Snippet[​](#insert-the-auto-generated-sdk-integration-snippet "Direct link to Insert the Auto-Generated SDK Integration Snippet")

The process of filling the form automatically generates the SDK code snippet. The product-specific snippet can be found under the ***SDK Integration*** page in the Freemius Developer Dashboard.

This snippet is used by the latest WordPress SDK in your product to manage licenses, payments, and more.

Please add (copy & paste) the snippet at the top of the appropriate file in your product's codebase. This will ensure that the SDK is initialized as early as possible in the execution flow of your product. We recommend:

- For **WordPress plugins**: to the top of your main plugin’s PHP file, right after the plugin's header comment and `if ( ! defined( 'ABSPATH' ) ) exit;` check.
- For **WordPress themes**: to the top of your theme’s `functions.php` file.

Visit the [SDK integration snippet guide](https://freemius.com/help/documentation/wordpress-sdk/integration/integration-snippet/) to find additional information about the SDK integration snippet, how to use and customize it.

Using hooks to add the SDK integration snippet

Do not use hooks like `plugins_loaded` when adding the integration snippet to your product. This causes unexpected behavior.

## Designate Your Premium Only Code[​](#designate-your-premium-only-code "Direct link to Designate Your Premium Only Code")

Next, add the Freemius-specific license handling logic to your codebase to [designate which features are premium-only](https://freemius.com/help/documentation/wordpress-sdk/integration/software-licensing/). This will ensure that

- Only users with an active license can access the premium features of your product.
- Premium code is [stripped from the free version](help-documentation-wordpress-deployment-process.md#how-does-freepremium-version-generation-work) of your product to keep it wordpress.org compliant.

To help you get started quickly here are some examples for different scenarios.

### Wrap Premium Code with Specific Plan[​](#wrap-premium-code-with-specific-plan "Direct link to Wrap Premium Code with Specific Plan")

```
if  ( my_fs()->is_plan_or_trial__premium_only( 'professional' ) ) {
  // The code here will only be executed if the user has an active license for the "professional" plan or is in a trial period for that plan.
  // This code will also be stripped from the free version of your product.
}
if ( my_fs()->is_plan_or_trial( 'professional' ) ) {
  // Same as above, but this code will not be stripped from the free version of your product.
}
```

### Wrap Premium Code with Any Paying Plan[​](#wrap-premium-code-with-any-paying-plan "Direct link to Wrap Premium Code with Any Paying Plan")

```
if ( my_fs()->is_paying_or_trial__premium_only() ) {
  // The code here will only be executed if the user has an active license for any premium plan or is in a trial period for any premium plan.
  // This code will also be stripped from the free version of your product.
}
if ( my_fs()->is_paying_or_trial() ) {
  // Same as above, but this code will not be stripped from the free version of your product.
}
```

### Wrap Premium Code with Single Plan[​](#wrap-premium-code-with-single-plan "Direct link to Wrap Premium Code with Single Plan")

```
if ( my_fs()->can_use_premium_code__premium_only() ) {
  // The code here will only be executed if the user has an active license (or trial) for any premium plan.
  // This code will also be stripped from the free version of your product.
}
if ( my_fs()->can_use_premium_code() ) {
  // Same as above, but this code will not be stripped from the free version of your product.
}
```

For more detailed information about the license handling methods, and to learn how to exclude files and folders from free version, please visit the [Software Licensing guide](https://freemius.com/help/documentation/wordpress-sdk/integration/software-licensing/).

## Testing the Integration[​](#testing-the-integration "Direct link to Testing the Integration")

After integrating the Freemius SDK into your WordPress product, test the product to ensure everything works properly before releasing a new version to production.

To begin this process, you will need to:

1. Set your [Freemius in development mode](help-documentation-wordpress-sdk-testing.md#setting-freemius-into-development-mode) by adding the following snippet in your `wp-config.php` file:
   
   ```
   /* Set Freemius into development mode */
   define( 'WP_FS__DEV_MODE', true );
   ```
2. Deactivate and reactivate the product. Because you have wrapped the code with the license handling methods, the SDK will display a license activation screen for the premium version.
   
   This screen requires adding a license key in the field and clicking the "**Activate License**" button. If you're following the integration form then it will give you a button to generate a test license.
   
   Otherwise you can follow this guide to [generate a license key for testing](help-documentation-wordpress-sdk-testing.md#generating-a-license-key-for-testing).
3. Once the license is activated, you will be redirected to the [product's account page](https://freemius.com/help/documentation/wordpress-sdk/features/wp-admin-account/).
4. After that, you can test the product's premium features.

## Deploying the Product[​](#deploying-the-product "Direct link to Deploying the Product")

If everything is as expected, the next step is to [deploy the product to Freemius](help-documentation-wordpress-deployment-process.md).

Benefits of using the Freemius Integration Process

Due to the robust nature of the deployment process, you can [maintain a single codebase](https://freemius.com/help/documentation/wordpress-sdk/integration/software-licensing/#managing-one-codebase-for-both-free-and-premium-versions) which will be used to generate the production-ready [free and premium versions](help-documentation-wordpress-deployment-process.md#how-does-freepremium-version-generation-work) of your product. These versions can be distributed to your users.

## Testing the Upgrade Flow[​](#testing-the-upgrade-flow "Direct link to Testing the Upgrade Flow")

If you have a freemium (free + premium) model, start by downloading the free version of your product from the Freemius Developer Dashboard and install it on a WordPress site.

You can use any of the following features to test the upgrade process from the free version to the trial/paid version:

1. [Trial purchase feature](help-documentation-wordpress-free-trials.md) to simulate the upgrade process from the free version to the trial version, which is a great way to test the upgrade flow without making an actual purchase.
2. [Sandbox Payments feature](help-documentation-wordpress-sdk-testing.md#check-out-the-wordpress-admin-pricing-page-with-sandbox-payments) to simulate transactions.
3. The [license key generation feature](help-documentation-wordpress-sdk-testing.md#generating-a-license-key-for-testing) to generate license keys for testing the activation process.
4. Test the [checkout process using coupons](help-documentation-selling-with-freemius-coupon-discount.md) to ensure that the coupon codes are applied correctly during the upgrade process.

Customize Upgrade Emails Instructions

When a customer upgrades from the free version to the trial/paid version, they will receive a post-purchase email with billing details, license keys and zip download instructions. You can customize the content of this email to include your installation steps using the [email content customization feature](https://freemius.com/help/documentation/emails/email-content-customization/).

Advanced Feature Customization

There are many more features to explore in the Freemius WordPress SDK, so we encourage you to check out the [SDK documentation](help-documentation-wordpress-sdk.md) to learn about all the available features and how to use them.

## Getting help with the integration[​](#getting-help-with-the-integration "Direct link to Getting help with the integration")

The integration form is very straightforward. You only need to fill out the required fields and the form will tell you the exact steps you need to follow to properly integrate and test.

For a few special use cases we also have separate guides which you can find below:

- [Bundles & Memberships](help-documentation-wordpress-selling-bundles-and-memberships.md#selling-bundles-from-the-wp-admin-dashboard)
- [Add-Ons & Extensions](help-documentation-wordpress-selling-add-ons-extensions.md#selling-add-ons-from-within-the-wp-admin-dashboard)
- [Multi-site integration](https://freemius.com/help/documentation/wordpress-sdk/integration/multisite-integration/) for a multi-site network environment usage.

However, if you have questions, please [email us](https://freemius.com/cdn-cgi/l/email-protection#ff8c8a8f8f908d8bbf998d9a9a92968a8cd19c9092) or ask for details in the `#integration` channel in our Freemius Slack.