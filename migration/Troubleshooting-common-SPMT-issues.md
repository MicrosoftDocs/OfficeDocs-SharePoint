---
title: "Troubleshooting SharePoint Migration Tool"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
ms.custom: 

description: "How to troubleshoot common errors in the SharePoint Migration Tool."
---
## Troubleshooting common SPMT errors
|**Error Code**|**Error description**|**Recommendations**|
|:-----|:-----|:-----|
|0x0201000D|The list does not exist or cannot be accessed.|Check if the list exists or if you can access the list in source site and target site.|
|0x02050008|Failed to access local storage.|Do not open, edit or delete the SPMT working folder %appdata%\Microsoft\MigrationToolStorage or its contents. Restart your migration.|