[Changelog](https://freemius.com/changelog/) / Data export permission-related improvements

We’ve improved the data export-related permissions in the Developer Dashboard. Only a Product Owner or an Admin can export data from the ‘Users’ page.

[![Freemius User Export](https://freemius.com/blog/wp-content/uploads/2024/03/export-permission-freemius-1024x449.png)](https://freemius.com/blog/wp-content/uploads/2024/03/export-permission-freemius.png)

The rest of the roles can either have view-only permissions (for example Developer or Support) or be completely blocked from viewing Users (for example Accountant).

The ‘Download’ button will now be hidden for roles with view-only permission. The API will also block a request to the `.csv` endpoint.