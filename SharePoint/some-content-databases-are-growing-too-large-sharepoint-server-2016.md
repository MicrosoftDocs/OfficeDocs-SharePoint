---
title: Some content databases are growing too large (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 156f69fe-1831-472f-8e42-01c138d408ed
---


# Some content databases are growing too large (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Some content databases are growing too large", in SharePoint Server 2016. **Rule Name:**   Some content databases are growing too large. **Summary:**   The content databases have grown larger than 100 gigabytes (GB). Large content databases can be difficult to back up and restore. They are also more likely to cause the application to stop responding when you perform operations that affect entire databases. **Cause:** Content databases exceed 100 GB. **Resolution: Edit the rule definition to prevent new sites from being added to these databases, and then move some site collections to other databases.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
  
4. On the Health Analyzer Rule Definitions page, in the **Availability** category, click the name of the rule.
    
  
5. In the **Health Analyzer Rule Definitions** dialog box, click **Edit Item**, and then select the **Repair Automatically** check box.
    
  
6. Click **Save**. You can no longer add new sites to databases that exceed 100 GB.
    
  
7. Move some site collections to smaller databases. For more information, see  [Move site collections between databases in SharePoint Server](html/move-site-collections-between-databases-in-sharepoint-server.md).
    
  

