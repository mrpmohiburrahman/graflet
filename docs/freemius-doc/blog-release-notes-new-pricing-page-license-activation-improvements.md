We’ve got a pretty cool update this time around – a new ReactJS pricing page for the WP Admin will be shipped soon directly with the Freemius SDK! Besides that, we’ve got license activation improvements that will improve the UX for bundles, bug fixes, and more. Let’s dive in.

## Getting Ready for the new ReactJS-based Pricing Page

Freemius’ current in-dashboard pricing page was developed back in 2015. Obviously, the page has undergone extensive development since then, as we’ve added many features throughout the years. However, the front-end technologies it uses are already outdated, making maintenance, bug fixing, and new feature development much slower.

While we still haven’t replaced the pricing in the SDK, this version introduces the required infrastructure to [start using the new pricing page](https://github.com/Freemius/pricing-page/tree/develop#how-can-i-test-it) right away, which is pretty stable.

![Freemius SDK 2.4.0 New ReactJS Pricing Page](https://freemius.com/blog/wp-content/uploads/2020/09/freemius-sdk-2-4-0-new-reactjs-pricing-page.png)

The [new pricing page](https://github.com/Freemius/pricing-page/tree/develop) is much “smarter” and facilitates many pricing use-cases we haven’t supported before.

As the new pricing page is open-source, it gives you complete flexibility to [modify it as you wish](https://github.com/Freemius/pricing-page/tree/develop#how-to-create-my-own-pricing-app-version), which hasn’t been possible until now.

### Bundles License Activation

If you are selling bundles with many products that users typically use in parallel on the same website, it is not very pleasant for customers to activate the same license key for each product in the bundle.

To improve this user experience, we introduced new logic that checks if a license is associated with a bundle and automatically activates the license key for all the other bundle’s paid products installed on the site that are not yet associated with a license key.

To activate this capability, you’ll need to add the following to the SDK init snippet params:

`'bundle_license_auto_activation' => true,`

We decided to release this option as turned off by default because it may lead to some confusion in the following scenario:

- A freelancer purchased a bundle license
- They install pluginX on their client’s site and activated it with their bundle’s license key
- The client installs pluginY independently, while pluginY is also part of the bundle
- If the option is turned on, the license will be automatically activated for pluginY, unexpectedly utilizing a license of the owner without them knowing about it

In the next iteration, we’ll enrich the mechanism to auto-activate the license if it hasn’t yet been flagged as white-labeled.

## Improved cURL Error Handling

Even though WordPress’ HTTP API is supposed to work with web sockets, some users still encounter cURL errors when the cURL module is missing or disabled by the host. Instead of showing the cURL error number, the SDK will now display an informative human-friendly error message that explains the issue and guides the user about how to fix the situation with their host.

## Themes

- The activation process of a theme that doesn’t have a settings page in the WP Admin was fixed.
- We addressed all the errors that were thrown by [Theme Sniffer](https://github.com/WPTT/theme-sniffer) and [Theme Check](https://wordpress.org/plugins/theme-check/).

## Affiliate Application Form

With our legal firm’s help, we recently developed an affiliate agreement that we and our makers can use for onboarding affiliates. If you are leveraging the in-dashboard affiliate form, you’ll notice that we added a new checkbox requiring users to accept the terms and conditions of the program before they can apply:

![Freemius Affiliate Terms & Conditions Confirmation](https://freemius.com/blog/wp-content/uploads/2020/09/freemius-affiliate-terms-and-conditions-confirmation.png)

## Removing \_fs\_blog\_admin & \_fs\_network\_admin from Heartbeat Requests

Due to WordPress limitations, when a WP AJAX call is invoked, there’s no way to identify if it was initiated from the WP admin area or the site front. As a workaround, we came up with a simple technique by adding a querystring argument \_fs\_blog\_admin=true (and \_fs\_network\_admin in the WP network admin) to all WP AJAX calls initiated from the WordPress admin area, which then allows us to identify if a request was triggered from the WordPress admin area or not.

WordPress has a keepalive mechanism ([Heartbeat API](https://developer.wordpress.org/plugins/javascript/heartbeat-api/)) that initiates a WordPress AJAX POST request every few seconds when the user is logged into their WordPress admin area. The querystring param was also added to those requests.

Troubleshooting website issues frequently involves checking the network tab. Naturally, seeing many requests with a Freemius “fingerprint” (\_fs\_blog\_admin=true in the querystring) generated lots of false-positives where admins and hosting companies assumed that those frequent AJAX requests were triggered by the SDK, when, in 99.99% of the cases, it had nothing to do with the SDK. Regardless, we optimized the logic a bit, and now it skips from “touching” the keepalive AJAX requests.

## Adding rel=”noopener noreferrer” to Relevant Links

We reviewed the entire SDK and added the noopener and noreferrer attributes to all applicable external links generated by the SDK.

## Reducing the SDK Size

As part of our efforts to reduce the SDK size, we enriched .gitattributes to exclude all the \*.po translation files from the downloaded ZIP file from GitHub. \*.mo files are the actual binary translation files that are in use by the SDK. This exclusion reduces the SDK by ~900Kb.

## Chinese Translation

Huge thanks to [@xiahengchen](https://github.com/xiahengchen) for translating the entire SDK to Chinese 💯

Xiaheng Chen is a new member of our development team specializing in frontend development.

## Shout out to this version’s contributors!

- Leo Fajardo – [@fajardoleo](https://github.com/fajardoleo) (Lead)
- Vova Feldman – [@vovafeldman](https://github.com/vovafeldman)
- Xiaheng Chen – [@xiahengchen](https://github.com/xiahengchen)
- David Gwyer – [@dgwyer](https://github.com/dgwyer)
- Dovy Paukstys – [@dovy](https://github.com/dovy)

## What’s coming next?

The next release will support the [new Updates UI](https://make.wordpress.org/core/2020/07/30/recommended-usage-of-the-updates-api-to-support-the-auto-updates-ui-for-plugins-and-themes-in-wordpress-5-5/), introduce an option to hide private Account info by white-labeling the license directly from the WP Admin, and hopefully, already bundle the new pricing page!