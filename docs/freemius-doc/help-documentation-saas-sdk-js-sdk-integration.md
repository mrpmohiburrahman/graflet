---
title: "Integrating the Freemius JS SDK into Your Application"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/integration/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 2365
---

Most SaaS applications have unique stacks and architectures. However, after analyzing common integration patterns, we have developed a straightforward guide that should work for the majority of applications.

In this integration guide, we will:

1. Create a local database table to store Freemius purchase information (in an entitlement table).
2. Demonstrate how to create Checkout Options in the backend to easily generate checkouts in the frontend.
3. Process a purchase and store the relevant information in your local database.
4. Synchronize license updates via [webhooks](help-documentation-saas-events-webhooks.md).

note

Refer to the [installation guide](help-documentation-saas-sdk-js-sdk-installation.md) if you have not set up the SDK yet.

This guide does not assume any specific framework or architecture.

- We use TypeScript, but you can easily adapt the examples to JavaScript.
- We use a generic `db` object to represent database operations. Replace it with your actual database library or ORM, such as Prisma or Drizzle. We provide examples for popular ORMs.
- We use a generic `fetch`-based API to illustrate how to create API endpoints. You can substitute this with your framework's routing and request handling mechanism, such as Express, Next.js, or Fastify.

tip

Using Next.js? See our [Next.js integration guide](help-documentation-saas-sdk-framework-nextjs.md) for a more tailored approach.

## Creating the Entitlement Table[​](#creating-the-entitlement-table "Direct link to Creating the Entitlement Table")

A license is the primary entitlement in Freemius. It represents a purchase made by a customer for a specific product, plan and pricing. A license may be associated with a subscription, which defines the billing cycle and renewal terms. For one-time purchases, the license will not be linked to any subscription.

We recommend creating a local `user_fs_entitlement` table in your database to store relevant information about each license. Below is an example schema:

- SQL
- Prisma
- Drizzle

```sql
-- First create the enum type
CREATE TYPE fs_entitlement_type AS ENUM ('subscription', 'lifetime');

-- Then create the table
CREATE TABLE user_fs_entitlement (
    id            TEXT PRIMARY KEY,
    "userId"      TEXT NOT NULL,
    "fsLicenseId" TEXT NOT NULL UNIQUE,
    "fsPlanId"    TEXT NOT NULL,
    "fsPricingId" TEXT NOT NULL,
    "fsUserId"    TEXT NOT NULL,
    type          fs_entitlement_type NOT NULL,
    expiration    TIMESTAMP(3) WITHOUT TIME ZONE,
    "isCanceled"  BOOLEAN NOT NULL,
    "createdAt"   TIMESTAMP(3) WITHOUT TIME ZONE NOT NULL,
    CONSTRAINT    fk_user FOREIGN KEY ("userId") REFERENCES "User"(id) ON DELETE CASCADE
);

-- Index on type for faster filtering
CREATE INDEX idx_user_fs_entitlement_type ON user_fs_entitlement (type);
```

```graphql
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

```ts
import {
  pgTable,
  text,
  boolean,
  timestamp,
  index,
  pgEnum,
} from 'drizzle-orm/pg-core';
import { users } from './user'; // your User table

// Enum type
export const fsEntitlementType = pgEnum('fs_entitlement_type', [
  'subscription',
  'lifetime',
]);

