---
title: "Let users connect classic team sites to new Office 365 groups"
ms.author: kaarins
author: kaarins
ms.date: 5/1/2018
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
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

1. Sign in to Office 365 as a global admin or SharePoint admin.
    
2. Select the app launcher icon ![The app launcher icon in Office 365](media/e5aee650-c566-4100-aaad-4cc2355d909f.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** \> **SharePoint**.
    
4. In the left pane, click **settings**.
    
5. Next to "Allow site owners to create Office 365 groups and attach them to existing sites," click **Do not allow site owners to create new Office 365 groups for their existing sites.** or **Allow site owners to create new Office 365 groups for their existing sites.**
    
When this setting is on, and the site collection administrator for a classic team site (with the template STS#0) is allowed to create groups, they will see the "Connect to a new Office 365 Group" option in settings. For more info, see:
  
- [Manage who can create Office 365 Groups](https://support.office.com/article/4c46c8cb-17d0-44b5-9776-005fced8e618)
    
- (Admin) Connect sites to new Office 365 groups using PowerShell: [Set-SPOSiteOffice365Group](https://go.microsoft.com/fwlink/?linkid=872615)
    
- (Admin) Connect sites to new Office 365 groups using the CSOM API: [CreateGroupForSite method](https://go.microsoft.com/fwlink/?linkid=872613)
    
- [SharePoint modernization scanner tool](https://go.microsoft.com/fwlink/?linkid=873066)
    
> [!NOTE]
> If your organization has set up OneDrive and SharePoint Multi-Geo, site collection administrators can connect a site to a new Office 365 group only if the site's location matches the user's preferred data location. 
  

