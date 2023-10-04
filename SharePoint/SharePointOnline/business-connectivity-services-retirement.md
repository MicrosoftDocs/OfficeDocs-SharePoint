---
ms.date: 10/04/2023
title: Business Connectivity Services (BCS) retirement in Microsoft 365
ms.reviewer: abloesch
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- MET150
ms.assetid: 2ced10aa-db9a-4828-a7a5-e47a57c3a823
description: Microsoft is announcing its plan to retire Business Connectivity Services (BCS) in Microsoft 365 and focus on Microsoft Power Apps as its replacement technology.
---

# Business Connectivity Services (BCS) retirement in Microsoft 365

SharePoint has a long history of helping users work with external data inside the SharePoint user experience, starting with the Business Data Catalog feature in SharePoint Server 2007. As SharePoint has evolved into a cloud-first service, so too have the options for customers who wish to integrate with external data sources. To simplify these options and provide the best experience for these scenarios going forward, Microsoft is announcing its plan to retire Business Connectivity Services (BCS) in Microsoft 365 and focus on Microsoft Power Apps as its replacement technology.

## Impacted features and scenarios

All Business Connectivity Services features will be retired in SharePoint in Microsoft 365. This includes features that such as:

- External lists
- External columns
- External content types
- Business Connectivity Services hybrid solutions

## Recommended replacement technology: Microsoft Power Apps

Microsoft encourages customers to explore using Power Apps to replace their Business Connectivity Services solutions in SharePoint in Microsoft 365. Although there's no direct migration from Business Connectivity Services to Power Apps, it supports a modern, cloud-first external data connectivity experience. Power Apps can integrate with various Microsoft 365 services and external data sources through its extensible connector technology, including SharePoint, Dynamics 365, SQL Server, and others. It also supports integrating with on-premises data sources through the on-premises data gateway.

To learn more about Power Apps, see the links in the [More information](#more-information) section.

## Retirement schedule

- October 2, 2023: Retirement announcement and customers can proactively set a property to block Business Connectivity Services features within their tenant.
- October 30, 2023: Microsoft will begin blocking Business Connectivity Services features based on the tenant property set by the customer.
- January 8, 2024: Microsoft will block Business Connectivity Services features in new Microsoft 365 tenants by default, and in tenants who haven't used the feature since October 30, 2023.
- September 30, 2024: Business Connectivity Services is fully retired in Microsoft 365.

### Blocking Business Connectivity Services features within your tenant

Starting today, customers can prepare for the Business Connectivity Services retirement by setting a property that will block this feature in their tenant. This will ensure that users within your tenant won't start using this feature if it isn't already in use.

Customers should only set this property once they've confirmed there's no business need to use the Business Connectivity Services features. Customers can confirm Business Connectivity Services usage by following these instructions:

1. Go to [**More features** in the SharePoint admin center](https://go.microsoft.com/fwlink/?linkid=2185077), and sign in with an account that has [admin permissions](sharepoint-admin-role.md) for your organization.
    > [!NOTE]
> If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/?linkid=850627), then browse to the SharePoint admin center and open the **More features** page.

2. Under **BCS**, select **Open**.
3. On the **BCS Home Page**, select **Manage BDC Models and External Content Types**.
4. In the **View** dropdown selector, select each of views including **BDC Models**, **External Systems**, and **External Content Types**. Confirm that no BDC models, external systems, or external content types have been added.
5. Return to the **BCS Home Page** and select **Manage connections to online services**.
6. Confirm that no connections have been added.
7. Return to the **BCS Home Page** and select **Manage connections to on-premises services**.
8. Confirm that no connections have been added.

To proceed with setting the property that will block this feature, tenant administrators can download and launch SharePoint Online Management Shell version 16.0.24120.12000 or higher and then run the following commands:

``Connect-SPOService -Url https://\<tenant\>-admin.sharepoint.com
 Set-SPOTenant -BusinessConnectivityServiceDisabled $true``

SharePoint in Microsoft 365 will begin blocking features based on this tenant property on October 30, 2023.

### Blocking Business Connectivity Services in new tenants by default

Starting January 8, 2024, Microsoft will block Business Connectivity Services in new tenants by default by automatically setting this property to true in those new tenants. In addition, Microsoft will also set this property to true on existing tenants who haven't used the Business Connectivity Services feature since October 30, 2023.

Customers who wish to re-enable Business Connectivity Services within their tenant may do so by setting this property to false as follows:

``
Connect-SPOService -Url https://\<tenant\>-admin.sharepoint.com
 Set-SPOTenant -BusinessConnectivityServiceDisabled $false
``

Note that re-enabling Business Connectivity Services in your tenant isn't recommended unless you have a specific need.

### Business Connectivity Services is retired in Microsoft 365

Starting September 30, 2024, Business Connectivity Services will be retired in Microsoft 365. Its features will no longer be available and can't be re-enabled through the ``Set-SPOTenant`` PowerShell cmdlet. This applies to all environments including Government Clouds and Department of Defense.

## Impact to SharePoint Server

This announcement has no impact on Business Connectivity Services in SharePoint Server.

This feature will remain supported in SharePoint Server 2016 and SharePoint Server 2019 until those products reach their end of support date of July 14, 2026.

Microsoft has no plans to retire Business Connectivity Services in SharePoint Server Subscription Edition at this time. Deprecation and removal announcements for SharePoint Server Subscription Edition are announced in the [What's deprecated or removed from SharePoint Server Subscription Edition](../SharePointServer/what-s-new/what-s-deprecated-or-removed-from-SharePoint-Server-Subscription-Edition.md) article.

## Summary

Microsoft remains committed to our customers' digital transformation by providing modern approaches to integrate with external data. By leveraging Power Apps as the platform for these scenarios, customers will gain modern capabilities not only in SharePoint, but in other Microsoft 365 services as well.

## More information

For more information about Power Apps and its integration capabilities with external data sources, see:

[What is Power Apps?](/power-apps/powerapps-overview)

[What is an on-premises data gateway?](/power-apps/maker/canvas-apps/gateway-reference)

[Scenarios for integrating SharePoint with Power Apps](/power-apps/maker/canvas-apps/sharepoint/scenarios-intro)

[Overview of connectors for canvas apps](/power-apps/maker/canvas-apps/connections-list)

Link to the announcement: [https://aka.ms/sp-bcs-retirement](https://aka.ms/sp-bcs-retirement)

Link to this support article: [https://aka.ms/sp-bcs-retirement-support](https://aka.ms/sp-bcs-retirement-support)