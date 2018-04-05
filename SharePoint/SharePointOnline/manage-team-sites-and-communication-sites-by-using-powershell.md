---
title: "Manage team sites and communication sites by using PowerShell"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 4/3/2018
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 52ecc2ab-88c3-486e-b8ff-ef6a968ccd87
description: "Learn how to use PowerShell to manage communication sites as well as team sites that are part of an Office 365 group."
---

# Manage team sites and communication sites by using PowerShell

This article describes how global admins and SharePoint Online admins can use Microsoft PowerShell cmdlets to manage communication sites as well as team sites that are part of Office 365 groups. These new site types can't be managed in the SharePoint admin center. For info about using the SharePoint Online Management Shell, see [Introduction to the SharePoint Online Management Shell](https://technet.microsoft.com/en-us/library/fp161388.aspx). 
  
## Manage external sharing
<a name="BKMK_GroupSiteCollections"> </a>

By default, communication sites and team sites that are part of an Office 365 group have the sharing setting set to **Allow external users who accept sharing invitations and sign in as authenticated users**. To change this setting, you can use the Set-SPOSite PowerShell cmdlet.
  
Example:
  
```
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/site1 -SharingCapability ExternalUserSharingOnly 
```

This example updates the external sharing capability of the site collection "https://contoso.sharepoint.com/sites/site1" to allow sharing with authenticated external users. This cmdlet is executed immediately.
  
To view the existing sharing setting, use the Get-SPOSite PowerShell cmdlet.
  
Example:
  
```
(Get-SPOSite -Identity https://contoso.sharepoint.com/sites/site1).SharingCapability
```

For detailed information about these cmdlets and their parameters in PowerShell, see [Set-SPOSite](https://technet.microsoft.com/en-us/library/fp161394.aspx) and [Get-SPOSite](https://technet.microsoft.com/en-us/library/fp161380.aspx).
  
## Specify site storage (quota)
<a name="BKMK_GroupSiteCollections"> </a>

To specify the storage allocated to a communication site or a team site that's part of an Office 365 group, use the Get-SPOSite cmdlet. The following example gets and sets the storage quota for a site in the Contoso domain.
  
1. Run this command to get storage space details for the site:
    
  ```
  Get-SPOSite -Identity https://contoso.sharepoint.com/sites/<name> -detailed |fl
  ```

    (Where \<name\> is the name of the group or site)
    
2. Run this command to set the storage space for the site:
    
    > [!NOTE]
    > Before you can use the Set-SPOSite command, your site collection storage management must be set to **Manual**. To learn how to change this setting, see [Manage site collection storage limits](https://support.office.com/article/77389c2c-8e7e-4b16-ab97-1c7103784b08). 
  
  ```
  Set-SPOSite -Identity https://contoso.sharepoint.com/sites/<name> -StorageQuota 3000 -StorageQuotaWarningLevel 2000
  ```

    (Where \<name\> is the name of the group or site)
    
To verify that the set action worked, run the Get-SPOSite cmdlet again and make sure the storage space was updated. If you changed the site collection storage management setting, you can change it back to Automatic after setting the storage space for the site.
  
For detailed information about these cmdlets and their parameters in PowerShell, see [Set-SPOSite](https://technet.microsoft.com/en-us/library/fp161394.aspx) and [Get-SPOSite](https://technet.microsoft.com/en-us/library/fp161380.aspx).
  
## Get the list of site collections
<a name="BKMK_GroupSiteCollections"> </a>

To get a list of all communication sites and team sites that are part of an Office 365 group in your organization, use the Get-SPOSite cmdlet. 
  
1. Run this command to get a list of team sites that have Office 365 groups:
    
  ```
  Get-SPOSite -Template GROUP#0 -Includepersonalsite:$false
  
  ```

    Or this command to get a list of communication sites:
    
  ```
  Get-SPOSite -Template SITEPAGEPUBLISHING#0 
  ```

For detailed information about this cmdlet and its parameters in PowerShell, see [Get-SPOSite](https://technet.microsoft.com/en-us/library/fp161380.aspx).
  

