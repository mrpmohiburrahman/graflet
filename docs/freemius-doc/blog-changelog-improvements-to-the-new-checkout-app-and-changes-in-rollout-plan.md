[Changelog](https://freemius.com/changelog/) / Improvements to the new checkout app and changes in rollout plan

Following feedback from our makers, we’ve made several improvements to the new version of our checkout app.

### Fixed sticky footer issue

We noticed that – in some cases – during browser and/or UI resizing, the sticky footer was not properly stuck.

[![](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-sticky-footer-1024x187.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-sticky-footer.png)

We were able to identify and fix the root cause.

### Form font size improvements

[![](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-bigger-font-size-888x1024.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-bigger-font-size.png)

We’ve increased the font size from 14px to 16px for better readability and more breathing space.

### Form validation and UX improvements

[![](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-form-validation-1024x955.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-form-validation.png)

We’ve made several improvements to the form validation, notably:

1. Clicking on the ‘Review Order’ or ‘Subscribe’ buttons would sometimes not focus the first visible invalid form element. For example, if both the email and credit card fields were empty, clicking on the ‘Review order’ might have focused the credit card field instead of the email field. This has been fixed. The first visible invalid form element will now be focused.
2. We identified an edge case where the zip code field was incorrectly focused even after entering a valid value. We fixed it.
3. In sandbox mode, using the autofill button would sometimes not clear some form-validation errors. We have fixed them as well.

### Improvements to the country picker

[![](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-dropdown-1024x580.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-dropdown.png)

We’ve integrated a custom dropdown with a search capability in the country picker form field. This improves the UX when going through a large list of countries.

### Fixing hidden currency bug

We noticed that if the default `USD` currency was configured as hidden and the checkout was loaded with another currency, then the currency picker in the front end would still show up, and selecting the USD will cause bugs.

We fixed it by not letting the currency picker show up in such cases. Loading the checkout without specifying a currency will still load the hidden `USD` by default, though. In the future, we will further enhance it to properly load the first visible currency by default instead of always loading the `USD`.

### New licensing unit `credit`

Following a request from our maker, we’ve implemented `credit` as a valid licensing unit.

[![](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-license-unit-1024x553.png)](https://freemius.com/blog/wp-content/uploads/2024/01/freemius-checkout-license-unit.png)

If you’re using Freemius for your SaaS or plugins and need a custom licensing unit, please get in touch with us.

### Making the new checkout the default

Due to the holiday season and to give some more time to our makers, we are enabling the new checkout for everyone who isn’t using a custom CSS for the legacy checkout starting 14 January. Please note that you can always use the `checkout_style` parameter to force-load the style of your choice. You can find more about it [here](blog-changelog-checkout-redesigning-phase-1-features-migration-guide.md).

Following the timeline of rollout, we plan to make the new checkout default for everyone, starting **1st February**. Please read the [migration guide](blog-changelog-checkout-redesigning-phase-1-features-migration-guide.md) and [prepare any custom CSS](help-documentation-selling-with-freemius-applying-css-customization.md) before the date.