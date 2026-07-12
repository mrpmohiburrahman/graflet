[Changelog](https://freemius.com/changelog/) / Better Product Settings UX, Transfer Flow Updates, and SaaS Refund Improvements

This week we’re rolling out various improvements and bug fixes to our Developer Dashboard. Many of these updates come directly from maker feedback, while others are aimed at improving the overall UX.

### Improved Product Transfer Form

Freemius allows you to easily [transfer your product](help-documentation-security-team-member-role-management.md#assigning-a-new-owner) to a new owner. This is especially useful when acquiring or selling a business.

[![Product transfer dialog](https://freemius.com/blog/wp-content/uploads/2026/03/product-transfer-dialog-1024x429.png)](https://freemius.com/blog/wp-content/uploads/2026/03/product-transfer-dialog.png)

We noticed some inconsistencies in the transfer dialog UI, especially around transferring a product to the new owner’s store. To make the flow easier to understand, we have revised the UI copy.

### Improved Product Settings Page UX

The product settings page intentionally does not auto-update when configurations are changed. Since some changes can have important side effects, we require makers to click the Update button for the changes to take effect. However, because the button was placed below a long form, it was easy to miss and often caused confusion.

[![Product settings page improvement](https://freemius.com/blog/wp-content/uploads/2026/03/product-settings-page-1024x754.png)](https://freemius.com/blog/wp-content/uploads/2026/03/product-settings-page.png)

To improve this:

1. The Update button will now stay stuck to the bottom whenever there are unsaved changes in the settings.
2. If you try to navigate away from the page with unsaved changes, we will show a confirmation message.

In addition, we noticed that the Delete button was placed next to the Update button.

[![Danger zone - delete product](https://freemius.com/blog/wp-content/uploads/2026/03/danger-zone-delete-product-1024x413.png)](https://freemius.com/blog/wp-content/uploads/2026/03/danger-zone-delete-product.png)

To make the action completely separate, we have moved the Delete button to a separate section and added a disclaimer for this destructive action.

### Improved Refund Dialog for SaaS

Freemius allows you to easily [process refunds](help-documentation-selling-with-freemius-refund-payment.md). The refund form is also quite powerful, letting you choose what to do with the associated subscription and license.

However, we noticed that showing options related to WordPress licenses in the SaaS context could be confusing. In WordPress, our SDK treats license flags such as `expiration` and `is_cancelled` differently depending on how [plans are configured](help-documentation-wordpress-license-utilization.md#blocking-or-allowing-features-after-license-expiration). This gives makers flexibility to block updates while keeping paid access, or revoke paid access altogether. SaaS products, on the other hand, do not have the same behavior or configuration model.

[![SaaS payment refund form](https://freemius.com/blog/wp-content/uploads/2026/03/refund-form-ux-saas-998x1024.png)](https://freemius.com/blog/wp-content/uploads/2026/03/refund-form-ux-saas.png)

To make the refund flow clearer, we now show only two license-related options in the SaaS refund dialog: whether to keep the paid benefit or revoke it. We hope this makes the system simpler and more intuitive for our SaaS makers.

### Other Enhancements

- The registration form has been updated to use the same questionnaire as our new product registration form.
- Fixed a UI glitch where the expiration date of a lifetime license was shown incorrectly.