// Table
export const userFsEntitlements = pgTable(
  'user_fs_entitlement',
  {
    id: text('id').primaryKey(),

    userId: text('userId')
      .notNull()
      .references(() => users.id, { onDelete: 'cascade' }),

    fsLicenseId: text('fsLicenseId').notNull().unique(),
    fsPlanId: text('fsPlanId').notNull(),
    fsPricingId: text('fsPricingId').notNull(),
    fsUserId: text('fsUserId').notNull(),

    type: fsEntitlementType('type').notNull(),

    expiration: timestamp('expiration', { withTimezone: false, precision: 3 }),
    isCanceled: boolean('isCanceled').notNull(),
    createdAt: timestamp('createdAt', {
      withTimezone: false,
      precision: 3,
    }).notNull(),
  },
  (table) => ({
    typeIdx: index('idx_user_fs_entitlement_type').on(table.type),
  })
);
```

## Creating Checkouts[​](#creating-checkouts "Direct link to Creating Checkouts")

We recommend using the backend to create checkouts. This allows you to easily scope the checkout to a specific user, pre-fill customer information, and apply discounts or trials.

```ts
const checkout = await freemius.checkout.create({
  user: session?.user,
  isSandbox: process.env.NODE_ENV !== 'production',
});
```

Here, we assume you have a `session` object that contains the authenticated user's information. The `user` property should include at least the `email`, and `name` or `firstName` and `lastName` fields.

With the `isSandbox` flag set to `true`, the checkout is created in sandbox mode, which is useful for testing. In production, you should set it to `false`. For more information, please refer to the [checkout documentation](help-documentation-saas-sdk-js-sdk-checkout.md).

Use the following method to generate the checkout options:

```ts
const options = checkout.getOptions();
const link = checkout.getLink();
```

We also provide a convenient `serialize` method that returns both:

```ts
const { options, link } = checkout.serialize();
```

You can then pass `options` and `link` to the frontend using your framework's preferred method, such as embedding them in the HTML, using a global JavaScript variable, or passing them as props to a React component. They are used to create either the overlay or hosted checkout in the frontend.

### Using the Overlay Checkout[​](#using-the-overlay-checkout "Direct link to Using the Overlay Checkout")

The overlay checkout opens the checkout in a modal overlay on top of your application. This provides a seamless user experience without redirecting users away from your site.

For the sake of this example, we will assume that the `options` object is now available in the frontend as `window.__FS_CHECKOUT_OPTIONS__`.

You can now use it to create a [checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) in the frontend:

```ts
// Front-end code
import { Checkout } from '@freemius/checkout';

const checkout = new Checkout(window.__FS_CHECKOUT_OPTIONS__);

checkout.open({
  success: (data) => {
    console.log('Purchase completed:', data);
  },
});
```

info

Please note that the example above uses the [Freemius Checkout JS SDK](https://github.com/Freemius/freemius-checkout-js/), which should not be confused with the Freemius JS SDK.

The **Checkout SDK** is designed specifically to handle the checkout process in the frontend, while the Freemius JS SDK is used for backend operations such as creating checkout options, managing licenses, and handling subscriptions.

### Using Hosted Checkout[​](#using-hosted-checkout "Direct link to Using Hosted Checkout")

Hosted Checkout are direct links that take users to a dedicated Freemius-hosted checkout page.

Again, for the sake of this example, we will assume that the `link` variable is now available in the frontend as `window.__FS_CHECKOUT_LINK__`.

```html
<a href="#" id="subscribe-button">Subscribe Now</a>
<script>
  document
    .getElementById('subscribe-button')
    .addEventListener('click', function (event) {
      event.preventDefault();
      window.location.href = window.__FS_CHECKOUT_LINK__;
    });
</script>
```

## Sending Purchase Data to the Backend[​](#sending-purchase-data-to-the-backend "Direct link to Sending Purchase Data to the Backend")

Next, we want to send purchase data to the backend to store it in the local database.

First, we will create a convenient function, `processPurchaseInfo`, to process the purchase data and store it in the local database.

user-entitlement.ts

As a convention, let's create all entitlement related functions in a file named `user-entitlement.ts`.

src/lib/user-entitlement.ts

```ts
import { type PurchaseInfo } from '@freemius/sdk';
import { freemius } from './freemius'; // our freemius instance
import { db } from './db'; // our database instance

export async function findUserByEmail(email: string) {
  // Replace with your actual user lookup logic
  return db.user.findUnique({ where: { email } });
}

