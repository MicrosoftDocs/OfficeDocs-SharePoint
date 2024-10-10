---
ms.date: 10/11/2024
title: Plan for SharePoint storage
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: concept-article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
- essentials-get-started
ms.custom: intro-get-started
search.appverid: MET150
description: Plan SharePoint storage for your organization.
---

# SharePoint storage planning 

SharePoint is the most trusted and flexible platform for your content, providing enterprise-grade security and compliance tooling, built-in high availability and disaster recovery, point in time restore, and much more. Depending on your business scenarios, it's important that you plan your content storage strategy to maximize user value and to optimize storage costs. This article highlights ways to gather data for insights into storage usage, tools to help manage or reduce storage footprint of less valuable content, and premium offerings for a richer experience.  

## Understand storage drivers  
As storage grows over time, it's important to understand what drives storage growth and identify the areas that could need your attention. There are options to review storage trends, ranging from usage reports in the Microsoft 365 admin center, which provide easy-to-consume visuals, to rich datasets available through Microsoft Graph Data Connect (MGDC). 

- Leverage [SharePoint site usage reports](/microsoft-365/admin/activity-reports/sharepoint-site-usage-ww) to review storage trends, such as usage by sites and active file count. There might be a 48-hour data latency in the usage reports. Note that the M365 admin center usage reports show usage across all geo locations while the SharePoint admin center usage values are geo location specific.  

- Use [SharePoint dataset from Microsoft Graph Data connect](https://aka.ms/SharePointData) to analyze site lifecycle, ownership, and storage used by SharePoint sites and OneDrive accounts. Answer questions such as which type of site uses the most storage, how much storage is used by previous versions, and how many sites haven’t changed in the past year. File level data is also available now through the [SharePoint Files dataset.](https://techcommunity.microsoft.com/t5/microsoft-graph-data-connect-for/update-on-the-sharepoint-files-dataset/ba-p/4189538)<sup>**(*)**</sup> 

## Set up storage configurations  
Configure the site storage limits, version history limits, and retention policies that would meet your organization’s needs. Whether that’s automatic limits for simplicity or custom limits for maximum control, setting up these limits is fundamental for storage management.  

- Set [site storage limits](/sharepoint/manage-site-collection-storage-limits) to Automatic, to simplify site storage management, or Manual for custom limits. Site limits cap the allocation of pooled tenant storage resources among sites within the organization.  

- Update [organization version history limits](https://aka.ms/versioning-overview) to Automatic for optimal version restore and storage.  

- Review [retention policies for SharePoint](/purview/retention-policies-sharepoint) to manage compliance requirements with storage use. 

## Optimize storage usage 
Increase available storage by cleaning up low-value versions and inactive sites, or by moving inactive content to a lower cost archive storage solution. 

- Archive inactive content to reduce active storage costs using [Microsoft 365 Archive.](https://aka.ms/M365Archive) 

- [Trim existing low-value versions](/sharepoint/trim-versions) to reduce storage.  

- Recover storage from deleted items by [emptying site recycle bin](https://support.microsoft.com/en-us/office/delete-items-or-empty-the-recycle-bin-of-a-sharepoint-site-2e713599-d13e-40d6-96dc-66f0a366f74e).  

- Leverage [retention settings](/purview/retention-policies-sharepoint) to automatically delete files after a specified period.  

- Manage site lifecycle policies through [SharePoint Advanced Management](/sharepoint/advanced-management). Set up an [inactive site policy](/sharepoint/site-lifecycle-management) to automatically detect inactive sites and send notifications to site owners via email. <sup>**(*)**</sup> 


## Purchase additional storage  
To increase SharePoint storage capacity, purchase additional storage in one-gigabyte increments or acquire more SharePoint licenses.  

- Purchase [additional storage](https://www.microsoft.com/en-us/microsoft-365/onedrive/additional-file-storage) at a cost per gigabyte (GB) per month.<sup>**(*)**</sup>  

- Purchase additional SharePoint licenses, adding 10 GB per license to the storage limit.<sup>**(*)**</sup>  

<sup>**(*)**</sup>: Additional licensing/charges might apply

## FAQs 

1. How is the SharePoint storage quota calculated?  
SharePoint storage quota for the tenant starts at 1 TB and each additional SharePoint license purchased adds 10 GB. For details, see [SharePoint limits - Service Descriptions | Microsoft Learn.](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits)   

1. What happens if my tenant exceeds the SharePoint storage quota?  
When the SharePoint storage quota is exceeded, you might need to purchase additional storage or manage existing storage more efficiently through deletion or archival. In addition, classic site creation is blocked.  

1. How does version trimming work with the preservation hold library?  
Version trimming doesn't impact the files in the preservation hold library since the original copies of the files are preserved. For more on how retention settings work in SharePoint, see [Learn about retention for SharePoint and OneDrive | Microsoft Learn.](/purview/retention-policies-sharepoint)  

## Related articles 
- Microsoft 365 Archive – cold tier SharePoint storage ideal for inactive content; learn more at [aka.ms/M365 Archive](https://aka.ms/M365Archive) 

- Enhanced version controls – right version limits to optimize for recovery and storage costs; learn more at [aka.ms/versioning-overview ](https://aka.ms/versioning-overview)

- Sites content lifecycle management – manage inactive sites across your tenant to optimize storage; learn more at [aka.ms/LearnSAM ](https://aka.ms/LearnSAM)

- Microsoft Graph Data Connect for SharePoint – rich datasets to understand your SharePoint storage trends; learn more at [aka.ms/SharePointData](https://aka.ms/SharePointData) 