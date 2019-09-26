---
title: "Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/31/2017
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 086fd0f5-8580-414f-a088-b1238ad02014
description: "Learn how to resolve the SharePoint Health Analyzer rule: Verify each User Profile Service Application has an associated Search Service Connection, for SharePoint Server."
---

# Verify each User Profile Service Application has an associated Search Service Connection (SharePoint Server)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
 **Summary:** The User Profile service presents URLs to end users in some Web Part and tag profile pages. These URLs are trimmed for security to make sure that users do not see URLs to which they do not have permissions. The User Profile service uses the Search service to perform this security trimming. If there is no Search service associated with the User Profile service application, security trimming does not work, and URLs are visible to everyone. Although users are denied access when they click a URL for which they do not have permissions, they nonetheless can see the URL in the search results. 
  
 **Cause:** A Search service connection is not included in the group of connections for the User Profile service application. 
  
 **Resolution: Edit the group of connections for the User Profile service application.**
  
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
2. On the SharePoint Central Administration website, click **Application Management**.
    
3. On the Application Management page, in the **Service Applications** section, click **Configure service application associations**.
    
4. On the Service Application Associations page, in the **View** list, click **Service Applications**.
    
5. In the **Web Application/Service Application** column, click the User Profile service application for which you want to edit connections. 
    
6. In the **Configure Service Application Associations** dialog box, select the **Search Service** check box, or select **Default** in the **Edit the following group of connections** list, and then click **OK**. By default, all connections are included.
    

