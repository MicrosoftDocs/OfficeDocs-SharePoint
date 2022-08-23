---
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
ms.custom:
- seo-marvel-apr2020
- intro-overview
- intro-get-started
description: "This article helps you understand which tool to use when migrating content to SharePoint and OneDrive in Microsoft 365."
---

# Migrate your content to Microsoft 365

Moving to Microsoft 365? Let us help you migrate your content easily and securely.

## Mover retirement

>[!Note]
>Attention businesses or those with EDU plans: We have retired the legacy [Mover](https://app.mover.io) tool's ability for admin-led migrations from [Google Drive](mm-google-overview.md), [Dropbox](mm-dropbox-overview.md), [Box](mm-box-overview.md), and [Egnyte](mm-egnyte-overview.md). Please use [Migration Manager](https://aka.ms/ODSP-MM), located in the SharePoint admin center.
>
>*Ongoing migrations are not impacted by this change. However, you cannot create new connectors.* If you are currently in the middle of a Mover migration, you may continue using Mover until you finish your migration using your existing connectors.
>
>[**Individuals or students**: You may continue to use Mover, learn how!](https://support.microsoft.com/en-us/office/move-your-school-files-when-you-graduate-7dbda93c-71e6-483f-8914-ad445554cd31)
>
>[Learn more about the Mover.io retirement timeline](mover-retirement-timeline.md)

>[!Important]
>**Attention FastTrack led customers:** Any FastTrack-led customer with multi-parent folders who has reached velocity migrations will NOT transition to Migration Manager.
>
>All other inflight content migration FastTrack-led customers will transition to Migration Manager. FastTrack completed their analysis of those customers who will remain on Mover due to a technical limitation of how multi-parent folders (a now deprecated Google feature) work.



## What's new

- Check out what's new and coming soon to [Migration Manager](mm-whats-new.md).

- Check out what's new and coming soon to [SharePoint Migration Tool (SPMT)](new-and-improved-features-in-the-sharepoint-migration-tool.md)


## We're listening!

Help us improve Migration Manager by sending your suggestions and reporting bugs you encounter. Just select the feedback button at the bottom of the page and filter on "Migration".  

##  Where are you migrating from?

|Migrate from|Description|
|:-----|:-----|
|![Get started **Box**](/office/media/icons/get-started-blue.png)</br> [**BOX**](mm-box-overview.md)|Collaborate all in one place by migrating your Box documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started File share](/office/media/icons/get-started-blue.png) </br> [**FILE SHARES**](mm-get-started.md)|With a centralized way of connecting servers, creating tasks, and managing your migration tasks, migrate your file shares to Microsoft 365.|
|![Get started Google Workspace](/office/media/icons/get-started-blue.png) </br> [**GOOGLE WORKSPACE**](mm-google-overview.md)|Migrate your Google Drives to Microsoft 365. |
|![Get started Dropbox](/office/media/icons/get-started-blue.png) </br> [**DROPBOX**](mm-dropbox-overview.md)|Collaborate all in one place by migrating your Dropbox documents, data, and users to OneDrive, SharePoint, and Teams in Microsoft 365. |
|![Get started SharePoint Server](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER**](introducing-the-sharepoint-migration-tool.md)|Migrate your SharePoint Server sites and content to take advantage of the latest collaboration, intelligence, and security solutions in Microsoft 365. SharePoint Server 2010, 2013, and 2016 environments only.|
|![Get started SharePoint Server workflows](/office/media/icons/get-started-blue.png)</br>  [**SHAREPOINT SERVER WORKFLOWS**](spmt-workflow-overview.md)|Microsoft removed **SharePoint Server 2010** workflow services from existing tenants on November 1, 2020. We recommend that you move your classic SharePoint Server workflows to Power Automate flows. With SPMT, you can migrate your **SharePoint Server 2010** out of the box (OOTB) approval and collect feedback workflows to PowerAutomate, List and library "out-of-box" (OOTB) approval workflows, and Workflow definitions and associations.|



## Other resources


- **Microsoft FastTrack**.  Microsoft FastTrack services can help you get started with your migration to the cloud.|When you need assistance to help you get started on your migration project.</br>

- **Azure Data Box**. Want to remove the dependency on your WAN link to transfer data?  The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy TBs of data from your servers to the device, ship it back to Microsoft, and your data is copied into Azure. Once your data is in Azure, use SPMT to migrate content to SharePoint. To learn more, see [Migrate using the Azure Data Box](how-to-migrate-file-share-content-to-SPO-using-AzureDataBox.md).</br>

- **OneDrive sync app**  To migrate users' Windows known folders (Desktop, Documents, Pictures, Screenshots, and Camera Roll) to OneDrive, you can use [Known Folder Move](/onedrive/redirect-known-folders). If users want to move other files from their local computer or a network file share to OneDrive or SharePoint, it's often easiest for them to use the OneDrive sync app. Users drag their files or folders to a folder they're syncing.  

>[!Note]
>When you migrate your content to Microsoft 365, you are copying the files.  Your source files are not deleted.
