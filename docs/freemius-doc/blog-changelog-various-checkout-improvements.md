[Changelog](https://freemius.com/changelog/) / Various Checkout improvements

We’ve released several updates to our Checkout application:

## Fixed VAT validation issues

We noticed some valid VAT IDs were being blocked by the Checkout app.

[![Improved VAT ID verification](https://freemius.com/blog/wp-content/uploads/2024/03/vat-id-verification-ui-1-1024x513.png)](https://freemius.com/blog/wp-content/uploads/2024/03/vat-id-verification-ui-1.png)

We fixed this by rolling out a more robust VAT ID validation system for the front-end app.

## Improved translations

Certain strings — especially those coming up as exceptions (for example, “Invalid coupon code”) — were not getting translated.

[![Improved translation in the Checkout](https://freemius.com/blog/wp-content/uploads/2024/03/improved-translation-1024x466.png)](https://freemius.com/blog/wp-content/uploads/2024/03/improved-translation.png)

We’ve introduced fixes for them. You can also use the Freemius [Checkout Buy Button API](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) to load the Checkout in one of the supported languages.

## Improved Country Selector search algorithm

[![Improved search algorithm in the country dropdown](https://freemius.com/blog/wp-content/uploads/2024/03/better-search-country-selector-1-1024x576.png)](https://freemius.com/blog/wp-content/uploads/2024/03/better-search-country-selector-1.png)

We’ve improved the “fuzzy” logic of the Country Selector UI search feature. The search is now more natural and accurate.

## Other bug fixes

- In cases where a coupon is used, the correct discounted first payment price on the billing cycle UI is now displayed.
- We’ve fixed an issue in the SDK Checkout mode, where the “Resend email” button was not working properly.
- We’ve added ZIP code validation in the [Dunning app](blog-dunning-in-dashboard-checkout-site-trials-march.md#what_is_dunning) and made general improvements to the form validation UX.
- The responsiveness of the Checkout footer has also been fixed.