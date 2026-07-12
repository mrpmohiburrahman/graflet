[Changelog](https://freemius.com/changelog/) / Enhanced Handling of Sender Addresses for Transactional Emails

We’ve deployed an improvement to how Freemius sends [transactional emails](help-documentation-marketing-automation-transactional-emails.md) to ensure higher deliverability and a more consistent experience for buyers.

Up until now, transactional emails were sent using either the [custom sender address configured by the maker](help-documentation-marketing-automation-email-settings.md) or the email associated with the Freemius account. While we’ve long supported [DKIM domain authentication](help-documentation-marketing-automation-email-deliverability.md#domainkeys-identified-mail-dkim) to help with deliverability, we noticed that incomplete or incorrectly configured DKIM setups could cause legitimate emails to get blocked or land in spam.

[![Various Configured Emails in Freemius](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-custom-email-addresses-1024x858.png)](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-custom-email-addresses.png)

To address this and ensure important messages reach customers reliably, Freemius will now automatically send transactional emails from `[email protected]` whenever:

- DKIM authentication has not been completed, or
- the sender address does not match the authenticated domain, or
- the sender address is using some generic provider like Gmail, Outlook etc.

In these cases the email will appear as **&lt;[\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection)&gt; {{ productTitle }} via Freemius**, keeping your product branding clear for customers. Your **Reply-To address remains unchanged**, so all customer responses will still reach you directly.

If your domain is already authenticated with DKIM and you’re using email addresses from that domain, nothing changes — your transactional emails will continue using your configured sender. Otherwise you can optionally authenticate your domain if you want to keep using your own sender address.