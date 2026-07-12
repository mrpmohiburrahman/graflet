---
title: "Providing Prorated Discounts on Upgrades & Downgrades in Freemius Checkout"
url: "https://freemius.com/help/documentation/checkout/features/proration/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 940
---

By default, Freemius *prorates* plan updates (upgrades or downgrades).

Unlike the commonly used *prorating* implementations which preserve the renewal payment processing time, Freemius’ *proration* works slightly different and will restart the billing date based on the time of the plan update. This methodology simplifies understanding the discount for the customers and also benefits the sellers who will receive the initial worth of the new plan (minus the discounts) for the full billing period right away.

See below for more details on how Freemius *prorates* plan updates.

## Proration from a Subscription (Monthly or Annual)[​](#proration-from-a-subscription-monthly-or-annual "Direct link to Proration from a Subscription (Monthly or Annual)")

Customers who are updating a plan that was purchased as a subscription will receive a *proration* discount, based on the unused portion of their previous plan:

```text
remaining_period = (1 - number_of_days_past_from_the_old_plan_last_payment / number_of_days_in_past_billing_cycle )
```

```text
proration_discount = max(0, remaining_period x old_plan_last_payment )
```

**Examples:**

- If a user purchased a single-site monthly pro package for $10 per month and after 2 months and 15 days upgrades to the annual billing cycle of the same single-site pro plan for $100 per year - the customer will have already paid $10, and will have used half of their current billing cycle. Therefore, the initial *prorated* amount will be $95 ($100 - $10 / 2).
- If a user subscribed to a single-site annual pro license for $100 per year and after 3 months decides to downgrade to a single-site annual starter plan for $80 per year - the customer will already have paid $100, and have used only a quarter of the current billing cycle. Therefore, the *proration* discount for the remaining period will be $75, and the initial price for the single-site annual starter plan will be $5 ($80 - $75). The first renewal payment will be scheduled for a year from the downgrade date and will cost $80.

## Proration from a Lifetime License[​](#proration-from-a-lifetime-license "Direct link to Proration from a Lifetime License")

Customers who purchased a lifetime plan will be eligible for a *proration* discount only if they update their plan within 30 days from the time of purchase. The *proration* discount is calculated as follows:

```text
proration_discount = min(prev_lifetime_payment, new_lifetime_price)
```

**Examples:**

- If a user purchased a single-site lifetime pro license for $300 and after 3 days upgrades to a 5-site lifetime pro license for $600, they are only charged $300 for the upgrade.
- If a user purchased a single-site lifetime starter license for $150 and after 6 days upgrades to a single-site lifetime business plan for $400, they are only charged $250 for the upgrade.
- If a user purchased a single-site lifetime pro license for $300 and after 2 months upgrades to a 5-site lifetime pro plan for $600, they are charged the full $600.

To understand why lifetime upgrades aren't just calculated as the difference in price, regardless of how long ago the original purchase was, the following two scenarios may help:

Long-Term Lifetime Upgrade Fairness

A customer purchases a lifetime license for $300. Then, after 5 years (intentionally exaggerated time for emphasis) decides to upgrade for a higher $500 plan. If you discount them with $300 it basically means that they’ve used your product/license/support for free for 5 years. If a different customer purchase that same lifetime plan for $500 at the same time the other user upgrades from the $300 to the $500 plan, they both end up paying the exact same amount in total ($500), yet, the 1st customer already been using the product for 5 years.

Car Upgrade Analogy

Or another example, to drive it home (pun intended!). Let’s say you buy a car and then after 5 years decide to buy a more expensive one from the same brand. Would you expect to get your money back? No, because you’ve already used the product, which is analogous to receiving support (aka warranty).

Therefore, we have the 30-day time limit in place to protect from this edge case.

### Customizing the 30-Day Period for Lifetime Licenses[​](#customizing-the-30-day-period-for-lifetime-licenses "Direct link to Customizing the 30-Day Period for Lifetime Licenses")

While we recommend keeping the 30-day period as is, you can customize it in the [Developer Dashboard](https://dashboard.freemius.com/).

1. Navigate to the desired product.
2. Go to the **Plans** → **Prorated Discount** tab.
3. Update the **Lifetime License Proration Period** to your desired number of days. You can also set it to **Unlimited** to always provide a proration discount for lifetime plan updates.

## Proration with Coupons[​](#proration-with-coupons "Direct link to Proration with Coupons")

When updating a plan with a percentage-based coupon, the *proration* discount will be calculated first, and the coupon discount will apply to the discounted price as the last discount.

## In-Dashboard Plan Update[​](#in-dashboard-plan-update "Direct link to In-Dashboard Plan Update")

When a customer updates their plan within their WP Admin on a website where they’ve already activated it, the license will automatically be recognized by the checkout, and the user will be presented with the following options:

If the 1st option is selected, the purchase will be *prorated*, as described in the *proration* algorithm above.

warning

If the account owner of the installed product is different than the license owner, there’s no way to update the plan and the only option is to purchase another license!

## Freemius Checkout Plan Update[​](#freemius-checkout-plan-update "Direct link to Freemius Checkout Plan Update")

When a customer is trying to update their plan from your website, the loaded checkout will include the following label:

This option will enable the customer to enter their license key. Once the license key is verified, the purchase will be *prorated* as described in the *proration* algorithm above.