export async function processPurchaseInfo(purchase: PurchaseInfo) {
  const user = await findUserByEmail(purchase.email);

  // We exit if the user hasn't registered to our application yet.
  // Alternatively, you can register the user automatically here if desired.
  if (!user) {
    return;
  }

  // Insert or update the purchase in our local database
  await db.userFsEntitlement.upsert({
    where: {
      fsLicenseId: purchase.licenseId,
    },
    update: purchase.toEntitlementRecord(),
    create: purchase.toEntitlementRecord({ userId: user.id }),
  });
}
```

In the previous steps, we covered both the overlay and hosted checkout methods. How you send the purchase data to the backend depends on which method you are using.

### Overlay Checkout[​](#overlay-checkout "Direct link to Overlay Checkout")

For the overlay checkout, use the `success` callback.

```ts
checkout.open({
  success: async (data) => {
    console.log('Purchase completed:', data);
    await fetch('/api/purchase', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
  },
});
```

On the backend, create an API endpoint to handle this request. The exact implementation depends on your framework, but here is a generic example:

src/api/purchase.ts

```ts
import { freemius } from './lib/freemius'; // our freemius instance
import { processPurchaseInfo } from './lib/user-entitlement';

export default {
  async fetch(request: Request) {
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    const purchaseData = await request.json();

    // Validate the purchase data
    if (!purchaseData.purchase?.license_id || !purchaseData.trial?.license_id) {
      return new Response('Bad Request: Missing licenseId', { status: 400 });
    }

    try {
      // Retrieve the full purchase details from Freemius
      const licenseId =
        purchaseData.purchase?.license_id ?? purchaseData.trial?.license_id;
      const purchase = await freemius.purchase.retrievePurchase(licenseId);

      await processPurchaseInfo(purchase);

      return new Response('Purchase recorded', { status: 200 });
    } catch (error) {
      console.error('Error processing purchase:', error);
      return new Response('Internal Server Error', { status: 500 });
    }
  },
};
```

The example above shows a serverless function that uses the Fetch API. You can adapt it to your framework's routing and request handling mechanism.

Using the React Starter Kit?

You can just implement the needed endpoints and use the pre-built UI components. See the [Starter Kit API Endpoints guide](help-documentation-saas-sdk-js-sdk-starter-kit-api-endpoints.md) for more details.

### Hosted Checkout[​](#hosted-checkout "Direct link to Hosted Checkout")

When using the hosted checkout method, you typically set up a [success redirection](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase) to return users to your application after they complete the checkout process.

In the success redirection handler, you can extract the purchase information from the query parameters, similar to the overlay checkout method.

First, we will create a function, `processRedirect`, to handle the redirect information and process the purchase in the backend.

src/lib/user-entitlement.ts

```ts
export async function processRedirect(
  info: CheckoutRedirectInfo
): Promise<void> {
  const purchaseInfo = await freemius.purchase.retrievePurchase(
    info.license_id
  );

  if (purchaseInfo) {
    await processPurchaseInfo(purchaseInfo);
  }
}
```

Now let’s create the redirection handler endpoint:

src/api/process-purchase.ts

```ts
import { freemius } from './lib/freemius'; // our freemius instance
import { processRedirect } from './lib/user-entitlement';

const PROXY_URL = 'https://yourdomain.com'; // The actual URL seen by the user

export default {
  async fetch(request: Request) {
    if (request.method !== 'GET') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    try {
      const currentUrl = request.url;
      const redirectInfo = await freemius.checkout.processRedirect(
        currentUrl,
        PROXY_URL
      );

      await processRedirect(redirectInfo);

      return new Response('Purchase recorded', { status: 200 });
    } catch (error) {
      console.error('Error processing purchase:', error);
      return new Response('Internal Server Error', { status: 500 });
    }
  },
};
```

The code automatically authenticates the redirection URL, extracts the information, and calls the backend function. To learn more about handling redirects, please refer to the [checkout documentation](help-documentation-saas-sdk-js-sdk-checkout.md#processing-redirects).

## Using Entitlement Logic[​](#using-entitlement-logic "Direct link to Using Entitlement Logic")

Finally, create a function to check if a user has an active entitlement.

src/lib/user-entitlement.ts

```ts
import { freemius } from './lib/freemius'; // our freemius instance
import { db, type UserFsEntitlement } from './lib/db'; // our database instance

// ... Existing code ...

/**
 * Get the user's entitlement.
 *
 * @returns The user's active entitlement or null if the user does not have an active entitlement.
 */
export async function getUserEntitlement(
  userId: string
): Promise<UserFsEntitlement | null> {
  const entitlements = await db.userFsEntitlement.findMany({
    where: { userId, type: 'subscription' },
  });

  return freemius.entitlement.getActive(entitlements);
}
```

The `entitlement.getActive` method will check if the license is still valid, not expired, and not canceled. If the license is valid, it will return the license data; otherwise, it will return `null`. You can read more about it in the [purchase documentation](help-documentation-saas-sdk-js-sdk-purchases.md).

Now you can use this function to check if a user has an active entitlement and grant or restrict access to your product accordingly. We recommend using the `fsPricingId` field to determine the level of access, as it is unique for each pricing plan.

```ts
export function hasAccessToFeatureX(
  entitlement: UserFsEntitlement | null
): boolean {
  if (!entitlement) {
    return false;
  }

  const requiredPricingId = 'your_required_pricing_id_here';

  return entitlement.fsPricingId === requiredPricingId;
}
```

## Handling License Updates via Webhooks[​](#handling-license-updates-via-webhooks "Direct link to Handling License Updates via Webhooks")

We need to handle license updates that may occur outside of our application, such as cancellations, renewals, or expirations. For this, we will use webhooks.

Do not avoid setting up webhooks

If you do not set up webhooks, your application will not be able to update the license's expiration date or cancellation status when they change in Freemius. This may lead to users losing access to your product even though they have an active subscription.

We will set up a webhook listener at `/api/webhook` to process incoming webhook events from Freemius.

src/api/webhook.ts

```ts
import { freemius } from './lib/freemius'; // our freemius instance
import { type LicenseEntity, type WebhookEventType } from '@freemius/sdk';
import { processPurchaseInfo } from './lib/user-entitlement';

async function syncEntitlementFromWebhook(licenseId: string) {
  const purchaseInfo = await freemius.purchase.retrievePurchase(licenseId);

  if (purchaseInfo) {
    await processPurchaseInfo(purchaseInfo);
  }
}

export default {
  async fetch(request: Request) {
    if (request.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 });
    }

    const listener = freemius.webhook.createListener();

    const licenseEvents: WebhookEventType[] = [
      'license.created',
      'license.extended',
      'license.shortened',
      'license.updated',
      'license.cancelled',
      'license.expired',
      'license.plan.changed',
    ];

    listener.on(licenseEvents, async ({ objects: { license } }) => {
      if (license && license.id) {
        await syncEntitlementFromWebhook(license.id);
      }
    });

    return await freemius.webhook.processFetch(listener, request);
  },
};
```

This will automatically synchronize the license information in your local database whenever a relevant event occurs in Freemius.

From the Freemius [Developer Dashboard](https://dashboard.freemius.com/), you can also delete licenses, which will trigger the `license.deleted` event. To listen for this event, you can add the following code to the entitlement file and webhook listener:

src/lib/user-entitlement.ts

```ts
// ... Existing code ...

