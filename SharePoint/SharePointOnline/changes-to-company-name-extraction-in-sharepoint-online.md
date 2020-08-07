---
title: "Changes to company name extraction in SharePoint"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/18/2019
audience: End User
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
description: "The Company Name Extraction option in SharePoint is being deprecated."
---

# Changes to company name extraction in SharePoint

As we continue to deliver new search experiences with Microsoft Search, we'll be making changes to some of the classic search experiences in Microsoft 365. Beginning on November 15, 2019, we'll remove Company Name Extraction from SharePoint. Company Name Extraction in SharePoint allows the search system to extract company names from content under a specific set of conditions using a pre-populated dictionary or using the Company Inclusions or Company Exclusions list. While company name extraction has become a relied-upon solution to derive one or more company names from content in SharePoint, both the dictionary and its underlying feature set have become obsolete.

![Screenshot of Search in SharePoint](media/spo-extraction-01.png)

### How do I know if company name extraction is enabled for a property?

If you configured company name extraction on a managed property, you will see it on the property configuration:

![Screenshot of Company Extraction option in SharePoint](media/spo-extraction-02.png)

### What happens when company name extraction is deprecated?

If you configured company name extraction to be surfaced in the classic Enterprise Search Center as a refiner (see the previous illustration), the refiner is not populated with data over time. The CompanyName refiner will be empty when the deprecation is complete. The rest of the search experience is not impacted. The Company Inclusions and Exclusions lists configured in the Term Store Management Tool will not be removed.

For developers and custom solutions, third-party applications using the SharePoint REST/CSOM API will not have the CompanyName refiner returned in the results. Any other refiners and query features will continue to work.

### Are there alternatives to company name extraction?

If company name extraction is required for your organization or solutions your organization uses, you can try the following alternatives:

Set the managed property that contains the content from which you previously extracted company names to 'searchable.' This will include the contents of the managed property in the full-text index, enabling users to query against it.

- Example: If the property is "VendorHistory", a simple query for "Contoso" returns items that contain the word "Contoso" and items whose VendorHistory property contains "Contoso".

Set the managed property that contains the content from which you previously extracted company names to 'queryable.' This will enable querying against the specific managed property by including the property name in the query.

- Example: If the property is "VendorHistory", a query containing "VendorHistory: Contoso" returns items whose VendorHistory property contains "Contoso".

### Does this affect SharePoint on-premises?

No. SharePoint on-premises versions are not affected by this change.

Learn more about Microsoft Search at https://aka.ms/microsoftsearch.
