---
title: "Sell in Local Languages and Currencies with Automatic Detection"
url: "https://freemius.com/help/documentation/checkout/features/local-languages-currencies/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 620
---

Freemius Checkout supports multiple languages and currencies, helping you provide a localized buying experience for customers worldwide.

For example, if a customer from Germany accesses the checkout, you can configure it to display in German automatically and show prices in euros.

## Customization Options[​](#customization-options "Direct link to Customization Options")

By default, the checkout loads in **English** and uses **USD**. Buyers can always change these settings using the dropdowns at the bottom of the checkout.

The currency selector also appears near the total price.

If you want to preload the checkout with a specific language or currency, you can do so by using the appropriate parameters when initializing the checkout.

### Language[​](#language "Direct link to Language")

Use the [`language`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#language%20%7C%20locale) parameter. The following values are currently supported:

- **Automatic** - - (*Recommended*) Automatically detects the best language for the customer based on their location.
- **English** -
- **Spanish / Español** -
- **French / Français** -
- **German / Deutsch** -
- **Italian / Italiano** -
- **Dutch / Nederlands** -
- **Croatian / Hrvatski** -

Here are some examples of how to set the language for both the [overlay checkout](help-documentation-checkout-integration-overlay-checkout.md) and the [hosted checkout](help-documentation-checkout-integration-hosted-checkout.md):

- Overlay Checkout
- Hosted Checkout

```javascript
const checkout = new FS.Checkout({
  product_id: '<productID>',
  plan_id: '<planID>',
  language: 'de', // Set the language to German
});
```

```text
https://checkout.freemius.com/plugin/12196/plan/36392/?language=de
```

### Currency[​](#currency "Direct link to Currency")

Set the [`currency`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#currency) parameter. Freemius Checkout supports three different currencies, provided you have already [set up multi-currency pricing](help-documentation-selling-with-freemius-multi-currency.md#how-to-start-accepting-multiple-currencies) for your products:

- **Automatic** - - (*Recommended*) Automatically detects the best currency for the customer based on their location.
- **United States Dollar** -
- **Euro** -
- **British Pound Sterling** -

Here are some examples of how to set the currency for both the [overlay checkout](help-documentation-checkout-integration-overlay-checkout.md) and the [hosted checkout](help-documentation-checkout-integration-hosted-checkout.md):

- Overlay Checkout
- Hosted Checkout

```javascript
const checkout = new FS.Checkout({
  product_id: '<productID>',
  plan_id: '<planID>',
  currency: 'eur', // Set the currency to Euro
});
```

```text
https://checkout.freemius.com/plugin/12196/plan/36392/?currency=eur
```

Multi-Currency Payouts

Freemius pays out your earnings separately for each currency you sell in. Learn more [here](help-documentation-selling-with-freemius-your-earnings.md).

## Best Practices[​](#best-practices "Direct link to Best Practices")

If you're selling globally, we recommend using automatic detection for both language and currency settings.

- Overlay Checkout
- Hosted Checkout

```javascript
const checkout = new FS.Checkout({
  product_id: '<productID>',
  plan_id: '<planID>',
  currency: 'auto',
  language: 'auto',
});
```

```text
https://checkout.freemius.com/plugin/12196/plan/36392/?currency=eur&language=auto
```

This ensures that your customers see the best language and currency for their location, providing a more personalized and localized buying experience that can lead to higher conversion rates.

## Checkout Geo API[​](#checkout-geo-api "Direct link to Checkout Geo API")

While Freemius Checkout can automatically detect the best language and currency for your customers, you can also leverage the same API to get the customer's location and set the appropriate language and currency on your own pricing page. Here's how it works:

1. From your pricing page, make a GET request to the following endpoint: .
2. The API returns a JSON object containing the customer's country and currency information.
3. Use this information to set the appropriate language and currency for your customers on your pricing page or custom checkout.

```javascript
fetch('https://checkout.freemius.com/geo.json')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    // Use the data to set the appropriate language and currency
  })
  .catch((error) => {
    console.error('Error fetching geo data:', error);
  });
```

The API provides an object similar to the one below:

```json
{
  "country": {
    "name": "India",
    "code": "in"
  },
  "currency": {
    "code": "usd",
    "symbol": "$"
  }
}
```

If you want to see more languages and currencies in checkout, please use our [feature request board](https://freemius.nolt.io/) and let us know which ones you would like to see. This helps us prioritize development and better meet customer needs.