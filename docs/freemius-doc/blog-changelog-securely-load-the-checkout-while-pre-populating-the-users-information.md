[Changelog](https://freemius.com/changelog/) / Securely load the Checkout while pre-populating the user’s information

We’re pleased to announce a new feature we implemented following our partners’ feedback. It allows you to safely and securely load the Freemius Checkout app where the user’s name, email, VAT, country, ZIP Code/Postal Code, etc. are pre-populated.

[![Using user token to pre-populate the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2023/08/user-token-checkout-freemius.jpg)](https://freemius.com/blog/wp-content/uploads/2023/08/user-token-checkout-freemius.jpg)

### High-level process

1. When the user clicks on the purchase button, make a call to YOUR backend.
2. Your backend will figure out the ID of the user and the ID of the product they’re trying to purchase.
3. The backend will call the Freemius API to generate a token.
4. The token will be given back to the JavaScript application that intercepted the ‘click’.
5. The JavaScript application will then `open` the Freemius checkout while passing the generated token as `user_token` in the configuration.

More details and code examples have been added to our [documentation](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#user_token_in_checkout_new).