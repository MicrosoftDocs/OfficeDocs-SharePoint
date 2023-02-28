---
ms.date: 03/13/2018
title: "SharePoint Migration Tool for SharePoint and OneDrive"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
- m365solution-scenario
- highpri
ms.custom:
- seo-marvel-apr2020
description: "Overview of the SharePoint Migration Tool and resources for download and support."
---

# Overview of the SharePoint Migration Tool (SPMT)

The SharePoint Migration Tool (SPMT) is a free and easy to use migration solution to help you migrate content from on-premises SharePoint sites to Microsoft 365.

Migrate your SharePoint Server sites and content to take advantage of the latest collaboration, intelligence, and security solutions in Microsoft 365. The modern experience features in Microsoft SharePoint are designed to be compelling, flexible, and performant.

SPMT supports migration to SharePoint, OneDrive, and Teams from:

- SharePoint Server 2010, 2013, 2016, and 2019
- SharePoint Foundation 2010 and 2013
- 
SPMT also supports the migration of workflows from:

- SharePoint Server 2010 out-of-the-box workflows (OOTB)
- SharePoint Designer 2010 & 2013 workflows

For a complete description of features, see [What does SPMT support?](what-is-supported-SPMT.md) 

All SPMT functionality is also supported in PowerShell, if you prefer to use that method. See [Migrate to SharePoint using PowerShell](overview-spmt-ps-cmdlets.md).

### Supported authentication methods

SPMT supports NTLM, Kerberos, Forms, ADFS, multifactor authentication, SAML-based claims, and Client certificate authentication.

> [!IMPORTANT]
> If the on-premises server is configured to support multiple authentication providers, including Windows authentication, then Windows authentication **will not be supported**. If this describes your environment, use other authentication methods instead of Windows authentication. 

## Planning and assessment

Planning is the key to successful data migration. The *SharePoint Migration Assessment Tool* (SMAT) is a simple command-line tool that scans your SharePoint Server 2013 farm to help identify potential issues with the data that you plan to migrate to SharePoint in Microsoft 365. The results report points to articles to help fix any issues that are discovered. The tool runs in the background and doesn't affect your production environment.
  
To download the tool, go to [SharePoint Migration Assessment Tool (SMAT)](https://www.microsoft.com/download/details.aspx?id=53598&amp;751be11f-ede8-5a0c-058c-2ee190a24fa6=True)
  
>[!NOTE]
>The *SharePoint Migration Tool* isn't available for users of Office 365 operated by 21Vianet in China.

## Get started

To get started:

Make sure that you have:

- **Access to the destination**: You must either be a global admin or OneDrive/SharePoint admin. 
- **Access to the source**: SharePoint credentials that have read access to the SharePoint Server content you plan to migrate.
- **Prerequisites installed:** Make sure you have the necessary prerequisites installed.

#### [Step 1: Install SPMT](how-to-use-the-sharepoint-migration-tool.md)
#### [Step 2: Create a migration task](spmt-create-task.md)
#### [Step 3: Monitor and report](using-the-sharepoint-migration-tool-reports.md)



## Related articles

[What does SPMT support?](what-is-supported-SPMT.md)

[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to use the SharePoint Migration Tool](how-to-use-the-sharepoint-migration-tool.md)
  
[How to format your JSON or CSV for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user-mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint and OneDrive migration speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint provided Azure containers and queues for SharePoint Migration API](sharepoint-online-provided-azure-containers-and-queues-for-spo-migration-api.md)
  
