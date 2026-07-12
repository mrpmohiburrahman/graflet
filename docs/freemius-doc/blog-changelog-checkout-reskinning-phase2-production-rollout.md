[Changelog](https://freemius.com/changelog/) / Checkout Reskinning phase2 production rollout

Following up on last week’s [announcement](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md), today we are marking the checkout `phase2` as production-ready.

[![Freemius Checkout Phase2 - Release Candidate](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate-1024x736.png)](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-phase2-checkout-release-candidate.png)

The deployment comes with a few improvements too.

- We have optimized various UI and UX as it has gone through many QA tests.
- We identified a bug where some strings were not translated and have fixed them.
- The form focus and validation experience have also been improved.

### Rollout Strategy

While the new checkout is production-ready, we have not yet made it the default. The old checkout will still show up unless you have specifically opted into the new system with `checkout_style: 'phase2'` JS parameter. For more information, please read our announcement post [here](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md).

### Bug fixes for the old checkout

We noticed a bug in the old checkout where the form could not handle some errors in rare cases. We have deployed a fix for the same.