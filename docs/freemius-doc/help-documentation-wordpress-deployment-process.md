---
title: "Deployment Process"
url: "https://freemius.com/help/documentation/wordpress/deployment-process/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 200
---

With the integration process completed, you're ready to [Deploy](help-documentation-release-management-deployment.md) your plugin or theme to the Freemius Developer Dashboard.

First, compress (Zip) the root folder of your product that will be uploaded to the Freemius Developer Dashboard.

Begin the deployment process by:

1. Going to ***Deployment*** page
2. Click the ***Add New Version*** button.
3. Then upload the product ZIP file.
4. The product code will then be parsed and checked before the final free/premium versions of the product are generated and compressed into production ready Zip files.

For products that have a free plan defined, Freemius generates both free and premium versions of your WordPress product directly from the Zip you upload. Code wrapped in premium-only conditional logic (in the previous step) will only be included in the premium version. It will be stripped out entirely from the free version.

The free version can be downloaded manually and uploaded to WordPress.org via SVN. The premium version, along with all future updates, will be served directly from the Developer Dashboard to paying customers with an active license (they'll see update notifications via the WP Admin).

Once you've integrated your WordPress product with Freemius and deployed it, you're ready to start selling!