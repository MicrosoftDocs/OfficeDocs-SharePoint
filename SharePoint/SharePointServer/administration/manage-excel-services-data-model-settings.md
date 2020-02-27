---
title: "Manage Excel Services data model settings (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: e1fb66ca-d0ee-4935-b8dc-a87abf98e216
description: "Configure instances of SQL Server 2012 Analysis Services for Data Model functionality in Excel Services."
---

# Manage Excel Services data model settings (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server 2013 Enterprise. 
  
Excel Services can use instances of SQL Server 2012 SP1 Analysis Services (SSAS) perform advanced data analysis calculations. This article describes how to register, edit, and unregister instances of SQL Server 2012 Analysis Services for use by Excel Services in performing these calculations.
  
Before you begin this operation, review the following information about prerequisites:
  
- To perform these procedures, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.
    
- The instance of SQL Server 2012 Analysis Services that you plan to use must be installed in SQL Server PowerPivot for SharePoint mode.
    
    
## Register an Analysis Services server
<a name="proc1"> </a>

Use the following procedure to register an instance of SQL Server 2012 SP1 Analysis Services (SSAS) with Excel Services.
  
 **To register an Analysis Services server**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **Data Model**.
    
4. Click **Add Server**.
    
5. In the **Server Name** box, type the name of the instance of SQL Server 2012 SP1 Analysis Services (SSAS) that you want to add. 
    
6. Optionally, in the **Description** box, type a description for the server. 
    
7. Click **OK**.
    
## Edit Analysis Services server details
<a name="proc2"> </a>

Use the following procedure to edit the server name or description for an instance of SQL Server 2012 SP1 Analysis Services (SSAS) that has been registered with Excel Services.
  
 **To edit Analysis Services server details**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **Data Model**.
    
4. Hover over the server that you want to edit, click the arrow that appears, and then click **Edit**.
    
5. Update the **Server Name** and **Description** as needed, and then click **OK**.
    
## Unregister an Analysis Services server
<a name="proc3"> </a>

Use the following procedure to remove an instance of SQL Server 2012 SP1 Analysis Services (SSAS) from Excel Services.
  
 **To unregister an Analysis Services server**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **Data Model**.
    
4. Hover over the server that you want to edit, click the arrow that appears, and then click **Delete**.
    
5. Click **OK** on the delete confirmation dialog box. 
    
## See also
<a name="proc3"> </a>

#### Other Resources

[Configure Excel Services in SharePoint](/SharePoint/administration/configure-excel-services)

