---
ms.date: 03/21/2023
title: "Manage sites in the SharePoint admin center"
ms.reviewer: daminasy
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.collection:  
- Strat_SP_admin
- M365-collaboration
- m365initiative-spsitemanagement
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid:
- SPO160
- MET150
- BSA160
ms.assetid: d8c63491-0410-405c-880a-8cef7fa4480a
description: "In this article, you'll learn about tasks you can perform on the Active sites page of the SharePoint admin center."
---

# Manage sites in the SharePoint admin center

The <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a> of the SharePoint admin center lets you view the SharePoint sites in your organization, including communication sites, channel sites, and sites that belong to Microsoft 365 groups. It also lets you [sort and filter sites](customize-admin-center-site-list.md), search for a site, and create new sites.
  
![Active sites page](media/active-sites-page.png)
  
The Active sites page lists the root website for each site collection. Subsites and the following sites aren't included.

- Sites with these URLs:
  
   |**URL**|**Description**|
   |:-----|:-----|
   |/sites/contentTypeHub |Content hub host |
   |/sites/CompliancePolicyCenter |Policy center |
   |/portal/hub |PointPublishing hub |
   |/search |Search site |
   |/personal/ |OneDrive sites |

- Sites with these templates:

   |**ID**|**Name**|**Description**|
   |:-----|:-----|:-----|
   |6000 |REVIEWCTR# |Review center |
   |10043 |FunSite# |SharePoint tenant fundamental site |
   |65 |POINTPUBLISHINGHUB# |PointPublishing hub |
   |66 |POINTPUBLISHINGPERSONAL#0 |Personal blog |
   |67 |POINTPUBLISHINGTOPIC#0 |PointPublishing topic |
   |3500 |POLICYCTR# |Compliance policy center |
   |30003 |TestSite# |Test site |
   |3 |CENTRALADMIN# |Central admin site |
   |54 |SPSMSITEHOST# |My Site host |
   |21 |SPSPERS# |SharePoint Portal Server personal space |
   |16 |TENANTADMIN# |Tenant admin site |
   |301 |REDIRECTSITE# |Redirect site |
   |70 |CSPCONTAINER# |CSP container |

> [!NOTE] 

> You will likely see differing usage results when comparing the SharePoint site usage report from the Microsoft 365 admin center by going to the Reports > [Usage]( https://go.microsoft.com/fwlink/p/?linkid=2074756) page versus the [Active sites page]( https://go.microsoft.com/fwlink/?linkid=2185220) of the SharePoint admin center. Particularly, the number of sites present in the Microsoft 365 admin center will likely be higher as the Microsoft 365 admin center report will include all sites, even the sites listed above as not included in SharePoint admin center Active sites. Here are examples of why that is:  

> -  Changing the site address in the SharePoint admin center will create a re-direct site. The re-direct site usage will continue to appear in the Microsoft 365 admin center by going to Reports > [Usage]( https://go.microsoft.com/fwlink/p/?linkid=2074756). The same re-direct site will not appear on the [Active sites page](https://go.microsoft.com/fwlink/?linkid=2185220) from the SharePoint admin center because it is no longer active. See [Effects of changing a site address](https://learn.microsoft.com/en-us/sharepoint/change-site-address#effects-of-changing-a-site-address).  

> -  Any Teams, Private or Shared channels can be associated to a SharePoint site. The number of Channel sites appears on the SharePoint site usage report from the Microsoft 365 admin center by going to the Reports > [Usage](https://go.microsoft.com/fwlink/p/?linkid=2074756) page. While [Active sites page] (https://go.microsoft.com/fwlink/?linkid=2185220) from the SharePoint admin center has a link to the Channel sites, you will need to click on the Channel sites link to view the site usage.  

> -  A Search Center site will appear in the Microsoft 365 admin center by going to Reports > [Usage]( https://go.microsoft.com/fwlink/p/?linkid=2074756), but will not appear on the [Active sites page] (https://go.microsoft.com/fwlink/?linkid=2185220) from the SharePoint admin center. The Seach Center is not considered an Active site.  

> - The MySite will appear in the Microsoft 365 admin center by going to Reports > [Usage]( https://go.microsoft.com/fwlink/p/?linkid=2074756), but will not appear on the [Active sites page] (https://go.microsoft.com/fwlink/?linkid=2185220) from the SharePoint admin center. The MySite is not considered an Active site.  

For more info about tasks on the Active sites page, see:

- [Create a site](create-site-collection.md)
- [Register a site as a hub site](create-hub-site.md) and [Unregister a site as a hub site](remove-hub-site.md)
- [Change sharing settings for a site](change-external-sharing-site.md)  
- [Delete a site](delete-site-collection.md)
- [Manage site storage limits](manage-site-collection-storage-limits.md)

## Add or remove site admins and group owners
<a name="addremoveadmins"> </a>

For all site types except channel sites, you can add or remove site admins and change the primary admin. For group-connected team sites, you can also add and remove group owners. Note that if you remove a person as a primary admin, they will still be listed as an additional admin. For info about each role, see [About site permissions](site-permissions.md).

1. In the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), select **Sites** > **Active sites** or browse to the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>.

2. In the left column, select a site. 
    
3. Select **Membership** on the command bar to open the details panel to update the permissions of the members.
   :::image type="content" source="media/membership-details-panel.png" alt-text="Screenshot of membership tab in details panel":::

4. Add or remove people or change their role, and then select **Save**.
    
## Change a site's hub association
<a name="hubsite"> </a>
  
1. In the [SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185219), select **Sites** > **Active sites** or browse to the <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** page</a>.

2. In the left column, select a site. 
    
3. Select **Hub** on the command bar. The options that appear depend on whether the site you selected is registered as a hub site, or associated with a hub. The Hub menu lets you register a site as a hub site, associate it with a hub, change its hub association, and unregister it as a hub site. For more information, see [More info about hubs](planning-hub-sites.md).

## View site details
<a name="viewsitedetails"> </a>

For more info about a site, select the site name or click anywhere on the site row except on the URL column to open the details panel or for channel sites select the link in the **Channel sites** column and then select the site name.
  
![The General tab of the details panel](media/general-tab-details-panel.png)
  
To view site activity including the number of files stored and storage usage, select the **Activity** tab. Activity information is not available for US Government GCC High and DoD customers.
  
To view site admins, owners, members, and visitors, select the **Membership** tab.

:::image type="content" source="media/membership-details-panel.png" alt-text="Screenshot of Membership tab selection on details panel":::
  
For info about the roles in this panel, see [About site permissions](site-permissions.md).

## Related topics

[Manage site storage limits](manage-site-collection-storage-limits.md)

