---
title: "Customize Email Sender and Reply-To Addresses"
url: "https://freemius.com/help/documentation/marketing-automation/email-settings/"
source: "docs"
section: "Docs"
category: "Marketing Automation"
scraped_at: "2026-04-09T19:58:39+06:00"
word_count: 603
---

Freemius allows developers to customize the sender and reply-to email addresses used in transactional emails sent to customers. These settings can be configured at both the store level and the product level within the Freemius Developer Dashboard.

This guide provides instructions for configuring email settings and invoice details to reflect your brand appropriately.

## Customizing Email Addresses[​](#customizing-email-addresses "Direct link to Customizing Email Addresses")

### Store-Level Email Settings[​](#store-level-email-settings "Direct link to Store-Level Email Settings")

When configured at the store level, the custom email addresses will be applied to all products under the selected store by default. Here is how to customize the email addresses:

1. Log in to your [Freemius Developer Dashboard](https://dashboard.freemius.com).
2. From the top-left menu, select the relevant Store under the Freemius logo.
3. Scroll down in the sidebar and select the Emails panel.
4. Fill in the required details for label and email address. The details are automatically saved once you focus out of the field.

### Product-Level Email Settings[​](#product-level-email-settings "Direct link to Product-Level Email Settings")

If you wish to override the store-level settings for a specific product, you can configure email addresses at the product level. Here is how to customize the email addresses:

1. Log in to your [Freemius Developer Dashboard](https://dashboard.freemius.com).
2. From the top-left menu, select the relevant Product.
3. Scroll down and click on the Emails panel.
4. Fill in the required details for label and email address. The details are automatically saved once you focus out of the field.

note

Make sure you setup [DKIM](help-documentation-marketing-automation-email-deliverability.md#domainkeys_identified_mail_dkim) to verify your custom email addresses so as to [minimize delivery issues](help-documentation-marketing-automation-email-deliverability.md). Otherwise Freemius [will fallback](#fallback-sender-behavior-for-transactional-emails) to using its own email addresses for sending transactional emails.

## Understanding Different Email Configurations[​](#understanding-different-email-configurations "Direct link to Understanding Different Email Configurations")

Freemius uses the following configuration for various emails:

### General System Address[​](#general-system-address "Direct link to General System Address")

Primarily used for all commerce-related transactional emails, such as purchase receipts, subscriptions, renewals, license expirations, and similar notifications.

We strongly recommend customizing this email address to reflect your brand.

### Don't Reply Address[​](#dont-reply-address "Direct link to Don't Reply Address")

Used as the `reply-to` address for transactional (e.g., payments, subscriptions, trials, and licenses) and other system emails where replies are not expected. However, if monitoring customer replies is desired, configure this field with an address that is regularly reviewed.

If you do not set this, your account's email address will be used instead.

### Developer Personal Assistance[​](#developer-personal-assistance "Direct link to Developer Personal Assistance")

This email address is used as the sender for specific customer cancellation actions; for example, when a trial is canceled or when a user immediately uninstalls a product.

### General Support[​](#general-support "Direct link to General Support")

Used as the:

- Reply-To address for [cart recovery emails](help-documentation-marketing-automation-cart-abandonment-recovery.md) sent to customers.
- Recipient of [contact form submissions](help-documentation-users-account-management-support-contact-form.md) from the Customer Portal.

## Fallback Sender Behavior for Transactional Emails[​](#fallback-sender-behavior-for-transactional-emails "Direct link to Fallback Sender Behavior for Transactional Emails")

While the above configuration customizes the sender and reply-to addresses, Freemius will apply a fallback to ensure deliverability in the following situations:

- Your domain is not authenticated with DKIM.
- The sender email does not belong to the authenticated domain.
- You are using a common email provider like Gmail or Outlook.

In these cases:

- The sender address will be `[email protected]`.
- The sender name will be `{{ productTitle }} via Freemius` (e.g., "Awesome Product via Freemius").
- The `reply-to` address will remain the email address configured in the Developer Dashboard.

This fallback ensures reliable delivery of important transactional commerce emails.

You can configure custom addresses and [authenticate your domain](help-documentation-marketing-automation-email-deliverability.md#domainkeys_identified_mail_dkim) to avoid this fallback behavior.