---
title: SharePoint Migration Tool download and overview
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
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
ms.custom:
- seo-marvel-apr2020
- seo-marvel-jun2020
description: Learn how to download and install the SharePoint Migration Tool, and then use the included resources to plan and complete your content migration.
---

# Download and install the SharePoint Migration Tool


Designed to be used for migrations ranging from the smallest set of files to a large scale enterprise migration, the SharePoint Migration Tool (SPMT) will let you bring your information to the cloud and take advantage of the latest collaboration, intelligence, and security solutions with Microsoft 365.

**SPMT** lets you migrate content to SharePoint and OneDrive from the following locations:

- SharePoint Server 2016 (Public Preview)
- SharePoint Server 2013
- SharePoint Foundation 2013
- SharePoint Server 2010
- SharePoint Foundation 2010
- Network and local file shares

>[!Note]
>Learn more about how to migrate your file shares with [Migration Manager](mm-get-started.md).
  
</br></br>


## Current and pre-release versions

Download and install SPMT using one of the links listed below.  


||**Public preview**|**First release**|**Rolling out**|**Full General Availability**|
|:-----|:-----|:-----|:-----|:-----|
|Last released build|[3.4.119.1](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)  |[3.2.119.0](https://aka.ms/spmt-ga-page)|[3.2.119.0](https://aka.ms/spmt-ga-page) |[3.2.118.0](https://aka.ms/spmt-ga-page)|




After downloading and installing SPMT, read [How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md) to help you get started.

If you experience issues with your installation, see [Troubleshooting installation issues](spmt-install-issues.md).



## Supported features

For a complete description of features see:  [What does SPMT support?](what-is-supported-SPMT.md) 

If you prefer using PowerShell, all SPMT functionality is supported. For more information see: [Migrate to SharePoint using PowerShell](overview-spmt-ps-cmdlets.md).



## Planning and assessment

Planning is the key to a successful data migration.  The SharePoint Migration Assessment Tool (SMAT) is a simple command line executable that will scan the contents of your SharePoint Server 2013 farm to help identify any issues with data you plan to migrate to SharePoint in Microsoft 365. The results report points you to articles to help you fix any issues that were discovered. The tool runs in the background without impacting your production environment.
  
To download the tool: [SharePoint Migration Assessment Tool (SMAT)](https://www.microsoft.com/download/details.aspx?id=53598&amp;751be11f-ede8-5a0c-058c-2ee190a24fa6=True)
  
>[!NOTE]
>The **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. It is also not available for users of Microsoft 365 with the German cloud using the data trustee, *German Telekom*. However, it is supported for users in Germany whose data location is not in the German datacenter.


## Related Topics

[What does SPMT support?](what-is-supported-SPMT.md)

[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md)
  
[How to format your JSON or CSV for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint and OneDrive migration speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint provided Azure containers and queues for SharePoint Migration API](sharepoint-online-provided-azure-containers-and-queues-for-spo-migration-api.md)
  

