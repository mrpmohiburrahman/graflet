[Changelog](https://freemius.com/changelog/) / A fresh new design for the Developer Dashboard with performance improvements

As 2024 draws to a close, we’re ending the year with an electrifying finale! Introducing a dazzling new design, game-changing UX enhancements, and lightning-fast performance upgrades specifically for the [Developer Dashboard](https://dashboard.freemius.com/)!

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-developer-dashboard-2024-light-1024x777.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-developer-dashboard-2024-light.png)

### Fresh New UI

Our brand and design team has delivered a new UI, focusing on readability and legibility for consuming large amounts of data.

Freemius provides you with a wealth of data and actionable insights in our Dashboard. The primary goal of the UI/UX team has been to make it as easy and seamless as possible to consume this information. With this mission in mind, we present the new UI for the Developer Dashboard.

We have introduced numerous changes to enhance your experience. Here are just a few highlights:

### Improved Data View

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dev-dashboard-data-view-1024x477.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dev-dashboard-data-view.png)

- All data tables are now consolidated within a clean white background for maximum legibility.
- The primary action button to create new entities is now placed inside the toolbar on the left-hand side.
- Row action buttons are aligned to the right without drawing too much attention, allowing you to focus on the data.
- Most inline action elements now appear only when hovering over a row.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dev-dashboard-data-actions-1024x854.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dev-dashboard-data-actions.png)

### Consolidated Details View

We have reviewed and streamlined all detail view items (side navigations), making them cleaner.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/developer-dashboard-item-details-view-1024x789.png)](https://freemius.com/blog/wp-content/uploads/2024/12/developer-dashboard-item-details-view.png)

- Only the most relevant information is displayed initially, with expandable sections to show more details as needed.
- Negative action buttons are now properly highlighted at the end of the details panel.

### Plans Page Improvements

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-plans-page-1024x506.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-plans-page.png)

- The action button has been moved to the top, including the “Release plans to users”.
- Checkout code and links are now consolidated into a single dropdown button.

### Deployment Page Improvements

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-deployment-page-1-1024x626.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-deployment-page-1.png)

- Notices for SDKs and other actionable items are now clearer and more attention-grabbing.
- Configuration options, such as “Add Freemius as a plugin contributor,” have been moved to the top for better visibility.

### Resizable and Collapsible Sidenav

[![](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-resizable-sidenav-1024x659.png)](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-resizable-sidenav.png)

The UX of the sidenav has been improved to accommodate large data views and different screen sizes.

- A drag handler allows you to adjust the width of the sidenav to suit your preference.
- A collapse button enables you to hide the sidebar, letting you focus more on the data.

### Unified Dialogs

[![](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-unified-modal-1024x580.png)](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-unified-modal.png)

All modal dialogs now feature a clear and consistent design. The primary button is always blue, providing a clear hint about the next step, and headers are sticky to maintain context within the dialog.

### Dark mode along with sync to system

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dashboard-themes-1024x578.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-dashboard-themes.png)

If you’re wondering where the dark mode is, don’t worry—it hasn’t gone anywhere! It has simply been relocated to the main dropdown menu on the far right.

Plus, there’s now a new option to sync the theme with your system or browser settings for a more seamless experience.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-developer-dashboard-2024-dark-1024x777.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-developer-dashboard-2024-dark.png)

### Performance Improvement

We saved the best for last! This release comes with a significant performance boost, making the Developer Dashboard noticeably snappier and rendering faster.

We identified the biggest bottleneck when navigating through different pages: the numerous HTTP requests made to load template files. Previously, the system had to wait until all the templates for all components were loaded, even though the data was already prepared.

So, we eliminated this bottleneck without compromising initial load time. The app now smartly makes a single HTTP request to preemptively cache all the template files.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-performance-improvement-1024x452.png)](https://freemius.com/blog/wp-content/uploads/2024/12/dashboard-performance-improvement.png)

This change results in significantly fewer HTTP requests when navigating between pages. It is clearly visible in the video below:

Contrast this with the previous experience, which was noticeably less snappy; the skeletons and components were loaded one after another before the data was finally being displayed (the traditional waterfall experience).

Additionally, we’ve removed outdated scripts that were no longer in use, further contributing to faster loading times.

We hope you enjoy these improvements! Explore the [Developer Dashboard](https://dashboard.freemius.com/) further to uncover even more changes!