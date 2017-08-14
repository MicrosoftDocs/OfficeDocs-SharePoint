---
title: Use Visio Services with SharePoint lists
ms.prod: SHAREPOINT
ms.assetid: 9d89800f-7ebb-4454-9e0a-779ba1737d04
---


# Use Visio Services with SharePoint lists
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-07* You can connect a Visio diagram to the data in a SharePoint list and maintain that connection when you publish the diagram to SharePoint Server 2013 or SharePoint Server 2016.To connect to the SharePoint list from Visio, you must have at least Read access to the SharePoint list. Likewise, once the diagram has been published to a SharePoint document library, viewers must have Read access to the list in order to refresh the data from the list.
> [!NOTE:]

  
    
    


## Publishing a diagram connected to a SharePoint list

Publishing a data-connected diagram that is connected to a SharePoint list consists of two steps:
- Create the diagram in Visio and connect shapes in the diagram to the data in the SharePoint list
    
  
- Publish the diagram to a SharePoint document library
    
  
 **To connect a Visio diagram to a SharePoint list**
1. In Visio, open the diagram that you want to connect to the SharePoint list, or create a new diagram.
    
  
2. On the **Data** tab, click **Link Data to Shapes**.
    
  
3. On the Data selector page, select the **Microsoft SharePoint Foundation list** option, and then click **Next**.
    
  
4. On the Select a site page, in the **Site** box, type the URL for the SharePoint site where the SharePoint list is located, and then click **Next**.
    
  
5. On the Select a list page, in the **Lists** list, select the list to which you want to connect, and then click **Next**.
    
  
6. Click **Finish**.
    
  
Once you have connected to the SharePoint list, you can drag the data rows onto the page to link data to your existing shapes, or add new shapes. When you have completed the diagram, you can save it to a SharePoint document library and render it with Visio Services. **To publish a diagram to a SharePoint document library**
1. In Visio, click **File**.
    
  
2. Click **Save**, and then browse to a SharePoint document library.
    
  
3. Type a file name, and then click **Save**.
    
  
4. Once the diagram has been saved to the SharePoint document library, you can view the diagram by clicking it directly or by configuring it to appear in a Visio Web Access Web Part. The diagram remains connected to the data in the SharePoint list, and the data refreshes based on the refresh settings that you have configured for Visio Services and for the Visio Web Access Web Part, if applicable.
