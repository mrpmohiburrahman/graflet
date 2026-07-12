[Changelog](https://freemius.com/changelog/) / New Design for the License & Download Recovery Tool

We’ve refreshed the design of our license-recovery mini-app — the small self-service tool you can share with customers to help them retrieve their license keys and download links using only their email address.

[![Freemius License Recovery Form](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-license-recovery-form-1-882x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-license-recovery-form-1.png)

When a customer submits the form, Freemius automatically sends them an email on your behalf containing download links for their purchased products along with all associated license keys.

[![Freemius License Recovery Email](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-license-recovery-email-1024x760.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-license-recovery-email.png)

This lightweight recovery flow gives your buyers a quick way to help themselves, which can significantly reduce routine support tickets. To link users directly to the mini-app for a specific product, use the URL pattern below:

```
https://dashboard.freemius.com/license-recovery/{product_id}/{product_slug}/
```

You can find the `product_id` and `product_slug` in your Developer Dashboard. Here’s an example:

[https://dashboard.freemius.com/license-recovery/11707/my-awesome-plugin/](https://dashboard.freemius.com/license-recovery/11707/my-awesome-plugin/).

If you prefer offering a unified recovery page for your entire developer account, you can use:

```
https://dashboard.freemius.com/license-recovery/{developer_id}/
```

Your `developer_id` is available on your [Profile page](https://dashboard.freemius.com/#!/profile/).