---
title: "How UPN changes affect OneDrive"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: Strat_OD_admin
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
- MET150
description: "Learn how changing a User Principal Name (UPN) affects the OneDrive URL and OneDrive features."
---

# How UPN changes affect the OneDrive URL and OneDrive features

A User Principal Name (UPN) is made up of two parts, the prefix (user account name) and the suffix (DNS domain name). For example:

user1@contoso.com

In this case, the prefix is "user1" and the suffix is "contoso.com."

You can change a user's UPN in the [Microsoft 365 admin center](/office365/admin/add-users/change-a-user-name-and-email-address?view=o365-worldwide) by changing the user's username or by setting a different email alias as primary. You can also change a user's UPN in the [Azure AD admin center](/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal) by changing their username. And you can change a UPN by [using Microsoft PowerShell](/powershell/module/msonline/set-msoluserprincipalname?view=azureadps-1.0).

> [!NOTE]
> A user's UPN (used for signing in) and email address can be different. If you just need to add a new email address for a user, you can add an alias without changing the UPN. 

You can change the prefix, suffix, or both. For example, if a person's name changed, you might change their account name:

```user1@contoso.com``` to ```user2@contoso.com```

If a person changed divisions, you might change their domain:

```user1@contoso.com``` to ```user1@contososuites.com```

In both of these cases, the change impacts the user's OneDrive URL:

```https://contoso-my.sharepoint.com/personal/```*user1*_*contoso*_com
  
## Sync

If the user has sync client build 18.212.1021.0008 or later (on either Windows or Mac), the sync client will switch to sync with the new location without any user interaction. Note that UPN changes can take several hours to propagate through your environment. During the transition period, users may see an error in the OneDrive sync client that "One or more libararies could not be synced." If they click for more information, they will see "You don't have permission to sync this library." Users who see this error should restart the sync client. The error will go away when the UPN change has been fully propagated and the sync client is updated to use the user's new OneDrive URL.  

> [!NOTE]
> Synced team sites are not impacted by the OneDrive URL change. 

## OneNote

After UPN changes, users will need to close and reopen their OneNote notebooks stored in OneDrive. 

[Close a notebook in OneNote for Windows](https://support.office.com/article/d4b52723-6f33-430b-b1f7-35dbb07548a8)

[Open a notebook in OneNote for Windows](https://support.office.com/article/2e99ead1-a1db-43e3-9945-0b0df9542888)

## Recent files lists

After UPN changes, users will need to browse to re-open active OneDrive files in their new location. Any links to the files (including browser favorites, desktop shortcuts, and "Recent" lists in Office apps and Windows) will no longer work.

## Shared OneDrive files

If a user shared OneDrive files with others, the links will no longer work after a UPN change. The user will need to re-share the files. 

## Recommendations

- If you're changing many UPNs within your organization, make the UPN changes in batches to manage the load on the system. Each SharePoint site to which a user has permission will need to be updated with the new UPN.

- If possible, apply changes before a weekend or during non-peak hours to allow time for the change to propagate and not interfere with your users' work.
  
## See also

[Info about UserPrincipalName attribute population in hybrid identity](/azure/active-directory/hybrid/plan-connect-userprincipalname)

