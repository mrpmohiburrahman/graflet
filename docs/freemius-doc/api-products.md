---
title: "Products API (19 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Products"
source: "api"
section: "API Reference"
category: "Products"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Products

All operations which can be done on a product.

## `PUT /developers/{developer_id}/products/{product_id}/emails/addresses.json`

**Update email addressses**

Update the email addresses associated with a product.

> Only a plugin's developer can update the email addresses of their plugin.

### Responses

| Status | Description |
|--------|-------------|
| `204` | Email addresses updated. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}.json`

**Retrieve a product**

Query and retrieve a specific product by ID.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | OK |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}.json`

**Update a product**

Update a specific product by ID.

### Responses

| Status | Description |
|--------|-------------|
| `200` | OK |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/addons.json`

**List all addons**

Retrieve the addons collection.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `show_pending` | query |  | Whether to show released addons only or the hidden as well. |
| `enriched` | query |  | If set to `true`, returns marketing info. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The list of all the addons. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/emails/addresses.json`

**Delete all email addresses**

Delete all email addresses associated with a product. Sets the product to use the default store-level email addresses.

### Responses

| Status | Description |
|--------|-------------|
| `204` | Email addresses deleted. Product set to use the default store-level email addresses. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/emails/addresses.json`

**List all email addresses**

Retrieve the email addresses collection associated with a product. In case the product is using the store's email address configuration, the endpoint will return a `404` error.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | The list of all the email addresses associated with a product. |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/features.json`

**List all features**

Retrieve the product features collection.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The product features collection. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/features/{feature_id}.json`

**Delete a feature**

Delete a product's feature.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `204` |  |

## `GET /products/{product_id}/features/{feature_id}.json`

**Retrieve a feature**

Retrieve a product's feature.

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
| `200` | The product's feature. |
| `400` |  |

## `PUT /products/{product_id}/features/{feature_id}.json`

**Update a feature**

Update a product's feature. Please note that the `value` attribute can only be set and updated per plan with a developer scope authorization.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The updated feature. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/info.json`

**Get product info**

Get product info. Please use the Developer Dashboard to update the information of a product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Successful operation |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/is_active.json`

**Check product status**

Check if the product is active.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_update` | query |  | You can use this flag in conjunction with the Moderation Setting of your product.

In case you want to limit the activation of your product to new instances only (say after migrating to Freemius) you can check the relevant settings from the Developer Dashboard and from your product make an API request like below:

- If your product is already active in some device before joining Freemius - Set value to `true`.
- Otherwise set value to `false`.

This will also work with any “Activation limitation” you have put in your Moderation settings. |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Product status. |

## `GET /products/{product_id}/ping.json`

**GDPR compliance check**

Find out if a product requires GDPR compliance based on the client's location.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `uid` | query | Yes | Unique identifier of the caller. The UID must be same when pinging and when activating or deactivating a license. The generation of the UID is a responsibility of the client. |
| `is_update` | query |  | If the call is during a product update. |
| `is_gdpr_test` | query |  | Whether the request is made for testing GDPR compliance from the client of the product. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Response from the product |
| `400` |  |
| `401` |  |
| `404` |  |

## `POST /products/{product_id}/portal/login.json`

**Generate portal login link**

Generate a direct login link for a user in the context of the store of the product. The login link is valid for 5 minutes from generation. Either user ID or email must be provided.

### Responses

| Status | Description |
|--------|-------------|
| `201` | Portal login link generated successfully. |
| `400` |  |
| `404` |  |

## `GET /products/{product_id}/pricing.json`

**Retrieve the pricing table data**

Retrieve the plugin's full features & pricing data for a pricing table. Used by our [JS SDK](help-documentation-saas-sdk-react-starter-components.md#subscription-plans-table), and [WordPress SDK](help-documentation-wordpress-sdk-wp-admin-in-dashboard-upgrading.md) to create pricing components and pages.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `currency` | query |  | The currency to use for the pricing. |
| `show_pending` | query |  |  |
| `type` | query |  | Whether to show all plans or only the visible ones. |
| `is_enriched` | query |  | If set to `true`, the result will be enriched with some of the context plugin's information. |
| `bundle_product_id` | query |  | (optional) (Development Only) The ID of the parent bundle product. When getting the pricing of a product, if the product is part of a bundle, you can set the value here (along with the public key of the bundle). This will be used to determine the trial status of the product in sandbox mode. Our WP SDK uses it internally. |
| `bundle_product_public_key` | query |  | (optional) (Development Only) Used alongside the `bundle_product_id` parameter. |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The features and pricing data. |

## `DELETE /products/{product_id}/settings/{setting_id}.json`

**Delete a setting**

Delete a specific product setting.

### Responses

| Status | Description |
|--------|-------------|
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/settings/{setting_id}.json`

**Retrieve a setting**

Retrieve a specific product setting.
 > Different settings are used for different functionalities around product. Please use the Developer Dashboard instead to modify the functionality.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The product setting. |
| `400` |  |
| `401` |  |
| `402` |  |

## `PUT /products/{product_id}/settings/{setting_id}.json`

**Update a setting**

Update a specific product setting.
 > Different settings are used for different functionalities around product. Please use the Developer Dashboard instead to modify the functionality.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Updated product settings. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/skip.json`

**Skip account connection**

Skip the account connection step for the specified product. This is useful for testing purposes or for WordPress product integration. The functionality is handled automatically by our [WordPress SDK](https://github.com/Freemius/wordpress-sdk).

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `204` |  |

