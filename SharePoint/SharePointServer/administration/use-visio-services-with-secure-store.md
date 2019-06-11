---
title: "Use Visio Services with Secure Store Service in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 7c82bdf9-453f-4ee9-a2e6-20adf05ad59c
description: "Secure Store can be used to store encrypted credentials for use in refreshing data-connected Visio diagrams in Visio Services."
---

# Use Visio Services with Secure Store Service in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Visio Services can be configured to use the Secure Store Service to provide user authentication for data-connected diagrams that use an external data source such as SQL Server.
  
> [!NOTE]
> This article assumes that you have already deployed a Secure Store Service service application. If you have not deployed Secure Store, see [Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)) and [Configure the Secure Store Service in SharePoint Server](configure-the-secure-store-service.md). 
  
Secure Store provides a method of mapping users who do not have direct data access to an account that does have data access. Secure Store and Visio Services work together in the following basic sequence of events:
  
1. A user accesses a data-connected diagram on a SharePoint site.
    
2. Visio Services passes the user's identity to Secure Store.
    
3. Secure Store determines whether the user is authorized to access the data. If so, Secure Store returns the data access credentials to Visio Services.
    
4. Visio Services impersonates the data access credentials, accesses the data, and displays the data to the user.
    
Visio Services provides three methods of using Secure Store to provide data access:
  
> **Unattended Service Account**: The unattended service account is an account that is used by Visio Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see [Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account](configure-the-unattended-service-account.md).
    
> **External Data Connections**: You can specify a Secure Store target application in an Office Data Connection (ODC) file and then connect to that ODC file in Visio. When you publish the diagram to a SharePoint document library, it maintains its connection to the ODC file. The connection information in the ODC file is used when Visio Services refreshes the data in the workbook. Using an ODC file has the following advantages:
    
    - A single ODC file can be referenced by multiple diagrams. If the data source connection parameters change (for example, if you want to use a different Secure Store target application than the one originally specified) you need only update the ODC file and not the diagrams themselves.
    
    - Using ODC files allows administrators to create and maintain the data connections used by the organization. You can create data connections appropriate for users, place them in a trusted data connection library, and then notify the users of which ODC files to use for their queries.
    
    For information about how to configure this scenario, see [Configure Visio Services data refresh in SharePoint Server by using external data connections](configure-data-refresh-by-using-external-data-connections.md).
    
Visio, which is used to create the diagrams, does not use Secure Store for data authentication. You must configure direct data access for diagram authors. Once the diagram has been published to a SharePoint site, Visio Services can use Secure Store when it renders the diagram.
  
## See also

#### Concepts

[Secure Store for Business Intelligence service applications](secure-store-for-business-intelligence-service-applications.md)

