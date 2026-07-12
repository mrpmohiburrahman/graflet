---
title: "Installations API (29 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Installations"
source: "api"
section: "API Reference"
category: "Installations"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Installations

Operations related to the installation of a product.

## `GET /products/{product_id}/installs.json`

**List all installs**

Retrieve the install collection associated with the product.

Various filtering and search parameters are available to narrow down the results.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `ids` | query |  | Install IDs collection to filter. |
| `filter` | query |  | Install status to filter the installs by. |
| `version` | query |  | Plugin version to filter the installs by. |
| `license_id` | query |  | License ID to filter the installs by. |
| `plan_id` | query |  | Plan ID to filter the installs by. |
| `title` | query |  | Install title to filter the installs by. |
| `url` | query |  | Install URL to filter the installs by. |
| `search` | query |  | Search item to filter the installs by e.g. domain, site_id, or reason info. |
| `all` | query |  | If true, loads all installs, including the uninstalled ones. |
| `reason_id` | query |  | Reason ID (either string or numeric) to filter the installs by. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Installs collection |
| `400` |  |

## `GET /products/{product_id}/installs/count.json`

**Retrieve installs count**

Retrieve the number of installs associated with the product.

### Filtering

You can filter the count by `plan_id` or `is_active`.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `plan_id` | query |  | (optional) Return the count of installs that are associated with a non-expired license for the given plan ID. |
| `is_active` | query |  | (optional) Return active installs only. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The number of installs with the product. |

## `DELETE /products/{product_id}/installs/{install_id}.json`

**Delete an install**

Delete a product install. This is different from an uninstall.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `204` |  |
| `400` |  |

## `GET /products/{product_id}/installs/{install_id}.json`

**Retrieve an install**

Retrieve the details related to the product install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `404` |  |
| `200` | The install details. |
| `400` |  |

## `PUT /products/{product_id}/installs/{install_id}.json`

**Update an install**

Update the details related to the product install.

### Responses

| Status | Description |
|--------|-------------|
| `200` | Install updated |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/installs/{install_id}/addons/{addon_id}/plans/{plan_id}/features.json`

**List all plan's features for Addon**

Get plan's features collection for an addon on a site.

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
| `200` | The plan's features collection for Addon on an install. |
| `400` |  |
| `401` |  |
| `402` |  |

## `POST /products/{product_id}/installs/{install_id}/clones.json`

**Create a clone**

Create a clone of an install associated with the product.

> Use this endpoint if you want to support migration or temporary or long-term duplicates for staging purposes.

By default the clone will be created in a pending state. For our [WP SDK](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) the clone will be created in a safe mode state.

After creating the clone, you will need to resolve the clone by updating its state and resolution. You will need to handle the licensing logic for the new install entity. Our [WP SDK](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) handles it automatically for WordPress products (plugins and themes).

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Install clone created. |
| `400` |  |
| `401` |  |
| `404` |  |

## `PUT /products/{product_id}/installs/{install_id}/clones/{clone_id}.json`

**Resolve a clone**

Resolve a clone of an install that was created by the product.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Install clone created. |
| `400` |  |
| `401` |  |

## `PUT /products/{product_id}/installs/{install_id}/downgrade.json`

**Downgrade to the default plan**

Downgrade install's plan to product’s default plan. This is usually the free plan.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Product plan downgraded. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/installs/{install_id}/events.json`

**List all events**

Retrieve the event collection related to a product install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |
| `type` | query |  | Filter events by type string or event name. |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | Events triggered by the install. |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/installs/{install_id}/license.json`

**Retrieve an active license by UID**

Retrieve the full information about the active license for the specified install when the UID of the install is known.

> No Authorization header is required.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `license_key` | query | Yes | The license key used for the activation of the install. |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Successful operation |
| `400` |  |
| `402` |  |

## `GET /products/{product_id}/installs/{install_id}/licenses.json`

**List all active licenses**

Retrieve the active licenses (usually only one) on an install.

> Use this endpoint only when the ID of the license is unknown.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_enriched` | query |  | If `true`, the parent license's and plan's info will be included in the result if there's any. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Active license. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `DELETE /products/{product_id}/installs/{install_id}/licenses/{license_id}.json`

**Deactivate a license**

Deactivate license from an install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `license_key` | query | Yes | The same license key used to activate the install. |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Activated licence. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/installs/{install_id}/licenses/{license_id}.json`

**Retrieve an active license by ID**

Retrieve specific license of the install when the license ID and the license key are known but the UID of the install is not known.

> Retrieve the license information with product level authorization when the UID of the install is unknown.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `license_key` | query | Yes | The license key used on the install. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Install's licence |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/installs/{install_id}/licenses/{license_id}.json`

