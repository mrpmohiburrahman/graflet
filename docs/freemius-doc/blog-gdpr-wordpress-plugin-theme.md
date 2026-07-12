As you all know, the [EU *General Data Protection Regulation* (GDPR)](https://www.eugdpr.org/) takes effect today! (May 25th, 2018). It aims to protect fundamental privacy rights and the personal data of European Union residents.

While they were 4 long and tiring weeks of full-time work towards GDPR compliance, in which almost all of our team took part in the efforts, we’re now ready to meet the new standards for the data privacy.

On a personal note, I’m super excited about the results and the tools that we’ve added to help you get ready as well!

**Disclaimer:** Before we get to it, please note that I’m not a lawyer and this is not legal advice. This article covers the best-practice we used and recommend for others to use in order to comply with the GDPR. That said, we can’t cover everything here, and you should definitely get some professional counseling on the subject.

## What does GDPR mean for the Freemius team?

In addition to tidying up our policies and preparing our products line, based on the GDPR requirements, we invested many efforts in providing you, our sellers and users, with as seamless as possible tools, product adjustments, and processes to help you get ready for GDPR. And the good news is that we’ve managed to do most of the heavy lifting for you 😉

## What Has Freemius Done to Be GDPR Ready?

- We worked on a new & shiny [Cookies Policy](https://freemius.com/privacy/cookies/) where we describe the functionality of all our 1st Party and 3rd Party Cookies. We’ve also added a one-click Opt-out button from our 1st Party cookies, as well as links to the 3rd party services’ cookies policies which have their own opt-out options.
- We’ve enriched our [Privacy Policy](privacy.md) with information on our privacy practices, including storage, processing, retention, and use of personal information.
- We crafted a [Data Processing Addendum (DPA)](https://freemius.com/terms/dpa/) to govern Freemius’ and your handling of personal data. It is now part of our [Vendor Terms of Service](https://freemius.com/terms/vendor/).
- We’ve added a cookies consent mechanism to all of our user-facing assets: Website, Blog, Knowledge Base, In-Dashboard Pricing, Checkout, Dashboard. Identifiable cookies are no longer created for EU visitors during the 1st time they visit any of the assets, without their explicit consent. More on that below.
- Our daily Database backups are now encrypted before they are stored on AWS S3. We use a different encryption key for every backup and the keys are stored on a different server. So even if AWS S3 is hacked, the attacker would still end up with encrypted, useless data in his hands..

## A Cookies Consent Mechanism for EU Visitors

GDPR’s strengthened requirements make it much harder to obtain legal consent for identifiable cookies. Implied consent is no longer sufficient, so messages like *‘By using this site, you accept cookies’* are no longer an option. An explicit consent must be collected using a clear affirmative action, like clicking on an “opt-in” button. Most 3rd party services, such as Google Analytics, automatically generate an identifiable cookie for tracking, right when their JS snippet is included. This is also relevant for chat widgets, retargeting pixels, social sharing buttons, and more.

Removing those valuable services, even if only for EU visitors, was not an option since those services are vital for our business. So we had to come up with a creative solution. The reason I’m mentioning this is because it’s probably relevant to your website as well, and can help you with GDPR compliance.

### Geolocation Identification

First and foremost, as a US-based business, we didn’t want to affect the UX for all visitors. The EU GDPR is relevant for EU visitors, so the first thing we had to do is identify who our EU based visitors are. Luckily, we’ve been using CloudFlare for years as our CDN, firewall, and an additional security layer. One of their perks is a [geolocation identification](https://support.cloudflare.com/hc/en-us/articles/200168236-What-does-Cloudflare-IP-Geolocation-do-). When turned on, a new HTTP header with the visitor’s 2-chars country code is added to all of your requests and can easily be consumed using PHP as follows:

```
$_REQUEST['HTTP_CF_IPCOUNTRY']
```

I highly recommend their service. They have a rich free-tier and the geolocation identification is included!

Once you have a mechanism to identify the country code, we can add a global JavaScript variable that will “tell” us whether the current visitor is located at the EU or not and we can use it on different parts of our client-side code:

```
<script type="text/javascript">
(function () {
window.__is_eu = <?php echo is_eu_visitor() ? 'true' : 'false'; ?>;
}());
</script>
```

**Important:**

1. EU-based businesses may be required to collect a cookies consent from all their visitors. Please advise with an attorney/professional.
2. To keep leveraging CloudFlare’s CDN layer, the [*cache key*](https://support.cloudflare.com/hc/en-us/articles/115004290387-Using-Custom-Cache-Keys) must be customized to incorporate the geolocation of the traffic source. That way, we keep the caching layer and make sure that a visitor from the EU won’t get a cached version of a visitor from outside the EU. This is the cache key we’re using: ${geo}::${scheme}://${host\_header}${uri}

### Conditional Tracking Scripts Inclusion

We’ve developed a small JavaScript [*Script Management* library](https://js.freemius.com/fs/script-manager.js), which uses jQuery and a [*JavaScript Cookie*](https://github.com/js-cookie/js-cookie) (lightweight JavaScript cookies API), to act as the “brain” and gateway for cookies when it comes to 3rd party scripts injection for services that generate identifiable cookies upon their inclusion.

A typical 3rd-party service JavaScript snippet will look like this (this is Twitter’s Tag snippet):

```
<script type="text/javascript">
!function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);
},s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='//static.ads-twitter.com/uwt.js',a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');
twq('init','YOUR-TWITTER-ID');
twq('track','PageView');
</script>
```

To leverage the *Script Management* lib, instead of including the 3rd party snippet to the page, we’ll register it with the script manager as follows:

```
<script type="text/javascript">
FS.Scripts.addTrackingScript(function() {
// 3rd party JS snippet goes here
});
</script>
```

When a page is loaded:

- If the visitor is not from the EU, the registered 3rd party scripts will execute immediately.
- If the visitor is from the EU or if they opted-out of cookies via our Cookies Policy page (`FS.Scripts.optOut()`), the 3rd party scripts will remain in the pending queue and no cookies will be created during that pageview, giving the visitor an opportunity to act before cookies are set on the first visit to a site.
- If a visitor opts-in to cookies (`FS.Scripts.optIn()`), the registered scripts will be executed.
- If an EU visitor continues browsing without opting-in, ignoring the cookies opt-in message, that would be considered as a “soft opt-in” consent, and the cookies and scripts will be included.

## How Does Freemius Help You Be GDPR Ready?

Our sellers and [*Freemius Insights*](wordpress-insights.md) users rely on Freemius as an emails capture tool for various reasons, including promotional email marketing. After reviewing the default opt-in messages delivered in our [WordPress SDK](https://github.com/freemius/wordpress-sdk) with a lawyer, we understood that while the copy is sufficient for marketing soft-opt-in, it’s insufficient for EU visitors. Also, EU customers that purchased plugins and themes via our checkout without opting-in, didn’t explicitly consent to promotional emails, which is required by the GDPR. Here’s what we’ve done to help you filter users that are good for promotional marketing emails:

### Introducing The `is_marketing_allowed` Flag

We’ve added a new property to each user (per product) that can have one of the following 3 values:

1. `'yes'` – means that you can send promotional emails to the user.
2. `'no'` – means that the user explicitly opted-out from marketing emails. You can still email announcements, security and feature updates, and other, non-promotional content.
3. `null` – means that the user still didn’t indicate whether they are willing to receive promotional emails or not.

This flag is now populated right on the user’s profile page in the Freemius Dashboard:

![freemius dashboard user profile is marketing allowed flag](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-dashboard-user-profile-is-marketing-allowed-flag.png)

We made the option editable for developers so you can modify the flag for cases where a user explicitly asks you to opt-in/out, giving you the freedom to control the state. We’ve also added a new column to the USERS section of the dashboard so you can quickly see the status of the flag right in the table:

![the status of the flag](https://freemius.com/blog/wp-content/uploads/2018/05/the-status-of-the-flag.png)

Also, when you export the users’ list via the Freemius Dashboard, the flag will be included as part of the generated CSV file so you can easily filter your spreadsheet based on that flag.

### Adding Marketing Opt-In To Freemius Checkout

Exactly a month ago (April 25th, 2018), we’ve released an update to our checkout that prompts EU residents with a mandatory field where they have to choose whether they are interested in promotional emails or not:

![freemius checkout gdpr opt-in](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-checkout-gdpr-opt-in.png)

The extra field will only be shown to EU users that have never opted-in before. If an EU-based customer had already provided their consent once, then the opt-in consent section will not be shown on the next time they will check out.

This selection basically controls the new `is_marketing_allowed` mentioned earlier.

### “Reverse Engineering” The Marketing Flag

Luckily, we’ve been tracking the geolocation of users to help you track the geo-distribution of your user base. We’ve automatically set the marketing flag to `yes` for those users. So as of today, the flag is set to `yes` for all users/customers that are not from the EU, and for customers that are from the EU that purchased after April 25th and have explicitly chosen to opt-in to promotional emails. The flag will be set to ‘no’ for all EU customers that purchased after April 25th and explicitly asked to not receive promotional emails. Lastly, it will be set to `null` for the rest of the EU users.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

### New WordPress SDK for Collecting Proper Marketing Consent From EU Users

To help you comply with the GDPR, we have just released [version 2.1.0](https://github.com/Freemius/wordpress-sdk/releases/tag/2.1.0) which incorporates key updates to the SDK for GDPR. Please update your plugin/theme with the newest SDK version asap. Like always, make sure that you test it thoroughly before the release.

#### A New Opt-In Message for EU Users

The default opt-in message was adjusted for EU users, making it clearer that they are also opting-in to potential marketing and offers via email. Once you upgrade to the new SDK, the marketing flag will be automatically set to `yes` for all new users that opt-in.

Here’s the phrasing we use for new EU users:

> Never miss an important update – opt-in to our security & feature updates notifications, educational content, offers, and non-sensitive diagnostic tracking with freemius.com.

**IMPORTANT**: If you’re overriding the default opt-in message with a custom one, please make sure to adjust it for EU users, making it clear that they are also opting-in to promotional emails. To help you identify EU users, we’ve introduced a helper method, which you can use in your opt-in message filter:

```
FS_GDPR_Manager::instance()->is_required()
```

### Gradual Marketing Consent Capture for Existing EU Users

#### Marketing Consent During License Activation

The license activation is now a 2-step mechanism. Once a user types in a license key, the 1st thing that will happen is an AJAX call that will ping our API to check if the marketing flag has already been set for the owner of that license. If not, an opt-in radio button will appear and the user will have to indicate if they wish to opt-in to marketing or not:

![The gdpr opt-in](https://freemius.com/blog/wp-content/uploads/2018/05/gdpr-opt-in.gif)

#### Marketing Consent Admin Notice for Opted-in EU Users

A new friendly admin notice will be shown to EU users that already opted-in before and their marketing flag is not set (or set to `null`), to encourage them to opt-in to marketing emails.

![Freemius sdk GDPR opt-in admin notice](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-sdk-gdpr-opt-in-admin-notice.png)

- To avoid a flood of admin notices, if the logged in EU admin opted-in to multiple plugins and themes on the same WordPress install, the SDK will only show a single collective message for all the products and the decision taken by the user will affect their marketing flag for all those products.
- If the admin chooses to dismiss the message it will reappear every 30-days until a decision is taken (`'yes'` or `'no'`), or if the marketing flag will be updated via one of the other mechanisms.

**IMPORTANT**: The admin notice consent collection is off by default since we didn’t want to force you to use it. To activate it, add the following filter handler right after your integration snippet:

```
my_freemius()->add_filter( 'handle_gdpr_admin_notice', '__return_true');
```

We’ve created a gist to help you customize this GDPR message:

[https://gist.github.com/vovafeldman/54fbc08635f66fd09b7d530cb027cc87](https://gist.github.com/vovafeldman/54fbc08635f66fd09b7d530cb027cc87)

## MailChimp Integration

If you’re using the [Freemius MailChimp integration](help-documentation-integrations-mailchimp-integration.md) we’ve got great news for you! The marketing flag was already synced with all your previously added subscribers and will keep syncing automatically, as long as your Freemius MailChimp rules are set and active.

The flag is synced using a new radio merge field named `FS_GDPR`:

![Freemius MailChimp gdpr merge field](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-mailchimp-gdpr-merge-field.png)

Here’s how it looks like on MailChimp’s subscriber profile of a list:

![MailChimp subscriber profile](https://freemius.com/blog/wp-content/uploads/2018/05/MailChimp-subscriber-profile.png)

When you’re setting up your next promotional marketing campaign, make sure that you create a proper segment where you only target subscribers that have their “Freemius GDPR” field set to `yes`:

![Freemius MailChimp GDPR-based segmentation](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-mailchimp-gdpr-based-segmentation.gif)

Keep in mind that while you are not allowed to send pure marketing offers (e.g. seasonal discounts) to subscribers who’ve not opted-in (their `FS_GDPR` field is not equal to `'yes'`), you can still email product-related announcements, security-related messages, and other non-promotional emails.

**Important**:

1. If the sole source of your MailChimp subscribers is Freemius, there’s no need to email-blast everyone asking for their consent. If you have subscribers from other sources and you would like to get their consent, you can target non-Freemius subscribers using the Signup Source filter in the segmentation functionality:  
   ![MailChimp Signup Source filter](https://freemius.com/blog/wp-content/uploads/2018/05/MailChimp-Signup-Source-filter.png)
2. The marketing flag sync is one-directional. Updates in Freemius will be reflected inside MailChimp, but not the other way around. So if a user unsubscribes from your MailChimp list, Freemius will not be aware of that! To achieve a bidirectional sync, you can leverage MailChimp’s webhooks mechanism to trigger corresponding calls to [our API](https://freemius.docs.apiary.io/).
3. The MailChimp integration is not included for users on the free plan that are not monetizing with Freemius. So even if you’ve been a paying customer before and are now on the free plan, we’ll not sync the marketing flag with subscribers that were previously generated via the integration.

## Freemius Checkout

Like any other checkout, our checkout uses cookies as well. Therefore, we’ve implemented a *blocking overlay cookies consent* for the in-dashboard checkout (in their WordPress admin):

![Freemius dashboard checkout cookies consent](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-dashboard-checkout-cookies-consent.png)

We decided not to activate this overlay when using Freemius Checkout on your site and let you handle the cookies consent logic. That way you have the freedom to implement the cookies consent as you see fit.

### Updates To Your Cookies Policy

If you’re using Freemius Checkout on your site you’ll need to include a paragraph mentioning that you’re using the Freemius service, which uses cookies for order fulfillment, security, fraud detection & prevention. You’ll also need to include a link to our checkout cookies policy ([https://freemius.com/privacy/cookies/checkout/](https://freemius.com/privacy/cookies/checkout/)) and a mention that they can opt-out of our cookies on that page. We’ve crafted a short paragraph which you can use:

*We sell our product(s) using Freemius secure checkout, which enables secure online payments, licensing, fulfillment, and more. The service automatically adds cookies when a user opens the checkout. Those are essential cookies for security, fraud detection & prevention, and completion of a purchase. There’s no way to check out without letting the service use cookies.*

Here’s a link to the [Freemius privacy policy](privacy.md) and its [checkout cookie policy](https://freemius.com/privacy/cookies/checkout/). If you wish to opt-out of Freemius’ cookies setting please go to their [cookie policy](https://freemius.com/privacy/cookies/checkout/) and follow their opt-out instructions.

## Handling a Subject Access Request (SAR)

If you receive a request to export a certain EU user’s data, please forward the request over to [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#a3d0d6d3d3ccd1d7e3c5d1c6c6cecad6d08dc0ccce) and we’ll export it into a JSON format and send it to the user in a timely manner. As we are already working on the members’ area, we’ll include a robust option where users will be able to export their data themselves, directly from the dashboard.

## Erasure

Users can erase their data from the “My Profile” section in the User Dashboard, or by requesting us (via [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#d9aaaca9a9b6abad99bfabbcbcb4b0acaaf7bab6b4)) or the product team to do it from their end.  
Please note that things are a bit trickier for users who purchase products through Freemius. As a US-based company, we are obligated to retain customer data for six years for potential IRS audits. To maintain privacy in this case, when paying customers request to remove user data, it is flagged as “deleted” and is scheduled for erasure.  
Here’s the supporting clause from the [European Commission](http://europa.eu/rapid/press-release_MEMO-17-1441_en.htm):  
”This does not mean that on each request of an individual all his personal data are to be deleted at once and forever. If, for example, the retention of the data is necessary for the performance of a contract, or for compliance with a legal obligation, the data can be kept as long as necessary for that purpose.”

While in “deleted” state, the data is no longer available to anyone, anywhere. It is only accessed by our team if we are legally obliged to retain it, or if the customer requests that we recover their account.

## Cart Abandonment Recovery

We’ve been closely watching at how companies like CartHook and Jilt address the EU GDPR compliance. Right now, it still seems to be a “loose end”. There are several interpretations of the GDPR requirements in regard to cart recovery emails. If we consider abandonment cart emails as transactional emails, then based on what those companies claim, collecting consent is not required due to the following two lawful bases:

1. Fulfillment of a contract
2. Legitimate interest

**Bottom line:** for now we’re not touching our [Cart Abandonment Recovery](help-documentation-marketing-automation-cart-abandonment-recovery.md) mechanism. This is the core business of some companies and they are already investing lots of dollars into legally figuring out this puzzle, so we’ll keep watching for updates and iterate based on their findings.

**Update: May 27th, 2018**  
We’ve added a clear notice right next to the email input to let the user know about the cart tracking with the ability to opt out with one-click:  
![Freemius Checkout GDPR Cart Opt-Out](https://freemius.com/blog/wp-content/uploads/2018/05/freemius-checkout-cart-opt-out.png)

## Final Notes

The EU GDPR has forced organizations to be more careful about what type of personal data is collected and processed, which is a good move that we at Freemius welcome and embrace! If you have any questions don’t hesitate to email us at [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection) or join the #gdpr channel on our closed Slack group [https://freemiusdev.slack.com](https://freemiusdev.slack.com)