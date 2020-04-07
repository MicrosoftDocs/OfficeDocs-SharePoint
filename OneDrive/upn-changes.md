---
title: "How UPN changes affect OneDrive"
ms.reviewer: waynewin
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
- MET150
description: Learn about how changing a User Principal Name (UPN) affects the OneDrive URL and OneDrive features.
ms.custom: seo-marvel-apr2020
---

# How UPN changes affect the OneDrive URL and OneDrive features

A User Principal Name (UPN) is made up of two parts, the prefix (user account name) and the suffix (DNS domain name). For example:

user1@contoso.com

In this case, the prefix is "user1" and the suffix is "contoso.com."

You can change a user's UPN in the [Microsoft 365 admin center](/office365/admin/add-users/change-a-user-name-and-email-address?view=o365-worldwide) by changing the user's username or by setting a different email alias as primary. You can also change a user's UPN in the [Azure AD admin center](/azure/active-directory/fundamentals/active-directory-users-profile-azure-portal) by changing their username. And you can change a UPN by [using Microsoft PowerShell](/powershell/module/msonline/set-msoluserprincipalname?view=azureadps-1.0).

> [!NOTE]
> A user's UPN (used for signing in) and email address can be different. If you just need to add a new email address for a user, you can add an alias without changing the UPN.

## Types of UPN changes

You can change a UPN by changing the prefix, suffix, or both:

- Changing the prefix. For example, if a person's name changed, you might change their account name:

    user1@contoso.com to user2@contoso.com

- Changing the suffix. For example, If a person changed divisions, you might change their domain:

    user1@contoso.com to user1@contososuites.com

> [!IMPORTANT]
> UPN changes can take several hours to propagate through your environment.

## OneDrive URL

A user's OneDrive URL is based on their UPN:

``https://contoso-my.sharepoint.com/personal/user1_contoso_com``

(where user1_contoso_com corresponds with user1@contoso.com)

In this case, if you changed the prefix to user2 and the suffix to contososuites.com, the user's OneDrive URL would change to:

``https://contoso-my.sharepoint.com/personal/user2_contososuites_com``

After you change a UPN, any saved links to the user's OneDrive (such as desktop shortcuts or browser favorites) will no longer work and will need to be updated.
  
## Sync

If a user has sync app build 18.212.1021.0008 or later on either Windows or Mac ([released to Production in November, 2018](https://support.office.com/article/845dcf18-f921-435e-bf28-4e24b95e5fc0), the sync app will automatically switch to sync with the new OneDrive location after a UPN change. While the UPN change is propagating through your environment, users may see an error in the OneDrive sync app that "One or more libraries could not be synced." If they click for more information, they will see "You don't have permission to sync this library." Users who see this error should restart the sync app. The error will go away when the UPN change has been fully propagated and the sync app is updated to use the user's new OneDrive URL.  

> [!NOTE]
> Synced team sites are not impacted by the OneDrive URL change.

## OneNote

After a UPN change, users will need to close and reopen their OneNote notebooks stored in OneDrive.

[Close a notebook in OneNote for Windows](https://support.office.com/article/d4b52723-6f33-430b-b1f7-35dbb07548a8)

[Open a notebook in OneNote for Windows](https://support.office.com/article/2e99ead1-a1db-43e3-9945-0b0df9542888)

## Recent files lists

After a UPN change, users will need to browse to re-open active OneDrive files in their new location. Any links to the files (including browser favorites, desktop shortcuts, and "Recent" lists in Office apps and Windows) will no longer work.

## Shared OneDrive files

If a user shared OneDrive files with others, the links will no longer work after a UPN change. The user will need to re-share the files.

## Office Backstage View

After a UPN change, although Office will continue to work as expected, the user's original UPN will continue to be displayed in the Office Backstage View. To update the Office Backstage View to display the changed UPN, the user will need to sign out and then sign in using the Office client.

## Search and Delve

After a UPN change, it might take a while for files at the new OneDrive URL to be indexed. During this time, search results in OneDrive and SharePoint will use the old URL. Users can copy the URL, paste it in the address bar, and then update the portion for the new UPN.

Delve will also link to old OneDrive URLs for a period of time after a UPN change. As activity occurs in the new location, the new links will start appearing.

## SharePoint automated workflows and customizations

Any automated workflows that were created with Power Automate or SharePoint 2013 workflows and refer to a OneDrive URL will not work after a UPN change. Similarly, any SharePoint apps (including Power Apps) that reference a OneDrive URL will need to be updated after a UPN change.

## Recommendations

- If you're changing many UPNs within your organization, make the UPN changes in batches to manage the load on the system.

- If possible, apply changes before a weekend or during non-peak hours to allow time for the change to propagate and not interfere with your users' work.
  
## See also

[Info about UserPrincipalName attribute population in hybrid identity](/azure/active-directory/hybrid/plan-connect-userprincipalname)
