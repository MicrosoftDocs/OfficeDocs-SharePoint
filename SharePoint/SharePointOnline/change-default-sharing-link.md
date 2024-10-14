---
ms.date: 10/09/2024
title: "Change the default sharing link for a site"
ms.reviewer: srice
ms.author: ruihu
author: maggierui
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'WSSCentralAdmin_SharingLinkTypeLearnMore'
- 'SharingLinkTypeLearnMore'
- 'seo-marvel-apr2020'
- admindeeplinkSPO
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: 81b763af-f301-4226-8842-8d13bd07face
description: "Learn how to change the default sharing link for a specific site. You can change this setting at the organization level and at the site level."
---

# Change the default link for a site

Users can share files and folders in Microsoft SharePoint by sending a link. They should select a link type based on the people to whom they want to give permission. The following link types are available: 

- Anyone with the link (previously called "anonymous access" or "shareable")
- People in your organization with the link 
- People with existing access
- Specific people 

  ![Screenshot of Link settings.](media/link-settings.png)

As a [SharePoint Administrator](./sharepoint-admin-role.md) or above, you may want to enable users to send "Anyone" links, but you may not want this to be the default type of link when users select to share files and folders. You can set the default type of link to something more restrictive, while still allowing users to select other types of links as needed. You can change this setting at the organization level and at the site (previously called "site collection") level. 
  
> [!NOTE]
> The default sharing link setting applies only to libraries that use the new experience.<br>This setting does not affect Outlook Web App, Outlook 2016, or Office clients prior to Office 2016. 


For info about the changing this setting at the organization level, see [File and folder links](turn-external-sharing-on-or-off.md#file-and-folder-links).

  
## Change the default link type for a site

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.
    
2. In the left column, select a site.

3. Select **Sharing** on the command bar.

4. Under **Default sharing link type**, clear the **Same as organization-level setting** checkbox.

    ![Screenshot of site-level default sharing link settings](media/link-settings.png)

5. Choose the default sharing link setting that you want to use for this site, and then select **Save**.

    > [!Note]
    > To change the default link type for a Teams private or shared channel site, you must use the [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) PowerShell cmdlet.

## Change the default link permission for a site

1. Following the steps 1-3 above, under **Default link permission**, clear the **Same as organization-level setting** checkbox.
1. Choose the default sharing link permission that you want to use for this site, and then select **Save**.

## Use a sensitivity label to configure the default sharing link settings

If you are using [sensitivity labels](/microsoft-365/compliance/sensitivity-labels) to classify and protect your SharePoint sites, you can also configure the default sharing link type and sharing link permissions for a site and also individual documents by using a sensitivity label.

For more information about this scenario, see [Use sensitivity labels to configure the default sharing link type for sites and documents in SharePoint and OneDrive](/microsoft-365/compliance/sensitivity-labels-default-sharing-link).

## Related topics

[Turn external sharing on or off for a site](change-external-sharing-site.md)

