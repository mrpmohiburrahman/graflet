Release notes — it’s been a while!

We’re thrilled to announce the latest additions to our platform to further empower software makers to build and grow successful businesses.

Here’s a list of what’s new and a brief explanation of how each new feature or enhancement helps you better your business:

## Sales and Analytics Dashboard: New Features, Updates, and Metrics

With these new additions, software makers have deeper, more intelligent analytics for sales performance and audience demographics.

### New Audience Analytics Metric: Total Installs

In the past, determining the number of active installations or sites for a plugin was prone to error due to the reliance on **Activations** and **Deactivations** events. Understanding this limitation, we have implemented a more effective and accurate metric to provide software makers with comprehensive insights into their user bases.

Here’s why the **Total Installs** feature is a valuable metric to track:

#### Accurate Calculation of Active and Abandoned Installs

- By leveraging our new metric, you gain a precise calculation of your total active and abandoned installations
- We’ve also added a category called **Uninstalled Installs** to give software makers a more granular understanding of how many products have been uninstalled manually against how many have been abandoned due to reasons such as abandoned sites and erased databases

<!--THE END-->

![Total Installs chart with new Uninstalled category in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/total-installs-chart-with-new-uninstalled-category-in-freemius-developer-dashboard.png)

- In the lifetime data section, the Total Installs metric is also used to give an accurate birds-eye view of the product’s current active installs from sites that opted in

![Improved Opted-In Active Installs metric in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/improved-opted-in-active-installs-metric-in-the-freemius-developer-dashboard.png)

### Average Order Value (AOV) Chart

The Average Order Value chart equips software makers with insights into the average revenue generated per order, enabling you to optimize pricing strategies and adjust marketing and sales tactics according to fluctuations.

- You now get your revenue per order accurately with Freemius. This includes subscription renewals, lifetime purchases, and paid trials

<!--THE END-->

![Average Order Value AOV metric card in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/average-order-value-aov-metric-card-in-the-freemius-developer-dashboard.png)

- You can also easily track changes in AOV over selected periods on the Sales Analytics page to get a better understanding of how it’s evolved:

![Average Order Value AOV metric chart in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/average-order-value-aov-metric-chart-in-the-freemius-developer-dashboard.png)

### Net Payments and Transactions Chart: Improved Tracking Accuracy

We’ve done some housekeeping and cleared up any confusion related to the first legend of the **Net Payments & Transactions** chart Initially, it was labeled as **New Subscriptions** which understandably caused some puzzlement as the metric was showing the first payment of a subscription.

As many software makers know, if you’re offering a paid trial, the first payment of a subscription can come weeks later.

- We have updated the **Net Payments and Transactions** chart to provide clarity on the **Subscription 1st Payments** metric, avoiding any confusion
- This improvement ensures that you can track and analyze your payments more accurately, especially for products with paid trials

![Updated Net Payments chart in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/updated-net-payments-chart-in-the-freemius-developer-dashboard.png)

### Know Your Audiences on a Deeper Level: Geolocation-Based Payments Distribution Chart

- We now make it possible to gain insights into the total distribution of payments by country, helping you identify where your audience is concentrated
- Use this data to make informed decisions on targeting your marketing efforts, such as content translation and paid ads, to reach your global audience effectively:

![Geo-Distribution Payments chart in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/geo-distribution-payments-chart-in-the-freemius-developer-dashboard.png)

Freemius is now the only platform on the market to offer software makers the ability to process VAT refunds. We’ve also enhanced the UX for buyers and streamlined the process with a behind-the-scenes implementation to ensure makers don’t lose out on gateway fees.

Let’s dig into the enhancements:

### Simplified VAT Refunds: Reduced Steps (and Headaches)

- We now support VAT refunds against a valid VAT number, right from the refund dialog. This provides a simple, effective solution for when the reverse charge schema wasn’t applied because a user forgot to input their VAT number
- A significant headache for our software makers community is gone!

![VAT Refund Process in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/vat-refund-process-in-the-freemius-developer-dashboard.png)

Please note:

- We currently only support EU/UK VAT refunds for now (US sales tax refund support for exempt entities is coming soon!)
- Software makers must supply the customer’s valid VAT number for the refund to take effect
- If the payment is associated with a subscription, the subscription will be updated automatically to exempt taxes for renewals

