---
title: "Showing a Dedicated UI for Changing the Billing Cycle"
url: "https://freemius.com/help/documentation/checkout/features/billing-cycle-selector-ui/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 285
---

The billing selector UI is a feature that provides buyers with more flexibility to select their preferred billing cycle at the time of purchase.

This feature is particularly useful for makers using Freemius Checkout directly, without a dedicated pricing page.

## Activation[​](#activation "Direct link to Activation")

**The billing selector UI is not enabled by default**. To activate it, add the following URL parameter to your Checkout URL:

```text
?billing_cycle_selector=responsive_list
```

Alternatively, if you’re using the Checkout JS SDK, you can enable it with the following configuration:

```js
const handler = new Checkout({
  billing_cycle_selector: 'responsive_list',
});
```

note

Enabling the billing cycle UI will automatically disable [annual](help-documentation-checkout-features-upsell-toggles.md#annual-upsell) and [lifetime](help-documentation-checkout-features-upsell-toggles.md#one-off-or-lifetime-upsell) upsells.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

The `billing_cycle_selector` parameter accepts the following values:

1. `responsive_list` which displays billing cycles in a smart list that adapts to available space.
2. `list` which works similar as `responsive_list` above will display the options **vertically**.
3. `dropdown` which shows a dropdown UI, allowing buyers to select their preferred billing cycle.

### Rendering a Responsive List[​](#rendering-a-responsive-list "Direct link to Rendering a Responsive List")

Use the `responsive_list` option to display all available billing cycles upfront. If only two billing cycles are available, they will appear in a horizontal layout to save space.

If you prefer a vertical list, you can use `list` instead of `responsive_list`.

### Rendering a Dropdown UI[​](#rendering-a-dropdown-ui "Direct link to Rendering a Dropdown UI")

If you want to minimize vertical space usage, set the parameter to `dropdown`. This will render a single item that buyers can click to open a dropdown menu for selection.

tip

Our recommendation is to use the `responsive_list` option. You can do so by setting the parameter value to `responsive_list` or simply `true`.