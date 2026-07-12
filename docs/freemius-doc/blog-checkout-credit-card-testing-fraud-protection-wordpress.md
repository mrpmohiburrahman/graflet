Taken at face value, the UX and security fundamentals of a high-converting WordPress checkout are straightforward. If you want prospects to stay the course, you strip away friction points and remove components that aren’t critical to building confidence and completing the transaction. All while ensuring security layers and validation points are working in the background to protect against credit card testing and to legitimize purchases.

Easier said than done, right?

Plugin and theme sellers know all too well that a high-converting checkout is a balance of compromises. Remove one layer of protection here and you run the risk of lowering security. Add an extra form field there — such as ‘zip code’ — and it may yield irritating validation problems that drive prospects away.

Yes, an optimal balance of UX and security is tough to achieve, but dammit if I’m not going to try and help you strike it!

To do so, I’ve divided this article into two chapters. The first investigates:

1. Factors that tilt the balance in favor of UX or security (often to the detriment of the other).
2. Attackers, their motivations, and why their existence warrants putting obstacles in place that can ruin the user experience.

The second chapter explores the measures and practices that can bring balance to a WordPress checkout’s force and help product sellers optimize UX while protecting against card testing.

*This one’s a biggie, so if you’re ready to get stuck into our recommendations for an optimum checkout balance, hit* [*this jump-to link*](#turn_your_checkout_into_a_security_powerhouse_that_squashes_credit_card_testing_fraud) *and I’ll catch you further down. If not, let’s get started.*

[1. UX and Security Factors That Reduce Checkout Fraud Protection](#ux_and_security_factors_that_reduce_checkout_fraud_protection)

- [Target Market and Niche Disconnect](#target_market_and_niche_disconnect)
- [Saying No to Strangers…](#saying_no_to_strangers)
- [Over-Relying on Credit Cards As Security Measures](#over_reliance_on_credit_cards_as_security_measures)
- [Governments and Mandatory Regulations](#governments_and_mandatory_regulations)
- [Zip Codes: Should You Collect Them at Checkout?](#zip_codes_should_you_collect_them_at_checkout)

[2. Turn Your Checkout into a Security Powerhouse That Squashes Credit Card Testing Fraud](#turn_your_checkout_into_a_security_powerhouse_that_squashes_credit_card_testing_fraud)

- [Choose a Payment Solution With a Network in Place](#choose_a_payment_solution_with_a_network_in_place)
- [Load the Checkout as a Dialogue](#load_the_checkout_as_a_dialogue)
- [reCAPTCHA](#recaptcha)
- [Email Validation Using a Service](#email_validation_using_a_service)

[3. Four Security Layers That Filter Out Credit Card Testing Attacks](#four_security_layers_that_filter_out_credit_card_testing_attacks)

- [Layer One: Unearthing Email Fakery](#layer_one_unearthing_email_fakery)
- [Layer Two: Unmasking Geo-Spoofing](#layer_two_unmasking_geo_spoofing)
- [Layer Three: Revealing Domain and Subdomain Subterfuge](#layer_three_revealing_domain_and_subdomain_subterfuge)
- [Layer Four: Unlocking Transactions With Payment Gateways](#layer_four_unlocking_transactions_with_payment_gateways)

## 1. UX and Security Factors That Reduce Checkout Fraud Protection

### Target Market and Niche Disconnect

*AKA: The More Information is Not Necessarily the Merrier*

Inexperienced WordPress product sellers often operate under the assumption that a checkout should collect as much customer information as possible.

Right? Wrong?

The answer depends on who you’re targeting and which space your products serve. If they’re SaaS solutions built for [enterprise companies](blog-selling-plugins-themes-enterprises.md) where transactions typically run into the thousands (and more), it’s a resounding *yes.* When there’s so much cash at stake, you’ll want to collect everything you can to protect yourself and the customer.

In the case of a plugin/theme ecosystem like WordPress — the focus of this article — transactions are typically under one hundred dollars, so you don’t need customers to share a life story’s worth of information at checkout.

Problem is that many plugin and theme sellers don’t tailor their checkouts for the audience and market they’re serving. If you’re a website developer working on a top-down redesign for a client, you’ll want to purchase a plugin as quickly as possible and get on with the job.

But what happens if the developer isn’t comfortable with giving out their address and contact number. What if the zip code is problematic and can’t be matched to the credit card? What if they couldn’t be bothered to register to purchase?

Any of the above could be enough to drive prospects away. There will always be a competitor product that’s priced the same, does the same thing, but has a checkout that takes a few clicks and keystrokes to transact.

### Saying No to Strangers…

![old man with glasses with the words nobody wants you here](https://freemius.com/blog/wp-content/uploads/2022/05/word-image-1.gif)

… until you’ve introduced yourself!

We’ve all been there. You select a product and grab your wallet, only to be redirected to a registration page or forced ‘off tab’ to an authorization link in your email. That’s right, you’re an unregistered guest in the product seller’s system and the checkout process doesn’t allow for strangers.

Only once you’ve created an account — maybe even changed your password because you were supplied one automatically — can you carry on with the purchase. From a user perspective, it’s a terrible experience, but from a security point of view, it’s a pretty solid practice.

**The Argument for User Registration**

It’s easy to set up a fake email and register to launch an attack. Similarly, it’s simple for plugin sellers to include security layers that lock user accounts attempting multiple transactions, in quick succession, from the same email addresses.

Attackers are also looking for the checkout of least resistance, so the mere presence of registration may be enough to turn them away. Plus, including the option to log in with services like Google or Apple streamlines the process somewhat.

**The Argument Against User Registration**

There are too many negative variables. A verification email may end up in the spam folder; it may not be delivered at all. Errors can occur when users attempt to register with services like Gmail. Updated passwords are easily forgotten.

For some users, the time/effort it takes to register could drive them to abandon, especially when the purchase is relatively trivial cash-wise. Sure, if you’re purchasing something *meaningful* — like concert tickets (or in my case trail running entries) — you’ll stay the bumpy course. But, if there are three similar plugins to the one you’re trying to buy, you’ll probably seek them out instead.

### Over-Reliance on Credit Cards As Security Measures

Or, as I like to call it, *‘It’s No Secret That Credit Card Information Isn’t All That Secret’*.

Theoretically, the card input fields should add some ‘mystery’ to the transaction process. But exploiters, WordPress product sellers, and defrauded customers know the truth: they aren’t considered secret from a security POV.

Information on the card itself isn’t encrypted, save for the magnetic strip which isn’t used for online transactions anyway. You could say that card numbers and expiry dates (even CVCs) are public knowledge — if you know where to look. Getting hold of card info is pretty cheap too, and stolen cards sell for as little as [$5 on the black market](https://spendmenot.com/blog/credit-card-fraud-statistics/).

#### Are Credit Card CVCs Secure and Should You Collect Them?

If anything can be considered even remotely ‘secret’ on a credit card, it’s the three- or four-digit number on the back. As the CVC number isn’t encoded into the card itself, it affords the cardholder some security and privacy (as long as they take measures to protect it from curious eyes).

Having said that, even the small measure of secrecy it adds may not be enough to justify its inclusion at checkout. In August of 2021, Stripe disabled both their CVC and postal code rules after research revealed that *‘turning off the default rules to block payments that fail a CVC or postal code check can increase acceptance rates by 0.08% on average, with negligible impact on fraud rates.’* Product sellers were given the option to opt-out of the change if they wanted to continue with the fields.

Now, nobody is forcing product sellers to include this mechanism since it’s not considered best practice as a standalone security measure. But in our experience, CVCs are integral to the validation process and add value when used as part of a layered security approach.

Putting aside CVCs for now, let’s move back to the overall security (or lack thereof) of credit information.

Just a few clicks away, there is publicly available documentation from Visa and Mastercard, etc. that explains how credit card structures work. *How are they issued? What do the prefixes mean and how does validation work?* It’s all there in the public domain to help make credit card validation easier for companies and WordPress plugin and theme sellers. And attackers.

#### If It’s Easy for Companies, It’s Easier for Attackers

***Disclaimer:* My info comes from good sources, not personal experience 😬. The only piece of tech I’ve hacked/attacked is my car’s Bluetooth (and even that required some Googling and dashboard smacking).**

[![a man with glasses with hackerman word pops out](https://freemius.com/blog/wp-content/uploads/2022/05/hacker.gif)](https://freemius.com/blog/wp-content/uploads/2022/05/hacker.gif)

Pictured: Not me

For the lazy attacker, it’s simple to create/run a script to test randomized numbers until illegal gold is struck. For the more willful, other avenues (such as the darknet) can be accessed easily, where literally thousands of stolen numbers are waiting to be purchased at low prices and be put to bad use.

*‘Bad use’* that’s made all the more simple by stripped-down checkouts that only require card numbers for the sake of frictionless UX. As mentioned, Stripe allows you to initiate a transaction without a CVC code or even a name.

So, for attackers:

1. Card information is easy to find if they know where to look
2. Numbers can be randomized with simple scripts until something sticks
3. There are a multitude of plugin checkouts in WordPress, many lacking backup security layers to make the transaction quicker.
4. Plugin prices are relatively low in the WordPress space, so there’s tons of profit to be—

Wait, that’s not right.

If there isn’t a lot of cash to be made by attacking WordPress plugin checkouts, then what gives?

#### Why Do Cyber Criminals Attack WordPress Plugin Checkouts?

![Scrooge McDuck jumping into a pile of coins](https://freemius.com/blog/wp-content/uploads/2022/05/word-image-2.gif)

Hint: Not for this

Most likely, attackers are not initiating the onslaught to get plugins for free. This is an [open-source, GPL ecosystem](blog-selling-wordpress-plugins-gpl.md) where it’s easy to find and download popular plugins (minus licensing) without spending a cent.

Also, many leading plugins these days have money-back guarantees which makes it even easier for fraudsters to buy the plugin legally, strip the licensing, and then request a refund. All while *illegally* distributing the product using dodgy channels.

So if not for the freebies or cash, then why?

#### Testing, Testing … Any Valid Card Numbers out There?

For the most part, attackers are using WordPress checkouts for credit card testing. Here are two common scenarios:

1. They’re trying random sets of numbers to see if anything goes through. Once the non-existent numbers are filtered out, they can sell the list of existing numbers online.
2. They’ve *purchased* a list of existing cards and are using checkouts to filter out canceled/expired ones. They can then identify functional cards through micro-transactions.

From our experience, the latter is the more common attack. Following on from Point 2, once an attacker has a working card, they can:

1. Sell the credit card number(s) at a higher price.
2. Find checkouts that aren’t [SCA/3DS-integrated to verify online payments](blog-strong-customer-authentication.md). These lack multi-factor authentication and thus make it easier for credit card testers to charge illegitimate purchases and maximize their working cards.
3. Make purchases below the SCA threshold so that secure authentications aren’t triggered. For example, transactions below £30 in the UK.

#### What Are the Penalties for Not Protecting Against Credit Card Testing?

Micro-transactions aside, credit card fraud runs into the billions of dollars every year globally. Industry research firm Nilson Report predicts that the card industry will lose $408.50 billion to fraud over the next decade 🤯.

For this reason, card companies are insured for fraud and have benchmarks in place to alert them to any unusual checkout activity. Stripe, for example, will flag checkouts with chargebacks that amount to over 0.7% of overall transactions. There is no set industry standard — Visa and Mastercard [penalize](https://business.ebanx.com/en/resources/payments-explained/chargeback) product sellers with rates above 1% — so you need to ensure you’re up-to-speed with the specifics of your provider.

Penalties vary too. Stripe will initially provide tips and practices to help sellers curb checkout abuse. If security leaks aren’t plugged as a matter of urgency, these ‘checkouts of concern’ run the risk of being closed, sometimes indefinitely. The strictness and severity make sense when you factor these numbers in:

[Nilson](https://nilsonreport.com/) [Report](https://nilsonreport.com/) states that *‘issuers, merchants and acquirers of merchant and ATM transactions collectively lost $28.58 billion to card fraud in 2020, equal to 6.8¢ per $100 in purchase volume.’*

Eek 😬

Strict penalties enforced by vigilant banks and card companies can understandably cause product sellers to shore up their checkout. But in their attempts to combat card testing, they run the risk of bloating purchase processes with unnecessary steps and layers.

There are more effective ways of securing a checkout — practices and technologies that aren’t overt and work in the background to validate cards and locations, etc. But, if you didn’t skip ahead earlier on, we’ll get to those in a bit 😉

From bank and card company overlords to…

### Governments and Mandatory Regulations

Earlier, I discussed the premise of simplicity and how it can be both a blessing and a curse to the UX/security balance of a checkout. Where simplicity is to create a better experience for the customer — pitfalls and all — mandatory government regulations like [GDPR](blog-gdpr-wordpress-plugin-theme.md) are there to protect customers’ identities and information through consent.

These regulations tip the balance towards security by legally obliging plugin/theme sellers to add additional fields to their WordPress plugin checkouts, such as obtaining permission to send marketing emails, etc. You can devise a way to obtain consent at a later stage, but the chances of being able to contact them after checkout are slim.

You can’t avoid these regulations and requirements, even if they do add friction to the checkout process.

### Zip Codes: Should You Collect Them at Checkout?

If you’re selling worldwide but a customer’s location isn’t certain, then you’re in the dark as to whether you’re obligated to charge them sales tax or not. Zip codes (along with the country) help you determine the regulations you need to follow, and while it’s becoming best practice to optimize your checkout so you don’t have to collect them, there are some caveats for doing so.

One method is to identify the user’s geo-location (and zip code) using the IP address, but you can’t know for sure if that specific zip code is the same as where they live/are registered for tax.

For example:

If a US customer purchases while traveling outside of their home state, the zip code served by the IP address will not be the same as the person’s home state. Because sales tax regulations differ from state to state in the US, you’ll run into regulatory red tape if you charge tax to the incorrect location.

By collecting zip codes, WordPress product sellers have been able to establish a link between customer locations and the credit cards being used. As this is private information that only banks or credit card issuers will have access to, it’s considered to be reasonably secure. For these reasons, plugin/theme sellers have tolerated the administrative headaches when issues arise.

But it looks like that patience is wearing thin and some payment gateways have started advising against it.

#### Zip Codes Add More UX Friction Than Security Value

Putting aside the pain of solving zip code-related problems, checkouts perform better without asking customers for them. The practice adds friction, reduces conversion, and can create problems down the line.

People move around, they forget, addresses change, codes are invalid — there are just too many variables involved to rely on the practice.

If the simple act of purchasing a $50 plugin gets me embroiled in a back-and-forth between bank and product seller, I’m taking my business elsewhere. Many times, it’s not the customer’s fault at all, and issues like outdated API records on the bank’s end are causing the problems.

Eventually, users will reach a ‘frustration threshold’ and move on to another product that does the same thing. Especially busy business owners, who want to make a quick purchase and move on to the next task.

Zip code collection is needed for tax purposes. But edge-case scenarios, bugs in the technology, etc. could make the process more troublesome if you validate zip codes along with credit card numbers.

*Now that we’ve examined factors that can cause imbalances in a WordPress checkout’s UX and security, let’s explore the measures, processes, and security layers that bring equilibrium.*

## Subscribe and grab a free copy to start Mastering SEO on the WordPress.org Repository

Make the WordPress.org search algorithm work for you with actionable tips to rank your plugin higher.

![Mastering SEO on the WordPress.org Repository](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## 2. Turn Your Checkout Into a Security Powerhouse That Squashes Credit Card Testing Fraud

Let’s make peace with it: a checkout for WordPress plugins/themes can never be completely impregnable nor the user experience 100% perfect.

But it is totally possible to increase conversions dramatically while minimizing card testing attacks with a layered security approach and a few choice measures. Here’s what we have so far:

✔ Allow guests to purchase without registration

✔ Require a name and email address

✔ Use an email address validation service

✔ Require the CVC digits as part of a layered security approach

✔ Avoid zip code validation

Now, let’s add the following to the UX and security mix:

### Choose a Payment Solution With a Network in Place

Solutions like Stripe leverage networks that can quickly determine whether a card is canceled, expired, or was used for another card testing attempt recently. The power of these networks can be equally effective as additional protection against fraud, and it’s one of the primary reasons product sellers should choose solutions backed by them.

Networks play host to many millions of transactions a month. For product sellers with checkouts that typically do a fraction of those numbers, there is much to be learned from taking a look at the entire network and the transactional data that’s exposed there (which is a good thing).

### Load the Checkout as a Dialogue

This is a ‘two birds with one stone’ scenario. By loading the checkout as a dialogue from the page the user’s on, you save them the hassle (and distraction) of navigating away from the product. This small mechanism not only makes for a better purchase experience but can also act as a deterrent for attackers who are after the path of least resistance.

![Freemius Checkout Loaded as a Dialogue](https://freemius.com/blog/wp-content/uploads/2022/05/freemius-checkout-loaded-as-a-dialogue.png)

*Checkout dialogue example from Freemius partner* [*Unlimited Elements*](https://unlimited-elements.com/)

### reCAPTCHA

I’ll admit that reCAPTCHA does detract from the checkout user experience, but if you’re serious about security, you should consider it. It’s been proven to deter most attackers and has built a reputation of being reliable and robust — it’s a [Google product](https://www.google.com/recaptcha/about/) after all, so it has resources behind it and is continually being made more intelligent.

Now to the friction. Sometimes just ticking the ***‘I’m not a robot’*** box isn’t enough and you’re prompted to click on taxis, buses, and so on — we’ve all been there. For savvy millennials brought up in the reCAPTCHA era, doing this is more of an annoyance than anything else. But for people older than 50, it can be confusing. Not to mention there may be a language barrier that further complicates the situation.

There is a silver lining to your efforts, however: Picking traffic lights out from grainy Google Street pictures helps Google classify and improve its vision algorithm.

To summarize, reCAPTCHA is a good security measure but the friction it adds isn’t trivial. **My advice:** Don’t use the mechanism by default. Instead, activate it when certain security layers are triggered — which we’ll get to in a bit — and if your audience is typically young, or your site is flooded by bots and spam entries.

![Freemius Checkout With reCAPTCHA for Credit Card Testing Fraud](https://freemius.com/blog/wp-content/uploads/2022/05/freemius-checkout-with-recaptcha-for-credit-card-testing-fraud.png)

An inoffensive reCAPTCHA appears at the Freemius checkout

### Email Validation Using a Service

While email validation services and mechanisms like reCAPTCHA are very different solutions, combining them into your checkout defense layers gives you the best of both worlds.

Every email address has a domain, and a very basic validation tactic is to ping a DNS server. DNS servers are mapping tables found in IP servers throughout the internet’s entire infrastructure. The purpose of these servers is to map/link domains with IP addresses.

For help, WordPress product sellers can turn to [services](https://www.google.com/search?q=email%20verification%20and%20validation%20services) that store gigantic lists of valid emails and provide important validation information. For example, additional metadata that lets you know if the email is disposable or a catch-all address. A catch-all address receives messages from a predefined list of ‘non-existent’ emails and can be used by fraudsters for mass attacks.

*Now that we have the recommended checkout pieces in place, let’s see how they work in tandem with a layered security approach.*

## 3. Four Security Layers That Filter Out Credit Card Testing Attacks

*Fake. Suspicious. Valid.* The three factors that determine which layer of security is triggered, based on the varied tactics of checkout fraudsters.

### Layer One: Unearthing Email Fakery

When a purchase attempt comes through, the first step is to identify the domain and to see if it’s legitimate or not. For this, you’ll need to rely on a DNS server and internet protocols.

The next step is to check if the supplied email address is valid. At Freemius, we base these validation protocols on a set of rules that I’m not at liberty to share. However, I will say that this isn’t a foolproof method and it does rely on how the email provider has configured its server.

Some email providers allow you to validate IP addresses and domains directly, while others — like Outlook — will always tell you that the email address is valid, even if it’s not. Whether for security reasons on their end or something related to the server structuring, this is a clear vulnerability as it allows credit card testers to spin out a bunch of fake emails that always appear to be valid.

Based on the above and the rules you have in place, you can expect one of three results. Either the email address is **fake**, **suspicious**, or **valid**.

1. If it’s fake, the attacker will be booted from the checkout.
2. If it’s suspicious, a reCAPTCHA can be dynamically introduced to clarify whether it’s an algorithm or a flesh-and-blood human.
3. If it’s valid, the customer and their address have passed the first layer.

### Layer Two: Unmasking Geo-Spoofing

Once the email address is validated, it needs to be linked to a legitimate IP address. Though VPN services can hide your location by routing to proxy servers, spinning out IP addresses en masse isn’t trivial. Yes, there are lists of proxies out in the wild, but only savvy attackers — with access to the right resources and a high level of programming knowledge — will be able to spin out more than a handful of IPs at any given time.

While product sellers have no way of deterministically knowing if an email/domain is linked to a specific card, there are IP-related checks to determine valid or suspicious activity.

#### Scenario I

**Not suspicious**

No additional purchase attempts from the same IP with the same email address within a short period.

**Potentially suspicious**

A few failed purchase attempts from the same IP with the same email address is suspicious but not necessarily a card testing attack. There’s a reasonable chance it was a legit user who put in the wrong card information or made some similar mistake. In these scenarios, the transactions should be flagged as suspicious and require reCAPTCHA validation to proceed**.**

#### Scenario II

**Not suspicious**

No additional purchase attempts (failed or successful) have occurred from the same IP with different emails within a short period.

**Definitely suspicious**

Three or more failed attempts in a certain time frame — all linked to the same IP and different email addresses — is 100% a credit card testing attack and the IP and purchase attempts should be blocked.

Assuming the transaction falls into the ‘not suspicious’ category, it will be allowed through to the next layer.

### Layer Three: Revealing Domain and Subdomain Subterfuge

If an attacker makes it this far but flags are still being raised, this next layer of defense is related to domains and subdomains. Broken down into three parts, these steps should reveal and hopefully halt their nefarious attempts.

#### Layer 3.1

While I obviously can’t mention the parameters we use, I can say that they involve checking the database for other attempts from the same email address, at the same time, or within a few minutes. It’s highly suspicious if the user has attempted to purchase multiple times — using different credit cards — in a short space of time.

What’s triggered based on those findings depends on how you’ve configured your system. If it’s just suspicious — like one or two attempts as mentioned earlier — consider serving up a reCAPTCHA so as not to lose sales. If it’s multiple attempts, then the parameters could be set to flag the purchases as fraudulent and to kick the user out of the system right away.

#### Layer 3.2

If you discover multiple attempts from different emails using the same IP address, that’s cause for concern. Of course, it’s common for people to have two email addresses — what’s not common is to see a person using three, four, or even five emails to transact within the same period.

In many cases, multiple card testing attacks are accompanied by randomized emails using identical domains. As mentioned, attackers are aware that spinning random Outlook email addresses can help them skirt product sellers’ validation processes.

Attackers are savvy too. At Freemius, we’ve seen multiple Outlook email addresses from different IP addresses being attempted at checkout. The common thread is that all of these addresses have the same domain — you can protect against these attacks by requiring that all purchases from Outlook addresses for that *specific* product be served reCAPTCHAs for the next *N* minutes as a cooling-off period.

#### Layer 3.3

For checkouts used across multiple plugins, fraudsters can orchestrate cross-product card testing attacks using multiple IPs.

To combat this kind of activity, Freemius uses a deterministic logic that alerts the system and escalates the issue. Not only will the checkout require reCAPTCHA for the specific domain being used, but it will also use reCAPTCHA for all purchase attempts on those particular products.

Unfortunately, this does impact the UX for potential buyers, but it’s a necessary evil that will only take place over a closed period. The period can be once-off and fixed, or tiered and incremental if the attacks continue.

At this point, if everything checks out, the user moves on to the last layer of security.

### Layer Four: Unlocking Transactions With Payment Gateways

Finally! We reach the last layer of defense — card validation.

Before I continue, it’s important to note that PayPal eliminates pretty much all of the above problems. With PayPal, a user needs to be logged in and verified before they can start the checkout validation process. This brings its own UX problems — a user may forget to log in beforehand or misremember their details — but the disruption is minimal.

For checkouts that use gateways like Stripe, card information needs to be deployed and validated by the gateway itself before the purchase can go through. Validity is further determined by the parameters you have in place. For example, CVC checks or address verification (AVS) to match billing addresses on file with the card issuers.

If everything’s in order, the purchase goes through. If not, the transaction will be flagged and then denied if the user or bank can’t prove otherwise, dismissing the attacker as if they were never there.

*‘So long, goodbye, and thanks for all the flags!’*

## Checking Out…

Thanks for sticking around!

The insights and practices in this article are informed by our learnings at Freemius, from experiences both good and bad. Tailoring a checkout is a trial and error process, and you may find that some of the advice isn’t relevant or doesn’t fit your checkout’s needs. That’s fine!

If one piece of advice or one nugget of insight makes a positive impact on your checkout’s conversion rate and helps you protect against credit card testing, then I consider my job done. Cheers for reading and let me know if you agree/disagree or have anything to add to the topic of UX and security in WordPress checkouts.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)