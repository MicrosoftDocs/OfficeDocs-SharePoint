---
title: "Create a site collection in SharePoint Server"
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
ms.assetid: a5c66813-3523-40d1-99d8-86e8359b6c73
description: "How to create a SharePoint Server site collection in an existing web application."
---

# Create a site collection in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
A site collection is a grouping of websites under a common top-level site that have the same owner and share administration settings, for example, permissions. When you create a site collection, a top-level site is automatically created in the site collection. You can then create one or more subsites below the top-level site. For info about creating site collections in SharePoint Online, see [Create a site collection](/sharepoint/create-site-collection).
  
    
## Before you begin
<a name="begin"> </a>

Before you create a site collection, ensure that the following prerequisites are available:
  
- A web application in which to create the site collection.
    
- A quota template, if you plan to define values that specify how much data can be stored in a site collection and the storage size that triggers an email alert to the site collection administrator. For more information, see [Create, edit, and delete quota templates in SharePoint Server](create-edit-and-delete-quota-templates.md).
    
- A custom managed wildcard path, if you plan to create the site collection somewhere other than under the root (/) directory or the /sites/ directory. For more information, see [Define managed paths in SharePoint Server](../administration/define-managed-paths.md).
    
## Create a site collection by using Central Administration
<a name="section1"> </a>

You typically use the SharePoint Central Administration website to create a site collection in a stand-alone deployment.
  
 **To create a site collection by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
   - To create a site collection, you must be a member of the Farm Administrators SharePoint group on the computer that is running the SharePoint Central Administration website.
    
2. Open Central Administration and in the **Application Management** section, click **Create site collections**.
    
3. On the **Create Site Collection** page, in the **Web Application** section, if the web application in which you want to create the site collection is not selected, on the **Web Application** menu, click **Change Web Application**, and then click the web application in which you want to create the site collection.
    
4. In the **Title and Description** section, type the title and description for the site collection. 
    
5. In the **Web Site Address** section, select the path to use for your URL (for example, a wildcard inclusion path such as /sites/, or the root directory (/). 
    
    If you select a wildcard inclusion path, you must also type the site name to use in your site's URL.
    
6. In the **Template Selection** section, in the **Select a template** list, choose the tab you want for the site collection ( **Collaboration**, **Enterprise**, or **Publishing**), and then select the template that you want to use for the top-level site in the site collection. You can also click the **Custom** tab to create an empty site and apply a template later. 
    
    A description for the template that you select appears below the list of templates.
    
7. In the **Primary Site Collection Administrator** section, type the user name (in the form DOMAIN\username) for the user who will be the site collection administrator. 
    
8. In the **Secondary Site Collection Administrator** section, type the user name for the secondary administrator of the site collection. 
    
    Assigning a secondary site collection administrator is a best practice to ensure that someone can manage the site collection when a primary site collection administrator is not available.
    
9. If you are using quotas to manage storage for site collections, in the **Quota Template** section, click a template in the **Select a quota template** list and then click **OK**.
    
## Create a site collection by using Microsoft PowerShell
<a name="section2"> </a>

You typically use Microsoft PowerShell to create a site collection when you want to automate the task, which is common in enterprises.
  
 **To create a site collection by using PowerShell**
  
1. Verify that you have the following memberships:
    
   - **securityadmin** fixed server role on the SQL Server instance. 
    
   - **db_owner** fixed database role on all databases that are to be updated. 
    
   - local Administrators group on the server on which you are running the PowerShell cmdlets.
    
2. Open the SharePoint Management Shell.
    
3. At the command prompt, type the following commands:
    
   ```powershell
   Get-SPWebTemplate
   ```

   ```powershell
   $template = Get-SPWebTemplate "STS#0"
   ```

   ```powershell
   New-SPSite -Url "<URL for the new site collection>" -OwnerAlias "<domain\user>" -Template $template
   ```

    This example retrieves a list of all available site templates and then creates a site collection by using the Team Site template. For more information, see [New-SPSite](/powershell/module/sharepoint-server/New-SPSite?view=sharepoint-ps) and [Get-SPWebTemplate](/powershell/module/sharepoint-server/Get-SPWebTemplate?view=sharepoint-ps).
    
    We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
    
## See also
<a name="section2"> </a>

#### Concepts

[Manage site collections in SharePoint Server](manage-site-collections.md)

