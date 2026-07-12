[Changelog](https://freemius.com/changelog/) / Enhanced Resilience for VAT Verification in Checkout

Freemius Checkout supports automatic [EU & UK VAT number verification and applies tax exemptions](eu-vat-uk-vat-europe.md) under the reverse-charge mechanism.

[![Freemius Checkout VAT Validation](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-checkout-vat-validation-1024x331.png)](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-checkout-vat-validation.png)

Over the past couple of weeks, we noticed intermittent degradation in the third-party service responsible for VAT number validation. To ensure buyers don’t face unexpected friction when requesting VAT exemption, we’ve rolled out an update that makes our verification flow more resilient to these temporary outages. This helps maintain a smooth Checkout experience even when external services are unstable.