---
ms.date: 06/19/2023
title: Manage sharing settings for SharePoint and OneDrive in Microsoft 365
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords: CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_OD_share
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 6288296a-b6b7-4ea4-b4ed-c297bf833e30
description: "Learn how global and SharePoint administrators can change the organization-level sharing settings for SharePoint and OneDrive in Microsoft 365."
---

# Manage sharing settings for SharePoint and OneDrive in Microsoft 365

This article describes how global administrators and SharePoint administrators in Microsoft 365 can change their organization-level sharing settings for SharePoint and OneDrive. (If you want to share a file or folder, read [Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c) or [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07).)

For end-to-end guidance around how to configure guest sharing in Microsoft 365, see:
- [Set up secure collaboration with Microsoft 365](/microsoft-365/solutions/setup-secure-collaboration-with-teams)
- [Collaborate with guests on a document](/microsoft-365/solutions/collaborate-on-documents)
- [Collaborate with guests in a site](/microsoft-365/solutions/collaborate-in-site)
- [Collaborate with guests in a team](/microsoft-365/solutions/collaborate-as-team)

To change the sharing settings for a site after you've set the organization-level sharing settings, see [Change sharing settings for a site](change-external-sharing-site.md). To learn how to change the external sharing setting for a specific user's OneDrive, see [Change the external sharing setting for a user's OneDrive](/onedrive/user-external-sharing-settings).

### SharePoint and OneDrive integration with Azure AD B2B

There are two external sharing models used in SharePoint and OneDrive:

- SharePoint external authentication

- SharePoint and OneDrive integration with Azure AD B2B

When using Azure AD B2B integration, Azure AD external collaboration settings, such as [guest invite settings and collaboration restrictions](/azure/active-directory/external-identities/external-collaboration-settings-configure) apply.

The following table shows the differences between the two sharing models.

|Sharing method|Files and folders|Sites|
|:--|:----------------|:----|
|SharePoint external authentication<br>(Azure AD B2B integration not enabled)|No guest account created*<br>Azure AD settings don't apply|N/A<br>(Azure AD B2B always used)|
|Azure AD B2B integration enabled|Guest account always created<br>Azure AD settings apply|Guest account always created<br>Azure AD settings apply|

*A guest account may already exist from another sharing workflow, such as sharing a team, in which case it's used for sharing.

For information on how to enable or disable Azure AD B2B integration, see [SharePoint and OneDrive integration with Azure AD B2B](sharepoint-azureb2b-integration.md).

## Video demonstration

This video shows how the settings on the <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** page in the SharePoint admin center</a> affect the sharing options available to users.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RE4yw9m?autoplay=false]

## Change the organization-level external sharing setting
<a name="__turn_external_sharing"> </a>
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.
 
2. Under **External sharing**, specify your sharing level for SharePoint and OneDrive. The default level for both is **Anyone**.

    > [!NOTE]
    > The SharePoint setting applies to all site types, including those connected to Microsoft 365 groups and teams. Groups and Teams guest sharing settings also affecte connected SharePoint sites.
    > 
    > The OneDrive setting can be more restrictive than the SharePoint setting, but not more permissive.

    ![External sharing settings](media/externalsharing.png)

    This setting is for your organization overall. Each site has its own sharing setting that you can set independently, though it must be at the same or more restrictive setting as the organization. See [Change the external sharing setting for a site](change-external-sharing-site.md) for more information.

> [!IMPORTANT]
> [Azure Active Directory external collaboration settings](/azure/active-directory/external-identities/external-collaboration-settings-configure) determine who can invite guests in your organization for site sharing (always) and file and folder sharing (if Azure B2B collaboration is enabled). Be sure to review Azure AD guest access settings as part of your SharePoint and OneDrive sharing setup.

### Which option to select

