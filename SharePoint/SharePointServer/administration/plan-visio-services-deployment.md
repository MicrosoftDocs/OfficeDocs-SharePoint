---
title: "Plan Visio Services deployment in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 7705a9ef-cc59-4b08-990c-e88014b4ac03
description: "Best practices for deploying Visio Services include performance planning, using a pilot program, monitoring your deployment, and backing up your data."
---

# Plan Visio Services deployment in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
As an integrated part of SharePoint Server, Visio Services is very easy to deploy. Planning your Visio Services deployment before rollout can help give you the best system performance and user satisfaction, and it can help you better manage system resources in your SharePoint Server farm and related systems. 
  
## Visio Services performance

Visio Services is implemented by using the Visio Graphics Service, which runs on the Front-end server role in the farm. Like all such services, this service consumes resources such as processing capacity and memory on each server where the service is running.
  
System performance of application servers that are running the Visio Graphics Service may be affected by various factors such as the following:
  
- The size of the diagrams being rendered
    
- The number of diagrams connected to a data source
    
- The performance of the data sources to which diagrams are connected
    
- The frequency of data refresh for data-connected diagrams
    
- Peak loads of users who are accessing diagrams
    
- Peak loads on external data sources accessed by diagrams
    
- Complexity of diagrams
    
- Visio Services cache settings
    
The diagram size limit and refresh parameters can be adjusted by the administrator. Being able to adjust these parameters can help you adjust the performance of the server. If changing these parameters does not provide the desired performance, you may have to add processing capacity or memory.
  
When planning system resources for Visio Services, the most important factor is peak load. For example, if users will make heaviest use of the Visio Services functionality early Monday morning, plan your server capacity for that peak load. Peak load times can vary widely depending on how Visio Services is used within your organization. It is important to estimate peak loads as best as possible to avoid overtaxing system resources.
  
In addition to SharePoint Server performance considerations, you should also examine the performance impact of Visio Services on your other systems. For example, if you have a data-connected diagram that is querying data from an Oracle database, what is the effect of your Visio Services peak load on that Oracle database? Large numbers of users querying any data source at the same time could put a strain on the resources of that data source.
  
The following best practices can be used to optimize the performance of Visio Services:
  
- Monitor the performance of the application servers in the farm and add CPU and memory or additional Front-end role servers if they are needed to handle peak loads.
    
- Limit the maximum diagram size.
    
- Increase the minimum cache age for diagrams. This increases the interval in which a user sees cached data for a particular diagram.
    
## Visio Graphics Service Application

SharePoint Server implements Visio Services through the Visio Graphics Service Application. It is within the Visio Graphics Service Application that you configure the various Visio Services settings, such as trusted data providers and drawing cache settings.
  
For many deployments, a single Visio Graphics Service Application is sufficient. However, SharePoint Server lets you create multiple service applications of each type if you want (for example, if you need to use different data sources that require different global settings or a different unattended service account within Visio Services).
  
## Use a Visio Services pilot deployment

To help determine capacity requirements for Visio Services, consider rolling Visio Services out to a limited pilot group that is representative of typical users. Giving a fairly small number of people access to Visio Services functionality lets you monitor server resource usage and effect on related systems, such as external data sources, without overtaxing system resources.
  
Once you have compiled performance data for the pilot group, you can extrapolate system requirements for Visio Services when you deploy it across your whole organization. The pilot data will also help you determine peak load requirements and times when peak loads are likely to occur.
  
By monitoring other affected systems—such as data sources used by data-connected diagrams—you can also determine the likely effect of Visio Services on other systems in your organization.
  
## Monitor system resources consumed by Visio Services

We highly recommend that you monitor system resources consumed by Visio Services—alongside the other services in your SharePoint Server farm. It is typical for resource usage to increase over time as additional users are brought online and existing users make more use of Visio Services and other SharePoint Server technologies.
  
The SharePoint Server services architecture enables easy addition of servers to the farm. As user demands increase, you can continue to add servers to the farm to provide additional capacity and redundancy.
  
By monitoring resource usage, you can predict when additional capacity is likely to be needed and include the needed hardware in your organization's regular budgetary procedures. This also helps avoid system downtime or slow response caused by unexpectedly high server loads.
  
## Backup and recovery of data used by Visio Services

Visio Services settings and Visio documents stored in SharePoint Server libraries can be backed up by the farm administrator when doing a standard farm backup. However, be aware that when working with Visio documents that are connected to data sources that are outside the farm, the data to which the Visio documents are connected is not backed up as part of a standard farm backup. In this case, the administrator of the system where the data resides should perform a separate backup procedure.
  
## Requirements for authors of Visio diagrams

Visio Services lets you display Visio diagrams in a Web Part without the need to have Visio installed on the client computer. However, Visio Services does not allow for creating or editing Visio diagrams. As part of your deployment plan for Visio Services, you should also plan for the needs of diagram authors within your organization. Each diagram author who has to use Visio Services must have a copy of Visio Professional, Visio Premium, or Visio Pro for Microsoft 365.
  

