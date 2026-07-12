---
title: "Onboarding Affiliate Marketers"
url: "https://freemius.com/help/documentation/affiliate-platform/onboarding-affiliate-marketers/"
source: "docs"
section: "Docs"
category: "Affiliate Platform"
scraped_at: "2026-04-09T19:58:36+06:00"
word_count: 884
---

## Adding Affiliates Manually[​](#adding-affiliates-manually "Direct link to Adding Affiliates Manually")

- Open the [Freemius Dashboard](https://dashboard.freemius.com/login/)
- Choose the Product from the **Products** tab under the Freemius logo.
- Click the ***Affiliation*** menu item.
- Click the *Affiliates* tab item.
- To add a new affiliate, click the **Add Affiliate** button
- Enter the affiliate’s email, name, and the domains via which the affiliate will be marketing your product.
  
  - The email address will be used for sending the affiliate their unique affiliate links, and for all future communications.
  - The name is used to personalize the emails sent to the affiliate.
  - The domain is used to validate that the affiliate is promoting your product from an approved domain. You can add multiple domains separated by commas.
  - You can also add additional optional information about the affiliate, such as their PayPal email (for payout purposes), promotional methods, stats description, and promotion method description.
- Then, click **Add Affiliate** button to complete the entry.

note

Once you add an affiliate, they will automatically receive an email with a direct link to their Affiliate Dashboard and their custom affiliated links, which they can start using right away to promote your product.

> Since the URLs aren’t very pretty, for WordPress websites, we recommend that affiliates use a plugin like [Shortlinks](https://wordpress.org/plugins/pretty-link/) to map the links with pretty URLs and use them instead.

## Affiliates Application Form[​](#affiliates-application-form "Direct link to Affiliates Application Form")

### User Dashboard affiliate application form[​](#user-dashboard-affiliate-application-form "Direct link to User Dashboard affiliate application form")

We provide a user account management platform that comes with a ready to use [affiliate sign up](help-documentation-users-account-management-earn-becoming-an-affiliate.md) section. It has a form with required fields that need to be filled by the applicant.

Once the potential affiliate agrees to the terms and submits the form, an email will be sent to you for approval.

Follow these steps to [activate the affiliate program](help-documentation-affiliate-platform-affiliate-program-activation.md) in the user dashboard.

### Affiliates Application Form on Your Website[​](#affiliates-application-form-on-your-website "Direct link to Affiliates Application Form on Your Website")

If you’d like to create an affiliates application form for your site, you can leverage our [API](https://docs.freemius.com/api/) and [PHP-SDK](https://github.com/freemius/php-sdk) to integrate your form with Freemius.

Here's a backend PHP implementation:

```php
<?php
  define( 'FS__API_SCOPE', 'developer' );
  define( 'FS__API_DEV_ID', 1234 );
  define( 'FS__API_PUBLIC_KEY', 'pk_YOUR_PUBLIC_KEY' );
  define( 'FS__API_SECRET_KEY', 'sk_YOUR_SECRET_KEY' );

  // Init SDK.
  $api = new Freemius_Api(FS__API_SCOPE, FS__API_DEV_ID, FS__API_PUBLIC_KEY, FS__API_SECRET_KEY);

  // You can get the product's affiliate program terms ID from the AFFILIATION section, it's stated right in the 1st tab.
  $api->Api("/plugins/{$productID}/aff/{$affiliateProgramTermsID}/affiliates.json", 'POST', array(
    'name'                         => 'Full Name',
    'email'                        => '[email protected]',
    'paypal_email'                 => '[email protected]',
    // Should not include an HTTP/S protocol.
    'domain'                       => 'affiliate-main-site.com',
    // An optional param to include additional domains/sub-domains where the applicant will promote your product.
    'additional_domains'           => array('affiliate-2nd-site.com', 'affiliate-3rd-site.com'),
    // Optional comma-separated combination of the following: 'social_media' and 'mobile_apps'.
    // This is useful if by default you don't allow promoting through mobile or social, to manually (& optionally) create custom terms for the applicant after approval.
    'promotional_methods'          => 'social_media,mobile_apps',
    // An optional free text where an applicant can provide some stats data about their reach.
    'stats_description'            => '100k monthly PVs. 1,000 Instagram followers. I manage a FB group of 20,000 members.',
    // An optional free text when an applicant can explain how they are planning to promote your product.
    'promotion_method_description' => 'I am going to write a review of your plugin and sharing through my social reach of 100k followers.',
    // An option applicant state. Defaults to 'active'. One of the following states: 'active', 'pending', 'rejected', 'suspended', 'blocked'.
    'state'                        => 'pending',
  ));
```

- Go to the ***SDK Integration*** section, scroll to the submenu items selection and check the **Affiliation** option:
- Checking the box will add a new parameter to the integration snippet: `'has_affiliation' => '<moderation>', // <moderation> - selected, customers, or all.`
- Copy the updated snippet code and place it in your plugin/theme instead of the previous snippet.
- Refresh the WP Admin and you should immediately see a new **Affiliation** submenu item which links to the affiliate program terms:
- Clicking the **Become an affiliate** will show the affiliate application form:

To increase the awareness about your Affiliate Program, the SDK will automatically trigger an admin notice after 30 days of your product usage:

If you set your Affiliate Program to only permit paying users to become your affiliates, the notice will only show up for your customers.

You can disable the notice by including the following code:

```php
// Replace “my_freemius” with your shortcode.
my_freemius()->add_filter( 'show_affiliate_program_notice', '__return_false' );
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

When an affiliate submits the form, you’ll immediately receive an application email with the affiliate’s name, email, and information on where and how they will be promoting your product:

Scroll to the bottom of the email to get the direct link to the affiliate settings in the Freemius Dashboard where you will be able to approve or reject the affiliate’s application request:

If you approve the affiliate, they will get an email notification with a link to their Affiliate Dashboard, and the affiliated links they can use to promote your product.

If you reject the affiliate you’ll be prompted with a dialog box where you can add the rejection reason, which will be sent, together with the rejection email to the applicant.