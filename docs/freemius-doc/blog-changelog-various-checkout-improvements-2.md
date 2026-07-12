[Changelog](https://freemius.com/changelog/) / Various Checkout Improvements

This week, we’re rolling out a series of backend and frontend upgrades to make the Freemius Checkout even smoother and more robust. Here are the highlights:

### Smarter PayPal Dunning

Freemius already retries failed PayPal payments automatically. With this update, our dunning mechanism gets even tougher — now more resilient against PayPal’s downtime or server hiccups.

### Free Plan Checkout: Polished and Perfected

Freemius Checkout isn’t just for paid plans — it also powers Free Plans, helping you collect leads and marketing consent.

[![Freemius Checkout Free plan UI in Hosted Mode](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-free-plan-checkout-hosted-1024x649.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-free-plan-checkout-hosted.png)

After our recent design revamp, a few UI glitches crept into the Free Plan checkout. Those are now fully fixed, and everything looks spot-on, both in hosted and modal modes.

Additionally, we noticed that translations were not working properly.

[![Freemius Checkout with fixed translation in dialog/modal mode](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-free-plan-checkout-translated-modal-1024x898.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-free-plan-checkout-translated-modal.png)

This has also been fixed. You can now load the Free Plan checkout in a pre-selected language, and your buyers will be able to switch languages seamlessly.

### Better Error Handling

The Checkout will now bail early and display a relevant message in case of an invalid pricing configuration (licenses, currency, etc.) instead of failing silently.