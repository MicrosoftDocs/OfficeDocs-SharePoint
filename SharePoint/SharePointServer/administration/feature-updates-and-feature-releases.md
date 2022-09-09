---
title: "Feature updates and feature releases"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 09/08/2022
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: 
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn about the feature release rings."
---


# Feature updates and feature releases

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

In previous versions of SharePoint Server, such as SharePoint Server 2019 and SharePoint Server 2016, new feature experiences were introduced at the launch of major new versions. Those versions would be serviced with new security and quality improvements via monthly Public Updates. On rare occasions, new feature experiences may be introduced via a Public Update as well. However, customers would typically have to wait for the next major version of SharePoint Server to be released to get additional feature experiences that weren’t part of the initial launch.

SharePoint Server Subscription Edition brings a more agile approach to how new feature experiences are introduced to SharePoint Server customers. Instead of waiting for the next major version of SharePoint Server to be released, new feature experiences will now be introduced to SharePoint Server Subscription Edition on a regular basis via Feature Updates. Customers will have access to these new feature experiences as soon as they're ready and will have control over how they're made available in their SharePoint farm deployments.

## Introducing feature updates

In addition to the desire for predictability of new feature releases, organizations desire the ability to manage the introduction of those new features into their environments. This gives organizations time to train their users and support staff on any new functionality, perform compatibility testing of those new feature experiences with existing customer scenarios, and develop new business processes to take full advantage of the new feature experiences. 

To meet this need, new feature experiences introduced in feature Updates will be grouped into feature release rings:  

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
 
