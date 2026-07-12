[Changelog](https://freemius.com/changelog/) / Enhanced Language Support and UI Updates for Freemius Checkout Translation

Following our release of [Checkout Translation](blog-changelog-freemius-checkout-translations-out-of-beta.md), we have made additional updates to the UI.

[![](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-language-selector-ui-1024x672.png)](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-language-selector-ui.png)

We now always display the language selector dropdown in the footer, with the default language set to ‘English.’ If you want to automatically select a supported language based on the buyer’s location, you can pass `language: 'auto'` to the [JavaScript SDK](blog-changelog-new-javascript-sdk-for-freemius-checkout-calling-for-testers.md).

```
const handler = new FS.Checkout({
  plugin_id: 'x',
  public_key: '...',
  language: 'auto',
});
```

Additionally,

1. We have renamed the language labels to their native names (e.g., ‘Español’ instead of ‘Spanish’) to help users select the correct language.
2. We have also added flag icons to better represent each language’s locale.
3. The German translation has been updated to fix a few minor UI glitches.

Stay tuned for more product updates.