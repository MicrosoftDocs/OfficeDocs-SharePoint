---
title: "Getting started with SharePoint Server workflow"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: cc73be76-a329-449f-90ab-86822b1c2ee8
description: "Learn about the two workflow platforms available in SharePoint Serverand the tools for working with them."
---

# Getting started with SharePoint Server workflow

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
SharePoint Server can use the workflow service built on the Windows Workflow Foundation. This service is called Workflow Manager and it is designed to play a central role in the enterprise. Processes are central to any organization and workflow is the orchestrator of processes. Workflow Manager integration was introduced with SharePoint Server 2013. SharePoint Server 2016 builds stability and reliability into this already proven workflow platform. The Workflow Manager platform continues to be called the SharePoint 2013 Workflow Platform and the traditional workflow platform continues to be called the SharePoint 2010 Workflow platform.
  
## Workflow development tools

There are several tools that come together to provide a rich workflow development experience. These include the following:
  
- SharePoint Designer 2013
    
- Visual Studio 2015
    
- A supported web browser such as Edge, Firefox, or Chrome
    
 **SharePoint Designer 2013**
  
The primary development tool for a SharePoint Server workflow is called SharePoint Designer 2013. SharePoint Designer 2013 provides a rich set of features specifically designed for workflow development against both the SharePoint 2010 Workflow platform and the SharePoint 2013 Workflow platform. You work with SharePoint Designer 2013 by opening it on your local computer and then connecting it to a SharePoint Server site. 
  
> [!TIP]
> SharePoint Designer 2013 can connect to any SharePoint Server site as long as you have permissions to that site and can access it over a network. For example, you might have SharePoint Designer 2013 installed on a computer in your home office and SharePoint Server might be installed on a server at your corporate data center. As long as you can connect to your site, you can use SharePoint Designer 2013 to develop workflows for it. 
  
 **Visual Studio 2015**
  
Visual Studio 2015 is used in many types of Microsoft development. You can use Visual Studio 2015 to develop workflows similar to SharePoint Designer 2013. However it can also be used to develop custom actions and tasks such as a workflow action that interacts with a custom application. 
  
SharePoint Server ships with a rich assortment of actions and tasks. If you need a very specific action, you can use Visual Studio 2015 to develop it. The custom action can then be used in SharePoint Designer 2013 by a workflow developer. 
  
 **Web browser**
  
A web browser, such as Edge, Firefox, or Chrome, is what you use to interact with SharePoint Server sites. For example, you can create lists and libraries, associate a workflow with a list and library, add items to a list or library, start a workflow on an item, and check the status of a workflow. 
  

