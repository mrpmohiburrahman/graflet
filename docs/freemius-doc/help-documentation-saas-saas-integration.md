---
title: "Integrating Freemius into Your SaaS Application"
url: "https://freemius.com/help/documentation/saas/saas-integration/"
source: "docs"
section: "Docs"
category: "Setup for SaaS & Apps"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 2324
---

This guide will walk you through the essential steps to integrate Freemius into your SaaS application. It covers everything from setting up the checkout process to managing user licenses and subscriptions, setting up webhooks for real-time updates, and providing a customer portal for your users.

**Are you building a SaaS application using Next.js?** You can **skip this** and check out our [Next.js SaaS Starter Guide](help-documentation-saas-sdk-framework-nextjs.md) for a complete walkthrough and starter repository on integrating with Freemius.

You can also check our [JavaScript SDK](help-documentation-saas-sdk-js-sdk.md) or [Framework Integration Guide](help-documentation-saas-sdk-framework.md) for **other popular frameworks**. Read on to learn the core concepts that apply to any technology stack!

## Initial Steps[​](#initial-steps "Direct link to Initial Steps")

1. [Sign-up to Freemius](https://dashboard.freemius.com/register/)
2. Create a new SaaS product
3. Go to the Plans and [configure the plans and prices](help-documentation-saas-saas-plans-pricing.md)
4. Optionally customize the [unit label](help-documentation-saas-customize-license-unit-label.md)

## Checkout Integration[​](#checkout-integration "Direct link to Checkout Integration")

You can integrate the Checkout as a [modal dialog triggered using JavaScript](help-documentation-checkout-integration-freemius-checkout-buy-button.md), or by using [direct checkout links](help-documentation-checkout-integration-hosted-checkout.md).

Regardless of the method you choose, ensure that you set [`user_email`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#user_email) to the logged-in user’s email. To enforce the purchase is made with the same customer email as in your system, you can direct the checkout to set the email input as read-only by setting [`readonly_user`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#readonly_user) to `true`.

Here’s an example of a direct checkout link:

```text
https://checkout.freemius.com/product/{product_id}/plan/{plan_id}/?user_email={email}&readonly_user=true
```

When `readonly_user` is set in a direct link, the checkout will auto redirect to

```text
https://checkout.freemius.com/product/{product_id}/plan/{plan_id}/
```

to ensure the user can’t easily tinker with the email address.

If you’re using the hosted Checkout, we recommend setting up a [redirection URL](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase) so your app can immediately process the purchase information.

If you're using the modal integration, use the [`success`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#success) or [`purchaseCompleted`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#purchaseCompleted) callback handler to receive the purchase data.

note

Please be sure to [URL encode](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding) the email address and other parameters when constructing the URL. Here is an example:

- JavaScript
- PHP

```javascript
function generateCheckoutLink(productId, planId, email, otherParams = {}) {
  const baseUrl = `https://checkout.freemius.com/product/${productId}/plan/${planId}/`;
  const params = new URLSearchParams({
    user_email: email,
    readonly_user: 'true',
    ...otherParams,
  });

  return `${baseUrl}?${params.toString()}`;
}
```

```php
function generateCheckoutLink($productId, $planId, $email, $otherParams = []) {
  $baseUrl = "https://checkout.freemius.com/product/{$productId}/plan/{$planId}/";
  $params = array_merge([
    'user_email' => $email,
    'readonly_user' => 'true',
  ], $otherParams);

  $queryString = http_build_query($params);

  return "{$baseUrl}?{$queryString}";
}
```

## Restricting or Relaxing Single Subscription Per User[​](#restricting-or-relaxing-single-subscription-per-user "Direct link to Restricting or Relaxing Single Subscription Per User")

Please note that by default, for SaaS products, users can have only one active subscription at a time. You can relax this limitation if needed by going to **Settings** and disabling the **Restrict Single Subscription Per User** toggle.

To learn how to facilitate upgrades, please [continue reading](#handling-license-or-subscription-upgrades).

tip

If you don't envision supporting multiple subscriptions per user, we recommend keeping the restriction enabled. This approach simplifies your integration, provides better experience to your customers, and reduces potential support requests and disputes. Find our [case study](blog-freemius-release-notes-april-2025.md#block_duplicate_subscriptions_with_a_simple_toggle).

## Database Updates[​](#database-updates "Direct link to Database Updates")

Your database likely have a `user` table with the following columns:

- `id`
- `email`
- …

To store the entitlement mapping between your users and Freemius, we recommend creating a new `user_fs_entitlement` table in your database with the following columns:

- `id` - The primary key.
- `user_id` - A foreign key referencing your `user` table.
- `fs_license_id` - A unique identifier for the Freemius license (text/string).
- `fs_plan_id` - The Freemius plan ID (text/string).
- `fs_pricing_id` - The Freemius pricing ID (text/string).
- `fs_user_id` - The Freemius user ID (text/string).
- `type` - The entitlement type (e.g., `subscription`, `lifetime`, etc.).
- `expiration` - The license expiration timestamp (nullable).
- `is_canceled` - A boolean flag indicating if the license is canceled.
- `created_at` - Timestamp when the record was created.

This table will hold the mapping between your user entities and their corresponding Freemius licenses, plans, and entitlements.

With Freemius, a user’s `License` is what governs their account level, providing you with significant flexibility. This setup allows you to maintain feature access even if a subscription is canceled mid-term, or restrict access even if a subscription remains active. To effectively manage user account levels, ensure that your webhook is configured to handle license-related events (a webhook implementation can be found [below](#creating-a-webhook-listener)).

If you prefer not to store canceled or deleted licenses, you can remove the `is_canceled` column and instead add a `license_id` column to the `user` table, establishing a 1:1 relationship. For the purposes of this example, however, we'll assume that you want to preserve the entire license history.

## Saving Purchase Information[​](#saving-purchase-information "Direct link to Saving Purchase Information")

When a user completes a purchase, you will receive the purchase data either through the [redirection URL](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase) (hosted Checkout) or the [callback function](help-documentation-checkout-integration-freemius-checkout-buy-button.md#success) (modal Checkout). You should then save the relevant information in your `user_fs_entitlement` table.

Our recommendation is to capture the `license_id` from the purchase data, [query the Freemius API](https://docs.freemius.com/api/licenses/retrieve) to retrieve the complete license details, and then store the necessary fields in your database. Here is an example of how to achieve this:

- JavaScript
- PHP

```typescript
const licenseId = request.query.license_id as string; // Or retrieve it from the modal callback data

// @see https://docs.freemius.com/api/licenses/retrieve
const license = await getLicenseFromFreemiusApi(licenseId);
// @see https://docs.freemius.com/api/users/retrieve
const user = await getUserFromFreemiusApi(license.user_id);

const localUserId = getLocalUserIdByEmail(user.email);

await storeOrUpdateUserFsEntitlement({
  user_id: localUserId,
  fs_license_id: license.id,
  fs_plan_id: license.plan_id,
  fs_pricing_id: license.pricing_id,
  fs_user_id: license.user_id,
  type: license.type,
  expiration: license.expiration,
  is_canceled: license.is_canceled,
});
```

```php
$license_id = $_GET['license_id']; // Or retrieve it from the modal callback data

// @see https://docs.freemius.com/api/licenses/retrieve
$license = getLicenseFromFreemiusApi($license_id);
// @see https://docs.freemius.com/api/users/retrieve
$user = getUserFromFreemiusApi($license->user_id);

$local_user_id = getLocalUserIdByEmail($user->email);

storeOrUpdateUserFsEntitlement([
  'user_id'       => $local_user_id,
  'fs_license_id' => $license->id,
  'fs_plan_id'    => $license->plan_id,
  'fs_pricing_id' => $license->pricing_id,
  'fs_user_id'    => $license->user_id,
  'type'          => $license->type,
  'expiration'    => $license->expiration,
  'is_canceled'   => $license->is_canceled,
]);
```

Another and more reliable way to capture this information is by setting up a webhook listener (see [below](#creating-a-webhook-listener)). This method ensures that you receive all purchase events, even if the user does not complete the redirection process after checkout.

## Checking User’s Plan[​](#checking-users-plan "Direct link to Checking User’s Plan")

To determine the account level of a logged-in user, search for an active/non-canceled license associated with the user. Ensure the license has not expired (via `expiration`) to confirm the user is on the right plan and pricing indicated by `user_fs_entitlement.fs_plan_id` or `user_fs_entitlement.fs_pricing_id`. We recommend using the `pricing_id` for more granular control, especially if you have multiple quotas for the same plan.

- JavaScript
- PHP

```javascript
function getUserPlanId(userId) {
  const license = loadLicense({
    userId: userId,
    isCanceled: false,
  });

  if (!license) {
    return null;
  }

  // In case you want to support a concept of non-expiring licenses, you can set their expiration to `null`.
  if (license.expiration === null) {
    return true;
  }

  const expiration = new Date(license.expiration);
  const now = new Date();

  return now < expiration ? license.fs_plan_id : null;
}
```

```php
function getUserPlanId($userId)
{
  $license = loadLicense([
    "user_id" => $userId,
    "is_canceled" => false,
  ]);

  if (!is_object($license)) {
    return null;
  }

  // In case you want to support a concept of non-expiring licenses, you can set their expiration to `null`.
  if (is_null($license->expiration)) {
    return true;
  }

  $expiration = new DateTime($license->expiration);
  $now = new DateTime("now");

  return $now < $expiration ? $license->fs_plan_id : null;
}
```

**How to Get the Plan ID or Pricing ID?**

To get the plan ID, simply navigate to the **Plan** page under your SaaS product in the [Freemius Developer Dashboard](https://dashboard.freemius.com/).

The ID of the plan is displayed next to the plan name.

To get the pricing ID, click on the specific plan to view its details. The pricing ID is listed next to each pricing option within the plan.

note

Freemius includes a built-in [dunning mechanism](help-documentation-marketing-automation-dunning-failed-payments.md). If a subscription renewal fails, the system will automatically attempt to process the payment through a series of emails sent over several days following the original renewal date. The subscription will remain active during this period, even though the license may expire, until the recovery process is complete or the subscription is eventually canceled.

## Handling License or Subscription Upgrades[​](#handling-license-or-subscription-upgrades "Direct link to Handling License or Subscription Upgrades")

Freemius allows your users to upgrade the plan or license quota of their subscription. The upgrade process goes through our Checkout again, which collects up-to-date information from the user. After a successful purchase, the license object will be updated with the new information.

The flow involves:

1. Sending an API request from your app with the `license_id` to generate the upgrade Checkout URL.
2. Passing the URL to your user or triggering the modal Checkout (depending on your integration).
3. Synchronizing your SaaS with the up-to-date information.

Below is the API endpoint and an example of how to call it:

```http
POST /v1/products/{product_id}/licenses/{license_id}/checkout/link.json HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: Bearer 123
Host: api.freemius.com
Content-Length: 127

{
  "plan_id": "planID",
  "billing_cycle": "annual",
  "quota": 1,
  "currency": "usd"
}
```

The API will return an object with three properties:

- `url` - The upgrade link of the hosted checkout that you can share.
- `settings` - Configuration parameter that you can use with the modal Checkout.
- `expires` - Expiration date of the link.

You will need to use a [Bearer Token](https://docs.freemius.com/api/section/bearer-token-auth) to authenticate the request from your backend. More information about our REST API is available [here](https://docs.freemius.com/api/).

Once the upgrade is complete, depending on your integration, the Checkout will either redirect to the success URL on your SaaS website or pass the data through the modal integration. From there, you can update your own system to reflect the changes in real time.

## Creating a Webhook Listener[​](#creating-a-webhook-listener "Direct link to Creating a Webhook Listener")

We strongly recommend setting up [webhooks](help-documentation-saas-events-webhooks.md) to ensure your backend reliably receives upgrade and license change notifications, even if the user's browser fails to complete the redirect or if network interruptions occur during the Checkout process.

- JavaScript
- PHP

```javascript
// Example Express-style handler (ensure raw body is available!)
// For Express, configure a raw body parser middleware to set req.rawBody.
const crypto = require('crypto');

function handleFreemiusWebhook(req, res) {
  const body = (req.rawBody || '').toString('utf8');
  const hash = crypto
    .createHmac('sha256', '<PRODUCT_SECRET_KEY>')
    .update(body)
    .digest('hex');
  const signature = req.headers['x-signature'] || '';

  if (hash !== signature) {
    // Invalid signature, don't expose any data to attackers.
    return res.status(200).end();
  }

  const fs_event = JSON.parse(body);

  function loadUser(fsUser) {
    // Query your local database to find the user ID by email.
    const localUser = findUserByEmail(fsUser.email);

    if (localUser) return localUser;

    // You can choose to create the user here if they don't exist.
    return registerUser(fsUser.email, fsUser.first, fsUser.last);
  }

  function loadLicense(fsLicense) {
    // Query your local database to find the license by fs_license_id.
    return loadUserFsEntitlement(fsLicense.id);
  }

  function createUserLicense(fsUser, fsLicense) {
    const localUser = loadUser(fsUser);

    // Insert or update the user's entitlement in your local database.
    storeOrUpdateUserFsEntitlement({
      user_id: localUser.id,
      fs_license_id: fsLicense.id,
      fs_plan_id: fsLicense.plan_id,
      fs_pricing_id: fsLicense.pricing_id,
      fs_user_id: fsLicense.user_id,
      type: fsLicense.type,
      expiration: fsLicense.expiration,
      is_canceled: fsLicense.is_canceled,
    });
  }

  function updateUserLicense(fsUser, fsLicense) {
    let license = loadLicense(fsLicense);

    if (!license) {
      // Likely the 'license.created' event failed processing.
      createUserLicense(fsUser, fsLicense);
    } else {
      license.plan_id = fsLicense.plan_id;
      license.pricing_id = fsLicense.pricing_id;
      license.expiration = fsLicense.expiration;
      license.is_canceled = fsLicense.is_canceled;
      license.update();
    }

    // You can also notify the user of the plan change or grant additional entitlements.
    return license;
  }

  switch (fs_event.type) {
    case 'license.created':
      createUserLicense(fs_event.objects.user, fs_event.objects.license);
      break;

    case 'license.extended':
    case 'license.shortened':
    case 'license.updated':
    case 'license.cancelled':
    case 'license.expired':
    case 'license.plan.changed':
      updateUserLicense(fs_event.objects.user, fs_event.objects.license);
      break;
  }

  return res.status(200).end();
}
```

```php
<?php
// Retrieve the request's body payload.
$input = @file_get_contents("php://input");
$hash = hash_hmac("sha256", $input, "<PRODUCT_SECRET_KEY>");
$signature = $_SERVER["HTTP_X_SIGNATURE"] ?? "";

if (!hash_equals($hash, $signature)) {
  // Invalid signature, don't expose any data to attackers.
  http_response_code(200);
  exit();
}

$fs_event = json_decode($input);

function loadUser($fsUser)
{
  // Query your local database to find the user ID by email.
  $local_user = findUserByEmail($fsUser->email);

  if ($local_user) {
    return $local_user;
  }

  // You can choose to create the user here if they don't exist.
  return registerUser($fsUser->email, $fsUser->first, $fsUser->last);
}

function loadLicense($fsLicense)
{
  // Query your local database to find the license by fs_license_id.
  return loadUserFsEntitlement($fsLicense->id);
}

function createUserLicense($fsUser, $fsLicense)
{
  $local_user = loadUser($fsUser);

  // Insert or update the user's entitlement in your local database.
  storeOrUpdateUserFsEntitlement([
    "user_id" => $local_user->id,
    "fs_license_id" => $fsLicense->id,
    "fs_plan_id" => $fsLicense->plan_id,
    "fs_pricing_id" => $fsLicense->pricing_id,
    "fs_user_id" => $fsLicense->user_id,
    "type" => $fsLicense->type,
    "expiration" => $fsLicense->expiration,
    "is_canceled" => $fsLicense->is_canceled,
  ]);
}

function updateUserLicense($fsUser, $fsLicense)
{
  $license = loadLicense($fsLicense);

  if (!is_object($license)) {
    // Likely the 'license.created' event failed processing.
    createUserLicense($fsUser, $fsLicense);
  } else {
    $license->plan_id = $fsLicense->plan_id;
    $license->pricing_id = $fsLicense->pricing_id;
    $license->expiration = $fsLicense->expiration;
    $license->is_canceled = $fsLicense->is_canceled;
    $license->update();
  }

  // You can also do other stuff like notifying the user of the plan change or give additional entitlements etc.

  return $license;
}

switch ($fs_event->type) {
  case "license.created":
    createUserLicense($fs_event->objects->user, $fs_event->objects->license);
    break;

  case "license.extended":
  case "license.shortened":
  case "license.updated":
  case "license.cancelled":
  case "license.expired":
  case "license.plan.changed":
    updateUserLicense($fs_event->objects->user, $fs_event->objects->license);
    break;
}

http_response_code(200);

```

To trigger custom emails for specific subscription events, you can handle events such as `subscription.created` and `subscription.canceled`.

Using a JavaScript Environment?

Do check our [JS SDK Integration Doc](help-documentation-saas-sdk-js-sdk-integration.md) for an easier integration.

## Customer Portal[​](#customer-portal "Direct link to Customer Portal")

Freemius comes with a self-service [customer dashboard](help-documentation-users-account-management.md) out-of-the-box. Allowing your customers to easily access their order history, subscriptions, billing information, license keys, and more. They can change plans, update payment methods, and cancel subscriptions, putting control directly in their hands.

Alternately if your front-end is using React, you can integrate the [Customer Portal Component](help-documentation-saas-sdk-react-starter-components.md#customer-portal-component) directly into your SaaS application.

However you’d like to implement your own, within your SaaS, here are the API endpoints that will help you out:

[**Payments history**](https://docs.freemius.com/api/users/list-payments)

```http
GET https://api.freemius.com/v1/products/{product_id}/users/{user_id}/payments.json
```

When selling add-ons:

```http
GET https://api.freemius.com/v1/stores/{store_id}/users/{user_id}/payments.json
```

**Invoice download**

```http
GET https://api.freemius.com/v1/products/{product_id}/users/{user_id}/payments/{payment_id}/invoice.pdf
```

[**Payment method update**](https://docs.freemius.com/api/licenses/generate-upgrade-link)

```http
POST https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/checkout/link.js
Content-Type: application/json
Accept: application/json
Authorization: Bearer 123
Host: api.freemius.com
Content-Length: 127

{
  "is_payment_method_update": true
}
```

[**Plan change**](https://docs.freemius.com/api/licenses/generate-upgrade-link)

```http
POST https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/checkout/link.js
Content-Type: application/json
Accept: application/json
Authorization: Bearer 123
Host: api.freemius.com
Content-Length: 127

{
  "plan_id": "newPlanID”
}
```

[**Get subscription by license**](https://docs.freemius.com/api/licenses/retrieve-latest-subscription)

```http
GET https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/subscription.json
```

[**Get subscriptions**](https://docs.freemius.com/api/users/list-subscriptions)

```http
GET https://api.freemius.com/v1/products/{product_id}/users/{user_id}/subscriptions.json
```

[**Cancel subscription by license**](https://docs.freemius.com/api/licenses/cancel-current-subscription)

```http
DELETE https://api.freemius.com/v1/products/{product_id}/licenses/{license_id}/subscription.json
```

[**Cancel subscription**](https://docs.freemius.com/api/subscriptions/cancel)

```http
DELETE https://api.freemius.com/v1/products/{product_id}/subscriptions/{subscription_id}.json
```

[**Get licenses**](https://docs.freemius.com/api/users/list-licenses)

```http
GET https://api.freemius.com/v1/products/{product_id}/users/{user_id}/licenses.json
```

When selling add-ons:

```http
GET https://api.freemius.com/v1/stores/{store_id}/users/{user_id}/licenses.json
```