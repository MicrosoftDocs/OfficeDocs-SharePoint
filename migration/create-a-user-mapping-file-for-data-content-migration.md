---
title: "Create a user-mapping file for data content migration"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
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
description: "Create a user-mapping file to use for data content migration via the SharePoint Migration Tool."
---

# Create a user-mapping file for data content migration

This article shows how to create a user-mapping file to use with the SharePoint Migration Tool (SPMT).

SPMT enables you to migrate your files from SharePoint on-premises document libraries or on-premises file shares to Microsoft 365. The tool is free for Microsoft 365 users.

> [!NOTE]
> The SharePoint Migration Tool isn't currently available for users of Office 365 operated by 21Vianet in China.

You can use the default user-mapping file when you migrate data from a local file share or on-premises SharePoint Server document library. Or, you can create your own mapping file by using the following guidelines. Use any text editor, or an application like Microsoft Excel, to create this CSV file.

## CSV file format

> [!IMPORTANT]
> For **SharePoint Server 2010** migrations, only the log-in name is supported in column A.
>
> For **SharePoint Server 2013 and later**, you can use either the log-in name or the SID in column A.

For all SharePoint Server versions:

![Screen shows a user-mapping file for data content migration.](media/spmt-user-mapping.png)

Only SharePoint Server 2013 and 2016 can use this format, in addition to using a log-in name:

![Screen shows a sample user-mapping file for SharePoint Server 2013 and 2016.](media/spmt-user-mapping-2013.png)

> [!IMPORTANT]
> Don't include a header row in your CSV file.

**To create a user-mapping file for data migration**

The following example uses Excel to create the CSV file.

1. Start Excel.

2. Enter the values for your user-mapping.
    
   - *Column A:* From the source location, enter the **log-in name of the user**. *Required.* 
    
   - *Column B:* On the target site, enter the **user principal name (UPN)**. *Required.* 
    
   - *Column C:* If the user principal name on the target site is an Active Directory (AD) group, enter **TRUE**. If it's not an AD group, enter **FALSE**.  *Required.* 
    
3. Close and save as a comma-delimited (\*.csv) file.

## Upload your user-mapping file to SharePoint Migration Tool

After you create your own user-mapping file, upload it to the SharePoint Migration tool.

1. Start SPMT. Enter your Microsoft 365 user name and password, and then select **Sign in**.

2. Select **Start your first Migration**.

3. Select your migration type.

4. Enter your source information, and then select **Next**.

5. Enter your destination information, and then select **Next**.

6. Review your migration details, and then select **Next**.

7. On the **Choose your settings** page, expand **View all settings**.

8. Under **Users** in the **User-mapping** box, select **Choose file**, and select your user-mapping file.

9. Select **Save**.

> [!Important]
> SPMT only migrates default SharePoint groups.
>
> You can't map an AD group to a SharePoint group in the target site. You can't use SPMT to map a SharePoint Server group to a SharePoint group.
