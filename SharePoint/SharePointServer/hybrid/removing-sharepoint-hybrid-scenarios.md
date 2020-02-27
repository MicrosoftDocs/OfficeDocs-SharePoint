---
title: "Remove SharePoint Server hybrid scenarios"
ms.reviewer: troys
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- M365-collaboration
description: "Removing SharePoint hybrid scenarios in SharePoint Server"
---

# Removing SharePoint hybrid scenarios

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

This guide will walk you through removing SharePoint Hybrid functionality from your SharePoint farm.

## Cloud Hybrid Search

Cloud Hybrid Search may be removed by deleting the Search Service Application.

1. In Central Administration, click **Application Management**.
2. In the Application Management page, click **Manage service applications**.
3. In the Service Application page, highlight your Cloud Hybrid Search Service Application. The name of the Service Application may vary, but the **Type** will be **Search Service Application**.

> [!NOTE]
> The **Type** is identical to the standard SharePoint Search Service Application.

4. In the ribbon, click **Delete**.
5. You may then create a new non-Cloud Search Service Application. See the SharePoint Server documentation on [Search](https://docs.microsoft.com/sharepoint/search/search) for information on how to create and manage your Search Service Application.

## OneDrive and sites

Once you have configured OneDrive for Business and Sites hybrid, you can manage it in the SharePoint Central Administration website.

1. In Central Administration, click **Office 365**.
2. On the Office 365 page, click **Configure hybrid OneDrive and Sites features**.
3. On the Configure hybrid OneDrive and Sites features page, under the **Select hybrid features**, click **None** and then the **OK** button.

Setting the option to **None** will also remove the Hybrid app launcher feature.

## SharePoint hybrid taxonomy and hybrid content types

See [Stopping replication of taxonomy groups](https://docs.microsoft.com/sharepoint/hybrid/configure-hybrid-sharepoint-taxonomy-and-hybrid-content-types#stopping-replication-of-taxonomy-groups).

## Hybrid self-service site creation

See [Manage hybrid self-service site creation](https://docs.microsoft.com/sharepoint/hybrid/hybrid-self-service-site-creation#manage-hybrid-self-service-site-creation).

## Removing the Azure Access Control Service Application Proxy and SharePoint Online Application Principal Management Service Application Proxy

The final step to removing hybrid is to delete the **Azure Access Control Service Application Proxy** and **SharePoint Online Application Principal Management Service Application Proxy** created by the hybrid picker.

1. In Central Administration, click **Application Management**.
2. In the Application Management page, click **Manage service applications**.
3. In the Service Applications page, highlight the Service Application named **ACS**. In the ribbon, click **Delete**.
4. In the Service Applications page, highlight the Service Application named **SPO App Management Proxy**. In the ribbon, click **Delete**.
5. Perform an iisreset on all SharePoint Servers in the farm.
