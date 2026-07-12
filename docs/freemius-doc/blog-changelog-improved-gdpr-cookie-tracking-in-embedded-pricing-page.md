[Changelog](https://freemius.com/changelog/) / Improved GDPR cookie tracking in embedded pricing page

We noticed that when the pricing page is loaded through our WordPress SDK, the cookie consent UI is always being shown, regardless of whether the user has already consented or rejected it.

The issue was rooted in how modern browsers are now treating iFrames and third-party cookies. We have fixed this issue. Additionally, to make it future-proof and more secure, we have implemented the partitioned cookie policy.