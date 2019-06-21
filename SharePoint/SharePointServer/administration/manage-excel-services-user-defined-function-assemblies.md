---
title: "Manage Excel Services user defined function assemblies (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 371181ec-d27c-4899-9d3c-ae0ffefa1cc0
description: "Add, edit or delete Excel Services user-defined function assemblies in SharePoint Server."
---

# Manage Excel Services user defined function assemblies (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server 2013 Enterprise. 
  
If your deployment scenarios include workbooks that contain user-defined functions to extend the capabilities of Excel Calculation Services, you must register the user-defined function assemblies on the Excel Services user-defined function assembly list.
  
Before you begin this operation, review the following information about prerequisites:
  
- To use user-defined functions, you must enable user-defined functions on trusted file locations that contain workbooks that require access to user-defined functions. For information about configuring trusted file locations, see [Configure a trusted file location](manage-excel-services-trusted-file-locations.md#proc2).
    
- You must be a member of the Farm Administrators group or an Excel Services service application administrator to perform the procedures in this article.
    
    
## Register a user-defined function assembly
<a name="proc1"> </a>

Use the following procedure to register a user-defined function assembly for use with Excel Services.
  
 **To register a user-defined function assembly**
  
1. On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **User Defined Function Assemblies**.
    
4. On the Excel Services User Defined Functions page, click **Add User-Defined Function Assembly**.
    
5. On the Add User-Defined Function Assembly page, in the **Assembly** section, type the assembly name or the full path of an assembly that contains the user-defined functions, which you want to call in the **Assembly** box. 
    
6. Under **Assembly Location**, select one of the following:
    
  - **Global assembly cache** (a global place where signed assemblies can be deployed and run with full trust by default) 
    
  - **File path** (a local or network file location) 
    
7. In the **Enable Assembly** section, select the **Assembly enabled** check box to enable Excel Calculation Services to call the assembly. You can clear the check box to disable the assembly without removing the function assembly from the list. 
    
8. In the **Description** box, you may choose to type a description of the purpose for the function assembly. 
    
9. Click **OK**.
    
## Edit user-defined function assembly details
<a name="proc2"> </a>

Use the following procedure to edit the user-defined function assembly details for a registered user-defined function assembly. You can also use this procedure to disable the assembly.
  
 **To edit user-defined function assembly details**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **User Defined Function Assemblies**.
    
4. On the Excel Services User Defined Functions page, point to the user-defined function assembly that you want to edit, click the arrow that appears, and then click **Edit**.
    
5. Update the assembly details as needed, and then click **OK**.
    
## Unregister a user-defined function assembly
<a name="proc3"> </a>

Use the following procedure to remove a user-defined function assembly from the user-defined function assembly list.
  
 **To unregister a user-defined function assembly**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click the Excel Services service application that you want to manage.
    
3. On the Manage Excel Services page, click **User Defined Function Assemblies**.
    
4. On the Excel Services User Defined Functions page, point to the user-defined function assembly that you want to delete, click the arrow that appears, and then click **Delete**.
    
5. Click **OK** in the message box that asks whether you want to proceed with the deletion. 
    
## See also
<a name="proc3"> </a>

#### Other Resources

[Configure Excel Services in SharePoint](/SharePoint/administration/configure-excel-services)

