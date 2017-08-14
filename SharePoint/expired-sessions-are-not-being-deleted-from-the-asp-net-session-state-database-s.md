---
title: Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 9983054b-ed90-491a-ac1d-cf95204f0931
---


# Expired sessions are not being deleted from the ASP.NET Session State database (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Expired sessions are not being deleted from the ASP.NET Session State database", for SharePoint Server 2016. **Rule Name:**    Expired sessions are not being deleted from the ASP.NET Session State database. **Summary:**    If expired sessions are not deleted, the server that hosts the ASP.NET Session State database may run out of disk space and the SharePoint farm may cease to function. **Cause:**    One or more of the following might be causing this:
- The SQL Server Agent service was stopped.
    
  
- SQL Server Express is installed.
    
    > [!IMPORTANT:]
      
 **Resolution:   Start the SQL Server Agent service**
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the database server that is hosting the ASP.NET Session State database.
    
  
2. In **SQL Server Configuration Manger**, start the **SQL Server Agent service**.
    
  

