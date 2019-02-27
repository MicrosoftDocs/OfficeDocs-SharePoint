---
title: "Sharing errors in SharePoint and OneDrive"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Find the solution to SharePoint and OneDrive sharing errors"
---

# Sharing errors in SharePoint and OneDrive

## OSE201
TenantDontAllowExternalSharing

Error OSE201 indicates that external sharing is turned off for all of your SharePoint and OneDrive sites. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.   
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 
4. In the left pane of the new SharePoint admin center, select **sharing**.
5. Under **Sharing outside your organization**, choose the type of sharing that you want to allow.

## OSE202
TenantOnlyAllowExistingUserSharing

## OSE203
TenantOnlyAllowAuthUserSharing

## OSE204
SiteDontAllowExternalSharing

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Try it now** to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, select **Active sites**.



## OSE205
SiteOnlyAllowExistingUserSharing

## OSE206
SiteOnlyAllowAuthUserSharing

## OSE207
AllMySitesDontAllowExternalSharing

## OSE208
AllMySitesOnlyAllowExistingUserSharing

## OSE209
AllMySitesOnlyAllowAuthUserSharing

## OSE301
TenantFolderAnonymousLinkPermission

## OSE302
TenantFileAnonymousLinkPermission

## OSE303
SharerNotInWhoCanShareGroup

## OSE304
SharerNotInGuestSharingGroup

## OSE305
ShareeNotInWhoCanShareWithList

## OSE401
TenantLevelNotInAllowDomainList

## OSE402
TenantLevelInDenyDomainList

## OSE403
SiteLevelNotOnAllowDomainList

## OSE404
SiteLevelInDenyDomainList
  
## See also

[External sharing overview](external-sharing-overview.md)

[Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)

[Stop sharing files or folders or change permissions](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
