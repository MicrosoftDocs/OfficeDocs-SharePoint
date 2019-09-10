---
title: "View all site collections in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 37277bfe-4e25-4050-9f99-aac16b47d079
description: "How to see the list of site collections in SharePoint Server."
---

# View all site collections in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A site collection is a group of websites that have the same owner and share administrative settings, for example, permissions, and quotas. Site collections are created within a web application. When you create a site collection, a top-level site is automatically created in the site collection. You can then create one or more subsites below the top-level site. The entire structure of the top-level site and all its subsites is called a site collection.
  
## View the site collections in a web application

Use the following procedures to view all the site collections in a web application.
  
### To view all site collections by using Central Administration

Refer to the following table in step 3.
  
|**Item**|**Description**|
|:-----|:-----|
|URL  <br/> |The URL of the site collection.  <br/> |
|Title  <br/> |The current title for site collection.  <br/> |
|Description  <br/> |The current description for the site collection.  <br/> |
|Primary administrator  <br/> |The primary administrator for the site collection.  <br/> |
|Email address  <br/> |The email address for the primary administrator.  <br/> |
|Database name  <br/> |The content database that is used by the site collection.  <br/> |
   
1. Verify that you have the following administrative credentials:
    
   - To view all site collections, you must be a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
2. Open Central Administration. On the **Application Management** page, in the **Site Collections** section, click **View all site collections**.
    
    The **Site Collection List** page lists all the site collections in the web application. 
    
3. To display more information about a site collection, in the **URL** column, click the site collection. 
    
    The table just before this procedure appears on the right side of the page.
    
4. If you want to change the selected web application, click the **Web Application** box, and then click **Change Web Application**. Use the **Select Web Application** page to select another web application. 
    
### To view all site collections by using Microsoft PowerShell

1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](/SharePoint/administration/manage-permissions-for-a-web-application).
    
2. Open **SharePoint Management Shell**.
    
3. At the PowerShell command prompt, type the following command, and then press ENTER:
    
   ```powershell
   Get-SPWebApplication | Get-SPSite -Limit All | Format-Table -Property URL,ContentDatabase
   ```

   > [!NOTE]
   > This command displays the URLs of all the web applications in a server farm and the site collections in each web application.
    
For more information, see [Get-SPWebApplication](/powershell/module/sharepoint-server/Get-SPWebApplication?view=sharepoint-ps) and [Get-SPSite](/powershell/module/sharepoint-server/get-spsite?view=sharepoint-ps). 

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## See also

#### Other Resources

[Manage site collections and global settings in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=845346)

