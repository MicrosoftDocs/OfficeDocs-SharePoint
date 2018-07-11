---
title: "Manage site creation in SharePoint Online"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 6/20/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection: Strat_SP_modern
search.appverid:
- SPO160
- BSA160
- GSP150
ms.assetid: e72844a3-0171-47c9-befb-e98b23e2dcf9
description: "Learn how to manage your user's self-service site creation."
---

# Manage site creation in SharePoint Online

As a SharePoint admin or Office 365 global admin, you can let your users create and administer their own SharePoint sites, determine what kind of sites they can create, and specify the location of the sites. By default, users can create communication sites as well as team sites that include [Learn about Office 365 groups](https://support.office.com/article/b565caa1-5c40-40ef-9915-60fdb2d97fa2).
  
Some functionality is introduced gradually to organizations that have signed up for the [Set up the Standard or Targeted release options in Office 365](https://support.office.com/article/3b3adfa4-1777-4ff0-b606-fb8732101f47). This means that you might not yet see this feature or it might look different than what is described in this article.
  
## Allow or prevent users from creating sites in SharePoint Online

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. Click **settings**.
    
5. Under **Site Creation**, select to show or hide the Create site command.
    
6. If you select **Show the Create site command to users who have permission to create sites**, specify the type of site that users can create.
    
    ![Site creation settings](media/df009314-836b-4ed1-b656-c5c6dd07f1a5.png)
  
    > [!NOTE]
    > To allow only a select set of users to create groups, use the PowerShell cmdlet  `GroupCreationAllowedGroupId`. For info about this cmdlet, see [Azure Active Directory cmdlets for configuring group settings](https://azure.microsoft.com/documentation/articles/active-directory-accessmanagement-groups-settings-cmdlets/). 
  
  - **A site that uses one of the new team site or communication site templates, or a classic site**: Use this option to let users who don't have permission to create a group still create classic sites. Select to create the groups under ( **/sites** or **/teams**) and specify whether a secondary contact is required. To let users create sites from a custom form you've created, enter its URL in the **Use the form at this URL** box. When users select which type of site they want to create, they'll be able to access the form by clicking "See other options." 
    
  - **A site that uses one of the new team site or communication site templates**: Use this option to allow only users who have permission to create groups to create sites. Select to create the groups under ( **/sites** or **/teams**) and whether a secondary contact is required. To let users create sites from a custom form you've created, enter its URL in the **Use the form at this URL** box. When users select which type of site they want to create, they'll be able to access the form by clicking "See other options." 
    
  - **A classic site**: Use this option to allow users to create only default classic sites or sites from your custom form. Specify where sites are created, and whether a site classification or secondary contact is required. To specify a custom form, enter the URL for the custom form in the **Use the form at this URL** box. 
    
    > [!NOTE]
    > For info about classifying sites that use one of the new team site or communication site templates, see [Manage Office 365 Groups with PowerShell](https://support.office.com/article/aeb669aa-1770-4537-9de2-a82ac11b0540#BKMK_CreateClassification). 
  