## Deployment Mechanism Improvements

Our [Version Deployment feature](https://freemius.com/help/documentation/selling-with-freemius/deployment/) is a robust tool for freemium software products that automatically generates a free product version, stripped of any paid logic.

It’s also one of the main reasons software makers choose Freemius, and it’s now even more powerful.

### Freemius Deployment Now Supports PHP 8.2

- Our Version Deployment feature now supports PHP syntax up to version 8.2 to ensure compatibility with the latest software developments

![Version Deployment in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/05/version-deployment-in-the-freemius-developer-dashboard.png)

## Checkout Reskinning and General Improvements

An update years in the making!

Giving our legacy Checkout a “from the ground up” functional redesign and a fresh, modern coat of paint was on the cards for a long time, but it kept getting pushed out due to more pressing commitments.

No more!

On February 18th, we [rolled out the new Checkout for everyone](blog-changelog-enabled-the-new-checkout-style-by-default.md) and called on our developers to let the legacy version have its final curtain call. In many ways, the process worked because our software makers community helped guide many critical decisions with meaningful feedback as we presented new iterations.

Check out this side-to-side comparison that proves there’s power in collective effort :

![Side-by-side comparison of the Freemius legacy Checkout and new Checkout](https://freemius.com/blog/wp-content/uploads/2024/05/side-by-side-comparison-of-the-freemius-legacy-checkout-and-new-checkout.png)

Out with the old, in with the new: a side-by-side comparison of the legacy and new Checkouts

Feel free to play around with the Live Demo [right here](https://checkout.freemius.com/mode/dialog/plugin/10041/plan/17132/)!

For more information on the custom CSS migration, beta testing phase, and other UI/UX improvements such as our Dunning app reskinning and improved optional inputs, please check out (ha!) our [changelog on Phase 1’s rollout](blog-changelog-checkout-redesigning-phase-1-features-migration-guide.md).

### Roadmap

- In Phase 2, we will introduce a two-column layout and tweak and simplify the UI/UX based on data and feedback to further enhance the Checkout’s performance for software makers and their revenue streams
- Check out the progress:

![Freemius Phase 2 Checkout](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-phase-2-checkout.png)

## SaaS-Related Checkout Improvements

As part of our gradual expansion to supporting SaaS businesses, we’ve implemented the following improvements to our Checkout.

### Introducing Licensing Units

- Since SaaS users pay for resources like API Credits, Users, Storage, etc., labels like “Single Site License” aren’t logical at Checkout
- In collaboration with SaaS creators, we are introducing new license units — such as “Credit” — to improve the “SaaS” logic of the Checkout and ensure we’re helping our makers cater to as wide an audience as possible

<!--THE END-->

![Freemius Checkout License Units for SaaS](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-checkout-license-units-for-saas.png)

- As you can see in the screenshot, we also removed the word **License** from the dropdown because licenses are not a thing with SaaS.
- Correspondingly, the option to renew an existing license was removed
- To avoid confusion, we renamed the **Lifetime** billing cycle to **One Time**, as one-time payments for a SaaS business typically mean purchasing a specific amount of resources

### Post-Purchase Message Customization

- Maintaining a consistent tone of voice is crucial for cutting through the clutter and helps to convince customers you’re authentic, making them more likely to return
- We’ve added the capability to customize the message shown after payments because SaaS requires different post-purchase instructions
- This feature is still in beta — if you’re a software maker using Freemius and want to change your post-purchase message, [please reach out to us](https://freemius.com/cdn-cgi/l/email-protection#166563666679646256706473737b7f63653875797b).

![Freemius post-purchase message improvements for SaaS](https://freemius.com/blog/wp-content/uploads/2024/05/freemius-post-purchase-message-improvements-for-saas.png)

## That’s a Wrap

If you’d like to discuss any of the features and enhancements mentioned here, or have any requests or questions about Freemius in general, [reach out to us here](https://freemius.com/cdn-cgi/l/email-protection#f0838580809f8284b0968295959d998583de939f9d).

For a deeper dive into the technicalities, [read our changelog](https://freemius.com/changelog/) (updated weekly).