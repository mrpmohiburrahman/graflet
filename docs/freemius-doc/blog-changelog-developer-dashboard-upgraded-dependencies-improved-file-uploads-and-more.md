[Changelog](https://freemius.com/changelog/) / Developer Dashboard: Upgraded dependencies, improved file uploads, and more

As part of our internal housekeeping effort to pay the tech debt we accumulated over the years, we’ve been hard at work to upgrade all dependencies in the Developer Dashboard app. We’re glad to announce it’s been accomplished. The app is now a little faster and contains less JavaScript (talk about dropping support of IE 8 from old dependencies 😅).

During the process, we also realized we weren’t properly utilizing the file upload mechanism in various places. We made significant improvements in that area too.

## Adding filters and supporting drag and drop to file uploads

…from places where you can upload image files, for example:

- Creating a new product
- Updating a product or store’s icon
- Updating your profile picture
- Uploading banner images and screenshots for add-ons

They now support drag-and-drop for better UX. Also, when selecting a file from the *Upload* button, it will filter out unsupported files.

[![File upload UI Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2023/04/new-file-upload-ui.gif)](https://freemius.com/blog/wp-content/uploads/2023/04/new-file-upload-ui.gif)

## Improved UI for add-ons, banner images, and screenshots

If you go to *Settings* on add-on pages, you’ll see we’ve improved the UI for uploading:

- Banner images
- Card banner images
- Screenshots

[![](https://freemius.com/blog/wp-content/uploads/2023/04/addon-banner-images-300x254.jpg)](https://freemius.com/blog/wp-content/uploads/2023/04/addon-banner-images.jpg)

Add-on banners

[![](https://freemius.com/blog/wp-content/uploads/2023/04/addon-screenshot-images-300x233.jpg)](https://freemius.com/blog/wp-content/uploads/2023/04/addon-screenshot-images-scaled.jpg)

Add-on Screenshots

They still support drag-and-drop and feature a nifty file selector.

## Fixed permission issues that arose when developers or support staff were logging in

The new Multi-store Dashboard would sometimes give prompts related to permissions when developers or support staff were logging in.

[![](https://freemius.com/blog/wp-content/uploads/2023/04/incorrect-insufficient-permission-dialog.jpg)](https://freemius.com/blog/wp-content/uploads/2023/04/incorrect-insufficient-permission-dialog.jpg)

We’ve fixed this regression, improved which pages are rendered for team members, and enhanced navigation to relevant pages when switching between products.

## Fixing MailChimp integration issue

Our [MailChimp integration](help-documentation-integrations-mailchimp-integration.md) was not working properly for the Multi-store Developer Dashboard. If your MailChimp list had groups, they weren’t being shown in the UI.

Thank you to our partners who made us aware of this issue. We’ve pushed a fix to mitigate it.

## Housekeeping

- All our AngularJS and related dependencies are up to date.
- We’ve significantly improved the build and dependency management process, which has led to better DX (Developer Experience) and less JavaScript.
- We now have an integration testing framework for the Developer Dashboard to help us develop features more confidently.