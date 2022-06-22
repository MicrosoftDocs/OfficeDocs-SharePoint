---
title: 
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
ms.custom: intro-get-started
search.appverid: MET150
description: 
---

# 


	Hybrid
	Performance / network
	systems requirements


### Hybrid

If you currently use OneDrive or MySites in SharePoint Server on-premises, we highly recommend deploying hybrid OneDrive. With hybrid OneDrive, users are redirected from their on-premises OneDrive to OneDrive in Microsoft 365. Hybrid OneDrive allows for seamless navigation to OneDrive in the cloud from both SharePoint on-premises and Microsoft 365.

When you deploy hybrid OneDrive, the OneDrive links in the SharePoint Server ribbon and app launcher will point to OneDrive in Microsoft 365. If your users have files in on-premises OneDrive, they may have trouble accessing them unless they've bookmarked the old URL. It's important to have a migration plan for these files before you deploy hybrid OneDrive. For migration options, see [Migrating data](#migrating-data) later in this article.

If you don't use OneDrive in SharePoint Server, but you do have an on-premises SharePoint environment, you may still want to consider deploying hybrid OneDrive. Doing so will update the OneDrive navigation links in SharePoint Server to point to OneDrive in Microsoft 365 – again, giving your users seamless navigation to OneDrive in the cloud from either location.

For more info about how to configure OneDrive in a hybrid scenario and how it works, see [Plan hybrid OneDrive](/sharepoint/hybrid/plan-hybrid-onedrive-for-business/).

SharePoint hybrid has a variety of features to create a seamless experience when using both SharePoint Server and SharePoint. If you're planning to configure hybrid OneDrive, consider including other SharePoint hybrid features for a better overall user experience. For more info, see [Explore SharePoint Server hybrid](/sharepoint/hybrid/explore-sharepoint-server-hybrid/).

After you've migrated your users' files from on-premises OneDrive and configured hybrid OneDrive, to save disk space, you can reduce the quota for your on-premises OneDrive top-level site collection to a minimal value.

Key decisions:

- Do you want to deploy hybrid OneDrive?

- Do your users have OneDrive on-premises data that needs to be migrated to OneDrive in Microsoft 365?




[Hybrid for SharePoint Server](/sharepoint/hybrid/hybrid)

[SharePoint hybrid sites and search](/sharepoint/hybrid/sharepoint-hybrid-sites-and-search)

### Network utilization

Various factors can impact the amount of network bandwidth used by OneDrive. For the best experience, we recommend that you assess this impact before doing a full OneDrive deployment across your organization. The article [Network utilization planning for the OneDrive sync app](network-utilization-planning.md) includes the recommended process for determining your network bandwidth needs for OneDrive. Be sure to include this as part of your deployment plan

[Networking roadmap for Microsoft 365](/microsoft-365/enterprise/networking-roadmap-microsoft-365)

[Office 365 URLs and IP address ranges](/enterprise/urls-and-ip-address-ranges)

[Use the Office 365 Content Delivery Network (CDN) with SharePoint Online](/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo)
