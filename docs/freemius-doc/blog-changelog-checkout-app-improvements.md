[Changelog](https://freemius.com/changelog/) / Checkout app improvements

We’ve made some minor improvements to the Checkout app to pave the way for big upcoming projects.

### Fixed form validation issues

[![Freemius Checkout Form Validation](https://freemius.com/blog/wp-content/uploads/2023/11/freemius-checkout-user-form-validation.png)](https://freemius.com/blog/wp-content/uploads/2023/11/freemius-checkout-user-form-validation.png)

We realized we weren’t validating the user form from the front end in some edge cases. We’ve fixed this and the form can now only be submitted once it is validated completely.

We also saw some regression in the error message in the zip/postal code field. We fixed this as well.

### Fixed marketing opt-in UI

In some edge cases, marking the marketing opt-in as ‘Yes’ would make the section disappear. We found the root cause and applied a fix.

### Other notable changes:

- We found out that the HMRC API we use to get exchange rates for invoices had been migrated. We’ve moved to the new API which should fix broken invoices.
- A few countries appeared out of order in the dropdown. This has also been fixed.
- Internal build script optimization is now resulting in smaller asset size, making our Checkout app load faster.