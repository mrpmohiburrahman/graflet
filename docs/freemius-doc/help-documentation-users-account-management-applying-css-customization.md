---
title: "Applying CSS Customization to the Customer Portal"
url: "https://freemius.com/help/documentation/users-account-management/applying-css-customization/"
source: "docs"
section: "Docs"
category: "Customer Portal"
scraped_at: "2026-04-09T19:58:43+06:00"
word_count: 331
---

You can customize the appearance of the Freemius Customer Portal with CSS to match your brand and site design. The portal supports custom style sheets and CSS variable overrides for flexible theming.

## How CSS Customization Works[​](#how-css-customization-works "Direct link to How CSS Customization Works")

- The Customer Portal is embedded via an iframe or direct link, and you can apply custom CSS by specifying a style sheet URL in the Freemius Developer Dashboard.
- The portal uses CSS variables for colors, typography, and layout. Overriding these variables makes theme adjustments easy.

## Overriding CSS Variables[​](#overriding-css-variables "Direct link to Overriding CSS Variables")

Inspect the portal's root element using your browser's developer tools to discover available CSS variables.

Common variable groups include:

- `--fs-ds-theme-*`: Theme colors for major components
- `--fs-ds-typography-*`: Font families, sizes, and weights
- `--fs-ds-appearance-*`: Border radius, sizing, etc.

For example, to change the primary color and font family, add the following CSS:

```css
:root {
  --fs-ds-theme-primary: #6753ff;
  --fs-ds-typography-font-family: 'Open Sans', sans-serif;
}
```

## Adding Your Custom CSS[​](#adding-your-custom-css "Direct link to Adding Your Custom CSS")

1. Host your CSS file on a secure (HTTPS) server.
2. Log in to your [Freemius Developer dashboard](https://dashboard.freemius.com/).
3. Navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
4. Select your store by name.
5. Scroll down the menu and select the **Settings** page.
6. Under the Customer Portal sub-page, scroll to the **Customization** section.
7. Paste your stylesheet URL into the **Customer Portal CSS stylesheet** field.
   
   Your styles will then load and apply to the portal.

## Tips[​](#tips "Direct link to Tips")

- Always use the `:root` selector for global variable overrides.
- Monitor changes in the Customer Portal HTML to avoid breaking your custom styles.
- For advanced theming, combine variable overrides with custom CSS rules targeting portal elements.

warning

Major portal updates may affect your custom styles; review changes after each update.

If you have questions or need help with advanced customization, contact Freemius Support.