---
title: "WP Admin Account"
url: "https://freemius.com/help/documentation/wordpress-sdk/wp-admin-account/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 497
---

By utilizing the [WordPress SDK](help-documentation-wordpress-sdk.md) an account section will be automatically added to your plugin/theme settings right within the WP Admin dashboard.

tip

If your **Account** menu item isn't available, you can access it via `/wp-admin/admin.php?page=my-slug-account`.

## Managing your account[​](#managing-your-account "Direct link to Managing your account")

The in-dashboard Account page allows users to manage their profile, license, subscription, and billing, right within the comfort of the WP Admin dashboard.

note

If the license is white-labeled, sensitive information like billing details and license key will be hidden, and user actions will be restricted. A license holder can unlock all options by clicking the **Start Debug** link and entering the license key.

### Deactivate a license from the website[​](#deactivate-a-license-from-the-website "Direct link to Deactivate a license from the website")

To deactivate a license from the website, an admin can click the **Deactivate License** link.

Users can go further by clicking the **Disconnect** link to disconnect the site completely from Freemius and remove it from their User Dashboard.

## White Label Mode[​](#white-label-mode "Direct link to White Label Mode")

Freelancers and agencies often use multi-site licenses when working on client sites, where revealing sensitive account information or allowing client access to certain account actions may be undesirable.

To address this, Freemius offers a built-in license white-labeling feature. This feature can be easily activated by users via the WP Admin dashboard and User Dashboard, or by you, the product owner, through the Developer Dashboard.

### How to activate white-label mode for a license?[​](#how-to-activate-white-label-mode-for-a-license "Direct link to How to activate white-label mode for a license?")

#### White-label mode via WP Admin Dashboard[​](#white-label-mode-via-wp-admin-dashboard "Direct link to White-label mode via WP Admin Dashboard")

Upon license activation, an admin notice will appear, allowing users to enable white-label mode directly from the WP Admin dashboard before handing over a site to their clients.

#### White-label mode via User Dashboard[​](#white-label-mode-via-user-dashboard "Direct link to White-label mode via User Dashboard")

Your customers can also activate [white-label mode through the User Dashboard](help-documentation-users-account-management-license-security.md#white-label-mode) by:

- Logging into their accounts
- Selecting **Licenses** from the menu
- Choosing the relevant license to open its editing panel:
- Checking the white-labeling box to hide confidential account and license information:

#### White-label mode via Developer Dashboard[​](#white-label-mode-via-developer-dashboard "Direct link to White-label mode via Developer Dashboard")

As a product owner, you can also enable white-label mode for a customer’s license from the Developer Dashboard:

- Navigate to the **Licenses** section.
- Locate the desired license.
- Toggle the white-labeling switch for that license:

### What exactly is hidden in white-label mode?[​](#what-exactly-is-hidden-in-white-label-mode "Direct link to What exactly is hidden in white-label mode?")

When a license is set to white-label mode, the following information is hidden:

- License owner information
- Billing details and invoices
- License key
- Pricing page
- Add-on prices (if you sell add-ons)
- Contact Us page

Additionally, these actions will be unavailable on the WP Admin account page in white-label mode:

- Subscription cancelation
- Plan changes
- License owner name and email edits