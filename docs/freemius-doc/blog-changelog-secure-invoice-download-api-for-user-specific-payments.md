[Changelog](https://freemius.com/changelog/) / Secure Invoice Download API for User-Specific Payments

We have introduced a new API endpoint to help makers easily and securely download invoices for users. The new endpoint is:

```
/products/{product_id}/users/{user_id}/payments/{payment_id}/invoice.pdf
```

Detailed documentation can be found [here](https://docs.freemius.com/api/users/download-invoice).

[![Download invoice from Freemius API from a user's scope](https://freemius.com/blog/wp-content/uploads/2026/03/user-scope-invoice-download-api-1024x378.png)](https://freemius.com/blog/wp-content/uploads/2026/03/user-scope-invoice-download-api.png)

This is especially useful if you’re implementing the [Customer Portal](help-documentation-users-account-management.md) inside your application (for example using the [JS SDK](help-documentation-saas-sdk-js-sdk-api.md#retrieve-users-purchase-information)). The endpoint validates that the payment belongs to the specified user before delivering the invoice, adding an extra layer of safety in user-facing integrations. For these use cases, we recommend using this new endpoint over the more [direct one](https://docs.freemius.com/api/payments/download-invoice).