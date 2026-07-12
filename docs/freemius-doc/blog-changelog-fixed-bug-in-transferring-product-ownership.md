[Changelog](https://freemius.com/changelog/) / Fixed Bug in Transferring Product Ownership

At Freemius, we make it really easy (and secure) to [transfer product ownership](help-documentation-security-team-member-role-management.md#assigning_a_new_owner). This becomes a valuable tool when selling products or during acquisitions.

Recently, we noticed an edge case where the product transfer was failing if the new owner had not yet registered a store with Freemius.

[![Freemius Change Owner dialog UI](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-product-transfer-1024x442.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-product-transfer.png)

We have now fixed this bug. If the new owner doesn’t have a store, Freemius will automatically create one for them, using the product’s name as the store name to help them get started quickly.