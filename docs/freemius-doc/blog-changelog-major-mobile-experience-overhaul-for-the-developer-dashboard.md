Following our recent rebranding and UI/UX improvements to the Developer Dashboard, this week we have deployed a major overhaul focused on enhancing the mobile experience. While our Developer Dashboard was already accessible on mobile, we wanted to take the experience even further and bring it up to today’s standards. If our makers need to check data *on the go*, we want to fully support that.

So, without further introduction, let’s dive into what has changed and what has been improved.

### Better UX for the data tables

When optimizing for mobile, we started with the most data-heavy UI elements—specifically, the **Payments, Subscriptions, and Licenses** pages.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/subscription-table-mobile-view-866x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/subscription-table-mobile-view.png)

We identified opportunities to improve visual feedback and streamline the display of data, ensuring makers can quickly access the most relevant information *on the go*. Here’s what we changed:

- Clicking on the **ID** cell now copies the value instantly for quick access.
- We rearranged some table cells, ensuring the most important information remains visible.
- Tables now feature a **loading animation**, providing clear feedback on background processes.
- To declutter the view, certain advanced data (such as **User ID** or **Site ID**, which previously appeared on hover) will no longer be displayed on mobile.

### Easy navigation for individual items

After optimizing the tables, we focused on improving how individual rows are presented in tables like **Subscriptions, Payments, and Carts**. On desktop, selecting a row opens a sidebar from the right, revealing more details about the item.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/subscription-table-detail-view-1024x703.png)](https://freemius.com/blog/wp-content/uploads/2025/02/subscription-table-detail-view.png)

Navigation is seamless—clicking on another item automatically updates the sidebar. However, on mobile devices, this experience was less intuitive. The sidebar appears in full-screen mode, requiring users to **first close the sidebar** before selecting another item.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/sidebar-details-navigation-menu-1024x857.png)](https://freemius.com/blog/wp-content/uploads/2025/02/sidebar-details-navigation-menu.png)

To improve navigation, we’ve introduced **Previous** and **Next** buttons in the sidebar header. Now, you can quickly move between items without needing to close the sidebar first.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/payments-detail-view-1024x608.png)](https://freemius.com/blog/wp-content/uploads/2025/02/payments-detail-view.png)

Additionally, we’ve added a sidebar view for the **Payments** table, making it easier to access detailed payment information.

### Full screen modals

We noticed that several of our **form-heavy dialogs and modals** weren’t optimized for smaller screens. Instead of overlaying them, we now display them in full-screen mode for a better mobile experience.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/refund-dialog-fullscreen-866x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/refund-dialog-fullscreen.png)

For example, when you click the **“Refund”** button on the Payments page, you’ll notice a much smoother experience. After all, managing your business *on the go* should feel effortless!

### Improved UI for Analytics

We fine-tuned the **charts UI** for mobile to ensure all data is properly displayed and fixed any visual glitches we found.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/improved-analytics-ui-945x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/improved-analytics-ui.png)

Viewing charts on mobile is now a significantly better experience.

### Improved main navigation

The **left sidebar** serves as the main navigation, and we’ve ensured it behaves smoothly on mobile by fixing a few glitches.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/main-navigation-sidebar-733x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/main-navigation-sidebar.png)

We also made the navigation menu smarter—it now automatically closes itself when it detects that it should get out of the way.

### Better User & Site pages

Unlike other details that appear in the right sidebar, **User and Site pages** contain too much information to fit within a sidebar. That’s why we continue to display them as regular pages.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/user-page-ui-669x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/user-page-ui.png)

We reviewed how these pages render on mobile and made several layout improvements.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/site-page-ui-686x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/site-page-ui.png)

Additionally, we took this opportunity to **rework certain sections** of the page, ensuring they use screen space more efficiently.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/ownership-licensing-ui-1024x360.png)](https://freemius.com/blog/wp-content/uploads/2025/02/ownership-licensing-ui.png)

For example, we have combined the **License, Subscription, Plan,** and **Owner** sections inside **Site** to display a simple list of actionable items.

### Editing plan now works under mobile

We noticed that **editing plans on mobile** wasn’t working at all. So, we revisited the design and made it fully responsive.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/editing-plan-mobile-793x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/02/editing-plan-mobile.png)

Now, you can configure plans *on the go*—because why not?

### An installable PWA

Saving the best for last! Now that our Developer Dashboard is fully optimized for mobile, we’ve taken it a step further by converting it into a **PWA (Progressive Web App)**. This means you can **install it on Android and iOS devices** for a more seamless experience.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/pwa-install-prompt-579x1024.jpg)](https://freemius.com/blog/wp-content/uploads/2025/02/pwa-install-prompt-scaled.jpg)

To install the app, simply **click the “Install” button** when prompted by your browser. On **Android**, you’ll also find a dedicated **“Install App”** button in the top-right dropdown menu.

[![](https://freemius.com/blog/wp-content/uploads/2025/02/install-app-button-1024x764.png)](https://freemius.com/blog/wp-content/uploads/2025/02/install-app-button.png)

- For **iOS** devices, you’ll need to manually select **“Add to Home Screen”** to save the app.
- For desktop you can also click the **Install App** button while using Chrome to create a shortcut under your launcher.

### Various bug fixes

As we refined the mobile experience, we also addressed several bugs across the Dashboard. Here are some of the most notable fixes:

- Fixed **touch issues** with the switch UI.
- Resolved **alignment issues** in grouped input fields.
- Fixed **UI regression** in the analytics screenshot modal.
- Made the **Profile page** fully responsive.
- Fixed an **image issue** on the **Perks** page—if you’re eligible, simply click the top-right menu button to access your perks.
- Fixed a bug where the **country** wasn’t displaying inside subscription details.
- Updated the **email instruction UI** for static products.
- Refreshed the **brand color palette** from our internal design library.

We hope you enjoy these latest improvements to the Dashboard app! 🚀

If you’d like to see more mobile features—such as **push notifications for sales**—let us know via our **feature request board**.