**Activate a license**

Activate license for an install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `license_key` | query | Yes | The license key received from the checkout. |
| `is_enriched` | query |  | If `true`, the parent license's and plan's info will be included in the result if there's any. |

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Activated licence. |
| `400` |  |

## `GET /products/{product_id}/installs/{install_id}/market_items.json`

**List all market items**

Retrieves all market items associated with an `Install` entity.

> Market items are other products (not necessarily powered by Freemius) that are installed in the same site as the Freemius powered product.

> It is only after the user chooses to opt-in that such data is collected and sent to Freemius. Right now we only support WordPress products i.e. plugins and themes.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `404` |  |
| `200` | All market items associated with the install. |

## `GET /products/{product_id}/installs/{install_id}/payments.json`

**List all payments**

Retrieve the payment associated with the install.

> This lists all payments collected from the license activated on this install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `extended` | query |  | If `true`, loads linked user email, install URL, subscription billing cycle and plan name. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Payments collection |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/installs/{install_id}/permissions.json`

**Update permissions**

Update permissions to a product install.

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Install permission updated. |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/installs/{install_id}/plans.json`

**List all plans**

Retrieve all the available product plans to which an install can subscribe.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `show_pending` | query |  | Show all plans whether released to customers or hidden. |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | Install Plans |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/installs/{install_id}/plans/{plan_id}.json`

**Retrieve a plan**

Retrieve the product plan details to which the install is subscribed.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Install Plan |
| `400` |  |
| `401` |  |
| `402` |  |

## `POST /products/{product_id}/installs/{install_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json`

**Create a new license**

Create a new license and assign it to the install.

> Either `period` or `expires_at` must be set.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | License created successfully. |
| `400` |  |
| `401` |  |
| `402` |  |

## `POST /products/{product_id}/installs/{install_id}/plans/{plan_id}/trials.json`

**Start a trial**

Start the trial of a plan for which an install is subscribed. The install must not have utilized the trial before.

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
| `200` | Started Trial |
| `400` |  |

## `DELETE /products/{product_id}/installs/{install_id}/trials.json`

**Cancel a trial**

Cancel a trial associated with a specific install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `reason_ids` | query |  | Optional cancellation reason IDs. |
| `reason` | query |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The install with cancelled trial. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/installs/{install_id}/uninstall.json`

**Retrieve uninstall details**

Retrieve the details of an install where the product has been uninstalled.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The uninstall details. |
| `400` |  |
| `401` |  |
| `404` |  |

## `GET /products/{product_id}/installs/{install_id}/updates.json`

**List all updates**

Retrieve the product update collection available for an install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `version` | query | Yes | The product's version of the current install. The endpoint will return newer versions when set. This is a required param unless `older_than` is provided. |
| `older_than` | query |  | If provided, only versions that are older than this will be returned. |
| `type` | query |  | The product type. If the type provide is `all`, the latest `released` or `pending` version will be returned, whichever has the higher version. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | Updates collection. |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/installs/{install_id}/updates/latest.json`

**Retrieve the latest update**

Retrieve the latest product update available for an install.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_premium` | query |  | If set, tries to fetch the requested version. If requires premium but no license, will throw an error. Otherwise, fetch version based on license. |
| `readme` | query |  | If set, tries to fetch the readme information. |
| `newer_than` | query |  | If set, return the latest version's data only if it's newer than this property's value. |
| `type` | query |  | The product type. If the type provided is `all`, the latest `released`, `beta`,  or `pending` version will be returned, whichever has the higher version. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | Updates collection. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `PUT /products/{product_id}/installs/{install_id}/users/{user_id}/ownership-change.json`

**Change ownership**

Change ownership of an install.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Install ownership changed successfully. No response will be sent, but it will be redirected to the `after_confirm_url` if it was used when initiating the ownership transfer. |
| `400` |  |

## `PUT /products/{product_id}/installs/{install_id}/users/{user_id}/verify.json`

**Send a verification email**

Sends an email to the user associated with the install, containing a link to verify the email address.

> With the `after_email_confirm_url` parameter, you can specify a URL address that the user will be auto forwarded to after email confirmation is clicked.

### Responses

| Status | Description |
|--------|-------------|
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | Successful operation. |

## `PUT /products/{product_id}/uninstall.json`

**Uninstall from anonymous site**

Uninstall a product from anonymous site

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | The product is uninstalled. |
| `400` |  |
| `401` |  |

