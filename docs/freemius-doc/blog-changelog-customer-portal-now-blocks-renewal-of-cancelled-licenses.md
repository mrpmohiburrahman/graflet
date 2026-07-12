[Changelog](https://freemius.com/changelog/) / Customer Portal Now Blocks Renewal of Cancelled Licenses

We received a bug report where the [Customer Portal](help-documentation-users-account-management.md) allowed customers to manually renew licenses that had already been cancelled.

Cancelling a license is a deliberate action taken by makers from the Developer Dashboard. In such cases, it’s expected that the license cannot be renewed by the customer afterward.

[![Disabled renew button in the customer portal](https://freemius.com/blog/wp-content/uploads/2026/01/customer-portal-license-renew-button-1024x476.png)](https://freemius.com/blog/wp-content/uploads/2026/01/customer-portal-license-renew-button.png)

To align the Customer Portal with this behavior, the **Renew** button is now disabled for licenses that were manually cancelled by makers. A tooltip is also shown to explain why renewal is no longer available in these cases.