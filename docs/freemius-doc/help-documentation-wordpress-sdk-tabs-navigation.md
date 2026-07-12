---
title: "Tabs Navigation"
url: "https://freemius.com/help/documentation/wordpress-sdk/tabs-navigation/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 788
---

If you are worried about cluttering the WordPress admin menu, you can easily change the default navigation by implementing navigational tabs at the top of your plugin settings page.

This is especially relevant when your plugin settings page is a submenu. e.g. Under the top-level **Settings** WordPress menu item (`options-general.php`).

This is just one plugin. If you have multiple active plugins with similar subpages then the menu could quickly become very unsightly.

## How to Enable Tabs[​](#how-to-enable-tabs "Direct link to How to Enable Tabs")

To add support for navigational tabs simply add the following property to the generated SDK code snippet for your plugin.

```php
'navigation' => 'tabs',
```

warning

**Important:** This currently has to be done manually as it isn't automatically added when the SDK integration snippet is generated. Don't forget to re-add this whenever your SDK integration code snippet changes.

This displays Freemius pages as tabs instead of menu items.

By default, your plugin settings won't be displayed inside a dedicated tab. This needs to be added manually.

## Adding a Custom Tab[​](#adding-a-custom-tab "Direct link to Adding a Custom Tab")

To blend your plugin settings page in with the Freemius tabs you can add a custom tab with a little custom HTML.

warning

**Important:** For the tabs to work correctly you need to make sure your plugin settings are contained in a `div.wrap` element, which is considered [standard practice](https://developer.wordpress.org/plugins/settings/custom-settings-page/).

Modify your existing plugin settings markup to include the following HTML. Make sure you replace the placeholder link with a full link to your plugin settings page.

```html
<div class="wrap fs-section fs-full-size-wrapper">
  <h2 class="nav-tab-wrapper">
    <a href="#" class="nav-tab fs-tab nav-tab-active home">Settings</a>
  </h2>
  <!-- Plugin settings go here -->
</div>
```

As you can see Freemius automatically adds styles needed to blend in with core Freemius tabs (as long as you include the CSS classes in the snippet above).

You might notice that when you click on a Freemius tab (e.g. **Contact Us**) a submenu item is displayed under the plugin settings menu to indicate which tab is currently visible. No submenu is displayed for the main plugin settings page.

If you need to fit the tabs with your own styling you do have some flexibility. The minimum markup needed to integrate with Freemius tabs is:

```html
<div class="wrap">
  <h2 class="nav-tab-wrapper">
    <a href="#" class="nav-tab nav-tab-active">Settings</a>
  </h2>
  <!-- Plugin settings go here -->
</div>
```

Depending on the size and complexity of your plugin settings page you might occasionally see a slight 'blip' when the tabs are rendered. This can be due to the custom tab being displayed immediately, whereas the Freemius tabs are added via JavaScript a few milliseconds later.

This is not normally an issue but if it's noticeable then you can try hiding the tabs initially with CSS, and displaying via JavaScript once the Freemius tabs have finished loading.

CSS (add as inline style or via style sheet)

```css
h2.nav-tab-wrapper {
  display: none;
}
```

JavaScript (enqueue in footer)

```javascript
jQuery(document).ready(function ($) {
  document.querySelector('h2.nav-tab-wrapper').style.display = 'block';
});
```

## Adding a Custom Tab Via JavaScript[​](#adding-a-custom-tab-via-javascript "Direct link to Adding a Custom Tab Via JavaScript")

It's also possible to add a custom tab purely via JavaScript instead of HTML which has some inherent advantages.

Namely, it avoids the 'blip' issue completely when adding a custom tab with HTML as all tabs are rendered to the DOM *before* they're displayed. And almost no alterations are necessary to your existing plugin settings page markup.

The JavaScript code should be enqueued to run in the page footer (to ensure it runs after the Freemius tabs JavaScript), and *only* on the plugin settings page and Freemius pages (Account, Contact Us, Upgrade).

To help whitelist admin pages you can use the [Freemius Menu Slugs](https://github.com/Freemius/wordpress-menu-slugs-plugin) plugin to find the menu slugs.

Here's an example snippet to add a custom tab via JavaScript:

```javascript
jQuery(document).ready(function ($) {
  // add a 'Settings' tab via JS
  const navTabWrapper = $('.nav-tab-wrapper');
  const currentTabs = $('.nav-tab-wrapper a');
  let activeTab = '';
  if (!currentTabs.hasClass('nav-tab-active')) {
    activeTab = ' nav-tab-active';
  }
  navTabWrapper.prepend(
    '<a href="#" class="nav-tab fs-tab svg-flags-lite home' +
      activeTab +
      '">Settings</a>'
  );
});
```

Again, make sure you replace the placeholder link with a full link to your plugin settings page.

It's also recommended that you add the `fs-section fs-full-size-wrapper` classes to the `div.wrap` element to your plugin settings page to help blend in with Freemius tabs.

## Clearing the Freemius Cache[​](#clearing-the-freemius-cache "Direct link to Clearing the Freemius Cache")

When editing custom tab code you might occasionally come across your tab changes not being updated as expected for core Freemius tab pages (Account, Contact Us, Upgrade, etc.).

This is usually due to Freemius caching the page markup. To solve this simply clear the cache via the Freemius [debugging admin page](help-documentation-wordpress-sdk-debugging.md).