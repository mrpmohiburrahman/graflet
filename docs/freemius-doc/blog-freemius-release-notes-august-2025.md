Improved failed renewal recovery, smarter SaaS emails, and a clearer signup experience for both makers and buyers make it easier to build trust, sell software, and stay top of mind.

WordPress developers will also notice a more intuitive SDK setup process that mirrors their in-product flow, and a handful of behind-the-scenes fixes keep things running smoothly across the Developer Dashboard, Checkout, and billing.

Here are August’s updates, big and small:

## Smarter Failed Renewal Recovery — Branded, Flexible, and Built for Buyer Trust

When a renewal fails, buyers deserve a recovery flow that feels secure, familiar, and in their control. This release introduces [a reimagined payment recovery (dunning) experience](blog-changelog-better-and-embeddable-payment-recovery-or-dunning-experience.md) that builds trust and removes friction by happening directly on your own domain, under your brand.

[**![our reimagined payment recovery (dunning) experience](https://freemius.com/blog/wp-content/uploads/2025/09/our-reimagined-payment-recovery-dunning-experience.jpeg)**](https://freemius.com/blog/wp-content/uploads/2025/09/our-reimagined-payment-recovery-dunning-experience.jpeg)

- **Embed the recovery flow on your site**  
  Instead of redirecting to `checkout.freemius.com`, you can now embed the payment update experience at a URL like `yourdomain.com/update-payment`
  
  - Buyers recognize that the domain is associated with the product renewal and feel confident proceeding with the update
- **Native, overlay experience**  
  The recovery form opens as an overlay dialogue on your website — no jarring redirects or disconnect in branding
- **Payment method switching is now supported**  
  Buyers can now resolve failed renewals by switching to a completely different payment method:
  
  - From **credit card → PayPal or iDEAL / From PayPal → credit card or another PayPal account**

This gives buyers a clearer, more trustworthy way to resolve billing issues. There are no confusing redirects, no unfamiliar URLs, and no need to contact support just to stay subscribed.

## Smarter SaaS Transactional Emails: One Account, One Experience

When buyers sign up for your SaaS, they expect to manage everything — product access, billing, subscriptions — in one place.

[![after purchase email with login details](https://freemius.com/blog/wp-content/uploads/2025/09/after-purchase-email-with-login-details.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/after-purchase-email-with-login-details.jpeg)

Until now, Freemius’ transactional emails automatically included login details for the [Customer Portal](customer-portal.md). That often left buyers with two logins: one for your product and another just for billing, with no clear sense of which to use.

[This update](blog-changelog-customize-customer-portal-links-in-transactional-emails.md) makes that journey clearer:

- **Customer Portal links removed by default:** For SaaS products, after-purchase emails no longer include Customer Portal credentials. Buyers use the login they already know: yours.
- **Stay up-to-date with SaaS norms:** Common practice in SaaS is to handle billing and subscriptions inside the product, not through an external portal.
- **Makers still have control:** Prefer to rely on Freemius’ Customer Portal? You can re-enable those links anytime in the Email Customization settings.

[![Developer dashboard with transaction email customization](https://freemius.com/blog/wp-content/uploads/2025/09/developer-dashboard-with-transaction-email-customization.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/developer-dashboard-with-transaction-email-customization.jpeg)

Buyers now enjoy a simpler, more familiar SaaS experience with fewer logins, fewer dashboards, and a clearer path to manage billing and subscriptions.

## A Smoother Start: Clearer Registration for Makers (and Buyers Who Wander In)

Two tales of mistaken identity: buyers creating maker accounts and makers signing up with products we don’t support.

The [new Developer Dashboard flow](blog-changelog-enhancing-the-registration-experience-for-makers.md) makes things clearer for both, from the start:

[![Login page with clear makerbuyer registration flow](https://freemius.com/blog/wp-content/uploads/2025/09/login-page-with-clear-makerbuyer-registration-flow.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/login-page-with-clear-makerbuyer-registration-flow.jpeg)

- **Clearer messaging up front:** The page now explains that Freemius is for “*thousands of makers and software companies selling their products*,” reducing confusion for buyers who see Freemius on their credit card statement.
- **Direct path to the Customer Portal:** Buyers who land on the registration page now see a clear link to the Customer Portal alongside the text “Purchased via Freemius?”.
- **Clear guidance on what you can (and can’t) sell:** New makers are asked what type of product they want to sell, with unsupported categories flagged immediately. This prevents time wasted setting up accounts for products Freemius doesn’t serve.
- **Refreshed trust signals:** Testimonials and logos have been updated to highlight active, real-world makers who currently use Freemius.

Buyers are guided to the right place, makers know up front if Freemius is a fit, and everyone benefits from a smoother, more trustworthy registration flow.

## WordPress Safety Net: Blocking Accidental Paid Version Uploads to .org

It’s rare, but when a paid plugin version is accidentally uploaded to WordPress.org, it causes confusion, update issues, and support headaches for everyone.

In collaboration with the WordPress.org plugin review team, we’ve [introduced a new safeguard](blog-changelog-new-safeguard-against-uploading-premium-code-to-the-wordpress-org-repository.md) to prevent accidental uploads of paid plugin versions to the repository.

[![Freemius code snippet blocking paid version uploads to WP repo](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-code-snippet-blocking-paid-version-uploads-to-wp-repo.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-code-snippet-blocking-paid-version-uploads-to-wp-repo.jpeg)

It works like a gatekeeper: a unique snippet is now added to the Freemius integration code. If WordPress.org detects that snippet during plugin submission, it blocks the update and immediately alerts the developer.

To keep things seamless, Freemius automatically strips this snippet from the generated free version so the correct variant uploads without issue.

This small line of code prevents a surprisingly big mess:

- Free users aren’t blindsided by sudden license activation prompts
- Makers avoid accidentally locking users into a version that can’t auto-update or downgrade, leaving them stuck unless they manually reinstall the free version
- The .org plugin review team gets fewer complaints
- Everyone avoids a frustrating support spiral

This safeguard is the result of years of collaboration between Freemius and the WordPress.org team, and a signal that even as we expand into SaaS and apps, we remain deeply committed to the WordPress community that helped us grow.

## Contextual SDK Instructions for a Smoother WordPress Integration

We’ve upgraded the WordPress SDK integration flow to reduce confusion and help new makers get started faster.

[![Context-aware integration wizard that updates by product state](https://freemius.com/blog/wp-content/uploads/2025/09/context-aware-integration-wizard-that-updates-by-product-state.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/context-aware-integration-wizard-that-updates-by-product-state.jpeg)

Previously, our SDK integration guide assumed that an opt-in screen would appear after installation. But if a maker had already created paid plans, they’d expect to see a license activation screen instead.

This mismatch caused confusion and support questions, so we’ve upgraded the in-page instructions in the Developer Dashboard. [The integration wizard is now context-aware and updates dynamically](blog-changelog-improved-wordpress-sdk-integration-flow-with-smarter-in-page-ux.md) based on your product state:

- If your product is still free (no paid plans), we’ll prompt you to opt in
- If paid plans exist, we’ll guide you to generate a license and activate it instead, keeping everything consistent with the in-product experience

[![Integration wizard for license generation and activation when paid plans exist](https://freemius.com/blog/wp-content/uploads/2025/09/integration-wizard-for-license-generation-and-activation-when-paid-plans-exist.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/integration-wizard-for-license-generation-and-activation-when-paid-plans-exist.jpeg)

This improvement ensures your first interaction with the SDK mirrors your actual WP admin flow to reduce ambiguity and eliminate setup guesswork. It’s part of our broader push to improve the developer experience (DX) and make onboarding smoother for all Freemius makers.

## Change Your Password Without the Reset Dance

You no longer have to go through the “[forgot password](https://dashboard.freemius.com/password/recover/?_gl=1%2At6mp0a%2A_ga%2AMzU4MDU5MTcyLjE3NDIxOTg4ODY.%2A_ga_KLSWMPC8SV%2AczE3NTczMjAxNzMkbzI0NiRnMCR0MTc1NzMyMDE3MyRqNjAkbDAkaDA.)” flow just to update your Freemius account credentials. There’s now [a simple option to change your password](blog-changelog-update-your-freemius-account-password-from-the-profile-page.md) directly from the **Profile page** in the Developer Dashboard.

[![Password change option in My Profile](https://freemius.com/blog/wp-content/uploads/2025/09/password-change-option-in-my-profile.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/password-change-option-in-my-profile.jpeg)

## Saying Goodbye to Freebo in Profile Avatars

As part of our rebrand, we officially retired Freebo, who is currently somewhere in Miami sipping cocktails in the sun and living his best life.

Previously, if buyers or makers hadn’t set up a [Gravatar account](https://en.gravatar.com/) for profile pics, we’d display a randomly generated Freebo instead. Now, we show [the first letter of the person’s name](blog-changelog-weve-retired-freebo-from-profile-avatars.md) against a clean, brand-aligned color background to keep things professional, simple, and on-theme.

[![Gravatar displays user’s initial instead of Freebo](https://freemius.com/blog/wp-content/uploads/2025/09/gravatar-displays-users-initial-instead-of-freebo.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/09/gravatar-displays-users-initial-instead-of-freebo.jpeg)

## Quality-of-Life Tweaks

From invisible bug fixes to subtle UI improvements, we’ve made a batch of changes designed to improve your day-to-day without interrupting it.

**Checkout:**

- [Back button icon improvement and social proof UI bug fix](blog-changelog-back-button-icon-improvement-social-proof-ui-bug-fix.md)

**Milestone emails:**

- [Rebranded email templates now scale properly on iOS devices](blog-changelog-fix-rebranded-emails-now-properly-scaled-on-ios-devices.md)

**Developer Dashboard:**

- [License table spacing, date-time rendering, and code fence fixes](blog-changelog-license-table-date-time-and-code-fence-fixes-in-developer-dashboard.md)
- [Fixed regression when adding localhost or custom dev URLs](blog-changelog-fixed-regression-in-managing-custom-development-or-localhost-url.md)
- [Removed outdated moderation UI for legacy opt-ins](blog-changelog-legacy-opt-in-moderation-ui-removed-from-developer-dashboard.md)

## Product Polish That Continues to Pay Off

That’s a wrap on August — a month of intentional updates designed to sharpen your product’s user journey from start to scale.

Whether it’s subscription recovery flows that feel like an extension of your brand, transactional emails that reinforce buyer trust, or setup instructions that meet your workflow where it is, each improvement helps your product feel more seamless, more professional, and more ready to grow.

Got thoughts, questions, or big ideas? [We’re all ears](https://freemius.com/cdn-cgi/l/email-protection#72111d1c0613110632140017171f1b07015c111d1f).