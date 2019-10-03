---
title: "Create a Search Center site in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: bd9db767-6b87-450d-a8e6-9dc684d59ae4
description: "Learn how to create a Search Center site and grant site access to users in SharePoint Server."
---

# Create a Search Center site in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A Search Center site, or Search Center, provides a classic interface for users to submit search queries and view search results. A Search Center site is the top-level site of a site collection that a farm administrator creates by using the Enterprise Search Center template or Basic Search Center template.
  
## Before you begin
<a name="begin"> </a>

Depending on the kind of installation that you performed and the site collection template that you selected at that time, the farm might already have a Search Center site. To check this, browse to the top-level site for the site collection that you created during installation. In either case, you can create a Search Center site and grant users access to it by using the procedures in this article.
  

    

<a name="begin"> </a>

 **To create a SharePoint Search Center site**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the home page of the Central Administration website, in the **Application Management** section, click **Create site collections**.
    
3. On the Create Site Collection page, do the following:
    
  - In the **Web Application** section, select a web application to contain the new site collection. To use a web application other than the one that is displayed, click the web application that is displayed, and then click **Change Web Application**.
    
  - In the **Title and Description** section, in the **Title** box, type the name for the new Search Center site. Optionally, type a description in the **Description** box. 
    
  - In the **Web Site Address** section, for the part of the URL immediately after the web application address, select **/sites/**, or select a managed path that was previously defined, and then type the final part of the URL.
    
    Note the address of the new Search Center for future reference.
    
  - In the **Template Selection** section, in the **Select a template** subsection, click the **Enterprise** tab, and select the **Enterprise Search Center** template. 
    
  - In the **Primary Site Collection Administrator** section, in the **User name** box, type the user name of the primary site collection administrator for this site collection in the form  _domain\user name_.
    
  - (Optional) In the **Secondary Site Collection Administrator** section, type the user name of a secondary site collection administrator in the form  _domain\user name_.
    
  - In the **Quota Template** section, select **No Quota**.
    
    A Search Center site is not intended to be a data repository. Therefore, you do not have to select a quota template.
    
  - Click **OK**.
    
4. On the Top-Level Site Successfully Created page, click the link to the Search Center site that you created.
    
After you create the Search Center site, you must grant site access to users so that they can perform search queries and view search results. Use the following procedure to grant site access to users.
  
 **To grant access to the SharePoint Search Center**
  
1. Verify that the user account that is performing this procedure is a member of the Owners group on the Search Center site.
    
2. In a web browser, go to the Search Center site.
    
3. Open the **Site** menu by clicking the gear icon in the upper-right portion of the page, and then click **Shared with**.
    
4. In the **Shared With** dialog box, click **Invite people**.
    
5. In the **Share \<SearchCenterName\>** dialog box, in the **Enter users separated with semicolons** text box, type the names of the Windows user groups and Windows users to whom you want to grant permissions for submitting queries and viewing search results in the Search Center. 
    
    For example, to grant access to the Search Center to all Windows users, type NT Authority\authenticated users.
    
6. Click **Show options**.
    
7. Clear the **Send an email invitation** check box. 
    
8. In the **Select a group or permission level** drop-down list, select **\<SearchCenterName\> Visitors [Read]**.
    
9. Click **Share**.
    
## Related Topics
<a name="begin"> </a>

[Create and configure a Search service application in SharePoint Server 2016](create-and-configure-a-search-service-application.md)
  
[Manage the Search Center in SharePoint Server](manage-the-search-center-in-sharepoint-server.md)
  

