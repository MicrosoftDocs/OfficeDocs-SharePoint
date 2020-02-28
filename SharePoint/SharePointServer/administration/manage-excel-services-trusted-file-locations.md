---
title: "Manage Excel Services trusted file locations (SharePoint Server 2013)"
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
ms.assetid: 9ed8159f-9501-4ef3-8c84-5d775a1e6223
description: "Add, configure, or delete an Excel Services trusted file location in SharePoint Server 2013."
---

# Manage Excel Services trusted file locations (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]. 
  
A trusted file location is a SharePoint Server 2013 location, network file share, or Web folder address that the administrator has explicitly enabled workbooks to be loaded from. Excel Services only loads workbooks from trusted file locations.
  
Use the procedures in this article to configure trusted file locations for Excel Services.
  
To perform these procedures, you must be member of the Farm Administrators group or an Administrator for the Excel Services service application that you are configuring.
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server 2013 Enterprise. 
  
    
## Add a trusted file location
<a name="proc1"> </a>

Use the following procedure to add a trusted file location in Excel Services.
  
 **To add a trusted file location**
  
1. On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage service applications page, click the Excel Services service application that you want to configure.
    
3. On the Manage Excel Services Application page, click **Trusted File Locations**.
    
4. On the Excel Services Application Trusted File Locations page, click **Add Trusted File Location**.
    
