---
title: "People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server)"
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
ms.assetid: 982d3ab2-d1a6-4625-b4c6-e12a1f4532d5
description: "Learn how to resolve the SharePoint Health Analyzer rule: People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure, for SharePoint Server."
---

# People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
>[!IMPORTANT]
>This health analyzer rule only applies to SharePoint 2010 as this was removed in [KB4011601](https://support.microsoft.com/help/4011601) for SharePoint Server 2013 and [KB4011576](https://support.microsoft.com/help/4011576) for SharePoint Server 2016.

 **Rule Name:** People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure. 
  
 **Summary:** In Active Directory Domain Services (AD DS), only company leaders should have the **Manager** property set to NULL. If the **Manager** property is set to NULL for other users, people search relevance is reduced. To optimize people search relevance, explicitly specify company leaders. People search can then use this information to improve relevance. 
  
 **Cause:** Company leaders have not been explicitly specified. 
  
 **Resolution: Specify company leaders.**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the Microsoft PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  $upaProxy = Get-SPServiceApplicationProxy <AppID>
  ```

    where  *\<AppID\>*  is the GUID of the User Profile service application proxy. For more information, see [Get-SPProfileLeader](/powershell/module/sharepoint-server/Get-SPProfileLeader?view=sharepoint-ps).
    
4. Type the following command:
    
  ```
  Add-SPProfileLeader -ProfileServiceApplicationProxy $upaProxy -Name "<Domain\UserName> "
  ```

    where  *\<Domain\UserName\>*  is the user account that you want to add as a leader — for example, Contoso\Joe.Healy. For more information, see [Add-SPProfileLeader](/powershell/module/sharepoint-server/Add-SPProfileLeader?view=sharepoint-ps).
    
5. You are prompted to confirm. Type **Y** to confirm. 
    
6. Run a full crawl on the content source that contains the start address (URL) of the User Profile application.
    
Repeat the commands to add more user accounts as company leaders.
  
## See also

#### Other Resources

[Add-SPProfileLeader](/powershell/module/sharepoint-server/Add-SPProfileLeader?view=sharepoint-ps)

