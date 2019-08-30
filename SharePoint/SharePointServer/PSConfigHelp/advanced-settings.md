---
title: "Advanced settings"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c122d39d-505d-4e74-bf25-622b22e5732d
description: "Summary: Learn how to use Active Directory creation mode in SharePoint Server."
---

# Advanced settings

 **Summary:** Learn how to use Active Directory creation mode in SharePoint Server. 
  
To create new unique user accounts automatically by using Active Directory Domain Services (AD DS), you must enable Active Directory account creation mode. 
  
Because at least one Central Administration web application is required for each server farm, the Central Administration web application is automatically installed in the first server in the server farm. Only one set of fields, for the Active Directory domain and the Active Directory organizational unit, are presented. When you run the configuration wizard on other servers in the farm, you will see the option on this screen to create the Central Administration web application.
  
If you want to create a load-balanced URL for Central Administration or to provide redundancy, you can create more than one Central Administration web site. However, in most installations this is unnecessary.
  
### To enable Active Directory account creation mode

1. On the Advanced Settings page, select **Enable Active Directory Account Creation Mode**.
    
2. In **Active Directory Domain**, type your domain name.
    
3. In **Active Directory Organizational Unit**, type your SharePoint organizational unit.
    
4. To return to the Completing the **SharePoint Products Configuration Wizard** page, click **OK**.
    
> [!CAUTION]
> If you enable this option, you might not be able to upgrade from SharePoint 2010 Products to other products. If you have trouble installing SharePoint products on this computer, run the SharePoint 2016 Products Configuration Wizard again to clear this option. 
  

