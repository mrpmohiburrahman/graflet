---
title: "Payments API (3 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Payments"
source: "api"
section: "API Reference"
category: "Payments"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Payments

All operations associated to a payment.

## `GET /products/{product_id}/payments.json`

**List all payments**

Retrieve the payment collection associated with the product.

### Filtering and searching

You search and/or filter payments with these parameters:

- `search` - You can search by `payment_id`, `external_payment_id`, or `user_email`. It can be a number or string.
- `user_id` - If you are looking to list all payments for a specific user use this.
- `billing_cycle` - Filter payments by billing cycle. `0` means lifetime payments.
- `currency` - Filter payments by currency.
- `coupon_id` - Filter payments by coupon ID.
- `filter` - Filter payments by different types: `all`, `refunds`, `not_refunded`, `disputed`, `won_disputes`, `chargebacks`.

Please see the parameters in the responses body for more information.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `search` | query |  | Search by `payment_id`, `external_payment_id`, or `user_email`. |
| `search_user_id` | query |  | User ID to filter with. |
| `` |  |  |  |
| `currency` | query |  |  |
| `coupon_id` | query |  | Filter payments by coupon ID. |
| `filter` | query |  | Filter payments by different types |
| `extended` | query |  | If true, loads linked user, plan and subscription. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The payment collection. |
| `400` |  |

## `GET /products/{product_id}/payments/{payment_id}.json`

**Retrieve a payment**

Retrieve a specific payment.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Retrieve a specific payment. |

## `GET /products/{product_id}/payments/{payment_id}/invoice.pdf`

**Download invoice**

Download invoice of a payment.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | PDF invoice |
| `400` |  |
| `401` |  |
| `402` |  |

