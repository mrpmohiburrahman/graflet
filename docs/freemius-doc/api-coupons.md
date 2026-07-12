---
title: "Coupons API (12 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Coupons"
source: "api"
section: "API Reference"
category: "Coupons"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Coupons

All operations which can be done on a coupon belonging to a store or a product.

## `GET /products/{product_id}/coupons.json`

**List all coupons**

Retrieve the coupon collection associated with your product.

### Searching and filtering

You can use filtering to search for a particular coupon or a group of coupons. The available parameters are:

- `code` - You can explicitly search coupon by the code.
- `search` - You can search by coupon code or coupon ID.
- `prefix` - You can filter by coupon code prefix.

> If using search and filtering, then the `is_enriched` parameter is ignored.


### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `code` | query |  | The coupon code filter. |
| `is_enriched` | query |  | If `true`, each coupon will include multi-currency discount properties. Coupons will only be enriched if no filtering is used. |
| `` |  |  |  |
| `` |  |  |  |
| `prefix` | query |  | Optional coupon code prefix for search coupons. |
| `search` | query |  | Optional coupon code(or code part) for search coupons. |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `200` | Provides a collection of coupons associated with the product. All coupons are listed under the `coupons` key. |

## `POST /products/{product_id}/coupons.json`

**Create a coupon**

Create a new coupon.

Alternatively, you can use the [Freemius Developer Dashboard](https://dashboard.freemius.com).

> If you're creating coupon from your SaaS for some specific use case, please be sure to set the `plans`, `redemptions_limit`, `end_date`, and `is_one_per_user` properties to the appropriate values, to avoid misuse.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `201` | The coupon is created. |

## `GET /products/{product_id}/coupons/special.json`

**Retrieve special coupons**

Get the details of a special coupon.
     *
### Searching and filtering

You can use filtering to search for a particular coupon or a group of coupons by `type`.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `type` | query |  | Filter based on a coupon type. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The special coupons details. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/coupons/{coupon_id}.json`

**Delete a coupon**

Delete a specific coupon by ID.

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/coupons/{coupon_id}.json`

**Retrieve a coupon**

Get details of a specific coupon by ID.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The coupon is retrieved successfully. |

## `PUT /products/{product_id}/coupons/{coupon_id}.json`

**Update a coupon**

Update a specific coupon's details by ID.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The coupon is updated. |

## `DELETE /products/{product_id}/coupons/{coupon_id}/note.json`

**Delete a note**

Delete a note for a coupon.

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/coupons/{coupon_id}/note.json`

**Retrieve a note**

Get the details of a note associated with a coupon.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The coupon note details. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/coupons/{coupon_id}/note.json`

**Create a note**

Create a new note for a coupon.

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `201` | The note was added to the coupon. |
| `400` |  |
| `401` |  |

## `PUT /products/{product_id}/coupons/{coupon_id}/note.json`

**Update a note**

Update a note for a coupon.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The coupon note was updated. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/coupons/{coupon_id}/special/{special_id}.json`

**Delete a special coupon**

Delete a special coupon by ID.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `204` |  |

## `PUT /products/{product_id}/coupons/{coupon_id}/special/{special_id}.json`

**Create a special coupon**

Create a special coupon.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `201` | The special coupon has been created. |

