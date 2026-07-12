# Boost Conversions with Collected Ratings and Reviews

Displaying user ratings and reviews is a proven way to improve conversion rates by building trust and credibility with potential customers. However, collecting reviews can be a challenge, especially for new products or those with a small user base.

This guide explains how Freemius helps you automatically collect reviews out of the box, with no additional setup required. Comparable services often charge hundreds of dollars per month for similar functionality.

![Freemius developer dashboard list of reviews](/help/assets/ideal-img/freemius-developer-dashboard-reviews-section.311300e.480.png)

Freemius [automatically sends review request emails to customers](#verified-buyer-reviews) a week after their purchase. The review form is embedded in the email, making it easy for customers to submit their feedback without leaving their inbox.

Each time a customer submits a review, you will receive an email notification. This allows you to easily engage with the reviewer to thank them or request additional details.

## Reviews Collection[​](#reviews-collection "Direct link to Reviews Collection")

### Verified Buyer Reviews[​](#verified-buyer-reviews "Direct link to Verified Buyer Reviews")

A week after a purchase is made, Freemius automatically sends a MAP (Mail After Purchase) email to the customer, asking them to review your plugin or theme.

The review request email is sent only to verified buyers, which means that the reviews you receive through this channel are authentic and trustworthy. This can help you build credibility with potential customers and increase conversion rates.

To make it as easy as possible for customers to provide feedback, we use a technique that embeds the review form directly in the email.

![Freemius mail after purchase software review request received by the customer](/help/assets/ideal-img/freemius-mail-after-purchase-software-review-request.2bc8336.480.png)

This allows customers to review your plugin or theme without leaving their inbox, which has been proven to increase review conversion rates by more than 100%.

If the customer only submits a partial review from their email, they’ll be forwarded to a review form to complete the required details:

![Freemius two columns Software Review request with empty fields](/help/assets/ideal-img/freemius-2-column-software-review-request.cf9859d.480.png)

note

You can disable the automated review request emails if you prefer to collect reviews through other channels. To do this, follow [these steps](#disabling-automated-review-requests).

### Generating Review Links[​](#generating-review-links "Direct link to Generating Review Links")

If you want to send a review request email manually, edit an existing review or resend a request email that didn't reach the customer, you can generate a personalized review link for the customer and send it to them directly.

This allows you to easily collect reviews from customers who may have missed the initial email or prefer to receive the request through a different channel. To do this, follow these steps:

1. Log in to your [Developer Dashboard](https://dashboard.freemius.com).

2. Navigate to the ***Users*** page.

3. Click the specific user's email address to open their profile page.

4. Click the "**Get Review URL**" button under the user's personal details.

   This will generate a personalized link that you can send directly to the user. You can also open the link yourself to see what the review form looks like.

   ![Freemius developer dashboard - Get Review URL button](/help/assets/ideal-img/freemius-developer-dashboard-review-request-link.3e2e80a.480.png)

5. Send the generated link to the user through your preferred communication channel (e.g., email, chat, etc.) to request their review.

### WordPress.org Reviews[​](#wordpressorg-reviews "Direct link to WordPress.org Reviews")

Freemius automatically imports your most powerful recent reviews once a week from your WordPress.org plugin reviews. This helps you manage your best reviews from one centralized place.

If your product has a free version available on WordPress.org, verified reviewers who left a 5-star review will receive a personalized automated email. This is to encourage them to copy their review and repost it on WordPress.org. which will have a huge [impact on search ranking](blog-seo-on-new-plugin-repository.md).

![Email sent from Freemius to customer requesting for a review on wordpress.org](/help/assets/ideal-img/freemius-wp-org-review-request.f9e1d68.480.png)

## Managing Reviews[​](#managing-reviews "Direct link to Managing Reviews")

Our dashboard offers a comprehensive set of tools to help you manage your product reviews efficiently. Reviews can be manually added, edited, deleted, or marked as featured, and shareable cards can be created for use on social media.

### Manually Add Reviews[​](#manually-add-reviews "Direct link to Manually Add Reviews")

You can add reviews collected from various sources, one at a time, to your reviews list. This can be useful for reviews collected offline. To do this:

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the ***Reviews*** page from the left sidebar.
3. Click the "**+ Add Review**" button at the top of your product reviews list to add new reviews.
   <!-- -->
   ![Freemius developer dashboard - Manually add Review button](/help/assets/ideal-img/freemius-developer-dashboard-add-review.6647bc5.480.png)
4. Fill in the review details and click the "**Add Review**" button at the end of the editing panel to save the review.

### Manually Edit Reviews[​](#manually-edit-reviews "Direct link to Manually Edit Reviews")

Only manually added reviews or reviews imported from WordPress.org are editable. This also includes deleting a review if you want to remove it from your list. For integrity, verified buyer reviews collected from customers can only be edited by their reviewers. You can send them a message to ask for any necessary changes with the editing instructions and [link to the review form](#generating-review-links).

Here are the steps to edit a review that you added manually or imported from WordPress.org:

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the ***Reviews*** page from the left sidebar.
3. Click to select a review row (all review rows are clickable). This will open the editing panel from the right.
   <!-- -->
   ![Freemius developer dashboard managing reviews](/help/assets/ideal-img/freemius-developer-dashboard-managing-reviews.ca20a09.480.png)
4. Make the necessary changes and click away from the fields. Your changes will be saved automatically.

### Delete Reviews[​](#delete-reviews "Direct link to Delete Reviews")

If you want to delete a review, follow [steps 1-3 above](#manually-edit-reviews), then click the "**Delete**" button at the bottom of the editing panel. This will remove the review from your list, and it will no longer be visible on your in-dashboard pricing page or anywhere else you use it.

### Disabling Automated Review Requests[​](#disabling-automated-review-requests "Direct link to Disabling Automated Review Requests")

If, for any reason, you’d like to turn off the automated review request emails:

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Click the profile icon in the top-right corner.
3. Select the **Notifications** center from the dropdown.
4. Under the "**Ask customer/user to...**" section, toggle the relevant checkboxes. Your changes will be saved automatically.
   <!-- -->
   ![Freemius developer dashboard - Manage Reviews Notifications](/help/assets/ideal-img/freemius-developer-dashboard-manage-reviews-notifications.ba3c12d.480.png)

### Manage Reviews with Freemius API[​](#manage-reviews-with-freemius-api "Direct link to Manage Reviews with Freemius API")

This allows you to manage your reviews programmatically and integrate them with your existing systems and workflows. You can:

* [Create a review](https://docs.freemius.com/api/reviews/create) from your custom form or import from other sources.
* [Update a review](https://docs.freemius.com/api/reviews/update) if you want to edit a review that you added manually or imported from WordPress.org. For verified buyer reviews, see [link to the review form](#generating-review-links).
* [Delete a review](https://docs.freemius.com/api/reviews/delete) as needed.

## Using Reviews in Your Marketing Efforts[​](#using-reviews-in-your-marketing-efforts "Direct link to Using Reviews in Your Marketing Efforts")

After collecting reviews, you can use them in your marketing efforts. This can be done in several ways, including:

### Featuring Reviews[​](#featuring-reviews "Direct link to Featuring Reviews")

You can flag your best reviews as **"featured"**. This is a great way to leverage your positive reviews and build trust with potential customers when they are in the decision-making stage.

To mark a review as featured:

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the ***Reviews*** page from the left sidebar.
3. Click to select the relevant review row. This will open its editing panel.
4. Toggle the **Is Featured** button to mark the review as featured.
   <!-- -->
   ![Freemius developer dashboard - Marking a review as featured](/help/assets/ideal-img/freemius-developer-dashboard-managing-reviews.ca20a09.480.png)

This makes your reviews usable via:

1. The checkout [social proofing ui feature](https://freemius.com/help/help/documentation/checkout/features/social-proofing-ui/.md#displaying-reviews-or-testimonials), which displays reviews in the checkout.
   <!-- -->
   ![Freemius checkout social proofing UI](/help/assets/ideal-img/freemius-checkout-social-proofing-ui.db4e32a.480.png)
2. A testimonials carousel on your [WP In-dashboard pricing page](https://freemius.com/help/help/documentation/wordpress-sdk/features/wp-admin-in-dashboard-upgrading/.md).
   <!-- -->
   ![Freemius in-dashboard Reviews carousel with 3 panels showing star rating, review and customer profiles](/help/assets/ideal-img/freemius-in-dashboard-pricing-page-testimonials-carousel.6606fb6.480.png)

note

In the future, we also plan to include featured reviews in certain transactional emails (e.g., [Cart Abandonment Recovery](https://freemius.com/help/help/documentation/marketing-automation/cart-abandonment-recovery/.md) emails).

### Shareable Cards for Social Media[​](#shareable-cards-for-social-media "Direct link to Shareable Cards for Social Media")

For every review, you can create a shareable card that can be shared on social media channels. This is a great way to leverage your positive reviews and spread the word about your product.

1. Log in to the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Navigate to the ***Reviews*** page from the left sidebar.
3. On every review, there is a *Shareable Card* button that creates an image card.
   <!-- -->
   ![Freemius dashboard - Create Shareable Review Card](/help/assets/ideal-img/freemius-developer-dashboard-create-shareable-review.b86c091.480.png)
4. You can share these on your social media channels to spread the love you receive from your customers.
   <!-- -->
   ![Freemius dashboard generated sharable review card sample](/help/assets/ideal-img/freemius-sharable-review-card-example.a4ace09.480.png)

### Using the Freemius API[​](#using-the-freemius-api "Direct link to Using the Freemius API")

This can be particularly useful for displaying them on your website or in your marketing materials. It can be done through these API endpoints:

* [Reviews Summary](https://docs.freemius.com/api/reviews/retrieve-summary): to retrieve a summary of your reviews and rating.
* [Reviews List](https://docs.freemius.com/api/reviews/list): to retrieve a list of your reviews.
* [Review Detail](https://docs.freemius.com/api/reviews/retrieve): to retrieve the details of a specific review.

## FAQ[​](#faq "Direct link to FAQ")

### Do we need to ask for permission to use verified buyer reviews publicly?[​](#do-we-need-to-ask-for-permission-to-use-verified-buyer-reviews-publicly "Direct link to Do we need to ask for permission to use verified buyer reviews publicly?")

Verified buyer reviews are meant to be used publicly. When a customer reviews your product, they are effectively consenting for it to be made public after submission.

### How can I send a "thank you" to a customer who left a review?[​](#how-can-i-send-a-thank-you-to-a-customer-who-left-a-review "Direct link to How can I send a \"thank you\" to a customer who left a review?")

When a customer submits a review, you'll receive an email notification with the review's rating and content. The notification's `replyTo` email header is set to the customer's email address, so you can easily hit the reply button to message the customer.

warning

If you are replying from a support system, some systems strip the `replyTo` header, so make sure the address is not <dont-reply@freemius.com> before sending the message.

### Can I automate a "thank you" email to customers who leave a review?[​](#can-i-automate-a-thank-you-email-to-customers-who-leave-a-review "Direct link to Can I automate a \"thank you\" email to customers who leave a review?")

The easiest way to automate a "thank you" message to customers who leave a review is by leveraging your email client's filtering capabilities and setting an auto-responder template.

If, for some reason, your email provider doesn't support this functionality, you can [configure a webhook](https://freemius.com/help/help/documentation/saas/events-webhooks/.md), listen to the `review.created` event, and trigger any programmatic logic you wish.
