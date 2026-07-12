[Changelog](https://freemius.com/changelog/) / Backend QoL Improvements: Invoice Wrapping & License Exports

We are rolling out a few quality-of-life improvements to our backend system.

### Fixed Long Strings in Invoices

We noticed a few edge cases where long strings in [invoices](help-documentation-users-account-management-orders-history.md#generate-a-printable-invoice) could break the layout and affect readability.

[![Breaking long URL in invoices](https://freemius.com/blog/wp-content/uploads/2025/12/invoice-long-string-with-url-1024x493.png)](https://freemius.com/blog/wp-content/uploads/2025/12/invoice-long-string-with-url.png)

We’ve identified all such areas and ensured that long text now wraps correctly onto the next line, keeping invoices clean and easy to read.

### User Emails Now Included in Licenses Export

[![Licenses export from the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/12/licenses-download-1024x464.png)](https://freemius.com/blog/wp-content/uploads/2025/12/licenses-download.png)

When [exporting licenses](blog-freemius-release-notes-december.md#data_liberation_updates) from the Developer Dashboard, the CSV will now include an additional `user_email` column alongside the existing `user_id`. This makes it easier to analyze exports and better understand and manage your user base when working with the data.