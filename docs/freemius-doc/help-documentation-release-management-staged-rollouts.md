---
title: "Staged Rollouts"
url: "https://freemius.com/help/documentation/release-management/staged-rollouts/"
source: "docs"
section: "Docs"
category: "Release Management"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 388
---

Staged Rollouts allows you to specify the number or percentage of websites you want to roll out a new paid version to. Instead of risking your entire customer base with potential bugs, you can release it progressively – starting with limited exposure and then increasing it incrementally as you build confidence in your release.

Staged Rollouts is THE best practice for releasing software updates, a process that many of the large companies outside the WordPress bubble follow. At Freemius, we are delighted to be the first (and currently only) WordPress eCommerce solution that supports Staged Rollouts out-of-the-box.

## How to use Staged Rollouts?[​](#how-to-use-staged-rollouts "Direct link to How to use Staged Rollouts?")

warning

While you can leverage Staged Rollouts for your release cycle regardless of your customer base size, there’s not much value in Staged Rollouts if you only have a few hundreds of active customers. As a rule of thumb, we recommend starting utilizing Staged Rollouts once you get to at least 500 customers.

1. When you are ready to start your release cycle, switch the newly deployed version state to *Released*:

<!--THE END-->

2. Then, choose how you’d like to limit the rollout – you can either specify an exact number of websites or choose to limit by percentage. Whichever method you choose, we recommend the initial rollout to be no less than 100 websites.
3. Give it a few days while watching the number of served updates and closely monitoring support tickets and complaints related to the release.

<!--THE END-->

4. If you discover a bug related to the release: 1. Patch it asap 2. Deploy a new version 3. Release it again as a Staged Rollout while limiting the update exposure to the same limit as your prev staged release.

warning

**Important:** Don't change the state of the prev staged release to make sure the new patched version will first go to websites that have already been exposed to the staged buggy release.

5. As you build confidence in the release, increase the release exposure by clicking the edit icon next to the release limit and setting a higher limit.

<!--THE END-->

6. Every time you discover a bug, repeat step #4.
7. Keep increasing the exposure and releasing patches as needed until you get to a stable release that eventually gets exposed to everyone.