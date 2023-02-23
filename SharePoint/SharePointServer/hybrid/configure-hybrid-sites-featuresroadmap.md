---
ms.date: 03/13/2018
title: "Configure hybrid sites features - roadmap"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 4bd426f4-105c-41cf-a4b8-815db62191ce
description: "Learn how to configure hybrid sites features for SharePoint in Microsoft 365 hybrid with Microsoft 365."
---

# Configure hybrid sites features - roadmap

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)]
  
This article provides a roadmap for configuring [hybrid sites features](sharepoint-hybrid-sites-and-search.md#SitesFeatures). Follow these steps in the order shown. If you already completed a step when you followed a different roadmap, skip that step, and go to the next one.
  
|**Step**|**Description**|
|:-----|:-----|
|1. [Configure Microsoft 365 for SharePoint in Microsoft 365 hybrid](configure-office-365-for-sharepoint-hybrid.md) <br/> |Configure your Microsoft 365 for enterprises organization for a hybrid environment, including registering your domain, configuring UPN suffixes, and synchronizing your user accounts.  <br/> |
|2. [Set up SharePoint in Microsoft 365 services for hybrid environments](set-up-sharepoint-services-for-hybrid-environments.md) <br/> |Configure the needed SharePoint in Microsoft 365 services for hybrid search, including User Profiles, MySites, and the Application Management service.  <br/> |
|**3. (SharePoint Server 2013 only) [Install the September PU for SharePoint Server 2013](/officeupdates/sharepoint-updates)** <br/> |Install the September 2015 PU or higher for SharePoint Server 2013. (We recommend installing the latest PU.)  <br/> |
|3. [Run Hybrid Picker](run-hybrid-picker.md) <br/> |Configure hybrid sites features by running the Hybrid Picker in Microsoft 365.  <br/> |
|4. Quick test  <br/> | Check to make sure hybrid sites features are working:  <br/>  Log in to a SharePoint Server as a regular user. (Be sure you're a member of the correct audience if you used audiences.)  <br/>  Select the Follow link at the top of the page.  <br/>  You should see a small pop-up under **Follow** letting you know that you're following the site. Select this pop-up and note that it navigates to your personal site, and the list of sites you're following in SharePoint in Microsoft 365.  <br/> |
   
## The extensible hybrid app launcher

The app launcher is included as part of SharePoint Server 2016. If you want to add it to SharePoint Server 2013, open the SharePoint 2013 Management Shell and run the following cmdlet:
  
```
install-SPFeature SuiteNav
```

For each site collection where you want to use the feature, run the following cmdlet:
  
```
Enable-SPFeature suitenav -url <SiteCollectionURL>
```

## Video demonstration

This video shows a walkthrough of configuring sites features.
  
**Video: Configure hybrid sites features**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/9097e969-aff1-479b-bcbf-3fc963051465?autoplay=false]

## See also

#### Concepts

[Hardware and software requirements for SharePoint in Microsoft 365 hybrid](hardware-and-software-requirements-for-sharepoint-hybrid.md)
  
[Accounts needed for hybrid configuration and testing](accounts-needed-for-hybrid-configuration-and-testing.md)


