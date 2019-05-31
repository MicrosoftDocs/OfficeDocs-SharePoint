---
title: "View diagnostic logs in SharePoint Server"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: ae1e3447-46e2-45f9-852a-ab39f23345d4
description: "Learn to view and filter log events by using Microsoft PowerShell, and view and export diagnostic logs by using the Out-GridView cmdlet."
---

# View diagnostic logs in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can troubleshoot problems in the farm by using data from the Unified Logging Service (ULS) logs in SharePoint Server . The ULS logs can collect data at varying levels depending on the logging settings. Use PowerShell to filter the data, display it in various ways, and output the data to a data grid with which you can filter, sort, group, and export data to Excel 2016.
  
  
## View and filter log events by using PowerShell
<a name="section1"> </a>

You can use PowerShell to view and filter log events. You cannot view or filter log events by using the SharePoint Central Administration website.
  
 **To view and filter log events by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Go to the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  - **All trace events**: 
    
  ```
  Get-SPLogEvent
  ```

  - **By level**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Level -eq "Information" }
  ```

  - **By area**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Area -eq <Area>}
  ```

    Where  _\<Area\>_ is the value of the **Area** property. 
    
  - **By category**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Category -eq <Category>
  ```

    Where  _\<Category\>_ is the value of the **Category** property. 
    
  - **By event ID**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.EventID -eq <EventID>}
  ```

    Where  _\<EventID\>_ is the value of the **EventID** property. 
    
  - **By message text**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Message -like "<string>"}
  ```

    Where  _\<string\>_ is the string found in the event message. 
    
  - **By process**: 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Process -like "<Process>"}
  ```

    Where  _\<Process\>_ is the value of the **Process** property. 
    
    By default, the command retrieves data from the default ULS log folder. To view and filter trace events that are on shared folder on a network, use the **Directory** parameter of the **Get-SPLogEvent** cmdlet. 
    
    To view more details about each trace event, use the **Format-List** cmdlet at the end of the command. For example, 
    
  ```
  Get-SPLogEvent | Where-Object {$_.Area -eq "SharePoint Foundation"} | Format-List
  ```

For more information, see [Get-SPLogEvent](/powershell/module/sharepoint-server/Get-SPLogEvent?view=sharepoint-ps). 
  
## View and export diagnostic logs by using the PowerShell Out-GridView cmdlet
<a name="section2"> </a>

PowerShell provides a powerful and easy-to-use feature that displays tabular data resulting from PowerShell commands in a filterable, searchable data grid in a separate window. You can use this grid to view log events and to perform the following operations on the data:
  
- Sort the data by any column.
    
- View the data in groups.
    
- Filter the data by Level, Area, Category, Message, Event ID, or Timestamp.
    
- Search the data for any string.
    
- Export raw or sorted or filtered data to a spreadsheet.
    
> [!NOTE]
> The **Out-GridView** cmdlet cannot be used with cmdlets that use the **Format** verb. The **Out-GridView** cmdlet receives objects whereas the cmdlets that use the **Format** verb return only formatted text. > You can view a subset of the data by using the **Where-Object** cmdlet that filters and passes the results to the **Out-GridView** cmdlet. For example,  `Get-SPLogEvent | Where-Object {$_.Area -eq "SharePoint Foundation"} | Out-GridView`. > If the grid is displaying more than several hundred rows, it might run slowly, especially if performing complex filtering operations. For faster performance, export the data to Excel 2016. 
  
 **To view and filter diagnostic logs by using Windows PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Go to the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command:
    
  ```
  Get-SPLogEvent | Out-GridView
  ```

4. To sort columns, click the column header.
    
5. To search for a specific string, type the string in the **Filter** box. Search is performed over all columns and rows. To clear the search, click **X**.
    
6. To filter data on only one criterion, type the following in the **Search** box: \<property name\>:\<value\>. For example, to search for all log entries raised by SharePoint Foundation 2013, type the following: Area:SharePoint Foundation. To clear the filter, click **X**.
    
7. To filter data by using more than one criterion or by using criteria with "contains, begins with, ends with" or other methods:
    
1. Click **Add criteria** button. 
    
2. Click the check box for the properties that you want to filter on, and then click **Add**.
    
3. Click **contains** to change to a different filter method. The methods that are available are **contains**, **does not contain**, **starts with**, **equals**, **does not equal**, **ends with**, **is empty**, and **is not empty**. 
    
4. Type a value in the text box.
    
5. Repeat steps "c" and "d" for each property that you selected in step "b".
    
6. When all the filtering criteria are specified, the data that satisfies the criteria will appear.
    
7. To clear a specific filter, click the **X** button. 
    
8. To clear all the filters, collapse the query view and then click the **Clear All** button. 
    
 **To export grid data to a spreadsheet**
  
1. Select the rows that you want to export. You can select multiple rows by using SHIFT+DRAG to select a block of rows, CTRL+CLICK to select specific rows, or CTRL+A to select all rows.
    
    You can also filter and sort the results before you copy the data into a spreadsheet. When you sort or filter data, only the resulting viewable data is copied over.
    
2. Copy the selected rows by using CTRL+C.
    
3. Open the spreadsheet workbook page, and then paste the copied rows into it by using CTRL+V.
    
For more information, see [Out-GridView](https://go.microsoft.com/fwlink/p/?LinkId=181248) and [Out-GridView Revisited](https://devblogs.microsoft.com/powershell/out-gridview-revisited/). 
  

