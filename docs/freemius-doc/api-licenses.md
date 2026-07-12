---
title: "Licenses API (18 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Licenses"
source: "api"
section: "API Reference"
category: "Licenses"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Licenses

All operations which can be done on a license belonging to a store or a product.

## `POST /developers/{developer_id}/products/{product_id}/licenses/{license_id}/installs/sync.json`

**Sync all activations**

Sync all the license activations with the actual available installs.

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
| `200` | License activations synced. |

## `GET /products/{product_id}/installs/{install_id}/licenses/{license_id}/subscriptions.json`

**List all subscriptions**

Retrieve the subscription collection associated with a license.

> A license can have one active and multiple inactive subscriptions. Subscriptions are inactivated when a license is downgraded or upgraded or when the payment method is updated.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Subscriptions collection. |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/licenses.json`

**List all licenses**

Retrieve the license collection associated with a product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `filter` | query |  | Filter licenses by status. |
| `plan_id` | query |  | Filter licenses by plan ID. |
| `search` | query |  | Search license id or key. |
| `enriched` | query |  | If `true`, returns the associated user information. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `source` | query |  | If set, returns only licenses that are associated with the given source ID. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The licenses collection is retrieved. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/licenses.json`

**Assign a license**

Associate an orphan license with a user and send a welcome email. If the user does not exist yet, one will be created.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The license is assigned. |
| `400` |  |
| `401` |  |
| `402` |  |

## `POST /products/{product_id}/licenses/activate.json`

**Activate a license**

Activate a license and if needed, create an install with the given properties.

> No Authorization header is required. If the provided license doesn't have an associated user, the endpoint will require the `first_name`, `last_name`, and `user_email` parameters to create a new user and associate it with the license.

This endpoint can return the following error codes:

- `license_expired`: License has already expired.
- `invalid_license_key`: License key is invalid (e.g., does not match any record).
- `license_error`: General error while validating the license.
- `license_utilized`: License quota has reached maximum capacity.
- `license_activated`: License is already activated on the given install. This usually indicates your app is out of sync with Freemius. You may accept the license and grant premium features. If needed, re-establish the connection by calling the [deactivation endpoint](../licenses/deactivate) and activating again.

All errors include a descriptive message from the API, which you may choose to display to the user. For example:

- `license_expired`: Your license has expired on 2025-01-01 (id = 12345).
- `invalid_license_key`: Invalid license key.
- `license_error`: License activation is not authorized for the site(s) listed below. Please follow the provided link to whitelist the site(s) from the User Dashboard.
- `license_activated`: License is already activated on install 12345.
- `license_utilized`: Your license quota of 1234 production site(s) has been reached. If you believe this is a mistake, please contact support at example@freemius.com.

You can get the error code from the `response.error.code`. For example

```js
fetch(activationEndpoint).then((response) => {
    return response.json();
}).then((data) => {
    if (data.error) {
        // Error detected
        const errorCode = data.error.code;
        const errorMessage = data.error.message;
        // handleError(errorCode, errorMessage);
    } else {
        // Operation successful
    }
}).catch((error) => {
    // Handle network error
});
``` 

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | License activated successfully. |
| `400` |  |
| `402` |  |

## `POST /products/{product_id}/licenses/deactivate.json`

**Deactivate a license**

Deactivate a license from an install (No Authorization header is required).

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | License deactivated. |
| `400` |  |
| `401` |  |
| `402` |  |

## `POST /products/{product_id}/licenses/resend.json`

**Resend license keys**

Send an email from Freemius with all the license keys associated with the given email address. The email is sent to the email address.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The license key has been resent. |

## `DELETE /products/{product_id}/licenses/{license_id}.json`

**Cancel a license**

Cancel or delete a license. The Delete action is irreversible and will remove the license from the system.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `delete` | query |  | (optional) Whether to delete the license. If not `true` then the license is cancelled. |
| `include_bundle` | query |  | (optional) Whether to include the bundle license in the deletion or delete the main license only. |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` |  |
| `204` |  |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/licenses/{license_id}.json`

**Retrieve a license**

Retrieve a specific license by its ID.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The retrieved license. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/licenses/{license_id}.json`

**Update a license**

Update a specific license by its ID. For ownership transfer please use the `new_user_id`. Ownership transfer is not supported for SaaS products.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The updated license. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/licenses/{license_id}/checkout/link.json`

**Generate upgrade link**

Generate an upgrade link for a license. The API accepts a variety of parameters with which you can specify new plans or quota or billing cycles. If you skip all those, then a manual renewal link will be generated instead. The link will be valid for 24 hours.

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `201` | Upgrade link generated successfully. |
| `400` |  |
| `402` |  |

## `DELETE /products/{product_id}/licenses/{license_id}/installs.json`

**Deactivate installs**

Deactivate license from all installs.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | Licenses deactivated from all installs. |
| `400` |  |
| `401` |  |

## `POST /products/{product_id}/licenses/{license_id}/renewals.json`

**Send the renewal email**

Send the manual license renewal email. The system will send emails only for licenses with cancelled or inactive subscriptions.

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | The license renewal email is sent. |
| `400` |  |
| `401` |  |

## `POST /products/{product_id}/licenses/{license_id}/resend.json`

**Resend the upgrade email**

Resend the license upgrade email.

### Responses

| Status | Description |
|--------|-------------|
| `200` | License email resent. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/licenses/{license_id}/subscription.json`

**Cancel current subscription**

Use this endpoint to **cancel the active subscription** associated with a license. If the license is currently in a **trialing state**, this will also cancel the trial.

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

## `GET /products/{product_id}/licenses/{license_id}/subscription.json`

**Retrieve latest subscription**

A license can have only **one active subscription** at any given time. However, users may **upgrade**, **downgrade**, or **change their payment method**, which may result in a new subscription being created and associated with the same license.

Use this endpoint to **retrieve the latest or currently active subscription** linked to a specific license.

This is useful when you're building tools for license management or need to inspect the billing state of a customer. If you're integrating Freemius with your SaaS please refer to our [guide here](help-documentation-selling-with-freemius-saas-integration.md).

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Subscription retrieved. |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/users/{user_id}/licenses/{license_id}/review_url.json`

**Get review URL**

Retrieve the review URL associated with a license.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The retrieved review URL. |
| `400` |  |

## `POST /products/{product_id}/users/{user_id}/licenses/{license_id}/reviews.json`

**Create a review**

Create a review associated with a license. If you want to create/import reviews which are not associated with a license or from a different system, please use the Review endpoint under `products/{product_id}/reviews.json`.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `201` | The created review. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

