---
title: "Safe Mode & Clone Resolution"
url: "https://freemius.com/help/documentation/wordpress-sdk/safe-mode-clone-resolution-duplicate-website/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 1128
---

Upon license key activation, Freemius assigns a unique ID and pair of public/secret keys tied to the website's URL. These are used for securely extending the license expiration date after subscription renewals, checking if there are new plugin/theme updates, and allowing customers to execute other account-related remote (or local) actions that get synced back to a website (or Freemius).

## What is a website clone?[​](#what-is-a-website-clone "Direct link to What is a website clone?")

A clone is a website (or a subsite in a multisite network) assigned with an ID and pair of keys identical to another website (or subsite).

## How's a clone created?[​](#hows-a-clone-created "Direct link to How's a clone created?")

There are several cases in which a site's URL could change:

- The site is updated to use a newly purchased domain name.
- A clone of a site from production to staging (or the other way around).
- Creation of a subsite by replicating an existing template subsite in a multisite network.
- WaaS multisite network environment where users can spin a website that is created by duplicating a template subsite.
- A network of websites/brands that are intentionally identical and automatically synced.

## What is the problem with clone websites?[​](#what-is-the-problem-with-clone-websites "Direct link to What is the problem with clone websites?")

If two websites are assigned with the same ID and keys, actions on one website will impact the other, potentially triggering unexpected behaviors.

For example, when a plugin is deactivated, the Freemius SDK automatically notifies the licensing engine to detach the license from the website to free up the license activations counter for reuse on another website. However, if there's a clone, the license deactivation would propagate to the clone, which will deactivate the license, and therefore, automatic updates will stop working.

## Clone Website Resolution[​](#clone-website-resolution "Direct link to Clone Website Resolution")

When a plugin/theme uses SDK v.2.5.0 or higher, it has a built-in clone identification and resolution mechanism.

### Clone Identification[​](#clone-identification "Direct link to Clone Identification")

The identification mechanism simply checks for unexpected mismatches between the URL of the website and the URL that is currently linked to the license on our backend (the "source of truth").

### Automatic Clone Resolution[​](#automatic-clone-resolution "Direct link to Automatic Clone Resolution")

Once a clone is identified, the mechanism will attempt to resolve it automatically based on different heuristics and the status of the buyer's account to reduce interruptions to the minimum.

For example, we know that it's common to have a template subsite on multisite networks for spinning new subsites using replication. Therefore, when a subsite is a clone of another subsite in the same multisite network, and the license's quota wasn't fully utilized, the clone subsite would be resolved automatically as a new website. It will be issued with a new ID and pair of keys, and the license will be auto-activated in the background.

This automatic resolution comes with 3 retries to overcome temporary connectivity issues and other unexpected server problems.

### Programmatic Clone Resolution[​](#programmatic-clone-resolution "Direct link to Programmatic Clone Resolution")

If cloning websites is part of your workflow (e.g., using a template for client sites), you can leverage the `FS__RESOLVE_CLONE_AS` flag to programmatically guide the clone resolution mechanism on how to resolve clones in your environment. Simply add the flag with one of the following optional values to your template site’s `wp-config.php` (or `functions.php`):

```php
// A temporary duplication for the purpose of testing, staging, or development.
define( 'FS__RESOLVE_CLONE_AS', 'temporary_duplicate' );

// The new site is replacing the old one – this will migrate the license activation to the new site to resolve the clone.
define( 'FS__RESOLVE_CLONE_AS', 'new_home' );

// The cloned site is a new and different one – this will auto activate the license on the new site to resolve the clone.
define( 'FS__RESOLVE_CLONE_AS', 'long_term_duplicate' );
```

### Safe Mode[​](#safe-mode "Direct link to Safe Mode")

If an automatic resolution isn't possible, the plugin/theme gets into a *Safe Mode*.

During *Safe Mode*, data syncing, as well as some account actions, will be temporarily disabled. However, automatic updates will continue working until the actual expiration date of the license or the one stored on the website, whichever comes first.

In addition, an admin notice for manual clone resolution will appear in the WP Admin:

### Manual Clone Resolution[​](#manual-clone-resolution "Direct link to Manual Clone Resolution")

The clone resolution notice is pretty straightforward and empowers users to choose how to resolve the clone issue.

#### Duplicate Website[​](#duplicate-website "Direct link to Duplicate Website")

If the website is a duplicate for testing, staging, or development, clicking the "Duplicate Website" will resolve the situation. The plugin/theme will remain fully functional, and automatic updates will be served as usual for 2 weeks (or until license expiration, whichever comes first).

In addition, the following dismissible notice will appear to remind about the 2-week period:

Suppose the duplicate testing/staging/development site is required for an extended period. In that case, the notice offers an option to activate a license to keep the paid functionality and automatic updates for more than 2 weeks.

If the duplicate website remains active for a long period, the manual resolution notice will reappear after 2 weeks with one difference. Instead of the “Duplicate Website” button a “Long-Term Duplicate” button will appear.

Clicking that option will activate a license and enable keeping the paid functionality and automatic updates for as long as the license is valid.

#### License Migration[​](#license-migration "Direct link to License Migration")

If the new site URL is replacing an old site’s URL, clicking the “Migrate License” (or “Migrate”) will migrate the site’s data, including the license, to the new website. And place the old site, if it still exists, into a safe mode. The most common case for this is taking a site from development (or staging) to production.

Cannot Migrate License?

If clicking the button triggers a page reload but the clone resolution notice still appears, the migration failed. We are improving the migration process so the WordPress SDK can catch the error and notify users.

This can happen if the license cannot be migrated to the new URL, for example, due to [license security settings](help-documentation-users-account-management-license-security.md#url-whitelisting-aka-license-firewall) or insufficient [license quota](help-documentation-wordpress-license-utilization.md) when migrating from staging to production.

#### New Website[​](#new-website "Direct link to New Website")

If the new site is separate & standalone, clicking the "Activate License" (or "New Website") will create a new site ID & pair of keys and will activate the license. The most common case for this would be to create a copy of a site from an existing template.

#### Taking No Action[​](#taking-no-action "Direct link to Taking No Action")

If no action is taken, the plugin/theme will remain fully functional, and automatic updates will be served as usual, for a grace period of 2 weeks (or until license expiration, whichever comes first).