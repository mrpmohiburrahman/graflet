# How to Set up a Refund Policy for Your Product

Upon creating a new product on Freemius, please choose one of the 4 available refund policies that suits your product and customers best from:

* [No Refunds Policy](#no-refunds-policy)
* [Strict - "Money Back Guarantee"](#strict---money-back-guarantee)
* [Moderate - "Satisfaction Guarantee"](#moderate---satisfaction-guarantee)
* [Flexible - "Double Guarantee"](#flexible---double-guarantee)

tip

A clear refund policy can help build trust with your customers and reduce purchase anxiety.

## Configure the Refund Policy[​](#configure-the-refund-policy "Direct link to Configure the Refund Policy")

To set up the refund policy for your product, follow these steps:

1. Go to your product in the [Freemius Dashboard](https://dashboard.freemius.com/).
2. Click on the **Plans** Page.
3. Then select the **Refund Policy** tab.
4. Set a **Refund Time Period**.
5. Choose one of the available **Refund Policy** option in the dropdown field.
6. Click away to autosave the changes.

![Freemius Dev Dashboard - Product plans Refund Policy settings](/help/assets/ideal-img/freemius-dashboard-plans-refund-policy.2052552.480.png)

## Consumptive Usage[​](#consumptive-usage "Direct link to Consumptive Usage")

If your product includes **one-off or consumptive usage**, such as AI content generation, video or image processing, data exports, API calls, or any service where value is delivered instantly and cannot be undone, we strongly recommend enabling the following option in your refund policy settings:

![Check the Consumptive usage policy](/help/assets/ideal-img/consumptive-refund-policy.d1c510a.480.png)

note

This option is currently available for SaaS products only. If you have a different product type that includes consumptive usage, please contact our support team for assistance.

When this option is enabled:

* Any instance of the text *“full refund of the Purchase price”* will be adjusted to *“refund of the Purchase price only for any unused credits”* in the buyer-facing terms.
* An additional clarification will be automatically added to the purchase terms, making the refund boundaries explicit for buyers.

The following disclaimer will be added to the refund policy text shown to buyers:

> For clarity, once credits are consumed, they are non-refundable, as the underlying service has already been delivered. This includes, for example, executing an AI-powered action, generating content, processing data, or any other one-time or consumptive operation that uses credits.

This setting helps protect your business from abuse while keeping the refund policy fair and transparent for legitimate customers.

## Our Recommendation[​](#our-recommendation "Direct link to Our Recommendation")

Here are our recommendations depending on the type of product you offer:

* [SaaS and Apps](https://freemius.com/help/help/documentation/saas/setup-refund-policy/.md).
* [WordPress Plugins and Themes](https://freemius.com/help/help/documentation/wordpress/setup-refund-policy/.md).

## Available Refund Policies[​](#available-refund-policies "Direct link to Available Refund Policies")

Freemius supports several refund policy types, designed to fit different product models and risk profiles. Each policy determines what buyers see at checkout, how refund requests are handled, and how much flexibility you retain as a seller.

### No Refunds Policy[​](#no-refunds-policy "Direct link to No Refunds Policy")

A conservative refund policy that limits refunds to very specific cases and leaves most refund decisions at your discretion.

#### What it means for you (the seller)?[​](#what-it-means-for-you-the-seller "Direct link to What it means for you (the seller)?")

##### SaaS[​](#saas "Direct link to SaaS")

Refunds are only expected if the buyer requests them within 14 days before accessing or using the service. Once the service has been accessed, any refund request becomes discretionary. You can review the case, check usage, and decide whether to approve or decline the refund. This policy works best for SaaS products where onboarding is immediate and value is delivered quickly.

##### Consumable Credits[​](#consumable-credits "Direct link to Consumable Credits")

This policy is well suited for credit-based or usage-based products. Once credits are used, you are under no obligation to refund. Requests made before any usage can be approved, but anything after consumption is fully at your discretion.

##### Downloadable Software (e.g. plugins)[​](#downloadable-software-eg-plugins "Direct link to Downloadable Software (e.g. plugins)")

Refunds are only expected if the buyer has not downloaded or accessed the software. Once downloaded, refund requests can be declined unless you choose otherwise. This helps reduce abuse for easily copyable or one-time-use software.

tip

If you're using our [WordPress solution](https://freemius.com/help/help/documentation/wordpress/.md), you can verify whether a plugin or theme was downloaded by checking the customer's events and looking for the `plugin.premium.downloaded` event.

#### Fine Print[​](#fine-print "Direct link to Fine Print")

```
If You change Your mind about your Purchase and have not yet downloaded, used or otherwise accessed the paid Software, then, upon Your request within 14 days from the Purchase date, we will issue a full refund of the Purchase price.



Refund requests made after downloading, using or otherwise accessing the service (but before expiry of 14 days from the Purchase date) are handled on a case by case basis and are issued at our sole discretion.
```

### Strict - "Money Back Guarantee"[​](#strict---money-back-guarantee "Direct link to Strict - \"Money Back Guarantee\"")

A defect-based refund policy focused on product stability, not subjective satisfaction.

#### TLDR[​](#tldr "Direct link to TLDR")

Refund when the product had a bug/problem you couldn't resolve.

#### What will the buyer see?[​](#what-will-the-buyer-see "Direct link to What will the buyer see?")

> If during the next `{{ period }}` you experience an issue that makes the product unusable and we are unable to resolve it, we'll happily consider offering a full refund of your money.

#### What it means for you (the seller)?[​](#what-it-means-for-you-the-seller-1 "Direct link to What it means for you (the seller)?")

##### SaaS[​](#saas-1 "Direct link to SaaS")

Refunds are only required when a verified defect makes the service’s core functionality unusable and your support team cannot resolve it within the refund period. Feature gaps, unmet expectations, or third-party conflicts are not grounds for refunds. This policy works well for mature SaaS products with stable infrastructure and clear documentation.

##### Consumable Credits[​](#consumable-credits-1 "Direct link to Consumable Credits")

Refunds should generally apply only if a defect prevents the credits from being used at all. Once credits are successfully consumed, refunds are typically not applicable, even if the buyer is unhappy with the outcome.

##### Downloadable Software (e.g. plugins)[​](#downloadable-software-eg-plugins-1 "Direct link to Downloadable Software (e.g. plugins)")

Refunds apply only when a defect renders the software unusable and cannot be fixed with reasonable support. Incompatibilities with third-party themes, plugins, or environments are excluded.

#### Fine print[​](#fine-print-1 "Direct link to Fine print")

```
If, during the first `{{ refundPeriod }}` days following the purchase date, You experience a defect that makes the Software's material functions unusable, and following Your cooperation with our support team we are unable to resolve it, then following Your request we will issue a full refund of the Purchase price or provide you with replacement, non-defective product.



For clarity, any defect or lack of use arising from a conflict or incompatibility with a third party product, software or services, is not covered by this policy, and nor are missing Software features.
```

### Moderate - "Satisfaction Guarantee"[​](#moderate---satisfaction-guarantee "Direct link to Moderate - \"Satisfaction Guarantee\"")

A balanced refund policy that covers both defects and reasonable dissatisfaction, while still requiring an attempt to resolve issues.

#### TLDR[​](#tldr-1 "Direct link to TLDR")

Refund when missing a feature, didn't work as expected, or had a problem you couldn't resolve (including 3rd party issues).

#### What will the buyer see?[​](#what-will-the-buyer-see-1 "Direct link to What will the buyer see?")

> If over the next `{{ refundPeriod }}` days you are unhappy with our product or have an issue that we are unable to resolve, we'll happily consider offering a 100% refund of your money.

#### What it means for you (the seller)?[​](#what-it-means-for-you-the-seller-2 "Direct link to What it means for you (the seller)?")

##### SaaS[​](#saas-2 "Direct link to SaaS")

Refunds may be requested for missing features, usability issues, or defects, as long as the buyer has worked with your support team to try to resolve them. This policy gives you a chance to save the customer before a refund is issued. It is a good fit for growing SaaS products where onboarding and expectations still vary.

##### Consumable Credits[​](#consumable-credits-2 "Direct link to Consumable Credits")

Refunds may apply only if credits could not reasonably be used due to product issues. Once credits are consumed successfully, refunds are generally not expected, even if the buyer is dissatisfied with the results.

##### Downloadable Software (e.g. plugins)[​](#downloadable-software-eg-plugins-2 "Direct link to Downloadable Software (e.g. plugins)")

Refunds may be granted for defects or incompatibilities, including third-party conflicts, provided the issue cannot be resolved with support. This is more generous than the Strict policy and may slightly increase refund volume.

#### Fine print[​](#fine-print-2 "Direct link to Fine print")

```
If, during the first `{{ refundPeriod }}` days following the Purchase date, You are not satisfied with the Software due to missing features or due to a defect that makes the Software’s functions unusable (including defects arising from a conflict or incompatibility with a third party product, software or services), and following Your cooperation with our support team we are unable to resolve the issue, then following Your request we will issue a full refund of the Purchase price.
```

### Flexible - "Double Guarantee"[​](#flexible---double-guarantee "Direct link to Flexible - \"Double Guarantee\"")

The most buyer-friendly refund policy, designed to maximize conversions and reduce purchase anxiety.

#### One liner[​](#one-liner "Direct link to One liner")

Risk free, no questions asked refund.

#### What will the buyer see?[​](#what-will-the-buyer-see-2 "Direct link to What will the buyer see?")

> If you don't like our product over the next `{{ refundPeriod }}` days, we'll happily refund 100% of your money. **No questions asked.**

#### What it means for you (the seller)?[​](#what-it-means-for-you-the-seller-3 "Direct link to What it means for you (the seller)?")

Any refund request made within the refund period should be honored, regardless of usage or reason.

##### SaaS[​](#saas-3 "Direct link to SaaS")

This policy is best suited for SaaS products with low marginal costs and strong onboarding, where refunds are rare in practice.

##### Consumable Credits[​](#consumable-credits-3 "Direct link to Consumable Credits")

This policy should be used with caution for credit-based products. Many sellers pair it with limitations such as refunds for unused credits only, or disable it entirely for consumptive use cases to prevent abuse.

##### Downloadable Software (e.g. plugins)[​](#downloadable-software-eg-plugins-3 "Direct link to Downloadable Software (e.g. plugins)")

Refunds are expected on request within the refund period, even after download. This policy can significantly improve conversion rates, but may also increase refund volume, especially for one-time-use plugins.

#### Fine print[​](#fine-print-3 "Direct link to Fine print")

```
If, during the first `{{ refundPeriod }}` days following the Purchase date, You are not satisfied with the Software for any reason whatsoever (no questions asked) and notify us that You would like to cancel Your Purchase, we will issue a full refund of the Purchase price.
```

## Refunds don't have to end the relationship[​](#refunds-dont-have-to-end-the-relationship "Direct link to Refunds don't have to end the relationship")

After processing a refund, consider reaching out and asking for feedback. While refunds are rarely anyone's favorite outcome, handling them quickly and respectfully can leave a positive impression and even build long-term loyalty.

For more ideas on turning refunds into learning opportunities, see [How to Win Customer Loyalty with Your Refund Process](https://returngo.ai/improve-customer-loyalty-with-returns/#:~:text=Process%20Returns%20Quickly\&text=If%20the%20returns%20process%20is,returns%20will%20improve%20customer%20loyalty).

## Disputes & Chargebacks[​](#disputes--chargebacks "Direct link to Disputes & Chargebacks")

A clear refund policy helps reduce disputes, but it cannot fully eliminate them.

Setting the right refund policy is an important step in protecting your business. However, some customers may still choose to dispute a payment through PayPal, their bank, or their credit card provider, regardless of the refund policy you've defined.

In those cases, [dispute or chargeback fees](https://freemius.com/help/help/documentation/getting-started/our-pricing/.md#dispute-and-chargeback-fees) may apply, and Freemius may need to step in to review and handle the case. Each dispute is evaluated individually, based on the circumstances, the selected refund policy, and the evidence available.
