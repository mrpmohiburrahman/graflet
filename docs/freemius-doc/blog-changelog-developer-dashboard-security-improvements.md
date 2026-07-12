[Changelog](https://freemius.com/changelog/) / Developer Dashboard security improvements

We now only use a secure httpOnly cookie for the Developer Dashboard. The change is transparent and you shouldn’t notice any changes. Please be aware of the following:

- If you select the ‘**remember me**‘ option during login, it will remember you for the next 7 days.
- If you do not, you will be logged out as soon as you close the browser window. This may play out differently if you’ve configured your browser to restore ‘sessions’.

This change won’t revert if you’ve been using your Developer Secret Key to communicate with the Freemius API.