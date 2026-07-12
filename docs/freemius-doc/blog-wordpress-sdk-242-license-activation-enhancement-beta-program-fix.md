[WordPress SDK 2.4.2](https://github.com/Freemius/wordpress-sdk/releases/tag/2.4.2) was just released with some great license activation improvements, a bugfix for the Beta Programs feature, and streamlined activations for Add-ons. Oh yeah, and we fixed a little conflict with the new ReactJS Pricing page that’s still in the works! Let’s jump right in so you can see all the improvements we’ve made.

## License Activation Enhancement

This release introduces several small, yet powerful, enhancements for the license activation screen. These annotations below go over each detail of the optimizations we’ve made, with details outlined below.

![Freemius WordPress SDK 2.4.2 License Activation Enhancements](https://freemius.com/blog/wp-content/uploads/2021/02/freemius-wordpress-sdk-2-4-2-license-activation-enhancements.png)

- The `Hey {{ firstName }}`, was removed to clean up some space.
- The welcoming message has changed from `Thanks for purchasing {{ producTitle }} to Welcome to {{ producTitle }}` to be more… welcoming 🙂
- The updates & licensing mechanism disclaimer was adjusted to a more inclusive form.
- A tooltip was introduced next to “freemius.com” to explain the relation of the plugin/theme and Freemius.
- The permissions overview trigger was merged into the disclaimer and is now triggered by the “diagnostic data” link.
- The ADMIN NOTICES permission was removed since there’s not much value in showing it for paid products.
- We realize that some people are very emotional about the plugins & themes permission even though it can be easily switched off. While there is a lot of [value in collecting it](https://github.com/Freemius/data-concerns-faq/blob/master/faq-08.md#list-of-installed-plugins--themes-optional), since it’s not mission-critical and probably the most dreaded capability among our data practices, the option is now turned off by default when activating a license key.
- To reduce concerns even further, we added tooltips to all of the permissions to explain why they’re needed.
- We’ve recently documented [known license activation issues](help-documentation-wordpress-sdk-license-activation-issues.md) (with solutions) in our [knowledge base](https://freemius.com/help/documentation/), so, to save customers time and reduce your support load, we added a new link “license issues?” to this document right after the license activation button. If you prefer to copy the documentation to your knowledge base and link to that instead, you can use the `known_license_issues_url` filter.

This GIF showcases the updated license activation screen behavior:

![Tickera License Activation](https://freemius.com/blog/wp-content/uploads/2021/02/tickera-license-activation.gif)

Just before we entered 2021, we discovered an issue in our implementation of the Beta Program functionality, and, therefore, temporarily paused delivery of beta releases. We’ve fixed the implementation, and this SDK version is now integrated with the fixed mechanism.

## How to migrate beta users to the new mechanism?

First of all – you’ll need to update the SDK to this latest version.

Then follow these instructions:

- Sign in to the [Developer Dashboard](https://dashboard.freemius.com/) and navigate to the USERS section of the relevant product.
- Change the filter to only show Beta Participants:

<!--THE END-->

![Freemius Developer Dashboard USERS Filter for Beta Participants](https://freemius.com/blog/wp-content/uploads/2021/02/freemius-developer-dashboard-users-filter-for-beta-participants.png)

- Click DOWNLOAD USERS to get a CSV of all users who previously enrolled in your Beta Program:

<!--THE END-->

![Freemius Developer Dashboard Download Users Button](https://freemius.com/blog/wp-content/uploads/2021/02/freemius-developer-dashboard-download-users-button.png)

- Finally, you’ll need to send a message asking them to join the beta program again from the site(s) in which they want to receive updates with beta releases. Here’s some copy you can use for your message:

> Hi {{ firstName }},
> 
> Thanks again for being part of our Beta program and helping us test/improve/shape {{ producTitle }}.
> 
> Apologies for the hassle, but due to an issue that was discovered in our Beta releases mechanism, if you’d want to keep getting updates with beta release, you’ll need to enroll in the Beta program again.
> 
> If you are no longer interested in being part of the Beta Program, simply ignore this message.

## Pricing Page

The SDK comes with a special mechanism to automatically use the newest version of the SDK available, whether it’s included in your plugin/theme or in other Freemius-powered plugins/themes installed on a site.

We recently discovered that even if you haven’t integrated our [ReactJS-based pricing page](https://github.com/Freemius/pricing-page/tree/develop), and another plugin/theme on the same website did, it was unexpectedly showing the new pricing for your product too.

Until we fully migrate to the new pricing page, we’ve updated it to only show up for products that include the build files in their product’s code, even if there’s another product running a newer version of the SDK.

## Add-Ons Opt-In Behavior

To maximize the opt-in rate to usage-tracking, previously, activating an add-on would trigger the parent product’s opt-in screen, even if the user had already skipped it before. After receiving some feedback, we realized this approach can be annoying, especially for products that usually need multiple add-ons installed just to get started.

We adjusted this behavior and from now on free add-ons inherit the opt-in state of their parent product.

## Thanks for Reading!

If you ever think of any features for us to consider, feel free to add them to our [Trello board](https://trello.com/b/I6o3BZOo/freemius-features-requests), and in the meantime, happy selling!