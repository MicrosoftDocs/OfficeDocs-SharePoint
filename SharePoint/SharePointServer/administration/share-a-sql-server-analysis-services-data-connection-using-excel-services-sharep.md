---
title: "Share a SQL Server Analysis Services data connection using Excel Services (SharePoint Server 2013)"
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
ms.assetid: 7021185c-1f2b-44a6-ba4a-8355dd8409e1
description: "Learn how to use Excel to create and share a connection to SQL Server Analysis Services data that people can use to create data models, reports, scorecards, and dashboards."
---

# Share a SQL Server Analysis Services data connection using Excel Services (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can use Excel to create connections to databases such as SQL Server Analysis Services, and then share those connections with others. When you can upload a data connection to an Excel Services in SharePoint Server 2013 trusted data connection library, the data connection is available for you and others to use to create data models, reports, scorecards, and dashboards. Depending on the particular data source that is used, people can easily refresh data in Excel Services workbooks so that the most current information is displayed.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this task, review the following information about prerequisites:
  
- You must be using Excel 2016 and SharePoint Server 2013.
    
- Excel Services must be configured to include a trusted data connections library and a trusted documents library. Ideally, you'll have a Business Intelligence Center site configured that you can use for your data connections and workbooks. For more information, see [Configure a Business Intelligence Center in SharePoint Server 2013](/SharePoint/sharepoint-server).
    
- You must have at least Contribute permissions assigned in SharePoint Server 2013.
    
- You will need information from a SharePoint administrator about how data authentication is configured for the databases your organization uses. This can affect how you connect to different data sources. 
    
- If you plan to publish workbooks that contain data models to SharePoint Server 2013, Excel Services must be configured to support data models. For more information, see [Configure Excel Services in SharePoint Server 2013 Preview](/SharePoint/administration/configure-excel-services).
    
## Step 1: Use Excel to create connections to SQL Server Analysis Services data
<a name="part1"> </a>

You can use Excel to create a connection a cube that is stored in Analysis Services. This kind of connection is an Office Data Connection (ODC) file that can be used to create reports, scorecards, and dashboards by using applications such as Excel.
  
 **To create an Analysis Services data connection by using Excel**
  
1. In Excel, on the **Data** tab, in the **Get External Data** group, click **From Other Sources**, and then select **From Analysis Services**.
    
    The **Data Connection Wizard** opens. 
    
2. On the **Connect to Database Server** page, in the **Server name** box, specify the name of the server where the Analysis Services data that you want to use resides. Do not click **Next** yet. 
    
3. In the **Log on credentials** section, take one of the following steps: 
    
  - If your organization is using Windows Authentication, choose **Use Windows Authentication**, and then choose the **Next** button. 
    
  - If your organization is using specific user credentials, choose **Use the following User Name and Password**, specify an appropriate user name and password, and then choose the **Next** button. 
    
4. On the **Select Database and Table** page, in the **Select the database that contains the data that you want** list, select the database that you want to use. Do not click **Next** yet. 
    
5. On the **Select Database and Table** page, select **Connect to a specific cube or table**, select the cube or table that you want to use, and then click **Next**.
    
6. On the **Save Data Connection File and Finish** page, take the following steps: 
    
1. In the **File Name** box, keep or change the default file name. 
    
2. In the **Description** box, type a brief description for the data connection. 
    
3. In the **Friendly Name** box, keep the default name or type a new name for file. 
    
4. In the **Search Keywords** box, type some words or phrases that will help users find the data connection when it is published to SharePoint Server 2013. 
    
5. Next to **Excel Services**, click **Authentication Settings…**, and then take one of the following steps:
    
  - If you want this connection to use Windows Authentication or the Effective User Name feature, select **Use the authenticated user's account**, and then click **OK**.
    
  - If you want this connection to use Secure Store Service, select **Use a stored account**. In the **Application ID** box, specify the Secure Store target application ID, and then click **OK**.
    
  - If Excel Services is configured to use the unattended service account, select **None**, and then click **OK**.
    
    > [!IMPORTANT]
    > If you do not know which option to choose, contact a SharePoint administrator. 
  
6. Click **Finish** to close the **Save Data Connection File and Finish** page. 
    
7. On the **Import Data** page, click **Only Create Connection**, and then click **OK**.
    
8. Repeat steps 1-7 until you have created all the Analysis Services data connections that you want.
    
9. Close Excel.
    
By default, data connections are saved in the **My Data Sources** folder in the **Documents** library on your computer. 
  
## Step 2: Upload data connections to SharePoint Server 2013
<a name="part2"> </a>

After data connections are created, the next step is to upload them to a data connection library. We recommend that you use a Business Intelligence Center site to store and manage business intelligence content, such as data connections. 
  
> [!NOTE]
> If you are not using a Business Intelligence Center site, make sure that you use a data connection library that is specified as a trusted location in Excel Services. For more information, see [Manage Excel Services trusted data connection libraries (SharePoint Server 2013)](manage-excel-services-trusted-data-connection-libraries.md). 
  
 **To upload a data connection to SharePoint Server**
  
1. Open a web browser and navigate to the SharePoint site that contains the data connection library that you want to use.
    
    If you are using a Business Intelligence Center, the website address (URL) resembles http://servername/sites/bicenter.
    
2. Click **Site Contents** to view the lists and libraries that are available for that site. 
    
3. Click **Data Connections** to open that library. 
    
4. Click **New Item** to open the **Add a document** dialog box. 
    
5. Click **Browse** to open the **Choose File to Upload** dialog box. 
    
6. Assuming the data connection is saved in its default location, click **Libraries**, click **Documents**, and then double-click **My Data Sources**.
    
7. Select the ODC file that you want to upload, and then click **Open**.
    
8. In the **Add a document** dialog box, click **OK**.
    
    A **Data Connections** form opens. 
    
9. In the **Data Connections** form, specify the following settings: 
    
  - In the **Content Type** section, confirm that **Office Data Connection File** is selected. 
    
  - In the **Name** box, keep or change the file name of the ODC file. 
    
  - In the **Title** box, keep or change the title of the ODC file. 
    
  - In the **Description** box, type a description of the data connection. 
    
  - In the **Keywords** box, type one or more words or phrases. This information is used by search queries to discover the data connection. 
    
    Then click **Save**.
    
    The data connection is added to the library. Repeat this procedure for each data connection that you want to share.
    
## See also
<a name="part2"> </a>

#### Concepts

[Share data connections by using Excel and Excel Services (SharePoint Server 2013)](share-data-connections-by-using-excel-and-excel-services-sharepoint-server-2013.md)
  
[Data sources supported in Excel Services (SharePoint Server 2013)](data-sources-supported-in-excel-services-sharepoint-server-2013.md)

