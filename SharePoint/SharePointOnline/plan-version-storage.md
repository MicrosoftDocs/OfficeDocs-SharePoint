---
title: "Plan Version Storage for Document Libraries"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 12/12/2023
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint
ms.localizationpriority: medium
search.appverid:
- SPO160
- SPS150
- MET150
description: "This article provides guidance on how to plan version storage for your organization."
---

# Plan Version Storage for Document Libraries

A file version is created when you edit the file, coauthor a document, another user starts working on the document, a user selects **Save** to upload changes to the library, or when a file's properties are changed. As Versions count towards your SharePoint storage usage, your Organization’s version limits needs to meet your recovery objectives and optimize on version storage.

In the following sections, we call out the options and decisions that you as an administrator should consider when setting up version limits for your organization:

## Determine Default Version limits for your organization

Before you decide the default version history limits for your organization, you need to consider your organization’s recovery objective,** and **version storage usage targets** and evaluate your needs with the **version restore options available to your users** and **storage usage** of the three version storage modes supported by SharePoint.  

In the following sections, we outline the options and decisions administrators should consider when setting up version limits for your organization:

|Select this option:|If you want to:|Benefits|
|---|---|---|
|**Automatic** (Recommended) |Automatically apply optimal storage of versions based on its age & restore probability.<br> With this setting, users have access to most of the recently created versions.<br> As versions age, fewer older versions are stored. No other input is required from Admins.| **Storage Use:** Automatic setting is the recommended setting that offers users' access to high value versions while optimizing storage consumption from versions.<br> <br> **Versions Restore Options:** This setting ensures Version History at key timestamps is always available for restore even on file with no new file edits.|
|**Manual** with Major Version Limit and Expiration Period set| Store versions only until the configured expiration period and within the configured major versions count limits.<br> With this setting, users have access to all versions within the count and expiration period.|**Storage Use:** This setting is the best option for ensuring the lowest quota Impact from version storage as it trims versions that are older than the configured expiration.<br> <br> **Versions Restore Options:** When an expiration limit is set, it's possible for files with no recent edits to have all their versions trimmed if the updated version policy dictates that. For example, if a file doesn't get edited in six months and a six-month version expiration policy is in place, then all that file’s versions are deleted.|
|**Manual** with **Major Version Limits and No Time** set| Always store the configured count of versions regardless of version age. Users have access to all the versions within the count limit.| **Storage Use:** This setting can lead to high quota consumption from versions if you have a high ratio of heavily edited files or if you set the limits too high. <br><br> **Version Restore Options:** This setting is the best option for storing a set number of versions offering you predictable version storage behavior. |

The following image depicts the restore options and the storage use for each setting:

:::image type="content" source="media/version-history/compare-restore-options-storage-use.png" lightbox="media/version-history/compare-restore-options-storage-use.png" alt-text="compare and restore":::

**Example Scenario**

Take an example of a file where 500 versions were created in May, June, and July. Let’s compare the versions available under each version limits:

- **Manual Limits: 500 major versions with expiration of 60 days:** No more than 500 versions are stored and any version older than 60 days are also be deleted. On this file, all versions are eventually deleted as the versions age.  

- **Manual Limits: 500 major versions with no limits:** All versions within the count limit of 500 continues to be stored.  

- **Automatic limits: Under automatic settings** intermittent older versions are trimmed over time resulting in 96% version storage reduction in a 6-month period compared to count limits. Users always have access to a set of versions even when there's no new file edit activity.

:::image type="content" source="media/version-history/automatic-setting-version-storage.png" lightbox="media/version-history/automatic-setting-version-storage.png" alt-text="automatic setting":::

:::image type="content" source="media/version-history/version-activity.png" lightbox="media/version-history/version-activity.png" alt-text="compare versions":::
  
## Understand Version storage under Automatic limits

When this option is selected, SharePoint employs an algorithm* behind the scenes. This algorithm deletes (thins out) intermittent older versions that are least likely to be needed, while preserving sufficient high-value versions. More versions in the recent past and fewer farther back in time - in case restores are required. The algorithm is based on the design principle that the restore value of a version degrades as the version ages and offers end users' access to most of the recently created versions with fewer older versions.

