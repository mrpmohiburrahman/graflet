In our [last user-facing release notes](blog-release-notes-user-focused-changes-wordpress-sdk-2-5-1.md) in November, we announced many big changes addressing around 90% of the concerns we collected. That said, some of the requested changes were infrastructural, and thus more complex and time-consuming to tackle, which meant we couldn’t get to them in the last batch.

Dear WordPress users, we’re thrilled to share that the newest [WordPress SDK 2.5.4](https://github.com/Freemius/wordpress-sdk/releases/tag/2.5.4) no longer makes a connectivity test (aka ping.json) to the Freemius API upon plugin/theme activation. In other words, the SDK is no longer “phoning home”.

This now-obsolete feature, which was initially used to improve user experience (more on that below) and later proved to be a cause for concern among users, is finally down and out.

Thanks, everyone, for sharing your feedback 🙌 keep it coming!

For demonstration, I downloaded the latest version of TablePress, which uses Freemius, and manually updated the SDK to 2.5.4. Here’s what happens after activation:

![instruction how to activate tablePress plugin](https://freemius.com/blog/wp-content/uploads/2023/03/word-image.gif)

Voilà 🎊 As you can see on Snitch, a plugin that monitors remote requests, no HTTP requests were made after plugin activation.

## Why the SDK Had a Connectivity Test (the Backstory)

After launching the WordPress SDK, we quickly discovered that API connectivity could not be taken for granted. Whether it’s related to cURL misconfiguration, HTTPS or OpenSSL issues, firewalls, or regional ISP blockages, servers are sometimes unable to make remote requests.

After researching popular plugins with an opt-in component, we stumbled upon Jetpack. The plugin initiates a connectivity test immediately after activation. You can test it yourself:

![instruction how to activate JetPack plugin](https://freemius.com/blog/wp-content/uploads/2023/03/word-image-1.gif)

Jetpack connectivity test API request

Long story short, as this approach enabled us to resolve the challenge we were facing — along with the fact that Jetpack is a super popular plugin with millions of active installs and developed by Automattic — we decided to replicate this approach to make sure we didn’t show the opt-in to users who wouldn’t be able to opt-in anyway due to connectivity issues.

The connectivity test was also useful in identifying clock differences between the WP site and the API server, which is essential for security reasons. And, as a bonus from the ping itself, developers were able to limit the exposure of the SDK — or even turn it off completely — without the need to release a new version.

If you are a developer who has been using the moderation capabilities, make sure to read the next section.

## Warning: Breaking Changes

By removing the connectivity test, the moderation capabilities had to be transitioned to SDK settings. So, if you are using the moderation section in the Developer Dashboard to activate Freemius only for new installs or you limit the number of installs, please make sure to add the new config.

For example, the settings to only show the opt-in for new installations looks like this:

```
  'opt_in_moderation' => array(
      'new'       => 100,
      'updates'   => 0,
      'localhost' => true,
  ),
```

- `‘new’` (`int | boolean`): An integer from `0` to `100` to control the exposure percentage of the opt-in to new product installs. It also supports a boolean value. When set to `true`, then assume 100% exposure; if set to `false`, then no exposure at all. Defaults to `true` (as 100%) when not set.
- `‘updates’`(`int | boolean`): Exactly as the `‘new’` parameter, but controls the opt-in exposure for product updates (i.e., what % of websites will see the opt-in after upgrading to a new version with the Freemius SDK, when the previous version didn’t include the SDK).
- `‘localhost’` (`boolean`): Whether to show the opt-in on localhost sites. Default’s to `true` if not set.

## “Quality is not an act, it is a habit.” — Aristotle

SDK version 2.5.4 was thoroughly code reviewed, fully tested, and soft-released as a release candidate more than 3 weeks ago to give enough time for testing. It’s also already running in production with our own plugin since last week without any issues. While we have high confidence it’s production-ready because the change is on the infrastructure level, it’s inevitably of a higher risk. So please take the time to test before deploying.

## What’s Next?

This SDK release seals all data-related concerns we are aware of 😅 It was pretty intense, and I’m proud of the team for making it happen in less than 5 months. There are still two more concerns that we’d like to address. One related to our storage layer and another to UX. We plan to start working on those in mid-March.

We would appreciate your feedback if we missed anything. It will help the team address your points and improve the Freemius platform for the entire WordPress community.

You can reach us anytime, and we’re open to hearing your great ideas.