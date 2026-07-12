[Changelog](https://freemius.com/changelog/) / Improved Invoice Details and Product Attribution

Following feedback from our makers community, we are releasing several improvements to the [customer invoices](help-documentation-users-account-management-orders-history.md#generate-a-printable-invoice) this week.

[![Freemius Customer Invoice](https://freemius.com/blog/wp-content/uploads/2025/11/customer-invoice-1024x815.png)](https://freemius.com/blog/wp-content/uploads/2025/11/customer-invoice.png)

### Better Invoice Header

For [SaaS & Apps](help-documentation-saas.md), it didn’t make sense to include the `slug` of a product in the invoice title. While the slug helps identify WordPress products, it only added confusion for other product types. With this change, the invoice header is now cleaner and more relevant for SaaS & Apps.

### Smarter Product URL

We’ve made the product URL smarter in the invoice. It will now first try to use the URL from the product settings.

[![Product Marketing URL reflected in the Invoice](https://freemius.com/blog/wp-content/uploads/2025/11/product-marketing-url-config-invoice-1024x639.png)](https://freemius.com/blog/wp-content/uploads/2025/11/product-marketing-url-config-invoice.png)

If no product URL is defined, it will fall back to the store URL and, finally, to the maker’s billing information. This makes the invoice better aligned with the actual product context, instead of defaulting to the general billing address as before.

### Dynamic License Unit Labels

We noticed a bug where the item description wasn’t showing [custom license unit labels](help-documentation-saas-customize-license-unit-label.md) for App & SaaS product types.

[![Dynamic License Unit Label in the Invoice](https://freemius.com/blog/wp-content/uploads/2025/11/invoice-customer-description-1024x505.png)](https://freemius.com/blog/wp-content/uploads/2025/11/invoice-customer-description.png)

This has now been fixed, ensuring that invoices clearly display what the customer purchased, with accurate and dynamic unit labels.