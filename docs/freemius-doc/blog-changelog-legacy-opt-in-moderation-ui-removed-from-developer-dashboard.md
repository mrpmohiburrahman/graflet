[Changelog](https://freemius.com/changelog/) / Legacy Opt-In Moderation UI Removed from Developer Dashboard

Our [Freemius WordPress SDK](help-documentation-wordpress-sdk.md) offers flexibility to existing product owners by allowing them to choose [what percentage of users will see the Opt-In screen](help-documentation-wordpress-sdk-integrating-freemius-sdk.md#configuration_for_opt_in_moderation_array). This has been a great tool for gradually migrating from a legacy system to Freemius without impacting all users at once.

Previously, this configuration was available through the Developer Dashboard. However, in alignment with `wordpress.org` guidelines, we had already [moved this control](blog-release-notes-wordpress-sdk-connectivity-test-stopped.md) from our API side into the WordPress SDK itself.

Today, we’re officially retiring the old UI in the Developer Dashboard that allowed configuring these legacy settings.

[![Moderation UI update for Freemius WordPress SDK](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-wp-sdk-opt-in-moderation-ui-1024x443.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-wp-sdk-opt-in-moderation-ui.png)

We had kept this UI active for a while since it takes time for our makers to update to the latest SDK versions. But now, with the majority already migrated and the legacy UI creating confusion for newer makers, we’ve decided to replace the interface with a deprecation notice. In the future, we plan to completely remove it.