---
title: "Users API (13 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Users"
source: "api"
section: "API Reference"
category: "Users"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Users

All operations which can be done on a user belonging to a store or a product.

## `GET /products/{product_id}/users.json`

**List all users**


Gets the user collection associated with a product.

## Filtering
There are a few filters that can be applied to the request.

### Search by email
You can specify the parameter `email` to filter the users by email. Optionally you can also put a valid email in the `search` parameter.

### Other filtering options
The `search` parameter also accepts the following values:

1. User ID (number).
2. Full or partial name (string).
3. Full or partial email (string).

## Pagination
You can use the combination of `count` and `offset` parameters to paginate the results.


### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `email` | query |  | Search user by email address. |
| `filter` | query |  | Filter user by their financial status |
| `search` | query |  | Search by user ID, email or name |

### Responses

| Status | Description |
|--------|-------------|
| `200` | OK |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/users.json`

**Create a user**

Create a new user associated with the product.

The user will be linked to the product if they already exist in Freemius.

> User can only be created for products with elevated permissions or during data migration.

## Migrating users from other platforms

Freemius allows to migrate your users from other platforms. To do so, you need to set the `is_migration` parameter to `true`. This will prevent any emails from being sent to the users and will not log any events.
Once migrated the user can use their existing licenses to activate your product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `201` | OK |
| `400` |  |

## `GET /products/{product_id}/users/{user_id}.json`

**Retrieve a user**

Retrieve a user associated with your product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The product user data. |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/users/{user_id}.json`

**Update a user**

Update a user associated with your product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The product user updated data. |

## `GET /products/{product_id}/users/{user_id}/billing.json`

**Retrieve billing**

Retrieves the billing information of a user for a specific product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Billing Information retrieved. |
| `401` |  |
| `402` |  |

## `PUT /products/{product_id}/users/{user_id}/billing.json`

**Update or create billing**

Update or create the billing information for a user.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Billing information updated. |

## `GET /products/{product_id}/users/{user_id}/events.json`

**List all events**

Retrieve a log of the events for the user associated with the product. Freemius tracks events such as opt-in, license activation, purchase etc. You can use this data for marketing and other automation purposes. More information can be found [here](help-documentation-marketing-automation-events-webhooks.md).

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The user's events log. |

## `GET /products/{product_id}/users/{user_id}/installs.json`

**List all installs**

Retrieve the install collection associated with the user.

 Various filtering and search parameters are available to narrow down the results.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `install_ids` | query |  | Comma-separated install IDs list to filter. |
| `license_id` | query |  | License ID filter. If set, return installs that are linked to the specified license. |
| `plan_id` | query |  | Plan ID filter. If set, return installs associated with the given plan. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Installs collection |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/users/{user_id}/licenses.json`

**List all licenses**

Retrieve the license collection associated with a user.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `license_key` | query |  | Retrieve specific license by its key. |
| `ids` | query |  | Comma-separated license IDs. |
| `license_keys` | query |  | Retrieve specific multiple license with a comma-separated string of their license keys. |
| `type` | query |  | The type of license. |
| `` |  |  |  |
| `is_enriched` | query |  | Returns the license's product type. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | License collection. |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/users/{user_id}/payments.json`

**List all payments**

Retrieve the payment collection associated with a user.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `extended` | query |  | If `true`, loads linked user, plan and subscription. |
| `include_addons` | query |  | Returns the plugin add-ons' payments as well. |
| `include_bundles` | query |  | Returns the plugin bundles' payments as well. |
| `filter` | query |  | Filter the payments by the status. |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Payment collection. |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/users/{user_id}/payments/{payment_id}/invoice.pdf`

**Download invoice**

Download invoice of a payment of a user. Use this endpoint to securely download the invoice of a payment belonging to a user. This is useful for implementing your own Customer Portal with download links to invoices.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | PDF invoice |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/users/{user_id}/subscriptions.json`

**List all subscriptions**

Retrieve the subscription collection associated with a user.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `extended` | query |  | Enrich the subscriptions with the plan name, install URL & title, and user email. |
| `filter` | query |  | Filter the subscriptions by the status. |
| `billing_cycle` | query |  | Filter by billing cycle. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `plan_id` | query |  | Filter the subscriptions by the plan ID. |
| `sort` | query |  | Sort the subscriptions by the ID or the next payment date. |
| `search` | query |  | Search by subscription ID, external subscription ID or user email. |
| `enrich_with_cancellation_discounts` | query |  | When set to `true` enrich the subscription to include any cancellation discounts applied to the subscriptions. |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Subscription collection. |

## `POST /products/{product_id}/users/{user_id}/tokens/checkout.json`

**Create a checkout token**

Create a 1 min long token that represents the details of the user for setting the user context in a checkout session. Please read our [documentation](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#user_token_in_checkout_new) to learn how to use it.

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `201` | The created checkout token. |
| `401` |  |

