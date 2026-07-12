[Changelog](https://freemius.com/changelog/) / Refined Customer Invoices with Discount Accuracy and Better Readability

In another round of polishing the [customer invoice](blog-changelog-rebranded-customer-invoices-are-live.md), we’re glad to announce the following improvements:

[![Freemius Customer Invoice with many discounts and support email](https://freemius.com/blog/wp-content/uploads/2025/06/customer-invoice-additional-discount-freemius-1024x739.png)](https://freemius.com/blog/wp-content/uploads/2025/06/customer-invoice-additional-discount-freemius.png)

### Discount Rows

Invoices will now properly display discounts, even when the plan or coupon configuration changes. This not only makes the breakdown easier to understand but also ensures there are no discrepancies in the calculated amounts.

### Support Email Fix

We identified and fixed an issue where, in some cases, the maker’s email was incorrectly shown as the support email. The invoice will now correctly use the support email configured either from the [product itself](help-documentation-selling-with-freemius-email-settings.md#product_level_email_settings) or from the [store of the product](help-documentation-selling-with-freemius-email-settings.md#store_level_email_settings).

### Improved Number Alignment

We’ve updated the number rendering to use our branded monospace font. This improves visual alignment of all amounts on the invoice, making it easier to read and verify.

### Better Tax Rounding

We noticed a glitch in rare edge case scenarios where the tax percentage values could appear slightly off. This issue has now been resolved, and the tax amounts will be correctly rounded and displayed.