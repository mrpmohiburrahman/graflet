[Changelog](https://freemius.com/changelog/) / Deployment now supports Update URI

WordPress 5.8 introduced a new [Update URI](https://make.wordpress.org/core/2021/06/29/introducing-update-uri-plugin-header-in-wordpress-5-8/) header/ This should prevent WordPress from mistakenly downloading an update from [WordPress.org](https://wordpress.org) when the plugin is not originated from [wp.org](https://wp.org), and therefore end up overriding the plugin with a different one.

Our WordPress SDK prevents such a situation from happening. Still, if the plugin is deactivated (i.e. the SDK is not executed as part of the updates logic), this problem can occur.

I’m happy to share that Freemius’s deployment mechanism now officially supports the [Update URI](https://make.wordpress.org/core/2021/06/29/introducing-update-uri-plugin-header-in-wordpress-5-8/) header and works as follows:

1. Add (or override) the Update URI header for paid versions with [https://api.freemius.com](https://api.freemius.com) to prevent the problem.
2. If the Update URI header was already added before deployment to Freemius, it will be stripped from the free version when pointing to [freemius.com](index.md). This is because we don’t support updates of free products, and also because we want to make sure that [wp.org](https://wp.org) updates will work as expected.
3. For now, if there’s a custom Update URI header that is pointing elsewhere (not to freemius.com) keep it as is in the free plugin version, assuming you had a good reason to custom set it.