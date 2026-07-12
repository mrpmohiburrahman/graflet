---
title: "Managing Purchases with the JS SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/purchases/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 1270
---

The `freemius.purchase` namespace in the Freemius JS SDK provides methods for retrieving and managing purchase-related data, including detailed purchase information, and subscription details. You may want to use this service to:

1. Verify and retrieve detailed information about a specific purchase using a license ID.
2. Retrieve all purchases for a user by their user ID or email.
3. Retrieve all active subscriptions for a user by their user ID or email.

With Freemius, a purchase can be either a one-off purchase or a subscription. This guide covers both scenarios.

tip

One-off purchases are ideal for selling consumables in a SaaS application, such as credits or tokens. Subscriptions are best suited for recurring billing models.

## Retrieving Purchase Information[​](#retrieving-purchase-information "Direct link to Retrieving Purchase Information")

The `retrievePurchase` method fetches detailed information about a purchase based on a license ID. This includes user details, plan information, expiration dates, and more.

```typescript
const purchase = await freemius.purchase.retrievePurchase(123456);
console.log('Purchase:', purchase);
```

This is useful when verifying purchase details after a successful checkout. For example, the [overlay checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) passes data such as `purchase.license.license_id` to the host application (your SaaS). You can then use this ID to retrieve the full purchase details. More information can be found in the [Integration Guide](help-documentation-saas-sdk-js-sdk-integration.md).

### Serializable Purchase Data[​](#serializable-purchase-data "Direct link to Serializable Purchase Data")

In environments like Next.js, where you may need to send purchase data to the client side, you can use the `toData` method to convert the purchase object into a format suitable for serialization.

```typescript
const purchaseData = purchase.toData();
```

Alternatively, the SDK provides a `retrievePurchaseData` method that directly returns serializable data:

```typescript
const purchaseData = await freemius.purchase.retrievePurchaseData(123456);
```

You can also use this to stream data from server to client components while using frameworks like Next.js.

```tsx
export default async function Page() {
  // We do not want to `await` the promise here, as we want to stream the data to the client component.
  const purchaseData = freemius.purchase.retrievePurchaseData(123456);

  return (
    <Suspense fallback={<div>Loading...</div>}>
      <PurchaseDetails purchaseData={purchaseData} />
    </Suspense>
  );
}
```

In the client component, leverage the `use` hook to resolve the promise.

```tsx
'use client';
import { use } from 'react';

export function PurchaseDetails({
  purchaseData,
}: {
  purchaseData: Promise<PurchaseData | null>;
}) {
  const data = use(purchaseData);

  if (!data) {
    return <div>No purchase data found.</div>;
  }

  return (
    <div>
      <h2>Purchase Details</h2>
      <p>License ID: {data.licenseId}</p>
      <p>User Email: {data.email}</p>
      {/* Render other purchase details as needed */}
    </div>
  );
}
```

## Retrieving Active Subscriptions of a User[​](#retrieving-active-subscriptions-of-a-user "Direct link to Retrieving Active Subscriptions of a User")

For most SaaS use cases, you might only be interested in active subscriptions. There are two ways to retrieve only active subscriptions:

1. Use the `retrieveSubscriptions` method if you already have the Freemius User ID.
2. Use the `retrieveSubscriptionsByEmail` method if you only have the user's email address.

```ts
const subscriptionByUserId =
  await freemius.purchase.retrieveSubscriptions(78910);
console.log('Subscriptions by User ID:', subscriptionByUserId);

const subscriptionsByEmail =
  await freemius.purchase.retrieveSubscriptionsByEmail('[email protected]');
console.log('Purchases by Email:', subscriptionsByEmail);
```

## Retrieving All Purchases for a User[​](#retrieving-all-purchases-for-a-user "Direct link to Retrieving All Purchases for a User")

If you want to retrieve all purchases made by a user, you have two options:

1. If you already have the Freemius User ID available, use the `retrievePurchases` method.
2. If you only have the user's email address, use the `retrievePurchasesByEmail` method.

```ts
const purchasesByUserId = await freemius.purchase.retrievePurchases(1234);
console.log('Purchases by User ID:', purchasesByUserId);

const purchasesByEmail =
  await freemius.purchase.retrievePurchasesByEmail('[email protected]');
console.log('Purchases by Email:', purchasesByEmail);
```

This will retrieve all purchases associated with the user, including both one-off purchases and subscriptions. You can also pass pagination parameters to handle large datasets.

