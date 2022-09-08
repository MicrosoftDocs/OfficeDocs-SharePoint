---
title: "Introducing feature updates
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 06/20/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn about the feature release rings."
---


# Introducing feature updates

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

Organizations often desire predictability for when new features are introduced to the products they use. To ensure we're meeting those needs, Microsoft will bundle new feature experiences for SharePoint Server Subscription Edition together in Feature Updates, so that they can be introduced on a predictable schedule. 

As Microsoft delivers on its promise of an evergreen experience for SharePoint Server Subscription Edition, we recognize that organizations desire the ability to manage the introduction of new feature experiences into their environments. To meet this need, new feature experiences introduced in SharePoint Server Subscription Edition Version 22H2 will be grouped into feature release rings.
 
The two rings in this version are as follows: 

- Early release

- Standard release

## Early release

In the **Early release** ring, new feature experiences will be enabled in your SharePoint farm as soon as they're ready. These experiences are supported for production use but may change before they're included in the Standard release ring. Enable **Early release** to:

- Use new feature experiences in a production environment as soon as possible.
- Perform compatibility testing and explore new feature experiences in a test environment and provide feedback to Microsoft.
- Prepare your internal help desk and user documentation for new feature experiences.

## Standard release

In the **Standard release** ring, new feature experiences are enabled in your SharePoint farm once they're ready for all customers to use by default. These feature experiences are supported for production use and have received additional validation during **Early release**. Enable **Standard release** if you prefer to minimize changes to your SharePoint experience and are willing to wait longer for new feature experiences. **Standard release** is the default feature release ring.


## Selecting feature release preference

Customers can switch between these two feature release rings at any time. However, you must run the SharePoint Products Configuration Wizard on every server in your SharePoint farm after changing this setting. The Wizard will perform a repair operation to ensure all features recognize the new setting.

Following are the steps to select a feature release preference for your SharePoint farm: 

1. Browse to **SharePoint Central Administration**.
2. Click **System Settings**.
3. Click **Feature release preference**, select either **Early release** or **Standard release (Default)**, and then click **OK**.

> [!NOTE]
> On each server in your SharePoint farm, run the **SharePoint Products Configuration Wizard** to ensure all features recognize the new feature release preference.
 
