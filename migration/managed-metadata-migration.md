---
title: "Migrating Managed Metadata"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
description: "Migrating Managed Metadata "
---

# Migrating Managed Metadata to SharePoint Online Using the SPMT

The SharePoint Migration Tool (SPMT) lets you migrate managed metadata from SharePoint Server 2013 to SharePoint in Office 365.

### What is supported

Currently, only the migration of the default site collection term store is supported. This is the term store which contains the site collection group. 

You should have only one default site collection term store in SharePoint Managed Metadata Services. If more than one term store is marked as the default, the SharePoint Migration Tool (SPMT) will not be able to determine which term store to migrate.

### Troubleshooting

If your managed metadata column list and library is not migrating correctly when using SPMT:

* Confirm that the SPO account you are using for migration has been added to the term store admin.
* Confirm that you have a Managed Metadata Service connected to the web application. If not, create one.
* Verify that only one term store in connected to the web application and only one term store is set to *This is the default storage location for column specific term sets*. Uncheck any others.




#### To configure a managed metadata service connection

1. In SharePoint Server 2013 Central Administration, under Application Management, click **Manage service applications**.
2. Find the managed metadata service connection for the service application that you want to configure. (Look for Managed Metadata Service Connection in the Type column.)
3. Highlight that row, and then click Properties.
4. Set the default site collection term store by selecting **This is the default storage location for column specific term sets**.</br>

 ![Default site collection term store](media/managed-metadata-issue1.png)

To learn more:</br></br>
 [Configure the SharePoint Server Managed Metadata service](https://docs.microsoft.com/en-us/SharePoint/governance/configure-the-managed-metadata-service).
 
[Overview, including download links to SPMT](https://docs.microsoft.com/en-us/sharepointmigration/introducing-the-sharepoint-migration-tool)



