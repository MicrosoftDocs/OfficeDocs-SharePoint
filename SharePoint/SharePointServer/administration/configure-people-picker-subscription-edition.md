---
title: "Configure People Picker in SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 08/29/2023
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
description: "Learn how to configure the People Picker web control in SharePoint Subscription Edition."
---

# Configure People Picker in SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

When modern authentication (a trusted identity provider) such as SAML 1.1 or OIDC 1.0 is used, the People Picker control can't search, resolve, and validate users and groups without writing a custom claim provider through C#. In SharePoint Server Subscription Edition, the People Picker has been enhanced to allow resolving users and groups based on their profiles in the User Profile Application (UPA). 

UPA must be configured to synchronize users and groups from the trusted identity provider membership store. This allows the People Picker to only resolve valid users and groups without requiring a custom claims provider. For more information, see [Enhanced People Picker for modern authentication](../administration/enhanced-people-picker-for-trusted-authentication-method.md).

This article will help you to configure People Picker in SharePoint Server Subscription Edition using PowerShell cmdlets.

## People Picker supports LDAPS (TLS connection encryption)

As organizations become more aware of the risks of unencrypted communication over a network, some are choosing to implement policies that require encryption for all network connections. HTTP is one of the most common protocols that organizations want to protect, but there are other network communication protocols as well. One of those is the Lightweight Directory Access Protocol (LDAP), which is used by applications to access directory services. The SharePoint People Picker feature uses LDAP to look up users and groups in Active Directory forests and domains. LDAP isn't an encrypted protocol by default, although there are several options to enable encryption with it. 

To facilitate organizations that require encryption for LDAP traffic, the SharePoint People Picker feature has added support for Secure LDAP (LDAPS) in SharePoint Server Subscription Edition Version 23H2. This allows the People Picker to use TLS connection encryption to protect LDAP traffic to TCP ports 636 and 3269. 

To enable Secure LDAP (LDAPS) in the SharePoint People Picker, use the `SecureSocketsLayer` switch parameter with the `Set-SPPeoplePickerConfig` and `Add-SPPeoplePickerSearchADDomain` PowerShell cmdlets.

Examples:

- `Set-SPPeoplePickerConfig -WebApplication https://team.contoso.local -SecureSocketsLayer`
- `Add-SPPeoplePickerSearchADDomain -WebApplication https://team.contoso.local -DomainName "contoso.local" -SecureSocketsLayer`

For more information, see [Plan for People Picker in SharePoint](plan-for-people-picker.md).

## PowerShell cmdlets to configure People Picker

With SharePoint Server Subscription Edition, you can use PowerShell cmdlets to configure the People Picker settings instead of `stsadm.exe` commands.

### Get-SPPeoplePickerConfig

Use the following PowerShell cmdlet to get People Picker settings of a specified Web application.

```powershell
Get-SPPeoplePickerConfig
   -WebApplication <SPWebApplicationPipeBind>
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Get-SPPeoplePickerConfig`](/powershell/module/sharepoint-server/get-sppeoplepickerconfig).

### Set-SPPeoplePickerConfig

Use the `Set-SPPeoplePickerConfig` cmdlet to configure the following People Picker settings of a specified Web application:

- Customized query filter sent to AD with People Picker query
- Customized query sent to AD with People Picker query
- The amount of time before AD search time-out
- Whether the People Picker control should only return the site collection users when clicking the "Check Names" button
- Whether the People Picker control should only return the site collection users when using the "Select People and Groups" dialog box
- Whether return only non-Active Directory users when the Web application uses form-based authentication

```powershell
Set-SPPeoplePickerConfig
   -WebApplication <SPWebApplicationPipeBind>
   [-ActiveDirectoryCustomFilter <String>]
   [-ActiveDirectoryCustomQuery <String>]
   [-ActiveDirectorySearchTimeout <Int32>]
   [-PeopleEditorOnlyResolveWithinSiteCollection]
   [-OnlySearchWithinSiteCollection]
   [-NoWindowsAccountsForNonWindowsAuthenticationMode]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Set-SPPeoplePickerConfig`](/powershell/module/sharepoint-server/set-sppeoplepickerconfig).

### Add-SPPeoplePickerSearchADDomain

Use this cmdlet to add a forest or domain to the list that the People Picker uses when searching for users.

```powershell
Add-SPPeoplePickerSearchADDomain
   -WebApplication <SPWebApplicationPipeBind>
   -DomainName <String>
   [-IsForest]
   [-Index <Int32>]
   [-Credential <PSCredential>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Add-SPPeoplePickerSearchADDomain`](/powershell/module/sharepoint-server/add-sppeoplepickersearchaddomain).

### Clear-SPPeoplePickerSearchADDomain

