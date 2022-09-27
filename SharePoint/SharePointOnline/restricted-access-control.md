---
title: "Restricted Access Control"
ms.reviewer: 
manager: serdars
recommendations: 
ms.author: mactra
author: its-mactra
ms.date: 09/30/2022
audience: Admin
f1.keywords:
- NOCSH 
ms.topic: conceptual
ms.service: sharepoint-online
ms.localizationpriority: 
ms.collection:  
search.appverid:
ms.assetid: TBD
description: "Enable restricted access control for SharePoint sites through Microsoft 365 Group Membership"
---
# Restricted Access Control for SharePoint sites

Use Restricted Access Control to allow only users in a specified Microsoft 365 group to access a SharePoint site. This setting enforces a label policy and provides newly-added flags to reduce the risk of oversharing sites throughout your organization.

Even if other users outside of the Microsoft 365 group have received sharing links for the site or its content, they won’t have access to the content unless they are members of the Microsoft 365 group connected to the site.

## Prerequisites

Two important things to keep in mind are:

1. To use this feature, your organization must first have the following subscription:

    - SharePoint Advanced Management

2. Restricted Access Control can only be applied to SharePoint sites connected to Microsoft 365 groups.

## How to enable restricted access control in your organization

SharePoint Administrators or Global Administrators can enable restricted access control feature in your organization at the tenant-level or site-level by following these steps:

1. [Download](https://go.microsoft.com/fwlink/p/?LinkId=255251) and install the latest version of SharePoint Online Management Shell.

2. Connect to SharePoint Online as a Global Administrator or [SharePoint Administrator](sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://learn.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. To enable restricted access control in SharePoint, run the following command:

    ```PowerShell
    Set-SPOTenant -EnableRestrictedAccessControl $true
    ```

4. After you've enabled restricted access control for SharePoint in your organization, wait for approximately 1 hour before managing restricted site access for a specific Microsoft 365 group connected site.

    > [!NOTE]
    > If you have Microsoft 365 Multi-Geo, you must run this command for each of your geo-locations.

## View and manage restricted access for site

SharePoint Administrators or Global Administrators can view and manage restricted access control on a Microsoft 365 group connected site as follows:

1. Connect to SharePoint Online as a Global Administrator or [SharePoint Administrator](sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](https://learn.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

2. To apply restricted access control on a Microsoft 365 group connected site, run the following command:

    ```PowerShell
    Set-SPOSite -siteurl<> -RestrictedAccessControl $true
    ```

    **For example:**

    ```powershell
    Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite -RestrictedAccessControl $true
    ```

    > [!NOTE]
    > Users who aren't members of the Microsoft 365 group connected to the site will see an error message. Users who previously had access to site or its content but currently are not members of the Microsoft 365 group, will lose access to the site and see an error message.

3. To view restricted access control configuration for a site, run the following command:

    ```Powershell
    Get-SPOSite –Identity <siteurl> | Select RestrictedAccessControl
    ```

4. To remove restricted access from a Microsoft 365 group connected site, run the following command:

    ```Powershell
    Set-SPOSite –Identify <siteurl> -RestrictedAccessControl $false
    ```

    **For example:**

    ```Powershell
    Set-SPOSite -Identity https://contoso.sharepoint.com/sites/ResearchTeamSite-RestrictedAccessControl $false
    ```

### Example scenario on how to use restricted access control

The following example illustrates using restricted access control for sites in an organization.

SharePoint site for Research team has content which should only be accessed by the Research group users. No user outside of the research group should be able to access any content on this site.

With the restricted access control policy, the SharePoint admin can restrict the access of the site and its content only to the members of Microsoft 365 group connected to the site. Users who are not added in the Microsoft 365 group, even if they previously had site access permissions will lose access.

Hence, the site access is guaranteed only to the members of the Microsoft 365 group members of the site.
