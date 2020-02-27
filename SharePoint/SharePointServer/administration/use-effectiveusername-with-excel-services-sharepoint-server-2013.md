---
title: "Use EffectiveUserName with Excel Services (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 4fbe0228-54c6-40ce-a9d3-3198423fe688
description: "Use the Analysis Services EffectiveUserName feature to refresh data-connected workbooks in Excel Services in SharePoint Server 2013 using the workbook viewer's Windows identity."
---

# Use EffectiveUserName with Excel Services (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
> [!IMPORTANT]
> This scenario applies only to Excel Services with an Analysis Services data source on SharePoint Server 2013 Enterprise. 
  
    
## Scenario overview
<a name="overview"> </a>

Using the EffectiveUserName feature with Excel Services allows the identity of a user viewing a report to be passed to SQL Server Analysis Services. This allows you to specify the appropriate level of data access for a given user on the OLAP cube itself.
  
Using the EffectiveUserName option allows passing the user's identity to SQL Server Analysis Services without the need to configure Secure Store or Kerberos delegation.
  
## Before you begin
<a name="begin"> </a>

Before starting, read the following information about permissions and software requirements.
  
- This scenario assumes that you have Excel Services configured on your farm and an Excel Services trusted file location where you can save your report. For information about configuring Excel Services, see [Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md) and [Configure Excel Services in SharePoint Server 2013 Preview](/SharePoint/administration/configure-excel-services). For information about configuring a trusted file location, see [Manage Excel Services trusted file locations (SharePoint Server 2013)](manage-excel-services-trusted-file-locations.md).
    
- This scenario requires that you have Farm Administrator access to the SharePoint Server 2013 farm and administrator access to SQL Server Analysis Services.
    
## Configure Excel Services Global Settings
<a name="ConfigureGlobalSettings"> </a>

The first step in configuring the EffectiveUserName feature is to enable the feature in Excel Services global settings. Use the following procedure to enable the EffectiveUserName feature.
  
 **To enable EffectiveUserName in Excel Services**
  
1. In Central Administration, under **Application Management**, click **Manage service applications**.
    
2. Click the Excel Services service application.
    
3. Click **Global Settings**.
    
4. On the Excel Services Application Settings page, in the **External Data** section, select the **Use the EffectiveUserName property** check box. 
    
5. Click **OK**.
    
## Configure Analysis Services access
<a name="ConfigureASAccess"> </a>

Using the EffectiveUserName feature requires that the account that is running the Excel Services application pool be an Analysis Services administrator.
  
If you do not know what account is running the Excel Services application pool in your farm, use the following procedure to determine the account. If you know the account, skip this procedure.
  
 **To determine the Excel Services application pool account**
  
1. On the SharePoint Central Administration Web site home page, click **Security**.
    
2. On the Security page, under **General Security**, click **Configure service accounts**.
    
3. On the Service Account page, in the **Credential Management** section, from the drop-down list, select the application pool that runs Excel Services Application. 
    
    When this option is selected, the name of the Excel Services service application appears in the box underneath the drop-down list. The account shown in the **Select an account for this component** dropdown list is the Windows identity that you need to add as an Analysis Services administrator. 
    
4. Click **Cancel**.
    
You must add the Excel Services application pool account as an Analysis Services administrator. Use the following procedure to add this account as an administrator in Analysis Services.
  
 **To add an Analysis Services administrator**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Right click the Analysis Services top node, and then click **Properties**.
    
3. On the **Security** page, click **Add**.
    
4. Type the name of the account that runs the Excel Services application pool, and then click **OK**.
    
5. Click **OK**.
    
## Configure OLAP cube access
<a name="ConfigureOLAP"> </a>

You must grant access to the OLAP cube for the users who will be creating or viewing Excel Services reports. To do this, you must create a role in the OLAP cube. (You can use an existing role if you have created one previously.)
  
Within the role, you can grant access to users or Active Directory groups. We recommend using Active Directory groups for easier administration.
  
Analysis Services provides a variety of access options for a given role. You can create multiple roles if you have different groups of users who need different levels of access to the cube.
  
Use the following procedure to create a role and assign permissions to users.
  
> [!NOTE]
> This procedure describes how to grant read access to a cube. You can adjust the permissions for the role as needed for your users. 
  
 **To create a role**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Expand **Databases** and expand the database where you want to create the role. 
    
3. Right-click **Roles** and click **New Role**.
    
4. On the General page, type a name for the role.
    
5. On the Membership page, add the users or Active Directory group containing the users to whom you want to grant cube access.
    
6. On the Cubes page, select **Read** from the **Access** dropdown list for the cubes that you want to grant access to. 
    
7. Click **OK**.
    
Once granted read permissions to the OLAP cube, users will be able to connect to the cube in Excel to create reports and will also be able to refresh the data in Excel Services.
  
> [!NOTE]
> Once granted access to an OLAP cube, users can also connect to the cube directly in SQL Server Management Studio. The access that they are granted to the cube determines what actions they can perform in Management Studio. 
  
## Create and publish a report
<a name="CreateAndPublish"> </a>

Once a user has been granted access to the cube, they can connect to it in Excel. Use the following procedure to connect to the cube.
  
 **To connect to an OLAP data source**
  
1. In Excel, on the **Data** tab, in the **Get External Data** section, click **From Other Sources**, and then click **From Analysis Services**.
    
2. In the **Server name** text box, type the name of the instance of Analysis Services that you want to connect to, and then click **Next**.
    
3. Select the cube that you want to connect to, and then click **Next**.
    
4. Click **Finish**.
    
In order for the EffectiveUserName feature to be used in a published report, the Excel Services authentication settings must be configured to use Windows authentication. Use the following procedure to configure the Excel Services authentication settings for your data source.
  
 **To configure Excel Services authentication settings**
  
1. In Excel, on the **Data** tab, in the **Connections** section, click **Connections**.
    
2. Select the connection to your Analysis Services cube, and then click **Properties**.
    
3. On the **Definition** tab, click **Authentication Settings**.
    
4. On the **Excel Services Authentication Settings** dialog box, select the **Use the authenticated user's account** (Excel 2016) or **Windows Authentication** (Excel 2010) option, and then click **OK**.
    
5. Click **OK** and then click **Close**.
    
When you have finished creating your report, the next step is to save it to a SharePoint Server 2013 document library that has been configured as a trusted file location in Excel Services. Use the following procedure to save your workbook.
  
> [!NOTE]
> This procedure uses Excel 2016. In Excel 2010, use **File**, **Save &amp; Send** to publish the workbook to SharePoint Server 2013. 
  
 **To publish the report to SharePoint Server**
  
1. In Excel, on the **File** tab, click **Save**.
    
2. Click **Computer**, and then click **Browse**.
    
3. Type the URL of the SharePoint document library where you want to save the file.
    
4. Type a filename, and then click **Save**.
    
Once the workbook has been saved to SharePoint Server 2013, you can render it using Excel Services and the data will refresh based on the refresh settings configured in the Excel Services trusted file location settings.
  

