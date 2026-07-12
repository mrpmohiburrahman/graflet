[Changelog](https://freemius.com/changelog/) / Misc Developer Dashboard bug fixes and improvements

This week’s release brings the following bug fixes and enhancements to the Developer Dashboard.

### Mailchimp integration improvement

Following up on the [Mailchimp integration improvement](blog-changelog-mailchimp-integration-improvements.md) – When unlinking a connection, the connection will be deleted from our server if it is not used by any other products.

[![](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-mailchimp-integration-disconnection-1024x435.png)](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-mailchimp-integration-disconnection.png)

This helps clean up any leftover connection data that is not in use anymore.

### Plan deletion bug fix

When deleting plans we will now show a notice if there are active licenses associated with the plan. If you want to deprecate some plan, we recommend hiding it instead of deleting it. We will come up with more follow-up updates to ease the deprecation of plans with active usage.

Right now, deleting a plan with active licenses can create issues for existing customers. Hence we have disabled this for the time being.

### Composer integration

We added a notice in the “Deployment” page of WordPress products to use a proper [semantic version](https://semver.org/) to support [composer integration](blog-release-notes-wordpress-sdk-2-4-1-deployment-composer-dkim-login-as-user-security.md#install_paid_products_via_composer).