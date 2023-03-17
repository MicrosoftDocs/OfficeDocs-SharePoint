---
ms.date: 06/03/2020
title: Mover Microsoft 365 Migration FAQ
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
description: "Frequently asked questions when using Microsoft Mover to migrate to Microsoft 365."
---
# Microsoft 365 FAQ


>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from external cloud sources has been fully integrated into Migration Manager.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and scheduled for release in Spring 2023.

## Data migrated by Mover

Mover only migrates data from:

- An individual's **online drive storage**, such as OneDrive, MyDrive, etc.

Mover **does not** migrate e-mails, mailboxes, contacts, calendars, site layouts/collections/pages/lists, etc.

## Unsupported files and characters

We automatically process file and folder names to ensure they are accepted by Microsoft 365:

- Files larger than `15 GB` are not migrated.
- Files with a size of `0 bytes` (zero-byte files) are not migrated.
- The following characters in file or folder names are removed:
`" * : < > ? / \ |`

- Leading tildes (`~`) are removed.
- Leading or trailing whitespace is removed.
- Leading or trailing periods (`.`) are removed.
- See [Invalid file names and file types](https://support.office.com/article/invalid-file-names-and-file-types-in-onedrive-onedrive-for-business-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa) for all other limitations.

In some possible circumstances with older sites, any file or folder ending in `_files` could fail. If you experience these errors, contact Support.

Microsoft currently has no file type limitations, meaning you can upload data with any file extension. For more info, see [Types of files that cannot be added to a list or library](https://support.microsoft.com/office/types-of-files-that-cannot-be-added-to-a-list-or-library-30be234d-e551-4c2a-8de8-f8546ffbf5b3)

## Character limits for files and folders

- Filenames can have up to 256 characters.
- Folder names may have up to 250 characters.
- Total path length for folder and filename combinations can have up to 400 characters. For more info, see below.

## What happens to long paths?

During a pre-scan, our app automatically detects and reports paths that are too long for OneDrive or SharePoint to accept. The current path length limit for Microsoft 365 is 400 characters. The path length is calculated when going in to Microsoft 365 and includes your tenant URL, user site, path, and any character encoding.

**Example**:

This path is 93 characters long despite *Documents/Old Docs* being only 18 characters:</br>

`https://example-my.sharepoint.com /personal /example_user /%2FDocuments%2FOld%20Docs`

If a file exists that has a very long path, our app skips it, and reports it in your log files.

To save time and headaches, before you migrate, you are encouraged to shorten any identified long paths.

![Turn this into this](media/turnthis-intothis-dropbox.png)

## What metadata is preserved in migrations into Office 365?

|Source Connector|Creation date|Created by user|File modified date|Last modified by (user)|Folder permissions|Notes|
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|Amazon S3|Buckets: Yes</br>Folders: No</br>Files: Same as Modified date|No|*Read clarification note below|Yes|No|No|
|Azure Blob Storage|No|No|*Read clarification note below|No|No||
|Box (co-admin)|Yes|Yes|*Read clarification note below|Yes|Yes|Box Notes are converted to Word documents.|
|Box (single user)|Yes|Yes|*Read clarification note below|Yes|Yes|Box Notes are converted to Word documents.|
|Dropbox (single user)|No|No|*Read clarification note below|No|No|We have a feature request to get the timestamp and authorship information out of Dropbox.|
|Dropbox Business (admin)|No|No|*Read clarification note below|No|Yes|We have a feature request to get the timestamp and authorship information out of Dropbox.|
|Egnyte|No|Yes|*Read clarification note below|No|Yes||
|G Suite (Admin)|Yes|Yes|*Read clarification note below|Yes|Yes||
|Google cloud storage|Buckets: Yes</br>Folders: No</br>Files: Same as modified date|No|*Read clarification note below|No|No||
|Google drive (Single user)|Yes|Yes|*Read clarification note below|Yes|No||
|Office 365 (OneDrive/SharePoint admin)|Yes|Yes|*Read clarification note below|Yes|Yes ||
|OneDrive Consumer|Yes|Yes|*Read clarification note below|Yes|No||
|OneDrive for Business (Single user)|Yes|Yes|*Read clarification note below|Yes|No||

> [!IMPORTANT]
> Clarification regarding **File modified date**
>
> Our tool sets the **File modified date** in Office 365 based on the time the file was updated in the storage provider's servers; *not the metadata timestamp uploaded with the document from your local computer.*
>
> Each cloud provider may refer to the **server modified timestamp** slightly differently.  For example, Box refers to the *server modified timestamp* as "Updated" in its UI and the *user modified timestamp* as "Modified".  Check with your cloud provider to confirm how they refer to these fields.

## Does the Mover app interact with the sync client in OneDrive for Business?

We do not interact with the sync client in **OneDrive for Business**. Before a migration, We recommend disabling it. If you use it during a migration, it tries to sync all the migrating data.

## What happens to shared data?

Data shared with a user by another user appears in the **Shared with me** folder. Data owned by a user appears in the user's designated destination folder.

## What about notifications?

To prevent users from being spammed, the Mover app silences notifications during the migration.

## What happens to data shared to Microsoft 365 Groups?

Data shared to a Microsoft 365 Group does not appear in the **Shared with me** section. Microsoft also does not notify users that they are now a member of a Microsoft 365 Group.

> [!NOTE]
> This is a limitation of Microsoft 365 Groups and cannot be changed on our end. The user must navigate to the appropriate group within either their Outlook Desktop Client, or by logging into their preferred email through **outlook.office.com**.

After the user has logged in:

1. Navigate to the left hand menu.
2. Scroll down the folder listings to **Groups**.
  a. If the available groups are not visible, to open the group directory, select the small arrow beside the **Groups** listing.
3. Select the desired group.
From here, the left-hand menu should change, enabling you to open and edit **Files/Notes** within the selected Microsoft 365 Group.

## What SharePoint site formats are supported?

Both Modern and Classic sites are supported, and appear the same in our app.

## What will my file paths look like in SharePoint?

During the migration setup (described later in this guide), you can edit the path(s) to specify where in SharePoint you would like your data to go. From the root level of SharePoint, you can go into **Site Collections**, and inside each **Site Collection**, directories for **Site Contents** and **Subsites** appear.

**Site Contents** takes you to document libraries (for example, the **Documents** section), whereas **Subsites** takes you to the **Subsites** of that site collection. Navigating **Subsites** takes you through the same dichotomy.

Most cloud storage providers, G Suite Drive for example, start the listing with a user such as `/user@example.com/Marketing Folder`. SharePoint does not do this, so you would be looking at a path such as `/Marketing/Site Contents/Documents`.

## How does library permissions inheritance affect migration?

To set specific permissions on folders in a document library, inheritance must be disabled. Permissions inheritance is typically turned on by default, which makes all the data within the library subject to the permissions set on the library. This is similar behavior to team folders or team drives in other cloud services, whereby if users have access to the root level, they have access to everything contained within.

If inheritance is not disabled at the root, any permissions we try to set on individual folders are overridden by the library access permissions.

**To disable inheritance:**

In the Library settings, visit **Permissions for this document library**:

1. Select **Stop Inheriting Permissions**.
  a. This enables you to select the permissions you would like to remove:
   - Site members
   - Site visitors
2. Select **Remove User Permissions**.

This prevents site members/visitors from inheriting permissions to all the data that we migrate into that library, allowing permissions to only those site members who we explicitly write to the folders themselves.

For more info see [SharePoint permissions inheritance](/sharepoint/what-is-permissions-inheritance).

## Does Mover support Microsoft Teams?

Microsoft Teams appears and operates the same as a SharePoint site.

## What is the item limit for SharePoint?

Many sites claim that SharePoint has a 5,000-item limit. This is not true. The SharePoint 5,000-item limit applies to how many items appear in a search list view: a maximum of 5,000.

SharePoint sites do have file size and number limits, which are covered in detail here: [SharePoint limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits).

Some list view options may prevent search list views with more than 5,000 items from appearing.

## How are permissions handled?

Permissions are handled in different ways depending on the source/destination connectors used.

- When migrating data from a Single User Connector, permissions will not be applied to any migrated data.
- When migrating from a non-Microsoft Administrative connector (such as G Suite or Dropbox), apply permissions at the folder level with the child folders inheriting those permissions.
- When migrating from one Office 365 tenant to another Office 365 tenant using Office 365 (OneDrive/SharePoint Admin), apply permissions at the file level.

## How many user Transfer Rows can I run at once?

At a maximum, only 50 user Transfer Rows can run simultaneously. This total includes both scanning and migrating.

If you select more than that total combined number and start scanning or migrating, only 50 randomly chosen rows will run. The rest will be in the "Queued Transfer Rows."

As a transfer row completes, another from the queue will start migrating or scanning automatically.  While 50 concurrent user transfer rows is the maximum allowed, if a migration experiences any slowdowns or back-off requests, it may drop lower than this number to keep the migration stable.

