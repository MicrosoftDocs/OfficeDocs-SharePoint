---
title: "Create a user-mapping file for Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
ms.date: 08/12/2020
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- M365-collaboration
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
search.appverid: MET150
description: "Create a user-mapping file for data content migration when using Migration Manager"
---

# Create a user-mapping file for data content migration in Migration Manager

This article shows how to create a user-mapping file to use with Migration Manager.
  
Migration Manager migrates your files from on-premises file shares and move them to Microsoft 365.
  
  
## Create a user-mapping file for data content migration

A default user-mapping file is used when migrating your data from a local file share or an on-premises SharePoint Server document library. You can also create your own using the following guidelines. Use any text editor, or an application like Excel, to create the CSV file.
  
 **CSV file format**


> [!IMPORTANT]
> Do not include a header row in your CSV file. 
  
  
The following example uses Excel to create the CSV file.
  
1. Start Excel.
    
2. Enter the values for your user-mapping.
    
  - **Column A:** From the source location, enter the **log in name of the user**.  *Required.* 
    
  - **Column B:** On the destination site, enter the **principal username**.  *Required.* 
    
  - **Column C:** If the principal username on the destination site is an Active Directory (AD) group, enter **TRUE**. If it's not an AD group, enter **FALSE**.  *Required.* 
    
3. Close and save as a comma-delimited (\*.csv) file.
    
 **Upload your user-mapping file to Migration Manager**
  
After you create your own user-mapping file, upload it to the SharePoint Migration tool.
  
1. Go to the [Migration Manager page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

2. Select **Global settings**.

3. Select **All settings**.

4. Select **User mapping file**, and then select **Choose file** to browse to the file to use.

5. Select **Save**.

>[!Note]
> It is not possible to map an AD group to a SharePoint group in the destination site.
