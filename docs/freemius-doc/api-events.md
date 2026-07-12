---
title: "Events API (GET /products/{product_id}/events.json, GET /products/{product_id}/events/{event_id}.json)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons#tag/Events"
source: "api"
section: "API Reference"
category: "Events"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Events

Operations related to events of a store or product.

## `GET /products/{product_id}/events.json`

**List all events**

Retrieve a list of events for a specific product. Supports filtering by type, state, and pagination. See the [documentation](help-documentation-saas-events-webhooks.md#how_to_create_a_webhook) for instructions on creating a webhook to listen for events.

### Parameters

| Name | In | Required | Description |
|------|----|----------|-------------|
| `type` | query |  | Filter events by type string or event name, such as `license.created`. See the [documentation](help-documentation-saas-events-webhooks.md#event_types) for a list of available event types. |
| `state` | query |  | Filter events by state: 'pending', 'processed', 'error', or 'canceled'. |
| `` |  |  |  |
| `` |  |  |  |
| `` |  |  |  |

### Responses

| Status | Description |
|--------|-------------|
| `200` | A collection of events. |
| `400` |  |
| `401` |  |
| `402` |  |
| `404` |  |

## `GET /products/{product_id}/events/{event_id}.json`

**Retrieve an event**

Retrieve a specific event by its ID. For instructions on creating webhook listeners, see the [documentation](help-documentation-saas-events-webhooks.md#how_to_create_a_webhook).

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
| `200` | The retrieved event. |
| `400` |  |

