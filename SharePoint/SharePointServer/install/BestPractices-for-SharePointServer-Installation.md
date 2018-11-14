---
title: "Best Practices for SharePoint Server Installation"
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
description: "Learn the best practices for SharePoint Server installation and how it will get your servers ready for easy transition to the cloud."
---

# Best practices for installation for SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 

## Introduction

Installing a new version gives the opportunity to review what you have done in the past, currently and envision your goals going forward.

As you prepare for your installation, consider the following:

•	Are you staying on Server (on-premises) for the foreseeable future?  

•	Do you currently have existing pieces of your system in the cloud?

•	What customizations or features do you no longer use?

•	Are you ready for a modern approach?

 •	What is working well now, and what isn’t?


## Evaluating what features or services are no longer supported

As you install a new version of SharePoint Server, take time to evaluate any service applications or features that you currently rely on that are no longer supported or listed as “deprecated”. 

If you have a reliance on any of the following, plan what you intend to replace that functionality with or if it is no longer being used actively by your company and it is time to phase it out.

Use supported service applications and consider phasing out the use of these deprecated service applications:


|**Deprecated feature or service**|**Recommended replacement**|
|:-----|:-----|
|Access Services and Access Services 2010 |Power BI |
|Document Conversions services|No Replacement |
|Lotus Notes Connector  |No Replacement |
|Machine Translation Services | |
|PerformancePoint Service |Power BI |
|PowerPoint Conversion Service | No Replacement|
|Visio Graphics Service  ||
|Word Automation Services  |No Replacement |
|InfoPath |Microsoft Forms or PowerApps |
|Workflow Manager |Microsoft Flow or SharePoint 2010 workflows|

## Customizations

If you currently have SharePoint Server installed, chances are you have made some customizations to suit your business needs. 

If you already have a portion of your company in the cloud or plan to do so in the future, know that certain customizations will not transfer to SharePoint Online.  Here is a list of few of those:

•	Workflows, User Alerts, and custom master pages will not transfer to SharePoint Online. We recommend you use Microsoft Flow for workflows, reconfigure alerts once migrated, and use the out of the box customization for site look and feel changes.

•	Custom Search schema will not transfer to SharePoint Online. When content is migrated to SharePoint Online, you may want to re-implement any custom Search schema configuration necessary.

•	Use SharePoint Add-ins with the Low Trust model.  To learn more, see [Creating SharePoint add in that use low trust authorization](https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/creating-sharepoint-add-ins-that-use-low-trust-authorization).

•	Use SharePoint Framework solutions for custom business solutions.  To get started, see [SharePoint Framework Overview](https://docs.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview).

## Connect your data the modern way

Do you use Business Data Connectivity Services (BCS) for any of your data connections?  Are your data sources available by using a web service? verify all data sources are available via other means, such as a web service.

•	Where is your data? Where will it reside?

Instead of using BCS to display your data, you could use PowerBI and a Data Management Gateway.

## Adopt the modern features 

If a portion of your sites are already in the cloud, or if you intend on moving online in the future, adopting the modern features now will help “futureproof” your installation.

•	Use Office 365 Groups and Microsoft Flow.   Retire the use of email, Site mailboxes, or Mobile Accounts (SMS/Text Messaging)

•	Solutions that intercept and/or modify the HTTP pipeline you could use Azure Conditional Access Policies by fronting the farm by using the Azure AD App Proxy. For more information on how to use AD FS, see [Access Control Policies in Windows Server 2016 AD FS](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/access-control-policies-in-ad-fs).

•	Implement only the necessary Web Application Policies, such as self-service site creation, Object Cache, and Search Crawler accounts, but try to avoid further usage of Web Application Policies as they are not available in SharePoint Online.

•	For security purposes, phase out the use of anonymous SharePoint Server sites.  Also note that anonymous site access is not available in SharePoint Online. 
