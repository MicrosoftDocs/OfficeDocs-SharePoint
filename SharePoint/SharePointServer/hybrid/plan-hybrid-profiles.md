---
title: "Plan hybrid profiles"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: ec40c4af-0344-43d3-97ac-5f91282db978
description: "When you have both SharePoint Server and Office 365, by default users have a different profile in each location. This can lead to a confusing profile experience for your users. With hybrid profiles, user have a single profile in Office 365 where they can maintain all of their profile information."
---

# Plan hybrid profiles

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

When you have both SharePoint Server and Office 365, by default users have a different profile in each location. This can lead to a confusing profile experience for your users. With hybrid profiles, user have a single profile in Office 365 where they can maintain all of their profile information.
  
If Office Delve is part of your Office 365 tenant, user profiles will be integrated with Delve and users can discover information and documents and see what their teammates are working on. If you've deployed [cloud hybrid search](/SharePoint/hybrid/plan-cloud-hybrid-search-for-sharepoint), users can also find on-premises documents through Delve.
  
## Profile redirection in SharePoint hybrid deployments

Hybrid profiles redirects hybrid users to their profiles in Office 365. This ensures that hybrid users have a single place for their profile information. Hybrid profiles is available with both SharePoint Server 2013 and SharePoint Server 2016.
  
Profile redirection works as follows:
  
- Profiles for all hybrid users are in Office 365. Clicking a hybrid user's profile in SharePoint Server redirects you to their profile in Office 365 (even if you're not a hybrid user yourself).
    
- If you choose to use a SharePoint audience when you configure hybrid sites features, non-hybrid users (those not in the audience) retain their SharePoint Server profiles, and they also have profiles in Office 365 if they are licensed Office 365 users.
    
## Moving custom profile properties to Office 365
<a name="MovingProfileData"> </a>

Many enterprises have business requirements to replicate custom attributes to the SharePoint Online user profile service. Some user attributes are synchronized from Active Directory Domain Services to Azure Active Directory. You can select which attributes are replicated from Active Directory Directory Services to Azure Active Directory. However, a standard set of attributes are replicated from Azure Active Directory to the SharePoint Online user profile store in Office 365. This set of attributes cannot be customized like it can in SharePoint Server.
  
Where in SharePoint Server you might use Business Connectivity Services or Microsoft Identity Manager to import custom profile properties that are not located in Active Directory Directory Services, SharePoint Online does not support these solutions. For custom properties in SharePoint Online, a user profile bulk update API is available.
  
The bulk update process works like this:
  
1. You compile the needed profile data from SharePoint Server, your line-of-business system, or any other external system, into a JSON formatted file. 
    
2. The tool uploads the JSON file to Office 365 and queues an import process.
    
3. A timer job running in SharePoint Online checks for queued import requests and performs the import operation based on the API calls and information in the provided file.
    
For more information about the bulk update API, see [Introducing Bulk UPA Custom Profile Properties Update API for SharePoint Online](https://go.microsoft.com/fwlink/p/?LinkId=786318).
  
## Working with Delve in SharePoint hybrid deployments
<a name="MovingProfileData"> </a>

If Delve is part of your Office 365 tenant, user profiles will be integrated with Delve, otherwise you'll have standard Office 365 profiles. If you haven't used Delve before, you'll want to [learn more about it](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca) and [how to administer it](/sharepoint/delve-for-office-365-admins). Delve user profiles contain the same properties as SharePoint Online profiles and can be imported in the same manner, as described above in [Moving custom profile properties to Office 365](plan-hybrid-profiles.md#MovingProfileData).
  
## Setting up hybrid profiles
<a name="MovingProfileData"> </a>

Hybrid profiles is part of several hybrid feature bundles for SharePoint Server. For details, see [Hybrid sites features and OneDrive for Business](sharepoint-hybrid-sites-and-search.md#SitesFeatures).
  
## See also
<a name="MovingProfileData"> </a>

#### Other Resources

[About user profiles in SharePoint Online](/sharepoint/manage-user-profiles)

