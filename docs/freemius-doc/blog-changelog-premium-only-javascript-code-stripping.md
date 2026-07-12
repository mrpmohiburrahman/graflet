[Changelog](https://freemius.com/changelog/) / Premium only JavaScript code stripping

We’ve been stripping premium-only JavaScript code written in between `<fs_premium_only>` and `</fs_premium_only>` comment tags. For example:

```
(function($){
    /* <fs_premium_only> */
    // ... my premium only code ...
 
    /* </fs_premium_only> */
})(jQuery);
```

Also, as a recommendation for minifiers, we [mentioned](https://freemius.com/help/documentation/selling-with-freemius/deployment/#stripping_premium_only_css_javascript_logic) the following:

```
module.exports = {
  optimization: {
    minimizer: [
      new UglifyJsPlugin({
        uglifyOptions: {
          output: {
            comments: /\<\/?fs_premium_only\>/i,
          },
        },
        extractComments: true,
      }),
    ],
  },
};
```

But in some cases, if you had other preserving comments with the `/*!` style, we didn’t properly take care of that. With this update, we will now be stripping all JS codes between `/*! <fs_premium_only> */` and `/!* </fs_premium_only> */` tags.