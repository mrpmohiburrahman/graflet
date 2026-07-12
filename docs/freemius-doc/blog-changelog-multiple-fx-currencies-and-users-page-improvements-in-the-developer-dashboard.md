[Changelog](https://freemius.com/changelog/) / Multiple FX currencies and Users page improvements in the Developer Dashboard

This week’s changelog comes with many new features in the Developer Dashboard.

### Supporting multiple Foreign Exchange currencies

After we introduced a “[Foreign Exchange – USD](blog-changelog-major-updates-to-the-multi-store-developer-dashboard.md)” virtual currency to display transactional data on the new “Sales Analytics” page, we received a request to support other foreign exchange currencies too. This week, we are releasing that feature.

[![](https://freemius.com/blog/wp-content/uploads/2023/01/multiple-fx-currencies.jpg)](https://freemius.com/blog/wp-content/uploads/2023/01/multiple-fx-currencies.jpg)

Apart from the “FX-USD”, you can convert your transactional data into any of the currencies Freemius supports.

### Subscriptions and Payments tabs on the Users page are now open by default

Feedback from our partners made us realize that Subscriptions and Payments are the primary things one wants to see when accessing the Users page. It was hidden behind an accordion, which you had to click to view information.

[![](https://freemius.com/blog/wp-content/uploads/2023/01/enhanced-user-page-subscriptions-payments.jpg)](https://freemius.com/blog/wp-content/uploads/2023/01/enhanced-user-page-subscriptions-payments.jpg)

To save you the hassle, those sections are now open by default and load as soon as the licenses are loaded.

### Other changes

- Fix: In some cases, the same currencies appeared multiple times in the filtering UI.
- Fix: Internal pub/sub architecture of the app.
  
  - In some edge cases, the plugin would not display when navigating between pages.
  - When navigating to one store away from another’s product, the state held incorrect data.
- Fix: Race condition when loading subscriptions/licenses of a user.
- Fix: Incorrect URL in the share menu.
- Fix: Login reCAPTCHA not showing up, due to a race condition in loading the script.
- Update: Improved validation in the login/registration/password recovery form.