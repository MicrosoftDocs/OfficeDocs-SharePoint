---
title: "Sensitivity labels Migration API"
ms.date: 01/08/2021
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
search.appverid: MET150
description: "Best practices for applying sensitivity labels when using the Migration API."
localization_priority: Priority
ms.service: sharepoint-online
---

# Applying Sensitivity Labels before using the Migration API

If you want to have senstivity labels applied to content you are migrating to Microsoft 365, it must be done before running the Migration API. There is currently not a parameter in the API to apply sensitivity labels on files.

At this time, the only label you can apply to files in the Migration API are compliance labels.

**Step 1:**  
Before you migrate your content with the Migration API, become familiar with how sensitivity labels work in Microsoft 365 and learn about the Microsoft Information Protection (MIP) SDK:

- [Enable senstivity labels for Offices files in SharePoint and OneDrive](https://docs.microsoft.com/en-us/microsoft-365/compliance/sensitivity-labels-sharepoint-onedrive-files?view=o365-worldwide)

- [Microsoft Information Protection SDK](https://docs.microsoft.com/information-protection/develop/overview)

**Step 2:**  
Download and configure the Microsoft Information Protection (MIP) SDK. 

- Download: [Microsoft Information Projection (MIP) SDK](https://docs.microsoft.com/en-us/information-protection/develop/setup-configure-mip) 


**Step 3:** 
Apply sensitivity labels using the MIP SDK. 
 
If you're currently using Azure Information Protection, you must migrate your labels to Office 365 Security and Compliance Center. For more information on the process, see [How to migrate Azure Information Protection labels to the Office 365 Security & Compliance Center](https://docs.microsoft.com/azure/information-protection/configure-policy-migrate-labels).  

**Step 4:** Migrate content using the [SharePoint Migration API](https://docs.microsoft.com/sharepoint/dev/apis/migration-api-overview)
