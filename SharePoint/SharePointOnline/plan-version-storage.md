---
title: "Plan version storage for document libraries(Preview)"
ms.reviewer: rekamath
ms.author: serdars
author: serdars
manager: serdars
recommendations: true
ms.date: 04/30/2024
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

# Plan version storage on document libraries (Preview)

The Version limits you configure need to meet your organization’s recovery objectives and optimize on version storage. In the following sections, we call out the options and decisions that you as an administrator should consider when setting up version limits for your organization:

## Determine default version limits for your organization

Before you decide the default version history limits for your organization, you need to consider your **organization’s recovery objective** and **version storage usage targets**. You need to evaluate your needs with the **version restore options available to your users** and **storage usage** of the three version storage modes supported by SharePoint.  


|Select this option:|If you want to:|Benefits|
|---|---|---|
|**Automatic** (Recommended) |Automatically apply optimal storage of versions based on its age and restore probability.<br> With this setting, users have access to most of the recently created versions.<br> As versions age, fewer older versions are stored. No other input is required from admins.| **Storage Use:** Automatic setting is the recommended setting that offers users' access to high value versions while optimizing storage consumption from versions.<br> <br> **Versions Restore Options:** This setting ensures version history at key timestamps is always available for restore even on file with no new file edits.|
|**Manual** with Major Version Limit and Expiration Period set| Store versions only until the configured expiration period and within the configured major versions count limits.<br> With this setting, users have access to all versions within the count and expiration period.|**Storage Use:** This setting is the best option for ensuring the lowest quota impact from version storage as it trims versions that are older than the configured expiration.<br> <br> **Versions Restore Options:** When an expiration limit is set, it's possible for files with no recent edits to have all their versions trimmed if the updated version policy dictates that. For example, if a file doesn't get edited in six months and a six-month version expiration policy is in place, then all that file’s versions are deleted.|
|**Manual** with **Major Version Limits and No Time** set| Always store the configured count of versions regardless of version age. Users have access to all the versions within the count limit.| **Storage Use:** This setting can lead to high quota consumption from versions if you have a high ratio of heavily edited files or if you set the limits too high. <br><br> **Version Restore Options:** This setting is the best option for storing a set number of versions offering you predictable version storage behavior. |

The following image depicts the restore options and the storage use for each setting:

:::image type="content" source="media/version-history/cmpr-res-sto-opt-2.png" lightbox="media/version-history/cmpr-res-sto-opt-2.png" alt-text="Screenshot of compare and restore.":::


**Example Scenario**

Take an example of a file where 500 versions were created in May, June, and July. Let’s compare the versions available under each version limits:

- **Manual limits: 500 major versions with expiration of 60 days:** No more than 500 versions are stored and any version older than 60 days are also deleted. On this file, all versions are eventually deleted as the versions age.  

- **Manual limits: 500 major versions with no limits:** All versions within the count limit of 500 continue to be stored.  

- **Automatic limits: Under automatic settings** intermittent older versions are trimmed over time, resulting in 96% version storage reduction in six months period compared to count limits. Users always have access to a set of versions even when there's no new file edit activity.

:::image type="content" source="media/version-history/automatic-setting-version-storage.png" lightbox="media/version-history/automatic-setting-version-storage.png" alt-text="Screenshot of automatic setting.":::

:::image type="content" source="media/version-history/version-activity.png" lightbox="media/version-history/version-activity.png" alt-text="Screenshot of compare versions.":::
  
## Understand version storage under automatic limits

When this option is selected, SharePoint employs an algorithm* behind the scenes. This algorithm deletes (thins out) intermittent older versions that are least likely to be needed, while preserving sufficient high-value versions. More versions in the recent past and fewer further back in time - in case restores are required. The algorithm is based on the design principle that the restore value of a version degrades as the version ages and offers end users' access to most of the recently created versions with fewer older versions.

In other words, SharePoint thins out low-value versions on your behalf to reduce the impact of versions on your quota consumption while maintaining your ability to recover from file deletion/corruption events. In addition, this method better protects you than does a count limit setting from a ransomware attack that creates many versions that would fill up your version queue.

*The algorithm behind automatic version history limits is based on the design principle that restore value of a version that degrades as the version ages. When Automatic limit is selected, SharePoint deletes (thins out) intermittent older versions that are least likely to be used, while preserving sufficient high-value versions. This ensures users have access to more versions in the recent past and fewer farther back in time in case restores are required.

Version storage under Automatic setting is determined by the following algorithm:

As versions are created, users have access to the following versions:

- **All versions** created within 500 count limit in first 30 days.
- **Hourly versions** (versions created at the top of the hour) between 30 to 60 day period.
- **Daily versions** (versions created at the beginning of each day) between 60 to 180 day period.
- **Weekly versions** (versions created at the beginning of the week) beyond 180 days or more are available indefinitely until the maximum 500 count limit has reached.

The service trims the intermediate versions as the above milestones are reached.

Take an example of file with a consistent version creation pattern between the months of June until January. Under Automatic setting, intermittent versions are purged as the versions age resulting in ~94% reduction in version storage used compared to applying count limits only.

:::image type="content" source="media/version-history/automatic-limit-impact-version.png" lightbox="media/version-history/automatic-limit-impact-version.png" alt-text="Screenshot of automatic limit impact.":::

## Determine right count or expiration version limits

In considering which limits to set, we recommend a balanced approach:

- Setting count limits too high or setting expiration limits for longer duration or never expiring,  stores most versions created, offering users most of versions to restore from. However, a high proportion of actively edited files can result in versions using a high storage.  

- Setting count or expiration limits that are too low can result in data loss due to unrecoverable changes impacting your user’s ability to undo unwanted changes, and other recovery scenarios.

