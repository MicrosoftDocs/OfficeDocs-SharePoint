---
title: "Let users connect classic team sites to new Office 365 groups"
ms.reviewer: 
manager: 
ms.author: kaarins
author: kaarins
ms.date: 5/1/2018
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 16fe6bf4-64f0-4078-b8c8-3761537303c5
description: "Learn how global and SharePoint admins can allow or prevent site collection administrators from connecting classing team sites to new Office 365 groups."
---

# Let users connect classic team sites to new Office 365 groups

As a global or SharePoint admin in Office 365, you can allow or prevent site collection administrators from connecting classic team sites to new Office 365 groups. You can also use Microsoft PowerShell or the API to connect sites to new Office 365 groups.
  
## Allow or prevent site collection administrators from connecting classic team sites to new Office 365 groups

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  
    
2. In the left pane of the admin center, under **Admin centers**, select **SharePoint** to open the SharePoint admin center. (You might need to select **Show more** to see the list of admin centers.) If this opens the new SharePoint admin center, select **Classic SharePoint admin center** in the left pane.
    
3. In the left pane, select **settings**.
    
4. Next to "Allow site owners to create Office 365 groups and attach them to existing sites," select **Do not allow site owners to create new Office 365 groups for their existing sites.** or **Allow site owners to create new Office 365 groups for their existing sites.**
    
When this setting is on, and the site collection administrator for a classic team site (with the template STS#0) is allowed to create groups, they will see the "Connect to a new Office 365 Group" option in settings. For more info, see:
  
- [Manage who can create Office 365 Groups](/office365/admin/create-groups/manage-creation-of-groups)
    
- Connect sites to new Office 365 groups using PowerShell: [Set-SPOSiteOffice365Group](https://go.microsoft.com/fwlink/?linkid=872615)
    
- Connect sites to new Office 365 groups using the CSOM API: [CreateGroupForSite method](https://go.microsoft.com/fwlink/?linkid=872613)
    
- [SharePoint modernization scanner tool](https://go.microsoft.com/fwlink/?linkid=873066)
    
> [!NOTE]
> If your organization has set up OneDrive and SharePoint Multi-Geo, site collection administrators can connect a site to a new Office 365 group only if the site's location matches the user's preferred data location. 
  

