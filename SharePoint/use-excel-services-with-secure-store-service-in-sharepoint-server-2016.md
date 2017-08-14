---
title: Use Excel Services with Secure Store Service in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 2d11e10c-c224-46a6-8c03-07913b38c13e
---


# Use Excel Services with Secure Store Service in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-06* **Summary:** Learn about the options available for using the Secure Store Service with Excel Services in SharePoint Server 2013 to refresh data from external data sources.This series of articles describes how to configure data refresh in Excel Services in SharePoint Server 2013 by using the Secure Store Service to map user and group credentials to the credentials of external data sources.In Secure Store you specify a group of users to whom you want to grant access to a data source and a set of credentials that has access to that data source. The user information is stored in a Secure Store  *target application*  and the associated credentials are stored, encrypted, in the Secure Store database. You can then specify the target application in a workbook, an Office Data Connection (ODC) file, or in Excel Services Global Settings, and Excel Services will use the stored credentials on behalf of the specified users to refresh data in a data-connected workbook.
> [!NOTE:]

  
    
    

Excel Services can be used with Secure Store in three primary scenarios:

  
    
    
> **Unattended Service Account:** The *unattended service account*  is an account that is used by Excel Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see [Configure Excel Services data refresh by using the unattended service account in SharePoint Server 2016](html/configure-excel-services-data-refresh-by-using-the-unattended-service-account-in.md).
    
  

  
    
    
> **Embedded Connections:** In Excel, you can specify a Secure Store target application directly in the workbook. When the workbook is published to a SharePoint document library and then rendered by using Excel Services, the specified target application is used to refresh the data. For information about how to configure this scenario, see **Configure Excel Online data refresh by using embedded data connections in Office Online Server**.
    
  

  
    
    
> **External Data Connections:** You can specify a Secure Store target application in an Office Data Connection (ODC) file and then connect to that ODC file in Excel. When you publish the workbook to a SharePoint document library, it maintains its connection to the ODC file. The connection information in the ODC file is used when Excel Services refreshes the data in the workbook. Using an ODC file has the following advantages:
    
    - A single ODC file can be referenced by multiple workbooks. If the data source connection parameters change (for example, if you want to use a different Secure Store target application than the one originally specified) you need only update the ODC file and not the workbooks themselves.
    
  
    - Using ODC files allows administrators to create and maintain the data connections that are used by the organization. You can create data connections appropriate for users, place them in a trusted data connection library, and then notify the users of which ODC files to use for their queries.
    
  

    For information about how to configure this scenario, see **Configure Excel Online data refresh by using external data connections in Office Online Server**.
    
  

