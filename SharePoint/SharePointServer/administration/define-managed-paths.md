---
title: "Define managed paths in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 0f95a1e6-7044-487e-8681-b1d717caabb3
description: "Learn how to add a managed path for a web application in SharePoint Server."
---

# Define managed paths in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can specify the paths in the URL namespace of a web application to use for site collections. This is known as a managed path. You can specify that one or more site collections exist at a specified path.
  
There are two types of managed paths that you can create:
  
- A wildcard inclusion allows you to append multiple site collections to the path that you specify. For example, if you add /engineering as a wildcard inclusion off of your root site of http://contoso, then you'll be able to create multiple site collections off of http://contoso/engineering. 
    
- An explicit inclusion allows you to create a single site collection with the specified address. For example, if you add /finance as an explicit inclusion off of your root site of http://contoso, then you'll be able to create a single site collection with the address http://contoso/finance. 
    
Note that the root of a web application is automatically included as an explicit inclusion. Changing the root to a wildcard inclusion is not supported.
  
## Define managed paths for a web application by using Central Administration
<a name="section1"> </a>

Use the procedures that are described here to add or delete managed paths for a web application by using Central Administration.
  
 **To add a managed path by using Central Administration**
  
1. Verify that the user account that is performing this task is a member of the Farm Administrators SharePoint group.
    
2. On the SharePoint Central Administration website, click **Application Management**.
    
3. On the **Application Management** page, click **Manage web applications**.
    
4. Click the web application for which you want to manage paths.
    
    The ribbon becomes active.
    
5. In the **Manage** group of the ribbon, click **Managed Paths**.
    
6. On the **Define Managed Paths** page, in the **Add a New Path** section, type the path to include. 
    
7. Click **Check URL** to confirm that the path does not already exist. 
    
8. In the **Type** list, select either **Wildcard inclusion** or **Explicit inclusion** to identify the type of path. 
    
    The **Wildcard inclusion** type includes all paths that are subordinate to the specified path. The **Explicit inclusion** type includes only the site that is indicated by the specified path. Sites subordinate to the specified path are not included. 
    
9. Click **Add Path**.
    
10. When you have finished adding paths, click **OK**.
    
 **To remove a managed path by using Central Administration**
  
1. Verify that the user account that is performing this task is a member of the Farm Administrators SharePoint group.
    
2. On the SharePoint Central Administration website, click **Application Management**.
    
3. On the **Application Management** page, click **Manage web applications**.
    
4. Click the web application for which you want to manage paths. The ribbon becomes active.
    
5. In the **Manage** group of the ribbon, click **Managed Paths**.
    
6. On the **Define Managed Paths** page, in the **Included Paths** section, click the check box next to the path that you want to remove. 
    
7. Click **Delete selected paths**.
    
    > [!CAUTION]
    > Be sure that you want to remove the selected path before you perform this action. You'll have no additional opportunity to confirm. Deletion is immediate. 
  
8. After you are finished removing paths, click **OK**.
    
## See also
<a name="section1"> </a>

#### Other Resources

[New-SPManagedPath](/powershell/module/sharepoint-server/New-SPManagedPath?view=sharepoint-ps)
  
[Get-SPManagedPath](/powershell/module/sharepoint-server/Get-SPManagedPath?view=sharepoint-ps)
  
[Remove-SPManagedPath](/powershell/module/sharepoint-server/Remove-SPManagedPath?view=sharepoint-ps)

