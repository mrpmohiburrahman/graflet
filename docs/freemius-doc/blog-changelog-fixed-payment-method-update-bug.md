[Changelog](https://freemius.com/changelog/) / Fixed Payment Method Update Bug

We discovered an edge case bug where, in some rare scenarios, our payment method update process would display an incorrect error message. Although the payment method was updated successfully, the UI mistakenly indicated a failure—causing unnecessary confusion for buyers.

The root cause of the issue has been identified and a fix has been deployed.