---
title: "API Reference for the TypeScript Node.js SDK"
url: "https://freemius.com/help/documentation/saas-sdk/js-sdk/api/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:41+06:00"
word_count: 1718
---

The `freemius.api` provides access to the full range of [API operations](https://docs.freemius.com/api) available on the Freemius platform. This includes methods for managing licenses, subscriptions, users, and more.

note

Checkout the [installation guide](help-documentation-saas-sdk-js-sdk-installation.md) if you haven't set up the SDK yet.

## Common Interfaces[​](#common-interfaces "Direct link to Common Interfaces")

Every API operation available under `freemius.api`—for example, `freemius.api.license`, `freemius.api.subscription`, and others—shares a common set of interfaces for filtering, pagination, and sorting.

- `retrieve(entityId: number)`: Retrieve a single entity by its ID.
- `retrieveMany(filter?: FilterOptions, pagination?: PaginationOptions)`: Retrieve multiple entities with optional filtering, and pagination.
- `iterateAll(filter?: FIlterOptions, pageSize: number = 50)`: An async generator to iterate over all entities, handling pagination automatically.

### Pagination[​](#pagination "Direct link to Pagination")

The `PaginationOptions` interface has the following properties:

1. `count` (number): The number of items to return per page. The maximum value is 50, which is also the default if not specified.
2. `offset` (number): The number of items to skip before starting to collect the result set. The default is 0.

Here's an example of using the `retrieveMany` method with filtering and pagination:

```ts
const subscriptions = await freemius.api.subscription.retrieveMany(
  { billing_cycle: 12 },
  { count: 20, offset: 20 }
);
```

### Filtering[​](#filtering "Direct link to Filtering")

The `FilterOptions` interface depends on the entity type. You can use any TypeScript IDE or editor with IntelliSense support to explore the available filtering options.

## Managing Licenses[​](#managing-licenses "Direct link to Managing Licenses")

Use the `freemius.api.license` namespace to manage licenses. Licenses are the primary entitlement mechanism in Freemius. Once a buyer makes a purchase, a license is created for them. Each Freemius license has its own expiration date and quota, depending on the purchased plan and pricing. You will need licenses in order to:

- Verify the purchase and the associated user, along with the plan and pricing.
- Check the license status (active, expired, canceled, etc.).
- Manage associated subscriptions.

tip

If you want to build a custom dashboard, consider using the [React Starter Kit](help-documentation-saas-sdk-react-starter.md) which comes with pre-built UI components and backend integration.

The following methods are available for license management:

### Retrieval of Licenses[​](#retrieval-of-licenses "Direct link to Retrieval of Licenses")

To retrieve a single license by its ID, use the `retrieve` method.

```ts
const license = await freemius.api.license.retrieve(licenseId);
```

To retrieve multiple licenses, use the `retrieveMany` method.

```ts
const licenses = await freemius.api.license.retrieveMany(filter, pagination);
```

You can also provide optional filtering and pagination parameters.

To fetch all licenses with automatic pagination, you can use the convenience method `iterateAll`.

```ts
const allLicenses = [];
for await (const entity of freemius.api.license.iterateAll({
  filter: 'active',
})) {
  allLicenses.push(entity);
}

console.log('Total active licenses:', allLicenses.length);
console.table(allLicenses);
```

### Retrieving Subscription Associated with a License[​](#retrieving-subscription-associated-with-a-license "Direct link to Retrieving Subscription Associated with a License")

```ts
const subscription = await freemius.api.license.retrieveSubscription(licenseId);
```

This method returns the [subscription associated with the license](https://docs.freemius.com/api/licenses/retrieve-latest-subscription), if any. If the license belongs to a one-off purchase, it will return `null`.

### Retrieving Upgrade Authorization[​](#retrieving-upgrade-authorization "Direct link to Retrieving Upgrade Authorization")

Freemius Checkout provides a built-in upgrade path for buyers to move from one plan or pricing to another. To facilitate this, you can retrieve an [upgrade authorization](https://docs.freemius.com/api/licenses/generate-upgrade-link) for a specific license.

```ts
const authorization =
  await freemius.api.license.retrieveCheckoutUpgradeAuthorization(12345);
```

You can now use it with [Freemius Checkout JS](help-documentation-checkout-integration-freemius-checkout-buy-button.md).

```ts
checkout.open({
  license_id: licenseId,
  authorization: authorization,
});
```

Optionally, you can also leverage [`freemius.checkout`](help-documentation-saas-sdk-js-sdk-checkout.md#handling-upgrade-flow) to build the Checkout options from the backend.

```ts
const options = (await freemius.checkout.create({ licenseId: 12345 }))
  // Or .getLink()
  .getOptions();
```

The SDK will automatically include the upgrade authorization in the generated options.

You can now safely pass the options to the frontend and use them with [Freemius Checkout JS](help-documentation-checkout-integration-freemius-checkout-buy-button.md).

## Managing Subscriptions[​](#managing-subscriptions "Direct link to Managing Subscriptions")

You can use the `freemius.api.subscription` namespace to manage subscriptions. Subscriptions are recurring payments that provide ongoing access to your product.

### Retrieval of Subscriptions[​](#retrieval-of-subscriptions "Direct link to Retrieval of Subscriptions")

To retrieve a single subscription by its ID, use the `retrieve` method.

```ts
const subscription = await freemius.api.subscription.retrieve(subscriptionId);
```

Similarly, to retrieve multiple subscriptions, use the `retrieveMany` method.

```ts
const subscriptions = await freemius.api.subscription.retrieveMany(
  filtering,
  pagination
);
```

You can also use the `iterateAll` method to fetch all subscriptions with automatic pagination.

```ts
const allSubscriptions = [];
for await (const subscription of freemius.api.subscription.iterateAll(
  { filter: 'active' },
  20
)) {
  allSubscriptions.push(subscription);
}
console.log('Total active subscriptions:', allSubscriptions.length);
console.table(allSubscriptions);
```

### Apply Cancellation Coupon to a Subscription[​](#apply-cancellation-coupon-to-a-subscription "Direct link to Apply Cancellation Coupon to a Subscription")

Freemius offers setting up [subscription cancellation coupon](help-documentation-marketing-automation-special-coupons-discounts.md#subscription-cancellation-coupon).

Our SaaS Starter Kit will automatically prompt users with the coupon when they attempt to cancel their subscription.

If you are creating a custom cancellation flow, you can retrieve the coupon code associated with a subscription and apply it during the cancellation process.

```ts
const coupon =
  await freemius.api.product.retrieveSubscriptionCancellationCoupon();

const result = await freemius.api.subscription.applyRenewalCoupon(
  subscriptionId,
  coupon[0].id!,
  true
);
```

### Cancel a Subscription[​](#cancel-a-subscription "Direct link to Cancel a Subscription")

To cancel a subscription, please use the following method:

```ts
const cancellation = await freemius.api.subscription.cancel(
  subscriptionId,
  'Log cancellation reason from SDK',
  reasonIds
);
```

The `reasonId` parameter is a `number[]` and can be one or more of the following values:

- `1`: I want to control when I pay.
- `2`: I'm not sure I want to keep it.
- `3`: I never/seldom use it.
- `4`: It was too difficult to set up.
- `5`: It didn't have the features I was looking for.
- `6`: It was too slow and/or buggy.
- `7`: The cost was too high.

## Managing Users[​](#managing-users "Direct link to Managing Users")

The `freemius.api.user` namespace allows you to manage users associated with your products.

### Retrieval of Users[​](#retrieval-of-users "Direct link to Retrieval of Users")

To retrieve a single user by their ID, use the `retrieve` method.

```ts
const user = freemius.api.user.retrieve(123);
console.log(user);
```

To retrieve multiple users, use the `retrieveMany` method.

```ts
const users = await freemius.api.user.retrieveMany(filter, pagination);
console.log(users);
```

You can also use the `iterateAll` method to fetch all users with auto pagination.

```ts
const allUsers = [];
for await (const user of freemius.api.user.iterateAll({ filter: 'paying' })) {
  allUsers.push(user);
}
console.table(allUsers);
```

### Searching User by Email[​](#searching-user-by-email "Direct link to Searching User by Email")

When creating an integration with your SaaS or app, you might want to search for a user by their email address. This is especially useful if the purchase happens outside of your product and you did not have any redirection or webhook to capture the license or user ID.

```ts
const userByEmail = await freemius.api.user.retrieveByEmail('[email protected]');
```

If the user has ever purchased your product, the API will return the user object; otherwise, it will return `null`.

### Manage User's Billing Information[​](#manage-users-billing-information "Direct link to Manage User's Billing Information")

The Freemius API allows you to manage a user's billing information, including retrieving and updating their billing details. Billing information is primarily used for payments and invoices. When users make a purchase, Freemius creates a billing profile for them.

```ts
// Retrieve billing
const billing = await freemius.api.user.retrieveBilling(123);
console.log(billing);

// Update billing
const updatedBilling = await freemius.api.user.updateBilling(123, {
  business_name: 'Foo Inc',
  tax_id: '12345',
});
```

Please refer to type IntelliSense or the [API documentation](https://docs.freemius.com/api/users/update-or-create-billing) to see the full set of updatable fields.

### Retrieve User's Purchase Information[​](#retrieve-users-purchase-information "Direct link to Retrieve User's Purchase Information")

You can use the following methods to retrieve a user's purchase information, including their licenses, subscriptions, and payments.

```ts
const userLicenses = await freemius.api.user.retrieveLicenses(123);
console.table(userLicenses);

const userSubscriptions = await freemius.api.user.retrieveSubscriptions(123);
console.table(userSubscriptions);

const userPayments = await freemius.api.user.retrievePayments(123);
console.table(userPayments);
```

You can use this information to build a custom dashboard or for customer support purposes.

tip

If you want to build a custom dashboard, consider using the [React Starter Kit](help-documentation-saas-sdk-react-starter.md) which comes with pre-built UI components and backend integration.

### Generate Magic Link for SSO to Customer Portal[​](#generate-magic-link-for-sso-to-customer-portal "Direct link to Generate Magic Link for SSO to Customer Portal")

If you want to use the Freemius hosted [Customer Portal](help-documentation-users-account-management.md) to allow your users to manage their licenses and subscriptions, you can generate a magic link for Single Sign-On (SSO) using the following method:

```ts
const customerPortal =
  await freemius.api.user.retrieveHostedCustomerPortal(9999);

redirectTo(customerPortal.link);
```

If you don't have the user ID but you have their email address, you can also generate a magic link using their email:

```ts
const customerPortal =
  await freemius.api.user.retrieveHostedCustomerPortalByEmail(
    '[email protected]'
  );

redirectTo(customerPortal.link);
```

More information can be found in the [Magic Login Link to Customer Portal documentation](help-documentation-users-account-management-magic-login-link.md).

## Managing Payments[​](#managing-payments "Direct link to Managing Payments")

The `freemius.api.payment` namespace allows you to manage payments associated with your products.

### Retrieval of Payments[​](#retrieval-of-payments "Direct link to Retrieval of Payments")

To retrieve a single payment by its ID, use the `retrieve` method.

```ts
const payment = await freemius.api.payment.retrieve(123);
console.log(payment);
```

To retrieve multiple payments, use the `retrieveMany` method.

```ts
const payments = await freemius.api.payment.retrieveMany({
  filter: 'not_refunded',
});
console.table(payments);
```

You can also use the `iterateAll` method to fetch all payments with automatic pagination.

```ts
const allPayments = [];
for await (const payment of freemius.api.payment.iterateAll({
  filter: 'not_refunded',
})) {
  allPayments.push(payment);
}
console.table(allPayments);
```

### Retrieve Payment Invoice[​](#retrieve-payment-invoice "Direct link to Retrieve Payment Invoice")

You can directly retrieve the invoice PDF (in blob format) for a specific payment using the following method:

```ts
const invoiceId = 123; // Replace with a valid payment ID that has an invoice
const pdf = await freemius.api.payment.retrieveInvoice(invoiceId);
const response = new Response(pdf, {
  headers: {
    'Content-Type': 'application/pdf',
    'Content-Disposition': `inline; filename="invoice_${invoiceId}.pdf"`,
  },
});
console.log(response);
```

note

Our [React Starter Kit](help-documentation-saas-sdk-react-starter.md) comes with pre-built UI components and backend integration to display users' payments and invoices.

## Pricing Information[​](#pricing-information "Direct link to Pricing Information")

The `freemius.api.product` namespace allows you to access product and pricing information. This is useful when you want to use Freemius as the single source of truth for pricing data.

### Retrieve Pricing Data[​](#retrieve-pricing-data "Direct link to Retrieve Pricing Data")

You can retrieve product and pricing information using the following methods:

```ts
const pricingData = await freemius.api.product.retrievePricingData();
console.log(pricingData);
```

You can use this data to create pricing tables or other marketing pages on your website.

The [React Starter Kit](help-documentation-saas-sdk-react-starter.md) comes with pre-built UI components to display pricing data in a beautiful pricing table component.

### Retrieve Subscription Cancellation Coupon[​](#retrieve-subscription-cancellation-coupon "Direct link to Retrieve Subscription Cancellation Coupon")

If you have set up a [subscription cancellation coupon](help-documentation-marketing-automation-special-coupons-discounts.md#subscription-cancellation-coupon), you can retrieve it using the following method:

```ts
const cancellationCoupon =
  await freemius.api.product.retrieveSubscriptionCancellationCoupon();
console.log(cancellationCoupon);
```