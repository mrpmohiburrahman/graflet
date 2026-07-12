[Changelog](https://freemius.com/changelog/) / Fixed Freemius Version Deployment adding unintentional line breaks in PHP comments

We saw a regression in our [latest upgrade](blog-changelog-added-support-for-php-8-2-through-freemius-deployment.md) of [Freemius Deployment](https://freemius.com/help/documentation/selling-with-freemius/deployment/). If a PHP file was written with `CRLF` (Windows) line-ending, then the system added additional line spaces in block comments.

For example, the following block comment:

```
/**
 * The main plugin file.
 * @since 1.0
 * @package MyAwesomePlugin
 */
```

was becoming

```
/**
 * The main plugin file.

 * @since 1.0

 * @package MyAwesomePlugin

 */
```

While this did not break any functionality, we’ve made a quick fix to prevent this from happening.