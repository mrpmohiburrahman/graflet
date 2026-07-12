For many plugin and theme shops, Strong Customer Authentication (SCA) has been a hot topic in recent months. So what exactly is all the noise about and why is it relevant to WordPress product developers?!

Let’s start with a bit of background.

SCA rose out of the European Union’s (EU) goal to secure online payments, which is a pretty good goal for everyone, right? We all want to have secure online payments that protect the legitimacy of purchases in eCommerce.

In order to achieve the goal of securing online payments and minimizing fraud, the EU has released two “Payment Services Directives” – PSD1 and PSD2 – and no, these aren’t new photoshop formats. PSD2 initially gave businesses in EU countries until Sept 14, 2019 to implement secure solutions for online payments that meet SCA requirements.

These requirements were not well received by many groups, especially [major credit card companies like Visa](https://www.visa.co.uk/partner-with-us/payment-technology/strong-customer-authentication.html) and other [payment institutions](https://paymentinstitutions.eu/pressroom/joint-industry-statement-on-sca-implementation/) in Europe, who [jointly signed a statement](https://paymentinstitutions.eu/wp-content/uploads/2019/08/Join-industry-Statement-on-SCA-Implementation.pdf) explaining the major challenges in the transition to securing payments with 2 factor authentication (2FA – required for many payments under SCA) and officially requesting an implementation period of 18 months.

In response, the European Banking Authority (EBA) [released a statement](https://paymentinstitutions.eu/pressroom/joint-industry-statement-on-sca-implementation/) that recognizes the challenges that financial services providers will face in meeting SCA requirements and provides an 18 month transition period.

## So what’s all the confusion about?

Overall, this back and forth at such a high level of government and industry has led to a TON of confusion across sectors about the timeline, execution, and overall requirements of SCA. So, let’s clear it up as best we can based on the currently available information.

The image below shows the most recent timeline we’ve found for PSD2 that falls in line with everything we’ve researched about SCA:

![chart of PSD2 recent timeline](https://freemius.com/blog/wp-content/uploads/2019/09/word-image-5.png)

Source: [https://www.signifyd.com/psd2-strong-customer-authentication/](https://www.signifyd.com/psd2-strong-customer-authentication/)

**Basically, everyone can take a big sigh of relief.** The “initial deadline” of Sept 14 has now passed, and because of all that discussion going on at such a high level, a lot of people are still worried that many online payments are simply going to stop working, which we can safely say is not the case (at least not until 2021).

Even given this timeline, it’s worth saying that if you’re selling with Freemius, we have it taken care of!

**We just updated our entire payment platform to fully support all aspects of SCA** through our relevant payment gateways, well before the enforcement date of March 14, 2021.

[![three glasses of wine tossing](https://freemius.com/blog/wp-content/uploads/2019/09/Cheers.gif)](https://freemius.com/blog/wp-content/uploads/2019/09/Cheers.gif)

This doesn’t make SCA irrelevant for plugin/theme shops though – whether or not you sell through Freemius. SCA is going to affect consumer payments, and it’s important to be aware of the new checkout experience that will be required for many eCommerce payments.

## Who exactly is impacted by SCA?

There’s still a lack of clarity on this one. Initially, the “word on the street” was that it only affects merchants in the European Economic Area (EEA) for transactions made by European cards. Then, Stripe started to communicate that SCA might also impact US merchants transacting European cards.

As everyone is still slowly coming to grips with the new payment directives, the situation continues to evolve quickly. We can say for sure that SCA will affect many online payments in relation to European cards, no matter where you’re located, and it’s vital to ensure that your payment gateway is fully prepared to handle PSD2 requirements under SCA.

### Does SCA impact previously created subscriptions that were not authenticated yet?

One of the biggest initial concerns was that SCA would require *re-verification of existing subscription payments*, which you might imagine could cause turmoil for eCommerce businesses that rely on their recurring revenue to continue operation (like many plugin and theme shops).

Some of the guidance released by Stripe has explained that many payments will be eligible for “exemptions” to SCA, including subscription payments started before Sept 14, which will generally be “[grandfathered in](https://stripe.com/docs/strong-customer-authentication/grandfathered-agreements/)”.

For subscription payments starting after Sept 14, 2019, it’s important to be using the latest APIs of your relevant payment gateways, which should have SCA requirements for verification built-in. These payments will be eligible for exemptions to the new requirements because they will have gone through an internal verification process in real-time.

Overall, the deal is that payments under €30 generally don’t have to go through additional verification if the fraud rate for the customer’s bank is very low – these are called “exemptions”.

Depending on the payment issuer’s fraud rating, the exemption ceiling for verification can increase up to €100 or even up to €250 if the issuing bank has very little fraud activity associated with it.

This is what Stripe’s website says about the topic:

![STRIPE low risk transaction definition and examples](https://freemius.com/blog/wp-content/uploads/2019/09/word-image-6.png)

STRIPE low risk transaction definition and examples

*Source:* [*https://stripe.com/en-de/guides/strong-customer-authentication#low-risk-transactions*](https://stripe.com/en-de/guides/strong-customer-authentication#low-risk-transactions)

Based on the timeline closer to the beginning of this article, every country in the EU has to start *enforcing* PSD2 after March 14, 2021, which means you may not experience any payment issues moving forward if your solution is upgraded by the enforcement date (but you have better chances of avoiding problems if your payment gateway and APIs are up to date as soon as possible).

The main risk we can see is that subscription payments started after Sept 14, 2019 that do not go through the 2FA verification process required under SCA – or gain an exemption – may not renew properly when the subscription is up for renewal. Those payments may require re-verification, but this is still not totally clear, and we will be sure to update this article as new information becomes available. If you find something online about this – feel free to post in the comments and let us know!

Even with the extended transition period, you should ensure your eCommerce solution and all relevant payment gateways have made the transition to verifying payments through SCA to minimize the risk of failed payments.

Payments will be given an exemption to SCA requirements in real-time based on the payment thresholds and fraud rates **OR** require verification through 2FA during the checkout process to add an extra layer of security when the risk of the payment is deemed too high.

All of this will happen behind the scenes. If you’re selling plugins and themes through your own online store – you need to adapt your existing solution to use the latest APIs with suitable gateways.

## How exactly does SCA and PSD2 work??

Functionally, SCA requirements are being met through the use of [3D Secure 2.0](https://stripe.com/guides/3d-secure-2) (3DS2) to verify online payments that are deemed too risky by using 2FA.

The actual checkout process for European customers will either look as it currently does today, which means their payment is probably exempt from SCA, or customers will be required to go through a second level of verification in the checkout process.

The extra verification step in 3DS2 requests one of the three security factors outlined in this [European Banking Authority opinion](https://eba.europa.eu/publications-and-media/events/discussion-rts-strong-customer-authentication-and-secure) as [Knowledge, Possession, or Inherence](https://proofid.com/blog/knowledge-factors-possession-factors-inherence-factors/). These are basic definitions of the 3 security factors that can be verified in the payment process:

Knowledge = Hidden information like a password, pin, or answers to secret questions.

Possession = A physical device of some kind, like a card reader or USB token

Inherence = Biometric data like a fingerprint or facial recognition, often from mobile devices.

Many payment gateways already include these kinds of factors in their checkout flow, so, depending on your gateway, your users may not see any changes to their checkout experience on your store. They may implement 3DS2 in the background or if other options for meeting SCA are/become available, those may be used too. 3DS2 is simply the online payment industry’s response to maintaining a seamless user experience while meeting the new security requirements.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Innovating the User Experience with 3DS 2.0

In fact, while SCA adds a layer of complexity for development, it has the potential to dramatically improve the end user experience during checkout. 3DS 2.0 brings with it the benefits of reduced fraud, wider availability of payment options, and a potentially faster verification and checkout process because payment providers will be required to include 2FA in their checkout flows as a possible verification procedure. So, some customers may actually see a greatly improved checkout experience than they previously had.

Freemius is happy to take advantage of this opportunity to innovate our checkout process in order to meet these new requirements so our plugin or theme selling makers don’t have to!

## How SCA Affects Freemius Selling Makers

Our team has been hard at work making sure that the transition to SCA is smooth and painless for everyone. We’ve spent a lot of time investigating the implications of SCA for the user experience of your customers, and we now have it fully integrated into our [Checkout](wordpress-checkout.md).

Keep in mind that this process might look a little different depending on the payment method being used, the type of credit card and card issuer used by the customer.

If your customers experience any issues during the checkout after this new update, be sure to ask them for a screenshot. For many payments, they will have to use some kind of secondary verification on the device they’re using – either a fingerprint, additional security information about their payment profile with their banking system, or other biometric data. This may be the reason payments get held up – but the customer will still need to verify it properly if the request is working properly.

## If You’re Struggling with Gateways…

We know many eCommerce platforms in the ecosystem are struggling to keep up with SCA requirements, and a lot of work is put on to the website administrator to ensure your platform is up to date with the latest plugin releases, server requirements, and more.

If you’re having a headache with this, it’s important that you take the time to address it because before you know it, some of your payments from European customers will simply stop working, which means your business is held back from success. Don’t let SCA eat you alive:

[![a goat and frog chewing](https://freemius.com/blog/wp-content/uploads/2019/09/chew-struggle.gif)](https://freemius.com/blog/wp-content/uploads/2019/09/chew-struggle.gif)

Regardless of where you live and how you sell your plugins and themes, you need to have a selling and licensing solution that allows your plugin and theme business to thrive. We’ve heard complaints from a bunch of developers that their selling solution doesn’t yet support SCA, and we can definitely sympathize with this feeling after years of experience in helping plugin and theme shops grow and meet their greatest potential.

We’ve created this useful chart of the major platforms used for selling plugins or themes and the status of SCA-supported gateways available through those platforms. We’ll keep this chart updated as things change.

**WordPress eCommerce Platform Support for SCA by Payment Gateway** **Payment Gateway** **Platform** [**WooCommerce**](https://woocommerce.com/posts/introducing-strong-customer-authentication-sca/) [**EDD (Easy Digital Downloads)**](https://easydigitaldownloads.com/blog/strong-customer-authentication-is-coming/) 2Checkout Onsite Not Supported Not Supported Amazon Pay Supported Not Supported Authorize.net Not Supported Not Supported Braintree Supported Not Supported Global Payments Gateway (formerly Realex) Supported Not Supported PayPal Payments Advanced Not Supported Not Supported PayPal Pro Not Supported Support coming soon Stripe Supported Support coming soon Sage Pay Supported Not Supported

## So What Next?

In the long-term, we will keep you updated on further changes to payment gateways, so you can be empowered with the knowledge to make the right decisions for how to sell your WordPress plugins and themes. We know payment gateways can be a huge hassle for developers to manage, especially when you mainly want to focus on your product development and marketing.

In regard to SCA, things are changing pretty quickly in this space, and there’s still not a lot of clarity as each country is implementing the regulations at different times. We’ll continue doing our research and updating folks as things progress.

Hopefully, this information helps you manage the transition more effectively and feel free to ask any questions in the comments!

** This article should not be construed as providing legal advice. We highly recommend contacting a legal professional to ensure your business stays up to date with the latest regulations relevant to your business.*