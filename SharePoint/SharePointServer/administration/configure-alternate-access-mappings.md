---
title: "Configure alternate access mappings for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/17/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: be9d31d2-b9cb-4442-bfc6-2adcdbff8fae
description: "Learn how to configure alternate access mappings in SharePoint Server."
---

# Configure alternate access mappings for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Each web application can be associated with a collection of mappings between internal and public URLs. Both internal and public URLs consist of the protocol and domain portions of the full URL (for example, https://www.fabrikam.com). A public URL is what users type to access the SharePoint site, and that URL is what appears in the links on the pages. Internal URLs are in the URL requests that are sent to the SharePoint site. Many internal URLs can be associated with a single public URL in multi-server farms (for example, when a load balancer routes requests to specific IP addresses to various servers in the load-balancing cluster).
  
Each web application supports five collections of mappings per URL. The five collections correspond to five zones (default, intranet, extranet, Internet, and custom). When the web application receives a request for an internal URL in a particular zone, links on the pages returned to the user have the public URL for that zone. For more information, see [Plan alternate access mappings for SharePoint 2013](plan-alternate-access-mappings.md).
  
## Manage alternate access mappings

1. On the SharePoint Central Administration website, click **System Settings**. 
    
2. On the **System Settings** page, in the **Farm Management** section, click **Configure alternate access mappings**.
    
For information about how to perform this procedure using a Microsoft PowerShell cmdlet, see [New-SPAlternateUrl](/powershell/module/sharepoint-server/New-SPAlternateUrl?view=sharepoint-ps).
  
## Add an internal URL

1. On the **Alternate Access Mappings** page, click **Add Internal URLs**. 
    
2. If the mapping collection that you want to change is not specified, then choose one. In the **Alternate Access Mapping Collection** section, on the **Alternate Access Mapping Collection** menu, click **Change alternate access mapping collection**. 
    
3. On the **Select an Alternate Access Mapping Collection** page, click a mapping collection. 
    
4. In the **Add internal URL** section, in the **URL protocol, host and port** box, type the new internal URL (for example, https://www.fabrikam.com). 
    
5. In the **Zone** list, click the zone for the internal URL. 
    
6. Click **Save**.
    
## Edit or delete an internal URL

> [!NOTE]
> You can't delete the last internal URL for the default zone. 
  
1. On the **Alternate Access Mappings** page, click the internal URL that you want to edit or delete. 
    
2. In the **Edit internal URL** section, change the URL in the **URL protocol, host and port** box. 
    
3. In the **Zone** list, click the zone for the internal URL. 
    
4. Do one of the following:
    
  - Click **Save** to save your changes. 
    
  - Click **Cancel** to discard your changes and return to the **Alternate Access Mappings** page. 
    
5. Click **Delete** to delete the internal URL. 
    
For information about how to perform this procedure using a Microsoft PowerShell cmdlet, see [Remove-SPAlternateUrl](/powershell/module/sharepoint-server/Remove-SPAlternateUrl?view=sharepoint-ps).
  
## Edit public URLs

> [!NOTE]
> There must always be a public URL for the default zone. 
  
1. On the **Alternate Access Mappings** page, click **Edit Public URLs**. 
    
2. If the mapping collection that you want to change is not specified, then choose one. In the **Alternate Access Mapping Collection** section, on the **Alternate Access Mapping Collection** menu, click **Change alternate access mapping collection**. 
    
3. On the **Select an Alternate Access Mapping Collection** page, click a mapping collection. 
    
4. In the **Public URLs** section, you can add new URLs or edit existing URLs in any of the following text boxes: 
    
  - **Default**
    
  - **Intranet**
    
  - **Extranet**
    
  - **Internet**
    
  - **Custom**
    
5. Click **Save**.
    
## Map to an external resource

You can also define mappings for resources outside intranet applications. To do so, you must supply a unique name, initial URL, and a zone for that URL. (The URL must be unique to the farm.)
  
1. On the **Alternate Access Mappings** page, click **Map to External Resource**. 
    
2. On the **Create External Resource Mapping** page, in the **Resource Name** box, type a unique name. 
    
3. In the **URL protocol, host and port** box, type the initial URL. 
    
4. Click **Save**.
    

