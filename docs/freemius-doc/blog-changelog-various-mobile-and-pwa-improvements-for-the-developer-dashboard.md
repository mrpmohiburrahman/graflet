[Changelog](https://freemius.com/changelog/) / Various Mobile and PWA Improvements for the Developer Dashboard

This week, we’re following up on the recent [PWA release of our Developer Dashboard](blog-changelog-major-mobile-experience-overhaul-for-the-developer-dashboard.md). Right after the initial launch, we gathered a lot of feedback and doubled down on improving the UX even further. While we conducted multiple audits and fixes, let’s take a look at the most important ones.

### Better PWA Lifecycle Management

Starting with the PWA (or the Installable App), we’ve made several significant improvements.

[![App Update UI](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-app-update-1024x555.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-app-update.png)

The “app update” dialog is now smarter and updates itself even when multiple tabs or windows are open.

[![Freemius App Offline UI](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-pwa-offline-ui-1024x472.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-pwa-offline-ui.png)

The PWA now detects if you’re offline during the initial load or when navigating through the dashboard and displays relevant UI accordingly.

[![Freemius Install instruction for non PWA platforms](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-pwa-install-dialog-1024x576.png)](https://freemius.com/blog/wp-content/uploads/2025/03/freemius-pwa-install-dialog.png)

We understand that the best PWA experience isn’t possible on some platforms and browsers, and the default installation method doesn’t apply to those. Initially, we only displayed the Install button for supported platforms.

To provide a more consistent experience, we now show the Install button for all platforms. If the current platform supports PWA, we display the native installation experience. Otherwise, we show a modal with platform-specific installation instructions.

[![Freemius Install button for the login and registration page](https://freemius.com/blog/wp-content/uploads/2025/03/login-page-install-button-1024x764.png)](https://freemius.com/blog/wp-content/uploads/2025/03/login-page-install-button.png)

To further streamline the experience, we’ve also added the Install button to the Login and Registration pages.

[![Freemius Developer Dashboard faster load time due to PWA caching](https://freemius.com/blog/wp-content/uploads/2025/03/faster-initial-load-time-879x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/03/faster-initial-load-time.png)

Finally, we’ve improved PWA cache management, which has resulted in approximately a **30% faster initial load time**.

### UI & Dark Theme improvements

[![Freemius App Dark Theme](https://freemius.com/blog/wp-content/uploads/2025/03/dark-ui-improvements-1024x683.png)](https://freemius.com/blog/wp-content/uploads/2025/03/dark-ui-improvements.png)

We adjusted several contrasting elements of the Dark Theme to enhance the readability of data-heavy UI components. At the same time, we identified and resolved some lingering UI inconsistencies. For example:

[![Freemius Plans Page under Mobile](https://freemius.com/blog/wp-content/uploads/2025/03/plan-page-improvement-1024x585.png)](https://freemius.com/blog/wp-content/uploads/2025/03/plan-page-improvement.png)

The **Plan** page now adapts better to different screen sizes.

[![Freemius date picker UI](https://freemius.com/blog/wp-content/uploads/2025/03/date-picker-ui-1024x907.png)](https://freemius.com/blog/wp-content/uploads/2025/03/date-picker-ui.png)

The **Date Picker** now renders more effectively on mobile and tablet screens, ensuring the text fits neatly with our new font.

[![Freemius Charts UI on Mobile](https://freemius.com/blog/wp-content/uploads/2025/03/charts-ui-improvement-1024x821.png)](https://freemius.com/blog/wp-content/uploads/2025/03/charts-ui-improvement.png)

The **Chart’s Customize button** and general UI alignment now match our design system.

### Cross browser improvements

[![Freemius Developer Dashboard on Safari](https://freemius.com/blog/wp-content/uploads/2025/03/cross-browser-improvements-1024x587.png)](https://freemius.com/blog/wp-content/uploads/2025/03/cross-browser-improvements.png)

We noticed some glitches and bugs in certain browsers like Safari and Firefox—those have now been fixed.