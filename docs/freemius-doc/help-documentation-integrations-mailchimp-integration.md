---
title: "MailChimp Integration"
url: "https://freemius.com/help/documentation/integrations/mailchimp-integration/"
source: "docs"
section: "Docs"
category: "3rd Party Integrations"
scraped_at: "2026-04-09T19:58:39+06:00"
word_count: 747
---

The *MailChimp* integration allows syncing user and/or customer emails directly with your *MailChimp* lists whenever certain events occur within your plugin or theme. Syncing the emails with your *MailChimp* is super easy! It doesn’t require any coding and only takes a few minutes:

1. Login to your [Freemius dashboard](https://dashboard.freemius.com/).
2. Navigate to **Integrations → MailChimp**:
3. Connect your Freemius plugin or theme with your MailChimp account:
4. Click on **Create New Rule**.
5. Tick the event types with which you would like to trigger the emails sync:
   
   You can access the documentation of the [events collection here](help-documentation-saas-events-webhooks.md).
6. Select the MailChimp list you’d like to sync the emails to.
7. If you prefer to sync the emails with any specific group, choose the group category and group.
8. Choose whether you’d like the rule to add the email to the list or remove it from the list:
9. Finally, don't forget to click save.

## MailChimp in the Prism of GDPR[​](#mailchimp-in-the-prism-of-gdpr "Direct link to MailChimp in the Prism of GDPR")

Freemius automatically manages a special property ( `is_marketing_allowed`) for each user (per product) to determine whether the user given their consent to receive marketing and promotional emails. When an email is added to your MailChimp through the Freemius integration, this property is synced too using a radio *merge field* named `FS_GDPR`:

Here’s how it looks like on MailChimp’s subscriber profile of a list:

When you’re setting up your next promotional marketing campaign, make sure that you create a proper segment where you only target subscribers that have their “Freemius GDPR” field set to `yes`:

![Freemius MailChimp GDPR-based segmentation](/help/assets/images/freemius-mailchimp-gdpr-based-segmentation-147ebd71840d84d29f005a700822b486.gif)

Keep in mind that while you are not allowed to send pure marketing offers (e.g. seasonal discounts) to subscribers who’ve not opted-in (their `FS_GDPR` field is not equal to `'yes'`), you can still email product-related announcements, security-related messages, and other non-promotional emails.

**Important:** The marketing flag sync is one-directional. Updates in Freemius will be reflected inside MailChimp, but not the other way around. So if a user unsubscribes from your MailChimp list, Freemius will not be aware of that! To achieve a bidirectional sync, you can leverage MailChimp’s webhooks mechanism to trigger corresponding calls to [our API](https://docs.freemius.com/api/).

## MailChimp + Freemius Best Practices[​](#mailchimp--freemius-best-practices "Direct link to MailChimp + Freemius Best Practices")

MailChimp's pricing is based on the number of subscribers in all lists combined. When the same email address is included in multiple lists, it counts as **multiple subscribers**. Therefore, whether you are selling a single plugin/theme, or have a shop with multiple products, in most cases, setting up a single list for all of your subscribers is good enough and a great way to save some money. Then, you can leverage MailChimp's groups and categories to associate the subscribers with their respective prodct(s) and target your email marketing campaigns at the right people.

### A Step-By-Step List and Groups Configuration[​](#a-step-by-step-list-and-groups-configuration "Direct link to A Step-By-Step List and Groups Configuration")

1. Go to [MailChimp](https://mailchimp.com/) and login.
2. Create a list named `My WordPress Shop` (or any other name).
3. Under the list management, go to **Manage Contacts → Groups**, and click **Create Groups**.
4. Use your product's name for the **Group Category** (e.g. `My Awesome Plugin`).
5. Then, add the following **Group names**: `Active`, `Inactive`, `Paying`, `Customers`, `Uninstalled`, `Trial Period`. It should look something like this:
6. Lastly, click **Save**.
7. Repeat steps 3-6 for every different product that you sell through Freemius.

### The Freemius-recommended MailChimp Rules[​](#the-freemius-recommended-mailchimp-rules "Direct link to The Freemius-recommended MailChimp Rules")

Login to your [Freemius dashboard](https://dashboard.freemius.com/) and go to **Integrations → MailChimp**.

Start creating the following rules:

01. Add email to `My WordPress Shop/My Awesome Plugin/Active` after `install.installed`, `install.activated`, or `install.user.opt_in`.
02. Add email to `My WordPress Shop/My Awesome Plugin/Paying` after `payment.created`.
03. Add email to `My WordPress Shop/My Awesome Plugin/Customers` after `plan.lifetime.purchase`, `subscription.created`, or `license.extended`.
04. Add email to `My WordPress Shop/My Awesome Plugin/Trial Period` after `install.trial.started` or `install.trial.extended`.
05. Add email to `My WordPress Shop/My Awesome Plugin/Inactive` after `install.deactivated`.
06. Add email to `My WordPress Shop/My Awesome Plugin/Uninstalled` after `install.uninstalled`.
07. Remove email from `My WordPress Shop/My Awesome Plugin/Active` after `install.deactivated`, `install.uninstalled`, `install.deleted`, or `install.user.opt_out`.
08. Remove email from `My WordPress Shop/My Awesome Plugin/Paying` after `license.expired` or `license.cancelled`, or `install.user.opt_out`.
09. Remove email from `My WordPress Shop/My Awesome Plugin/Trial Period` after `install.trial.cancelled`, `install.trial.expired`, or `install.user.opt_out`.
10. Remove email from `My WordPress Shop/My Awesome Plugin/Inactive` after `install.installed`, `install.activated`, or `install.user.opt_out`.
11. Remove email from `My WordPress Shop/My Awesome Plugin/Uninstalled` after `install.installed`, `install.activated`, or `install.user.opt_out`.