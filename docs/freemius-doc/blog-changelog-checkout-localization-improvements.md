[Changelog](https://freemius.com/changelog/) / Checkout localization improvements

We made some small but useful improvements to the new feature we rolled out last week: supporting localization in our checkout.

- The URL query parameter `language` will now serve as an alias to the `locale` parameter.
- You can supply a valid (and supported) language code too, instead of the full locale code. For example, this will work `https://checkout.freemius.com/...?language=fr` as well as `https://checkout.freemius.com/...?language=fr_FR`.
- We improved the UX of the language selector UI to show a loading animation while the selected locale is loaded in the background.