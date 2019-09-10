---
title: "The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/5/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0d326419-25c2-4591-acc6-9e487aa80c6e
description: "Learn how to resolve the SharePoint Health Analyzer rule: The InfoPath Forms Services Maintenance timer job is not enabled, in SharePoint Server."
---

# The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** The InfoPath Forms Services Maintenance timer job is not enabled. 
  
 **Summary:** The InfoPath Forms Services Maintenance timer job is not enabled. 
  
The InfoPath Forms Services Maintenance timer job is used by InfoPath Forms Services to improve performance by caching form template data on each front-end web server.
  
 **Cause:** The timer job may have been disabled on the Job Definitions page on the SharePoint Central Administration website or the Microsoft PowerShell **Disable-SPTimerJob** cmdlet was used. 
  
 **Resolution: Enable the timer job by using the Central Administration web site**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators SharePoint group.
    
2. Start Central Administration.
    
3. On Central Administration, click **Monitoring**.
    
4. Click **Review Job definitions**.
    
5. Click **InfoPath Forms Services Maintenance**.
    
6. Click **Enable**.
    
**Resolution: Enable the timer job by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPTimerJob "<FormsMaintenanceJobDefinition>"
  ```

    Where:
    
  -  _\<FormsMaintenanceJobDefintion\>_ is the actual name of the timer job to enable. 
    
For more information, see [Enable-SPTimerJob](/powershell/module/sharepoint-server/Enable-SPTimerJob?view=sharepoint-ps).
  