| Select this option: | If you want to: |
|:-----|:-----|
|**Anyone**  <br/> | Allow users to share files and folders by using links that let anyone who has the link access the files or folders without authenticating. This setting also allows users to share sites with new and existing guests who authenticate. If you select this setting, you can restrict the Anyone links so that they must expire within a specific number of days, or so that they can give only View permission.<br/><br/>[File requests](https://support.office.com/article/f54aa7f8-2589-4421-b351-d415fc3b83af) requires that OneDrive be set to **Anyone** and edit permissions for **Anyone** links be enabled. OneDrive settings other than **Anyone** disable file requests.<br/><br/>See [Best practices for sharing files and folders with unauthenticated users](/Office365/Enterprise/best-practices-anonymous-sharing) for more information.<br/>|
|**New and existing guests** <br/> | Require people who have received invitations to sign in with their work or school account (if their organization uses Microsoft 365) or a Microsoft account, or to provide a code to verify their identity. Users can share with guests already in your organization's directory, and they can send invitations to people who will be added to the directory if they sign in. For more info about verification codes, see [Secure external sharing in SharePoint](what-s-new-in-sharing-in-targeted-release.md) |
|**Existing guests** <br/> |Allow sharing only with guests who are already in your directory. These guests may exist in your directory because they previously accepted sharing invitations or because they were manually added, such as through [Azure B2B collaboration](/azure/active-directory/b2b/what-is-b2b). (To see the guests in your organization, go to the [Guests page in the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/GuestUsers)).  <br/> |
|**Only people in your organization** <br/> | Turn off external sharing.

> [!NOTE]
> If you turn off external sharing for your organization and later turn it back on, guests who previously had access regain it. If you know that external sharing was previously turned on and in use for specific sites and you don't want guests to regain access, first turn off external sharing for those specific sites.
> 
> If you restrict or turn off external sharing, guests typically lose access within one hour of the change.  

### More external sharing settings

![More external sharing settings](media/external-sharing.png)

**Limit external sharing by domain**

This is useful if you want to limit sharing with particular partners, or help prevent sharing with people at certain organizations. The organization-level setting on this page affects all SharePoint sites and each user's OneDrive. To use this setting, list the domains (maximum of 3000) in the box, using the format *domain.com*. To list multiple domains, press Enter after adding each domain. 

You can also limit external sharing by domain by using the [Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant) Microsoft PowerShell cmdlet with -SharingDomainRestrictionMode and either -SharingAllowedDomainList or -SharingBlockedDomainList. For info about limiting external sharing by domain at the site level, see [Restricted domains sharing](restricted-domains-sharing.md).

[Allowed or blocked domains in Azure AD](/azure/active-directory/external-identities/allow-deny-list) also affect SharePoint and OneDrive site sharing (always) and file and folder sharing (if Azure B2B collaboration is enabled). Be sure to review Azure AD collaboration restrictions as part of your SharePoint and OneDrive sharing setup.

**Allow only users in specific security groups to share externally**

For info about this setting, see [Manage security groups](./manage-security-groups.md).

**Guests must sign in using the same account to which sharing invitations are sent**

By default, guests can receive an invitation at one account but sign in with a different account. After they redeem the invitation, it can't be used with any other account. This setting only applies to sharing that doesn't use Azure AD B2B collaboration.

**Allow guests to share items they don't own**

By default, guests must have full control permission to share items externally.

**Guest access to a site or OneDrive will expire automatically after this many days**

If your administrator has set an expiration time for guest access, each guest that you invite to the site or with whom you share individual files and folders will be given access for a certain number of days. For more information visit, [Manage guest expiration for a site](https://support.microsoft.com/en-us/office/manage-guest-expiration-for-a-site-25bee24f-42ad-4ee8-8402-4186eed74dea)

**People who use a verification code must reauthenticate after this many days**

If people who use a verification code have selected to "stay signed in" in the browser, they must prove they can still access the account they used to redeem the sharing invitation by entering a code sent to that account. If Azure B2B collaboration is enabled, the [Azure AD setting](/azure/active-directory/external-identities/one-time-passcode) is used instead of this setting.

## File and folder links

Choose the option you want to show by default when a user creates a sharing link. 

![Default links](media/defaultlinks.png)

> [!NOTE]
> This setting specifies the default for your organization, but you can choose a different default link type for a site.

- **Specific people** - This option is most restrictive and impedes broad internal sharing. If you allow external sharing, this option lets users share with specific people outside the organization. 

- **Only people in your organization** - If links are forwarded, they'll work for anyone in the organization. This option is best if your organization shares broadly internally and rarely shares externally.

- **Anyone with the link** - This option is available only if your external sharing setting is set to **Anyone**. Forwarded links work internally or externally, but you can't track who has access to shared items or who has accessed shared items. This is best for friction-free sharing if most files and folders in SharePoint and OneDrive aren't sensitive. 
  
  > [!IMPORTANT]
  > If you select **Anyone with the link**, but the site or OneDrive is set to allow sharing only with guests who sign in or provide a verification code, the default link is **Only people in your organization**. Users need to change the link type to **Specific people** to share files and folders in the site or OneDrive externally. 

### Advanced settings for **Anyone** links

![Settings in the new SharePoint admin center](media/advanced-settings-anyone-links.png)

**Link expiration** - You can require all **Anyone** links to expire, and specify the maximum number of days allowed. If you change the expiration time, existing links will keep their current expiration time if the new setting is longer, or be updated to the new setting if the new setting is shorter.

**Link permissions** - You can restrict **Anyone** links so that they can only provide view permission for files or folders.

If you are using file requests, the link permissions must be set for **View and edit** for files and **View, edit, and upload** for folders.

## Other settings

![Other sharing settings](media/othersettings.png)

**Show owners the names of people who viewed their files in OneDrive**

This setting lets you control whether the owner of a shared file can see on the file card the people who only view (and don't edit) the file in OneDrive. The file card appears when users hover over a file name or thumbnail in OneDrive. The info includes the number of views on the file, the number of people who viewed it, and the list of people who viewed it. To learn more about the file card, see [See files you shared in OneDrive](https://support.office.com/article/6b67b82b-9c5c-4348-ab10-fd5b0d8df76c). 

> [!NOTE]
> This setting is selected by default. If you clear it, file viewer info is still recorded and available to you to audit as an admin. OneDrive owners can also still see people who have viewed their shared Office files by opening the files from Office.com or from the Office desktop apps.

**Let site owners choose to display the names of people who viewed files or pages in SharePoint**

This setting lets you specify whether site owners can allow users who have access to a file, page, or news post to see on the file card who has viewed the item. 

![Viewer information on the file card for a document.](media/8ff30cde-b358-4b35-9f9d-77cb01c69f09.png)

This setting is turned on by default at the organization level and off at the site level for existing sites. Viewer information is shown only when the setting is on at both the organization and site level. We recommend that site owners turn on this feature only on team sites that don't have sensitive information. [Learn how site owners can turn on this feature](https://support.office.com/article/ee26dde0-c30e-4eca-b1c3-38922c450967).

> [!NOTE]
> Historical data is included when this setting is enabled. Likewise, if the setting is turned off and back on at the organization level or site level, the views during the off period are included in the history.

**Use short links for sharing files and folders**

Uses a shorter link format for sharing files and folders. This may be useful if you have integrations that require a shorter URL.

## Need more help?

[!INCLUDE[discussionforums.md](includes/discussionforums.md)]

You can also find help on security and permissions in these [YouTube videos from SharePoint community experts](https://www.youtube.com/playlist?list=PLKurDp05sqD0oE3KnohD69dkP5fHmrfuN).

## See also

[Limit accidental exposure to files when sharing with guests](/Office365/Enterprise/sharing-limit-accidental-exposure)

[Create a secure guest sharing environment](/Office365/Enterprise/create-a-secure-guest-sharing-environment)

[Stop sharing files or folders or change permissions](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)

