---
title: "Manage a paused Search service application in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 18b1dbaf-d8e1-416b-b2fb-fe6cd0a369f1
description: "Learn why the Search service application is paused and what you can do to resume it in SharePoint Server."
---

# Manage a paused Search service application in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Most operations that require the Search service application to be paused have to complete before the Search service application automatically resumes.
  
We'll show you how you can find out if and why the Search service application is paused. There are many reasons why the Search service application can be paused -- we'll list only the most common situations.
  
 **To manage a paused search service application**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. Start a SharePoint Management Shell on one of the servers in the farm.
    
3. At the Microsoft PowerShell command prompt, type the following command(s) to find out if the Search service application is paused.
    
  ```
  $ssa.IsPaused() -ne 0
  ```

If this command returns **False**, the Search service application is running.
    
If this command returns **True**, the Search service application is paused. Go to step 4 to find out why, and what action you should take.
    
4. At the Microsoft PowerShell command prompt, type the following command(s) until you find the reason why the Search service application is paused.
    
|              **Command**              | **If the command returns True, the Search service application is paused for this reason:** |                                                                                                                                    **Action**                                                                                                                                    |
| :------------------------------------ | :----------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `($ssa.IsPaused() -band 0x01) -ne 0`  | A change in the number of crawl components or crawl databases is in progress.              | Wait until the topology change completes.                                                                                                                                                                                                                                        |
| `($ssa.IsPaused() -band 0x02) -ne 0`  | A backup or restore procedure is in progress.                                              | Wait until the backup or restore completes. After the procedure completes, run the command  `$ssa.ForceResume(0x02)` to verify. For more information, see [Restore Search service applications in SharePoint Server](../administration/restore-a-search-service-application.md). |
| `($ssa.IsPaused() -band 0x04) -ne 0`  | A backup of the Volume Shadow Copy Service (VSS) is in progress.                           | Wait until the backup completes. After the VSS backup completes, run the command  `$ssa.ForceResume(0x02)` to verify.                                                                                                                                                            |
| `($ssa.IsPaused() -band 0x08) -ne 0`  | One or more servers in the search topology that host query components are offline.         | Wait until the servers are available again.                                                                                                                                                                                                                                      |
| `($ssa.IsPaused() -band 0x20) -ne 0`  | One or more crawl databases in the search topology are being rebalanced.                   | Wait until the operation completes.                                                                                                                                                                                                                                              |
| `($ssa.IsPaused() -band 0x40) -ne 0`  | One or more link databases in the search topology are being rebalanced.                    | Wait until the operation completes.                                                                                                                                                                                                                                              |
| `($ssa.IsPaused() -band 0x80) -ne 0`  | An administrator has manually paused the Search service application.                       | If you know the reason, you can resume the Search service application. Run the command  `$ssa.resume()` to resume the Search service application.  <br/><br/>If you don't know the reason, find out why someone has manually paused the Search service application.                        |
| `($ssa.IsPaused() -band 0x100) -ne 0` | The search index is being deleted.                                                         | Wait until the search index is deleted.                                                                                                                                                                                                                                          |
| `($ssa.IsPaused() -band 0x200) -ne 0` | The search index is being repartitioned.                                                   | Wait until the operation completes. For more information, see [Manage the index component in SharePoint Server](manage-the-index-component.md).                                                                                                                                  |
   
After you've waited until the operation completes, at the Microsoft PowerShell command prompt, type the following command to make sure that the Search service application is running:
  
```
$ssa.IsPaused() -ne 0
```

If this command returns **False**, the Search service application is running.
  
If this command returns **True**, the Search service application is paused. Re-run the commands from step 4 to find out why.
  
**Resume a paused Search service application in SharePoint Server**

To resume a paused Search service application, use the following PowerShell.

```
$ssa = Get-SPEnterpriseSearchServiceApplication -Identity MySSA
$ssa | Resume-SPEnterpriseSearchServiceApplication
