[Changelog](https://freemius.com/changelog/) / “Log in as User” Now Safer for Debugging Without Triggering Cart Recovery

Freemius has a very handy feature called **“Log in as User”**. While working with customer support, it is often helpful to view the [Freemius Customer Portal](help-documentation-users-account-management.md) exactly as your customer would see it. This allows you to pinpoint the exact button a customer should click or the specific information they need to look for. To use this feature, simply click the **Log in as User** button from the Users page of your product in the Developer Dashboard.

[![Freemius Log in as User feature from the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-login-as-user-1024x385.png)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-login-as-user.png)

Recently, we noticed that when makers were using this feature to debug license upgrade scenarios, it sometimes created a cart entity on Freemius on behalf of the user. As a result, our [cart recovery mechanism](help-documentation-marketing-automation-cart-abandonment-recovery.md) was triggered, and recovery emails were sent to the buyer. This could understandably be a little annoying to your customers.

To address this, we’ve now ensured that carts are not created in these scenarios. This means you can safely use the **Log in as User** feature to debug customer issues without triggering any unnecessary cart recovery workflows or side-effects.