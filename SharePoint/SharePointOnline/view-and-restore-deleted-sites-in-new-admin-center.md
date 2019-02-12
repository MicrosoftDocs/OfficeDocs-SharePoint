---
title: "View and restore deleted sites in the new SharePoint admin center"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 3bde21ee-fb76-431a-98f6-24f97b58f233
description: "Learn about viewing and restoring sites on the Recycle bin page of the new SharePoint admin center."
---

# View and restore deleted sites in the new SharePoint admin center

Deleted sites are retained for 93 days. After 93 days, sites and all their content and settings are permanently deleted, including lists, libraries, pages, and any subsites.
  
> [!NOTE]
> If you need to retain content for a minimum period of time to comply with industry regulations or internal policies, you can create a retention policy to keep a copy of it in the Preservation Hold library. For info, see [Overview of retention policies](/office365/securitycompliance/retention-policies). 
  
To view deleted sites in the new SharePoint admin center, go to the classic SharePoint admin center, select "Try it now" in the upper right, and then select **Deleted sites** in the left pane. 
  
![Deleted sites in the new SharePoint admin center](media/b195b8c7-ee2b-4a02-92cb-ed61899edd24.png)

You can sort and filter deleted sites the same way you sort and filter sites on the Active sites page. You can also sort and filter deleted sites by Time deleted.
  
## Restore a deleted site

The new SharePoint admin center now enables both global admins and SharePoint admins to delete and restore sites that belong to an Office 365 group.

1. Select the site. 
    
2. Select **Restore**. (If you don't see the Restore button, make sure only one site is selected. The button won't appear if multiple sites are selected.)
 
> [!NOTE]
> Restoring a site that belongs to an Office 365 group restores the Office 365 group and all its resources. Note that the other group resources are retained for only 30 days, whereas the site is retained for 93. If the other group resources have been deleted, you can use the PowerShell command [Remove-SPODeletedSite](/powershell/module/sharepoint-online/remove-spodeletedsite) to permanently delete the site.   
    
For more info about the new SharePoint admin center, see [Get started with the new SharePoint admin center](get-started-new-admin-center.md).
  