## Storing the Purchase Data on your local Database[​](#storing-the-purchase-data-on-your-local-database "Direct link to Storing the Purchase Data on your local Database")

Regardless of how you choose to build the integration, you might want to store the purchase data in your own database. This approach provides easy access to determine whether a user has an active subscription, without needing to call the Freemius API on every request.

Integration Guide

Do not forget to check out our [Integration Guide](help-documentation-saas-sdk-js-sdk-integration.md) for more details on how to integrate the SDK with your SaaS application that covers the recommended approach to store purchase information and work with entitlements.

The rest of the guide will show some code snippets that you can use as a reference for custom implementations.

The recommended data structure for storing purchase data is as follows:

```ts
export interface PurchaseEntitlementData {
  /**
   * The unique identifier of the user in the Freemius system.
   */
  fsLicenseId: string;
  /**
   * The unique identifier of the plan in the Freemius system.
   */
  fsPlanId: string;
  /**
   * The unique identifier of the pricing in the Freemius system.
   */
  fsPricingId: string;
  /**
   * The unique identifier of the user in the Freemius system.
   */
  fsUserId: string;
  /**
   * The type of entitlement, which can be either 'subscription' or 'oneoff'.
   */
  type: PurchaseEntitlementType;
  /**
   * The expiration date of the entitlement. If `null`, the entitlement does not expire.
   * If you are passing a string, then it must of the format "YYYY-MM-DD HH:mm:ss" in UTC.
   */
  expiration: Date | null | string;
  /**
   * The date when the entitlement was created. This is useful for record-keeping and auditing purposes.
   */
  createdAt: Date | string;
  /**
   * Indicates whether the entitlement has been canceled.
   */
  isCanceled: boolean;
}
```

We do not have any strong recommendations regarding your choice of database or ORM. However, the `PurchaseInfo` object returned by the SDK has a `toEntitlementRecord` method that converts the object into a plain data structure that is easy to store in any database.

Here is an example of how you might store it in a [Prisma model](https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma):

```graphql
enum FsEntitlementType {
    subscription
    oneoff
}

// For the sake of this example, we are using a single active subscription license per user.
// But the schema can handle multiple licenses per user.
model UserFsEntitlement {
    id     String @id @default(cuid())
    userId String
    User   User   @relation(fields: [userId], references: [id], onDelete: Cascade)

    // The following matches the PurchaseDBData from Freemius Node SDK.
    // You can also use these fields as BigInt if you prefer, and in that case you will need to convert the String to BigInt in your application.
    fsLicenseId String            @unique
    fsPlanId    String
    fsPricingId String
    fsUserId    String
    type        FsEntitlementType
    expiration  DateTime?
    isCanceled  Boolean
    createdAt   DateTime

    // Add the index to optimize queries filtering by type (as needed for the JS SDK).
    @@index(type)
    @@map("user_fs_entitlement")
}
```

In your application code, you can upsert the purchase data as follows:

```ts
// Retrieve the local user from your database
const localUserId = getLocalUserIdSomehow();

// Fetch the purchase from Freemius
const fsPurchase = await freemius.purchase.retrievePurchase(123456);

// Upsert the purchase data into your database
await prisma.userFsEntitlement.upsert({
  where: {
    fsLicenseId: fsPurchase.licenseId,
  },
  update: fsPurchase.toEntitlementRecord(),
  create: fsPurchase.toEntitlementRecord({ userId: user.id }),
});
```

You will notice that we are storing the `expiration` and `isCanceled` fields. When retrieving the user's purchase data from your database, you can use these fields to determine whether the user has an active subscription.

```ts
const entitlement = await prisma.userFsEntitlement.findUnique({
  where: { fsLicenseId: fsPurchase.licenseId },
});

const hasEntitlement =
  entitlement &&
  (!entitlement.expiration || entitlement.expiration > new Date()) &&
  !entitlement.isCanceled;
```

However, our SDK also provides a convenience method.

```ts
const entitlement = await freemius.entitlement.getActive(
  prisma.userFsEntitlement.findMany({ where: { userId, type: 'subscription' } })
);
// Will be `null` if not valid.
const hasEntitlement = null !== entitlement;
```

Next, you can use this `hasEntitlement` boolean to gate access to premium features in your SaaS application.

If you have a more advanced integration where features depend on the subscribed plan, you can use the `entitlement.fsPricingId` to determine which plan the user is subscribed to.