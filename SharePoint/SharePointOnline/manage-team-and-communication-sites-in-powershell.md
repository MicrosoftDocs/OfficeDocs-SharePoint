---
title: "Manage team sites and communication sites by using PowerShell"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/17/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 52ecc2ab-88c3-486e-b8ff-ef6a968ccd87
description: "Learn how to use PowerShell to manage communication sites as well as team sites that are part of an Office 365 group."
---

# Manage team sites and communication sites by using PowerShell

This article describes how global admins and SharePoint admins in Office 365 can use Microsoft PowerShell cmdlets to manage communication sites as well as team sites that belong to Office 365 groups. You can't manage these new site types in the classic SharePoint admin center, but you can in the SharePoint admin center preview. [Learn how](manage-sites-in-new-admin-center.md)  
  
## Manage external sharing
<a name="BKMK_GroupSiteCollections"> </a>

By default, team sites that belong to Office 365 groups and communication sites and have the same sharing setting as your organization-wide setting, unless the organization-wide setting allows anonymous access links. In this case, the external sharing setting for these new site types is "Allow external users who accept sharing invitations and sign in as authenticated users." Follow these steps to change the external sharing setting for a site.
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Run the following command:
    
  ```
  Set-SPOSite -Identity <site URL> -SharingCapability <sharing level>
  ```

   (Where  _\<site URL\>_ is the URL of the site and  _\<sharing level\>_ is Disabled, ExternalUserSharingOnly, or ExternalUserAndGuestSharing.) For example,  `Set-SPOSite -Identity https://contoso.sharepoint.com/sites/site1 -SharingCapability ExternalUserSharingOnly`. This cmdlet is executed immediately.
    
To view the existing sharing setting, run the following command.
  
```
(Get-SPOSite -Identity <site URL>).SharingCapability
```

For detailed information about these cmdlets and their parameters in PowerShell, see [Set-SPOSite](https://go.microsoft.com/fwlink/?linkid=872325) and [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326).
  
## Specify site storage space (quota)
<a name="BKMK_GroupSiteCollections"> </a>

If you manage site collection storage limits manually, you can use PowerShell to specify the storage space for a communication site or a team site that belongs to an Office 365 group. [Learn more about managing site collection storage limits](manage-site-collection-storage-limits.md)
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Run this command to check the current storage limit for the site:
    
  ```
  Get-SPOSite -Identity <site URL> -detailed |fl
  ```

   (Where \<site URL\> is the URL of the group or site.) The command will return "StorageQuota" in megabytes, for example 1048576 for 1 TB or 5242880 for 5 TB.
    
4. Run this command to set the storage space for the site:
    
  ```
  Set-SPOSite -<site URL> -StorageQuota <limit> -StorageQuotaWarningLevel <warning>
  ```

   (Where \<site URL\> is the name of the group or site, \<limit\> is the storage limit in megabytes, and \<warning\> is the storage warning level in megabytes.)
    
To verify that the set action worked, run the Get-SPOSite cmdlet again and make sure the storage space was updated. 
  
For detailed information about these cmdlets and their parameters in PowerShell, see [Set-SPOSite](https://go.microsoft.com/fwlink/?linkid=872325) and [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326).
  
## Get the list of site collections
<a name="BKMK_GroupSiteCollections"> </a>

Follow these steps to get a list of all communication sites in your organization, or all team sites that belong to Office 365 groups. 
  
1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).
    
2. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://go.microsoft.com/fwlink/?linkid=869066).
    
3. Run this command to get a list of communication sites:
    
  ```
  Get-SPOSite -Template SITEPAGEPUBLISHING#0 
  ```

   Or run this command to get a list of team sites that belong to Office 365 groups:
    
  ```
  Get-SPOSite -Template GROUP#0 -Includepersonalsite:$false
  
  ```

For detailed information about this cmdlet and its parameters in PowerShell, see [Get-SPOSite](https://go.microsoft.com/fwlink/?linkid=872326).
  

