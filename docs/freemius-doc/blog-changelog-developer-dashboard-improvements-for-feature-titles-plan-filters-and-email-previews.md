[Changelog](https://freemius.com/changelog/) / Developer Dashboard Improvements for Feature Titles, Plan Filters, and Email Previews

We have deployed the following bug fixes and feature enhancements to our Developer Dashboard.

## Accented Characters Are Now Supported for Features

As part of our ongoing effort to make [Freemius better suited for local markets](blog-freemius-release-notes-june-2026.md), we noticed that accented Latin characters, such as `à` and `è`, were not properly supported in [feature titles](help-documentation-saas-saas-plans-pricing.md#configure-a-plans-features). Features are a great way to promote your plans through [pricing pages](help-documentation-saas-sdk-react-starter-components.md#subscription-plans-table), and we understand that presenting them in the local language can be important for makers selling in their local markets.

[![showing a feature title with accented characters](https://freemius.com/blog/wp-content/uploads/2026/07/accented-char-features-1024x363.png)](https://freemius.com/blog/wp-content/uploads/2026/07/accented-char-features.png)

With that in mind, we have deployed an update where feature titles now fully support any valid characters in any language.

## Improved Plan Filtering UI in Store Pages

We noticed that the plan filter in [several store pages](help-documentation-getting-started-explore-the-developer-dashboard.md) had some UX issue. It shows plans from all products, which you can use for filtering. For example, on the Licenses page, you can choose to filter only by the Professional plan of a specific product. However, because multiple products can have the same plan name, it could become ambiguous.

[![improved plan filter with product icons](https://freemius.com/blog/wp-content/uploads/2026/07/plan-filtering-ui-1024x611.png)](https://freemius.com/blog/wp-content/uploads/2026/07/plan-filtering-ui.png)

The UI has now been improved to show the product icon, along with the product title on hover, making it easier to understand which product’s plan you are selecting.

## Email Customization Preview Improvements

We noticed a few glitches and some room for UX improvements in the [Email Customization](https://freemius.com/help/documentation/emails/email-content-customization/) preview UI. We did a round of optimizations to make the preview more reliable and improve the overall experience.

[![improved Email Customization preview UI](https://freemius.com/blog/wp-content/uploads/2026/07/email-preview-ui-1024x509.png)](https://freemius.com/blog/wp-content/uploads/2026/07/email-preview-ui.png)

For example, the preview UI will now show up eagerly when you set a title. We also fixed a few Markdown syntax rendering issues where the preview did not reflect formatting that our system already supported.