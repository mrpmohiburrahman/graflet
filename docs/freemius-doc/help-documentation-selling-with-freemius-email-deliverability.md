Freemius uses SendGrid for sending all the transactional emails to users and customers. While their deliverability performance is outstanding, from time to time, emails may fail to get delivered to your users’ mailbox for various reasons like:

- The user’s email server flags a message as spam
- The user’s WP Admin email is an invalid email address
- The user’s mailbox is full
- The user’s email address has a typo

## Increasing Emails Deliverability[​](#increasing-emails-deliverability "Direct link to Increasing Emails Deliverability")

### DomainKeys Identified Mail (DKIM)[​](#domainkeys-identified-mail-dkim "Direct link to DomainKeys Identified Mail (DKIM)")

> [DKIM](https://sendgrid.com/blog/what-is-dkim/) stands for DomainKeys Identified Mail which was designed to help ISPs prevent malicious email senders by validating email from specific domains.

We highly recommend authenticating your domain using DKIM to minimize email deliverability issues.

1. Login to the [Developer Dashboard](https://dashboard.freemius.com).
2. Navigate to the ***Emails*** section.
3. Click the **Authenticate Domain with DKIM** button to initiate the authentication process.
4. Fill in the domain you intend to send emails from and click **Authenticate**:
5. SendGrid will create a set of CNAME records you'll need to add to your host's DNS section:
6. Once all records are added, check the "I've added these records" checkbox and click **Verify**.

### SPF Records[​](#spf-records "Direct link to SPF Records")

Once you complete the DKIM setup, Freemius handles SPF automatically. No additional configuration is required on your end.

Any existing SPF records on your root domain will not conflict with your Freemius integration.

## Handling Deliverability Issues[​](#handling-deliverability-issues "Direct link to Handling Deliverability Issues")

If you receive an email from a customer saying they have just upgraded their license and haven’t received their license key plus download link. Here’s what you need to do in such a scenario:

1. Open the [Freemius dashboard](https://dashboard.freemius.com) and go to ***Users***.
2. Search for the email address of the customer.
   
   tip
   
   If you can’t find a user with that address, ask the customer to confirm the email address they used for the upgrade. If they’ve upgraded from within their WP Admin, ask them for the email address that is associated with their WP user and search for that address.
3. Once you find the user, open their profile by clicking their email address.
4. Scroll to the **Emails Log** section. Click the dropdown icon to expand the section while loading the emails activity log:
   
   warning
   
   SendGrid’s email activity logs are stored only for 30 days. If you get an empty email logs list, it means that there were no attempts to send any emails during the past 30 days.
5. After the emails log loads you’ll notice a status column. If the status of the messages is `delivered` then the emails were successfully delivered to the user: Ask the customer to search their mailbox and check their spam folder. If the status is different like in the image below: Click the **Action** button next to it and wait for the bounce logs to load.
6. Once the dialog is loaded, you will see the deliverability failure reasons: If the issue is related to the customer’s email server, contact the customer to let them know about the issue so that they can contact their email provider for a solution.
7. After confirming with the customer that the deliverability issue was resolved, hit the **Resend Message** to remove the address from the "Blocked" list.
8. Direct the customer to recover their license key and secure download link using the [License Recovery Self-Service tool](help-documentation-wordpress-license-recovery-tool.md#product-specific-license).