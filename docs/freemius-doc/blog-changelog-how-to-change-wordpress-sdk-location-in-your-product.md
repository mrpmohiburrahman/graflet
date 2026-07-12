[Changelog](https://freemius.com/changelog/) / How to change WordPress SDK location in your product

Starting with WordPress SDK 2.10.1, we introduced Composer support. What we didn’t realize at the time was that changing the SDK location in existing products could cause issues during updates. While this issue did not break any functionality, it still displayed error messages in the WordPress admin panel, confusing users.

To address this, we introduced a fix in SDK version 2.11.0. However, to completely avoid the issue, it is important to first release a version of your product with SDK 2.11.0 while keeping the SDK location unchanged. Once websites update to that version, any subsequent release where the SDK location is changed will work seamlessly.

So how do we ensure websites update to the correct version first? That’s where our recently deployed **Incremental Release** feature comes into play.

### Preparing your product for SDK location change

1. Upgrade the Freemius WordPress SDK to version 2.11.0.
2. **Do not** change the SDK location or integration method yet.
3. Release a new version of your product.
4. During the release process, choose **“Incremental Release.”**

[![](https://freemius.com/blog/wp-content/uploads/2025/02/choosing-incremental-release-1024x821.png)](https://freemius.com/blog/wp-content/uploads/2025/02/choosing-incremental-release.png)

This ensures that all websites first update to this version before receiving any later updates.

At this stage, you may notice that our system has already detected your intent and marked this release as **Incremental**. If you previously released a version of your product with SDK 2.11.0 in the past few weeks, this configuration may already be in place.

Once the first version with SDK 2.11.0 (and an unchanged SDK location) has been deployed and marked Incremental, you can release another version where you actually move the SDK to a new location. We strongly recommend:

1. Moving it to the `vendor/freemius` folder.
2. Using the Composer integration method.

The WordPress.org review team recommends placing any third-party code inside the `vendor` folder. You can also find updated integration instructions in our **Developer Dashboard.**

And that’s it! Now, all websites will follow the proper update path, ensuring users don’t encounter errors and that everything works seamlessly.

Additionally, if you’re interested in learning more about **Incremental Release,** you can read all about it [here](blog.md).