The latest WordPress SDK 2.4.1 is now available with easier white labeling via the WP Admin and updates for WP 5.5. Plus, we enriched the Deployment mechanism to show the latest SDK version link, added Composer support for installing paid products, introduced an option for self-served DKIM verification to improve your transactional emails deliverability, enhanced the login security for both dashboards, and a few other UI/UX improvements.

### WP Admin White Labeling Notification

Previously, white label options for your customers were “hidden” in the User Dashboard and customers would have to know where it was to access it.

With [WordPress SDK 2.4.1](https://github.com/Freemius/wordpress-sdk/releases/tag/2.4.1), your customers who are site builders can much more easily white-label the WP Admin before handing over a site to their clients – we added a notification to allow users to easily turn on white-label mode directly from the WP Admin themselves, so this feature can be more accessible:

![Freemius SDK WP Admin Notification Click here to white label this site's account settings area](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-sdk-wp-admin-notification-click-here-to-white-label-this-sites-account-settings-area.png)

### WP 5.5 jQuery Compatibility

The [WordPress 5.5 jQuery update](https://motopress.com/blog/wordpress-5-5-fix-jquery-migrate-helper/) is now resolved in the latest SDK release; the problem was that WordPress 5.5 no longer supports deprecated methods using jquery-migrate, so we replaced all `jQuery.live()` usages with `jQuery.on().`

### Improved Plugin/Theme Data Collection

As you may already know, we’ve exposed the data that was previously collected about the installed plugins and themes on your users’ sites (with their ‘opt-in’ permission, of course). You can find the data under each Site profile by expanding the Themes & Plugins section.

The latest SDK 2.4.1 fixes a small bug that flagged all installed plugins as if they were “inactive”, so the proper activation status is now collected and displayed.

### Auto-Updates Support

WordPress 5.5 brought with it UI support for [auto-updates of free plugins and themes](https://make.wordpress.org/core/2020/07/15/controlling-plugin-and-theme-auto-updates-ui-in-wordpress-5-5/), and we’ve responded by adding support for auto-updates of paid products based on [this recommendation from the WordPress Core team](https://make.wordpress.org/core/2020/07/30/recommended-usage-of-the-updates-api-to-support-the-auto-updates-ui-for-plugins-and-themes-in-wordpress-5-5/).

## SDK Updates Deployment Notification

If your latest release is not using the latest version of our WordPress SDK, you will now get a notification in the Deployment section to ensure that you’re always updated about the latest WordPress SDK available before deploying new releases. The latest release is pulled directly from GitHub’s API so it doesn’t rely on us remembering to update it manually 🙂

![Freemius Deployment Mechanism SDK Update Notice](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-deployment-mechanism-sdk-update-notice.png)

This way, you don’t have to check Github manually to see the latest SDK updates – just click the dynamic link and find out everything you need to know.

## Install Paid Products via Composer

We are very excited to share that Freemius now supports installing paid products through Composer. It’s a capability we’ve been asked a lot during the past two years, so we decided to deliver.

In the plugin and theme space, Composer is mostly used by agencies, hosting companies, and larger organizations. These companies leverage command-line tools for executing different actions across a collection of sites (e.g., updating a plugin on 1000 sites), or automations like spinning a new WordPress website with a pre-configured plugins collection as composer dependencies.

Therefore, this new capability is a very appealing selling point to that audience, so we encourage you to market it with your “Enterprise” packages (i.e., the plans targeting larger businesses) by adding the feature “Composer Support” with the description “You can install & update the using Composer”.

Currently, the capability is available for any active license holder. Since this feature gives you a competitive advantage and most relevant to larger companies, another option would be only to support it in selected plans. That way, you’ll be able to upsell it as a benefit, which will only be included in your higher plans.

## Self-Served DKIM Domain Authentication

Previously, authenticating DKIM records for your domain was a manual process where each developer would have to contact our support and request that we generate their DKIM DNS records for improved email deliverability using their domain.

Because of the workload behind this, we only provided the added layer of email deliverability to makers who crossed $5k in lifetime gross sales.

However, since we know how mission-critical email deliverability is, we developed a self-served authentication process that now allows any maker, regardless of their size or revenue, to improve email deliverability from custom domains sent by Freemius on their behalf.

![Freemius Developer Dashboard Self-Authenticate with DKIM](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-self-authenticate-with-dkim.png)

## Brute Force Protection with reCAPTCHA

We’ve now added protection against brute force attacks with Google’s reCAPTCHA, including the monitoring of failed logins to ensure they’re blocked after a certain number of attempts within a specific duration.

This is for both the User Dashboard and Developer Dashboard:

![Freemius Login reCAPTCHA](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-login-recaptcha.png)

We’re also working on two-factor authentication, which we’re hoping to deploy later this year.

## “Login as User” Fix

The LOGIN AS USER feature enables developers to login to their customers’ accounts to “see what they see” for troubleshooting issues and other support-related inquiries.

![Freemius Developer Dashboard LOGIN AS USER Button](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-login-as-user-button.png)

Previously, if you were logged in the User Dashboard clicking the LOGIN AS USER would automatically redirect you to the already logged in session. This behavior added an extra step, you had to remember to logout before clicking the button. This is fixed now by automatically logging out to save you the extra steps.

## Until Next Time…

Did you find these release notes useful? Subscribe to our blog to get future release notes in your inbox.