---
title: "Configure Business Connectivity Services solutions for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: f255d39a-8231-42e7-957d-c4855b9ab529
description: "Find links to steps that will help you install and configure SharePoint Server Business Connectivity Services (BCS). Choose from on-premises, cloud-only, and hybrid BCS solutions."
---

# Configure Business Connectivity Services solutions for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article is your starting place for the procedures to install common Microsoft Business Connectivity Services scenarios for SharePoint Server 2016. The Business Connectivity Services solution that you deploy will most likely look different from the solutions presented here, but you can model your installation on these examples. Also, you can select the individual procedures from here to build your own procedural documents for your Business Connectivity Services solution scenario.
  
## Choose the Business Connectivity Services scenario that meets your needs

Every Business Connectivity Services solution is unique because each business has unique data integration problems that it solves with Business Connectivity Services. The solutions can range from something simple and straightforward that a power user or IT professional (who has the appropriate permissions) can perform by themselves, to complex solutions that require developer, IT professional, and end-user solution development involvement.
  
This guide presents the configuration choices for the common scenarios.
  
- **[On-premises deployment](configure-business-connectivity-services-solutions.md#sectiononprem)** All the Business Connectivity Services components are under your organizations control behind your firewall. 
    
- **[Cloud-only deployment](configure-business-connectivity-services-solutions.md#sectioncloud)** All the Business Connectivity Services components are in SharePoint in Microsoft 365. 
    
- **[Hybrid deployment](configure-business-connectivity-services-solutions.md#sectionhybrid)** SharePoint in Microsoft 365 uses Business Connectivity Services to connect to data that lives in the cloud. 
    
## Prerequisites
<a name="s"> </a>

Before you begin with any Business Connectivity Services scenario configuration, make sure that you have read [Overview of Business Connectivity Services in SharePoint Server](business-connectivity-services-overview.md) and completed the steps in [Plan a Business Connectivity Services solution in SharePoint Server](plan-a-business-connectivity-services-solution.md).
  
## On-premises deployment
<a name="sectiononprem"> </a>

The procedures in [Deploy a Business Connectivity Services on-premises solution in SharePoint Server](deploy-an-on-premises-solution.md) show you how to deploy a solution that involves the following: 
  
- A Business Connectivity Services infrastructure that is on your corporate network.
    
- Information workers who access the Business Connectivity Services solution are on your corporate network.
    
- External content that is surfaced in SharePoint as an external list.
    
- External content that is synchronized into Microsoft Outlook for offline use.
    
- Accessing external data that is in SQL Server database on your corporate network.
    
- SharePoint Designer 2013 to create the external content type for the SQL Server data source.
    
- The Secure Store Service to manage mapping of user credentials to group credentials for accessing the external systems.
    
## Cloud-only deployment
<a name="sectioncloud"> </a>

The procedures in [Make an External List from a SQL Azure table with Business Connectivity Services and Secure Store](/sharepoint/make-external-list)[Deploy a Business Connectivity Services cloud-only solution in SharePoint 2013](/SharePoint/administration/deploy-an-on-premises-solution) show you how to deploy a solution that involves a Business Connectivity Services infrastructure that is in SharePoint in Microsoft 365. 
  
## Hybrid deployment
<a name="sectionhybrid"> </a>

The procedures in [Deploy a Business Connectivity Services hybrid solution in SharePoint](../hybrid/deploy-a-business-connectivity-services-hybrid-solution.md) shows you how to publish on-premises data to an external list or app for SharePoint in Microsoft 365. 
  
## See also

