---
title: "Change your SharePoint domain name"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 2/21/2018
ms.audience: Admin
ms.topic: troubleshooting
f1_keywords:
- 'SPOTADNS'
- 'O365M_DomainsWizAdd_SPOUseMultiServices'
- 'O365M_DomainsProp_SPO'
- 'O365E_DomainsWizAdd_SPOUseMultiServices'
- 'O365E_DomainsProp_SPO'
- 'O365E_DomainsMain_PublicWebsite'
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MOE150
- MED150
- MBS150
- BCS160
- MET150
ms.assetid: 576325ad-8c40-4fe8-8a63-68c3b7d536cf
description: "Learn what you need to do to switch to a new domain name for SharePoint Online"
---

# Change your SharePoint domain name

Unfortunately, it isn't possible to change the SharePoint Online domain name for your organization in Office 365. For example, if the name of your organization changes from "Contoso" to "Fourth Coffee," you can't change  *contoso.sharepoint.com*  to  *fourthcoffee.sharepoint.com*. 
  
To use the domain name  *fourthcoffee.sharepoint.com*  , you would need to purchase a new Office 365 subscription and move all email, files, and any other data you want to keep to the new subscription. 
  
> [!NOTE]
> To change the name of a site, for example, from  *https://contoso.sharepoint.com/sites/sample1*  to  *https://contoso.sharepoint.com/sites/sample2*, you need to leverage the PowerShell commandlet Start-SPOSiteRename. Details can be found here: https://docs.microsoft.com/en-us/powershell/module/sharepoint-online/start-spositerename?view=sharepoint-ps 
  

