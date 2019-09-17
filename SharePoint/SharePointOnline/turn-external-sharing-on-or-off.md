---
title: "Turn external sharing on or off"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: 6288296a-b6b7-4ea4-b4ed-c297bf833e30
description: "Learn how to change your SharePoint sharing settings."
---

# Turn external sharing on or off

This article describes how global and SharePoint admins in Office 365 can change their organization-level sharing settings for SharePoint and OneDrive.

For end-to-end guidance around how to configure guest sharing in Microsoft 365, see:
- [Collaborate with guests on a document](https://docs.microsoft.com/Office365/Enterprise/collaborate-on-documents)
- [Collaborate with guests in a site](https://docs.microsoft.com/Office365/Enterprise/collaborate-in-a-site)
- [Collaborate with guests in a team](https://docs.microsoft.com/Office365/Enterprise/collaborate-as-a-team)

To learn how to change the external sharing setting for a user's OneDrive, see [Change the external sharing setting for a user's OneDrive](/onedrive/user-external-sharing-settings). 
  
 
## Change the organization-level external sharing setting
<a name="__turn_external_sharing"> </a>
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Under **External sharing**, specify your sharing level for SharePoint and OneDrive. The default level for both is "Anyone."

> [!NOTE]
>  The SharePoint setting applies to all site types, including those connected to Office 365 groups. <br> The OneDrive setting can be more restrictive than the SharePoint setting, but not more permissive. <br> The SharePoint external sharing setting on this page is the same as the one in the Microsoft 365 admin center, under **Settings** \> **Services & add-ins** \> **Sites**. These settings are also the same as those in the OneDrive admin center. 

![External sharing settings in the new SharePoint admin center](media/externalsharing.png)

This setting is for your organization overall. Each site has its own sharing setting which you can set independently, though it must be at the same or more restrictive setting as the organization. See [Change the external sharing setting for a site](change-external-sharing-site.md) for more information.
  
### Which option to select...

|**Select this option:**|**If you want to:**|
|:-----|:-----|
|**Anyone**  <br/> | Allow users to share files and folders by using links that let anyone who has the link access the files or folders anonymously. This setting also allows users to share sites with new and existing guests who authenticate. If you select this setting, you can restrict the Anyone links so that they must expire within a specific number of days, or so that they can give only View permission.<br>|
|**New and existing guests** <br/> | Require people who have received invitations to sign in with their work or school account (if their organization uses Office 365) or a Microsoft account, or to provide a code to verify their identity. Users can share with guests already in your organization's directory, and they can send invitations to people who will be added to the directory if they sign in. For more info about verification codes, see [Secure external sharing in SharePoint Online](what-s-new-in-sharing-in-targeted-release.md)<br/>  Invitations to view content can be redeemed only once. After an invitation has been accepted, it cannot be shared or used by others to gain access.  <br/> |
|**Existing guests** <br/> |Allow sharing only with guests who are already in your directory. These guests may exist in your directory because they previously accepted sharing invitations or because they were manually added, such as through [Azure B2B collaboration](/azure/active-directory/b2b/what-is-b2b). (To see the guests in your organization, go to the [Guests page in the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/GuestUsers)).  <br/> |
|**Only people in your organization** <br/> | Turn off external sharing.


> [!NOTE]
>  If you turn off external sharing for your organization and later turn it back on, guests who previously had access will regain it. If you know that external sharing was previously turned on and in use for specific sites and you don't want guests to be able to regain access, first turn off external sharing for those specific sites.<br>If you restrict or turn off external sharing, guests will typically lose access within one hour of the change.  

### Advanced settings for external sharing

![External sharing settings in the new SharePoint admin center](media/advanced-external-sharing.png)

**Limit external sharing by domain**

This is useful if you want to limit sharing with particular partners, or help prevent sharing with people at certain organizations. The organization-level setting on this page affects all SharePoint sites and each user's OneDrive. To use this setting, list the domains (maximum of 1000) in the box, using the format *domain.com*. To list multiple domains, press Enter after adding each domain. 
    
You can also limit external sharing by domain by using the [Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant) Microsoft PowerShell cmdlet with -SharingDomainRestrictionMode and either -SharingAllowedDomainList or -SharingBlockedDomainList. For info about limiting external sharing by domain at the site level, see [Restricted domains sharing](restricted-domains-sharing.md).

**Guests must sign in using the same account to which sharing invitations are sent**

By default, guests can receive an invitation at one account but sign in with a different account. After they redeem the invitation, it can't be used with any other account.

**Allow guests to share items they don't own**

By default, guests must have full control permission to share items externally.


## File and folder links

Choose the option you want to show by default when a user gets a link. 

![External sharing settings in the new SharePoint admin center](media/defaultlinks.png)

> [!NOTE]
> This setting specifies the default for your organization, but site owners can choose a different default link type for a site.

- **Specific people** - This option allows users to enter external email addresses. This is the best option for external sharing of sensitive or proprietary information because it requires that the recipient verify their identity before they can access the file.
- **Only people in your organization** - If links are forwarded, they'll work for anyone in the organization. This option is best if your organization shares broadly internally and rarely shares externally.
- **Anyone with the link** - This option is available only if your external sharing setting is set to "Anyone." Forwarded links will work internally or externally, but you won't be able to track who has access to shared items or who has accessed shared items. This is best for friction-free sharing if most files and folders in SharePoint and OneDrive aren't sensitive. 
  
> [!IMPORTANT]
> If you select "Anyone with the link," but the site or OneDrive is set to allow sharing only with guests who sign in or provide a verification code, the default link will be "Only people in your organization." Users will need to change the link type to "Specific people" to share files and folders in the site or OneDrive externally. 



### Advanced settings for "Anyone" links

![External sharing settings in the new SharePoint admin center](media/advanced-settings-anyone-links.png)

**Link expiration** - You can require all "Anyone" links to expire, and specify the maximum number of days allowed

**Link permissions** - You can restrict "Anyone" links so that they can only provide view permission for files or folders.

## Other

![External sharing settings in the new SharePoint admin center](media/othersettings.png)

**Display to owners the names of people who viewed their files**

This setting lets you control whether the owner of a shared file can see the people who only view (and don't edit) the file in OneDrive file access statistics. File access statistics appear on a card when users hover over a file name or thumbnail in OneDrive. The statistics include the number of views on the file, the number of people who viewed it, and the list of people who viewed it.

> [!NOTE]
> This setting is selected by default. If you clear it, file viewer info is still recorded and available to you to audit as an admin. OneDrive owners will also still be able to see people who have viewed their shared Office files by opening the files from Office.com or from the Office desktop apps.

On the classic sharing page, you can choose whether you want the default link permission to be view or edit. 

You can also allow only users in specific security groups to share externally. To see the security groups in your organization, go to the [Groups page in the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/groups).

## Need more help?

[!INCLUDE[discussionforums.md](includes/discussionforums.md)]

You can also find help on security and permissions in these [YouTube videos from SharePoint community experts](https://www.youtube.com/playlist?list=PLKurDp05sqD0oE3KnohD69dkP5fHmrfuN).

## See also

[Stop sharing files or folders or change permissions](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
