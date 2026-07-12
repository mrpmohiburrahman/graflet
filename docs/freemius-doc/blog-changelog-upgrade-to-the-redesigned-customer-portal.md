[Changelog](https://freemius.com/changelog/) / Upgrade to the Redesigned Customer Portal

Since you have a custom CSS set with the Customer Portal (previously called the User Dashboard), we didn’t immediately update your integration to the [new design](blog-changelog-customer-portal-redesigned-with-a-fresh-look-and-improved-ux.md). To ensure your existing styling continues to work smoothly, we’ll keep showing the old Customer Portal until you explicitly make the switch.

Here’s how you can move to the new design:

### Migrating the CSS

This step is optional. If you’re happy to use the new redesigned Customer Portal as-is, you can skip it.

However, if you want to apply your own branding, you’ll need to manually load `customers.freemius.com/store/<storeID>/` and update your CSS to target the new system. Refer to our [documentation](help-documentation-users-account-management-applying-css-customization.md) to learn how to properly write CSS that reflects your brand colors and design.

Once done, go to the Developer Dashboard → Store Settings. Scroll down until you find the “Customer Portal CSS Stylesheet” field and paste your new stylesheet URL there.

[![Set up stylesheet URL for Customer Portal branding](https://freemius.com/blog/wp-content/uploads/2025/10/customer-portal-new-and-legacy-stylesheet-1024x609.png)](https://freemius.com/blog/wp-content/uploads/2025/10/customer-portal-new-and-legacy-stylesheet.png)

You’ll notice that your old stylesheet has been moved to a new setting called “Legacy Customer Portal CSS Stylesheet.” You can keep it there for reference or rollback purposes.

Now, follow the steps below to make the switch:

### If you’re using direct links

Instead of using the link:

```
https://users.freemius.com/store/<storeID>/
```

use this new link:

```
https://customers.freemius.com/store/<storeID>/
```

### If you’re using the WordPress Plugin

Please update to the latest version of the plugin from [GitHub](https://github.com/Freemius/freemius-users-dashboard).

### If you’re using the JavaScript API

Please change your code from:

```
<script src="https://users.freemius.com/dashboard.js" type="text/javascript"></script>
```

to:

```
<script src="https://customers.freemius.com/js/v1/" type="text/javascript"></script>
```

Once you make these changes, you’ll start seeing the new design.

Please note that your old CSS customizations will not be applied to the new design. You’ll need to set up your custom styles again following our [updated CSS customization guide](help-documentation-users-account-management-applying-css-customization.md).

### Automatic Upgrade

If you haven’t been using custom CSS, we’ve already upgraded you to the new design by redirecting the `users.freemius.com` subdomain to `customers.freemius.com`. This means you don’t have to make any explicit changes, though we still recommend updating your integration for consistency and long-term support.

Starting February 1st, 2026, all integrations will be automatically upgraded to the new design. Any old CSS that hasn’t been migrated by then will be discarded.