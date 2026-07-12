[Changelog](https://freemius.com/changelog/) / Fix for Incorrect Cart Recovery Emails During Payment Method Update

We noticed a regression in our Checkout where the system was incorrectly sending [cart recovery emails](help-documentation-marketing-automation-cart-abandonment-recovery.md) when customers were simply updating their payment method.

The root cause has been identified and a fix has been deployed to ensure cart recovery emails are only triggered in the correct purchase scenarios.