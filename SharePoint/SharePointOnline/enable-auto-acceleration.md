---
title: "Enable auto-acceleration in SharePoint Online"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/20/2018
ms.audience: Admin
ms.topic: article
ms.service: o365-administration
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 74985ebf-39e1-4c59-a74a-dcdfd678ef83
description: "Use AD FS auto-acceleration to allow your users to log in by using your organization's Active Directory Federation Services (AD FS) endpoint. They can be signed in immediately, without having to enter their credentials twice."
---

# Enable auto-acceleration in SharePoint Online

SharePoint Online now supports home realm discovery when users log on by using third-party identity providers, such as Active Directory Federation Services (ADFS). This feature reduces logon prompts for users by "accelerating" the user through the Azure Active Directory home realm discovery logon page. This feature is called auto-acceleration and is applied by running a Windows PowerShell cmdlet in the SharePoint Online Management Shell.
  
Without auto-acceleration, when a user accesses a site and needs to be authenticated, they are sent to Azure Active Directory. If their company uses Azure Active Directory for identity management, the user can immediately log on. If the company uses a third-party identity provider, such as AD FS, the user must first enter their email account before being forwarded to the appropriate identity provider (IdP). The Azure Active Directory page is important when companies have more than one IdP or take advantage of guest scenarios (which require users to authenticate with other IdPs or Azure Active Directory itself).
  
This approach can be frustrating to many users. The auto-acceleration feature smooths this experience.
  
By default, only site collections that are not shared externally (i.e. external sharing is disabled) can be accelerated. When a site is shared externally, the AAD login page is usually required to direct users to an endpoint where they can authenticate. If the company has configured their IdP to authenticate guest users (e.g. an extranet add-on), then it is possible to accelerate all site collections.
  
> [!NOTE]
> The  _whr_ parameter can also be used to customize the Azure Active Directory logon page as part of the Azure Active Directory Premium package. 
  
## Before you can enable auto-acceleration

Your SharePoint Online tenant must meet the following requirements before auto-acceleration can be enabled.
  
|**Requirement**|**Reason**|
|:-----|:-----|
|There must be a single identity provider.  <br/> |SharePoint Online must have a specific site to target when accelerating. The organization can have multiple domains as long as there is a single AD FS endpoint.  <br/> |
   
## Enable auto-acceleration

To enable AD FS auto-acceleration for internal site collections, you use the  _SignInAccelerationDomain_ parameter with the Windows PowerShell cmdlet **Set-SPOTenant**. 
  
For example, to set auto-acceleration for the Contoso.com domain:
 
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
3. Run the following command:
```PowerShell
Set-SPOTenant -SignInAccelerationDomain "contoso.com"
```
4. If you have configured your IdP to support guest users, you can accelerate sites with external sharing enabled by running:
  
```PowerShell
Set-SPOTenant -EnableGuestSignInAcceleration $true
```

> [!NOTE]
> You must set SignInAccelerationDomain before executing this command. 
  
For more information, see [Set-SPOTenant](https://go.microsoft.com/fwlink/?LinkId=617177).
  
## Disable auto-acceleration

If you have already enabled auto-acceleration and want to disable it, you can change $true to $false for  _EnableGuestSignInAcceleration_, as in this example:
  
```PowerShell
Set-SPOTenant -EnableGuestSignInAcceleration $false
```

Alternatively, you can to disable auto-acceleration for the domain by using  _SignInAccelerationDomain_ with a null value, as in this example: 
  
```PowerShell
Set-SPOTenant -SignInAccelerationDomain ""
```

For more information, see [Set-SPOTenant](https://go.microsoft.com/fwlink/?LinkId=617177).
  
## Frequently asked questions about auto-acceleration
<a name="FAQ"> </a>

### Q: What can I do to make the experience as smooth as possible for my users?

A: You can do two things. First, ensure that your internal and external sites are clearly separated. Second, encourage users to access internal sites first as part of their daily workflow. Perhaps consider creating an internal-only site that serves as a welcome page. You can also modify your Group Policy so that users will be directed to an internal home page whenever they open their browser. After the user has logged on to one site (by using either method), they will not be prompted to log on to other sites.
  
### Q: What do I need to do to take advantage of auto acceleration on externally shared sites?

A: External users can potentially authenticate in one of three places: Azure Active Directory (if their organization is a "cloud" tenant or they use a Microsoft account), the user's company's identity provider or your company's identity provider (if using an on-premise extranet solution). If you want to enable auto-acceleration for externally shared sites, your IdP needs to be capable of supporting these use cases (or at least the ones that you want your guests to use). To support guests in AAD, MSA or other IdP's, your IdP will need to be capable of returning the user to the AAD login screen for authentication.
  

