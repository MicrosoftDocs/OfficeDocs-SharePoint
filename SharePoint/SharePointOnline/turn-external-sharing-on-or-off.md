---
title: "Turn external sharing on or off for SharePoint Online"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/5/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection: Strat_OD_share
search.appverid: SPO160
ms.assetid: 6288296a-b6b7-4ea4-b4ed-c297bf833e30
description: "Learn how to turn sharing on and off for SharePoint Online."
---

# Turn external sharing on or off for SharePoint Online

If you're working with vendors, clients, or customers outside of your organization, you might want to give them access to certain areas of your site or to specific documents. In this article, we'll show you how to turn sharing on or off sharing for SharePoint Online. You must be a global or SharePoint admin in Office 365 to do this.
  
External sharing is controlled at both the tenant level (global settings that affect all of SharePoint Online) and the site collection level. The tenant-level settings determine what options are available at the site collection level.
  
The external sharing settings for individual site collections cannot be *less* restrictive than whatever is allowed at the tenant level, but these settings can be *more* restrictive. For example, if external sharing is turned on at the tenant level, but it is limited to allowing only authenticated users, then that will be the only kind of external sharing you can allow in a specific site collection. If external sharing through both sign-in and anonymous guest links is allowed at the tenant level, then those options are also available for each site collection. 
  
Choose one of the tabs below to configure sharing in SharePoint Online.
  
## Turn external sharing on or off globally for SharePoint Online
<a name="__turn_external_sharing"> </a>

Turning external sharing on at the tenant level means that site collections can then be enabled for sharing. In turn, sites and documents in a site collection that is enabled for sharing can be enabled for sharing.
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. In the left pane, click **sharing**.
    
5. Select one of the following:
    
    ![Tenant external sharing page](media/11d21d51-a5c8-41aa-a6bb-22484a389cd4.png)
  
### Which option to select...

|**Select this option:**|**If you want to:**|
|:-----|:-----|
|**Don't allow sharing outside your organization** <br/> |Prevent all users on all sites from sharing sites or sharing content on sites with external users. Users will not be able to share sites or content with external users, even if those users are already in your directory.  <br/> |
|**Allow sharing only with the external users that already exist in your organization's directory** <br/> |Allow sharing only for external users who are already in your directory. These users may exist in your directory because they previously accepted sharing invitations or because they were manually imported, such as through [Azure B2B collaboration](https://docs.microsoft.com/azure/active-directory/active-directory-b2b-what-is-azure-ad-b2b). (You can tell an external user because they have **#EXT#** in their user name.)  <br/> |
|**Allow users to invite and share with authenticated external users** <br/> | Require external users who have received invitations to view sites or content to sign-in with a Microsoft account before they can access the content.  <br/>  Site owners or others with full control permission can share sites with external users.  <br/>  Site owners or others with full control permissions on a site can share documents with external users.  <br/>  All external users will be required to sign in before they can view content.  <br/>  Invitations to view content can be redeemed only once. After an invitation has been accepted, it cannot be shared or used by others to gain access.  <br/> |
|**Allow sharing to authenticated external users and using anonymous access** <br/> (Optionally, you can set links to expire in a specific number of days, and select how recipients can use the links .)  <br/> | Allow site users to share sites with people who sign in as authenticated users, but you also want to allow site users to share documents through the use of anonymous guest links, which do not require invited recipients to sign in.  <br/>  Site owners or others with full control permissions can share sites with external users.  <br/>  All external users will be required to sign in before they can view content on a site that has been shared.  <br/>  When sharing documents, site owners or others with full control permissions can opt to require sign-in or send an anonymous guest link.  <br/>  When users share a document, they can grant external users either view or edit permissions to the document.  <br/>  External users who receive anonymous guest links can view or edit that content without signing in.  <br/>  Anonymous guest links could potentially be forwarded or shared with other people, who might also be able to view or edit the content without signing in.  <br/> |
   
### Additional settings

 **Set a default link type**
  
To better manage the type of links users share, you can set the default type of link that shows when users select **Get a link** to share documents and folders. 
  
![Default link type dialog box](media/4dc58d77-dccd-474f-b0fb-8ff8b3f1c088.png)
  
The most permissive types of links, of course, are Anonymous Access links which grant access to anyone who has the link. Internal links can be used only by users within your organization, and Direct links are accessible only by users who already have permission to access the document or folder. For more information, see [Change the default link type when users get links for sharing](change-default-sharing-link.md).
  
 **Additional settings**
  
When you choose to allow users to share outside your organization, you have some additional ways to allow or limit sharing.
  
