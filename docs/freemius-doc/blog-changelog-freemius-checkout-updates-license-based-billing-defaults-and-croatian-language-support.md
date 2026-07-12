[Changelog](https://freemius.com/changelog/) / Freemius Checkout Updates: License-Based Billing Defaults and Croatian Language Support

This week we rolled out the following updates for the Freemius Checkout.

### Billing Cycle Now Defaults to the License

We found that our Checkout defaulted to the annual billing cycle in the context of a [license update](help-documentation-checkout-integration-generate-renewal-payment-method-update-link.md#generate-links-with-api). This could create confusion for buyers, especially when renewing their license from the [Customer Portal](help-documentation-users-account-management.md) or [upgrading to a different plan](https://docs.freemius.com/api/licenses/generate-upgrade-link). To make the experience more consistent, Checkout will now respect the billing cycle of the license by default.

[![Checkout License Update](https://freemius.com/blog/wp-content/uploads/2026/03/license-update-1024x752.png)](https://freemius.com/blog/wp-content/uploads/2026/03/license-update.png)

You can still generate [custom upgrade links](help-documentation-saas-saas-integration.md#handling-license-or-subscription-upgrades) with a different billing cycle, for example to promote an upgrade from monthly to annual, and that behavior remains unchanged.

### New Hrvatski Language Support for Croatia

We have released beta language support for Hrvatski. To use it right away, simply pass `language: 'hr'` while configuring the [language of the Checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md#language%20%7C%20locale).

[![Croatian language support for Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2026/03/hr-checkout-language-1024x672.png)](https://freemius.com/blog/wp-content/uploads/2026/03/hr-checkout-language.png)

Our Checkout already supports the EUR currency, and with this release we hope to make the buying experience feel more native for buyers in Croatia. The translation is currently in beta as we gather feedback from makers. Once it is out of beta, it will be selected automatically when the Checkout is loaded with `language: 'auto'`.