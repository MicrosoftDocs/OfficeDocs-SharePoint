---
title: "Enable auto-acceleration in SharePoint"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 74985ebf-39e1-4c59-a74a-dcdfd678ef83
description: "Enable auto-acceleration to send users directly to your identity provider to sign in."
---

# Enable auto-acceleration in SharePoint

Auto-acceleration is a feature in SharePoint in which you specify the default identity provider endpoint for your organization. When a user accesses a resource, instead of signing in to login.microsoftonline.com, the user is sent directly to the identity provider (IdP). If you configured Integrated Windows Authentication on AD FS and the user's computer is domain-joined, they will have a completely seamless single sign on experience, just like accessing an on-premises resource.
  
## Requirements

To enable auto-acceleration, you must have a single identity provider (IdP). SharePoint must have a specific site to target when accelerating. Your organization can have multiple domains as long as there is a single IdP endpoint.
   
## Enable auto-acceleration

To enable auto-acceleration, you need to use Microsoft PowerShell. 
 
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a [global admin or SharePoint admin](/sharepoint/sharepoint-admin-role) in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command to enable auto-acceleration on sites that are not shared externally:

```PowerShell
Set-SPOTenant -SignInAccelerationDomain "contoso.com"
```

4. If you have configured your IdP to support guests, you can enable auto-acceleration on sites that have external sharing enabled by running:
  
```PowerShell
Set-SPOTenant -EnableGuestSignInAcceleration $true
```

> [!NOTE]
> You must run SignInAccelerationDomain before running this command. 
  
For more information, see [Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant).
  
  
## Frequently asked questions about auto-acceleration
<a name="FAQ"> </a>

### Q: What can I do to make the experience as smooth as possible for my users?

A: You can do two things. First, ensure that your internal and external sites are clearly separated. Second, encourage users to access internal sites first as part of their daily workflow. Perhaps consider creating an internal-only site that serves as a welcome page. You can also modify your Group Policy so that users will be directed to an internal home page whenever they open their browser. After the user has signed in to one site (by using either method), they will not be prompted to sign to other sites.
  
### Q: What do I need to do to take advantage of auto acceleration on externally shared sites?

A: Guests can potentially authenticate in one of three places: Azure Active Directory (if their organization is a "cloud" organization or they use a Microsoft account), the IdP of the user's organization, or your IdP (if you use an on-premises extranet solution). If you want to enable auto-acceleration for externally shared sites, your IdP needs to be capable of supporting these use cases (or at least the ones that you want your guests to use). To support guests in Azure AD, Microsoft account, or other IdPs, your IdP will need to be capable of returning the user to the Azure AD signin screen for authentication.
  

