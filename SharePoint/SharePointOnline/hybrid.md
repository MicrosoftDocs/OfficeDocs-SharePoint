---
title: Hybrid OneDrive and SharePoint in Microsoft 365
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
description: Learn about setting up hybrid OneDrive and SharePoint in Microsoft 365.
---

# Hybrid OneDrive and SharePoint in Microsoft 365

If you use SharePoint Server on-premises, there are several options for integrating that environment with SharePoint in Microsoft 365 to provide your users with a more seamless environment when navigating back and forth between the two. You can configure these options to improve your users' experience during a migration from on-premises to the cloud, or you can use them in the long term if you plan to continue using SharePoint Server.

If you have a SharePoint Server environment, we recommend setting up SharePoint Server hybrid as part of your SharePoint and OneDrive in Microsoft 365 rollout. For complete details on setting up SharePoint and OneDrive hybrid, see [Hybrid for SharePoint Server](/sharepoint/hybrid/hybrid) and [Explore SharePoint Server hybrid](/sharepoint/hybrid/explore-sharepoint-server-hybrid/).

### Hybrid features

The following hybrid features are available for integrating SharePoint Server with Microsoft 365:

- **OneDrive** - OneDrive links are provided in SharePoint Server which direct users to OneDrive in Microsoft 365.

- **Site following** - Followed sites from both locations are consolidated in the SharePoint in Microsoft 365 followed sites list. 

- **Profiles** - Profiles exist in both locations, but SharePoint Server links to users' profiles redirect to profiles in Microsoft 365.

- **Extensible app launcher** - The SharePoint Server app launcher includes several tiles that link to Microsoft 365.

- **Hybrid self-service site creation** - Users going to the default SharePoint Server site creation page are redirected to the Microsoft 365 Groups creation page, allowing them to create sites in SharePoint in Microsoft 365.

- **Search** - Cloud hybrid search crawls on-premises content and indexes it in the search index in Microsoft 365. Users can search the Microsoft 365 index from either location.

- **Taxonomy and content types** - Enables you to have a single taxonomy and content types list that spans SharePoint Server and SharePoint in Microsoft 365. See [Plan hybrid SharePoint in Microsoft 365 taxonomy and hybrid content types](/sharepoint/hybrid/plan-hybrid-sharepoint-taxonomy-and-hybrid-content-types) for more information.

See [SharePoint hybrid sites and search](/sharepoint/hybrid/sharepoint-hybrid-sites-and-search) for more details on these options.

### Hybrid OneDrive

If you currently use OneDrive or MySites in SharePoint Server, we highly recommend deploying hybrid OneDrive. With hybrid OneDrive, users are redirected from their on-premises OneDrive to OneDrive in Microsoft 365. Hybrid OneDrive allows for seamless navigation to OneDrive in the cloud from both SharePoint Server and Microsoft 365.

When you deploy hybrid OneDrive, the OneDrive links in the SharePoint Server ribbon and app launcher will point to OneDrive in Microsoft 365.

If you don't use OneDrive in SharePoint Server, but you do have an on-premises SharePoint environment, you may still want to consider deploying hybrid OneDrive. Doing so will update the OneDrive navigation links in SharePoint Server to point to OneDrive in Microsoft 365 – again, giving your users seamless navigation to OneDrive in the cloud from either location.

> [!IMPORTANT]
> If your users have files in on-premises OneDrive, they may have trouble accessing them unless they've bookmarked the old URL. It's important to have a migration plan for these files before you deploy hybrid OneDrive.

For more info about how to configure OneDrive in a hybrid scenario and how it works, see [Plan hybrid OneDrive](/sharepoint/hybrid/plan-hybrid-onedrive-for-business/).

## Next steps

> [!div class="nextstepaction"]
> [Plan file sync](plan-file-sync.md)

## Related topics

[Plan for SharePoint and OneDrive in Microsoft 365](plan-for-sharepoint-onedrive.md)
