---
title: "Migration Guide"
url: "https://freemius.com/help/documentation/saas-sdk/checkout-js-sdk/migration/"
source: "docs"
section: "Docs"
category: "SDKs & Starter Kits"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 654
---

This guide applies to you only if you're using the legacy version of the Checkout JS SDK, using the following script to include it:

```html
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="https://checkout.freemius.com/checkout.min.js"></script>
```

There are two ways to migrate your existing code to the new version:

## Direct Migration (recommended)[​](#direct-migration-recommended "Direct link to Direct Migration (recommended)")

This approach requires some code changes, but it is the recommended way to migrate to the new version.

### Instructions:[​](#instructions "Direct link to Instructions:")

1. In your existing code, locate the following scripts that might be used to include the Checkout SDK:

```html
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="https://checkout.freemius.com/checkout.min.js"></script>
```

2. Remove the jQuery script tag if you are not using jQuery.
3. Replace the checkout script with the new one.

```html
<script src="https://checkout.freemius.com/js/v1/"></script>
```

4. Change `FS.Checkout.configure()` to `new FS.Checkout()`:

```diff
- // Legacy checkout code
- const handler = FS.Checkout.configure({
+ // New checkout code
+ const handler = new FS.Checkout({
    plugin_id: '1234',
    plan_id: '5678',
    public_key: 'pk_xxxxxxxxxxxxxxxxx',
    image: 'https://your-plugin-site.com/logo-100x100.png',
});
```

The rest of the code will continue to work exactly as it is, with no changes.

Optionally, you can also change `plugin_id` to `product_id`. Both are supported (with preference given to `product_id` if both are set), and we do not plan to remove `plugin_id` in the near future.

Your event listener code will remain the same:

```js
document.querySelector('#purchase').addEventListener('click', (e) => {
  handler.open({
    name: 'My Awesome Plugin',
    licenses: getSelectedLicenses(),
    // You can consume the response for after purchase logic.
    purchaseCompleted: function (response) {
      // The logic here will be executed immediately after the purchase confirmation.
      // alert(response.user.email);
    },
    success: function (response) {
      // The logic here will be executed after the customer closes the checkout, after a successful purchase.
      // alert(response.user.email);
    },
  });

  e.preventDefault();
});
```

### Adding Multiple Checkouts[​](#adding-multiple-checkouts "Direct link to Adding Multiple Checkouts")

If you need to add a checkout for a different configuration on the same page, create a new checkout instance:

```js
const anotherHandler = new FS.Checkout({
  product_id: '4321',
  plan_id: '9876',
  public_key: 'pk_xxxxxxxxxxxxxxxxx',
  image: 'https://your-plugin-site.com/logo-100x100.png',
});
```

Now, add another event listener that opens the new checkout:

```js
document
  .querySelector('#another-purchase-button')
  .addEventListener('click', (e) => {
    anotherHandler.open({
      name: 'My Awesome Plugin',
      licenses: getSelectedLicenses(),
      purchaseCompleted: function (response) {
        //...
      },
      success: function (response) {
        //...
      },
    });

    e.preventDefault();
  });
```

### Upgrading from the Singleton Interface[​](#upgrading-from-the-singleton-interface "Direct link to Upgrading from the Singleton Interface")

If you have been using the `FS.Checkout` singleton interface like

```js
FS.Checkout.open({
  plugin_id: '1234',
  // ...
});
```

Adjust your code to call the methods on the instance instead of the singleton.

```js
const handler = new FS.Checkout({
  plugin_id: '1234',
  // ...
});

handler.open({
  // ...
});
```

## Migration Adapter (not recommended)[​](#migration-adapter-not-recommended "Direct link to Migration Adapter (not recommended)")

We have also introduced a compatibility layer that you can use as a quick path to migrate to the new Checkout JS without making changes to your checkout code.

However, this approach has the following limitations:

- It may stop working in a future version.
- It uses a singleton pattern, which can be confusing when configuring multiple products on the same page.
- Using the adapter will add extra bytes.

### Instructions:[​](#instructions-1 "Direct link to Instructions:")

1. Look for the checkout script:
   
   ```html
   <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
   <script src="https://checkout.freemius.com/checkout.min.js"></script>
   ```
2. Remove the jQuery script tag if you are not using jQuery.
3. Replace the checkout script with the new one.
   
   ```html
   <script src="https://checkout.freemius.com/js/v1/legacy/"></script>
   ```

Now all your existing code should work as is.

```js
const handler = FS.Checkout.configure({
  plugin_id: '1234',
  plan_id: '5678',
  public_key: 'pk_xxxxxxxxxxxxxxxxx',
  image: 'https://your-plugin-site.com/logo-100x100.png',
});

document.querySelector('#purchase').addEventListener('click', (e) => {
  handler.open({
    name: 'My Awesome Plugin',
    licenses: getSelectedLicenses(),
    // You can consume the response for after purchase logic.
    purchaseCompleted: function (response) {
      // The logic here will be executed immediately after the purchase confirmation.
      // alert(response.user.email);
    },
    success: function (response) {
      // The logic here will be executed after the customer closes the checkout, after a successful purchase.
      // alert(response.user.email);
    },
  });

  e.preventDefault();
});
```