![Additional settings for sharing](media/04c2257b-3af1-4902-8946-e7e251481da3.png)
  
 **Limit external sharing using domains**: You can allow or restrict access to specific domains. For more information, see [Restricted Domains Sharing in Office 365 SharePoint Online and OneDrive for Business](restricted-domains-sharing.md).
  
 **Prevent external users from sharing files, folders, and sites they don't own**: External users cannot share anything they don't own with anyone else. 
  
 **External users must accept sharing invitations using the same account that the invitations were sent to**: External users cannot use a different account than the one that the sharing invitation was sent to get access. 
  
 **Notifications**
  
To help your OneDrive for Business users monitor and control which external users have access to their files, you can specify that owners of OneDrive for Business files and folders are emailed when:
  
- Another user invites external users to shared files
    
- An external user accepts an invitation to access their files
    
- An anonymous access link is created or changed.
    
> [!NOTE]
>  If you turn off external sharing for your entire environment and later turn it back on, external users who previously had access to content or documents on sites will regain access to them. If you know that external sharing was previously turned on and in use for specific site collections and you do not want external users to be able to regain access if external sharing is ever turned on again globally, we recommend that you first turn off external sharing for those specific site collections. If you disable external access, or limit external access to a more restrictive form, external users will typically lose access within one hour of the change. >  If you disable external access, access to resources will also be blocked to guest members of Office 365 Groups. 
  
## Turn external sharing on or off for individual site collections
<a name="__toc332198786"> </a>

You must be a SharePoint Online admin to configure external sharing for individual site collections. Site collection administrators are not allowed to change external sharing configurations.
  
Note that this procedure applies to both classic sites and Office 365 Group-connected sites.
  
1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Click **Try the preview** to open the new SharePoint admin center. 
    
5. In the left pane, click **Site management**.
    
6. Locate the site that you want to update, and click the site name.
    
7. In the right pane, under **Sharing status**, click **Change**.
    
8. Select your option (see the following table) and click **Save**.
    
### Which option to select...

|**Select this option:**|**If you want to:**|
|:-----|:-----|
|Only people in current organization  <br/> |Prevent all users on all sites from sharing sites or sharing content on sites with external users. Users will not be able to share sites or content with external users, even if those users are already in your directory.  <br/> |
|Existing external users  <br/> |Allow sharing only for external users who are already in your directory. These users may exist in your directory because they previously accepted sharing invitations or because they were [manually imported](https://support.office.com/article/1a377d8f-4175-4c8f-ab09-7f1ed4b35404). (You can tell an external user because they have **#EXT#** in their user name.)  <br/> |
|New and existing external users  <br/> | Require external users who have received invitations to view sites or content to sign-in with a Microsoft account before they can access the content.  <br/>  Site owners or others with full control permission can share sites with external users.  <br/>  Site owners or others with full control permissions on a site can share documents with external users by requiring sign-in.  <br/>  All external users will be required to sign in before they can view content.  <br/>  Invitations to view content can be redeemed only once. After an invitation has been accepted, it cannot be shared or used by others to gain access.  <br/> |
|Anyone  <br/> | Allow site users to share sites with people who sign in as authenticated users, but you also want to allow site users to share documents through the use of anonymous guest links, which do not require invited recipients to sign in.  <br/>  Site owners or others with full control permissions can share sites with external users.  <br/>  All external users will be required to sign in before they can view content on a site that has been shared.  <br/>  When sharing documents, site owners or others with full control permissions can opt to require sign-in or send an anonymous guest link.  <br/>  When users share a document, they can grant external users either view or edit permissions to the document.  <br/>  External users who receive anonymous guest links can view or edit that content without signing in.  <br/>  Anonymous guest links could potentially be forwarded or shared with other people, who might also be able to view or edit the content without signing in.  <br/> |
   
> [!NOTE]
>  If you change the external sharing settings for the My Site site collection, these changes will also apply to any existing or newly created personal sites (formerly called My Sites). >  You might have site content shared with an Office 365 group that has guest members, and the group settings prevent guest members from accessing group resources. In this case, even if you turn on external sharing for the site collection, guests of the group may not be able to access site content. To enable or disable Office 365 Group guest member access, see [Manage guest access to Office 365 Groups](https://support.office.com/article/7c713d74-a144-4eab-92e7-d50df526ff96). >  If external sharing is turned off globally in the SharePoint Online Admin center, any shared links will stop working. If the feature is later reactivated, these links will resume working. It is also possible to disable individual links that have been shared if you want to permanently revoke access to a specific document. 
  

