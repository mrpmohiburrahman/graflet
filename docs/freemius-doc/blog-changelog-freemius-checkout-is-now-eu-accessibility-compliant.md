[Changelog](https://freemius.com/changelog/) / Freemius Checkout is Now EU Accessibility Compliant

We’re excited to announce that the Freemius Checkout is now fully compliant with the [EU Accessibility Act](https://digital-strategy.ec.europa.eu/en/policies/web-accessibility), which comes into enforcement on **June 28th**. This means that by using Freemius Checkout, your website remains compliant with EU law.

[![Freemius Checkout fully EU accessibility act compliant](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout-1024x621.png)](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout.png)

But we didn’t stop at just the legal requirements. We’ve gone a few steps further by also implementing **recommended** accessibility best practices, making sure our Checkout delivers an inclusive and user-friendly experience for everyone.

Here are some of the key improvements we’ve made:

### Better Contrast Ratio & Focus States

We updated color schemes and font sizes to ensure compliance with [WCAG 2.2 Level AA](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum).

[![Checkout contrast and focus](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout-contrast-ratio-focus-1024x488.png)](https://freemius.com/blog/wp-content/uploads/2025/06/freemius-checkout-contrast-ratio-focus.png)

Additionally, all interactive elements like buttons and links now have clear focus states, supporting both keyboard and assistive tech navigation.

### Best Possible Keyboard Navigation

We audited and improved keyboard navigation across the entire Checkout experience.  There are no keyboard focus traps, and every component is now fully navigable using the keyboard, with relevant focus states clearly visible at all times.

### Proper ARIA Live Regions

Freemius Checkout is dynamic. Price calculations and form updates happen in real-time.  

[![Checkout live region with dynamic text](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-live-region-1024x751.png)](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-live-region.png)

We’ve added ARIA live regions to ensure screen readers can detect and announce content changes appropriately.

[![Checkout form validation with descriptive text](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-form-validation-1024x398.png)](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-form-validation.png)

All form validation errors are now *descriptive*, with appropriate ARIA roles applied.

### Accessible Form Components

[![Accessible form component](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-accessible-form-component-1024x580.png)](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-accessible-form-component.png)

We’ve audited all form elements, both native and custom, to ensure:

1. Proper use of labels and descriptions
2. Clear visual states for hover, focus, and errors
3. Conformance with [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/) (WAI-APG) for components like [listboxes](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/), [landmarks](https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/), and [buttons](https://www.w3.org/WAI/ARIA/apg/patterns/button/)

### Manual Audits and Support for Screen Readers

We’ve manually audited and optimized our Checkout experience to ensure it works seamlessly with screen readers including **VoiceOver (macOS/iOS)**, **NVDA**, and **JAWS**. You can watch a demonstration in the video below.

This update reflects our continued commitment to accessibility and inclusivity, ensuring that everyone, regardless of their browsing method, can interact with Freemius Checkout with confidence.

### Updated Checkout JS SDK

[![Accessible Checkout Overlay with Freemius JS SDK](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-overlay-accessibility-1024x517.png)](https://freemius.com/blog/wp-content/uploads/2025/06/checkout-overlay-accessibility.png)

Our [JavaScript SDK](https://github.com/Freemius/freemius-checkout-js/) has also received accessibility enhancements:

1. The close (`×`) button is now **always visible**, not just on hover
2. The modal overlay and iFrame includes appropriate \`role\` and \`title\` attributes
3. The active element is now focused back when the modal closes

If you are using the hosted version of the SDK (`https://checkout.freemius.com/js/v1/`) then no action is necessary from your side. If you’re using the npm package, then we urge that you update as soon as possible.

With these improvements wrapped up for the Checkout, our next focus is the Customer Portal.  

Stay tuned for further updates and if you notice any accessibility issues or have suggestions, reach out to our support team. We’d love to hear from you!