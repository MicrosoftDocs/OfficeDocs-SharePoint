---
ms.date: 12/01/2023
title: "Migrate to Microsoft 365"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: conceptual
ms.service: microsoft-365-migration
ms.localizationpriority: null
search.appverid: MET150
msCollection: 
- SPMigration
- M365-collaboration
- m365solution-migratetom365
- m365solution-overview
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
- intro-overview
- intro-get-started
description: "This article helps you understand which tool to use when migrating content to SharePoint and OneDrive in Microsoft 365."
---

# Migrate your content to Microsoft 365

Moving to Microsoft 365? **Migration Manager** helps you migrate your content easily and securely.

### Announcing the new Migration Admin role

>[!Note]
>This feature is currently in public preview, with full availability by mid-January 2024.

A new Microsoft 365 Migration Administrator role has been created to provide access to Migration Manager within the Microsoft 365 Admin Center. Currently, companies must assign their migration team the SharePoint admin role, giving them more access than needed. With this new role you can limit usage to only what is required to migrate your content, keeping more comprehensive access to only those who need it.

>[!Important]
>This role doesn't allow access to Migration Manager from the SharePoint admin center. Continue to use the SharePoint Administrator role to migrate from network file shares.

In addition, this role provides all the functionality required to migrate including the ability to:

- Access Migration Manager to migrate from Google Drive, Dropbox, Box and Egnyte
- Select migration sources, create migration inventories (such as Google Drive user lists), schedule and execute migrations, and download reports
- Create new SharePoint sites if the destination sites don't already exist, create SharePoint lists under the SharePoint admin sites, and create and update items in SharePoint lists
- Manage migration project settings and migration lifecycle for tasks
- Manage permission mappings from source to destination

To use this feature, you must create a new user in the Microsoft 365 admin center, then assign them the Migration Administrator role. This role allows access to only to Migration Manager.

TYou can continue to use Migration Manager as you currently do today.  Your projects will continue to work normally.


## What's new

- What's new and coming soon to [Migration Manager](mm-whats-new.md).

- What's new and coming soon to [SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md)

#### Mover retirement

**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte is fully integrated into Migration Manager. All FastTrack-led migrations have transitioned to Migration Manager. Migration Manager doesn't support the migration of Amazon S3 or Azure blob storage.

**Individuals or students**: You can continue to use Mover. Learn more: [Move your school files when you graduate](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)


### Cross-tenant migration

Tenant to tenant migration for OneDrive is now available outside of Migration Manager.  To learn more:

- [**Cross-tenant OneDrive migration**](/microsoft-365/enterprise/cross-tenant-onedrive-migration)  

A cross tenant migration solution for SharePoint is currently in private preview.  To learn more, see:

-  [**How to participate in the Cross-tenant SharePoint migration preview**](/microsoft-365/enterprise/cross-tenant-sharepoint-migration)

### Transform your classic SharePoint Server pages

If you're onboarding your classic on-premises SharePoint Server pages to SharePoint Online, help is here!  Learn more at:  [**Transform classic pages to modern pages**](/sharepoint/dev/transform/modernize-userinterface-site-pages)


##  Where are you migrating from?

|Migrate from|Description|
|:-----|:-----|
|![Get started **Box**](/office/media/icons/get-started-blue.png)</br> [**BOX**](mm-box-overview.md)|Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started File share](/office/media/icons/get-started-blue.png) </br> [**FILE SHARES**](mm-get-started.md)|With a centralized way of connecting servers, creating tasks, and managing your migration tasks, migrate your file shares to Microsoft 365.|
|![Get started Google Workspace](/office/media/icons/get-started-blue.png) </br> [**GOOGLE WORKSPACE**](mm-google-overview.md)|Migrate your Google Drives to Microsoft 365. |
|![Get started Dropbox](/office/media/icons/get-started-blue.png) </br> [**DROPBOX**](mm-dropbox-overview.md)|Collaborate all in one place by migrating your Dropbox documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started SharePoint Server](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER**](introducing-the-sharepoint-migration-tool.md)|Migrate your SharePoint Server sites and content to take advantage of the latest collaboration, intelligence, and security solutions in Microsoft 365. SharePoint Server 2010, 2013, and 2016 environments only.|
|![Get started SharePoint Server workflows](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER WORKFLOWS**](spmt-workflow-overview.md)|Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. With SPMT, you can migrate your **SharePoint Server 2010** out of the box (OOTB) approval and collect feedback workflows to PowerAutomate, List and library "out-of-box" (OOTB) approval workflows, and Workflow definitions and associations.|
|![Get started classic SharePoint Server pages](/office/media/icons/get-started-blue.png)</br>[**SHAREPOINT SERVER CLASSIC PAGES**](/sharepoint/dev/transform/modernize-userinterface-site-pages)|Are you onboarding your classic on-premises SharePoint Server content to SharePoint Online? Here's how: [Transform classic pages to modern pages](/sharepoint/dev/transform/modernize-userinterface-site-pages)|


## Other resources

- **Cross-tenant OneDrive migration**. During mergers or divestitures, you commonly need the ability to move your users OneDrive accounts into a new Microsoft 365 tenant. With Cross-tenant OneDrive migration, tenant administrators can use PowerShell to transition users into their new organization. To learn more, see [**Cross-tenant OneDrive migration**](/microsoft-365/enterprise/cross-tenant-onedrive-migration)</br>

- **Microsoft FastTrack**.  Microsoft FastTrack services can help you get started with your migration to the cloud.|When you need assistance to help you get started on your migration project.</br>

- **Azure Data Box**. Want to remove the dependency on your WAN link to transfer data?  The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy TBs of data from your servers to the device, ship it back to Microsoft, and your data is copied into Azure. Once your data is in Azure, use SPMT to migrate content to SharePoint. To learn more, see [Migrate using the Azure Data Box](how-to-migrate-file-share-content-to-SPO-using-AzureDataBox.md).</br>

- **OneDrive sync app**  To migrate users' Windows known folders (Desktop, Documents, Pictures, Screenshots, and Camera Roll) to OneDrive, you can use [Known Folder Move](/onedrive/redirect-known-folders). If users want to move other files from their local computer or a network file share to OneDrive or SharePoint, it's often easiest for them to use the OneDrive sync app. Users drag their files or folders to a folder they're syncing.  

>[!Note]
>When you migrate your content to Microsoft 365, you are copying the files.  Your source files are not deleted.

