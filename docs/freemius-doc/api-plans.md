---
title: "Plans API (14 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Plans"
source: "api"
section: "API Reference"
category: "Plans"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Plans

Operations related to plans, pricings and features of a product.

## `POST /developers/{developer_id}/products/{product_id}/plans.json`

**Create a plan**

Create a new plan for the product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | A new plan is created. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /developers/{developer_id}/products/{product_id}/plans/{plan_id}.json`

**Delete a plan**

Delete a specific plan by ID.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |

## `PUT /developers/{developer_id}/products/{product_id}/plans/{plan_id}.json`

**Update a plan**


Update an existing plan by ID.

> Only developers can update plans.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Plan updated |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing.json`

**Create a pricing**

Create new pricing for a plan.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `currency` | query |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The pricing for the plan has been created. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json`

**Delete a plan's pricing**

Delete the plan pricing by ID.

> Only developers can delete a plan pricing.

### Responses

| Status | Description |
|--------|-------------|
| `204` | The plan pricing was deleted. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json`

**Update a pricing**

Update the plan's pricing by ID.

> Only developers can update a plan pricing.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The plan pricing was updated. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/plans.json`

**List all plans**

Retrieve the plans collection.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | List of all the plans. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/plans/currencies.json`

**List all currencies**

Retrieve all the currencies available for all the plans.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The list of all currencies for all the plans. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/plans/{plan_id}.json`

**Retrieve a plan**

Retrieve a specific plan by ID.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Plan listing. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/plans/{plan_id}/features.json`

**List all features**

Retrieve the features collection of a plan.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Feature listing of a plan. |
| `400` |  |

## `GET /products/{product_id}/plans/{plan_id}/pricing.json`

**List all plan's pricing**

Retrieve the collection of all the plan's pricings.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `currency` | query |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The collection of the plan's pricing. |

## `POST /products/{product_id}/plans/{plan_id}/pricing/clone.json`

**Clone pricing to other currency**

Create new pricing in a specified currency from an existing one.

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `201` | New pricing for the currency created. |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json`

**Retrieve a pricing**

Retrieve a specific plan pricing by ID.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The plan pricing. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json`

**Create a license**

Create a new license for the plan and pricing. Please note that:
1. Either `period` or `expires_at` or `is_block_features` must be set.
2. If you create a license with `is_block_features` set to `false` and do not specify `period` and `expires_at`, the license will never expire or block features and will continue to work for lifetime.
3. If you specify an email address, the user must have already activated a license or installed your product before. If your user has not activated a license, then please don't use the field and when they activate the license we will collect their email and register the user with Freemius.
4. Use the `source` parameter only when creating migrated licenses from a legacy system.

More information about every other parameters can be found below.


### Responses

| Status | Description |
|--------|-------------|
| `200` | The license created successfully. |

