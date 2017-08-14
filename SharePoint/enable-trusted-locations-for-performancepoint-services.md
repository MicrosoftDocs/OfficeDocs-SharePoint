---
title: Enable trusted locations for PerformancePoint Services
ms.prod: SHAREPOINT
ms.assetid: 7eea752e-5bdc-48b1-99cb-05e6c3669c4a
---


# Enable trusted locations for PerformancePoint Services
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-06* **Summary:**   Learn how to limit PerformancePoint Services features that use trusted locations by allowing only designated sites, lists or document libraries rather than the entire site collection.After you enable a feature on a site collection in SharePoint Server, the content types or PerformancePoint Services objects are made available for others to use on any site within that site collection. An administrator may want to limit PerformancePoint Services features that use trusted locations by allowing one or more sites, lists, or document libraries rather than an entire site collection. In this way the administrator can limit use of PerformancePoint Services to specific locations in the farm to prevent unauthorized access to data sources. See  [To add a trusted data source location](#proc1).
## Establish trusted locations for data sources and dashboard content
<a name="establish_trusted_locations"> </a>

You can specify locations in SharePoint Server where dashboard content and data sources are secured. The default is to trust all locations, but administrators can specify other trusted locations.
- **PerformancePoint Content List:** A PerformancePoint Content List stores the elements that are used to construct a dashboard. A PerformancePoint Services dashboard is a related group of interactive scorecards, filters, and report views organized into a set of Web pages.
    
  
- **PerformancePoint Data Source Library:** A PerformancePoint Data Source Library contains data-source definitions that identify a source of business data. It may include cubes or perspectives based on online analytical processing (OLAP) cubes, relational databases, CSV files, and Microsoft Excel Services worksheets.
    
  
- **Trusted Data Sources and Trusted Content Locations:** When you navigate to either Trusted Data Sources or Trusted Content Locations pages from the Manage PerformancePoint Services page, there are two option buttons. When the **Only specific locations** option button is selected, the list of trusted locations is enabled. For data source or content locations, if there are no items in the list, only the toolbar button is enabled. When one or more items are listed, the **Edit** and **Delete** buttons are enabled.
    
    The URL you type is checked for a valid site collection, site, document library, and list. Option buttons are enabled or disabled depending on the type of site. Validation depends on whether your URL is a valid site and/or already exists. 
    
  

> [!CAUTION:]

  
    
    

 **To add a trusted data source location**
1. On the SharePoint Central Administration website, select **Manage Service Applications**.
    
  
2. On the Manage Service Applications page, select the PerformancePoint Services service application you want to manage.
    
  
3. On the **Service Application** tab, click **Manage**. The Manage PerformancePoint Services page opens.
    
  
4. Click **Trusted Data Source Locations**. The Trusted Data Source Locations page opens.
    
  
5. Select one of the following options and click **Apply**.
    
1. **All SharePoint locations:** Specifies that data sources are trusted from all SharePoint Server locations.
    
  
2. **Only specific locations:** Specifies that data sources are only trusted when found in the locations listed.
    
  
6. If you select **Only specific locations** and click **Apply**, **Add Trusted Data Source Location** appears; otherwise **All SharePoint locations** is the current setting.
    
  
7. Click **Add Trusted Data Source Location** to specify the URL and location for this trusted location.
    
  
8. Enter the full Web address (it must be a site collection, site, or document library for this trusted location).
    
  
9. Select the location type, type a description (optional), and then click **OK**. The location type appears under **Location**.
    
  
 **To add a trusted content location**
1. In Central Administration select **Manage Service Applications**.
    
  
2. In the Manage Service Applications page, select the PerformancePoint Services service application you want to manage.
    
  
3. On the **Service Application** tab, click **Manage**. The Manage PerformancePoint Services page opens.
    
  
4. Click **Trusted Content Locations**. The Trusted Content Locations page opens.
    
  
5. Select one of the following options, and then click **Apply**.
    
1. **All SharePoint locations:** Specifies that content is trusted from all SharePoint Server locations.
    
  
2. **Only specific locations:** Specifies that content is only trusted when found in the locations listed.
    
  
6. If you select **Only specific locations** and click **Apply**, **Add Trusted Content Location** appears; otherwise **All SharePoint locations** is the current setting.
    
  
7. Click **Add Trusted Content Location** to specify the URL and location for this trusted location.
    
  
8. Enter the full Web address (it must be a site collection, site, or list address for this trusted location.)
    
  
9. Select the location type, type a description (optional), and then click **OK**. The location type appears under **Location**.
    
  

