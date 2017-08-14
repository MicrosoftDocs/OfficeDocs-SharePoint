---
title: Use Visio Services with Secure Store Service in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 7c82bdf9-453f-4ee9-a2e6-20adf05ad59c
---


# Use Visio Services with Secure Store Service in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:** Secure Store can be used to store encrypted credentials for use in refreshing data-connected Visio diagrams in Visio Services.Visio Services can be configured to use the Secure Store Service to provide user authentication for data-connected diagrams that use an external data source such as SQL Server.
> [!NOTE:]

  
    
    

Secure Store provides a method of mapping users who do not have direct data access to an account that does have data access. Secure Store and Visio Services work together in the following basic sequence of events:
1. A user accesses a data-connected diagram on a SharePoint site.
    
  
2. Visio Services passes the user's identity to Secure Store.
    
  
3. Secure Store determines whether the user is authorized to access the data. If so, Secure Store returns the data access credentials to Visio Services.
    
  
4. Visio Services impersonates the data access credentials, accesses the data, and displays the data to the user.
    
  
Visio Services provides three methods of using Secure Store to provide data access:

  
    
    
> **Unattended Service Account:** The *unattended service account*  is an account that is used by Visio Services to provide broad database access to all users in the farm. Use the unattended service account for accessing data that is not considered sensitive or where you do not want to restrict access to a certain group of users. For information about how to configure this scenario, see [Configure Visio Services data refresh in SharePoint Server 2016 by using the unattended service account](html/configure-visio-services-data-refresh-in-sharepoint-server-2016-by-using-the-una.md).
    
  

  
    
    
> **External Data Connections:** You can specify a Secure Store target application in an Office Data Connection (ODC) file and then connect to that ODC file in Visio. When you publish the diagram to a SharePoint document library, it maintains its connection to the ODC file. The connection information in the ODC file is used when Visio Services refreshes the data in the workbook. Using an ODC file has the following advantages:
    
    - A single ODC file can be referenced by multiple diagrams. If the data source connection parameters change (for example, if you want to use a different Secure Store target application than the one originally specified) you need only update the ODC file and not the diagrams themselves.
    
  
    - Using ODC files allows administrators to create and maintain the data connections used by the organization. You can create data connections appropriate for users, place them in a trusted data connection library, and then notify the users of which ODC files to use for their queries.
    
  

    For information about how to configure this scenario, see  [Configure Visio Services data refresh in SharePoint Server by using external data connections](html/configure-visio-services-data-refresh-in-sharepoint-server-by-using-external-dat.md).
    
  
Visio, which is used to create the diagrams, does not use Secure Store for data authentication. You must configure direct data access for diagram authors. Once the diagram has been published to a SharePoint site, Visio Services can use Secure Store when it renders the diagram.
# See also

#### 

 [Secure Store for Business Intelligence service applications](html/secure-store-for-business-intelligence-service-applications.md)
  
    
    

  
    
    

