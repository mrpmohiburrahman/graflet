### Beta Developer Dashboard fixes

- FIX: The `/stores/` landing page was creating a broken layout in some instances.
- FIX: Redirect to the first available plugin from the first available store if logging in to the new system for the first time.
- FIX (Internal): Certain store-related pages were not working due to some race conditions.
- FIX: Incorrect store name being shown on the menu when a store is freshly edited (from the settings page).
- FIX: Upgrade button not linking to the proper URL (relevant to products that are not selling with Freemius).
- FIX (Internal): Navigating to top-level pages could sometime mess with the selected store in the sidebar menu.
- FIX: Accessing coupons from store level + adding notes to coupons.

### Freemius API-related updates

- FIX: Rare edge case where an opted-in website’s properties were not being updated.
- FIX: Edge case bug fix of the unit price calculation for unlimited-site prices in the invoice.

### Miscellaneous updates

- FIX (Affiliate): Make sure we don’t attribute payments/subscriptions if the affiliate program is no longer active.
- FIX (Automation): For sending wrong missing payout notifications on rare edge cases.