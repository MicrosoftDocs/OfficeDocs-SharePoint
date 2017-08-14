---
title: Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 85aa1c35-1322-42ad-a625-1496aee67858
---


# Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state" in SharePoint Server 2016. **Rule Name:**   Databases within this farm are set to read only and will fail to upgrade unless it is set to a read-write state. **Summary:**   The databases are set to read-only and cannot be upgraded. **Cause:** The databases are set to read-only. **Resolution: Set the databases to read-write using SQL Server.**
1. Verify that the user account that is performing this procedure is a member of the **db_owner** fixed database role in each database.
    
  
2. Start SQL Server Management Studio.
    
  
3. Right-click the content database that you want to make read-only, and then click **Properties**.
    
  
4. Select the **Options** page, and, in the **Other options** list, scroll to the **State** section.
    
  
5. In the **Database Read-Only** row, click the arrow next to **True**, select **False**, and then click **OK**.
    
  
6. Repeat for all other content databases.
    
    > [!NOTE:]
      

