[Changelog](https://freemius.com/changelog/) / Updated Generic Statement Descriptor for Broader Software Support

Freemius always attempts to display a clear and [verbose statement descriptor](help-faq-sales.md#what-will-my-customers-see-on-their-credit-card-and-paypal-statement) in your customers’ credit/debit card or bank statements. This helps buyers immediately recognize their purchase and avoid accidental disputes. The descriptor we try to show is:

```
FREEMIUS* PRODUCT_NAME
```

However, depending on the bank or card issuer, the soft descriptor may not always be supported. In those cases, our system falls back to a generic descriptor. With this week’s deployment, we are updating that fallback from `FREEMIUS-PLUGIN-THEME` to `FREEMIUS SOFTWARE`.

As more makers [across different ecosystems](freemius-for-saas.md) started using Freemius beyond WordPress, the old descriptor no longer reflected the diversity of software being sold on the platform. This update ensures that the descriptor feels accurate and relevant regardless of the product type.

We initially attempted to use `FREEMIUS SOFTWARE PAY`, but the payment processors did not accept it, so we adopted `FREEMIUS SOFTWARE` instead.

[![Freemius transactional email showing the possible descriptor in statements](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-transactional-email-descriptor-1024x638.png)](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-transactional-email-descriptor.png)

Please note that Freemius will continue trying to use the soft descriptor `FREEMIUS* PRODUCT_NAME` first, and only fall back to the generic descriptor when the payment provider does not support it. This update is also reflected in the [transactional emails](help-documentation-marketing-automation-transactional-emails.md#purchase-payment-and-subscription-emails) sent from our system.