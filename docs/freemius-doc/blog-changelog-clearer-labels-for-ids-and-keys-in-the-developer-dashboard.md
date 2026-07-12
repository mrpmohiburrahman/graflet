[Changelog](https://freemius.com/changelog/) / Clearer Labels for IDs and Keys in the Developer Dashboard

Our Developer Dashboard shows IDs and keys in various places. For example, the **Settings → API & Keys** section displays the product ID along with its public and secret keys.

[![Freemius product ID and keys](https://freemius.com/blog/wp-content/uploads/2026/01/product-keys-1024x415.png)](https://freemius.com/blog/wp-content/uploads/2026/01/product-keys.png)

Similarly, on the **Plans** page we show the plan ID.

[![Freemius plan ID](https://freemius.com/blog/wp-content/uploads/2026/01/plan-id-1024x609.png)](https://freemius.com/blog/wp-content/uploads/2026/01/plan-id.png)

And within individual plans, we display the pricing ID.

[![Freemius pricing ID](https://freemius.com/blog/wp-content/uploads/2026/01/pricing-id-1024x353.png)](https://freemius.com/blog/wp-content/uploads/2026/01/pricing-id.png)

These details are critical, especially for [SaaS](help-documentation-saas.md) makers integrating with our [official SDK](help-documentation-saas-sdk-js-sdk-installation.md#retrieving-keys-from-the-developer-dashboard), as keys and IDs are required at different stages of the integration process.

Until now, we used generic labels such as *ID* or *Secret Key* across the UI. It came to our attention that this could be confusing, particularly for makers who are new to the Freemius platform.

To improve clarity and make the UI more intuitive, we reviewed the Developer Dashboard and introduced more descriptive labels, such as *Plan ID* and *Product Secret Key* as you can see in the screenshots above. This helps makers quickly identify the exact information they need without ambiguity.