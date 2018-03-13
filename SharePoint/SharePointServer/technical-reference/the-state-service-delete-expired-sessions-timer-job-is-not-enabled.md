---
title: "The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)"
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
ms.assetid: 17d06bdf-69e1-4a85-86f9-da78a3c79952
description: "Summary: Learn how to resolve the SharePoint Health Analyzer ruleThe State Service Delete Expired Sessions timer job is not enabled, for SharePoint Server 2016 and SharePoint 2013."
---

# The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The State Service Delete Expired Sessions timer job is not enabled", for SharePoint Server 2016 and SharePoint 2013. 
  
 **Rule Name:** The State Service Delete Expired Sessions timer job is not enabled. 
  
 **Summary:** The State Service uses a timer job to delete data for expired sessions from the State Service databases. If this timer job is not enabled, the server that hosts the State Service database will run out of disk space and the SharePoint farm will cease to function 
  
 **Cause:** The State Service Delete Expired Sessions timer job is not enabled. 
  
 **Resolution: Enable the timer job by using the SharePoint Central Administration website**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
    > [!NOTE]
    > The timer job settings are farm-wide and cannot be set for individual servers in the farm. 
  
2. Start Central Administration.
    
3. In Central Administration, click **Monitoring**.
    
4. On the Monitoring page, in the **Timer Jobs** section, click **Review job definitions**.
    
5. On the Job Definitions page, click the State Service Delete Expired Sessions timer job.
    
6. On the Edit Timer Job page, specify the schedule that you want, and then click **Enable**.
    
 **Resolution: Enable the timer job by using Microsoft PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPTimerJob StateServiceExpiredSessionJobDefinition
  ```

For more information, see [Enable-SPTimerJob](http://technet.microsoft.com/library/https://technet.microsoft.com/en-us/library/ff607892%28v=office.16%29.aspx.aspx). We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  

