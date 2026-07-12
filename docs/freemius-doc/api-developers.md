---
title: "Developers API (3 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Developers"
source: "api"
section: "API Reference"
category: "Developers"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Developers

All operations which can be done from on a developer.

## `POST /developer/{developer_id}/products/{product_id}/installs/{install_id}/members.json`

**Add team member**

Add new team member to the product.

> Only a developer with priviledge can add a new team member to a product.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Team member added successfully. |
| `400` |  |

## `GET /developers/{developer_id}/bank_account/{bank_account_id}.json`

**Retrieve bank account**

Retrieve the developer's bank account.

### Responses

| Status | Description |
|--------|-------------|
| `200` | OK |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /developers/{developer_id}/login.json`

**Log in**


Call this endpoint with your developer email and password and optionally 2FA auth code to login and set the authorization cookie.

> This is a public endpoint and does not require any authentication.

Please note that this endpoint is not meant for public use and should only be used by the Freemius Developer Dashboard. The login can expect a reCAPTCHA token and it will only work if the reCAPTCHA widget is initialized from the Developer Dashboard itself.
To get API tokens for a product or a store, please do it from the Developer Dashboard app itself.


### Responses

| Status | Description |
|--------|-------------|
| `200` | Successful login. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

