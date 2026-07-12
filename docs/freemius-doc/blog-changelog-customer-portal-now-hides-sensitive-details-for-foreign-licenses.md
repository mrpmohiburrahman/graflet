[Changelog](https://freemius.com/changelog/) / Customer Portal Now Hides Sensitive Details for Foreign Licenses

Freemius’ robust [licensing system](help-documentation-wordpress-license-utilization.md) allows activating a license on a WordPress product that isn’t owned by the website owner. This is particularly useful for agencies that manage client sites, as they can install and manage licenses on behalf of their clients. To maintain privacy, agencies often enable [whitelabel mode](help-documentation-users-account-management-license-security.md#white-label-mode) to hide license keys and other sensitive information from the [WordPress SDK](help-documentation-wordpress-sdk.md).

However, depending on how the client initially installed the product, the same license could sometimes appear as a “foreign license” under the client’s own Customer Portal account.

In such cases, the portal previously displayed the license and allowed actions like upgrading the plan or updating the payment method—actions that should have been restricted.

In this week’s deployment, we’ve addressed and fixed this privacy issue.

[![Foreign license now have restricted view in the Customer Portal](https://freemius.com/blog/wp-content/uploads/2025/11/foreign-license-1024x563.png)](https://freemius.com/blog/wp-content/uploads/2025/11/foreign-license.png)

Now, license keys associated with foreign licenses will remain hidden. The only available action for clients will be to change the license, matching the limited actions available from within the WordPress SDK.

We appreciate our makers for reporting this. While the issue posed no direct security risk, it did raise valid privacy concerns, especially in agency-client setups.