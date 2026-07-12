[Changelog](https://freemius.com/changelog/) / Hosted Checkout Redirect: Trial Support + New Parameters

Freemius supports [redirecting the Hosted Checkout](https://freemius.com/help/documentation/checkout/hosted-checkout/#redirection_after_a_successful_purchase) after a successful purchase. This enables immediate post-purchase handling for SaaS and apps when you prefer not to wait for webhooks and want to process data right away.

We discovered that redirects were not triggering for Free Trials. We’ve fixed the issue to ensure trials behave consistently with paid purchases.

[![Enable redirect Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-redirection-1024x883.png)](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-redirection.png)

Alongside the fix, the redirect now includes additional query parameters so you can branch your logic without extra API calls:

- `action` – One of `purchase`, `license_update`, `payment_method_update`, or `trial`, indicating the type of action performed.
- `trial` – For trials, either `free` or `paid`, describing the trial type.
- `trial_ends_at` – For trials, a `YYYY-MM-DD HH:MM:SS` timestamp indicating when the trial ends.