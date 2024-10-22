---
ms.date: 10/22/2024
title: "Domain restrictions when sharing SharePoint & OneDrive content"
ms.reviewer: srice
ms.author: jtremper
author: jacktremper
manager: pamgreen
recommendations: true
audience: End User
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- Strat_OD_share
- M365-collaboration
ms.custom:
- seo-marvel-mar2020
- admindeeplinkSPO
search.appverid: MET150
ms.assetid: 5d7589cd-0997-4a00-a2ba-2320ec49c4e9
description: "Allow sharing only with guests on specific domains, or block sharing with guests on specific domains."
---

# Restrict sharing of SharePoint and OneDrive content by domain

If you want to restrict sharing with other organizations (either at the organization level or site level), you can limit sharing by domain.

> [!NOTE]
> If you have enrolled in the [SharePoint and OneDrive integration with Microsoft Entra B2B](sharepoint-azureb2b-integration.md), invitations in SharePoint are also subject to any [domain restrictions configured in Microsoft Entra ID](/azure/active-directory/b2b/allow-deny-list).

## Limiting domains

You can limit domains by allowing only the domains you specify or by allowing all domains except those you block.
  
### Limit domains at the organization level
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.
    
2. Under **More external sharing settings**, select the **Limit external sharing by domain** check box, and then select **Add domains**.
    
3. To create an allowlist (most restrictive), select **Allow only specific domains**; to block only the domains you specify, select **Block specific domains**.
    
4. List the domains (maximum of 5000) in the box provided, using the format  *domain.com.* If listing more than one domain, enter each domain on a new line.
    
    > [!NOTE]
    > Wildcards are not supported for domain entries.

5. Select **Save**.

You can also configure the organization-wide setting by using the [Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant) PowerShell cmdlet.

### Limit domains at the site level
  
You can also limit domains at the site level. Note the following considerations:
  
- In the case of conflicts, the organization-wide configuration takes precedence over the site configuration.
    
- If an organization-wide allowlist is already set up and you want to set up a site-level allowlist, then the site-level allowlist must be a subset of the organization's allowlist.
    
- If an organization-wide blocklist is already set up, then you can set up either an allowlist or a blocklist at the site collection level.
    
- For individual OneDrive site collections, you can only set up limit domains by using the [Set-SPOSite](/powershell/module/sharepoint-online/Set-SPOSite) Windows PowerShell cmdlet.
    
 **To limit domains for a site**

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.
    
2. Select the site name that you want to restrict domains to open the details panel.
 
3. On the panel, select the **Settings** tab and select **More sharing settings** under **External file sharing**.
    
4. Under **Advanced settings for external sharing**, select the **Limit external sharing by domain** check box, and then select **Add domains**.
    
5. Select **Allow only specific domains** to create an allowlist (most restrictive), or to block only the domains you specify, select **Block specific domains**.
    
6. List the domains (maximum of 500) in the box provided, using the format  *domain.com.* If listing more than one domain, enter each domain on a new line.
    
    > [!NOTE]
    > Wildcards are not supported for domain entries.

7. Select **Save**, and then select **Save** again.  

    > [!NOTE]
    > To configure the site collection setting for site collections that do not appear in this list (such as Group-connected sites or individual OneDrive site collections), you must use the [Set-SPOSite](/powershell/module/sharepoint-online/Set-SPOSite) PowerShell cmdlet.
  
## Sharing experience

After you limit sharing by domain, here's what you'll see when you share a document:
  
- **Sharing content with email domains that are not allowed.** If you attempt to share content with a guest whose email address domain isn't allowed, an error message will display and sharing will not be allowed.

    (If the user is already in your directory, you won't see the error, but they will be blocked if they attempt to access the site.)
    
    ![Screenshot of sharing error message when sharing with blocked user.](media/fb280460-388d-4596-9938-6b69101d11fb.png)

- **Sharing OneDrive files with guests on domains that aren't allowed.** If a user tries to share a OneDrive file with a guest whose email domain isn't allowed, an error message will display and sharing will not be allowed.

    ![Screenshot of error message when sharing OneDrive files with blocked users.](media/992f367d-1caa-4019-8fd8-af84c172319c.png)
  
- **Sharing content with email domains that are allowed.** Users will be able to successfully share the content with the guest. A tooltip will appear to let them know that the guest is outside of their organization.
    
    ![Screenshot of successfully sharing content with restricted users.](media/4e5ff064-a1d4-4a7d-bc7b-0541312e9383.png)
  
## User auditing and lifecycle management

As with any extranet sharing scenario it's important to consider the lifecycle of your guests, how to audit their activity, and eventually how to archive the site. See [Planning SharePoint business-to-business (B2B) extranet sites](./create-b2b-extranet.md) for more information.
  
## See also

[External sharing overview](external-sharing-overview.md)
  
[Extranet for Partners with Microsoft 365](create-b2b-extranet.md)
  
[Set-SPOTenant](/powershell/module/sharepoint-online/Set-SPOTenant)
