---
title: View diagnostic logs in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: ae1e3447-46e2-45f9-852a-ab39f23345d4
---


# View diagnostic logs in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-08* **Summary:** Learn to view and filter log events by using Windows PowerShell, and view and export diagnostic logs by using the **Out-GridView** cmdlet.You can troubleshoot problems in the farm by using data from the Unified Logging Service (ULS) logs in SharePoint Server . The ULS logs can collect data at varying levels depending on the logging settings. Use PowerShell to filter the data, display it in various ways, and output the data to a data grid with which you can filter, sort, group, and export data to Excel 2016.In this article:
## In this article


-  [View and filter log events by using Windows PowerShell](#section1)
    
  
-  [View and export diagnostic logs by using the Windows PowerShell Out-GridView cmdlet](#section2)
    
  

## View and filter log events by using Windows PowerShell
<a name="section1"> </a>

You can use PowerShell to view and filter log events. You cannot view or filter log events by using the SharePoint Central Administration website. **To view and filter log events by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.
    
    > [!NOTE:]
      
2. Go to the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  - **All trace events:**
    
  ```
  
Get-SPLogEvent
  ```

  - **By level:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.Level -eq "Information" }
  ```

  - **By area:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.Area -eq <Area> }
  ```


    Where  *<Area>*  is the value of the **Area** property.
    
  
  - **By category:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.Category -eq <Category>
  ```


    Where  *<Category>*  is the value of the **Category** property.
    
  
  - **By event ID:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.EventID -eq <EventID> }
  ```


    Where  *<EventID>*  is the value of the **EventID** property.
    
  
  - **By message text:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.Message -like "<string> "}
  ```


    Where  *<string>*  is the string found in the event message.
    
  
  - **By process:**
    
  ```
  Get-SPLogEvent | Where-Object {$_.Process -like "<Process> "}
  ```


    Where  *<Process>*  is the value of the **Process** property.
    
  

    By default, the command retrieves data from the default ULS log folder. To view and filter trace events that are on shared folder on a network, use the **Directory** parameter of the **Get-SPLogEvent** cmdlet.
    
    To view more details about each trace event, use the **Format-List** cmdlet at the end of the command. For example,
    


  ```
  Get-SPLogEvent | Where-Object {$_.Area -eq "SharePoint Foundation"} | Format-List
  ```

For more information, see **Get-SPLogEvent**.
## View and export diagnostic logs by using the Windows PowerShell Out-GridView cmdlet
<a name="section2"> </a>

PowerShell provides a powerful and easy-to-use feature that displays tabular data resulting from Microsoft PowerShell commands in a filterable, searchable data grid in a separate window. You can use this grid to view log events and to perform the following operations on the data:
- Sort the data by any column.
    
  
- View the data in groups.
    
  
- Filter the data by Level, Area, Category, Message, Event ID, or Timestamp.
    
  
- Search the data for any string.
    
  
- Export raw or sorted or filtered data to a spreadsheet.
    
  

> [!NOTE:]

  
    
    

 **To view and filter diagnostic logs by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions.
    
    > [!NOTE:]
      
2. Go to the SharePoint Management Shell.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPLogEvent | Out-GridView
  ```

4. To sort columns, click the column header.
    
  
5. To search for a specific string, type the string in the **Filter** box. Search is performed over all columns and rows. To clear the search, click **X**.
    
  
6. To filter data on only one criterion, type the following in the **Search** box: **<property name>:<value>**. For example, to search for all log entries raised by SharePoint Foundation 2013, type the following: **Area:SharePoint Foundation**. To clear the filter, click **X**.
    
  
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
    
  
For more information, see  [Out-GridView](https://go.microsoft.com/fwlink/p/?LinkId=181248) (https://go.microsoft.com/fwlink/p/?LinkId=181248) and [Out-GridView Revisited](https://go.microsoft.com/fwlink/p/?LinkId=181249) (https://go.microsoft.com/fwlink/p/?LinkId=181249).
