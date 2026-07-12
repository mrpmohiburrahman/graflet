---
title: "Deploying your Files"
url: "https://freemius.com/help/documentation/selling-templates/deployments/"
source: "docs"
section: "Docs"
category: "Setup for Templates"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 278
---

Creating a release is the only step required to make your template files available for download after a successful purchase. Follow the steps below to deploy your template files:

1. First, ensure to create a ZIP file containing your template files. This ZIP file will be downloaded by your customers after a successful purchase.
   
   Release Notes
   
   We recommend including a `readme.txt` or `readme.md` file in your ZIP file that contains release notes for the version you are releasing. This will help your customers understand what changes or updates are included in the new version or how to use the template files effectively.
2. Navigate to the ***Deployment*** page in the [Freemius Developer Dashboard](https://dashboard.freemius.com/).
3. Click the **Add New Version** button.
4. Add the version number and the required platform version. The version number should follow the [Semantic Versioning](help-documentation-release-management-semantic-versioning.md) so as to make it easier to manage updates and compatibility.
5. The dialog box will prompt you to upload a ZIP file containing your template files. Select the right file and upload it.
6. Once the upload is complete, by default, the zip has an `Unreleased` tag.
   
   Unreleased Tag
   
   The zip is not available for the customers to download, however, this allows you to download the files and test.
7. Once everything is set, change the status from `Unreleased` to `Released` to make the files available for download after a successful purchase for your customers.

Once the release is made, your customers will be able to download the template files after a successful purchase. Learn more about [distributing your templates and providing updates](help-documentation-selling-templates-distribution.md). If you wish to test the checkout flow here how you can make a [sandbox purchase](help-documentation-checkout-integration-testing.md).