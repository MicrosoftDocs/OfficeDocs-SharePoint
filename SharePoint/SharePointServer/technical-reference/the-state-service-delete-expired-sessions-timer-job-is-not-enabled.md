---
title: "The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)"
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
ms.assetid: 17d06bdf-69e1-4a85-86f9-da78a3c79952
description: "Learn how to resolve the SharePoint Health Analyzer rule: The State Service Delete Expired Sessions timer job is not enabled, for SharePoint Server."
---

# The State Service Delete Expired Sessions timer job is not enabled (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
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
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Enable-SPTimerJob StateServiceExpiredSessionJobDefinition
  ```

For more information, see [Enable-SPTimerJob](/powershell/module/sharepoint-server/enable-sptimerjob?view=sharepoint-ps). We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  

