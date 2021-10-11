---
title: "Update a web application URL and IIS bindings for SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: v-bshilpa
author: Benny-54
manager: serdars
ms.date: 
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 
description: "Learn how to change a web application bindings for SharePoint Server."
---

# Update a web application URL and IIS bindings for SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

In previous versions of SharePoint, it was difficult to change the IIS bindings of your SharePoint web application once it was created. You could try to remove a web application from a zone and then re-extend it to the zone with updated bindings, but this was a time consuming operation and risked potentially losing customizations in that IIS web site. Or you could manually edit the bindings of the IIS web site itself, but SharePoint would be unaware of such manual changes, so you risked SharePoint overwriting those bindings at any time. 

You can now easily change the SharePoint web application IIS bindings in place through PowerShell or Central Administration.

> [!NOTE]
> This functionality is available only to those users who are a member of the local Administrator's group on the server.
 
This article provides detailed guidance for changing the IIS bindings of a web application.

## Editing a web application bindings through Central Administration 

To edit the web application and set the port, URL, SSL certificate host header, do the following:

 1. To edit the web application, navigate to **SharePoint** > **WEB APPLICATIONS** and click **Edit**.
 
    ![Select-edit](../media/extend-exit.PNG)
    
 2. In **Edit a Web Application Zone** dialog box, click **Default**.
 
    ![edit-web-application-part1](../media/edit2.PNG)
    
 3. In **IIS Web site** section, you can change the port and host header.
 
 4. In **Security Configuration** section, you can **Use Secure Sockets Layer (SSL)**, **Server Certificate** and **Use Server Name Indication**.
     
  5. In **Public URL** section, you can change the URL.
  
  6. Click **Save** to save the changes.
    
     ![edit-web-application-part2](../media/edit3.PNG)

## Editing a web application bindings through Central Administration 

To edit the web application with new bindings through PowerShell, use `Set-SPWebApplication` cmdlet. This functionality is supported in all web application zones. 

For example, you can run the following PowerShell command to change a SharePoint web application on HTTP port 80 to instead use a host header binding on SSL port 443: 

 ```PowerShell
 Set-SPWebApplication -Identity http://servername -Zone Default -Port 443 -SecureSocketsLayer -HostHeader sharepoint.contoso.com -Url https://sharepoint.contoso.com 
 ```
 
 

