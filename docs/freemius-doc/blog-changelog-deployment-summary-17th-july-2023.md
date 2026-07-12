[Changelog](https://freemius.com/changelog/) / Deployment Summary – 17th July, 2023

### Freemius API & Backend

- We fixed our [composer integration](blog-release-notes-wordpress-sdk-2-4-1-deployment-composer-dkim-login-as-user-security.md#install_paid_products_via_composer) which was raising some warnings due to package name mismatches.
- We added a permission for the developer role to generate secure download links for licenses.

### Developer Dashboard

We removed the code snippet that includes the `secret_key` of a product in the SDK integration code. Previously, we included an update to give clear instructions on how to activate development mode in the SDK.

[![](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-developer-dashboard-sdk-integration-code.jpg)](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-developer-dashboard-sdk-integration-code.jpg)

We believe removing the `secret_key` from the main product file is the safer approach, since one can forget to remove it before doing manual deployments to the WordPress.org repository.