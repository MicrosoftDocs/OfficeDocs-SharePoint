---
ms.date: 08/14/2023
title: "Migrate to Microsoft 365"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: conceptual
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
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

Moving to Microsoft 365? **Migration Manager** will help you migrate your content easily and securely.


## What's new

- Check out what's new and coming soon to [Migration Manager](mm-whats-new.md).

- Check out what's new and coming soon to [SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md)

## Mover retirement

**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte is fully integrated into Migration Manager. All FastTrack-led migrations have transitioned to Migration Manager. Migration Manager does not support the migration of Amazon S3 or Azure blob storage.

>[!Tip]
>[**Individuals or students**: You may continue to use Mover. Learn how!](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)


## Cross-tenant migration

Tenant to tenant migration for OneDrive is now available outside of Migration Manager.  To learn more see:

- [**Cross-tenant OneDrive migration**](/microsoft-365/enterprise/cross-tenant-onedrive-migration)  

A cross tenant migration solution for SharePoint is currently in private preview.  To learn more, see:

-  [**How to participate in the Cross-tenant SharePoint migration preview**](/microsoft-365/enterprise/cross-tenant-sharepoint-migration)

## Transform your classic SharePoint Server pages

If you are onboarding your classic on-premises SharePoint Server pages to SharePoint Online, help is here!  Learn more at:  [**Transform classic pages to modern pages**](/sharepoint/dev/transform/modernize-userinterface-site-pages)


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

