[Changelog](https://freemius.com/changelog/) / Freemius Checkout Improvements

We’ve made various under-the-hood improvements to the Freemius Checkout app. Here are the notable ones.

### Improving the error messages and the UI

We’ve updated the error message to improve the UX when the server returns an error.

[![Freemius Checkout Error Message](https://freemius.com/blog/wp-content/uploads/2023/06/freemius-checkout-better-error-message.png)](https://freemius.com/blog/wp-content/uploads/2023/06/freemius-checkout-better-error-message.png)

Previously, it was showing an obscure message. While the message was relevant to attackers, it was misleading to legit customers. We hope the new message will clearly indicate to a legit customer the next steps they need to take.

### Improvement of the 2FA mechanism

We found quite a few edge cases, where the 2FA mechanism was breaking the UX due to some browser policy. To make the 2FA work – regardless of whether the browser is blocking cookies – we completely overhauled the system. Now, the 2FA should work no matter if it is embedded in an iframe and regardless of whether the browser or some extension is blocking cookies.

### Improvements in the localization

We improved a few of the translations and their plural forms to make them compatible with [transifex](https://explore.transifex.com/freemius/).