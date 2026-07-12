[Changelog](https://freemius.com/changelog/) / Checkout and backend improvements – Fixing the Dunning app

### Fixed the Dunning app on Freemius Checkout

We fixed an integration issue with our Checkout Dunning app and the new security layer. Due to a bug in the system, the dunning app would be stuck in limbo when the security layer was throwing a reCAPTCHA error and would not show the UI to render the reCAPTCHA.

[![Freemius Checkout dunning app](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-checkout-dunning-recaptcha.jpg)](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-checkout-dunning-recaptcha.jpg)

As a part of the fix, we also improved the error messages shown to the end user that may come from the firewall. The dunning app will also work well if the security layer asks for a 2FA authentication.

[![Freemius Checkout Dunning app 2FA](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-checkout-dunning-2fa.jpg)](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-checkout-dunning-2fa.jpg)

### Other Backend Changes (API)

- Fixed an API endpoint issue that meant a product’s settings could not be updated if the product was not a theme or a plugin.