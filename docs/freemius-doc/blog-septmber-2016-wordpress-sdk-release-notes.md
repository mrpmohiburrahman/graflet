![](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)

These are the release notes for a major release (more than 80 commits) with a bunch of enhancements and one crucial license related bug fix for developers who monetize with Freemius.

## Bug Fixes

1. \[Major] There was a problem with the daily wp-cron execution for plugins and themes with a premium offering. This issue sometimes caused to a license expiration, even though payments were successfully processed. If you monetize with Freemius and your module supports monthly payments, I would highly recommend updating the SDK asap.
2. Submenu items are now inheriting permissions from the parent menu item (issue [#81](https://github.com/Freemius/wordpress-sdk/issues/81)).
3. Fixed discount calculations with annual and multi-site licensing (issue [#79](https://github.com/Freemius/wordpress-sdk/issues/79)).

We are finally loading Freemius translations using `load_plugin_textdomain()`. The SDK is fully translated into English and Italian (thanks to Alessandro Benassi), it would be awesome if you can help us [translating to additional languages](https://transifex.com/freemius/wordpress-sdk/).

## Deactivation Feedback Form Enhancements

1. The order of the uninstallation reasons is now randomized. By randomizing the order, if a subset of the users is just picking the 1st option, it will be equally distributed, and will help devs to identify the main uninstallation reasons by removing the noise.
2. Even if the user skipped the opt-in mechanism, we added an option to be identified when sending uninstallation feedback: [![uninstallation feedback form](https://freemius.com/blog/wp-content/uploads/2016/09/4ec6f5fe-80d3-11e6-9277-8dfe2c968e6b.png)](https://freemius.com/blog/wp-content/uploads/2016/09/4ec6f5fe-80d3-11e6-9277-8dfe2c968e6b.png)

This gives the ability to contact with users who deactivated and didn’t opt-in (unless they check the anonymous feedback box).

## After Upgrade Instructions

We’ve improved the admin notice triggered after a successful upgrade process (thanks to the guys at [@fooplugins](https://github.com/fooplugins)):  
[![2c01acca-80d4-11e6-9ef5-e7d13e2ed4d5](https://freemius.com/blog/wp-content/uploads/2016/09/2c01acca-80d4-11e6-9ef5-e7d13e2ed4d5.jpg)](https://freemius.com/blog/wp-content/uploads/2016/09/2c01acca-80d4-11e6-9ef5-e7d13e2ed4d5.jpg)

## Mobile Friendly

We adjusted the in-dashboard Contact us page to be responsive and work well on mobile. We’ll be working on making the pricing and checkout pages responsive as well.

![Vova Feldman](https://secure.gravatar.com/avatar/8155c30df4def3db68d14b39933f7691?s=700&d=mm&r=g)

Published by [Vova Feldman](blog-author-vova.md)

Freemius CEO & Founder, a serial entrepreneur and full-stack developer since age 14, propelled by a pursuit of excellence, embraces a holistic approach to life shaped by invaluable lessons in hard work and discipline.