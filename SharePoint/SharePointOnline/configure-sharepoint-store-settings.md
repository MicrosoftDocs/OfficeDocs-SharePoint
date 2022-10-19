---
title: "Configure settings for the SharePoint Store"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.collection: M365-collaboration
ms.custom: admindeeplinkSPO
ms.localizationpriority: medium
search.appverid:
- SPO160
- MET150
ms.assetid: 6b806fb8-9295-441d-b954-07009021dc48
description: "Learn how to allow or prevent users from getting apps from the SharePoint Store, and how to manage app requests."
---

# Configure settings for the SharePoint Store

The [SharePoint Store](https://appsource.microsoft.com/marketplace/apps?product=sharepoint) is a public marketplace that offers apps for Microsoft 365, as well as Dynamics 365 and Power Platform. Site users can access the SharePoint Store directly from a SharePoint site to browse for and add third-party apps. If a SharePoint environment has been configured to prevent users from getting apps from the SharePoint Store, users can still browse for and request apps. These requests are added to the App Requests list in the SharePoint admin center.

## Specify whether users can get apps from the SharePoint Store

By default, SharePoint is configured to allow users to get or request apps from the SharePoint Store. The option to change this setting will not be enabled if you have not yet created an Apps site. For information about how to create an Apps site, see [Use the Apps site to make custom business apps available for your SharePoint environment](use-app-catalog.md).
  
Even if you choose not to allow users to add apps from the SharePoint Store, they will still be able to browse the SharePoint Store and request apps.
  
1. Go to the [More features page of the SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true), and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

1. Under **Apps**, select **Open**, and then select **More features**.

1. Select **Configure store settings**.
    
1. Next to **App Purchases**, do one of the following:
    
   - If you want users to be able to add apps, select **Yes**.
    
   - If you do not want users to be able to get third-party apps, select **No**. 

## Specify whether to allow apps for Office to start in documents
<a name="__top"> </a>

Documents stored on sites may contain apps for Office from several sources. You can specify whether or not you want to allow these apps to work when documents are opened in the browser.
  
1. Go to the [More features page of the SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true), and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

   > [!NOTE]
   > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

1. Under **Apps**, select **Open**, and then select **More features**.

1. Select **Configure store settings**.

1. Next to **Apps for Office from the Store**, do one of the following:
    
   - If you want to allow apps for Office to start when documents are opened in the browser, select **Yes**. 
    
   - If you do not want to allow apps for Office to start when documents are opened in the browser, select **No**.

## Related topics

[Add an app to a site](https://support.office.com/article/dd98e50e-d3db-4ecb-9bb7-82b189822d43)

[Office Store and SharePoint Store Terms of Use](https://support.office.com/article/64c7f343-16b5-40bb-b39f-66c9d1c4d405)
