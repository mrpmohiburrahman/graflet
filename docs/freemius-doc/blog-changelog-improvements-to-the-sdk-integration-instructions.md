[Changelog](https://freemius.com/changelog/) / Improvements to the SDK Integration instructions

Over time, we’ve made improvements to our WordPress SDK and its integration code for both production and local development and testing.

Integrating the SDK with your WordPress plugin or theme for the first time can be slightly challenging — especially getting the correct flow of the [Opt-In screen](help-documentation-wordpress-sdk-opt-in-message.md). By default, Freemius may send a confirmation email during opt-in. If you’re using a “local” email address in your localhost environment (like ‘[\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection)’) or the same email address you used to sign-up with Freemius, you might not receive the email, and the activation will be stuck.

However, [skipping email activation in testing or development mode](help-documentation-wordpress-sdk-testing.md#skipping_email_activation) is easy. We need to put three constants in the `wp-config.php` file. Previously, the information about these was hidden on the SDK Integration page, far below.

To make it easier for first-time developers, we’ve rearranged the SDK Integration instructions in our Developer Dashboard.

[![Freemius Developer Dashboard SDK Integration testing code improvement](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-developer-dashboard-sdk-integration-improvement.jpg)](https://freemius.com/blog/wp-content/uploads/2023/07/freemius-developer-dashboard-sdk-integration-improvement.jpg)

The steps now clearly state what code you need to put inside your plugin/theme and what code you need to put inside the `wp-config.php` file.

This improvement of the Developer Dashboard was led by our new team member [Aleksandr Manukyan](https://www.linkedin.com/in/aleksandr-manukyan-36298644/) who joined us as a full-stack engineer.