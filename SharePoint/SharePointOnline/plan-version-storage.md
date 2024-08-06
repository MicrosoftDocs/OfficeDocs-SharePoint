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

The Version history limits you configure need to meet your organization’s recovery objectives. In the following sections, we call out the options and decisions that you as an administrator should consider when setting up version limits for your organization.

As you plan your version storage strategy, consider these key decision areas: 
- Determine the default document library version history limit for your organization.
- Identify any sites or OneDrive user accounts that would need an exception from the organization default limit. 
- Determine whether to enforce organization version history limits on current content by updating settings on existing document libraries and reducing file version history.  


## Determine default version limits for your organization

To set appropriate default limits for your organization, assess the restore options and storage consumption associated with the three version storage modes offered by SharePoint. This helps you to evaluate how the default limits could affect your users' access to their document versions and the overall storage space utilized by those versions.  


|Select this option:|If you want to:|Benefits|
|---|---|---|
|**Automatic** (Recommended) |Automatically apply optimal storage of versions based on its age and restore probability.<br> With this setting, users have access to most of the recently created versions.<br> As versions age, fewer older versions are stored. No other input is required from admins.| **Storage use:** Automatic setting is the recommended setting that offers your users access to high value versions while optimizing version storage use.<br> <br> **Restore options:** This setting ensures version history at key timestamps is always available for restore even on file with no new file edits.|
|**Manual** with Major Version Limit and Expiration Period set| Store versions only until the configured expiration period and within the configured major versions count limits.<br> With this setting, users have access to all versions within the count and expiration period.|**Storage use:** This setting is the best option for ensuring the lowest quota impact from version storage as it trims versions that are older than the configured expiration.<br> <br> **Restore options:** When an expiration limit is set, it's possible for files with no recent edits to have all their versions trimmed if the updated version policy dictates that. For example, if a file doesn't get edited in six months and a six-month version expiration policy is in place, then all that file’s versions are deleted.|
|**Manual** with **Major Version Limits and No Time** set| Always store the configured count of versions regardless of version age. Users have access to all the versions within the count limit.| **Storage use:** This setting can lead to high quota consumption from versions if you have a high ratio of heavily edited files or if you set the limits too high. <br><br> **Restore options:** This setting is the best option for storing a set number of versions offering you predictable version storage behavior. |

> [!TIP]
> - Consider running a ‘What-if’ analysis report on a site or library to run impact analysis of applying either automatic or manual limits on version storage or users impacted before updating your default limits. 
> - Provide information about default organization version history limits to your users. Tell site owners if you have a process and policy for requesting more.  


The following image depicts the restore options and the storage use for each setting:

:::image type="content" source="media/version-history/cmpr-res-sto-opt-2.png" lightbox="media/version-history/cmpr-res-sto-opt-2.png" alt-text="Screenshot of compare and restore.":::


**Example Scenario**

Take an example of a file where 500 versions were created in May, June, and July. Let’s compare the versions available under each version limits:

- **Manual limits: 500 major versions with expiration of 60 days:** No more than 500 versions are stored and any version older than 60 days are also deleted. On this file, all versions are eventually deleted as the versions age.  

- **Manual limits: 500 major versions with no limits:** All versions within the count limit of 500 continue to be stored.  

- **Automatic limits: Under automatic settings** intermittent older versions are trimmed over time, resulting in 96% version storage reduction in six months period compared to count limits. Users always have access to a set of versions even when there's no new file edit activity.

:::image type="content" source="media/version-history/automatic-setting-version-storage.png" lightbox="media/version-history/automatic-setting-version-storage.png" alt-text="Screenshot of automatic setting.":::

:::image type="content" source="media/version-history/version-activity.png" lightbox="media/version-history/version-activity.png" alt-text="Screenshot of compare versions.":::
  
## Understand Version storage under Automatic limits

The algorithm behind automatic version history limits is based on the design principle that restores value of a version degrades as the version ages. When Automatic limit is selected, SharePoint deletes (thins out) intermittent older versions that are least likely to be used, while preserving sufficient high-value versions. In case restores are required, it ensures that users have access to more versions in the recent past and fewer farther back in time.

Version storage under Automatic setting is determined by the following algorithm:

As versions are created, users have access to the following versions:

- All versions created within 500 count limit in first 30 days.
- Hourly versions (versions created at the top of the hour) between 30 to 60 day period.
- Daily versions (versions created at the beginning of each day) between 60 to 180 day period.
- Weekly versions (versions created at the beginning of the week) beyond 180 days or more are available indefinitely until the maximum 500 count limit has reached.

The service trims the intermediate versions as the above milestones are reached.

Take an example of file with a consistent version creation pattern between the months of June until January. Under Automatic setting, intermittent versions are purged as the versions age resulting in ~94% reduction in version storage used compared to applying count limits only.

:::image type="content" source="media/version-history/automatic-limit-impact-version.png" lightbox="media/version-history/automatic-limit-impact-version.png" alt-text="Screenshot of automatic limit impact.":::

## Determine right Count or Expiration version limits

In considering which limits to set, we recommend a balanced approach:

- Setting count limits too high or setting expiration limits for longer duration or never expiring,  stores most versions created, offering users most of versions to restore from. However, a high proportion of actively edited files can result in versions using a high storage.  

- Setting count or expiration limits that are too low can result in data loss due to unrecoverable changes impacting your user’s ability to undo unwanted changes, and other recovery scenarios.

## Identify Sites or OneDrive User accounts that need an exception from organization defaults
Since default organization settings are applied to all new document libraries created in your organization, you may need to set distinct version history limits on individual SharePoint Sites, OneDrive user accounts, or individual document libraries to meet business requirements. When diverging from the default inheritance settings of your organization, it's advisable to limit the extent of changes to maintain consistency with your organization's version storage practices. For instance, evaluate if your business requirements can be met by applying different version limits to select document libraries, instead of setting a site level policy and applying changes broadly across the entire site, to keep your version storage policies in sync. 

## Decide how the organization version history limits are applied to existing content 
We recommend considering the impact to existing content when updating your organization version limits. Depending on your requirements, you can choose to avoid impacting existing content by applying the limits to new libraries only or update existing content to align to the organization limits by updating the settings of existing libraries or trimming existing file versions.

| If you want to  | Steps to follow |
|---|---|
| **Apply organization defaults to new libraries only.** This option is suitable if your goal is to handle file versioning exclusively in new libraries without altering configurations in existing ones. | [Set default organization version limit to new libraries](set-default-org-version-limits.md) applies the new limits to all new libraries created in your organization. |
| **Apply organization defaults to new libraries, update settings on existing libraries but do not trim existing versions.** This option is suitable if your goal is to adjust the settings for both new and current libraries to handle new file versions without altering any existing file versions. | 1. [Set default organization version limit for new libraries](set-default-org-version-limits.md).<br> 2. Update the limits on existing document libraries on existing sites. <br>**Note:** As the organization limits apply to all new libraries created on your existing sites, you will not need to set a site level policy.<br> For more information, see: [Setting version limits for a site.](site-version-limits.md) |
| **Apply organization defaults to new libraries, update the settings on existing libraries, and trim existing file versions.** Choose this option to fully align new and existing versions to organization limits. | 1. [Set default organization version limit for new libraries.](set-default-org-version-limits.md)<br> 2. Update the limits on existing document libraries on existing sites while allowing the new document libraries created in the site to inherit the organization level version history limits. For more information, see: [Setting version limits for a site.](site-version-limits.md)<br> 3. Trim existing versions on existing sites. For more information, see: [Trim existing versions on a site.](trim-versions.md)  |
