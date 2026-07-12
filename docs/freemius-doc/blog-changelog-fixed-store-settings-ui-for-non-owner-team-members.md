[Changelog](https://freemius.com/changelog/) / Fixed Store Settings UI for Non-Owner Team Members

We noticed a UI glitch on the Store Settings page affecting team members who are not the store owner. For security reasons, non-owners are not allowed to update any store configuration. However, the UI did not fully reflect this restriction and displayed the settings in an editable state.

While any interaction with the form was correctly blocked at the API level, the editable UI created confusion for makers and their teams.

[![Freemius Store Config page for non team owners](https://freemius.com/blog/wp-content/uploads/2025/12/store-config-page-1024x584.png)](https://freemius.com/blog/wp-content/uploads/2025/12/store-config-page.png)

To address this, we’ve released an update where non-store owners now see the Store Settings in a read-only state, along with a clear notice explaining why the configuration cannot be updated.