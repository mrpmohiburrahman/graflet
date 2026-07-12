[Changelog](https://freemius.com/changelog/) / Customer Portal Now Supports App Activations Management

This week we are rolling out a significant upgrade to our [Customer Portal](help-documentation-users-account-management.md), aimed specifically at [App makers](help-documentation-saas-app-integration.md). Our system already allows you to handle [license key activations](help-documentation-saas-integrating-license-key-activation.md) using the Freemius API. Once a license is activated, an “[Install](https://docs.freemius.com/api/installations)” entity is created on our end.

However, until now, buyers did not have a simple or proper way to view and manage those activations from the Freemius Customer Portal. To deactivate a license, they had to rely on the app itself or contact the maker, which did not provide the best experience.

Starting today, we are introducing a new **Activations** page in the Customer Portal. From here, your buyers can see the devices or instances where the license has been activated.

[![Activation page Customer Portal](https://freemius.com/blog/wp-content/uploads/2026/03/activations-page-customer-portal-1024x462.png)](https://freemius.com/blog/wp-content/uploads/2026/03/activations-page-customer-portal.png)

Clicking an item will also show the corresponding plan and provide an easy option to upgrade or downgrade.

[![Activation details Customer Portal](https://freemius.com/blog/wp-content/uploads/2026/03/activation-details-customer-portal-1024x347.png)](https://freemius.com/blog/wp-content/uploads/2026/03/activation-details-customer-portal.png)

In addition, buyers can now deactivate a license directly from a device by clicking the deactivate button. A confirmation step is shown before the license is actually deactivated.

[![Deactivate License from the Activations page](https://freemius.com/blog/wp-content/uploads/2026/03/deactivate-license-1024x445.png)](https://freemius.com/blog/wp-content/uploads/2026/03/deactivate-license.png)

### Other Improvements

In addition, we have also refined other sections like Websites and Downloads to make them more suitable for all kinds of products. For example:

1. The Websites and Downloads pages will no longer show App or SaaS products, and they will be completely hidden if no WordPress or template products exist in your store.
2. Similarly, we no longer show the Licenses page if the store contains only SaaS products, since these do not [expose the license key](help-documentation-saas-integrating-license-key-activation.md#revealing-license-keys-to-customers).

Please stay tuned as we continue rolling out more features for App makers. Coming up next is support for configurable download links.