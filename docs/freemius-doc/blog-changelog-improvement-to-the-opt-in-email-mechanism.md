[Changelog](https://freemius.com/changelog/) / Improvement to the Opt-in Email Mechanism

The Freemius WordPress SDK includes an [opt-in mechanism](help-documentation-wordpress-sdk-opt-in-message.md) that allows users to decide whether to connect their site with Freemius. To prevent misuse, this mechanism incorporates an email verification process.

[![](https://freemius.com/blog/wp-content/uploads/2025/01/opt-in-screen-1024x571.png)](https://freemius.com/blog/wp-content/uploads/2025/01/opt-in-screen.png)

We recently discovered that certain misconfigurations in a WordPress site could lead to the verification email being sent multiple times, causing confusion for buyers.

To address this, we have improved the system on our end to identify and prevent duplicate messages. No changes to the SDK are required for this update to take effect.