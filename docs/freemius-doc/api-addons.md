---
title: "Addons API (3 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Addons"
source: "api"
section: "API Reference"
category: "Addons"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Addons

Operations related to an addon of a product.

## `GET /products/{product_id}/addons/{addon_id}/plans.json`

**List all plans**

Retrieve the plans collection for the addon.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `show_pending` | query |  | If set to `true`, retrieves unreleased add-ons as well. |
| `type` | query |  | Whether to show released addons only or the hidden as well. |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The list of all the plans for the addon. |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/addons/{addon_id}/plans/{plan_id}/features.json`

**List all plan's features**

Retrieve the plan's features collection for the addon.

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
| `200` | List of all the plan's features for the addon. |
| `400` |  |

## `GET /products/{product_id}/addons/{addon_id}/plans/{plan_id}/pricing.json`

**List all pricings**

Retrieve the pricing collection for the addon for specific the plan.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `currency` | query |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The list of all the plans for the addon. |
| `400` |  |
| `401` |  |
| `402` |  |

