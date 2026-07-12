We’re thrilled to unveil a major update to one of the most customer-facing parts of our platform — the [**Customer Portal**](help-documentation-users-account-management.md). It’s now fully [redesigned and rebranded](blog-freemius-rebrand-website-developer-dashboard-redesign.md) with a cleaner interface and smarter UX throughout.

[![Freemius Customer Portal Rebranded](https://freemius.com/blog/wp-content/uploads/2025/10/rebranded-customer-portal-1024x570.png)](https://freemius.com/blog/wp-content/uploads/2025/10/rebranded-customer-portal.png)

The Customer Portal is a self-service dashboard your customers use to manage their **purchases, subscriptions, licenses, and billing information**. From changing payment methods or upgrading plans to downloading software and generating VAT-compliant invoices — everything happens here seamlessly. And with this release, it all just got a lot better.

We’re rolling out the redesigned portal for everyone under a new subdomain: `https://customers.freemius.com`.  
If your integration or website still links to the old `https://users.freemius.com` domain, you’ll be automatically redirected to the new one.

However, if your store uses custom CSS to style the Customer Portal, your integration will stay on the legacy version until you manually migrate. You can find the [migration guide at the end of this changelog](#how_to_upgrade_to_the_new_design).

Now, let’s go through some of the key updates:

### Websites Page Improvement

On the main Websites page, we group and display all the websites where buyers have activated any Freemius-powered product. Each website may have one or more products associated with it.

[![Website pages improvement in the Customer Portal](https://freemius.com/blog/wp-content/uploads/2025/10/customer-portal-websites-compare-1024x263.png)](https://freemius.com/blog/wp-content/uploads/2025/10/customer-portal-websites-compare.png)

Previously, it wasn’t very clear that you could click and navigate individual items inside the list. We’ve added a folder icon and removed the right-side chevron to make the navigation more intuitive.

### Better UI Positioning

Across the app, we conducted UX audits and made numerous layout adjustments to position key UI elements where users expect them.

For example, in the [Downloads](help-documentation-users-account-management-downloads.md) page, the download button was previously placed at the end, often requiring a horizontal scroll on smaller screens to access it.

[![Better UI positioning](https://freemius.com/blog/wp-content/uploads/2025/10/ui-positioning-compare-1024x555.png)](https://freemius.com/blog/wp-content/uploads/2025/10/ui-positioning-compare.png)

Now, the button appears just after the product title, bringing important actions closer to your fingertips.

This is just one of many small but impactful improvements throughout the portal.

### Better Table Layout

We revamped the table design across the Customer Portal for better usability and consistency.

[![Table layout improvement](https://freemius.com/blog/wp-content/uploads/2025/10/table-ui-compare-1024x594.png)](https://freemius.com/blog/wp-content/uploads/2025/10/table-ui-compare.png)

1. Tables now better adapt to the available screen space.
2. Tables that open a window or side panel are now clearly marked with a chevron.
3. Labels and action buttons have been standardized to make their purpose clear. For instance, expired licenses are now highlighted in red for quick visibility.

### FAQ Page Redesigned

The FAQ page has been restructured into two columns and organized by categories, making it easier to browse and find what you’re looking for.

[![Redesigned FAQ page](https://freemius.com/blog/wp-content/uploads/2025/10/faq-page-compare-1024x1004.png)](https://freemius.com/blog/wp-content/uploads/2025/10/faq-page-compare.png)

With this new layout, finding answers to your questions is now faster and more intuitive.

### Other Notable Improvements

1. Menu items have been renamed for clarity and industry alignment—for example, “Subscriptions” replaces “Renewals & Billings,” and “Invoices” replaces “Order History.”
2. Breadcrumbs and other navigation elements have been refreshed, fixing several old bugs.
3. If you use custom CSS for the Customer Portal, the initial flash of unbranded UI will no longer appear.
4. All new brand-related changes continue to meet accessibility standards.

### How to Upgrade to the New Design

We’ve released the newly rebranded Customer Portal under the subdomain `https://customers.freemius.com`. For most makers still using the old domain `https://users.freemius.com`, we’ve set up automatic redirects to ensure a seamless transition.

However, if you’re using custom CSS to brand your portal, we’ve preserved your old design since the latest CSS and markup changes are breaking in nature.

To help you migrate smoothly, your existing CSS has been moved under a new setting called **“Legacy Customer Portal CSS Stylesheet”**, leaving the original configuration empty. You can view this update in your Developer Dashboard under Store Settings.

[![Customer Portal CSS Configuration](https://freemius.com/blog/wp-content/uploads/2025/10/moved-customer-portal-css-url-config-1024x634.png)](https://freemius.com/blog/wp-content/uploads/2025/10/moved-customer-portal-css-url-config.png)

To migrate to the new Customer Portal, follow these steps:

1. Update your CSS according to the new [customization guidelines](help-documentation-users-account-management-applying-css-customization.md).
2. Save your configuration in the Developer Dashboard.
3. Follow [our migration guide](blog-changelog-upgrade-to-the-redesigned-customer-portal.md) to complete the upgrade.