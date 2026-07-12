[Changelog](https://freemius.com/changelog/) / Support for Custom Bulk Pricing, Smarter Pricing UI, and API Page Improvements

This week we are releasing a set of UI/UX enhancements to our Developer Dashboard. These updates are tailored for SaaS makers but also bring benefits to our WordPress makers community, making configuration and integration smoother across the board.

## Smarter Pricing UI

We refined the [pricing input UI](help-documentation-saas-saas-plans-pricing.md#setting-up-plans) to be smarter, clearer, and adaptive to how you’re configuring your product.

For example, if you are configuring only a single pricing inside a plan, the UI will simply ask you to configure the billing cycles for that pricing.

[![Simple pricing UI in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-pricing-ui-simple-1024x267.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-pricing-ui-simple.png)

However, if you are configuring [multiple bulk units](help-documentation-saas-customize-license-unit-label.md) (like selling credits), the UI will adjust accordingly, as shown in the screenshot below.

[![Bulk Pricing UI in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-pricing-bulk-ui-1024x687.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-pricing-bulk-ui.png)

## Support for Custom Bulk Pricing

Previously, our system was limited to a preset list of unit options for [creating bulk pricing](help-documentation-saas-saas-plans-pricing.md#setting-up-plans).

[![Custom pricing creation mode in Freemius Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-bulk-unit-1024x711.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-bulk-unit.png)

Now we’ve introduced a new option called `Custom Unit...` (where the term `Unit` represents your [selling unit](help-documentation-saas-customize-license-unit-label.md) and is dynamic based on your configuration), which lets you define the exact number of units you want for bulk pricing. Simply click on the button and you will be presented a new dialog from where you can configure the pricing.

[![Custom configuration for bulk selling units in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-bulk-pricing-input-1024x1020.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-bulk-pricing-input.png)

This is especially useful for SaaS products selling consumable units such as credits or tokens.

## Plan Description is Back for the React Starter Kit

With the release of the [React Starter Kit](help-documentation-saas-sdk-react-starter.md), the Plan Description section is now back under plans.

[![Configure plan description from the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-plan-description-1024x565.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-plan-description.png)

If you configure the description, it will show up in the [Pricing Data API](https://docs.freemius.com/api/products/retrieve-pricing-table-data) endpoint as well as be rendered by the React Starter Kit.

[![React Starter Kit Pricing Table UI](https://freemius.com/blog/wp-content/uploads/2025/09/react-starter-kit-pricing-1024x511.png)](https://freemius.com/blog/wp-content/uploads/2025/09/react-starter-kit-pricing.png)

## Improved API & Keys Page

With the release of our [JS SDK](help-documentation-saas-sdk-js-sdk.md), we’ve also improved the **API & Keys** page under **Settings**.

Now, all the keys you need to communicate with Freemius are consolidated into a single page.

[![](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-api-integration-page-1024x855.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-dashboard-api-integration-page.png)

We’ve also added improved [usage examples](help-documentation-saas-sdk-js-sdk-installation.md#retrieving-keys-from-the-developer-dashboard) with ready-to-use, copy-pastable snippets for getting started quickly with our SDKs.