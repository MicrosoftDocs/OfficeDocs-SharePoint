---
ms.date: 4/14/2024
title: "Restricted SharePoint Search Admin PowerShell Scripts"
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: administrator
ms.topic: how-to
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- M365-collaboration
- m365copilot
- magic-ai-copilot
description: "Learn how to use PowerShell scripts as a SharePoint Administrator or above in Microsoft 365 to get current mode of Restricted SharePoint Search, enable/disable Restricted SharePoint search, add to or remove from the allowed list, and get the list of current sites in the allowed list."
---

# Use PowerShell Scripts for Restricted SharePoint Search

> [!IMPORTANT]
> Restricted SharePoint Search is designed for customers of Microsoft 365 Copilot. Visit [here](https://go.microsoft.com/fwlink/p/?linkid=2260808) and the [overview of Restricted SharePoint Search](/sharepoint/restricted-sharepoint-search) for more information.

By default, **Restricted SharePoint Search** isn't enabled. To enable and set up Restricted SharePoint Search, you need to have a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or [above](/microsoft-365/admin/add-users/about-admin-roles) role in Microsoft 365. Depending on the scenario, some actions you need to take are:

- Get the current mode that is set for Restricted Search

- Enable and disable restricted SharePoint search

- Add sites to the allowed list by providing URL

- Remove sites from the allowed list by providing URL

- Get the existing list of URLs that are added in allow list

 This article covers how to use admin scripts in PowerShell for these actions.

## Before you start

You must be a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or [above](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365 to run the following admin scripts.
Before you use the PowerShell scripts in this article, you need to do the following:

1. If you haven’t, [download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

   > [!NOTE]
   > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

1. Connect to SharePoint as a [SharePoint Administrator](/sharepoint/sharepoint-admin-role) or [above](/microsoft-365/admin/add-users/about-admin-roles) in Microsoft 365 in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

## Get the current mode that is set for Restricted Search

Restricted SharePoint Search is disabled by default. To verify this feature’s current mode, you can run the following script:

**Get-SPOTenantRestrictedSearchMode**

**Module**: [Microsoft.Online.SharePoint.PowerShell](/powershell/module/sharepoint-online)

**Applies to:** SharePoint Online

**Syntax**

```powershell
Get-SPOTenantRestrictedSearchMode
```

**Example**

```powershell
Get-SPOTenantRestrictedSearchMode
```

This example lets the admin get the existing allowed list in the tenant. Result can be ‘Enabled’ or ‘Disabled’ based on the current setting.

## Enable or disable the Restricted Search setting

Enable or disabled the Restricted Search setting with the default being disabled. The first time when the setting is enabled the allow list is empty. To enable or disable the Restricted SharePoint Search, you can run:

**Set-SPOTenantRestrictedSearchMode**

Module: [Microsoft.Online.SharePoint.PowerShell](/powershell/module/sharepoint-online)

Applies to: SharePoint Online

**Syntax**

```powershell
Set-SPOTenantRestrictedSearchMode 
[-Mode] {Disabled | Enabled}
 [<CommonParameters>]
```

**Example 1**

```powershell
Set-SPOTenantRestrictedSearchMode -Mode Enabled  
```

Example 1 sets or enables the Restricted Tenant Search mode for the tenant.

**Example 2**

```powershell
Set-SPOTenantRestrictedSearchMode – Mode Disabled  
```

Example 2 disables the Restricted Tenant Search mode for the tenant.

**Parameters**

**-Mode**

Sets the mode for the Restricted Tenant Search.

| Type                         | String    |
|------------------------------|-----------|
| Position:                    | 0         |
| Default Value:               | Disabled  |
| Required:                    | True      |
| Accept Pipeline input:       | False     |
| Accept wildcard characters:  | False     |

## Add sites to the allowed list

When Restricted SharePoint Search is enabled, you can add site URLs to the allowed list in string or csv file:

**Add-SPOTenantRestrictedSearchAllowedList**

**Module:** [Microsoft.Online.SharePoint.PowerShell](/powershell/module/sharepoint-online)

**Applies to:** SharePoint Online

**Syntax**

```powershell
Add-SPOTenantRestrictedSearchAllowedList -SitesList <List[string]> [<CommonParameters>]
```

```powershell
Add-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl <string> [-ContainsHeader <bool>]  
 [<CommonParameters>]
```

**Example 1**

```powershell
Add-SPOTenantRestrictedSearchAllowedList -SitesList @(“[https://contoso.sharepoint.com/sites/Marketing](https://contoso.sharepoint.com/sites/Marketing)”, “[https://contoso.sharepoint.com/sites/Benefits](https://contoso.sharepoint.com/sites/Benefits)”)
```

This example lets the admin add the sites to the allowed list.

**Example 2**

```powershell
Add-SPOTenantRestrictedSearchAllowedList  -SitesListFileUrl C:\Users\admin\Downloads\UrlList.csv
```
  
This example lets the admin add the sites to the allowed list by giving a CSV file. Add the list of site URLs in URL column.

**Parameters**

**-SitesList**

Site list for allowed list.

| Type                         | String  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

**-SitesListFileURL**

File that has list of sites URLs that can be added to an allowed list when the tenant is set to Restricted Tenant Search Mode.

| Type                         | String  |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

## Remove sites from the allow list

You can remove sites from the allowed list by providing the Site URL in string or csv file using PowerShell script:

**Remove-SPOTenantRestrictedSearchAllowedList**

**Module:** [Microsoft.Online.SharePoint.PowerShell](/powershell/module/sharepoint-online)

**Applies to:** SharePoint Online

**Syntax**

```powershell
Remove-SPOTenantRestrictedSearchAllowedList -SitesList <List[string]> [<CommonParameters>]
```

```powershell
Remove-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl <string> [-ContainsHeader <bool>]
 [<CommonParameters>]
```

**Example 1**

```powershell
Remove-SPOTenantRestrictedSearchAllowedList -SitesList @(“[https://contoso.sharepoint.com/sites/Marketing](https://contoso.sharepoint.com/sites/Marketing)”, “[https://contoso.sharepoint.com/sites/HR](https://contoso.sharepoint.com/sites/HR)”)
```

Example 1 lets the admin remove the sites to the allowed list.

**Example 2**

```powershell
Remove-SPOTenantRestrictedSearchAllowedList -SitesListFileUrl C:\Users\admin\Downloads\UrlList.csv
```

Example 2 lets the admin add the sites to the allowed list by giving a CSV file.

**Parameters**

**-SitesList**

 Site list that will be removed from allowed list.

| Type                         | String   |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

**-SitesListFileURL**

File that has list of sites that can be removed from an allowed list when the tenant is set to Restricted Tenant Search Mode.

| Type                         | String   |
|------------------------------|----------|
| Position:                    | 0        |
| Default Value:               | None     |
| Required:                    | True     |
| Accept Pipeline input:       | False    |
| Accept wildcard characters:  | False    |

## Get the existing list of URLs in the allowed list

You can get the existing list of URLs in the allowed list by running the following PowerShell script:

**Get-SPOTenantRestrictedSearchAllowedList**

**Module:** [Microsoft.Online.SharePoint.PowerShell](/powershell/module/sharepoint-online)

**Applies to:** SharePoint Online

**Syntax**

```powershell
Get-SPOTenantRestrictedSearchAllowedList
```  

**Example**

```powershell
Get-SPOTenantRestrictedSearchAllowedList
```

This example lets the admin get the existing allowed list in the tenant.
