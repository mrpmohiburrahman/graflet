[Changelog](https://freemius.com/changelog/) / Freemius Checkout translations out of beta

Great news! The Freemius Checkout now fully supports the following languages out of the box.

- Spanish
- German
- French
- Italian
- Dutch

[![](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-checkout-translation-1024x636.png)](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-checkout-translation.png)

Freemius Checkout in Italian

Loading the checkout page in a buyer’s native language significantly improves conversion rates. That’s why we’ve prioritized translating the Checkout into the most popular languages.

To display the Checkout in a specific language, you can use the `language` parameter when configuring the [Checkout JavaScript SDK](blog-changelog-new-javascript-sdk-for-freemius-checkout-calling-for-testers.md). For example:

```
const handler = new FS.Checkout({
  plugin_id: 'x',
  public_key: '...',
  language: 'de_DE',
});
```

The example above will load the Checkout in German. Alternatively, you can use the value `'auto'`, which automatically determines the buyer’s location and loads the Checkout in their supported language. For more information please see our documentation [here](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md).