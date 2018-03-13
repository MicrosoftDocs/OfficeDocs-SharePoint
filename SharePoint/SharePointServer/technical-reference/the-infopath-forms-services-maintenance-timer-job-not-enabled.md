---
title: "The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 12/5/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 0d326419-25c2-4591-acc6-9e487aa80c6e
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleThe InfoPath Forms Services Maintenance timer job is not enabled, in SharePoint Server 2016 and SharePoint Server 2013."
---

# The InfoPath Forms Services Maintenance timer job is not enabled (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The InfoPath Forms Services Maintenance timer job is not enabled", in SharePoint Server 2016 and SharePoint Server 2013. 
  
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
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPTimerJob "<FormsMaintenanceJobDefinition>"
  ```

    Where:
    
  -  _\<FormsMaintenanceJobDefintion\>_ is the actual name of the timer job to enable. 
    
For more information, see [Enable-SPTimerJob](http://technet.microsoft.com/library/https://technet.microsoft.com/en-us/library/ff607892%28v=office.16%29.aspx.aspx).
  

