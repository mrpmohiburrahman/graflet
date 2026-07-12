[Changelog](https://freemius.com/changelog/) / Fixed checkout bug allowing unintentional downgrade or re-purchase of a lifetime license

We got a report where a user, in an edge case, could accidentally re-purchase a lifetime license from our Checkout. They already had a lifetime license for a particular plan. Then they accidentally entered that license key for “upgrade” to the same plan and therefore got charged again.

[![](https://freemius.com/blog/wp-content/uploads/2024/04/lifetime-license-upgrade-notice-freemius-checkout-1024x622.png)](https://freemius.com/blog/wp-content/uploads/2024/04/lifetime-license-upgrade-notice-freemius-checkout.png)

In this iteration, we have fixed this behavior by simply blocking it from happening. The UI will also show a proper message to the user asking to choose a different number of licenses.