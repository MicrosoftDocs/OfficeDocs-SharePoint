---
title: Manage Excel Services trusted data providers (SharePoint Server 2013)
ms.prod: SHAREPOINT
ms.assetid: 74b5c26f-a033-4d3a-a2ae-812ef043c3a7
---


# Manage Excel Services trusted data providers (SharePoint Server 2013)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-07-06* **Summary:** Add, configure, or delete Excel Services trusted data providers in SharePoint Server 2013.
> [!IMPORTANT:]

  
    
    

Trusted data providers are data providers from which Excel Services accesses data. A data provider is a database type combined with a protocol for accessing data (for example, SQL Server combined with ODBC). 
- Excel Services does not access data that does not come from a trusted data provider.
    
  
- Excel Services contains entries for common data providers. Add additional data providers as needed.
    
  
In this article:
-  [Add a trusted data provider](#proc1)
    
  
-  [Configure a trusted data provider](#proc2)
    
  
-  [Delete a trusted data provider](#proc3)
    
  

## Add a trusted data provider
<a name="proc1"> </a>

Use the following procedure to add a trusted data provider in Excel Services. **To add a trusted data provider**
1. In the Central Administration page, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.
    
  
3. On the Manage Excel Services page, click **Trusted Data Providers**.
    
  
4. On the Excel Services Application Trusted Data Providers page, click **Add Trusted Data Provider**.
    
  
5. On the Excel Services Application Add Trusted Data Provider page, in the **Provider** section, type the provider ID of the trusted data provider in the **Provider ID** box (for example, type SQL Server). Look in a valid connection string to find the provider ID.
    
  
6. Under **Provider Type**, select one of the following:
    
  - **OLE DB**    Select this option to access data by using Object Linking and Embedding (OLE).
    
  
  - **ODBC**    Select this option to access data by using Open Database Connectivity (ODBC).
    
  
  - **ODBC DSN**    Select this option to access data by using Open Database Connectivity with Data Source Name (ODBC DSN).
    
  
7. In the **Description** box, you can also type a description of the purpose for this trusted data provider.
    
  
8. Click **OK**.
    
  

## Configure a trusted data provider
<a name="proc2"> </a>

Use the following procedure to configure a trusted data provider in Excel Services. **To configure a trusted data provider**
1. In the Central Administration page, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.
    
  
3. On the Manage Excel Services page, click **Trusted Data Providers**.
    
  
4. On the Excel Services Application Trusted Data Providers page, click **Edit** on the menu of the data provider that you want to configure.
    
  

## Delete a trusted data provider
<a name="proc3"> </a>

Use the following procedure to delete a trusted data provider from Excel Services. **To delete a trusted data provider**
1. In the Central Administration page, in the **Application Management** section, click **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, click the Excel Services service application that you want to configure.
    
  
3. On the Manage Excel Services page, click **Trusted Data Providers**.
    
  
4. On the Excel Services Application Trusted Data Providers page, click **Delete** on the menu of the data provider that you want to delete.
    
  
5. Click **OK** in the message box that asks whether you want to continue with the deletion.
    
  

# See also

#### 

 **Configure Excel Online administrative settings**
  
    
    

  
    
    

