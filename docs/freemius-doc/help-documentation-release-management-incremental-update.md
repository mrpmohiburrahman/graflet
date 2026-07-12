---
title: "Incremental Versions Support"
url: "https://freemius.com/help/documentation/release-management/incremental-update/"
source: "docs"
section: "Docs"
category: "Release Management"
scraped_at: "2026-04-09T19:58:40+06:00"
word_count: 496
---

The **Incremental Versions Support** (also known as **Sequential** or **Staged Upgrades** or **Dependency Upgrade**) feature allows to control the flow of the update process. When a version is marked as incremental, customers must first update to that version before they can update to any subsequent versions.

This feature is useful when introducing some changes in your software where one or more intermediate versions must be installed when upgrading to the latest version. This is a common industry practice and there are various reasons why a software maker might want to do it. For example:

- **Database schema changes**: Where one specific intermediate version does the schema change that subsequent versions rely on.
- **Breaking API changes**: Where an intermediate version bridges the gap between the old and new APIs.
- **Data Migration**: An intermediate version migrates data from the old data structure to the new data structure.

With **Freemius Deployment Mechanism** you can leverage this feature right out of the box to make your software update process more robust and stable.

## How to Mark Incremental Versions[​](#how-to-mark-incremental-versions "Direct link to How to Mark Incremental Versions")

### 1. Flagging Incremental Versions for Deployed Versions[​](#1-flagging-incremental-versions-for-deployed-versions "Direct link to 1. Flagging Incremental Versions for Deployed Versions")

On the **Deployment** page of the **Developer Dashboard**, you will find a table listing all the deployed versions of your product. For each deployed version, a new switch has been added under the new `Incremental` column.

To mark a deployed version as incremental, simply toggle the incremental switch accordingly.

### 2. Flagging Incremental Versions for New Releases[​](#2-flagging-incremental-versions-for-new-releases "Direct link to 2. Flagging Incremental Versions for New Releases")

When changing the status of a version to `Released`, you will see a dialog for **Release Management**. Inside the dialog you will find a section named **Incremental Release**.

To mark a deployed version as incremental, simply toggle the incremental switch accordingly.

## How It Works for Customers[​](#how-it-works-for-customers "Direct link to How It Works for Customers")

Once a version is marked as incremental:

- Customers must update to the first incremental version before they can proceed to any newer incremental version or the latest version.
- If there are no more incremental versions available, customers will be able to update directly to the latest version.

For example, let’s assume you have the following versions deployed:

**Version****Is Incremental**`1.0.0``False``1.1.0``False``**1.1.1**``True``2.0.0``False``2.1.0``False``**2.2.0**``True``2.3.0``False``2.3.1``False`

If a customer is on version `1.0.0`, then they would receive updates in the following sequence:

1. `1.0.0` → `1.1.1`
2. `1.1.1` → `2.2.0`
3. `2.2.0` → `2.3.1`

## Additional Notes[​](#additional-notes "Direct link to Additional Notes")

- This feature can be used both for **newly deployed versions** and for **existing deployed versions**.
- This feature is only for plugins and themes that have a paid version.
- The incremental version state can be toggled any-time, allowing developers flexibility in managing version updates.
- While the incremental update feature is not dependent on our **WordPress SDK**, we recommend always using the latest version of our SDK when deploying an incremental update.