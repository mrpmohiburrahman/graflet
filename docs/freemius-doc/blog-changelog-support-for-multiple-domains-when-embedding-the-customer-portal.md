[Changelog](https://freemius.com/changelog/) / Support For Multiple Domains When Embedding The Customer Portal

This week we are releasing a new feature to support embedding our [Customer Portal](help-documentation-users-account-management.md) on more than one domain. Freemius allows you to [embed the Customer Portal](help-documentation-users-account-management-embedding-customer-portal.md#embedding-the-customer-portal-in-your-store) into your own WordPress website to provide a more seamless experience for your buyers. However, for security purposes, the portal will not load unless it has been embedded on the [specified domain](help-documentation-users-account-management-embedding-customer-portal.md#embedding-the-customer-portal-in-your-store).

We understood this could be limiting in real-world workflows. Especially when testing the integration locally or in a staging environment, the URL is often different, making it impossible to see the portal in action.

To address this, you can now go to the **Settings** page of your Store and use the newly introduced **Additional Whitelisted Domains** configuration.

[![Whitelisted domains for customer portal embedding](https://freemius.com/blog/wp-content/uploads/2026/02/additional-whitelisted-domain-customer-portal-1024x528.png)](https://freemius.com/blog/wp-content/uploads/2026/02/additional-whitelisted-domain-customer-portal.png)

You can add as many additional domains or hostnames as needed, and the Customer Portal will load securely on those domains without any issues.