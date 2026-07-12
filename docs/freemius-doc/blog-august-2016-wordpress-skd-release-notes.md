![](https://freemius.com/blog/wp-content/uploads/2019/10/release-notes-october-featured-image.jpg)

This is a major version release (89 commits) with many important bug fixes and significant enhancement of the licensing mechanism for the paid plugin authors.

1. **Quotes Localization:** I’m not going to dive deep here, but there was a problem with quotes localization due to the early call of `get_plugin_data()` in the SDK. The problem was fixed. [Click here to learn more](https://github.com/Freemius/wordpress-sdk/issues/77).
2. **Updates Mechanism:** When a user had both the free plugin version and the premium plugin version installed in parallel, version updates were not showing for the premium version in `plugins.php` page until the free version was uninstalled.
3. **Free plugin version uninstallation**: Uninstalling a free plugin version while the premium was running generated PHP errors due to the uninstall hook mechanism was unintentionally triggered.

## Licensing

1. Paying user who purchased a license outside the in-dashboard checkout, can now easily activate the license from the **Account** page by clicking the **Activate License** button:  
   [![account details](https://freemius.com/blog/wp-content/uploads/2017/01/account-details.png)](https://freemius.com/blog/wp-content/uploads/2017/01/account-details.png)  
   [![license key](https://freemius.com/blog/wp-content/uploads/2017/01/license-key.png)](https://freemius.com/blog/wp-content/uploads/2017/01/license-key.png)  
   If the user can’t find his license, we added a simple mechanism to email the license on the fly by clicking the **Can’t find your license key?**:  
   [![resend license key](https://freemius.com/blog/wp-content/uploads/2017/01/resend-license-key.png)](https://freemius.com/blog/wp-content/uploads/2017/01/resend-license-key.png)
2. We also added the same license recovery mechanism to the plugin’s initial activation screen:  
   [![plugin initial activation screen](https://freemius.com/blog/wp-content/uploads/2017/01/plugin-initial-activation-screen.png)](https://freemius.com/blog/wp-content/uploads/2017/01/plugin-initial-activation-screen.png)
3. Users can now find their activated license key in the **Account** section:  
   [![Activated license key](https://freemius.com/blog/wp-content/uploads/2017/01/Activated-license-key.png)](https://freemius.com/blog/wp-content/uploads/2017/01/Activated-license-key.png)

We understand that licensing management is a big hurdle and time waste in the WP plugins ecosystem, and we are doing our best to keep iterating and improving that mechanism, making it as seamless as we can. If you have any further suggestions on how we can improve it, please let us know!

## Billing

Since at the moment users doesn’t have a “Member Area” outside of the WP admin, we added a billing tab for paying customers where the user can see his billing history and easily print invoices:  
[![billing tab for paying customers](https://freemius.com/blog/wp-content/uploads/2017/01/billing-tab-for-paying-customers.png)](https://freemius.com/blog/wp-content/uploads/2017/01/billing-tab-for-paying-customers.png)

The goal is to extend this area with other billing-related components, like payment methods, billing address & company information (currently only editable via the developer’s dashboard), etc.

### Themes Support

We released the beta of our themes integration. If you have a theme and like to be part of the beta please send us a note to \[themes AT freemius DOT com ] and we’ll provide you with further details.

**Happy SDK update!**

![Vova Feldman](https://secure.gravatar.com/avatar/8155c30df4def3db68d14b39933f7691?s=700&d=mm&r=g)

Published by [Vova Feldman](blog-author-vova.md)

Freemius CEO & Founder, a serial entrepreneur and full-stack developer since age 14, propelled by a pursuit of excellence, embraces a holistic approach to life shaped by invaluable lessons in hard work and discipline.