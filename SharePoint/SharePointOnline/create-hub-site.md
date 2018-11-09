---
title: "Create a hub site in SharePoint Online"
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 92bea781-15d8-4bda-805c-e441e2191ff3
description: "Learn how to create a hub site in SharePoint Online"
---

# Create a hub site in SharePoint Online

If you're a global or SharePoint admin in Office 365, you can convert any existing site to a hub site.
  
> [!NOTE]
>  We recommend selecting a communication site, or a team site that uses the new template. If you use a classic team site, the hub navigation will appear only on modern pages, and hub site settings will only appear on modern pages.<br>Sites that are already associated with another hub can't be converted to a hub site. <br>You can create up to 100 hub sites for an organization. There is no limit on the number of sites that can be associated with a hub site. <br>When users associate their sites with a hub, it doesn't impact the permissions of either the hub site or the associated sites. It's important to make sure all users you allow to associate sites to the hub have permission to the hub. 
  
<!--## Create a hub site in the new SharePoint admin center

> [!NOTE]
>  Some functionality is introduced gradually to organizations that have opted in to the [Targeted release option in Office 365](/office365/admin/manage/release-options-in-office-365). This means that you may not yet see some features described in this article.

1. In the new SharePoint admin center, under **Sites**, click **Active sites**.

2. Select the site, click **Hub site**, and then click **Convert to hub site**.

3. Enter a display name for the hub site, and then click **Save**.

    > [!TIP]
    > Using the Hub site menu, you can also associate a site with the hub site, change a site's association to a different hub site, or disassociate a site from a hub site.   -->

## Create a hub site using PowerShell

1. Download and install the latest [SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). If you already have a previous version installed, uninstall it first and then install the latest version.
    
2. Connect the SharePoint Online Management Shell to SharePoint Online for your organization. For info, see [Connect the SharePoint Online PowerShell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online). 
    
3. (Optional) If you want a group of people to be able to associate their sites to the hub, create a mail-enabled security group and add the users.
    
4. Run the following command to convert the site to a hub site and enable the hub site features:
    
  ```PowerShell
  Register-SPOHubSite URL
  ```

   (Where  *URL*  is the URL of the site.) 
    
5. When prompted with **Principals[0]**, provide the group created in step 3, or the UPN of an individual user. You can enter additional principals, one per line. Once you are finished assigning permissions, press Enter. If you want all site collection administrators in the organization to be able to associate their sites with the hub, press Enter at the first prompt.
    
    > [!NOTE]
    > To restrict permission to associate sites to the hub after creation, run the following command: >  `Grant-SPOHubSiteRights -Identity URL -Principals GroupEmail -Rights Join`> (Where  *Identity*  is the URL of the site and  *GroupEmail*  is the email address of the mail-enabled security group.) 
  
6. Notify the hub site owners that their site has been converted to a hub site.

7. Optionally, use a site design that gets applied when sites join the hub. For info, see [Set up a site design for your hub site](set-up-site-design-hub-site.md). For more info about site designs and site scripts, see [SharePoint site design and site script overview](/sharepoint/dev/declarative-customization/site-design-overview).
    
## More info

- For info about the above PowerShell commands, as well as the other commands for managing hub sites, see [Manage SharePoint hub sites](https://go.microsoft.com/fwlink/?linkid=869058).
    
- For info about how site owners can customize hub sites, see [Set up your SharePoint hub site](https://support.office.com/article/e2daed64-658c-4462-aeaf-7d1a92eba098).

    
## See also

[Remove a hub site](remove-hub-site.md)

