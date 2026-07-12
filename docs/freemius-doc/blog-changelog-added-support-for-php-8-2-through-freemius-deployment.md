[Changelog](https://freemius.com/changelog/) / Added support for PHP 8.2 through Freemius deployment

[Version Deployment](https://freemius.com/help/documentation/selling-with-freemius/deployment/) is one of the powerful tools Freemius provides to our Software makers to ease their lives. The concept is simple; wrap your code in `if ( my_fs()->is__premium_only() )` family of methods and Freemius will strip out the premium code to make a WordPress.org-compliant free version of your WordPress theme or plugin.

So far, this feature has been limited to parsing PHP 7.1 code. With today’s update, you can start using PHP syntax up to version 8.2 and our deployment mechanism will properly strip off premium codes.

[![Create deployment Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/04/create-deployment-freemius-developer-dashboard-1024x570.png)](https://freemius.com/blog/wp-content/uploads/2024/04/create-deployment-freemius-developer-dashboard.png)

We have also made subtle improvements to the prettifier. It will now output code closer to WordPress formatting standards.