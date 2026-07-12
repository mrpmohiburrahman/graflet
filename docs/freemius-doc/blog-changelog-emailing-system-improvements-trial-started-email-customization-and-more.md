[Changelog](https://freemius.com/changelog/) / Emailing System Improvements: Trial Started Email Customization and More

This week we’re rolling out various improvements and fixes to our emailing system.

### Customize Trial Started Email

Following up on our last deployment, where we enabled makers to [customize emails](help-documentation-marketing-automation-email-content-customization.md), we have added a new email to the customization list: the “Trial Started” email.

[![Trial email customization](https://freemius.com/blog/wp-content/uploads/2026/03/trial-email-customization-1024x415.png)](https://freemius.com/blog/wp-content/uploads/2026/03/trial-email-customization.png)

We understand that the [trial](help-documentation-selling-with-freemius-set-up-trials.md) email plays an equally crucial role as the new subscription or purchase email, since many Apps & SaaS products use trials to onboard customers. With this rollout, our emailing system becomes more customizable to better support your software business needs. Please reach out to us if you have additional requirements.

### Other Fixes

- The [tone customization](help-documentation-marketing-automation-email-style-customization.md#customizing-your-tone) setting was not respected for a few emails. This has now been fixed.
- We also fixed an issue with markdown processing in some emails.
- We fixed the retrieval of the last [30 days of email logs from SendGrid](help-documentation-marketing-automation-email-deliverability.md#handling-deliverability-issues), which in some cases—especially for products without proper DKIM configuration—was not working correctly.