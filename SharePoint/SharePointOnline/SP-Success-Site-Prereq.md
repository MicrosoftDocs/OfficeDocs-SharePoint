---
title: "SharePoint Success Site Prerequisites"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- OSU150
- MET150
description: "SharePoint Success Site solution prerequisites."
---

# SharePoint Success Site Prerequisites

To successfully set up the SharePoint Success Site in your tenant you must install it using the SharePoint Online Provisioning Service. 

The person doing the provisioning must meet the following pre-requisites:


- The person provisioning the SharePoint Success Site must be a Tenant Administrator of the tenant, otherwise known as the Office 365 Global Administrator role, where the Success Site will be provisioned. If you are not sure if you have been assigned the Global Administrator role, please see our troubleshooting steps. 

- A tenant App Catalog must be available within the Apps option of the SharePoint Admin Center. If your organization does not have an SharePoint tenant App catalog, refer to the SharePoint Online documentation to create one. 

> [!Important]
>If you need to create an app catalog, wait at least 30 minutes after creating the Tenant App Catalog before provisioning the SharePoint Success Site. This ensures that the App Catalog provisioning process is complete within SharePoint.

- The person provisioning the SharePoint Success Site must be a Site Collection Owner of the Tenant App Catalog. If the person provisioning Custom Learning is not a Site Collection Owner of the App Catalog complete these instructions and continue.