In other words, SharePoint thins out low-value versions on your behalf to reduce the impact of versions on your quota consumption while maintaining your ability to recover from file deletion/corruption events. In addition, this method better protects you than does a count limit setting from a ransomware attack that creates many versions that would fill up your version queue.

*When Automatic setting is selected, the service uses the following algorithm to determine version storage:

- Users can access to a maximum of 500 versions created within the last 30 days.
- Hourly versions (versions that were created at the top of the hour) between 30 to 60 days.
- Daily versions (version created at the beginning of the day) between 60 to 180 days.
- Weekly versions (versions created at the beginning of the week) beyond 180 days or more, is available indefinitely until the maximum 500 count limit has reached.
The service trims the intermediate versions as the above milestones are reached.

Take an example of file with a consistent version creation pattern between the months of June until January. Under Automatic setting, intermittent versions are purged as the versions age resulting in ~94% reduction in version storage used compared to applying count limits only.

:::image type="content" source="media/version-history/automatic-limit-impact-version.png" lightbox="media/version-history/automatic-limit-impact-version.png" alt-text="automatic limit impact":::

## Determine right Count or Expiration version limits

In considering which limits to set, we recommend a balanced approach:

- Setting count limits too high or setting expiration limits for longer duration or never expiring,  stores most versions created, offering users most of versions to restore from. However, a high proportion of actively edited files can result in versions using a high storage.  

- Setting count or expiration limits that are too low can result in data loss due to unrecoverable changes impacting your user’s ability to undo unwanted changes, and other recovery scenarios.

## Report on Version Storage Usage in a SharePoint Site

As a SharePoint Site Administrator, you can request an inventory of the versions on a site, library, or file, which can be used for various scenarios:

- Review current version storage used by existing versions.

- Understand how a version limit impacts new versions by applying the desired limits on existing versions. before configuring limits.  

- Analyze the impact of trimming existing versions before scheduling a trim job.

> [!NOTE]
> Additional reporting options are available with [Microsoft Graph Data Connect](/graph/data-connect-datasets#onedrive-and-sharepoint-online).

When, you run the report a background timer job is scheduled to generate a CSV file of every file version on a given SharePoint Site. The CSV file is saved to the location of your choosing on the site. If you don't want site members to see the report, consider creating a folder with different permissions where only site owners can access the report.

### Report Format

The file version expiration report is in Comma-Separated Values (CSV) format. Each row corresponds to a file version, and it contains the following columns:

| **File Version Identifiers:** | Description |
|:-----|:-----|
|`WebId`|The unique identifier of the web and is a compact column <sup>1</sup>.|
|`DocId`|The unique identifier of the document and is a compact column.|
|`MajorVersion`|The major version number of the file version.|
|`MinorVersion`|The minor version number of the file version.|

| **File Version Information:** | Description |
|:-----|:-----|
|`WebUrl`|The SharePoint Url to the web and is a compact column.|
|`FileUrl`|The web relative Url to the file and is a compact column.|
|`Size`|The size of the version in bytes.|
|`ModifiedBy_UserId`|The identifier of the user who created this version and is a compact column.|
|`ModifiedBy_UserDisplayName`|The display name of the user who created this version and is a compact column.|
|`LastModifiedDate`|The time when the version was last modified.|
|`SnapshotDate`|The time when the version became a historical version.|
|`IsSnapshotDateEstimated`|If this identifier is set to true, then the `SnapshotDate` is a best-effort estimation. The `SnapshotDate` might be estimated if the version was snapshot before January 1, 2023.|

| **Expiration Schedule information:** | Description |
|:-----|:-----|
|`CurrentExpirationDate`|Time when the version is going to expire as it currently stands.|
|`AutomaticPolicyExpirationDate`|Time when the version would be expiring if an automatic expiration policy were to be retroactively applied, estimated on a best-effort basis.|
|`TargetExpirationDate`|Is populated to the same value as `CurrentExpirationDate`. This column is useful for any What-If analysis and batch-updating the expiration dates.|

<sup>1</sup> Compact columns are columns that won't repeat values if two consecutive rows have the same value. It puts empty string for the repeated records. The header for these columns have "Compact" postfix.

### Learn More

For more information, check out the following resources:

- [Tutorial: Generate Version Usage Report](tutorial-generate-version-usage-report.md).
- [Tutorial: Run 'What-If' analysis](tutorial-run-what-if-analysis.md).

