![](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)

Here’s the Freemius Release Notes update that highlights recent product improvements made, so you can easily stay up to date on what’s new for June 2016.

1. Major bug fix for all devs using the **“Activate Freemius only for new plugin installs”** feature from the dashboard. We fixed the logic that determines if it’s a new plugin install or a plugin update \[[`aba9c51`](https://github.com/Freemius/wordpress-sdk/commit/aba9c51ffaf507021fd0692ad3231cccdc4da243)].
2. Another important bug that we resolved related to licensing. When from some reason a license sync fails and the user tries to activate a license. So far the request was failing, since on our backed, the license was already activated and reached its quote. The fix check if the site is already associated with that license, and instead of trying to activate another license, it just syncs it \[[`1746110`](https://github.com/Freemius/wordpress-sdk/commit/174611089c93530c87ae78549783d518e87b3c51)].

## License Key Activation

So far we were focused on freemium products monetization, and everything was API based directly from within the WP admin dashboard (no need for keys). With the recent launch of [Freemius Checkout](wordpress-checkout.md) we introduced the concept of license keys. Once a user installs a premium code version of a plugin, instead of just showing an opt-in, the user will be prompted to enter his license key:  
![license key prompt](https://freemius.com/blog/wp-content/uploads/2017/01/license-key-prompt.png)

For freemium plugins, the user would be able to click on **Activate Free Version** and just use the free features. While for premium only plugins, this option would not be available, and the user won’t be able to use the plugin without a valid license key.

The additional benefit of the license keys concept is to prevent confusion when activating a multi-site license on siteX; that was purchased on siteY. The license key eliminates the process of the additional email authentication (assuming that if a user has a valid license key, he got it in his email), and also prevents the mess that happens when the wp admin user that tries to active the plugin on siteX has a different email then on siteY.

If the user used the plugin before on siteX, then purchased a license via [Freemius Checkout](wordpress-checkout.md), the user will be able to activate the license in the plugins page by clicking the **Activate License** link:  
![Activate License link](https://freemius.com/blog/wp-content/uploads/2017/01/Activate-License-link.png)

Here’s what happens when it clicked:  
![Enter License key](https://freemius.com/blog/wp-content/uploads/2017/01/Enter-License-key.png)

We are still working on the after purchase email instruction changes, facilitating all the use-cases while trying to keep the upgrade instructions short and sweet.

![Vova Feldman](https://secure.gravatar.com/avatar/8155c30df4def3db68d14b39933f7691?s=700&d=mm&r=g)

Published by [Vova Feldman](blog-author-vova.md)

Freemius CEO & Founder, a serial entrepreneur and full-stack developer since age 14, propelled by a pursuit of excellence, embraces a holistic approach to life shaped by invaluable lessons in hard work and discipline.

![Benjamin Intal](https://freemius.com/fs-site/wp-content/uploads/2018/07/benjamin-intal-300x300-compressed.jpg "Benjamin Intal")

“Since switching from EDD to Freemius in 2017, we’ve had happier customers, lower uninstall rate, and overall a better performance in getting sales. If you’re looking to monetize your WordPress plugins or themes, Freemius is definitely the way to go.”

Benjamin Intal - [Founder at Stackable](https://wpstackable.com/) [Try Freemius Today](pricing.md)

## Hand-picked related articles

[![Licensing, Billing, Themes Support, Bug Fixes – August Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-august-2016-wordpress-skd-release-notes.md)

### [Licensing, Billing, Themes Support, Bug Fixes – August Release Notes](blog-august-2016-wordpress-skd-release-notes.md)

This is a major version release (89 commits) with many important bug fixes and significant enhancement of the licensing mechanism for the paid plugin authors. Bug Fixes Quotes Localization: I’m…

[Continue Reading](blog-august-2016-wordpress-skd-release-notes.md)

[![Submenu Items, Automatic Updates Mechanism, Plugin Trials – May Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-may-2016-wordpress-skd-release-notes.md)

### [Submenu Items, Automatic Updates Mechanism, Plugin Trials – May Release Notes](blog-may-2016-wordpress-skd-release-notes.md)

Here’s the Freemius Release Notes update that highlights recent product improvements made, so you can easily stay up to date on what’s new for May 2016.

[Continue Reading](blog-may-2016-wordpress-skd-release-notes.md)

[![Localization, Feedback Form, After Upgrade Instructions & Mobile Friendlier – September Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-septmber-2016-wordpress-sdk-release-notes.md)

### [Localization, Feedback Form, After Upgrade Instructions & Mobile Friendlier – September Release Notes](blog-septmber-2016-wordpress-sdk-release-notes.md)

These are the release notes for a major release (more than 80 commits) with a bunch of enhancements and one crucial license related bug fix for developers who monetize with…

[Continue Reading](blog-septmber-2016-wordpress-sdk-release-notes.md)

[![Deactivation Feedback Form, Admin Menu, Add-On Trials, Infrastructure – April Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-april-2016-wordpress-skd-release-notes.md)

### [Deactivation Feedback Form, Admin Menu, Add-On Trials, Infrastructure – April Release Notes](blog-april-2016-wordpress-skd-release-notes.md)

Here’s the Freemius Release Notes update that highlights recent product improvements made, so you can easily stay up to date on what’s new for April 2016.

[Continue Reading](blog-april-2016-wordpress-skd-release-notes.md)

[![Trials, Upgrade Flow, 100% Coupon Code & Editable Billing Information – December Product Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-december-2016-wordpress-skd-release-notes.md)

### [Trials, Upgrade Flow, 100% Coupon Code & Editable Billing Information – December Product Release Notes](blog-december-2016-wordpress-skd-release-notes.md)

Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched in…

[Continue Reading](blog-december-2016-wordpress-skd-release-notes.md)

[![Dunning, New In-Dashboard Checkout & Site Trials! – March Product Release Notes](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)](blog-dunning-in-dashboard-checkout-site-trials-march.md)

### [Dunning, New In-Dashboard Checkout & Site Trials! – March Product Release Notes](blog-dunning-in-dashboard-checkout-site-trials-march.md)

Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched in…

[Continue Reading](blog-dunning-in-dashboard-checkout-site-trials-march.md)