5. Configure the settings for the trusted file location as described in [Configure a trusted file location](manage-excel-services-trusted-file-locations.md#proc2), below.
    
## Configure a trusted file location
<a name="proc2"> </a>

Use the following procedure to configure a trusted file location.
  
 **To configure a trusted file location**
  
1. On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage service applications page, click the Excel Services service application that you want to configure.
    
3. On the Manage Excel Services Application page, click **Trusted File Locations**.
    
4. In the **Address** column, click the trusted file location that you want to configure. 
    
5. Configure the settings as described in the following table:
    
|**Option**|**Description**|
|:-----|:-----|
|Address  <br/> |The location of the Excel documents that you want Excel Services to trust.  <br/> |
|Location Type  <br/> |If the document library is stored in the SharePoint Server 2013 content database, select **Microsoft SharePoint Foundation**. If the document library is stored in a network file share, select **UNC**. If the document library is stored in a Web folder address, select **HTTP**.  <br/> |
|Trust Children  <br/> |Select **Children trusted** if you want to trust all child libraries or directories.  <br/> |
|Description  <br/> |Text description of the file location you specified.  <br/> |
|Session Timeout  <br/> |Value in seconds that an Excel Calculation Services session can stay open and inactive before it is shut down, as measured from the end of each open request. The default is 450 seconds.  <br/> |
|Short Session Timeout  <br/> |Value in seconds that an Excel Services session stays open and inactive, before any user interaction, before it is shut down. This is measured from the end of the original open request. The default is 450 seconds.  <br/> |
|New Workbook Session Timeout  <br/> |Value in seconds that an Excel Calculation Services session for a new workbook stays open and inactive before it is shut down, as measured from the end of each request. The default value is 1,800 seconds (30 minutes).  <br/> |
|Maximum Request Duration  <br/> |Value in seconds for the maximum duration of a single request in a session. The default is 300 seconds.  <br/> |
|Maximum Chart Render Duration  <br/> |Value in seconds for the maximum time that is spent rendering any single chart. The default is 3 seconds.  <br/> |
|Maximum Workbook Size  <br/> |Value in megabytes (MB) for the maximum size of workbooks that Excel Calculation Services can open. The default size is 10 megabytes.  <br/> |
|Maximum Chart or Image Size  <br/> |Value in megabytes (MB) for the maximum size of charts or images that Excel Calculation Services can open. The default size is 1 megabyte.  <br/> |
|Volatile Function Cache Lifetime  <br/> |Value in seconds that a computed value for a volatile function is cached for automatic recalculations. The default is 300 seconds.  <br/> |
|Workbook Calculation Mode  <br/> |Select **File** to perform calculations as specified in the file.  <br/> Select **Manual** if you want recalculation to occur only when a Calculate request is received.  <br/> Select **Automatic** if you want any change to a value to cause the recalculation of all other values that depend on that value. Also, volatile functions are called if their time-out has expired.  <br/> Select **Automatic except data tables** if you want any change to a value to cause the recalculations of all other values dependent on that value (the values cannot be in a data table.) Also, volatile functions are called if their time-out has expired.  <br/> |
|Allow External Data  <br/> |Select **None** to disable all external data connections for the trusted file location.  <br/> Select **Trusted data connection libraries only** to only enable using connections to data sources that are stored in a trusted data connection library. The server will ignore settings embedded in the worksheet.  <br/> Select **Trusted data connection libraries and embedded** to enable connections that are embedded in the workbook file or connections that are stored in a trusted data connection library. If you do not have to have tight control or restrictions on the data connections that are used by workbooks on the server, consider selecting this option.  <br/> |
|Warn on Refresh  <br/> |Select the **Refresh warning enabled** check box to display a warning before refreshing external data for files in this location. When you select this option, you make sure that external data is not automatically refreshed without user interaction.  <br/> |
|Display Granular External Data Errors  <br/> |Select the **Granular External Data Errors** check box to display specific error messages when external data failures occur for files in this location. Displaying specific error messages can help troubleshoot data connectivity issues if they occur.  <br/> |
|Stop When Refresh on Open Fails  <br/> |Select the **Stopping open enabled** check box to prevent users from viewing files that are configured to refresh on open, if the refresh fails. This prevents users from seeing cached information in the workbook. This option is only effective if the user does not have Open Item permissions on the workbook. (A user with Open Item permissions on the workbook can open the workbook in Excel and thus has access to any cached information.)  <br/> |
|External Cache Lifetime (Automatic Refresh)  <br/> |In the **Automatic refresh (periodic / on-open)** box, type a value in seconds for the maximum time that the system can use external data query results for automatically refreshed external query results. The default is 300 seconds.  <br/> |
|External Cache Lifetime (Manual Refresh)  <br/> |In the **Manual refresh** box, type a value in seconds for the maximum time that the system can use external data query results for manually refreshed external query results. To prevent data refresh after the first query, type -1. The default is 300 seconds.  <br/> |
|Maximum Concurrent Queries Per Session  <br/> |Type a value for the maximum number of queries that can run at the same time during a single session. The default is 5 queries.  <br/> |
|Allow External Data Using REST  <br/> |Select the **Data refresh from REST enabled** check box to all requests from the REST API to refresh external data connections. Note that this setting has no effect if Allow External Data is set to **None**. Note too, that this setting has no effect if Warn on Refresh is enabled.  <br/> |
|Allow User-Defined Functions  <br/> |Select **User-defined functions allowed** if you want to allow user-defined functions in Excel Calculation Services for workbooks from this location.  <br/> |
   
6. Click **OK**.
    
## Delete a trusted file location
<a name="proc3"> </a>

Use the following procedure to delete a trusted file location.
  
> [!NOTE]
> Deleting a trusted file location does not affect the file location itself or its contents. It only removes the location from the Excel Services trusted location list, and Excel Services no longer loads workbooks from that location. 
  
 **To delete a trusted file location**
  
1. On the SharePoint Central Administration website home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage service applications page, click the Excel Services service application that you want to configure.
    
3. On the Manage Excel Services Application page, click **Trusted File Locations**.
    
4. On the Excel Services Application Trusted File Locations page, point to the trusted file location that you want to delete, click the arrow that appears, and then click **Delete**.
    
5. Click **OK** in the message box that asks whether you want to continue with the deletion. 
    
## See also
<a name="proc3"> </a>

#### Other Resources

[Configure Excel Services in SharePoint](/SharePoint/administration/configure-excel-services)

