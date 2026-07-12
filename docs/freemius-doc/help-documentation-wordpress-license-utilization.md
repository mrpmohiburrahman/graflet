---
title: "License Utilization"
url: "https://freemius.com/help/documentation/wordpress/license-utilization/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 967
---

In this guide we will explain how Freemius license utilization works and how to configure it from the Developer Dashboard.

## Using One License for Live / Production, Staging, Dev and Localhost Sites[​](#using-one-license-for-live--production-staging-dev-and-localhost-sites "Direct link to Using One License for Live / Production, Staging, Dev and Localhost Sites")

When creating a new plan, by default, generated licenses can be activated on localhost/staging/dev environments without the need to purchase any additional licenses.

If you keep that option set as recommended, one license should keep your customers covered. Localhost, staging and development environments won't get counted toward the license’s maximum allowed sites if its domain name is clearly a dev or staging site.

### TLDs that are considered as dev or staging:[​](#tlds-that-are-considered-as-dev-or-staging "Direct link to TLDs that are considered as dev or staging:")

- `*.dev`
- `*.dev.cc` (DesktopServer)
- `*.test`
- `*.local`
- `*.staging`
- `*.example`
- `*.invalid`

### Subdomains that are considered as dev or staging:[​](#subdomains-that-are-considered-as-dev-or-staging "Direct link to Subdomains that are considered as dev or staging:")

- `local.*`
- `dev.*`
- `test.*`
- `stage.*`
- `staging.*`
- `stagingN.*` (SiteGround; `N` is an unsigned int)
- `*.myftpupload.com` (GoDaddy)
- `*.cloudwaysapps.com` (Cloudways)
- `*.wpsandbox.pro` (WPSandbox)
- `*.ngrok.io` (tunneling)
- `*.mystagingwebsite.com` (Pressable)
- `*.tempurl.host` (WPMU DEV)
- `*.wpmudev.host` (WPMU DEV)
- `*.websitepro-staging.com` (Vendasta)
- `*.websitepro.hosting` (Vendasta)
- `*.instawp.co` (InstaWP)
- `*.instawp.link` (InstaWP)
- `*.instawp.xyz` (InstaWP)
- `*.wpengine.com` (WP Engine)
- `*.wpenginepowered.com` (WP Engine)
- `dev-*.pantheonsite.io` (Pantheon)
- `test-*.pantheonsite.io` (Pantheon)
- `staging-*.kinsta.com` (Kinsta)
- `staging-*.kinsta.cloud` (Kinsta)
- `*-dev.10web.site` (10Web)
- `*-dev.10web.cloud` (10Web)

Additionally, if your domain is `localhost` (with any port), it will also be treated as a localhost domain.

If your customer wants to utilize a license on a dev site that doesn’t fit the criteria listed above, they can deactivate the license from within the Account page in their WP Admin dashboard, and then reuse the license.

### Custom Staging / Development / Testing / Localhost Patterns[​](#custom-staging--development--testing--localhost-patterns "Direct link to Custom Staging / Development / Testing / Localhost Patterns")

If a customer uses custom URL/pattern for their staging/development/testing/localhost environment, you can now easily add the URL/pattern in their profile on the Developer Dashboard in the **Custom localhost URLs** section:

warning

The *Custom localhost URLs* section is only available for customers who have at least one purchased & non-expired license from your store.

## Multisite Networks / WaaS[​](#multisite-networks--waas "Direct link to Multisite Networks / WaaS")

[Freemius WordPress SDK](help-documentation-wordpress-sdk.md) comes with an advanced multisite network integration that can simplify the license activation experience for customers with multisite networks.

### How to activate the multisite network integration?[​](#how-to-activate-the-multisite-network-integration "Direct link to How to activate the multisite network integration?")

To activate the network-level integration, go to the product's ***SDK Integration*** page in the Freemius Dashboard, where you’ll notice a new checkbox to activate the network integration:

### Network-Level License Activation[​](#network-level-license-activation "Direct link to Network-Level License Activation")

Once the multisite network integration is enabled, super-admins can activate a license across their entire network, delegate the license activation to site admins, or handpick which subsites to activate the license for:

### Multisite Network License Utilization[​](#multisite-network-license-utilization "Direct link to Multisite Network License Utilization")

When using the Freemius WordPress SDK, by default, each subsite in a multisite setup requires an activation. Therefore, if for example, a user with a 20-subsite network would like to activate a license for their entire network, they'll need to purchase a license that can be activated on at least 20 sites, or multiple licenses whose combined activations limit is 20 or more.

#### Why a license activation on a multisite network isn't considered as a single activation?[​](#why-a-license-activation-on-a-multisite-network-isnt-considered-as-a-single-activation "Direct link to Why a license activation on a multisite network isn't considered as a single activation?")

Multisite networks are way more complex than standard WordPress installations, have significantly more edge cases, and a higher chance for conflicts as subsites in the network can run different combinations of plugins and themes.

Also, multisite-networks are largely used by bigger entities like agencies, boutique hosting providers and WaaS, who generate revenue from their networks and therefore, have higher financial bandwidth.

Consequently, it's only fair to charge them more for protecting your business from the potentially increased support load and allowing you to offer even better support for those customers.

### Network-Level Management[​](#network-level-management "Direct link to Network-Level Management")

Super-admins that didn’t delegate the activation to the site admins will now have an Account page on the network WP Admin, enabling them to manage the Account on the network level without the need to open the page for every subsite:

## Blocking or Allowing Features after License Expiration[​](#blocking-or-allowing-features-after-license-expiration "Direct link to Blocking or Allowing Features after License Expiration")

With Freemius, you can easily configure whether to block or allow features after a license expires. This configuration is applied per plan and can be set in the plan settings in the Freemius Developer Dashboard.

Go to the plan page and scroll down to the **Features** section. There you can configure the behavior as needed.

You can choose to block features, allow features, or selectively block features for monthly subscriptions. Usually WordPress makers choose to block features for monthly subscriptions and allow features for yearly subscriptions. Please note that the Freemius WP SDK will automatically block updates and support for expired licenses, regardless of this setting.

## Overriding License Settings Per License[​](#overriding-license-settings-per-license "Direct link to Overriding License Settings Per License")

If you want to customize these settings for an individual license, go to the **Licenses** page and click the specific license to open the advanced side-pane with the relevant license details.

From there, you can override the default plan settings for that specific license. For example, you can enable features for a particular license even if the plan blocks features after expiration, or restrict localhost, staging, or development usage for a license even if those environments are allowed at the plan level.