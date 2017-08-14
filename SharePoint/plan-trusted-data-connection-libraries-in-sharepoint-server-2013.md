---
title: Plan Trusted Data Connection Libraries in SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: cbb210e8-2969-4fd5-a82d-08ad1996c5b4
---


# Plan Trusted Data Connection Libraries in SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-06-23* **Summary:** Use Excel Services trusted data connection libraries to manage and secure data connections for Excel Services in SharePoint Server 2013.Excel Services provides the ability to connect to external data sources and refresh the data in data-connected Excel workbooks when it renders them in a browser. Data connections can be loaded by using information from the workbook file, but using a data connection library provides an additional layer for data connections so that they can be managed separately from workbooks. *Trusted data connection libraries*  are SharePoint Server 2013 data connection libraries that contain data connection files that Excel Services will trust to use to connect to databases. These files contain everything that Excel Services and Excel client have to have to connect to an external data source.Data connection libraries enable broad reuse and sharing of data connections. By using trusted data connection libraries with Excel Services, you can create, deploy, and manage the data connections that your users use. By managing connections in this way, you can ensure that connections are configured correctly and maintained properly and that your users are all using a consistent group of connection files that have been created and approved by authorized users and administrators.Excel Services does not use data connection files that are not stored in a trusted data connection library. However, data connection information can be embedded directly in a workbook that is trying to make a connection.You can create different trusted data connection libraries for different purposes or projects, and you can customize the settings and permissions to the libraries accordingly.For workbooks that use the same data connection file, changing the data connection file is all that is required to change connection information; changing the individual workbooks is not necessary.Initially, there are no Excel Services trusted data connection libraries. To store data connection files, you must create at least one trusted data connection library.For information about creating trusted data connection libraries, see  [Manage Excel Services trusted data connection libraries (SharePoint Server 2013)](html/manage-excel-services-trusted-data-connection-libraries-sharepoint-server-2013.md).
# See also

#### 

 [Plan Trusted File Locations in SharePoint Server 2013](html/plan-trusted-file-locations-in-sharepoint-server-2013.md)
  
    
    

  
    
    

