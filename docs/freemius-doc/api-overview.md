---
title: "Freemius API — Overview (140 endpoints, 15 tags)"
url: "https://freemius.com/help/documentation/openapi.yaml#tag/Coupons"
source: "api"
section: "API Reference"
scraped_at: "2026-04-09T19:58:51+06:00"
---

# Freemius API


Welcome to the Freemius API Documentation!

You can use our API to access Freemius API endpoints, which can get information on various aspects of Freemius.

- Manage products.
- Manage license verifications.
- Create custom integration with your SaaS.

If you're using Freemius for a WordPress product, please check out our official [SDK](https://github.com/Freemius/wordpress-sdk).

## Bearer Token Auth

Freemius API supports Bearer Token authentication for product-specific operations.

To retrieve your API token:

1. Go to the [Freemius Developer Dashboard](https://dashboard.freemius.com).
2. Open the **Settings** page of the relevant product.
3. Click on the **API Token** tab.
4. Copy the **API Bearer Authorization Token** from the UI.

Use this token by including it in the `Authorization` header of your API requests:

```http
Authorization: Bearer {api_token}
```

Bearer tokens are **scoped to a specific product**. This means they can only be used with endpoints under the `/products/{product_id}/` namespace. For example:

```http
GET /products/12345/users.json
Authorization Bearer {api_token}
```

Requests to endpoints outside the product scope will result in an authorization error.

## Other Scopes and Authentication

The Freemius API is organized around different **scopes**, based on the top-level entity of the operation:

For example, let's say you want to list all payments of a product. This operation can be done in several scopes:

- **Product Scope**: `/products/{product_id}/payments.json`.
- **Developer Scope**: `/developers/{developer_id}/products/{product_id}/payments.json`.

On the other hand, if a user would want to list their payment, then endpoint will be scoped to the user:

- **User Scope**: `/users/{user_id}/payments.json`.

Some operations can be done from a particular scope only. For example only a developer can update a plan of a product or create a new plan. So the following operations will work:

- **Update Plan**: POST `/developers/{developer_id}/products/{product_id}/plans/{plan_id}.json`
- **Create Plan**: POST `/developers/{developer_id}/products/{product_id}/plans.json`

If you try to perform the same operation on a product scope, it will return an error. The scopes provides a way to control access and permissions for different entities in the Freemius ecosystem.

Currently, **Bearer Token authentication is supported for product scope only**. If you need access to endpoints in others scopes, use the secret-key based authentication with the following SDKs:

- [PHP SDK]( https://github.com/Freemius/freemius-php-sdk)
- [NodeJS SDK](https://github.com/Freemius/freemius-node-sdk)

For most use cases, managing your products, licenses, and customers through the [Developer Dashboard](https://dashboard.freemius.com) or [Customer Portal](https://customers.freemius.com) provides all the necessary capabilities.


Version: 1.0

## API Sections

- **Products** — All operations which can be done on a product.
- **Developers** — All operations which can be done from on a developer.
- **Subscriptions** — All operations associated to a subscription.
- **Users** — All operations which can be done on a user belonging to a store or a product.
- **Licenses** — All operations which can be done on a license belonging to a store or a product.
- **Coupons** — All operations which can be done on a coupon belonging to a store or a product.
- **Carts** — All operations which can be done on a cart belonging to a store or a product.
- **Payments** — All operations associated to a payment.
- **Installations** — Operations related to the installation of a product.
- **Trials** — Operations related to a trial license of a product.
- **Addons** — Operations related to an addon of a product.
- **Plans** — Operations related to plans, pricings and features of a product.
- **Events** — Operations related to events of a store or product.
- **Reviews** — Operations related to reviews of a product.
- **Deployments** — Operations related to version deployments and retrieval.

## Endpoints Summary

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/developer/{developer_id}/products/{product_id}/installs/{install_id}/members.json` | Add team member |
| `GET` | `/developers/{developer_id}/bank_account/{bank_account_id}.json` | Retrieve bank account |
| `POST` | `/developers/{developer_id}/login.json` | Log in |
| `PUT` | `/developers/{developer_id}/products/{product_id}/emails/addresses.json` | Update email addressses |
| `POST` | `/developers/{developer_id}/products/{product_id}/licenses/{license_id}/installs/sync.json` | Sync all activations |
| `POST` | `/developers/{developer_id}/products/{product_id}/plans.json` | Create a plan |
| `DELETE` | `/developers/{developer_id}/products/{product_id}/plans/{plan_id}.json` | Delete a plan |
| `PUT` | `/developers/{developer_id}/products/{product_id}/plans/{plan_id}.json` | Update a plan |
| `POST` | `/developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing.json` | Create a pricing |
| `DELETE` | `/developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json` | Delete a plan's pricing |
| `PUT` | `/developers/{developer_id}/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json` | Update a pricing |
| `GET` | `/products/{product_id}.json` | Retrieve a product |
| `PUT` | `/products/{product_id}.json` | Update a product |
| `GET` | `/products/{product_id}/addons.json` | List all addons |
| `GET` | `/products/{product_id}/addons/{addon_id}/plans.json` | List all plans |
| `GET` | `/products/{product_id}/addons/{addon_id}/plans/{plan_id}/features.json` | List all plan's features |
| `GET` | `/products/{product_id}/addons/{addon_id}/plans/{plan_id}/pricing.json` | List all pricings |
| `GET` | `/products/{product_id}/carts.json` | List all carts |
| `DELETE` | `/products/{product_id}/carts/{cart_id}.json` | Delete a cart |
| `GET` | `/products/{product_id}/carts/{cart_id}.json` | Retrieve a cart |
| `PUT` | `/products/{product_id}/carts/{cart_id}.json` | Update a cart |
| `GET` | `/products/{product_id}/carts/{cart_id}/events.json` | Retrieve cart events |
| `GET` | `/products/{product_id}/coupons.json` | List all coupons |
| `POST` | `/products/{product_id}/coupons.json` | Create a coupon |
| `GET` | `/products/{product_id}/coupons/special.json` | Retrieve special coupons |
| `DELETE` | `/products/{product_id}/coupons/{coupon_id}.json` | Delete a coupon |
| `GET` | `/products/{product_id}/coupons/{coupon_id}.json` | Retrieve a coupon |
| `PUT` | `/products/{product_id}/coupons/{coupon_id}.json` | Update a coupon |
| `DELETE` | `/products/{product_id}/coupons/{coupon_id}/note.json` | Delete a note |
| `GET` | `/products/{product_id}/coupons/{coupon_id}/note.json` | Retrieve a note |
| `POST` | `/products/{product_id}/coupons/{coupon_id}/note.json` | Create a note |
| `PUT` | `/products/{product_id}/coupons/{coupon_id}/note.json` | Update a note |
| `DELETE` | `/products/{product_id}/coupons/{coupon_id}/special/{special_id}.json` | Delete a special coupon |
| `PUT` | `/products/{product_id}/coupons/{coupon_id}/special/{special_id}.json` | Create a special coupon |
| `DELETE` | `/products/{product_id}/emails/addresses.json` | Delete all email addresses |
| `GET` | `/products/{product_id}/emails/addresses.json` | List all email addresses |
| `GET` | `/products/{product_id}/events.json` | List all events |
| `GET` | `/products/{product_id}/events/{event_id}.json` | Retrieve an event |
| `GET` | `/products/{product_id}/features.json` | List all features |
| `DELETE` | `/products/{product_id}/features/{feature_id}.json` | Delete a feature |
| `GET` | `/products/{product_id}/features/{feature_id}.json` | Retrieve a feature |
| `PUT` | `/products/{product_id}/features/{feature_id}.json` | Update a feature |
| `GET` | `/products/{product_id}/info.json` | Get product info |
| `GET` | `/products/{product_id}/installs.json` | List all installs |
| `GET` | `/products/{product_id}/installs/count.json` | Retrieve installs count |
| `DELETE` | `/products/{product_id}/installs/{install_id}.json` | Delete an install |
| `GET` | `/products/{product_id}/installs/{install_id}.json` | Retrieve an install |
| `PUT` | `/products/{product_id}/installs/{install_id}.json` | Update an install |
| `GET` | `/products/{product_id}/installs/{install_id}/addons/{addon_id}/plans/{plan_id}/features.json` | List all plan's features for Addon |
| `POST` | `/products/{product_id}/installs/{install_id}/clones.json` | Create a clone |
| `PUT` | `/products/{product_id}/installs/{install_id}/clones/{clone_id}.json` | Resolve a clone |
| `PUT` | `/products/{product_id}/installs/{install_id}/downgrade.json` | Downgrade to the default plan |
| `GET` | `/products/{product_id}/installs/{install_id}/events.json` | List all events |
| `GET` | `/products/{product_id}/installs/{install_id}/license.json` | Retrieve an active license by UID |
| `GET` | `/products/{product_id}/installs/{install_id}/licenses.json` | List all active licenses |
| `DELETE` | `/products/{product_id}/installs/{install_id}/licenses/{license_id}.json` | Deactivate a license |
| `GET` | `/products/{product_id}/installs/{install_id}/licenses/{license_id}.json` | Retrieve an active license by ID |
| `PUT` | `/products/{product_id}/installs/{install_id}/licenses/{license_id}.json` | Activate a license |
| `GET` | `/products/{product_id}/installs/{install_id}/licenses/{license_id}/subscriptions.json` | List all subscriptions |
| `GET` | `/products/{product_id}/installs/{install_id}/market_items.json` | List all market items |
| `GET` | `/products/{product_id}/installs/{install_id}/payments.json` | List all payments |
| `PUT` | `/products/{product_id}/installs/{install_id}/permissions.json` | Update permissions |
| `GET` | `/products/{product_id}/installs/{install_id}/plans.json` | List all plans |
| `GET` | `/products/{product_id}/installs/{install_id}/plans/{plan_id}.json` | Retrieve a plan |
| `POST` | `/products/{product_id}/installs/{install_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json` | Create a new license |
| `POST` | `/products/{product_id}/installs/{install_id}/plans/{plan_id}/trials.json` | Start a trial |
| `DELETE` | `/products/{product_id}/installs/{install_id}/trials.json` | Cancel a trial |
| `GET` | `/products/{product_id}/installs/{install_id}/uninstall.json` | Retrieve uninstall details |
| `GET` | `/products/{product_id}/installs/{install_id}/updates.json` | List all updates |
| `GET` | `/products/{product_id}/installs/{install_id}/updates/latest.json` | Retrieve the latest update |
| `PUT` | `/products/{product_id}/installs/{install_id}/users/{user_id}/ownership-change.json` | Change ownership |
| `PUT` | `/products/{product_id}/installs/{install_id}/users/{user_id}/verify.json` | Send a verification email |
| `GET` | `/products/{product_id}/is_active.json` | Check product status |
| `GET` | `/products/{product_id}/licenses.json` | List all licenses |
| `PUT` | `/products/{product_id}/licenses.json` | Assign a license |
| `POST` | `/products/{product_id}/licenses/activate.json` | Activate a license |
| `POST` | `/products/{product_id}/licenses/deactivate.json` | Deactivate a license |
| `POST` | `/products/{product_id}/licenses/resend.json` | Resend license keys |
| `DELETE` | `/products/{product_id}/licenses/{license_id}.json` | Cancel a license |
| `GET` | `/products/{product_id}/licenses/{license_id}.json` | Retrieve a license |
| `PUT` | `/products/{product_id}/licenses/{license_id}.json` | Update a license |
| `POST` | `/products/{product_id}/licenses/{license_id}/checkout/link.json` | Generate upgrade link |
| `DELETE` | `/products/{product_id}/licenses/{license_id}/installs.json` | Deactivate installs |
| `POST` | `/products/{product_id}/licenses/{license_id}/renewals.json` | Send the renewal email |
| `POST` | `/products/{product_id}/licenses/{license_id}/resend.json` | Resend the upgrade email |
| `DELETE` | `/products/{product_id}/licenses/{license_id}/subscription.json` | Cancel current subscription |
| `GET` | `/products/{product_id}/licenses/{license_id}/subscription.json` | Retrieve latest subscription |
| `GET` | `/products/{product_id}/payments.json` | List all payments |
| `GET` | `/products/{product_id}/payments/{payment_id}.json` | Retrieve a payment |
| `GET` | `/products/{product_id}/payments/{payment_id}/invoice.pdf` | Download invoice |
| `GET` | `/products/{product_id}/ping.json` | GDPR compliance check |
| `GET` | `/products/{product_id}/plans.json` | List all plans |
| `GET` | `/products/{product_id}/plans/currencies.json` | List all currencies |
| `GET` | `/products/{product_id}/plans/{plan_id}.json` | Retrieve a plan |
| `GET` | `/products/{product_id}/plans/{plan_id}/features.json` | List all features |
| `GET` | `/products/{product_id}/plans/{plan_id}/pricing.json` | List all plan's pricing |
| `POST` | `/products/{product_id}/plans/{plan_id}/pricing/clone.json` | Clone pricing to other currency |
| `GET` | `/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}.json` | Retrieve a pricing |
| `POST` | `/products/{product_id}/plans/{plan_id}/pricing/{pricing_id}/licenses.json` | Create a license |
| `POST` | `/products/{product_id}/portal/login.json` | Generate portal login link |
| `GET` | `/products/{product_id}/pricing.json` | Retrieve the pricing table data |
| `GET` | `/products/{product_id}/reviews.json` | List all reviews |
| `POST` | `/products/{product_id}/reviews.json` | Create a review |
| `GET` | `/products/{product_id}/reviews/summary.json` | Retrieve reviews summary |
| `DELETE` | `/products/{product_id}/reviews/{review_id}.json` | Delete a review |
| `GET` | `/products/{product_id}/reviews/{review_id}.json` | Retrieve a review |
| `PUT` | `/products/{product_id}/reviews/{review_id}.json` | Update a review |
| `DELETE` | `/products/{product_id}/settings/{setting_id}.json` | Delete a setting |
| `GET` | `/products/{product_id}/settings/{setting_id}.json` | Retrieve a setting |
| `PUT` | `/products/{product_id}/settings/{setting_id}.json` | Update a setting |
| `PUT` | `/products/{product_id}/skip.json` | Skip account connection |
| `GET` | `/products/{product_id}/subscriptions.json` | List all subscriptions |
| `DELETE` | `/products/{product_id}/subscriptions/{subscription_id}.json` | Cancel a subscription |
| `GET` | `/products/{product_id}/subscriptions/{subscription_id}.json` | Retrieve a subscription |
| `PUT` | `/products/{product_id}/subscriptions/{subscription_id}.json` | Update a subscription |
| `GET` | `/products/{product_id}/subscriptions/{subscription_id}/payments.json` | List all payments |
| `POST` | `/products/{product_id}/subscriptions/{subscription_id}/payments.json` | Create a new migrated payment |
| `GET` | `/products/{product_id}/tags.json` | List all deployments |
| `POST` | `/products/{product_id}/tags.json` | Create a deployment |
| `GET` | `/products/{product_id}/tags/latest.json` | Get latest deployment |
| `GET` | `/products/{product_id}/tags/latest.zip` | Download latest deployment |
| `PUT` | `/products/{product_id}/tags/{tag_id}.json` | Update a deployment |
| `GET` | `/products/{product_id}/tags/{tag_id}.zip` | Download a deployment |
| `GET` | `/products/{product_id}/trials.json` | List all trials |
| `PUT` | `/products/{product_id}/uninstall.json` | Uninstall from anonymous site |
| `GET` | `/products/{product_id}/users.json` | List all users |
| `POST` | `/products/{product_id}/users.json` | Create a user |
| `GET` | `/products/{product_id}/users/{user_id}.json` | Retrieve a user |
| `PUT` | `/products/{product_id}/users/{user_id}.json` | Update a user |
| `GET` | `/products/{product_id}/users/{user_id}/billing.json` | Retrieve billing |
| `PUT` | `/products/{product_id}/users/{user_id}/billing.json` | Update or create billing |
| `GET` | `/products/{product_id}/users/{user_id}/events.json` | List all events |
| `GET` | `/products/{product_id}/users/{user_id}/installs.json` | List all installs |
| `GET` | `/products/{product_id}/users/{user_id}/licenses.json` | List all licenses |
| `GET` | `/products/{product_id}/users/{user_id}/licenses/{license_id}/review_url.json` | Get review URL |
| `POST` | `/products/{product_id}/users/{user_id}/licenses/{license_id}/reviews.json` | Create a review |
| `GET` | `/products/{product_id}/users/{user_id}/payments.json` | List all payments |
| `GET` | `/products/{product_id}/users/{user_id}/payments/{payment_id}/invoice.pdf` | Download invoice |
| `GET` | `/products/{product_id}/users/{user_id}/subscriptions.json` | List all subscriptions |
| `POST` | `/products/{product_id}/users/{user_id}/tokens/checkout.json` | Create a checkout token |

