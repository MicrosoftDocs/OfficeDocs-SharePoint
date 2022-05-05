---
title: "Let users connect classic team sites to new Microsoft 365 groups"
ms.reviewer: tmehta
manager: serdars
recommendations: true
ms.author: mikeplum
author: MikePlumleyMSFT
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: 16fe6bf4-64f0-4078-b8c8-3761537303c5
description: "Learn how global and SharePoint admins can allow or prevent site collection administrators from connecting classing team sites to new Microsoft 365 groups."
---

# Let users connect classic team sites to new Microsoft 365 groups

As a global or SharePoint admin in Microsoft 365, you can allow or prevent site collection administrators from connecting classic team sites to new Microsoft 365 groups. You can also use Microsoft PowerShell or the API to connect sites to new Microsoft 365 groups.
  
## Allow or prevent site collection administrators from connecting classic team sites to new Microsoft 365 groups

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

>[!NOTE]
>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the **Settings** page.
    
2. Select **classic settings page**.
    
3. Next to "Connections from sites to Microsoft 365 groups," select **Prevent site collection administrators from connecting sites to new Microsoft 365 groups** or **Allow site collection administrators to connect sites to new Microsoft 365 groups**.
    
When this setting is on, and the site collection administrator for a classic team site (with the template STS#0) is allowed to create groups, they will see the "Connect to a new Microsoft 365 Group" option in settings. For more info, see:
  
- [Manage who can create Microsoft 365 Groups](/office365/admin/create-groups/manage-creation-of-groups)
    
- Connect sites to new Microsoft 365 groups using PowerShell: [Set-SPOSiteOffice365Group](/powershell/module/sharepoint-online/Set-SPOSiteOffice365Group)
    
- Connect sites to new Microsoft 365 groups using the CSOM API: [CreateGroupForSite method](/sharepoint/dev/features/groupify/groupify-csom)
    
- [SharePoint modernization scanner tool](https://go.microsoft.com/fwlink/?linkid=873066)
    
> [!NOTE]
> If your organization has set up OneDrive and SharePoint Multi-Geo, site collection administrators can connect a site to a new Microsoft 365 group only if the site's location matches the user's preferred data location.