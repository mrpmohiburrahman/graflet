[Changelog](https://freemius.com/changelog/) / Fixed UI bug in proration discount for migrated licenses

Freemius supports both [proration discounts](help-documentation-selling-with-freemius-proration.md) and [migrations](help-documentation-migration.md) from various other platforms.

[![](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-checkout-proration-1024x705.png)](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-checkout-proration.png)

Freemius proration applying 100% first-time discount on a migrated license

Additionally, Freemius automatically offers a proration discount to your customers when they upgrade an existing license to renew through Freemius. This helps with transferring your subscription from the old platform to Freemius, where we handle taxes, disputes, and many [other details](help-documentation-selling-with-freemius.md).

Recently, we identified an edge case bug where the UI incorrectly displayed a proration discount for some migrated licenses that shouldn’t have received one. Although the final payment did not apply the discount, the UI caused confusion for both buyers and makers. We have now fixed this issue.