![](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)

Here’s the Freemius Release Notes update that highlights recent product improvements made, so you can easily stay up to date on what’s new for April 2016.

1. Added new option “It’s a temporary deactivation. I’m just debugging an issue.”

![deactivation feedback form](https://freemius.com/blog/wp-content/uploads/2017/01/deactivation-feedback-form.png)  
2\. Made the “Other” input field required. Hopefully, this will increase the amount of descriptive feedback.

![descriptive feedback](https://freemius.com/blog/wp-content/uploads/2017/01/descriptive-feedback.png)

### Admin Menu

Show *Contact Us*, *Support Forum* and *Add-Ons* submenu items also for users who skipped or pending activation.

### Add-Ons

1. Added the capability of add-on trial without a payment method (just a free trial). This is currently working only for users that opt-in. We might expand that in the future.
2. Added visual support for multiple billing cycles.

![multiple billing cycles](https://freemius.com/blog/wp-content/uploads/2017/01/multiple-billing-cycles.png)  
3\. If a premium add-on comes with a trial period, we add the tag *Trial* right after the add-ons price.

![Trial tag](https://freemius.com/blog/wp-content/uploads/2017/01/Trial-tag.png)

### Misc

Replaced the deprecated `add_object_page` with `add_menu_page`.

### More Data

We prepared the [infrastructure](https://freemius.com/careers/devops-sysadmin/) to capture installed plugins & themes for opted-in users. It’s still work in progress, and we don’t capture it yet on our side. The goal is to help you understand your users better, see what other plugins/themes are frequently used with yours, etc.

### Last but not least – please test!

We ran as many tests as we could and also deployed it in production with our plugin before releasing it to you. Having said that, please run some sanity tests before deploying it. You know WordPress, it’s impossible to release something that is bullet proof for all environments.

### Coming soon…

1. One of the developers we work with found that if the “Turn Freemius on only for new users” is turned on in the Freemius dashboard, submenu items like the *Contact Us* are not appearing in the dashboard for users who’ve been using the plugin before the Freemius integration. That’s a problem, especially for developers who monetize with Freemius and don’t want to opt-in their previous users. We already have this in testing, so it should be ready very soon.
2. I recently was doing some testing with WooCommerce, and noticed that they’ve added an opt-in as well:

![WooCommerce opt-in](https://freemius.com/blog/wp-content/uploads/2017/01/WooCommerce-opt-in.png)

WooCommerce implements an opt-in, too

First of all, I’m excited that opt-ins are becoming mainstream 🙂 What was also cool about this opt-in is the link it reference, the [“Find out more”](https://www.woothemes.com/woocommerce/usage-tracking/). It’s a great inspiration, and we are going to create a similar page for Freemius and reference it instead of our current link that some end users might find confusing.  
3\. We are wrapping the development of coupons, discounts, and promotional codes support. Hope to release it in the next few weeks.

![Vova Feldman](https://secure.gravatar.com/avatar/8155c30df4def3db68d14b39933f7691?s=700&d=mm&r=g)

Published by [Vova Feldman](blog-author-vova.md)

Freemius CEO & Founder, a serial entrepreneur and full-stack developer since age 14, propelled by a pursuit of excellence, embraces a holistic approach to life shaped by invaluable lessons in hard work and discipline.