export async function deleteEntitlement(fsLicenseId: string) {
  await db.userFsEntitlement.delete({
    where: { fsLicenseId },
  });
}
```

And update the webhook listener:

src/api/webhook.ts

```ts

// ... Existing code ...

export default {
  async fetch(request: Request) {
    // ...
    const listener = freemius.webhook.createListener();
    // ... Existing event listeners ...

    listener.on('license.deleted', async ({ data} }) => {
      await deleteEntitlement(data.license_id);
    });

    return await freemius.webhook.processFetch(listener, request);
  },
};
```

Notice that the data structure for the `license.deleted` event is different from the other events, so we need to handle it separately.

Finally, configure the webhook URL in the [Freemius Developer Dashboard](help-documentation-saas-events-webhooks.md#how-to-create-a-webhook).

## What's next?[​](#whats-next "Direct link to What's next?")

You have now fully integrated Freemius into your SaaS application. You can explore different features of the SDK to create even richer experiences for your users.

If you are looking for pre-made UI components for Checkout, Paywall, Customer Portal, Pricing Table, and more, please take a look at our [React Starter Kit](help-documentation-saas-sdk-react-starter.md).

The starter kit requires setting up two API endpoints, which you can implement using the examples provided [in this guide](help-documentation-saas-sdk-js-sdk-starter-kit-api-endpoints.md).