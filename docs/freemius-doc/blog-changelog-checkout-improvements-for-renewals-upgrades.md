[Changelog](https://freemius.com/changelog/) / Checkout Improvements for Renewals & Upgrades

This week we’re rolling out several improvements and bug fixes across the Checkout, especially around license renewals, upgrades, and payment-method updates. These updates aim to reduce friction for makers who generate Checkout links programmatically or rely on dynamic license flows.

### `plan_id` no longer required for payment-method updates

Previously, updating a payment method required passing a `plan_id`. While this worked fine when using our [API](https://docs.freemius.com/api/licenses/generate-upgrade-link) or the [Developer Dashboard](blog-changelog-checkout-related-enhancements-for-the-developer-dashboard.md#new_license_action_to_copy_payment_method_update_link), generating these links directly in code often created confusion because it wasn’t clear where the `plan_id` should come from.

[![Payment method update UI in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-payment-method-update-1024x909.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-payment-method-update.png)

To simplify the process, the Checkout can now infer the correct plan automatically. All you need is the license key, making the payment-method update flow far easier to integrate.

```
https://checkout.freemius.com/product/<productID>/?license_key=<licenseKey>&is_payment_method_update=true
```

### Respecting the `licenses` parameter in License Update flows

The Checkout supports pre-loading a quota using the [`licenses`](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/#licenses) parameter. For example, if your pricing includes tiers for 1000, 5000, and 10,000 units, you can preselect one like:

```
https://checkout.freemius.com/product/<productID>/plan/<planID>/licenses/5000/
```

[![Preselected license quantity in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-licenses-dropdown-1024x713.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-licenses-dropdown.png)

However, this didn’t previously work during [license-upgrade flows](help-documentation-saas-saas-integration.md#handling-license-or-subscription-upgrades), where makers often rely on preselected quantities to guide users toward the correct tier. This has now been fixed so the parameter is consistently honored.

### Additional Fixes

- We identified an edge case where altering a license’s quota in the Developer Dashboard could cause the Checkout’s quota dropdown to display incorrect values. The UI glitch has been resolved.
- The legacy Checkout has now been fully removed from our platform. Passing `checkout_style=legacy` will no longer have any effect and the new design will load by default.