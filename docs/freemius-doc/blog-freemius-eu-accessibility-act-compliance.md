The EU Accessibility Act (EAA) is now in effect and we’ve made key updates to help software makers stay on the right side of the law without writing a single line of code.

When you build with Freemius, components like the Checkout and Customer Portal become core to your user experience — which means their EAA accessibility helps safeguard your overall compliance.

This is why we’ve made the two most important user-facing touchpoints fully accessible, inclusive, and ready out of the box.

But before we dive into how, some clarity on the new directive:

## What the EU Accessibility Act Means for Software Makers

The [EU Accessibility Act](https://digital-strategy.ec.europa.eu/en/policies/web-accessibility) is a regulation that requires digital products and services sold in the European Union to be accessible to people with disabilities.

As of **June 28, 2025**, compliance is no longer optional…

**It’s mandatory**.

If you sell software, SaaS tools, WordPress plugins, or any other consumer-facing digital product in the EU, this legislation applies to you. The new law is based on [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/) standards, which include practical accessibility requirements like:

- Full keyboard navigation (no mouse needed)
- Screen reader compatibility
- Clear content structure and labels
- Sufficient color contrast
- Accessible forms and error messages
- Alt text for images and icons

You’re expected to comply, even if you’re a solo software maker or small team. Failure to do so can result in:

- Legal complaints or removal from EU markets
- Damaged brand reputation and trust
- Lost sales from frustrated or excluded users

This new rule is not something unique to the EU. Countries like the United States, Canada, the UK, Australia, and South Korea already have similar accessibility laws in place — all grounded in the same WCAG standards. In short: accessible design is no longer optional. It’s fast becoming the global standard.

Staying ahead in the software game means building for **everyone, everywhere**.

***Want the full EAA breakdown before diving into our accessibility enhancements?*** 

*Check out [our deep-dive article](https://freemius.com/blog/eu-accessibility-act-software-compliance/). It covers the law, common misconceptions, practical examples, and insights from accessibility experts.*

Now to the updates:

## Freemius Checkout: Seamless, Compliant, and Inclusive

The full Freemius Checkout experience, including popup, embedded, and full-screen versions, is now fully compliant with EAA.

No huge changes. No disruptions. Just a better, accessibility-friendly checkout experience — already live and ready to go:

### Real Assistive Tech Guided Our Decisions

The Freemius Checkout was manually audited with screen readers like VoiceOver, NVDA, and JAWS to ensure it works smoothly across real-world assistive technologies, and not just in theory.

Watch the upgrades in action:

[https://freemius.com/blog/wp-content/uploads/2025/06/Checkout-Voice-a11y.mp4](https://freemius.com/blog/wp-content/uploads/2025/06/Checkout-Voice-a11y.mp4)

### Best-in-Class Keyboard Navigation

This matters more than many realize — [a vast majority](https://webaim.org/projects/screenreadersurvey9/) of users with motor impairments rely on keyboard-only navigation to browse and buy online.

The entire checkout flow now works seamlessly without a mouse. Users can tab through all elements, use arrow keys to move within dropdowns, press Enter to select, and hit Esc to close menus. No focus traps and just like native controls.

[https://freemius.com/blog/wp-content/uploads/2025/06/Checkout-Keyboard-Navigation.mp4](https://freemius.com/blog/wp-content/uploads/2025/06/Checkout-Keyboard-Navigation.mp4)

### Better Contrast Ratio and Focus States

We’ve adjusted color schemes and font sizes across the Checkout to meet best practices and industry standards.

Buttons, links, and other interactive elements now feature clearly defined focus states, making navigation easier for users relying on keyboards or other assistive technologies.

[![Refreshed Checkout design with improved color schemes and font sizes](https://freemius.com/blog/wp-content/uploads/2025/07/refreshed-checkout-design-with-improved-color-schemes-and-font-sizes.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/refreshed-checkout-design-with-improved-color-schemes-and-font-sizes.jpeg)

### Real-Time Feedback via ARIA Live Regions

From pricing calculations to form validation, the Freemius Checkout updates in real-time. For this reason, we’ve added [ARIA live regions](https://www.a11y-collective.com/blog/aria-live/) so screen readers can detect and display content changes as they happen.

[![Freemius Checkout with ARIA live regions](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-aria-live-regions.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-aria-live-regions.jpeg)

Validation errors are now clearly described with accessible roles, helping users understand what went wrong without needing to guess or tab around.

[![Freemius Checkout with clearly described validation errors](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-clearly-described-validation-errors.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-clearly-described-validation-errors.jpeg)

### Accessible Form Components

Whether native or custom, we refined every form element to meet accessibility best practices. Labels and descriptions are now properly applied, visual states for hover, focus, and errors are clearly defined, and components like listboxes, landmarks, and buttons follow [WAI-ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/patterns/).

[![Freemius Checkout with refined form elements](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-refined-form-elements.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-with-refined-form-elements.jpeg)

The result is a form experience that’s more intuitive, predictable, and easier to navigate — whether using a screen reader, keyboard, or any tool in between.

### Updated Checkout JS SDK

The [JavaScript SDK](https://github.com/Freemius/freemius-checkout-js/) now comes packaged with a few key accessibility enhancements:

- The close (×) button is now always visible — not just on hover
- The modal overlay and iframe include appropriate `role` and `title` attributes
- Focus now returns to the active element when the modal closes

[![Updated Checkout JS SDK with a few key accessibility enhancements](https://freemius.com/blog/wp-content/uploads/2025/07/updated-checkout-js-sdk-with-a-few-key-accessibility-enhancements.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/updated-checkout-js-sdk-with-a-few-key-accessibility-enhancements.jpeg)

If you’re using the **hosted file version** `(https://checkout.freemius.com/js/v1/)` you’re already up to date. Using the **npm package**? Make sure to pull the latest version to get all the benefits.

And why stop the accessibility enhancements at the Checkout?

## Freemius Customer Portal: Fully Accessible and Freshly Polished

Mandatory requirements and best practices? The Freemius Customer Portal now meets WAI accessibility guidelines on both fronts, which is awesome news for makers who embed the portal on their sites.

Changes include improved keyboard navigation, enhanced screen reader support, clearer focus states, proper color ratios, and fully accessible interactive elements for all users.

[![Improved Freemius Customer Portal](https://freemius.com/blog/wp-content/uploads/2025/07/improved-freemius-customer-portal.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/improved-freemius-customer-portal.jpeg)

Your users can now access and manage their purchases, subscriptions, [order history](help-documentation-users-account-management-orders-history.md), and license details with ease, regardless of their device or assistive technology.

[![Customer Portal Order History section](https://freemius.com/blog/wp-content/uploads/2025/07/customer-portal-order-history-section.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/customer-portal-order-history-section.jpeg)

### Subtle Visual Refresh with Accessibility in Mind

Alongside the accessibility improvements, our Customer Portal has been given a soft rebranding. You’ll notice:

- Clean new typography
- Updated button styles and color palette
- Improved spacing and content hierarchy

Everything works exactly as before. It just looks and feels better.

The above sets the tone for something bigger, too: a full Customer Portal rebrand/modernization in the coming months!

[![Freemius Customer Portal with soft rebranding](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-customer-portal-with-soft-rebranding.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-customer-portal-with-soft-rebranding.jpeg)

This update is already live and working, and we took care to avoid breaking any existing custom CSS overrides. So, no changes needed from your end.

## What These Accessibility Enhancements Mean for Software Makers (And Why They Matter)

With both the Freemius Checkout and Customer Portal now fully accessibility-compliant, Freemius makers are in a stronger position to meet the requirements of the EU Accessibility Act (without needing to change a single line of code).

Just like with [GDPR](blog-gdpr-wordpress-plugin-theme.md), accessibility compliance isn’t only about what you build. It also depends on the services and components you use. We’ve done the work to make sure Freemius supports your compliance goals, not stands in the way.

In the EU alone, [around 87 million people](https://www.inclusion-europe.eu/european-commission-presents-strategy-for-the-rights-of-persons-with-disabilities-2021-2030) — roughly 1 in 5 — have some form of disability, highlighting why accessible design is no longer optional.

This goes beyond regulation. Improving accessibility makes your product better for everyone:

- It removes friction for users relying on screen readers, keyboard navigation, or zoomed-in views
- It improves clarity, structure, and usability, even for users without disabilities
- It reflects the kind of product experience that builds trust and keeps people coming back

This update didn’t just check a box. It opened a door to more opportunities.