Use this cmdlet to clear the list of People Picker search forests and domains for a specified Web application.

```powershell
Clear-SPPeoplePickerSearchADDomain
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see [`Clear-SPPeoplePickerSearchADDomain`](/powershell/module/sharepoint-server/clear-sppeoplepickersearchaddomain).

### Get-SPPeoplePickerSearchADDomain

Use this cmdlet to return all Active Directory forests or domains that the People Picker uses when searching for users.

```powershell
Get-SPPeoplePickerSearchADDomain
   -WebApplication <SPWebApplicationPipeBind>
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Get-SPPeoplePickerSearchADDomain`](/powershell/module/sharepoint-server/get-sppeoplepickersearchaddomain).

### Remove-SPPeoplePickerSearchADDomain

Use this cmdlet to remove a forest of domain from the list that the People Picker uses when searching for users.

```powershell
Remove-SPPeoplePickerSearchADDomain
      -WebApplication <SPWebApplicationPipeBind>
      -DomainName <String>
      [-IsForest]
      [-UserName <String>]
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see [`Remove-SPPeoplePickerSearchADDomain`](/powershell/module/sharepoint-server/remove-sppeoplepickersearchaddomain).

### Add-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to add a domain to the People Picker distribution list search domains.

```powershell
Add-SPPeoplePickerDistributionListSearchDomain
   -WebApplication <SPWebApplicationPipeBind>
   -DomainName <String>
   [-Index <Int32>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Add-SPPeoplePickerDistributionListSearchDomain`](/powershell/module/sharepoint-server/add-sppeoplepickerdistributionlistsearchdomain).

### Clear-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to clear the list of People Picker distribution list search domains.

```powershell
Clear-SPPeoplePickerDistributionListSearchDomain
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see [`Clear-SPPeoplePickerDistributionListSearchDomain`](/powershell/module/sharepoint-server/clear-sppeoplepickerdistributionlistsearchdomain).

### Get-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to return all domains in the People Picker distribution list search domains.

```powershell
Get-SPPeoplePickerDistributionListSearchDomain
   -WebApplication <SPWebApplicationPipeBind>
   [-DomainName <String>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Get-SPPeoplePickerDistributionListSearchDomain`](/powershell/module/sharepoint-server/get-sppeoplepickerdistributionlistsearchdomain).

### Remove-SPPeoplePickerDistributionListSearchDomain

Use this cmdlet to remove a domain from the People Picker distribution list search domains.

```powershell
Remove-SPPeoplePickerDistributionListSearchDomain
      -WebApplication <SPWebApplicationPipeBind>
      -DomainName <String>
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see [`Remove-SPPeoplePickerDistributionListSearchDomain`](/powershell/module/sharepoint-server/remove-sppeoplepickerdistributionlistsearchdomain).

### Add-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to add an OU to People Picker service account directory path list.

```powershell
Add-SPPeoplePickerServiceAccountDirectoryPath
   -WebApplication <SPWebApplicationPipeBind>
   -OrganizationalUnitName <String>
   [-Index <Int32>]
   [-AssignmentCollection <SPAssignmentCollection>]
   [-WhatIf]
   [-Confirm]
   [<CommonParameters>]
```

For more information, see [`Add-SPPeoplePickerServiceAccountDirectoryPath`](/powershell/module/sharepoint-server/add-sppeoplepickerserviceaccountdirectorypath).

### Clear-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to clear the OUs of People Picker service account directory path list.

```powershell
Clear-SPPeoplePickerServiceAccountDirectoryPath
     -WebApplication <SPWebApplicationPipeBind>
     [-AssignmentCollection <SPAssignmentCollection>]
     [-WhatIf]
     [-Confirm]
     [<CommonParameters>]
```

For more information, see [`Clear-SPPeoplePickerServiceAccountDirectoryPath`](/powershell/module/sharepoint-server/clear-sppeoplepickerserviceaccountdirectorypath).

### Remove-SPPeoplePickerServiceAccountDirectoryPath

Use this cmdlet to remove an OU from People Picker service account directory path list.

```powershell
Remove-SPPeoplePickerServiceAccountDirectoryPath
      -WebApplication <SPWebApplicationPipeBind>
      -OrganizationalUnitName <String>
      [-AssignmentCollection <SPAssignmentCollection>]
      [-WhatIf]
      [-Confirm]
      [<CommonParameters>]
```

For more information, see [`Remove-SPPeoplePickerServiceAccountDirectoryPath`](/powershell/module/sharepoint-server/remove-sppeoplepickerserviceaccountdirectorypath).

## See also

- [Configure People Picker in SharePoint Server](configure-people-picker.md)
- [Plan for People Picker in SharePoint](plan-for-people-picker.md)