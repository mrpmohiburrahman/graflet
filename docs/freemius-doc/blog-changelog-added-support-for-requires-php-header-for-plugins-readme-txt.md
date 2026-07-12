[Changelog](https://freemius.com/changelog/) / Added support for “Requires PHP” header for plugin’s readme.txt

WordPress supports a special `Requires PHP` [header](https://make.wordpress.org/plugins/2017/08/29/minimum-php-version-requirement/) in a plugin’s `readme.txt` file. If this has been implemented but the current web host is not running a compatible PHP version, WordPress blocks plugin updates.

Following feedback from our partners, we have added the same capability to our SDK and deployment strategy. If you include the `Requires PHP` header in your plugin’s `readme.txt` file, the SDK will show an appropriate notice on the update page and will block updates when needed.

[![Freemius SDK showing notice when "Requires PHP" header is not compatible.](https://freemius.com/blog/wp-content/uploads/2022/12/freemius-sdk-requires-php.png)](https://freemius.com/blog/wp-content/uploads/2022/12/freemius-sdk-requires-php.png)

You will also be able to see the new information under the Developer Dashboard’s Deployment page. We have added a new column: Min PHP Version.

[![Freemius Developer Dashboard showing Min PHP Version column.](https://freemius.com/blog/wp-content/uploads/2022/12/freemius-min-php-version-developer-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2022/12/freemius-min-php-version-developer-dashboard.png)

The above feature will only work for new deployments as of today. Also, please note that you’ll need to update the Freemius SDK to [v2.5.3](https://github.com/Freemius/wordpress-sdk/releases/tag/2.5.3) to fully utilize this feature.