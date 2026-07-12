---
title: "Integrating License Key Activation"
url: "https://freemius.com/help/documentation/saas/integrating-license-key-activation/"
source: "docs"
section: "Docs"
category: "Setup for SaaS & Apps"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 610
---

This guide covers software such as desktop apps (macOS or Windows), Chrome extensions, and SaaS products that rely on license key activation.

warning

If you are integrating Freemius with a WordPress plugin, theme, or add-on, please follow the [WordPress SDK integration guide](help-documentation-wordpress-integration-with-sdk.md).

## Initial Steps[​](#initial-steps "Direct link to Initial Steps")

1. [Sign up for Freemius](https://dashboard.freemius.com/register/).
2. Create a new SaaS or App product tailored to your needs.
3. Go to the Plans and [configure the plans and prices](help-documentation-wordpress-setup-product-pricing-plans-refunds.md).

For pre-purchase registration, see the [Checkout integration section](help-documentation-saas-saas-integration.md#checkout-integration) in the [SaaS Integration doc](help-documentation-saas-saas-integration.md).

## Revealing License Keys to Customers[​](#revealing-license-keys-to-customers "Direct link to Revealing License Keys to Customers")

note

This configuration is only relevant for SaaS products. For [**Apps**](help-documentation-saas-app-integration.md), license keys are always shown to buyers.

Go to ***Settings*** and toggle on the switch to display license keys to customers:

## Checkout Integration[​](#checkout-integration "Direct link to Checkout Integration")

[Integrate the checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) with your buy buttons as a modal dialog triggered by JavaScript, or by using direct checkout links.

If you require registration prior to purchasing, check the ***Checkout integration*** section in the [SaaS Integration doc](help-documentation-saas-saas-integration.md).

## License Key Integration[​](#license-key-integration "Direct link to License Key Integration")

Create a license form in your app to validate the key.

### License Activation[​](#license-activation "Direct link to License Activation")

To activate a license key via the API:

```text
POST https://api.freemius.com/v1/products/{product_id}/licenses/activate.json?uid={uuid}&license_key={license_key}
```

- `{uuid}` – Must be replaced with a unique 32-character identifier (you need to generate it).
  
  - You can use `crypto.randomUUID().replace(/-/g, '')` with JavaScript, which is now standard on all modern browsers and JS runtimes. Make sure to store it in the local storage where the license is activated (for Chrome extension use [chrome.storage](https://developer.chrome.com/docs/extensions/reference/api/storage)).
- `{license_key}` – The entered license key

If the license key is valid, the endpoint will return an object with `install_id`, `install_api_token`, and other useful properties.

- Make sure you store it in the local storage where the license is activated, as you'll need it for license validation and deactivation (for Chrome extension use [chrome.storage](https://developer.chrome.com/docs/extensions/reference/api/storage)).
- The `install_api_token` is a bearer token that can be used to update the properties of the `Install` entity. More information can be found [here](help-documentation-saas-app-integration.md#synchronizing-application-state-with-freemius).

### License Deactivation[​](#license-deactivation "Direct link to License Deactivation")

To deactivate a license via the API:

```text
POST https://api.freemius.com/v1/products/{product_id}/licenses/deactivate.json?uid={uuid}&install_id={install_id}&license_key={license_key}
```

- `{uuid}` – Must be replaced with the stored install’s uuid
- `{install_id}` – Must be replaced with the stored install’s ID
- `{license_key}` – Must be replaced with the stored license key

### License Validation[​](#license-validation "Direct link to License Validation")

To validate a license, first fetch the activated license:

```text
GET https://api.freemius.com/v1/products/{product_id}/installs/{install_id}/license.json?uid={uuid}&license_key={license_key}
```

- `{uuid}` – Must be replaced with the stored install’s uuid
- `{install_id}` – Must be replaced with the stored install’s ID
- `{license_key}` – Must be replaced with the stored license key

If the license is activated on the specified install, the endpoint returns a `License` object that includes the `expiration` and `is_cancelled` properties (among others).

If `is_cancelled` is `true`, the license was canceled from the Developer Dashboard and is therefore invalid. If the license wasn’t canceled, `expiration` contains the license expiration date formatted as `Y-m-d H:i:s` (it can also be equal to `null` for lifetime licenses).

URL-encode query parameters for GET requests

When sending any query parameter with a GET request, for example, the license key or the UUID, please make sure to encode the values. For example:

- PHP
- JavaScript

```php
$url = "https://api.freemius.com...?license_key=" . url_encode($license_key);
```

```javascript
const url = `https://api.freemius.com...?license_key=${encodeURIComponent(licenseKey)}`;
```

## Distributing the Software[​](#distributing-the-software "Direct link to Distributing the Software")

After integrating license key activation, the next step is to set up [custom download links](help-documentation-saas-custom-download-links.md), where your customers can download the app files.