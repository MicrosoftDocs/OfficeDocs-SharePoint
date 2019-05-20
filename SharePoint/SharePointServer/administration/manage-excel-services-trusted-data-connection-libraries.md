---
title: "Manage Excel Services trusted data connection libraries (SharePoint Server 2013)"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 4e26b32c-f5f8-40b7-a240-bad147c33402
description: "Add, configure, or delete trusted data connection libraries in Excel Services in SharePoint Server."
---

# Manage Excel Services trusted data connection libraries (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server 2013 Enterprise. 
  
Trusted data connection libraries are SharePoint Server 2013 data connection libraries that Excel Services has been configured to trust. Excel Services does not use data connection files that are not stored in a trusted data connection library.
  
To perform the procedures in this article, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.
  
    
## Add a trusted data connection library
<a name="proc1"> </a>

Use the following procedure to add a trusted data connection library.
  
 **To add a trusted data connection library**
  
1. In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure. 
    
3. On the Manage Excel Services page, click **Trusted Data Connection Libraries**.
    
4. On the Excel Services Application Trusted Data Connection Libraries page, click **Add Trusted Data Connection Library**.
    
5. On the Excel Services Application Add Trusted Data Connection Library page, in the **Location** section, type the address of the trusted data connection library in the **Address** box. 
    
6. In the **Description** box, you can also type a description of the purpose for this trusted data connection library. 
    
7. Click **OK**.
    
## Configure a trusted data connection library
<a name="proc2"> </a>

Use the following procedure to configure an existing trusted data connection library.
  
 **To configure a trusted data connection library**
  
1. In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure. 
    
3. On the Manage Excel Services page, click **Trusted Data Connection Libraries**.
    
4. On the Excel Services Application Trusted Data Connection Libraries page, either click the data connection library that you want to configure or point to the data connection library, click the arrow that appears, and then click **Edit**.
    
## Delete a trusted data connection library
<a name="proc3"> </a>

Use the following procedure to delete a trusted data connection library.
  
> [!NOTE]
> Deleting a trusted data connection library does not affect the library itself or its contents. It only removes the library as a trusted data connection library in Excel Services. 
  
 **To delete a trusted data connection library**
  
1. In the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure. 
    
3. On the Manage Excel Services page, click **Trusted Data Connection Libraries**.
    
4. On the Excel Services Application Trusted Data Connection Libraries page, point to the data connection library that you want to delete, click the arrow that appears, and then click **Delete**.
    
5. Click **OK** in the message box that asks whether you want to continue with the deletion. 
    
## See also
<a name="proc3"> </a>

#### Other Resources

[Configure Excel Services in SharePoint](/SharePoint/administration/configure-excel-services)

