---
title: "Trials API (GET /products/{product_id}/trials.json)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Trials"
source: "api"
section: "API Reference"
category: "Trials"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Trials

Operations related to a trial license of a product.

## `GET /products/{product_id}/trials.json`

**List all trials**

List the trial collection associated with the product.

To support trials, configure your product to [offer trial](help-documentation-selling-with-freemius-free-trials.md) and then users can use the [Freemius Checkout](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) to start a trial.

You will need to pass `trial=paid` or `trial=free` to the Checkout's paramters to start a trial.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Trial collection. |

