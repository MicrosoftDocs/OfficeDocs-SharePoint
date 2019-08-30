---
title: "InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server)"
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
ms.assetid: 8de5bc7f-026c-4685-a6f6-a8fd814c2b70
description: "Learn how to resolve the SharePoint Health Analyzer rule: InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured."
---

# InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Rule Name:** InfoPath Forms Services forms cannot be filled out in a Web browser because no State Service connection is configured. 
  
 **Summary:** InfoPath Forms Services depends on the Web application having a service connection to a State Service Proxy to store data across HTTP requests. Without a service connection, users cannot successfully open or fill browser-enabled InfoPath forms. 
  
 **Cause:** No service connection for the State Service is configured for the Web application that is in the Health Analyzer alert. 
  
 **Resolution: Configure a service connection by using the SharePoint Central Administration website**
  
1. Verify that the user account performing this procedure is a member of the Farm Administrators group.
    
2. If a State Service already exists, you must associated the State Service with the Web application mentioned tin the health analyzer rule.
    
3. In Central Administration, under **Application Management**, click ** Manage web applications **.
    
4. On the Web Applications page, click the Web application for which you want to configure a service connection, and then click **Service Connections** on the ribbon. 
    
5. In the **Configure Service Application Associations** dialog box, ensure that the **State Service** check box is selected, and then click **OK**.
    
**Create a new State Service application by using Microsoft PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint 2013 Products cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  New-SPStateServiceDatabase -Name "State Service Database" | New-SPStateServiceApplication -Name "StateServiceApp1" | New-SPStateServiceApplicationProxy -DefaultProxyGroup
  ```

For more information, see [New-SPStateServiceApplication](/powershell/module/sharepoint-server/New-SPStateServiceApplication?view=sharepoint-ps).
    

