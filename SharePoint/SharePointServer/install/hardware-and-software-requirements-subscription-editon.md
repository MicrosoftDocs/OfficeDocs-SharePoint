---
title: "Hardware and software requirements for SharePoint Subscription edition"
ms.reviewer: 
ms.author: v-nsatapathy
author: nimishasatapathy
manager: serdars
ms.date: 6/22/2021
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.custom: 
ms.assetid: 4d88c402-24f2-449b-86a6-6e7afcfec0cd
description: "Find out the minimum hardware and software requirements you need to install and run on SharePoint Subscription edition."
---

# Hardware and software requirements for SharePoint Subscription edition

[!INCLUDE[appliesto-xxx-xxx-2019-xxx-md](../includes/appliesto-xxx-xxx-2019-xxx-md.md)] 
  
> [!IMPORTANT]
> If you contact Microsoft Customer Support Services about a production system that does not meet the minimum hardware specifications described in this document, support will be limited until the system is upgraded to the minimum requirements. 
  
    
## Hardware requirements

We recommend testing SharePoint Server v.Next in a pre-production environment with the following hardware configurations:

|**Installation scenario**|**Deployment type and scale**|**Processor**|**RAM**|**Hard disk**|
|:-----|:-----|:-----|:-----|:-----|
|Single server role that uses SQL Server  <br/> |Development or evaluation installation with the minimum recommended services for development environments.  <br/> |64-bit, 4 cores <br/> |16 GB  <br/> |80 GB for system drive  <br/> 100 GB for second drive  <br/> |
|Single server role that uses SQL Server  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores <br/> |24 GB   <br/> |80 GB for system drive  <br/> 100 GB for second drive and additional drives  <br/> |
|SharePoint server in a multi-tier farm  <br/> |Development or evaluation installation with a minimum number of services.  <br/> |64-bit, 4 cores <br/> |12 GB  <br/> |80 GB for system drive  <br/> 80 GB for second drive  <br/> |
|SharePoint server in a multi-tier farm  <br/> |Pilot or user acceptance test installation running all available services.  <br/> |64-bit, 4 cores  <br/> |16 GB    <br/> |80 GB for system drive  <br/> 80 GB for second drive and additional drives  <br/> 

> [!NOTE]
> Hard disk space and number of drives depends on the amount of content and the way you choose to distribute data for a SharePoint environment.

   
## Deployment requirements: Farm Topology
<a name="hwforwebserver"> </a>

SharePoint Server v.Next supports the same farm topologies as SharePoint Server 2019. For more information, see [Planning for a MinRole server deployment in SharePoint Server 2019](planning-for-a-minrole-server-deployment-in-sharepoint-server.md).

## Minimum requirements for client computers

A supported browser. For more information, see [System requirements for Microsoft 365 and office:Browsers](https://www.microsoft.com/microsoft-365/microsoft-365-and-office-resources?rtc=1#coreui-heading-uyetipy).
    
  
## Software requirements
<a name="section4"> </a>

The requirements in the following section apply to the following installations:
  
- Operating systems
    
- Database servers

### Operating systems

SharePoint Server v.Next requires Windows Server 2019 or Windows Server 2022. Earlier versions of Windows Server are not supported. SharePoint Server v.Next supports both the Standard and Datacenter editions of Windows Server, as well as both the Windows Server with Desktop Experience and Windows Server Core installation options.

You can download evaluation copies of Windows Server 2019 and Windows Server 2022 Preview from the Microsoft Evaluation Center.
- [Windows Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2019)
- [Windows Server 2022](https://www.microsoft.com/en-in/evalcenter/evaluate-windows-server-2022-preview)

### Database servers

SharePoint Server v.Next requires SQL Server 2019 for its databases. Earlier versions of SQL Server are not supported.
You can download evaluation copies of SQL Server 2019 from the Microsoft Evaluation Center.

- [SQL Server 2019](https://www.microsoft.com/en-in/evalcenter/evaluate-sql-server-2019)
  