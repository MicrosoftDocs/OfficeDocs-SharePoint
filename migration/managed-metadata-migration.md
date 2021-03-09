---
title: "Migrate managed metadata by using SPMT"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
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
description: "Migrating-managed metadata by using SPMT."
---

# Migrate managed metadata to SharePoint by using SPMT

The SharePoint Migration Tool (SPMT) enables you to migrate managed metadata from SharePoint Server 2013 to SharePoint in Microsoft 365.

## What's supported

The SharePoint Migration Tool supports having only one Managed Metadata Service (MMS) term store *set as the default* for the site collection.

> [!NOTE]
> If more than one site collection term store is marked as the default, the SharePoint Migration Tool can't determine which term store to migrate. This uncertainty can break managed metadata columns that refer to the term store content.

## Troubleshooting

**Symptom:**  Your Managed Metadata Service (MMS) term store and its content (term groups/terms sets/terms) doesn't migrate.  

**Likely cause:** More than one term store is set as the default.

**Action:**  
- To migrate a Managed Metadata Service (MMS) term store, set it as the default. 
- If you have more than one MMS term store, decide which one you want to migrate and set it as the default. Remove the default setting from all others.

### To configure a managed metadata service connection

1. On the **SharePoint Server 2013 Central Administration** website, under **Application Management**, select **Manage service applications**.
2. Find the managed metadata service connection for the service application that you want to configure. (In the **Type** column, look for **Managed Metadata Service Connection**.)
3. Highlight that row, and then select **Properties**.
4. To set the default site collection term store, select **This is the default storage location for column specific term sets**.
</br></br>
 ![Default site collection term store](media/managed-metadata-issue1.png)

To learn more, see:</br></br>
 [Configure the SharePoint Server Managed Metadata service](https://docs.microsoft.com/SharePoint/governance/configure-the-managed-metadata-service).
 
[Download and install the SharePoint Migration Tool](https://docs.microsoft.com/sharepointmigration/introducing-the-sharepoint-migration-tool)
