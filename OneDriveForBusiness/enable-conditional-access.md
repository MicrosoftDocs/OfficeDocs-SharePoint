---
title: "Enable conditional access support in the OneDrive sync client for Windows"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/11/2018
ms.audience: Admin
ms.topic: get-started-article
ms.prod: office-online-server
localization_priority: Normal
search.appverid:
- ODB160
- ODB150
ms.assetid: 028d73d7-4b86-4ee0-8fb7-9a209434b04e
description: "Learn how to enable conditional access in the new OneDrive sync client."
---

# Enable conditional access support in the OneDrive sync client for Windows

Conditional access control capabilities in Azure Active Directory offer simple ways for you to secure resources in the cloud. The new OneDrive sync client works with the conditional access control policies to ensure syncing is only done with compliant devices. For example, you might require sync to be available only on domain-joined devices or devices that meet compliance as defined by the Mobile Device Management system (like Intune).
  
For information about how conditional access works, see:
  
- [Azure Active Directory conditional access](https://go.microsoft.com/fwlink/?LinkId=823173)
    
- [How to set Azure Active Directory device-based conditional access policy for access control to Azure Active Directory connected applications](https://docs.microsoft.com/en-us/active-directory/active-directory-conditional-access-policy-connected-applications)
    
- [How to set up automatic registration of Windows domain-joined devices with Azure Active Directory](https://go.microsoft.com/fwlink/?LinkId=823174)
    
## Getting started

Use the following steps on each computer.
  
 **To enable conditional access support on the OneDrive sync client**
  
1. [Download and install](https://go.microsoft.com/fwlink/?linkid=844652) the OneDrive sync client. 
    
2. Download and open [EnableCAPreview.reg](http://go.microsoft.com/fwlink/?LinkId=824970) to enable the conditional access feature. 
    
3. Restart the sync client.
    
If you want to disable this feature, you can delete the registry key by running [DisableCAPreview.reg](http://go.microsoft.com/fwlink/?LinkId=828724). You need to restart the sync client for the change to take effect.
  
## Known issues

The following are known issues with this release:
  
- If you create a new access policy after the device has authenticated, it may take up to twenty-four hours for the policy to take effect.
    
- Conditional access for macOS is in preview.
    
- This release will not automatically take over sync from the previous OneDrive for Business sync client (Groove.exe). If you are already syncing with Groove.exe, it will continue to sync after you set up the OneDrive sync client. (We are working on a fix for this issue.) For instructions, see [Transition from the previous OneDrive for Business sync client](transition-from-the-previous-onedrive-for-business-sync-client.md).
    
- In some cases, the user may be prompted for credentials twice. We are working on a fix for this issue.
    
- Certain ADFS configurations may require additional setup to work with this release. Please run the following command on your ADFS server to ensure FormsAuthentication is added to the list of PrimaryIntranetAuthenticationProvider:
    
     `Set-AdfsGlobalAuthenticationPolicy -PrimaryIntranetAuthenticationProvider @('WindowsAuthentication', 'FormsAuthentication')`
    
- If you enable location-based conditional access, users will need to sign in immediately when they leave the set of approved IP address ranges. While outside of the set of approved IP address ranges, they will need to sign in again every time their access expires (every 90 minutes by default).
    
## Reporting problems

Please let us know if you run into any problems while using this release.
  
 **To report a problem**
  
1. Right-click the white or blue OneDrive cloud icon in the Windows taskbar notification area.
    
2. Click **Report a problem**.
    
3. Type a brief description of your issue, and then click **OK**. You will receive an email notification with a support ticket number to track your issue.
    
## Related Topics

[Deploy the new OneDrive sync client](deploy-the-sync-client-for-windows.md)
  
[Sync files with the new OneDrive sync client in Windows](https://support.office.com/article/615391c4-2bd3-4aae-a42a-858262e42a49)
  

