[Changelog](https://freemius.com/changelog/) / New Safeguard Against Uploading Premium Code to the WordPress.org Repository

We’ve been working closely with the [WordPress.org plugin review team](https://make.wordpress.org/plugins/handbook/the-team/) to implement a new safeguard in our system that prevents accidental uploading of premium versions of a product to the WordPress.org plugin repository.

Freemius’ [deployment mechanism](help-documentation-release-management-deployment.md) automatically creates a free, wp.org-compliant version of your product whenever you upload the premium version’s zip file. Makers are then expected to upload that free version to the official repository. However, mistakes can happen—sometimes the premium file gets uploaded instead. This often results in wasted time and back-and-forth with the Plugin Review team.

To solve this, and based on the review team’s recommendation, we’ve implemented a gatekeeping mechanism. Our integration code now includes a unique snippet: if that snippet is present, WordPress.org will block the submission and notify the maker of the error immediately.

[![Freemius SDK Integration snippet with gatekeeper](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-sdk-snippet-with-gatekeeper-1024x786.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-sdk-snippet-with-gatekeeper.png)

Meanwhile, Freemius’ deployment process automatically strips this snippet from the generated free version. This ensures that when the correct variant is uploaded, the submission proceeds smoothly without interruption.

Please note that no updates to the [WP SDK](https://github.com/Freemius/wordpress-sdk) are required for this rollout. We urge existing makers to immediately update the [integration snippet](help-documentation-wordpress-sdk-integrating-freemius-sdk.md) as shown in the Developer Dashboard to take advantage of this feature.