---
title: "Enable conditional access support in the OneDrive sync app"
ms.reviewer: 
ms.author: adjoseph
author: adeejoseph
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: medium
search.appverid:
- ODB160
- ODB150
- MET150
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
ms.assetid: 028d73d7-4b86-4ee0-8fb7-9a209434b04e
description: "In this article, you'll learn how to enable conditional access in the new OneDrive sync app."
---

# Enable conditional access support in the OneDrive sync app

Conditional access control capabilities in Azure Active Directory offer simple ways for you to secure resources in the cloud. The new OneDrive sync app works with the conditional access control policies to ensure syncing is only done with compliant devices. For example, you might require sync to be available only on domain-joined devices or devices that meet compliance as defined by the Mobile Device Management system (like Intune).
  
For information about how conditional access works, see:
  
- [Azure Active Directory conditional access](/azure/active-directory/conditional-access/)
    
- [Require managed devices for cloud app access with conditional access](/azure/active-directory/conditional-access/require-managed-devices)
    
- [Configure hybrid Azure Active Directory join for managed domains](/azure/active-directory/devices/hybrid-azuread-join-managed-domains)

- [Control access from unmanaged devices](/sharepoint/control-access-from-unmanaged-devices#block-or-limit-access-to-a-specific-sharepoint-site-or-onedrive)
    
## Recommendations for Windows

We recommend using this feature on Windows together with [silent account configuration](use-silent-account-configuration.md) for the best experience. The OneDrive sync app will automatically use ADAL, and will support both device-based and location-based conditional access policies.

If you don't use silent account configuration, set the EnableADAL registry key:

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\OneDrive] 
"EnableADAL"=dword:1

Setting this registry key configures the OneDrive sync app to use ADAL directly.
  
## Known issues

The following are known issues with this release:
  
- If you create a new access policy after the device has authenticated, it may take up to twenty-four hours for the policy to take effect.
    
- In some cases, the user may be prompted for credentials twice. We are working on a fix for this issue.
    
- Certain AD FS configurations may require additional setup to work with this release. Please run the following command on your AD FS server to ensure FormsAuthentication is added to the list of PrimaryIntranetAuthenticationProvider:
    
     `Set-AdfsGlobalAuthenticationPolicy -PrimaryIntranetAuthenticationProvider @('WindowsAuthentication', 'FormsAuthentication')`
    
- If you enable location-based conditional access, users will get a prompt about every 90 to 120 minutes by default when they leave the set of approved IP address ranges. The exact timing depends on the access token expiry duration (60 minutes by default), when their computer last obtained a new access token, and any specific conditional access timeouts put in place.
    
## Reporting problems

Please let us know if you run into any problems while using this release.
  
 **To report a problem**
  
1. Right-click the blue OneDrive cloud icon in the Windows taskbar notification area or macOS menu bar.
    
2. Click **Get help**.
    
3. Type a brief description of your issue, and then click **Submit**. 
