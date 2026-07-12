[Changelog](https://freemius.com/changelog/) / Expiring Trial notification enhancements

As part of our automated marketing efforts, we send out a reminder email to customers with expiring trials. However, if the product was uninstalled or the website was deleted, the links in the marketing email – which pointed to the user’s WordPress Dashboard – became ghosted, resulting in broken upgrade links. This is how the email looks when linking to the WordPress Admin Dashboard.

[![Freemius Expiring free trial notification email with WP Dashboard links](https://freemius.com/blog/wp-content/uploads/2022/09/freemius-expiring-free-trial-notification-inactive-install.png)](https://freemius.com/blog/wp-content/uploads/2022/09/freemius-expiring-free-trial-notification-inactive-install.png)

We fixed this issue by proactively checking if the site is active. Only once and if we have confirmed this do we include the WordPress Dashboard links. If the site is inactive, we link to direct checkout (in the context of the license), making sure that the user can always update their package should they change their mind.

If Freemius finds the site to be inactive, the email will look like this:

[![Freemius Expiring Free trial email for ghosted sites](https://freemius.com/blog/wp-content/uploads/2022/09/freemius-expiring-free-trial-notification-active-install.png)](https://freemius.com/blog/wp-content/uploads/2022/09/freemius-expiring-free-trial-notification-active-install.png)

Please note: If the user activated the trial and then requested a data erasure, we respect their decision. Since we do remove this type of data from our database, we do not send any emails. This behavior has not changed.