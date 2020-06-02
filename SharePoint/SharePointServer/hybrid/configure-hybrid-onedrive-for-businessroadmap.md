---
title: "Configure hybrid OneDrive for Business - roadmap"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/21/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 81ea6763-c331-453b-80f7-8028c3e551f8
description: "Learn how to configure hybrid OneDrive for Business with Microsoft 365."
---

# Configure hybrid OneDrive for Business - roadmap

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
This article provides the roadmap for configuring OneDrive for Business hybrid, which allows your users to use OneDrive for Business with SharePoint Server.
  
Follow these steps in the order shown. If you already completed a step when you did a different roadmap, skip that step and go to the next.
  
|**Step**|**Description**|
|:-----|:-----|
|**1. [Configure Microsoft 365 for SharePoint hybrid](configure-office-365-for-sharepoint-hybrid.md)** <br/> |Configure your Microsoft 365 organization for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts.  <br/> |
|**2. [Set up SharePoint services for hybrid environments](set-up-sharepoint-services-for-hybrid-environments.md)** <br/> |Configure the needed SharePoint services for hybrid search, including User Profiles, MySites, and the Application Management service.  <br/> |
|**3. (SharePoint Server 2013 only)[Install Service Pack 1 for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkId=521936)** <br/> |Be sure you've installed at least Service Pack 1 on your SharePoint Server 2013 farm or the OneDrive for Business redirect option will not be available.  <br/> |
|**4. [Redirect OneDrive for Business users to Microsoft 365](configure-hybrid-onedrive-for-business.md)** <br/> |Configure hybrid OneDrive for Business in the SharePoint Central Administration website.  <br/> |
|**5. Quick test** <br/> | Check to make sure OneDrive for Business is being redirected to Microsoft 365:  <br/>  Log in to a SharePoint Server as a regular user. (Be sure you're a member of the correct audience if you used audiences.)  <br/>  Click **OneDrive** in the app launcher.  <br/>  The URL in the browser address bar should change from that of your on-premises farm, to the personal site URL of SharePoint Online.  <br/> |
   
## See also

#### Concepts

[Hardware and software requirements for SharePoint hybrid](hardware-and-software-requirements-for-sharepoint-hybrid.md)
  
[Accounts needed for hybrid configuration and testing](accounts-needed-for-hybrid-configuration-and-testing.md)

