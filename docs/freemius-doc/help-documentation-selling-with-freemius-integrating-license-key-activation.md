This guide covers software such as desktop apps (macOS or Windows), Chrome extensions, and SaaS products that rely on license key activation.

## Initial Steps[​](#initial-steps "Direct link to Initial Steps")

1. [Sign up for Freemius](https://dashboard.freemius.com/register/).
2. Create a new SaaS or App product tailored to your needs.
3. Go to the Plans and [configure the plans and prices](help-documentation-wordpress-setup-product-pricing-plans-refunds.md).

For pre-purchase registration, see the [Checkout integration section](help-documentation-saas-saas-integration.md#checkout-integration) in the [SaaS Integration doc](help-documentation-saas-saas-integration.md).

## Revealing License Keys to Customers[​](#revealing-license-keys-to-customers "Direct link to Revealing License Keys to Customers")

This configuration is only relevant for SaaS products. For [**Apps**](help-documentation-saas-app-integration.md), license keys are always shown to buyers.

1. Log in to the [developer dashboard](https://dashboard.freemius.com/).
2. Navigate to ***Settings*** page.
3. Under the **License Keys** section, toggle on the switch to "show license keys to customers". The setting is automatically saved.

## Checkout Integration[​](#checkout-integration "Direct link to Checkout Integration")

[Integrate the checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) with your buy buttons as a modal dialog triggered by JavaScript, or by using direct checkout links.

If you require registration prior to purchasing, check the ***Checkout integration*** section in the [SaaS Integration doc](help-documentation-saas-saas-integration.md).

## License Key Integration[​](#license-key-integration "Direct link to License Key Integration")

Create a license form in your app to validate the key.

### License Activation[​](#license-activation "Direct link to License Activation")

To activate a license key, send a `POST` request to the [license activation API endpoint](https://docs.freemius.com/api/licenses/activate):

```
POST /v1/products/{product_id}/licenses/activate.json
Host: api.freemius.com
Content-Type: application/json
{
  "uid": "{uuid}",
  "license_key": "{license_key}",
  "title": "{title}"
}
```

The following parameters must be included in the request body:

- `{title}` – The name of the installation device. This helps you and [your customer](help-documentation-users-account-management-activations.md#activation-details-and-plan-upgrade) identify the device during deactivation. For example, "John's MacBook Pro".
- `{license_key}` – The entered license key
- `{uuid}` – An unique 32-character identifier. You need to generate it from your application. See [below](#generating-a-unique-identifier-uuid) for examples.

You can also include additional parameters which you can find in our [API documentation](https://docs.freemius.com/api/licenses/activate#licenses/activate/request/body).

#### Generating a Unique Identifier (UUID)[​](#generating-a-unique-identifier-uuid "Direct link to Generating a Unique Identifier (UUID)")

Here are some code snippets to generate a unique identifier (UUID) for different platforms. The UUID should be consistent for the same device, so it can be used to track license activations and deactivations.

- Node.js
- Browser
- Windows
- MacOS

```
import nodeMachineId from 'node-machine-id';
import crypto from 'node:crypto';
// Works for any JS runtime, like Nodejs, Bun, Deno, etc.
function getDeviceGuid() {
  const rawMachineId = nodeMachineId.machineIdSync();
  return crypto
    .createHash('sha256')
    .update(`freemius-my-app:${rawMachineId}`)
    .digest('hex')
    .slice(0, 32);
}
console.log(getDeviceGuid());
```

If the license key is valid and activated, the endpoint will return an object with various useful properties which you can find in the [API documentation](https://docs.freemius.com/api/licenses/activate#licenses/activate/response&c=200). The most important properties are:

- `install_id`: The ID of the created `Install` entity. This is essentially the record of the activation for the specific device.
- `install_api_token`: A bearer token that can be used to update the properties of the `Install` entity. More information can be found [here](help-documentation-saas-app-integration.md#synchronizing-application-state-with-freemius).
- `license_plan_name`: The name of the plan associated with the activated license key. This is useful for showing the user which plan they are currently subscribed to.

Save the activation details

Ensure to store the `uuid`, `install_id`, `install_api_token` and `license_key` in the local storage (for Chrome extension use [chrome.storage](https://developer.chrome.com/docs/extensions/reference/api/storage)) where the license is activated. You'll need these details during license validation and deactivation.

### License Deactivation[​](#license-deactivation "Direct link to License Deactivation")

To deactivate a license, send a `POST` request to the [license deactivation API endpoint](https://docs.freemius.com/api/licenses/deactivate):

```
POST /v1/products/{product_id}/licenses/deactivate.json?fields=id%2Cname%2Cslug
Host: api.freemius.com
Content-Type: application/json
{
  "uid": "{uuid}",
  "install_id": "{install_id}",
  "license_key": "{license_key}"
}
```

- `{uuid}` – Must be replaced with the stored install’s uuid
- `{install_id}` – Must be replaced with the stored install’s ID
- `{license_key}` – Must be replaced with the stored license key

### License Validation[​](#license-validation "Direct link to License Validation")

To validate a license, first fetch the activated license with a `GET` request to the [Retrieve an active license by ID API endpoint](https://docs.freemius.com/api/installations/retrieve-active-license-by-id):

```
GET /v1/products/{product_id}/installs/{install_id}/license.json?uid={uuid}&license_key={license_key}
Host: api.freemius.com
```

- `{uuid}` – Must be replaced with the stored install’s uuid
- `{install_id}` – Must be replaced with the stored install’s ID
- `{license_key}` – Must be replaced with the stored license key

If the license is activated on the specified install, the endpoint returns a `License` object that includes the `expiration` and `is_cancelled` properties (among others).

If `is_cancelled` is `true`, the license was canceled from the Developer Dashboard and is therefore invalid. If the license wasn’t canceled, `expiration` contains the license expiration date formatted as `Y-m-d H:i:s` (it can also be equal to `null` for lifetime licenses).

URL-encode query parameters for GET requests

When sending any query parameter with a `GET` request, for example, the license key or the UUID, please make sure to encode the values. For example:

- PHP
- JavaScript

```
$url = "https://api.freemius.com...?license_key=" . url_encode($license_key);
```

## Distributing the Software[​](#distributing-the-software "Direct link to Distributing the Software")

After integrating license key activation, the next step is to set up [custom download links](help-documentation-saas-custom-download-links.md), where your customers can download the app files.