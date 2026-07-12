---
title: "Support Integration in the Customer Portal"
url: "https://freemius.com/help/documentation/users-account-management/support-contact-form/"
source: "docs"
section: "Docs"
category: "Customer Portal"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 765
---

## How to enable the Contact Form[​](#how-to-enable-the-contact-form "Direct link to How to enable the Contact Form")

To activate the contact form,

1. Log into your [Freemius Developer dashboard](https://dashboard.freemius.com/).
2. Navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
3. Select your store by name.
4. Scroll down the menu and select the **Settings** page.
5. Under the Customer Portal sub-page, scroll to the **Support Form** section.
6. Toggle the *Show support contact form* switch on:
7. Refresh the Customer Portal, and you should see the new “Support” menu item.

### Contextual Categories[​](#contextual-categories "Direct link to Contextual Categories")

The contact form dynamically shows different categories according to the selected product and user information.

For example, a “Trial Extension” category will only appear for products offering free trials:

We plan to keep improving this as we go, making it more intelligent over time.

### FAQ Integration[​](#faq-integration "Direct link to FAQ Integration")

Upon a category and subcategory selection, the contact form will automatically reveal the relevant questions and answers from the FAQ, when applicable:

### Refund Policy Integration[​](#refund-policy-integration "Direct link to Refund Policy Integration")

When a customer indicates they are contacting support for a refund, a short human-readable summary of the refund policy will reactively appear to remind the customer what they agreed to when purchasing your product:

The commonest refund request is for subscription renewals. So, we hope that the policy reminder, which highlights that renewals are generally not refundable, will reduce the number of customers asking for refunds.

### Help Scout Docs Integration[​](#help-scout-docs-integration "Direct link to Help Scout Docs Integration")

If you integrate the contact form with Help Scout Docs, you can auto-populate relevant articles directly from your knowledge base:

To enable the integration of the contact form with your Help Scout Docs, head to ***Integrations*** -&gt; ***Help Scout*** in the Developer Dashboard, and set your Docs API Key:

More information can be found [here](help-documentation-integrations-help-scout.md).

note

If you are not using Help Scout for your documentation center, we plan to enrich the capability for custom API endpoints to search documents.

### Public Knowledge Base Integration[​](#public-knowledge-base-integration "Direct link to Public Knowledge Base Integration")

Whether you use Help Scout Docs or any other publicly available knowledge base, we now encourage users to check your docs while waiting to hear back from support:

To enable this extra capability, you’ll need to enable the “Knowledge Base” switch in any of your product’s plans, and include the link to your knowledge base:

### Freemius Checkout Integration[​](#freemius-checkout-integration "Direct link to Freemius Checkout Integration")

If you are not offering free support, you’ll notice that support-related categories highlighted as **PAID ONLY**, making it clear to users that they need to be a paying customer to receive support.

If the user chooses to ignore that, all the integrations mentioned above will continue functioning, trying to surface all the relevant data to help the user in a self-served approach. But, if the user pursues a ticket, they’ll be prompted with a dialog box explaining they need to purchase (or renew) a license first. If they choose to get a license, the checkout will be opened right on the spot, offering them an uninterrupted experience until the submission of their ticket without even leaving the page!

## Customizations[​](#customizations "Direct link to Customizations")

### Link to Your Own Support Page[​](#link-to-your-own-support-page "Direct link to Link to Your Own Support Page")

If you'd like to link to your own support page instead of using the built-in form, you can configure it from your store settings.

1. Log into your [Freemius Developer dashboard](https://dashboard.freemius.com/).
2. Navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
3. Select your store by name.
4. Scroll down the menu and select the **Settings** page.
5. Under the Customer Portal sub-page, scroll to the **Support Form** section.
6. Fill in the URL of your external support page.
7. When a customer accesses support from the Customer Portal, they will see a **Continue** button that opens your custom support page in a new tab.

### How to hide selected categories of the contact form[​](#how-to-hide-selected-categories-of-the-contact-form "Direct link to How to hide selected categories of the contact form")

Each category of the contact form is assigned with a unique `id` attribute. These attributes allow you to easily hide any category using your [custom CSS stylesheet set in the “My Store” configuration page](help-documentation-users-account-management-applying-css-customization.md#adding-your-custom-css).

For example, the “Technical Support” category’s unique `id` is `contact__technical_issue` enabling you to hide the category using:

```css
#contact__technical_issue {
  display: none;
}
```

tip

Learn how to [embed the Customer Portal](help-documentation-users-account-management-embedding-customer-portal.md) right into your website.