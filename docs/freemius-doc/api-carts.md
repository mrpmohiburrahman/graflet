---
title: "Carts API (5 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Carts"
source: "api"
section: "API Reference"
category: "Carts"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Carts

All operations which can be done on a cart belonging to a store or a product.

## `GET /products/{product_id}/carts.json`

**List all carts**

Retrieve the cart collection associated with your product.

> If `enriched=true` you will get more details about the cart for example the `gross`, `coupon_code` and `licenses` fields.

> You can use the `filter` or `email` or `count` parameters to get more refined results from your query. Please learn more about the individual parameters below.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `filter` | query |  | You can use the `filter` parameter to filter by status. If you don't provide a status, the endpoint will return all carts. |
| `` |  |  |  |
| `` |  |  |  |
| `enriched` | query |  | Defaults to false, if true returns enriched cart details. |
| `email` | query |  | Filter the cart collections by the email address. |
| `count` | query |  | Number of carts to retrieve. |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `200` | Provides a collection of carts associated with the product. All carts are listed under the `carts` key. |
| `400` |  |
| `401` |  |

## `DELETE /products/{product_id}/carts/{cart_id}.json`

**Delete a cart**

Delete a particular cart.

### Responses

| Status | Description |
|--------|-------------|
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/carts/{cart_id}.json`

**Retrieve a cart**

Retrieve cart details associated with the product.

> You can use `enriched=true` to get more details about the cart, for example the `gross`, `coupon_code` and `licenses` fields will only be returned if enriched is enabled. Please see individual parameters in the response data below to learn more.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `enriched` | query |  | Defaults to false, if true returns enriched cart details. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Cart details associated with the product. |
| `400` |  |
| `401` |  |
| `402` |  |

## `PUT /products/{product_id}/carts/{cart_id}.json`

**Update a cart**

Update the details of a particular cart.

> Updating a completed checkout cart is prohibited.

> Updating the coupon requires both the `coupon_id` and `coupon_code`.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `200` | Provides the updated cart with details. |
| `400` |  |

## `GET /products/{product_id}/carts/{cart_id}/events.json`

**Retrieve cart events**

Get the list of events associated with a cart.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The cart's events collection. |

