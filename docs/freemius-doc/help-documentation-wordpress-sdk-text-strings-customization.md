---
title: "Text & Strings Customization"
url: "https://freemius.com/help/documentation/wordpress-sdk/text-strings-customization/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 84
---

All the SDK's text and strings are customizable. Every string has its own unique key which you can use to override it.

You can use the `fs_override_i18n()` function as following:

```php
fs_override_i18n( array(
    'opt-in-connect' => __( "Yes - I'm in!", '{your-text_domain}' ),
    'skip'           => __( 'Not today', '{your-text_domain}' ),
), '{your_slug}' );
```

Or the `override_i18n()` public method of the `Freemius` class:

```php
my_fs()->override_i18n( array(
    'opt-in-connect' => __( "Yes - I'm in!", '{your-text_domain}' ),
    'skip'           => __( 'Not today', '{your-text_domain}' ),
) );
```