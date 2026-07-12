[Changelog](https://freemius.com/changelog/) / New Feature: Billing Selector UI for Checkout

This week, we’re introducing one of the most anticipated features for our Checkout. Last year, we released [Phase 2 of the Checkout](blog-new-freemius-checkout-drive-conversions-increase-sales-price.md#phase_two), which underwent a major redesign. At that time, we removed the legacy Billing Cycle UI in favor of a more compact Upsell UI.

However, we’ve received feedback requesting the return of the billing selector UI. This feature is particularly useful for makers using Freemius Checkout directly, without a dedicated pricing page. It provides buyers with more flexibility to select their preferred billing cycle at the time of purchase.

[![Freemius Checkout Billing Selector UI](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-new-billing-selector-ui-1024x545.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-new-billing-selector-ui.png)

We’ve listened to your feedback and are now introducing an optimized and visually enhanced Billing Cycle UI that complements the new Checkout experience.

This feature is **not enabled by default**. To activate it, add the following URL parameter to your Checkout URL:

```
?billing_cycle_selector=responsive_list
```

Alternatively, if you’re using the Checkout JS SDK, you can enable it with the following configuration:

```
const handler = new Checkout({
  billing_cycle_selector: 'responsive_list',
});
```

### Configuration Options

The `billing_cycle_selector` parameter accepts the following values:

1. **`responsive_list`** – Displays billing cycles in a smart list that adapts to available space.
2. **`dropdown`** – Shows a dropdown UI, allowing buyers to select their preferred billing cycle.
3. `list` – Same as `responsive_list` but always show up vertically.

If none of the values are present the UI will not show up. Read more details below.

### Rendering a Responsive List

Our recommendation is to use the `responsive_list` option. You can do so by setting the parameter value to `responsive_list` or simply `true`.

[![Responsive list of Billing Cycle in Freemius Checkout ](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-responsive-list-billing-ui-1024x723.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-responsive-list-billing-ui.png)

This will display all available billing cycles upfront. If only two billing cycles are available, they will appear in a horizontal layout to save space.

[![Flat vertical list of Billing cycle UI in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-list-1024x921.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-list.png)

If you prefer a **vertical list**, you can use `list` instead of `responsive_list`.

### Dropdown UI

If you want to minimize vertical space usage, set the parameter to `dropdown`.

[![](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-dropdown-1024x450.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-dropdown.png)

This will render a single item that buyers can click to open a dropdown menu for selection.

[![Billing Cycle dropdown UI in open state - Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-dropdown-open-1024x801.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-billing-cycle-dropdown-open.png)

### Adjustment with Upsells

Enabling the billing cycle UI will **automatically disable annual and lifetime upsells**.

[![Disabled upsells when Billing Cycle UI is shown](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-upsell-1024x591.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-checkout-upsell.png)

As always, we’re building this feature with our community. If you’d like to discuss anything, feel free to join our Slack or reach out to our support team.