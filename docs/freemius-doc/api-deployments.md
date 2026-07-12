---
title: "Deployments API (6 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Deployments"
source: "api"
section: "API Reference"
category: "Deployments"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Deployments

Operations related to version deployments and retrieval.

## `GET /products/{product_id}/tags.json`

**List all deployments**

Get the product version collection. This is for WordPress products only.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `200` | The product version collection. |
| `400` |  |
| `401` |  |

## `POST /products/{product_id}/tags.json`

**Create a deployment**

Upload a new version of the product (for WordPress products only). The endpoint supports only the `multipart/form-data` content type and expects two payloads: `file` and `data`.

- `file` - The zip file containing the product. For WordPress plugins or themes this must contain the root directory.
- `data` - Please omit this when deploying WordPress plugins and themes. In case of deploying templates and widgets, this needs to be a **stringified JSON** and must have the `version` and `requires_platform_version` properties.

An example of the `data` property:

```
{"version": "2.0.0", "requires_platform_version": "1.0.0"}
```

> After you have created a deployment, please send another PUT request to the newly created version to update the `release_status` to either `released` or `beta`. The default value is `pending` which means none of the customers will be able to see the new version.

You can learn more about the deployment process [here](https://freemius.com/help/documentation/getting-started/deployment-process/).


### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | OK |
| `400` |  |

## `GET /products/{product_id}/tags/latest.json`

**Get latest deployment**

Get the information about the latest deployment the product has, including a secure download link. The download link will work without any authentication header and will expire in 24 hours.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_premium` | query |  | (Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only. |
| `type` | query |  | Type of the latest deployment to load. If the type provided is `all`, the latest `released`, `beta`, or `pending` version will be returned, whichever has the higher version. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The latest deployment information. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/tags/latest.zip`

**Download latest deployment**

Download the latest deployment the product has. This is for WordPress products only (including plugins, themes, templates and widgets). It outputs the zip file of the deployed version.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_premium` | query |  | (Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only. |
| `type` | query |  | Type of the latest deployment to load. If the type provided is `all`, the latest `released`, `beta`, or `pending` version will be returned, whichever has the higher version. |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The zip file of the deployed version. |
| `400` |  |
| `401` |  |
| `402` |  |

## `PUT /products/{product_id}/tags/{tag_id}.json`

**Update a deployment**

Update a specific deployed version of the product. This applies to WordPress products only. Use this endpoint to update the `release_mode` of a deployment to make it available to your customers.

### Release Modes

Defined by the `release_mode` property, with the following possible values:

- `pending` – The deployment is pending and not visible to customers. This is the default value.
- `beta` – The deployment is in beta mode. Only customers with beta access will see this version.
- `released` – The deployment is released and visible to all customers.

Additionally, WordPress plugins and themes support **incremental releases** and **staged rollouts**:

- [**Incremental Release**](help-documentation-release-management-incremental-update.md): Controlled via the `is_incremental` flag, incremental releases enforce sequential updates, requiring users to install designated intermediate versions before proceeding to newer ones.
- [**Staged Rollout**](help-documentation-release-management-staged-rollouts.md): Managed through the `limit` and `percentage_limit` flags, staged rollouts enable gradual deployment of updates to a subset of users, allowing for monitoring and issue resolution before full release.

> Note: Incremental Release and Staged Rollout are not supported for templates and widgets.


### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The updated deployment. |
| `400` |  |
| `401` |  |
| `402` |  |

## `GET /products/{product_id}/tags/{tag_id}.zip`

**Download a deployment**

Download a specific deployed version of the product. This is for WordPress products only (including plugins, themes, templates and widgets). It outputs the zip file of the deployed version.

> You can download both the premium and the free version of the deployment using the `is_premium` flag. This will help you setup automation to deploy Freemius generated free version to WordPress.org repository.


### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `is_premium` | query |  | (Optional) Whether to retrieve a premium version of the product or not. For WordPress products (plugins and themes) only. |

### Responses

| Status | Description |
|--------|-------------|
| `200` | The zip file of the deployed version. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

