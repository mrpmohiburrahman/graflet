[Changelog](https://freemius.com/changelog/) / Reverse Invoice Bug Fixes and Improvements

Last month, we released the [Reverse Invoice feature within the Payouts email](blog-changelog-payouts-email-now-includes-the-reverse-invoice.md), eliminating the need for our makers to manually send invoices to us as their Merchant of Record (MoR).

Following the rollout, we identified a few edge case bugs that prevented invoice generation for a small number of makers. These issues have now been resolved and the system has been updated accordingly.

We also introduced a few improvements based on feedback and internal reviews:

- For FinTech banks (e.g., Wise, Revolut, Evolve), the invoice will now use the maker’s billing address instead of the bank account address.
- Freemius’ own address on the invoice is now consistent across all payout methods, regardless of whether it’s a wire transfer via Mercury or otherwise. Previously, our registered address varied based on the payout channel.
- The label “**Service Month**” has been updated to “**Service Period**” to better reflect multi-month invoice coverage.

If you notice any further issues, please let us know.