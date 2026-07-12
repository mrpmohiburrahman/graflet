[Changelog](https://freemius.com/changelog/) / New Checkout Feature for SaaS – Readonly user mode + Bug fix

This week’s deployment brings enhancements to the Freemius Checkout.

### Read-only user mode – aimed for SaaS integrations

This is yet another push to make our Freemius platform more friendly for SaaS integrations. For SaaS, we understand most solutions would have their own user system. When loading the Checkout you can already populate the fields with the following [parameters](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md).

- `user_firstname` – The first name of the user.
- `user_lastname` – The last name of the user.
- `user_email` – The email address of the user.

[![Freemius Checkout with prefilled user data](https://freemius.com/blog/wp-content/uploads/2024/08/editable-user-field-freemius-1024x542.png)](https://freemius.com/blog/wp-content/uploads/2024/08/editable-user-field-freemius.png)

However, the user could still change their information if they wanted to from the checkout. This could make it difficult for SaaS products to [consume webhook events](help-documentation-marketing-automation-events-webhooks.md) and find the right user.

To solve this, we have introduced a new parameter `readonly_user`.

[![Freemius checkout with readonly user data](https://freemius.com/blog/wp-content/uploads/2024/08/non-editable-user-field-freemius-checkout-1024x418.png)](https://freemius.com/blog/wp-content/uploads/2024/08/non-editable-user-field-freemius-checkout.png)

When set to `true` the fields will not let the user edit the information anymore. It works for both JS integration as well as standalone mode (when the checkout is opened directly).

### Bug fix in success dialog

[![](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-thank-you-dialog-1024x692.png)](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-checkout-thank-you-dialog.png)

We discovered that the ‘support’ email address was mistakenly shown as the sender in the thank you dialog after a purchase. Emails should be sent from the ‘system’ email you’ve configured. This bug has now been fixed.

[![](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-email-configuration-1024x468.png)](https://freemius.com/blog/wp-content/uploads/2024/08/freemius-email-configuration.png)

You can configure the email addresses on the ‘Emails’ page of your product or store.