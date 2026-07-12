[Changelog](https://freemius.com/changelog/) / Changelog summary 5 March, 2023

## Backend changes

- Minor edge case fix in the weekly reporting system.
- Data sanitization in some internal systems.
- Fixed a minor edge case issue in PayPal dispute sync system.
- Fixed a glitch in the password reset mechanism where the reset token in some cases would get invalidated prematurely.
- Enriched the ‘new license creation’ endpoint with a new parameter to optionally white label the license when creating it.
- Updated the system to inherit the white label property when creating child licenses for items in a bundle.
- Increased max file upload size for static files to 120 MB.

## Developer Dashboard

- Increased max file upload size for static files to 120 MB.
- Improvements in the instructions inside the Webhooks Integration page.
- Made the payout email notification read-only, since we want to notify developers and send instructions for the invoice.
- Changed read-only notification configurations to be ‘checkable’ only if they were previously off.
- Removed the unnecessary button from the ‘create license’ dialog.