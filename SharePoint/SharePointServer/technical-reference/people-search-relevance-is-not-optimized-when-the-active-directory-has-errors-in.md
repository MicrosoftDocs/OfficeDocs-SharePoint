---
title: "People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server)"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 12/5/2017
ms.audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 982d3ab2-d1a6-4625-b4c6-e12a1f4532d5
description: "Summary: Learn how to resolve the SharePoint Health Analyzer rulePeople Search relevance is not optimized when the Active Directory has errors in the manager reporting structure, for SharePoint Server 2016 and SharePoint 2013."
---

# People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure (SharePoint Server)

 **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "People Search relevance is not optimized when the Active Directory has errors in the manager reporting structure", for SharePoint Server 2016 and SharePoint 2013. 
  
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
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](http://technet.microsoft.com/library/2ddfad84-7ca8-409e-878b-d09cb35ed4aa.aspx). 
  
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  $upaProxy = Get-SPServiceApplicationProxy <AppID>
  ```

    where  *\<AppID\>*  is the GUID of the User Profile service application proxy. For more information, see [Get-SPProfileLeader](http://technet.microsoft.com/library/604f034f-f2bb-4bc3-a32d-66128a908360.aspx).
    
4. Type the following command:
    
  ```
  Add-SPProfileLeader -ProfileServiceApplicationProxy $upaProxy -Name "<Domain\UserName> "
  ```

    where  *\<Domain\UserName\>*  is the user account that you want to add as a leader — for example, Contoso\Joe.Healy. For more information, see [Add-SPProfileLeader](http://technet.microsoft.com/library/99675c8e-b164-4229-9b8f-eebfda5d5adb.aspx).
    
5. You are prompted to confirm. Type **Y** to confirm. 
    
6. Run a full crawl on the content source that contains the start address (URL) of the User Profile application.
    
Repeat the commands to add more user accounts as company leaders.
  
## See also

#### Other Resources

[Add-SPProfileLeader](http://technet.microsoft.com/library/99675c8e-b164-4229-9b8f-eebfda5d5adb.aspx)

