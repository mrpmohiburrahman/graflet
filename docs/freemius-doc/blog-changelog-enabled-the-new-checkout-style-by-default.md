[Changelog](https://freemius.com/changelog/) / Enabled the new Checkout style by default

Today, we’re rolling out the new Checkout for everyone.

[![New checkout style](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-bigger-font-size-888x1024.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-bigger-font-size.png)

The new style will show up regardless of whether you have a custom CSS setting for the legacy checkout or not.

If you want to customize the new Checkout with CSS, please see our official guide [here](help-documentation-selling-with-freemius-applying-css-customization.md).

[![Freemius Developer Dashboard - Checkout CSS setting](https://freemius.com/blog/wp-content/uploads/2024/02/checkout-custom-css-setting-1024x796.png)](https://freemius.com/blog/wp-content/uploads/2024/02/checkout-custom-css-setting.png)

Make sure to save the URL in the ‘**Custom Checkout CSS file’** under the Developer Dashboard and not the one marked as `(Legacy)`.

If for some reason you’d still like to use the legacy Checkout, we are offering it for a limited time. You must pass the `checkout_style: 'legacy'` in the JS snippet configuration.

```
    const handler = FS.Checkout.configure({
        plugin_id:  '9987',
        plan_id:    '16744',
        public_key: 'pk_f6ac0907ee421b1db0c94833cf26b',
        image:      'https://your-plugin-site.com/logo-100x100.png'
    });
    
    $('#purchase').on('click', function (e) {
        handler.open({
            // Force load the legacy checkout
            checkout_style: 'legacy',
            name     : 'My Awesome SaaS',
            // ...
        });
        e.preventDefault();
    });
```

We urge you to stop using the legacy Checkout and migrate to the new one as soon as possible.