[Changelog](https://freemius.com/changelog/) / New API Endpoints to Access and Cancel Subscriptions from a License

We have deployed two new API endpoints this week to ease our [SaaS integration experience](help-documentation-selling-with-freemius-saas-integration.md). In our guide, we ask to store the license ID after purchase to identify the user and their active plan on Freemius. However, we didn’t have a clear way to access the subscriptions of the user from the license itself. The recommended way was to search for the subscription using the `user_id` from the license. But since a license can have multiple subscriptions associated with it (due to plan upgrades, payment method updates, etc.), we didn’t have a clear instruction or method to find the latest and current subscription associated with the license.

To ease this integration and to provide better Developer Experience, we have introduced two new API endpoints:

### Access Subscription of a License

```
GET https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/subscription.json
```

This will give you the latest subscription under a license. You can use it to show current billing information to your users. More information can be found [here](https://docs.freemius.com/api/licenses/retrieve-latest-subscription).

### Cancel the Subscription

```
DELETE https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/subscription.json
```

This will immediately cancel the subscription and it will not go for any upcoming renewals. The license itself will still stay active until the next renewal time and after that will expire. Find the [API reference](https://docs.freemius.com/api/licenses/cancel-current-subscription) here.