---
title: "Remove a hub site"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 3/20/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 8b1f8b6b-09c6-41c9-b1ca-88cbeee86ba2
description: "Learn how to use PowerShell to disable the hub site feature on a site"
---

# Remove a hub site

If you're a global or SharePoint admin in Office 365, you can remove a hub site by using Microsoft PowerShell to disable the hub site feature on the hub site. Make sure you do this before you delete the hub site. When you disable the hub site feature, any sites still associated with the hub site will be automatically disassociated.
  
## 

1. Download and install the latest [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you already have a previous version installed, uninstall it first and then install the latest version.
    
2. Connect the SharePoint Online Management Shell to SharePoint Online for your organization. For info, see [Connect the SharePoint Online PowerShell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Run the following command:
    
  ```
  Unregister-SPOHubSite URL
  ```

    (Where  *URL*  is the URL of the site.) 
    

