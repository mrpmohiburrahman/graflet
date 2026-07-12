[Changelog](https://freemius.com/changelog/) / Checkout licensing UI bug fixes

A maker provided us with some bug reports for the Checkout’s licensing UI.

[![](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-checkout-license-selector-ui-fix-1024x505.png)](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-checkout-license-selector-ui-fix.png)

We noticed we did not show the short label in the “License label” (where it says “Single Site”) when there was only one unit available. It was wrongly showing “Single Site License” causing inconsistency in the UI. We have fixed that.

[![](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-checkout-license-error-ui-fix-1024x485.png)](https://freemius.com/blog/wp-content/uploads/2024/09/freemius-checkout-license-error-ui-fix.png)

We also noticed a broken UI in case the error message when entering a license key was long. Previously the “Try again?” button would try to appear in the same line, breaking the flow of the UI. We have improved that as well.