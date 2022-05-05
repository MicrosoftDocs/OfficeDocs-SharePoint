---
title: "Configure scheduled data refresh for Power Pivot by using the unattended data refresh account (SharePoint Server 2013)"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 7/6/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.assetid: 3fdbc40b-8562-4bec-be89-113a64e19911
description: "Learn to configure scheduled data refresh in Power Pivot for SharePoint by using the unattended data refresh account."
---

# Configure scheduled data refresh for Power Pivot by using the unattended data refresh account (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-xxx-md.md)] 
  
> [!IMPORTANT]
> This scenario applies only to SharePoint Server 2013. 
  
In this article, we'll take a look at configuring scheduled data refresh in SQL Server 2012 Power Pivot for SharePoint 2013 by using the unattended data refresh account.
  
By using the unattended data refresh account, you can have the data in your workbooks refreshed using an account that was configured by your administrator.
  
## Before you begin
<a name="begin"> </a>

Before starting, you will need:
  
- The user name of the unattended data refresh account that was configured [when you set up Power Pivot for SharePoint originally](configure-power-pivot-for-sharepoint-2013.md).
    
- Contribute access to the SharePoint document library that you will be using.
    
Additionally, be sure that [Excel Services](excel-services-overview.md) is configured in your SharePoint Server 2013 farm. 
  
## Video demonstration
<a name="VideoDemonstration"> </a>

This video shows the steps involved in configuring scheduled data refresh in SQL Server 2012 Power Pivot for SharePoint 2013 by using the unattended data refresh account, as described in this article.
  
**Video: Configure scheduled data refresh for Power Pivot by using the unattended data refresh account**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/e6d852d5-c321-4703-a5a5-8b8f37a8ffa7?autoplay=false]
## Configure access to your data source
<a name="proc1"> </a>

The first step in setting up scheduled data refresh by using the unattended data refresh account is to ensure that it has the proper access to the data source used in your report. We'll take a look at SQL Server and Analysis Services data sources.
  
### Use a SQL Server data source

If you're using SQL Server for your data source, you'll need to make sure that your unattended data refresh account has read permissions to the SQL Server database where your data resides.
  
 **To set read permission on a SQL Server database**
  
1. In SQL Server Management Studio, connect to the database engine.
    
2. Expand **Security**.
    
3. Right-click **Logins**, and then choose **New Login**.
    
4. In the **Login name** box, type the domain and user name of your unattended data refresh account. 
    
5. On the **User Mapping** page, select the **Map** check box for the database to which you want to grant access. 
    
6. Select the **db_datareader** check box. 
    
7. Choose **OK**.
    
If you're also using Analysis Services, see the next section for information about how to set up access to Analysis Services data sources. If you're not using Analysis Services, skip ahead to [Set up a data refresh schedule in Power Pivot for SharePoint](data-refresh-using-the-unattended-data-refresh-account.md#ver).
  
### Use an Analysis Services data source

If you're using Analysis Services, you'll need to make sure that your data access account is a member of the proper Analysis Services role and that the role has read access to the Analysis Services cube.
  
 **To set read permission on an Analysis Services cube**
  
1. In SQL Server Management Studio, connect to Analysis Services.
    
2. Expand **Databases**, and expand the database to which you want to grant access.
    
3. Right-click **Roles**, and then choose **New Role**.
    
4. Type a name for the role.
    
5. On the **Membership** page: 
    
1. Choose **Add**.
    
2. Type your unattended data refresh account, and then choose **OK**.
    
6. On the **Cubes** page, select **Read** access for the cubes to which you want to grant access. 
    
7. Choose **OK**.
    
## Set up a data refresh schedule in Power Pivot for SharePoint
<a name="ver"> </a>

Now that everything is configured, we can set up the refresh schedule and other settings in Power Pivot for SharePoint. We'll start by building a test workbook with a data model in Excel and publishing it to a document library in a site collection where Power Pivot for SharePoint is enabled. Then, we can set the refresh schedule.
  
 **To create a test workbook**
  
1. In Excel, on the **Data** tab, choose **From Other Sources**, and then choose **From SQL Server**.
    
2. Type the name of the instance of SQL Server where your data resides.
    
3. Follow the wizard through to connect to the table that contains your data.
    
4. When the wizard completes, you should see the **Import Data** dialog. Choose the **Only Create Connection** option, and then select the **Add this data to the Data Model** check box. 
    
5. Choose **OK**.
    
6. On the **Power Pivot** tab, choose **Manage**.
    
7. On the **Power Pivot** ribbon, choose **PivotTable**.
    
8. On the **Insert Pivot** dialog, choose the **Existing Worksheet** option, and then choose **OK**.
    
9. Select the fields that you want in the PivotTable report.
    
10. Save the workbook to a document library on the site collection where you enabled Power Pivot.
    
Now that the workbook has been saved to a SharePoint document library, let's configure the refresh settings.
  
 **To configure refresh settings for a workbook**
  
1. In the document library where your Excel workbook is stored, choose the ellipsis (...) control twice, and then choose **Manage Power Pivot Data Refresh**.
    
    ![Screenshot of controls in document library.](../media/PowerPivotDocLibraryControls.png)
  
2. On the **Manage Data Refresh** page, select the **Enable** check box. 
    
3. In the **Schedule Details** section, choose the schedule options that you want for refreshing the data in this workbook. 
    
4. Optionally, if you want the workbook to refresh right away, select the **Also refresh as soon as possible** check box. 
    
5. In the **Credentials** section, choose the **Use the data refresh account configured by the administrator** option. 
    
6. Choose **OK**.
    
You can test if data refresh is working properly by making some changes to your data, and then setting the workbook to refresh right away by using the **Also refresh as soon as possible** option. 
  
## See also
<a name="ver"> </a>

#### Concepts

[Configure Power Pivot for SharePoint 2013](configure-power-pivot-for-sharepoint-2013.md)
  
[Configure scheduled data refresh for Power Pivot by using a specified account (SharePoint Server 2013)](data-refresh-using-a-specified-account.md)
  
[Configure scheduled data refresh for Power Pivot by using the unattended data refresh account (SharePoint Server 2013)](data-refresh-using-the-unattended-data-refresh-account.md)

