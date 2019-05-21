---
title: "Overview of Visio Services in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 9e952b26-fb0e-48a5-89b1-054f54f9b986
description: "Visio Services lets users share and view Visio diagrams. It also enables data-connected Visio diagrams to be refreshed and updated from various data sources."
---

# Overview of Visio Services in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Visio Services runs as a SharePoint Server service application. It uses the Visio Graphics Service which runs under the Front-end server role.
  
## Use and benefits of Visio Services

Using Visio Services, you can render Visio diagrams in a Web browser. This lets users view Visio documents without having Visio or the Visio Viewer installed on the local computer. This also allows diagrams to be viewed on mobile devices.
  
Basic exploration and navigation of these rendered diagrams are supported within the Visio Web Access Web Part. Page designers can configure the user interface and functionality of the Web Part.
  
Visio Services can also refresh the data and recalculate the visuals of a Visio diagram hosted on a SharePoint site. This enables published diagrams to refresh connections to various data sources and to update affected data graphics and text fields.
  
Visio diagrams can be published to SharePoint Server by using Visio Professional, Visio Premium, or Visio Pro for Office 365.
  
## Data sources supported by Visio Services

Connections to the data sources listed here may be refreshed by using Visio Services. The original data connection must be configured using Visio. Refresh of data through any other mechanism into a Visio diagram is not supported.
  
- SQL Server 7.0
    
- SQL Server 2000
    
- SQL Server 2005 (32- &amp; 64-bit)
    
- SQL Server 2008 (32- &amp; 64-bit)
    
- SQL Server 2008 R2 (32- &amp; 64-bit)
    
- SQL Server 2012 (32- &amp; 64-bit)
    
- Sheet information that is stored in Excel workbooks (.xlsx files) published from Office Excel 2007, Excel 2010, Excel 2013, or Excel 2016 hosted on the same SharePoint Server farm
    
- SharePoint Server lists that are hosted on the same farm
    
- External lists exposed in SharePoint Server through Microsoft Business Connectivity Services.
    
- OLE DB or ODBC 
    
- Custom Data Providers implemented as .NET Framework assemblies
    
## Compatible Visio versions for Visio Services

Visio Services can render diagrams created in: 
  
- Visio 2010 Professional
    
- Visio 2010 Premium
    
- Visio 2013 Professional
    
- Visio 2013 Premium
    
- Visio 2016 Professional
    
- Visio Pro for Office 365
    
Visio diagrams created in Visio 2010 must be published to a SharePoint site as a Visio Web drawing (\*.vdw) file. Standard Visio 2010 diagrams (.vsd files) are not rendered by Visio Services and require Visio 2010 to be viewed.
  
The standard diagram format in later versions of Visio (\*.vsdx files) can be rendered by Visio Services, along with the Web drawing (.vdw) format. We recommend that you use the .vsdx format unless you require compatibility with previous versions of Visio.
  
## Configuring Visio Services

Before you configure Visio Services, be sure to review [Plan Visio Services deployment in SharePoint Server 2013](plan-visio-services-deployment.md), [Plan Visio Services security in SharePoint Server 2013](visio-services-security-planning.md), and [Data authentication for Visio Services in SharePoint Server 2013](data-authentication-for-visio-services.md). These articles contain important information about planning your Visio Services infrastructure.
  
To get started deploying Visio Services, see [Configure Visio Services](/SharePoint/administration/configure-visio-services).
  

