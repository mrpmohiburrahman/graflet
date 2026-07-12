---
title: "Subscriptions API (6 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Subscriptions"
source: "api"
section: "API Reference"
category: "Subscriptions"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Subscriptions

All operations associated to a subscription.

## `GET /products/{product_id}/subscriptions.json`

**List all subscriptions**

Retrieve the subscription collecttion associated with your product.
> Subscriptions are created when someone purchases your product using the [Freemius Checkout](checkout.md).

### Searching and filtering
There are various parameters to help you search and/or filter subscription.
- You can search by subscription ID, external subscription ID, or user email.
- You can also filter by billing cycle, gateway, plan ID, and subscription status.
Please see the parameters for more information.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `search` | query |  | Optional search: subscription id, external subscription id or user email |
| `` |  |  |  |
| `` |  |  |  |
| `filter` | query |  | Optional filtering based on the status of the subscription. Defaults to `all`. |
| `extended` | query |  | When set to `true` enrich the subscriptions with the plan name, install URL & title, and user email. |
| `enrich_with_cancellation_discounts` | query |  | When set to `true` enrich the subscription to include any cancellation discounts applied to the subscriptions. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `sort` | query |  | The sort order of the subscriptions. Example: -id. Default: -id. |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | Provides a collection of subscriptions associated with the product. All subscriptions are listed under the `subscriptions` key. |
| `400` |  |
| `401` |  |

## `DELETE /products/{product_id}/subscriptions/{subscription_id}.json`

**Cancel a subscription**

Use this endpoint to **cancel the subscription**. If the subscription is currently in a **trialing state**, this will also cancel the trial.

This is useful when you want to programmatically offer a cancellation feature from within your SaaS or custom dashboards. If you're integrating Freemius with your SaaS, please see our [guide here](help-documentation-selling-with-freemius-saas-integration.md).

> ⚠️ This action is irreversible and will immediately cancel the subscription or trial.

Cancelling an already cancelled subscription will not have any effect and the endpoint will return the same subscription details as before.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `reason_ids` | query |  | Optional cancellation reason IDs. |
| `reason` | query |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Subscription retrieved. |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/subscriptions/{subscription_id}.json`

**Retrieve a subscription**

Retrieve a subscription associated with your product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | Subscription retrieved. |
| `401` |  |

## `PUT /products/{product_id}/subscriptions/{subscription_id}.json`

**Update a subscription**

Update a subscription to activate a cancellation coupon.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Subscription retrieved. |

## `GET /products/{product_id}/subscriptions/{subscription_id}/payments.json`

**List all payments**

Retrieve the payment collection associated with the subscription.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Provides a collection of payments associated with the subscription. All payments are listed under the `payments` key. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/subscriptions/{subscription_id}/payments.json`

**Create a new migrated payment**

In case you want to synchronize migrated subscription from the legacy platform use this endpoint to have our system log a migrated payment. Depending on your use case you can also choose to extend the license. Please read our [migration documentation](help-documentation-migration.md) to learn more.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The payment was successfully created. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

