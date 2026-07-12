---
title: "Reviews API (6 endpoints)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Reviews"
source: "api"
section: "API Reference"
category: "Reviews"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Reviews

Operations related to reviews of a product.

## `GET /products/{product_id}/reviews.json`

**List all reviews**

Retrieve the reviews collection.

### Responses

| Status | Description |
|--------|-------------|
| `200` | The reviews collection. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `POST /products/{product_id}/reviews.json`

**Create a review**

Create a product review.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The retrieved review. |
| `400` |  |

## `GET /products/{product_id}/reviews/summary.json`

**Retrieve reviews summary**

Retrieve the summary of the reviews collection. Every item is an object with a `rate` and `count` properties, where `rate` is the rating value (0-100) and `count` is the number of reviews with that rating. Reviews are grouped by their rating.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `type` | query |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `404` |  |
| `200` | The summary of the review collection. |
| `400` |  |
| `401` |  |
| `402` |  |

## `DELETE /products/{product_id}/reviews/{review_id}.json`

**Delete a review**

Delete a product review by ID.

### Responses

| Status | Description |
|--------|-------------|
| `402` |  |
| `404` |  |
| `204` |  |
| `400` |  |
| `401` |  |

## `GET /products/{product_id}/reviews/{review_id}.json`

**Retrieve a review**

Retrieve a product review by ID.

### Responses

| Status | Description |
|--------|-------------|
| `401` |  |
| `402` |  |
| `404` |  |
| `200` | The retrieved review. |
| `400` |  |

## `PUT /products/{product_id}/reviews/{review_id}.json`

**Update a review**

Update a product review by ID
> The rate can only be modified for developer generated reviews.

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
| `200` | The updated review. |

