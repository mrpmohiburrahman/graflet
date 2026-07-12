[Changelog](https://freemius.com/changelog/) / Beta Checkout Updates: Flexible discounts and more

We have pushed various updates to the beta checkout. Just like before, to try it out, use `checkout_style=phase2` in the URL parameter or `checkout_style: 'phase2'` in the [JavaScript integration](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md). If you’ve missed the various updates to the `phase2` beta checkout, you can find it [here](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md) and [here](blog-changelog-beta-checkout-updates-enhancements-and-bug-fixes.md).

### Flexible discounts parameters

We have three kinds of discounts we show in the checkout before the subtotal.

[![Different discounts in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/different-subtotal-discounts-freemius-checkout-1024x675.png)](https://freemius.com/blog/wp-content/uploads/2024/06/different-subtotal-discounts-freemius-checkout.png)

- **Annual Discount** – The difference between the monthly billing cycle price and the annual billing cycle price.
- **Multisite Discount –** The difference between the single license/site price and the multi-license/site price.
- **Bundle Discount** – The difference between the compounded price of a bundle’s children and the price of the bundle itself.

The reason we show all these discounts is to encourage the purchase of a higher billing cycle, licenses, or bundles.

But over the year we received feedback from our partners asking us to give the flexibility to determine which discounts are to be shown. There are cases where a huge discount can discourage a buyer. For example, if a seller is providing 100-site pricing, then it can often result in an undiscounted price of $10,000, whereas the amount to pay could be less than $500.

[![Big multi site discount](https://freemius.com/blog/wp-content/uploads/2024/06/big-multi-site-discount-1024x607.png)](https://freemius.com/blog/wp-content/uploads/2024/06/big-multi-site-discount.png)

So in this update, we are not only giving the ability to turn off discounts through configuration but also remade our discounting system from the ground up, making it smarter. Please find below the three newly introduced configuration parameters and their different values.