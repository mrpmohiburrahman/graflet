---
title: "Showing Reviews and Money-Back Guarantee in the Checkout"
url: "https://freemius.com/help/documentation/checkout/features/social-proofing-ui/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 277
---

To improve sales conversion, the checkout includes two social proofing UI components:

- **Money-back guarantee**, which displays the product's [refund policy](help-documentation-selling-with-freemius-refund-policy.md).
- **Featured Review**, which displays a [featured review](help-documentation-marketing-automation-reviews.md#how-to-make-featured-reviews).

When the checkout opens as a standalone page or as the [Hosted Checkout](help-documentation-getting-started-making-your-first-sale.md#hosted-checkout), both components appear automatically.

However, in the [Checkout Overlay](help-documentation-checkout-integration-freemius-checkout-buy-button.md), you must explicitly enable them using the [show\_reviews](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_reviews) and [show\_refund\_badge](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_refund_badge) settings.

## Displaying Reviews or Testimonials[​](#displaying-reviews-or-testimonials "Direct link to Displaying Reviews or Testimonials")

To display reviews or testimonials, ensure that you have at least one review to feature. Here's how to manually add a featured review to your product:

1. Go to your product in the [Freemius Dashboard](https://dashboard.freemius.com/).
2. Click on the **Reviews** tab.
3. Click the **Add Review** button to add a new review, or select an existing review to edit.
4. Fill in the review details, including the reviewer's name, content, rating, and any other relevant information.
5. Select the **Featured** checkbox to mark the review as featured.
6. Click the **Save** button to save your changes.

If you have multiple featured reviews, the most recently added one will display.

Showing a specific review

You can also specify a particular review to display in the checkout using the [`review_id`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#review_id) setting.

## Displaying the Money-Back Guarantee[​](#displaying-the-money-back-guarantee "Direct link to Displaying the Money-Back Guarantee")

To display the money-back guarantee component, first set up the refund policy in the product "Plans" settings. Here is how to [configure the refund policy](help-documentation-selling-with-freemius-refund-policy.md#configure-the-refund-policy).

If the refund policy is set to "No Refunds," the money-back guarantee component will not appear in the checkout.

In overlay mode, set the [`show_refund_badge`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_refund_badge) setting to `true` to display the money-back guarantee component in the checkout.