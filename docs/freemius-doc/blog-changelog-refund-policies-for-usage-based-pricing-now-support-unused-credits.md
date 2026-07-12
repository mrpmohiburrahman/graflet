[Changelog](https://freemius.com/changelog/) / Refund Policies for Usage-Based Pricing Now Support Unused Credits

We are releasing a new feature aimed at easing the life of AI SaaS makers. In the age of AI, consumptive or usage-based pricing has become increasingly popular, and Freemius supports this model out of the box (check our [video tutorial](help-documentation-saas-sdk-framework-nextjs.md#video-tutorial-and-advanced-example)).

We also understand that this pricing model can directly impact your refund policy. For example, if you are building a generative AI application with a subscription and top-up model, you may want to offer a money-back guarantee only for unused credits.

You can now configure this behavior directly from the [Freemius Developer Dashboard](https://dashboard.freemius.com/). Simply go to **Plans → Refund Policy** and enable the *“Limit refunds to unused credits for usage-based features”* checkbox.

[![Enable consumptive usage policy from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/01/consumptive-usage-ui-1024x765.png)](https://freemius.com/blog/wp-content/uploads/2026/01/consumptive-usage-ui.png)

Once enabled, Freemius will automatically include the appropriate clause in the refund policy generated for your product. You can read more about this behavior in our [documentation](help-documentation-selling-with-freemius-refund-policy.md#consumptive-usage).

Please note that this feature is currently available for SaaS-type products only. If you have other product types and a valid use case, feel free to reach out to our support team and we will be happy to explore enabling this option.