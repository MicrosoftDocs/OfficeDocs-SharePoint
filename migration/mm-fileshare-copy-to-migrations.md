---
title: "Step 3: Copy to migrations for file share migration"
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
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario 
- M365-collaboration
- SPMigration
search.appverid: MET150to the migration list in Migration Manager."
---

# Step 3: Copy to migrations

After a file share has been scanned and determined ready, add it to your migration list.  

1. Highlight one or rows from the scanned list. From the menu bar, select **Copy to migrations**.

2. Add a destination -- OneDrive, SharePoint or Teams. Select **Next**.

![File share scan list](/media/mm-fileshare-scan-list.png)

3.  Select a SharePoint site destination.  Enter the site path and the location within the site from the dropdown list. Select **Next**.

![Select a destination for your file share](/media/mm-fileshare-copy-migrattions-destinations.png)

![Select a sharepoint site destination](/media/mm-fileshare-copy-migrations-destination-path.png)


5. Under configure settings, enter a friendly name for your migration.
6. Select if you want to run the task now or later. If you select **Run later**, select a date and time.
7. Select an agent group and then review and edit your settings as needed.
8. Select **Schedule.**

![Configure settings for your file share migration](/media/mm-fileshare-copy-migrations-configure-settings.png)


>[!NOTE]
>Migration Manager for file shares isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. 
>
>It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.