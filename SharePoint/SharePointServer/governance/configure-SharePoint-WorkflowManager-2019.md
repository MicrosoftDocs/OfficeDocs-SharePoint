---
title: "Overview of SharePoint Workflow Manager in SharePoint Servers 2016 and 2019 Public Preview"
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
description: "Summary: Learn the steps to set up and configure eDiscovery in SharePoint Server 2013, SharePoint Server 2016, Exchange Server 2016, and Exchange Server 2013."
---

# Configure eDiscovery in SharePoint Server

 **Summary:** Learn the features and steps to configure SharePoint Workflow Manager in SharePoint Server 2019 Public Preview.
  
This article gives a brief overview of the new version of Workflow Manager and the steps that are required to configure Workflow Manager in SharePoint Server 2019 Public Preview. 

## Overview

SharePoint Workflow Manager is a new product that is designed to support running and managing SharePoint 2013 workflows in on-premises deployments. It replaces Microsoft Workflow Manager and is designed to be used with any version of SharePoint Server that supports SharePoint 2013 workflows, including SharePoint Server 2013, 2016 and 2019 Public Preview.

## System Requirements

The following table describes the system requirements, supported databases, and hardware requirements to use the new SharePoint Workflow Manager. 

|**Supported Operating System**|**Supported databases**|**Hardware requirement**
|:-----|:-----|:-----|:-----
Windows Server 2016 <br/>|Microsoft SQL Server 2014 or higher <br/> | Minimum RAM- 2 gigabytes (GB) <br/> Minimum Processor- 2 GHz dual core processor <br/>Minimum hard disk space- 1 GB

## Features

SharePoint Workflow Manager includes all features and fixes found in Microsoft Workflow Manager 1.0, Cumulative Update 5 (CU5). For a list of fixes in CU5, see [Description of the Cumulative Update 5 for Workflow Manager 1.0 ](https://support.microsoft.com/en-us/help/4055730/description-of-the-cumulative-update-5-for-workflow-manager-1-0).

Some additional features in this release are the following: 

- Support for SharePoint Server 2019 Public Preview
- Fixed activity update issues (such as "duplicate closure")
- Improved database cleanup
- Performance improvements due to reduced SQL resource usage
- Numerous performance and reliability improvements


## Install Instructions

1. From Web PI, install Microsoft Service Bus with TLS 1.2 .
2. Run "Workflow_Manager.msi" and follow the instructions on the      screen.
3. Run "WorkflowManagerClient_x64.msi" to install the Workflow Manager Client.
4. After the installer has completed, run the Workflow Manager Configuration Wizard from your Start menu and follow the instructions on the screen.

>[!NOTE]
>It is recommended that you install SharePoint Workflow Manager on a standalone computer. This version of the SharePoint Workflow Manager does not support upgrading an existing Workflow Manager that is already installed. 

Installation instructions for this version are the same as previous versions. For installation instructions on how Workflow Manager was installed on earlier versions of SharePoint Server and Workflow Manager, see [Install and configure workflow for SharePoint Server](https://docs.microsoft.com/en-us/SharePoint/governance/install-and-configure-workflow-for-sharepoint-server).




