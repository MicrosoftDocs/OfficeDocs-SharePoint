---
ms.date: 05/26/2020
title: Mover Migration FAQ
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Mover Migration FAQ"
---
#  Mover Migration FAQ

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte has been fully integrated into Migration Manager. For full details see: [Mover retirement timeline](mover-retirement-timeline.md).  Migration Manager does not support the migration of Amazon S3 or Azure blob storage.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and in private preview.  To learn more, see [How to participate in the Cross-tenant SharePoint migration preview](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).




## What gets transferred?

Only owned folders and the root files for each user are copied. If a user isn't the owner of data they can access, we do not copy it. Content may be automatically reshared after it's migrated so that each user has access to their content exactly as before.

## Does Mover sync files?

Our app offers a source-to-destination delta—when you run a transfer, we compare the destination directory to the source, and only transfer new or modified files over. We call this our incremental feature.

We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on.

Here are a few examples of how we deal with changes to files and folders.

**Content changes**: If a document is edited in your source or you have added a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing file(s) in the destination.

**Name changes**: If the name of a file or folder changes in Office 365, we treat it as a brand new object. This can lead to duplicate files being migrated to Office 365, or worse in that entire folders worth of data would be duplicated from the changed folder downwards.

**Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.

## Does Mover delete files?

We never delete your data from any source. Our app simply takes your data from one place and copies it to another—akin to *copy and paste* rather than *cut and paste.* We also don't retain any of your cloud storage data for any reasons.

We strive to keep your users' experience as similar as possible between your new Office 365 and old Office 365 domains.

## How are permissions affected?

When moving to Office 365 from Office 365, user roles *on folders* change.

During a migration, we don't explicitly set a user as an owner of data.

In Office 365, ownership of files and folders is always implicitly set by virtue of copying data into a user.

## Translating permissions


>[!Note]
>Our app only sets permissions on folders.

## Can I rearrange content during a migration?

Not recommended. Any major changes in directory structure should happen before or after your migration. It is also not a good idea to use our app to rearrange content.

The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is retransferred, including all subfolders.

When sharing permissions are transferred, both owners and collaborators receive duplicate data if content has been rearranged or renamed.

## What happens to external sharing links?

Our app doesn't recreate external sharing links. After migration, these have to be set in the destination manually.

## What about external collaborators?

We don't share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external users.

## Does Mover preserve file versions?

We don't preserve file versions. During a migration, only the most recent version of a file is transferred to Office 365 from Office 365.

## Does Mover notify users?

We automatically suppress all emails to users so they aren't bombarded with excessive notifications about the data they now have access to.

## Will multiple duplicate migrations and accounts help?


Creating multiple duplicate migrations, either in a single account or across multiple accounts, isn't recommended.

The Mover application has an allotted amount of resources per tenant-to-tenant connection. Creating multiple duplicate migrations won't increase the number of resources provided.

>[!Warning]
>Creating multiple or duplicate migrations of the same source or destination tenant connection typically result in throttling, crashes, and even outright failures.



