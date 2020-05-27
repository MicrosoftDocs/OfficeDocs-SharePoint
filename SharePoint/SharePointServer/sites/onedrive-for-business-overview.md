---
title: "Overview of OneDrive in SharePoint Server"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 7/24/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 56a95840-704c-4aa0-9d37-078e7ab4f83c
description: "Learn about OneDrive in SharePoint Server."
---

# Overview of Microsoft OneDrive in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
> [!NOTE]
> While OneDrive is used in both SharePoint Server on-premises and Microsoft 365 environments, this article describes how it works in SharePoint Server. For more information about how it works in a Microsoft 365 environment, see [What is OneDrive?](https://go.microsoft.com/fwlink/?LinkId=747076). 
  
Microsoft OneDrive is the default document library in a user's [What's new in social computing in SharePoint Server 2013](/sharepoint/what-s-new/what-s-new#MySites) in SharePoint Server or in Microsoft 365. The contents of this library can optionally be synchronized with one or more of the user's computers or devices. 
  
By using OneDrive, you can help ensure that business files for your users are stored in a central location. Storing business files in one location makes it easy for users to share and collaborate on documents. If you're using OneDrive, you can also reduce your on-premises storage costs by moving your users' files to the cloud.
  
OneDrive is different from the consumer OneDrive service in that OneDrive is based on SharePoint and is meant for storing a user's business documents and files. Consumer OneDrive is a separate service that is meant for personal use.
  
## Why use OneDrive in a SharePoint Server on-premises environment?

While OneDrive may serve as an optimal storage solution for many businesses, some businesses may be restricted from saving their company data to the cloud for various reason, including:
  
- Business rules that prohibit transmitting data over the internet
    
- Industry rules
    
- Compliance standards
    
Additionally, your environment may require your IT-staff to have strict control on updates that are applied in your environment. One of the reasons may be that you have specialized third-party applications or customization that have only been tested to work with specific versions of a product or service. 
  
For these types of customers, OneDrive can be implemented in a SharePoint Server on-premises environment, providing your business users with the sync and storage features provided by OneDrive, but keeping all of your data within your on-premises environment. 
  
Additionally, updates to SharePoint Server and the services run on it (such as OneDrive) are controlled internally by you. 
  
## How does it work?

In SharePoint Server, OneDrive is simply the document library in a user's MySite. This provides personal storage for your users, either directly through the document library in their My Site, or as a save location in Office 2013 or Office 2016. While OneDrive files are saved to the cloud, in OneDrive in a SharePoint Server on-premises environment, user files are stored in the SharePoint Content database in the SQL Server that you are using for SharePoint Server. User storage quotas are set through site settings for the web application that is hosting the My Site host site.
  
![OneDrive in SharePoint Server 2013 on-premises](../media/17d99a5e-4b0b-42a6-ac17-0118efdf56df.jpg)
  
## Synchronizing files

To synchronize OneDrive files, you need to use a sync app. Sync apps automatically [synchronize files between OneDrive and a user's computer](https://go.microsoft.com/fwlink/?LinkId=288863) or a mobile device. They are available for [a variety of operating systems and mobile devices](https://go.microsoft.com/fwlink/?LinkId=522308). The OneDrive Windows sync app is also included as part of an Office installation.
  
When you're using OneDrive in SharePoint Server, you can synchronize your files to a variety of devices, but those devices need to be connected to the network where SharePoint Server resides in order for the sync to work. Synchronizing is mostly useful for laptops that are used while disconnected from your corporate network at times, such as when traveling. This differs from usingOneDrive, in which an Internet connection is required since files are synchronized from your users device to Microsoft 365 instead of to an on-premises location in your network.
  
## OneDrive hybrid

If you use SharePoint Server and want to take advantage of cloud storage for your users' business documents, you can set up OneDrive and have your users automatically redirected to Microsoft 365 when they select the OneDrive link in SharePoint Server.
  
By using Microsoft 365 for document storage, you can take advantage of cloud storage without having to migrate all of your workloads to Microsoft 365.
  
Setting up OneDrive hybrid requires [configuring Microsoft 365](https://go.microsoft.com/fwlink/?LinkID=521431) if you haven't already, and configuring your OneDrive in your SharePoint Server environment to "redirect" to OneDrive. For info about planning OneDrive hybrid, see [Configure hybrid OneDrive - roadmap](../hybrid/configure-hybrid-onedrive-for-businessroadmap.md).
  
## Getting started

Setting up OneDrive in SharePoint Server requires configuring a User Profile Service application and setting up My Sites. For detailed planning information, see [Plan for OneDrive in SharePoint Server](onedrive-for-business-planning.md).
  
For more information about syncing OneDrive files in SharePoint Server 2016 or 2013, see [Sync SharePoint files with the OneDrive sync app (Groove.exe)](https://support.office.com/article/59b1de2b-519e-4d3a-8f45-51647cf291cd).
  

