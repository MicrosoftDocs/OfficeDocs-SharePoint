---
title: "Configure hybrid federated search from SharePoint Online to SharePoint Server - roadmap"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/21/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
localization_priority: Priority
ms.custom: 
ms.assetid: f6d49e94-ad29-456d-8cd9-f940154d5a0e
description: "Learn how to configure hybrid federated search from SharePoint Server to SharePoint Online."
---

# Configure hybrid federated search from SharePoint Online to SharePoint Server - roadmap

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)] 
  
This article provides the roadmap for configuring hybrid search from SharePoint Online in Office 365 for enterprises to SharePoint Server, which allows your users to use see search results from SharePoint Server when searching from Office 365.
  
Follow these steps in the order shown. If you already completed a step when you did a different roadmap, skip that step and go to the next.
  
|**Step**|**Description**|
|:-----|:-----|
|**1. [Configure Office 365 for SharePoint hybrid](configure-office-365-for-sharepoint-hybrid.md)** <br/> |Configure your Office 365 tenant for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts.  <br/> |
|**2. [Set up SharePoint services for hybrid environments](set-up-sharepoint-services-for-hybrid-environments.md)** <br/> |Configure the needed SharePoint services for hybrid search, including User Profiles, MySites, and the Application Management service.  <br/> |
|**3. [Configure server-to-server authentication from SharePoint Server to SharePoint Online](configure-server-to-server-authentication.md)** <br/> |Configure server-to-server authentication between SharePoint Server and Office 365.  <br/> |
|**4. Synchronize user profiles** <br/> |Run SharePoint user profile synchronization to update the SharePoint User Profile Store with the new account UPNs that you added when you configured Office 365. For information about how to run profile sync, see [Manage user profile synchronization in SharePoint Server](../administration/manage-profile-synchronization.md).  <br/> |
|**5. [Configure inbound connectivity](configure-inbound-connectivity.md)** <br/> |Configure authentication from Office 365 to SharePoint Server.  <br/> |
|**6. [Configure a reverse proxy device for SharePoint Server hybrid](configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md)** <br/> |Configure a reverse proxy device for your on-premises environment.  <br/> |
|**7. [Display hybrid federated search results in SharePoint Online](display-hybrid-federated-search-results-in-sharepoint-online.md)** <br/> |Configure your search service application to display search results from SharePoint Server in Office 365.  <br/> |
   
## See also

#### Concepts

[Plan SharePoint Server hybrid](plan-sharepoint-server-hybrid.md)

