---
title: "Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/7/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: cdaaf121-3fd3-4889-9020-9cf7606c8f6b
description: "Learn how to use Excel to create and share OLE DB or ODBC connections that people can use to create data models, reports, scorecards, and dashboards."
---

# Share an OLE DB or ODBC connection using Excel Services (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
You can use Excel to create OLE DB or ODBC connections and then share those connections with others. An OLE DB or ODBC connection is useful for connecting to data sources, such as Excel workbooks, legacy databases, or non-Microsoft databases. When you can upload a data connection to an Excel Services trusted data connection library in SharePoint Server 2013, the data connection is available for you and others to use to create data models, reports, scorecards, and dashboards. Depending on the particular data source that is used, people can easily refresh data in Excel Services workbooks so that the most current information is displayed.
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this task, review the following information about prerequisites:
  
- You must be using Excel 2016 and SharePoint Server 2013.
    
- Excel Services must be configured to include a trusted data connections library and a trusted documents library. Ideally, you'll have a Business Intelligence Center site configured that you can use for your data connections and workbooks. For more information, see [Configure a Business Intelligence Center in SharePoint Server 2013](/SharePoint/sharepoint-server).
    
- You must have at least Contribute permissions assigned in SharePoint Server 2013.
    
- You will need information from a SharePoint administrator about how data authentication is configured for the databases your organization uses. This can affect how you connect to different data sources. 
    
- You will need information about the data source that you want to use. In particular, you must know the data source name, user name, and password to connect to the data source.
    
- If you plan to publish workbooks that contain data models to SharePoint Server 2013, Excel Services must be configured to support data models. For more information, see [Configure Excel Services in SharePoint Server 2013 Preview](/SharePoint/administration/configure-excel-services).
    
## Step 1: Use Excel to create OLE DB or ODBC data connections
<a name="proc1"> </a>

You can use Excel to create an OLE DB or ODBC connection. This enables you to connect to lots of different data sources. Examples include Microsoft SQL Server, Microsoft Access, and Oracle databases, although there are many others. You can create an OLE DB or ODBC data connection by using one of several methods:
  
- You can create a connection by using the Data Connection Wizard in Excel. (This is the recommended method to use.)
    
- You can create a connection by using a Microsoft Query Wizard in Excel. 
    
Use the following procedures to create OLE DB or ODBC data connections
  
 **To create a connection by using the Data Connection Wizard in Excel**
  
1. In Excel, on the **Data** tab, in the **Get External Data** group, click **From Other Sources**, and then select **From Data Connection Wizard**.
    
    The Data Connection Wizard opens.
    
2. In the **What kind of data source do you want to connect to?** list, choose a data source, and then click **Next**.
    
3. Depending on the kind of data source that you selected, specify the necessary information for that data source.
    
    > [!TIP]
    > The information that you specify varies according to the data source. For example, a Data Feed data source requires a link or location to a data feed and logon credentials, whereas an Excel workbook data source requires you to locate where the workbook is stored. Contact a database administrator for specific details regarding the connection that you want to create. 
  
4. On the **Select Database and Table** page, in the **Select the database that contains the data that you want** list, select the database that you want to use. Do not click **Next** yet. 
    
5. On the **Select Database and Table** page, select the table (or tables) that you want to use, and then click **Next**. 
    
6. On the **Save Data Connection File and Finish** page, take the following steps: 
    
1. In the **File Name** box, keep or change the default file name. 
    
2. In the **Description** box, type a brief description for the data connection. 
    
3. In the **Friendly Name** box, keep the default name or type a new name for file. 
    
4. In the **Search Keywords** box, type some words or phrases that will help users find the data connection when it is published to SharePoint Server 2013. 
    
5. Next to **Excel Services**, click **Authentication Settings…**.
    
6. Select **None**, and then click **OK**.
    
7. Click **Finish** to close the **Save Data Connection File and Finish** page. 
    
7. On the **Import Data** page, click **Only Create Connection**, and then click **OK**.
    
8. Repeat steps 1-7 until you have created all the data connections that you want.
    
If cannot create the connection that you want by using the Data Connection Wizard in Excel, you can try to create the connection by using a Microsoft Query wizard. This is useful for connecting to older databases. However, the connection that you create might not be supported in Excel Services. Contact a SharePoint administrator to verify that the connection that you create is supported so that people can refresh data in Excel Services files. The following procedure describes how to create a connection by using a Microsoft Query wizard.
  
 **To create a connection by using a Microsoft Query wizard in Excel**
  
1. In Excel, on the **Data** tab, in the **Get External Data** group, click **From Other Sources**, and then select **From Microsoft Query**.
    
    The Choose Data Source dialog box appears.
    
2. Use the **Databases**, **Queries**, or **OLAP Cubes** tab to specify the data source that you want to use. 
    
    > [!TIP]
    > The information that you specify varies according to the data source. For example, if you select an Access database or an Excel file, you'll be prompted to navigate to the database or file on your computer. Or, if you choose to use a data source that is not listed, you'll be prompted to create a data source and then specify the kind of data source, location, and credentials to connect to it. Contact a database administrator for specific details regarding the connection that you want to create. 
  
3. On the **Import Data** page, click **Only Create Connection**, and then click **OK**.
    
4. Repeat steps 1-3 until you have created all the data connections that you want.
    
By default, the data connection is saved in the **My Data Sources** folder in the **Documents** library on your computer. 
  
## Step 2: Upload data connections to SharePoint Server
<a name="part2"> </a>

After data connections are created, the next step is to upload it to a data connection library. We recommend that you use a Business Intelligence Center site to store and manage business intelligence content, such as data connections. 
  
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

