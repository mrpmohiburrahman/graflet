[Changelog](https://freemius.com/changelog/) / Improved WordPress Deployment Screen UI and Misc Documentation and UI Updates

## Deployment Page Improvements

Freemius offers a fully managed deployment solution for various WordPress products — including Plugins, Themes, Templates, Widgets, and more. Among the many features, we take care of Free and Premium version generation, license activation, and pushing updates to your buyers’ sites.

[![Deployment page UI - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-deployment-page-1024x766.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-deployment-page.png)

We realized that many of these features weren’t well surfaced in the deployment page UI. So, we’ve rolled out an update to better expose the most commonly used features, such as:

1. **Deployment Automation** – With our community-powered [GitHub Action](https://github.com/marketplace/actions/deploy-on-freemius) and other libraries.
2. **Paid and Free Version Generation** – Clearer information on how these versions are generated.
3. [**Release Management**](https://freemius.com/help/documentation/selling-with-freemius/deployment/#free_version_auto_generation_paid_logic_stripping_php_preprocessor) – Documentation on using [staged rollouts](help-documentation-release-management-staged-rollouts.md) and [incremental versions](help-documentation-release-management-incremental-update.md).
4. **Composer Integration** – Guidance on leveraging Freemius’ built-in Composer support.

We’ve also updated our [documentation](https://freemius.com/help/documentation/selling-with-freemius/deployment/) to reflect these enhancements. In addition, we’ve opened up the relevant [API endpoints](https://docs.freemius.com/api/deployments) to work with your product’s [Bearer Token](https://docs.freemius.com/api/section/bearer-token-auth) — allowing you to create new versions directly from your CI/CD pipeline.

We hope these updates help you streamline and automate your version deployments more effectively.

### License Unit Customization

We’ve published new [documentation covering license unit customization](help-documentation-selling-with-freemius-customize-license-unit-label.md) for SaaS and App products.

[![Freemius Pricing page showing Unit Label Customization](https://freemius.com/blog/wp-content/uploads/2025/05/license-unit-label-ui-1024x761.png)](https://freemius.com/blog/wp-content/uploads/2025/05/license-unit-label-ui.png)

To help surface this feature better, the pricing page UI now displays a tooltip near the license unit until it’s customized.

### Fixed Sidebar Drawers

We identified and resolved a UI regression affecting sidebar drawers in Dark Theme mode.

[![Freemius Sidebar Drawer UI in Dark Theme](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-sidebar-drawer-ui-1024x528.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-sidebar-drawer-ui.png)

The drawers now render correctly across both light and dark themes.