[Changelog](https://freemius.com/changelog/) / Improved UX when adding a team member in the Developer Dashboard

Previously we could re-add a team member using the UI from the **Settings &gt; Team** page (or just the **Team** page from the Beta Developer Dashboard).

We discovered this edge case bug and fixed it with a notification that the person is already a team member.

[![](https://freemius.com/blog/wp-content/uploads/2022/10/freemius-team-member-re-adding.gif)](https://freemius.com/blog/wp-content/uploads/2022/10/freemius-team-member-re-adding.gif)

This also prevents accidentally using our API to demote oneself from Owner or Admin. In order to change the permission of a team member, please use the dropdown menu next to the member.

[![Freemius Developer Dashboard Member Permission](https://freemius.com/blog/wp-content/uploads/2022/10/freemius-change-member-permission.png)](https://freemius.com/blog/wp-content/uploads/2022/10/freemius-change-member-permission.png)