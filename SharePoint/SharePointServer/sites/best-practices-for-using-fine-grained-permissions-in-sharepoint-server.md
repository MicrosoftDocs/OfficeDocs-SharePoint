---
title: "Best practices for using fine-grained permissions in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/27/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 86ffc7e1-293e-4ca9-8235-4480307f4210
description: "Learn about best practices for fine-grained permissions and how to use them within your organization when you use SharePoint Server."
---

# Best practices for using fine-grained permissions in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Fine-grained permissions can influence security on a SharePoint farm. Potential performance issues can occur when you use fine-grained permissions. The following information helps you address issues when an environment is experiencing issues that incorrect use or scale of fine-grained permissions might have caused.
  
You can avoid fine-grained permissions by doing the following:
  
- Break permission inheritance as infrequently as possible.
    
- Use groups based on folder membership to assign permissions.
    
- Due to a change in SharePoint Server search continuous crawl capabilities that now include security information, we no longer recommend that you avoid using SharePoint groups to manage dynamic user and group memberships. Prior to SharePoint Server, using dynamic memberships in SharePoint groups could cause search results to not show up correctly for all members until a full crawl occurred after the membership change. Now with the continuous crawl capability including security information a dynamic membership or other security change will be picked up sooner (default value is 15 minutes) and be used by search query result trimming.
    
- Assign permissions at the highest possible level. As part of this strategy, consider the following techniques:
    
  - Put documents that require fine-grained permissions in document libraries that are defined to support each group of permissions Keep the document libraries in a separate site collection or site.
    
  - Use different document publish levels to control access. Before a document is published, the advanced permissions and versioning settings can be set for users who can only approve items in the document library. 
    
  - For non-document libraries (lists), use the **ReadSecurity** and **WriteSecurity** permission levels. When a list is created, the owners can set the Item-level permissions to either Read access or Create and Edit access. 
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
- [Fine-grained permission reference for SharePoint Server](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server)
    
- [Troubleshoot common fine-grained permissions issues for SharePoint Server](/SharePoint/administration/troubleshoot-common-fine-grained-permissions-issues)
    
## Best practices to avoid common limit issues of fine-grained permissions
<a name="avoidcommonfgpissues"> </a>

If your business requirement must use fine-grained permissions, consider the following recommended best practices:
  
- Ensure that you do not have too many items at the same level of hierarchy in the document libraries, because the time that is required to process items in the views increases.
    
- Use event handlers to control edit permission. You can have an event handler that registers an event using the **SPEventReceiverType.ItemUpdating** and **SPEventReceiverType.ItemUpdated** methods, and then use code to control whether the update should be allowed. This is very powerful, because you can make security decisions based on any metadata of a list or item, without affecting the view-rendering performance. 
    
- Use the **AddToCurrentScopeOnly** method to assign Limited Access membership in a SharePoint group. The key element in this principle is to redesign the architecture so that scope membership does not cause Access Control List (ACL) recalculation at the parent document library and web. For additional information about scope changes, Issue 3: Use fine-grained permissions by scope structure changes (2010 only). 
    
When working with fine-grained permissions, it is easy to unintentionally encounter limits that prevent permissions from resolving. This section describes some of these limits and best practices on how to set them to allow permissions to resolve correctly.
  
### Too many scopes in a list
<a name="toomanyscopesinalist"> </a>

There is a built-in limit of 50,000 scopes per list or document library. After 50,000 scopes are reached addition of new scopes in a given list or document library is prohibited.
  
 **Best practices:**
  
- Only set unique scopes on parent objects such as folders.
    
- Do not create a system with many uniquely-permissioned objects below an object that has many scopes.
    
- If your business requires more than 50,000 uniquely permissioned items in a list or document library, then you must move some items to a different list or document library.
    
### Change the built-in scope limit
<a name="changebuiltinscope"> </a>

Change the built-in scope limit by using a Microsoft PowerShell script.
  
 **To change the built-in scope limit by using Windows PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  - Add memberships that are required beyond the minimums above.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Start the **SharePoint Management Shell**. 
    
3. At the PowerShell command prompt, type the following command:
    
   ```
   $webapp = Get-SPWebApplication http://<serverName>
   $webapp.MaxUniquePermScopesPerList
   $webapp.MaxUniquePermScopesPerList = <Number of scope limit>
   ```

   Where:
    
   - Where  _\<serverName\>_ is the name of the application server in the SharePoint farm. 
    
   - Where  _\<Number of scope limit\>_ is the maximum number of unique permissions scopes that you want to allow per SharePoint list. Often, the effective limit is much smaller than 50,000 if many scopes exist at the same hierarchical level. This is because display checks for items below that hierarchical level must be checked against all scopes above them. This limitation can cause the effective number of scopes allowed in a particular query to be reduced to 1,000 to 2,000. 
    
> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### Too many members in a permission scope
<a name="toomanymembersinapermscope"> </a>

As described earlier, a binary ACL is calculated when the membership of the associated permission scope changes. This includes when a new limited access member is added. As the scope membership number increases, the time that is required to recalculate the binary ACL increases.
  
The problem can be made worse as the addition of users at a child object's unique scope will cause its parent scopes to be updated with the new Limited Access members, even if this ultimately results in no change to the parent scope membership. When this occurs, the binary ACL for the parent scopes must also be recalculated, at the expense of more processing time, even if it ultimately results in the same ACL.
  
 **Best practice:**
  
Rely on group membership instead of individual user membership in permission scopes. For example, if a single group can be used instead of 1,000 individual users, the scope will be 999 membership entries smaller for the permission scope and any of its parent scopes. Also, the single group will be updated with Limited Access rights instead of updating each user who has Limited Access rights. This also helps increase the speed of Limited Access rights push and ACL recalculation on the parent scope objects. 
  
> [!IMPORTANT]
> Using a SharePoint group will cause a full crawl of the index. If possible, use a domain group. 
  
### Very deep scope hierarchy
<a name="verydeepscopehierarchy"> </a>

As indicated earlier, the hierarchical depth of permission scopes can affect the work that is required to add Limited Access users to parent scopes. The larger the number of unique scopes above an item, up to and including the uniquely permissioned web, the larger the number of additions that must occur. If a scope hierarchy is very deep, a scope membership change can take a very long time to occur, as each membership change in the deepest scope item will have to iteratively update parent scopes with a membership addition for the explicitly added user or group that has Limited Access rights. Additionally this will increase the number of binary ACLs that have to be recalculated, with an according performance effect.
  
 **Best practice:**
  
Reduce the numbers of uniquely permissioned parent objects. This reduces the number of scopes that have to be updated with Limited Access members when any child object's scope changes.
  

