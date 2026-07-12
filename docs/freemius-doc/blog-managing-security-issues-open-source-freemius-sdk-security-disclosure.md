Running a startup is a rollercoaster. And like any good rollercoaster, there’ll be peaks, troughs, and curves that throw you for a loop along the way. During the last two weeks, we’ve been riding downhill, strategizing and executing the development and distribution of a security patch for our WordPress SDK. What was supposed to be a smooth and discrete ‘ride’ turned into an unexpectedly bumpy one. For the sake of transparency, here’s everything you need to know about the latest security vulnerability in our WordPress SDK.

On February 9th, we received a report about potential security issues in our [WordPress SDK](https://github.com/Freemius/wordpress-sdk). After careful inspection of the code, we quickly confirmed that *some* of the issues were indeed valid and immediately followed up with the reporter to ask them to hold off on a public disclosure for 30 days. This would give our team enough time to patch it, distribute the patched release to all developers using our SDK, and give their users and customers enough time to update.

## The Planning

We learned a bunch of lessons from our [first security incident](blog-sdk-security-vulnerability.md) three years back. So before jumping right into patching the SDK, we had a strategy meeting to assess the severity of the issues and to plan ahead and coordinate how we were going to tackle it while minimizing exposure in the process.

Here’s the plan we came up with:

- Have all the reported issues reviewed by two different team members to make sure we weren’t missing anything.
- Unlike last time when we rushed to patch the SDK right on our public GitHub repo, this time we decided to create a private fork of the repository and patch it privately.
- Contain the exposure to only relevant people by only notifying developers who are *actively* using the SDK in their plugins and themes.
- As it’s the same reporter we dealt with last time, we learned it’s better to get into a ‘silent mode’ and keep interactions to a minimum — they disclosed the previous incident shortly after our patch without our knowledge and without following [Responsible Disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) practices.
- Finally, push the patch to the public GitHub repo and publicly disclose the incident on March 9th under the assumption that the patch would have already propagated as several weeks should be enough for everyone involved to update.

We felt great about the plan! And established a squad of four team members for its execution.

## Execution

Everything was going as planned! The SDK was privately patched, we emailed only relevant developers about the issue along with the patched SDK, and also targeted the same group of developers by adding a special message in the Developer Dashboard.

![Developer Dashboard Security Update Message](https://freemius.com/blog/wp-content/uploads/2022/03/developer-dashboard-security-update-message.png)

And then to our surprise, it happened again 🤦‍♂️

## The Unexpected (Ahead of Time) Disclosure

On Monday we received an email about a new ‘freemius’ search result picked up by Google Alerts. To our surprise, we discovered that almost immediately after developers started to patch their plugins/themes on WordPress.org, the reporter went ahead and publicly disclosed the incident in detail, without even letting us know (I intentionally don’t link to it — they don’t deserve the backlink).

Unlike last time, we didn’t even try to ask the reporter to remove the article as we’ve learned it’s a waste of time and our request can only backfire on us. Instead, we politely tried to understand the reasoning behind the unexpected disclosure to assess if/how we could avoid it in the future.

Here’s their justification:

*We noticed the fixes right away once plugin developers starting releasing updates. We are not the only ones that do that type of monitoring, so trying to cover up that you are making security fixes like this doesn’t work.*

Obviously, we agree that once updates are released onto WordPress.org the code is publicly available. But, it’s very different from publicly handing out the ‘recipe’ of the security issues to potential attackers, and that’s the point we simply can’t agree on with the reporter.

## Was There a Better Way to Manage This? 🤔

Because developers don’t have a private communication channel with their free WordPress.org users, they can’t notify them about security issues. Based on the reporter’s approach, they believe that reporting a vulnerability as soon as a patch is released — without giving any buffer time for users to update — is legit and the way to go.

We strongly feel that this approach once again does not follow responsible disclosure practices and hope that other WP security-related outlets don’t follow the same route. I believe the real reason behind rushing a public disclosure was about publishing a scoop before others, and not about caring for users.

This brings me to a question — as long as there are security researchers trolls out there, how the hack can developers with products on WordPress.org (or other public repositories that don’t offer a private communication channel with their users) distribute patched releases without exposing users who don’t immediately update?!

Thinking retrospectively, we could have slightly improved the process by splitting the notifications into two batches. First, only notify developers with paid products to go ahead and patch their paid releases, as those do have their customers’ emails. Next, and only in the second batch after a few days, message developers to update their free version on wp.org.

But even with those slight changes the moment the first plugin gets patched on wp.org the threat of an unexpected early disclosure is real. The only option I can think of is to somehow coordinate everyone to patch their products on the same day, but I’m not sure how realistic this is as we are talking about a lot of developers from all over the world.

Now that we’ve published the disclosure, let’s get down to the actual security issues and the involved risks.

## What Are the Potential Risks of the Security Issues?

After conducting a thorough security review of the reported issues, we discovered that all of the valid ones are minor, except for one that I’ll cover in detail below.

But before I get there, let’s start with reassurance.

The reported security issues are **not** weakening the security of WordPress websites. Meaning, **even if a website is running a non-patched SDK version, it does not make the site more vulnerable to attacks.**

> Even if a website is running a non-patched SDK version, it does not make the site more vulnerable to attacks.

The most ‘interesting’ reported issue allows WP logged-in users to turn the SDK’s debug mode on, which activates logging and can *potentially* expose some Freemius-related sensitive variables — like an opted-in email address and API keys.

If the option to register on a WordPress site is disabled, assuming there are no hackers among the website’s existing users, there’s nothing to worry about.

Even if there is an option to register, if there was no opt-in nor license activation — i.e., a free plugin/theme that uses Freemius and an admin skipped the opt-in — there’s also nothing to worry about.

If an option for users to register is active and a license was activated (or an admin did opt-in), the API keys of the user can be obtained by an attacker, which will potentially allow them to access the license owner’s information on Freemius. While obviously this is not good, there’s no risk of obtaining credit card numbers since those never get sent to our servers. Probably the most sensitive information a hacker can get is the license keys and invoices associated with the account.

Having said that, it’s not trivial to reverse engineer how to use the keys to access the API as those endpoints are currently not documented. Second, if an attacker is after license keys it’s much easier to strip the licensing restriction from Freemius-powered products anyway. Also, to leverage the vulnerability, an attacker would need to attack a site per account. So realistically, unless an attacker is targeting a specific WordPress site, the potential gain doesn’t seem to be worth the effort, and therefore we assess that the chance someone can coordinate an attack at scale to abuse this weakness is extremely slim.

Don’t get me wrong, it is a security vulnerability and if a site is not running a patched release, updating to the latest version is important and we urge you to do so.

## How to Check If a Website Is Running a Patched Version of the SDK?

Our WordPress SDK comes with a special mechanism to automatically use the newest SDK available on the site. So when a website actively uses multiple plugins/themes with Freemius, it’s sufficient enough that only one of them uses the patched SDK.

To verify a website is already on a patched version, an admin would need to open the SDK’s debug page by navigating to `/wp-admin/admin.php?page=freemius`, and there, making sure that the *Active* SDK version is either `2.4.3` or `2.5.0.1` like here:

![Freemius Active WordPress SDK Version](https://freemius.com/blog/wp-content/uploads/2022/03/freemius-active-wordpress-sdk-version.png)

## Recap

Security issues are an inevitable part of the software world and they can happen to anyone, whether you’re an indie plugin developer, theme designer, team of twenty, or Microsoft. What’s more important is how we deal with the situation and what we learn in the process to come out of it better and stronger.

What we’ve learned at Freemius is that when it happens, we need to keep calm, assess the risks, and strategize a recovery plan while minimizing the exposure. We need to execute it in a timely manner and make sure that we are there for you (our makers) to provide the help you’d need to navigate the patching process.

On behalf of the whole Freemius team, we are truly sorry for the inconvenience and will be here to offer support, advice, or any other help related to the issue. And for our new users, we know how important the first impression is, and this is definitely not a good one. I hope that you’ll give Freemius another chance, and with time, see (and experience) the [amazing features](wordpress-features-comparison.md) we offer for your WordPress plugins and themes.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)