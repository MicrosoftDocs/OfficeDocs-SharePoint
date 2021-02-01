---
title: "SharePoint Migration Tool for SharePoint and OneDrive"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
description: "Overview of the SharePoint Migration Tool and resources for download and support."
---

# Download and install the SharePoint Migration Tool

You can use the SharePoint Migration Tool (SPMT) for migrations ranging from the smallest set of files to a large-scale enterprise migration. It lets you bring your information to the cloud and take advantage of the latest collaboration, intelligence, and security solutions in Microsoft 365.

SPMT supports migration to SharePoint and OneDrive from:

- SharePoint Server 2016
- SharePoint Server 2013
- SharePoint Foundation 2013
- SharePoint Server 2010
- SharePoint Foundation 2010
- Network and local file shares

>[!Note]
>Learn more about how to migrate your file shares with [Migration Manager](mm-get-started.md).

## Current and pre-release versions

Use on of the following links to download SPMT:
- [Public preview](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)
- [First release](https://aka.ms/spmt-ga-page)
- [General availability](https://aka.ms/spmt-ga-page)

After you download and install SPMT, read [How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md) to get started.

If you experience installation issues, see [Troubleshooting installation issues](spmt-install-issues.md).

## Supported features

For a complete description of features, see [What does SPMT support?](what-is-supported-SPMT.md) 

If you prefer to use PowerShell, all SPMT functionality is supported. See [Migrate to SharePoint using PowerShell](overview-spmt-ps-cmdlets.md).

## Planning and assessment

Planning is the key to successful data migration.  The *SharePoint Migration Assessment Tool* (SMAT) is a simple command-line executable that scans your SharePoint Server 2013 farm to help identify potential issues with data you plan to migrate to SharePoint in Microsoft 365. The results report points you to articles to help fix any issues that are discovered. The tool runs in the background and doesn't affect your production environment.
  
To download the tool, go to [SharePoint Migration Assessment Tool (SMAT)](https://www.microsoft.com/download/details.aspx?id=53598&amp;751be11f-ede8-5a0c-058c-2ee190a24fa6=True)
  
>[!NOTE]
>The *SharePoint Migration Tool* is not available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud using the data trustee, *German Telekom*. However, it is supported for users in Germany whose data location is not in the German datacenter.

## Related articles

[What does SPMT support?](what-is-supported-SPMT.md)

[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md)
  
[How to format your JSON or CSV for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user-mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint and OneDrive migration speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint provided Azure containers and queues for SharePoint Migration API](sharepoint-online-provided-azure-containers-and-queues-for-spo-migration-api.md)
  