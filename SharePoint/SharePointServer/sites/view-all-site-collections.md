---
title: "View all site collections in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 37277bfe-4e25-4050-9f99-aac16b47d079
description: "How to see the list of site collections in SharePoint Server."
---

# View all site collections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
A site collection is a group of websites that have the same owner and share administrative settings, for example, permissions, and quotas. Site collections are created within a web application. When you create a site collection, a top-level site is automatically created in the site collection. You can then create one or more subsites below the top-level site. The entire structure of the top-level site and all its subsites is called a site collection.

Learn about [Managing sites in the new SharePoint admin center in Microsoft 365](../../SharePointOnline/manage-sites-in-new-admin-center.md).
  
## View the site collections in a web application

Use the following procedures to view all the site collections in a web application.
  
### To view all site collections by using Central Administration

Refer to the following table in step 3.
  
| Item | Description |
|:-----|:-----|
|URL  |The URL of the site collection.  |
|Title  |The current title for site collection.  |
|Description  |The current description for the site collection.  |
|Primary administrator  |The primary administrator for the site collection.  |
|Email address  |The email address for the primary administrator.  |
|Database name  |The content database that is used by the site collection.  |
   
1. Verify that you have the following administrative credentials:
    
    To view all site collections, you must be a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
2. Open Central Administration. On the **Application Management** page, in the **Site Collections** section, click **View all site collections**.
    
    The **Site Collection List** page lists all the site collections in the web application. 
    
3. To display more information about a site collection, in the **URL** column, click the site collection. 
    
    The table just before this procedure appears on the right side of the page.
    
4. If you want to change the selected web application, click the **Web Application** box, and then click **Change Web Application**. Use the **Select Web Application** page to select another web application. 
    
### To view all site collections by using Microsoft PowerShell

1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](../administration/manage-permissions-for-a-web-application.md).
    
2. Open **SharePoint Management Shell**.
    
3. At the PowerShell command prompt, type the following command, and then press ENTER:
    
   ```powershell
   Get-SPWebApplication | Get-SPSite -Limit All | Format-Table -Property URL,ContentDatabase
   ```

   > [!NOTE]
   > This command displays the URLs of all the web applications in a server farm and the site collections in each web application.
    
For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps&preserve-view=true) and [Get-SPSite](/powershell/module/sharepoint-server/get-spsite?view=sharepoint-ps&preserve-view=true). 

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## See also

#### Other Resources

[SharePoint planning guide](../../SharePointOnline/planning-guide.md)
