As part of our ongoing efforts to help plugin and theme developers optimize the support experience for their customers, we’re excited to share a brand new contact form in the hosted Customer Portal, which can be embedded into your website if you’re selling with Freemius. This will allow your users and customers to contact support directly from the comfort of your branded site or their own embedded self-service portal.

As we approached the challenge of optimizing the contact form, we set ourselves a goal to build an exceptional user experience that auto-surfaces relevant information – such as documentation – all with the goal of reducing the number of tickets you receive and the average time to resolution.

![Freemius User Dashboard Contact Form](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form.png)

As we’re always thinking about how we can help you grow your bottom line, we kept in mind that a contact form is an excellent place for encouraging free users to become paying customers.

Therefore, the new contact form is integrated with:

- Contextual Categories
- FAQ
- Refund Policy
- Help Scout Docs (if you use it)
- Public Knowledge Base
- Freemius Checkout

As this is a new capability, we had the privilege to design the user experience (and UI) from scratch. We reviewed dozens of contact forms in the plugin and theme space, collected valuable feedback from several of our selling makers (thanks guys!), and got inspired by advanced contact forms from companies like Google.

I’m excited to share what we came up with! But first, let me show you how to enable the contact form for your users.

## How to enable the Contact Form for your Customer Portal

We realized that some of you would prefer to stick with their own contact forms, so if you [embedded the Customer Portal](https://freemius.com/help/documentation/users-account-management/users-dashboard/) on your site, the contact form menu item is hidden by default.

You can learn how to [activate the contact form for your portal here](help-documentation-users-account-management-support-contact-form.md#how_to_enable_the_contact_form_in_the_user_dashboard).

## Contextual Categories

Instead of overwhelming users with all possible support categories, the new contact form dynamically shows different categories according to the selected product and their unique user information.

For example, a “Trial Extension” category will only appear for products offering free trials:

![Freemius User Dashboard Contact Form Trial Extension](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form-trial-extension.png)

We plan to keep improving this as we go, making it more intelligent over time.

## FAQ Integration

Upon a category and subcategory selection, the contact form will automatically reveal the relevant questions and answers from the FAQ, when applicable:

![Freemius User Dashboard Contact Form FAQ Integration](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form-faq-integration.png)

## Refund Policy Integration

When a customer indicates that they are contacting support for a refund, a short human-readable summary of the refund policy will reactively appear to remind the customer what they agreed to when purchasing your product:

![Freemius User Dashboard Refund Request and Policy Integration](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-refund-request-and-policy-integration.png)

If you still haven’t noticed, the most common refund request is for subscription renewals.

We hope that the policy reminder (which highlights the fact that renewals are generally not refundable) will reduce the number of customers asking for refunds.

## Help Scout Docs Integration

As many of you are using Help Scout and have already documented many product-specific topics, we decided to integrate the contact form with [Help Scout Docs](https://www.helpscout.com/knowledge-base/) in order to [auto-populate relevant articles](help-documentation-users-account-management-support-contact-form.md#help_scout_docs_integration) directly from your knowledge base:

![Freemius User Dashboard Contact Form Help Scout Integration](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form-helpscout-docs.gif)

Overall, access to the docs in the contact form should lessen the support load for many products considerably.

You can learn how to [activate the contact form Help Scout Docs integration here](help-documentation-users-account-management-support-contact-form.md#help_scout_docs_integration).

## Public Knowledge Base Integration

Whether you use Help Scout Docs or any other publicly available knowledge base, we now encourage users to check your docs while waiting to hear back from support:

![Freemius User Dashboard Contact Form Check documentation while waiting](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form-check-documentation-while-waiting.png)

To enable this capability, you’ll just have to enable the *“Knowledge Base”* switch in any of your product’s plans, and include the link to your knowledge base:

![Freemius Developer Dashboard Plans Knowledge Base URL](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-developer-dashboard-plans-knowledge-base-url.png)

## Freemius Checkout Integration

If you are not offering free support, you’ll notice that support-related categories are now highlighted as PAID ONLY, making it clear to users that they need to be a paying customer to receive support.

If the user chooses to ignore that, all the integrations mentioned above will continue functioning, trying to surface all the relevant data to help the user in a self-served approach. But, if the user attempts to pursue a ticket, they’ll be prompted with a dialog box explaining that they need to purchase (or renew) a license first.

If they choose to buy a license, the checkout will be opened right on the spot, offering them an uninterrupted experience until the submission of their ticket, without even leaving the page!

![Freemius User Dashboard Contact Form Contextual Upsell](https://freemius.com/blog/wp-content/uploads/2020/06/freemius-user-dashboard-contact-form-contextual-upsell.gif)

## Customizations

Since we understand that you may want to hide some of the contact form categories, we assigned a unique `id` attribute to every category, to allow you [custom control of its visibility via CSS](help-documentation-users-account-management-support-contact-form.md#customizations).

## What’s next?

We have tons of new features & capabilities that are already in development and planned to be shipped soon, including:

- 2FA / Two-Factor Authentication with an authentication app to better secure your accounts.
- Brute force attack protection with reCAPTCHA.
- Entire revamp of the earnings page, which will simplify the understanding of the data and will also include earnings predictions!
- Self-serve DKIM domain authentication.
- Special coupons for increasing CTR and reducing churn.
- An affiliate application form that will be introduced in the Customer Portal.

You might be wondering – “What’s the progress with the store-level Developer Dashboard?”

Due to the complexity of that project and since we more than doubled our engineering team, to maintain the same high-level of code quality & testing, we asked our senior devs to temporarily shift their focus from that task to code review and training.

Therefore, unfortunately, the store-level Developer Dashboard is delayed. We haven’t forgotten about it – not at all – and we hope to get back to it in full force by the end of June.