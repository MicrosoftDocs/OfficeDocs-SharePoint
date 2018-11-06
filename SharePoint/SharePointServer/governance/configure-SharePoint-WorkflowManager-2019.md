---
title: "Overview of SharePoint Workflow Manager in SharePoint Servers 2016 and 2019"
ms.author: kirks
author: kirks
manager: pamgreen
ms.date: 7/24/2018
ms.audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 5cdce2aa-fa6e-4888-a34f-de61713f5096
description: "Learn the steps to set up and configure eDiscovery in SharePoint Server 2013, SharePoint Server 2016, Exchange Server 2016, and Exchange Server 2013."
---

# Configure SharePoint Workflow Manager for SharePoint Server

 **Summary:** Learn the features and steps to configure SharePoint Workflow Manager in SharePoint Server 2019.

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article gives a brief overview of the Workflow Manager and the steps that are required to configure Workflow Manager in SharePoint Server 2019. 

## Overview

SharePoint Workflow Manager is a new product that is designed to support running and managing SharePoint 2013 workflows in on-premises deployments. It replaces Microsoft Workflow Manager and is designed to be used with any version of SharePoint Server that supports SharePoint 2013 workflows, including SharePoint Server 2013, 2016 and 2019.

## System Requirements

The following table describes the system requirements, supported databases, and hardware requirements to use the SharePoint Workflow Manager. 

|**Supported Operating System**|**Supported databases**|**Hardware requirement**
|:-----|:-----|:-----|:-----
Windows Server 2016 <br/>|Microsoft SQL Server 2014 or higher <br/> | Minimum RAM- 2 gigabytes (GB) <br/> Minimum Processor- 2 GHz dual core processor <br/>Minimum hard disk space- 1 GB

## Features

SharePoint Workflow Manager includes all features and fixes found in Microsoft Workflow Manager 1.0, Cumulative Update 5 (CU5). For a list of fixes in CU5, see [Description of the Cumulative Update 5 for Workflow Manager 1.0 ](https://support.microsoft.com/en-us/help/4055730/description-of-the-cumulative-update-5-for-workflow-manager-1-0).

Some additional features in this release are the following: 

- Support for SharePoint Server 2019
- Fixed activity update issues (such as "duplicate closure")
- Improved database cleanup
- Performance improvements due to reduced SQL resource usage
- Numerous performance and reliability improvements


## Install Instructions

1. From Web PI, install SharePoint Workflow Manager. This will also install the needed Service Bus components.
2. After the installer has completed, run the Workflow Manager Configuration Wizard from your Start menu and follow the instructions on the screen.

>[!NOTE]
>It is recommended that you install SharePoint Workflow Manager on a standalone computer. This version of the SharePoint Workflow Manager does not support upgrading an existing Workflow Manager that is already installed. 

Configuration instructions for this version are the same as its predecessor Workflow Manager. For configuration instructions on  Workflow Manager for earlier versions of SharePoint Server, see [Install and configure workflow for SharePoint Server](https://docs.microsoft.com/en-us/SharePoint/governance/install-and-configure-workflow-for-sharepoint-server).




