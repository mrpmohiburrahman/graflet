[Changelog](https://freemius.com/changelog/) / Fixes and Enhancements to Affiliate Exports and Cross-Store or Account Attribution

We have released a few small improvements to the Affiliates section in the Developer Dashboard.

### Fixed Affiliate Exports Functionality

[![Affiliate export feature freemius developer dashboard](https://freemius.com/blog/wp-content/uploads/2025/11/affiliate-download-freemius-dashboard-1024x424.png)](https://freemius.com/blog/wp-content/uploads/2025/11/affiliate-download-freemius-dashboard.png)

We identified an issue where clicking the Download button on the [Affiliates](help-documentation-affiliate-platform.md) page did not export the full list of affiliates—some records were being cut off. This was especially problematic for makers with larger affiliate programs. The fix is now deployed, and downloading will correctly generate a CSV containing all available affiliates.

### Fixed Payouts for Cross Store or Account Attribution

Freemius’ affiliate system allows [attributing commissions across store or account](help-documentation-affiliate-platform-affiliate-program-activation.md#sales-attribution). This means if an affiliate promotes one product but the buyer ends up purchasing another product under the same store or account, the affiliate still earns the commission.

However, we noticed these attributions were not being reflected accurately in the Payouts tab. This led to confusion and occasionally missed payments since makers couldn’t always see why a commission was attributed.

[![Affiliate payout attribution across products](https://freemius.com/blog/wp-content/uploads/2025/11/affiliate-payout-cross-attribution-1024x420.png)](https://freemius.com/blog/wp-content/uploads/2025/11/affiliate-payout-cross-attribution.png)

With this week’s deployment, these attributions are now clearly shown in the Payouts tab, including an icon of the relevant product when the commission came from a cross-store or cross-account purchase. This brings full transparency into the payout breakdown, ensuring everything is visible and easy to verify.