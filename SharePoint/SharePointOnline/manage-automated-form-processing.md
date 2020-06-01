---
title: "Manage automated form processing"
ms.reviewer: ssquires
ms.author: toresing
author: tomresing
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: 0d84b4ce-a1d4-4e58-9ff0-eda67f96d332
description: "Admins control the visibility of form processing in SharePoint document libaries through the admin center."
ROBOTS: NOINDEX, NOFOLLOW
---

# Manage automated form processing

Admins can show or hide [automated form processing options in SharePoint document libaries](https://support.office.com/article/form-processing-in-sharepoint-cecf236f-224d-4630-9082-b5c79e0cd59a) through the admin center. 

* During private preview, the menu options will either show in all libraries or none.
* The options are shown in the **Automate** menu under the heading **[AI Builder](https://docs.microsoft.com/ai-builder/overview)**.
* Creating a [form processing AI model](https://docs.microsoft.com/ai-builder/form-processing-model-overview) from SharePoint applies the model to the library it was created in. 
  * When the model is applied, a [Power Automate](https://docs.microsoft.com/power-automate/getting-started) flow is created that is triggered when new files are added to the library.
  * The flow will extract information from files that match the model. 
  * The information will be available in the values of the columns in the library. 
* The [default environment for the Power Platform](https://docs.microsoft.com/power-platform/admin/environments-overview#the-default-environment) will be used for all form processing models built through these options.
