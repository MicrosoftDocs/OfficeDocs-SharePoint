---
ms.date: 4/12/2024
title: "Restricted SharePoint Search Admin PowerShell Scripts"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: administrator
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- M365-collaboration
description: "Learn how to use PowerShell scripts as a global admin to get current mode of Restricted SharePoint Search, enable/disable Restricted SharePoint search, add to or remove from the allowed list, and get the list of current sites in the allowed list."
---

# Use PowerShell Scripts for Restricted SharePoint Search
> [!IMPORTANT]
> Restricted SharePoint Search is designed for customers of Copilot for Microsoft 365. visit [here](https://go.microsoft.com/fwlink/p/?linkid=2260808) and [here](/restricted-sharepoint-search.md) to more information.

By default, **Restricted SharePoint Search** is not enabled. To enable and set up Restricted SharePoint Search, you need to have Global/Tenant and SharePoint admin roles. Depending on the scenario, some actions you need to take are:

- Get the current mode that is set for Restricted Search

- Enable and disable restricted SharePoint search

- Add sites to the allowed list by providing URL

- Remove sites to the allowed list by providing URL

- Get the existing list of URLs that are added in allow list

 This article covers how to use admin scripts in PowerShell for these actions.

## Before you start

Before you using the PowerShell scripts in this article, you need to do the following:

1. If you haven’t, [download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

> [!NOTE]
> If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](/sharepoint/sharepoint-admin-role) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

## Get the current mode that is set for Restricted Search

Restricted SharePoint Search is disabled by default. To verify this feature’s current mode, you can run the following script:

> **Get-SPOTenantRestrictedSearchMode**
>
> **Module**: [<u>Microsoft.Online.SharePoint.PowerShell</u>](/powershell/module/sharepoint-online)
>
> **Applies to:** SharePoint Online
>
> **Syntax**
>
> Get-SPOTenantRestrictedSearchMode
>
> **Description**
>
> Restricted SharePoint Search gives Global/Tenant and SharePoint admins the ability to enable/disable organization-wide search. The Get-SPOTenantRestrictedSearchMode cmdlet will return the current mode that is set in the tenant."
>
>  
>
> **Example 1**
>
> Get-SPOTenantRestrictedSearchMode
>
> This example lets the admin get the existing allowed list in the tenant. Result can be ‘Enabled’ or ‘Disabled’ based on the current setting.

## Enable or disable the Restricted Search setting

To enable or disable the Restricted SharePoint Search, you can run:

> **Set-SPOTenantRestrictedSearchMode**
>
> Module: [<u>Microsoft.Online.SharePoint.PowerShell</u>](/powershell/module/sharepoint-online)
>
> Applies to: SharePoint Online
>
> **Syntax**
>
> Set-SPOTenantRestrictedSearchMode  
>
> \[-Mode\] {Disabled \| Enabled}
>
>  \[\<CommonParameters\>\]
>
> **Description:** Enable or disabled the Restricted Search setting with the default being disabled. The first time when the setting is enabled the allow list is empty.  
>
>  
>
> **Example 1**
>
> Set-SPOTenantRestrictedSearchMode -Mode Enabled  
>
> This example sets or enables the Restricted Tenant Search mode for the tenant.
>
> **Example 2**
>
> Set-SPOTenantRestrictedSearchMode – Mode Disabled  
>
> This example disables the Restricted Tenant Search mode for the tenant.
>
>  
>
> **Parameters**
>
> **-Mode**
>
> **Sets the mode for the Restricted Tenant Search.**

| Type:                        | String:   |
|------------------------------|-----------|
| Position:                    | 0         |
| Default Value:               | Disabled  |
| Required:                    | True      |
| Accept Pipeline input:       | False     |
| Accept wildcard characters:  | False     |



## Add sites to the allowed list

When Restricted SharePoint Search is enabled, you can add site URLs to the allowed list in string or csv file:

> **Add-SPOTenantRestrictedSearchAllowedList**
>
> **Module:** [<u>Microsoft.Online.SharePoint.PowerShell</u>](/powershell/module/sharepoint-online)
>
> **Applies to:** SharePoint Online
>
> **Syntax**
>
> Add-SPOTenantRestrictedSearchAllowedList -SitesList \<List\[string\]\> \[\<CommonParameters\>\]
>
> Add-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl \<string\> \[-ContainsHeader \<bool\>\]  
>
> \[\<CommonParameters\>\]
>
> **Description**
>
> Restricted SharePoint Search gives Global/Tenant and SharePoint admins the ability to enable/disable organization-wide search. When enabled, this control offers up to 100 sites to be included in organization-wide search, including user's previously accessed files and content from user's frequent sites. The allow list is a set of curated sites where the customer has reviewed the permissions and applied data governance to them. The allow list supports Site Collections, Hub, and Communication sites.
>
> **Example 1**
>
> Add-SPOTenantRestrictedSearchAllowedList -SitesList @(“[<u>https://contoso.sharepoint.com/sites/Marketing</u>](https://contoso.sharepoint.com/sites/Marketing)”, “[<u>https://contoso.sharepoint.com/sites/Benefits</u>](https://contoso.sharepoint.com/sites/Benefits)”)
>
> This example lets the admin add the sites to the allowed list.
>
> **Example 2**
>
> Add-SPOTenantRestrictedSearchAllowedList  -SitesListFileUrl C:\Users\admin\Downloads\UrlList.csv
>
>  
>
> This example lets the admin add the sites to the allowed list by giving a CSV file. Add the list of site URL’s in URL column.
>
>  
>
> **Parameters**
>
> **-SitesList**
>
> **Site list for allowed list.**

| Type:                        | String:  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

>  
>
> **-SitesListFileURL**
>
> **File that has list of sites URLs that can be added to an allowed list when the tenant is set to Restricted Tenant Search Mode.**

| Type:                        | String:  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |



## Remove sites from the allow list

You can remove sites from the allowed list by providing the Site URL in string or csv file using PowerShell script:

> **Remove-SPOTenantRestrictedSearchAllowedList**
>
> **Module:** [<u>Microsoft.Online.SharePoint.PowerShell</u>](/powershell/module/sharepoint-online)
>
> **Applies to:** SharePoint Online
>
> **Syntax**
>
> Remove-SPOTenantRestrictedSearchAllowedList -SitesList \<List\[string\]\> \[\<CommonParameters\>\]
>
> Remove-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl \<string\> \[-ContainsHeader \<bool\>\]
>
> \[\<CommonParameters\>
>
>  
>
> **Description**
>
> Restricted SharePoint Search gives an ability to Global/Tenant and SharePoint admins to Global/Tenant and SharePoint admins to enable/disable organization wide search. This control, when enabled offers up to 100 sites to be allowed in organization wide search, includes user’s previously accessed files and includes content from user’s frequent sites. Allow list is a set of curated sites where the customer has reviewed the permissions and has applied data governance on them. Allow list will support Site Collections, Hub and Comm sites. This command gives the ability to remove sites from existing allowed list so they can be removed from organization wider search.  
>
> **Example 1**
>
> Remove-SPOTenantRestrictedSearchAllowedList -SitesList @(“[<u>https://contoso.sharepoint.com/sites/Marketing</u>](https://contoso.sharepoint.com/sites/Marketing)”, “[<u>https://contoso.sharepoint.com/sites/HR</u>](https://contoso.sharepoint.com/sites/HR)”)
>
> This example lets the admin remove the sites to the allowed list.
>
> **Example 2**
>
> Remove-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl C:\Users\admin\Downloads\UrlList.csv
>
> This example lets the admin add the sites to the allowed list by giving a CSV file.
>
>  
>
> **Parameters**
>
> **-SitesList**
>
> **Site list that will be removed from allowed list.**

| Type:                        | String:  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

>  
>
>  
>
> **-SitesListFileURL**
>
> **File that has list of sites that can be removed from an allowed list when the tenant is set to Restricted Tenant Search Mode.**

| Type:                        | String:  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |



## Get the existing list of URLs in the allowed list

You can get the existing list of URLs in the allowed list by running the following PowerShell script:

> **Get-SPOTenantRestrictedSearchAllowedList**
>
> **Module:** [<u>Microsoft.Online.SharePoint.PowerShell</u>](/powershell/module/sharepoint-online)
>
> **Applies to:** SharePoint Online
>
> **Syntax**
>
> Get-SPOTenantRestrictedSearchAllowedList
>
> **Description**
>
> Restricted SharePoint Search gives an ability to Global/Tenant and SharePoint admins to Global/Tenant and SharePoint admins to enable/disable organization wide search. This control, when enabled offers up to 100 sites to be allowed in organization wide search, includes user’s previously accessed files and includes content from user’s frequent sites. Allow list is a set of curated sites where the customer has reviewed the permissions and has applied data governance on them. Allow list will support Site Collections, Hub and Comm sites.
>
> The Get-SPOTenantRestrictedSearchAllowedList cmdlet will return all the sites that are in the allowed list in the tenant.  
>
> You must be a SharePoint Online or global administrator to run the Get-SPOTenantRestrictedSearchAllowedList cmdlet.
>
>  
>
> **Example 1**
>
> Get-SPOTenantRestrictedSearchAllow<u>ed</u>List
>
> This example lets the admin get the existing allowed list in the tenant.
