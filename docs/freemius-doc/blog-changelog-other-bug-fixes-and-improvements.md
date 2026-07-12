[Changelog](https://freemius.com/changelog/) / Other bug fixes and improvements

### Fixed some store-scoped API endpoints not working properly

Since we released the [multi-store](blog-release-notes-real-time-analytics-and-multi-store-dashboard.md) Developer Dashboard, we noticed some API endpoints were not working properly. We have investigated all such endpoints and have made fixes.

### Improved the email address verification mechanism for users

We noticed that if a Developer changes a User’s email from the Developer Dashboard, the User will see a blank screen upon clicking the confirmation button. Although their email change was getting verified, this still presented a poorer UX. We have improved this UX, by redirecting the User to the User Dashboard and showing an appropriate message.

[![Freemius User Dashboard email address verification UI](https://freemius.com/blog/wp-content/uploads/2024/05/verified-email-address-ui-freemius-user-dashboard-1024x903.png)](https://freemius.com/blog/wp-content/uploads/2024/05/verified-email-address-ui-freemius-user-dashboard.png)

We also took this opportunity to improve the email message itself.

### Fixed loading of white-listed sites for license activation

In some edge cases, we found that a few users were facing issues activating their [white-listed](help-documentation-users-account-management-license-security.md#url_whitelisting_aka_license_firewall) licenses. We found out the cause and have fixed it.

### Fixed coupon code issues with PayPal

One partner of ours reported that some coupons were not working with the PayPal payment method. We investigated the cause and have deployed a fix.

### Small Analytics graph improvement

We noticed in some cases we were plotting incorrect `0` values on some graphs where data was not available.

[![](https://freemius.com/blog/wp-content/uploads/2024/05/improved-analytics-ui-freemius-developer-dashboard-1024x603.png)](https://freemius.com/blog/wp-content/uploads/2024/05/improved-analytics-ui-freemius-developer-dashboard.png)

We have fixed this by removing the zero points from the graph, which presents a nicer UX.