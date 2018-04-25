---
title: "Connect sites to new Office 365 groups"
ms.author: kaarins
author: kaarins
ms.date: 4/23/2018
ms.audience: ITPro
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.assetid: 16fe6bf4-64f0-4078-b8c8-3761537303c5
description: "As a global or SharePoint admin in Office 365, you can allow or prevent site owners from connecting existing classic team sites to new Office 365 groups. You can also use Microsoft PowerShell or the API to connect sites to new Office 365 groups."
---

# Connect sites to new Office 365 groups

As a global or SharePoint admin in Office 365, you can allow or prevent site owners from connecting existing classic team sites to new Office 365 groups. You can also use Microsoft PowerShell or the API to connect sites to new Office 365 groups.
  
## Allow or prevent site owners from connecting classic team sites to new Office 365 groups

1. [Sign in to Office 365](e9eb7d51-5430-4929-91ab-6157c5a050b4.md) as a global admin or SharePoint admin. 
    
2. Select the app launcher icon ![The icon that looks like a waffle and represents a button click that will reveal multiple application tiles for selection.](media/3b8a317e-13ba-4bd4-864e-1ccd47af39ee.png) in the upper-left and choose **Admin** to open the Office 365 admin center. (If you don't see the Admin tile, you don't have Office 365 administrator permissions in your organization.) 
    
3. In the left pane, choose **Admin centers** > **SharePoint**.
    
4. In the left pane, click **settings**.
    
5. Next to "Connections from sites to Office 365 groups," click **Allow site owners to connect sites to new Office 365 groups** or **Prevent site owners from connecting sites to new Office 365 groups**. 
    
When this setting is on, and the owner of a classic team site (with the template STS#0) is allowed to create groups, they will see the "Connect to a new Office 365 Group" option in settings. For more info, see:
  
- [Manage who can create Office 365 Groups](https://support.office.com/article/f68aada0-7700-4e61-b822-6ce203afd145)
    
- [Connect a classic experience SharePoint team site to a new Office 365 Group](https://support.office.com/article/469c6ee0-2139-4496-9914-7e39d07ac49d)
    
- (Admin) Connect sites to new Office 365 groups using PowerShell: [Set-SPOSiteOffice365Group](https://go.microsoft.com/fwlink/?linkid=872615)
    
- (Admin) Connect sites to new Office 365 groups using the CSOM API: [CreateGroupForSite method](https://go.microsoft.com/fwlink/?linkid=872613)
    
> [!NOTE]
> If your organization has set up OneDrive and SharePoint Multi-Geo, site owners can connect a site to a new Office 365 group only if the site's location matches the user's preferred data location. 
  

