[Changelog](https://freemius.com/changelog/) / Refreshed SDK Integration UI – Now with Composer Support

With the release of [**WordPress SDK 2.11.0**](https://github.com/Freemius/wordpress-sdk/releases/tag/2.11.0), we’ve revamped our **SDK Integration UI** to make it clearer and align with the latest WordPress.org guidelines.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-location-ui-dropdown-1024x435.png)](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-location-ui-dropdown.png)

Simply navigate to the **SDK Integration** page to check out the new UI. The first step now asks how you’d like to integrate the **Freemius WordPress SDK** into your project. You can choose from the following options:

1. **Manual** – You need to download the SDK from our GitHub repository and manage updates manually.
2. **Composer** – The SDK is downloaded and managed automatically through the package manager.

Once you make a selection, the UI will display the relevant instructions and code snippets.

### Choosing Composer Integration

If you’re already using **Composer** for your project, it makes sense to use the same package manager to install the **Freemius WP SDK**. As of **SDK [version 2.10.1](blog-changelog-do-not-change-sdk-v2-10-1-directory-to-vendor.md)**, Composer auto-loading is fully supported. To use Composer integration, ensure that you’re running at least this version.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-composer-integration-1024x598.png)](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-composer-integration.png)

If you’ve been using the old integration method (where the SDK is placed in the **main** folder of your plugin) and want to switch to Composer, please follow the instructions below.

### Migrating from the old integration method

If you’ve been using Freemius for a while, you might have noticed that we now require placing the SDK inside the `vendor/freemius` directory. This change aligns with **WordPress.org** guidelines, which recommend placing all third-party code inside the `vendor` directory.

Previously, we instructed developers to place the SDK directly inside the main folder of their plugin/theme. This is now reflected in the UI, where a **“Legacy”** option is available in the dropdown.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-legacy-location-1024x555.png)](https://freemius.com/blog/wp-content/uploads/2025/02/sdk-legacy-location.png)

Unfortunately, changing the SDK location isn’t straightforward due to a bug in SDK versions prior to **2.11.0**. To update the SDK location in your product, follow these steps:

1. **Release a version with the SDK location unchanged**, but ensure you’re using **SDK version 2.11.0 or later**.
2. **Mark this version as an [Incremental Release](help-documentation-release-management-incremental-update.md).**
3. **Release another version where you update the SDK location.**

To make this process easier, the last version you deployed with **SDK 2.11.0**, where the SDK was located in the root of your product, is automatically marked as **Incremental**.

For more detailed instructions, please refer to [our documentation](blog.md).