---
title: Databases used by SharePoint have outdated index statistics (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 25970085-39e6-4b1f-83c7-8687a5f8e939
---


# Databases used by SharePoint have outdated index statistics (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Databases used by SharePoint have outdated index statistics" for SharePoint Server 2016. **Rule Name:**   Databases used by SharePoint have outdated index statistics. **Summary:**   Outdated index statistics can decrease query performance and cause SharePoint Server 2016 to respond slowly. **Cause:** Index statistics in SharePoint Server 2016 databases are out of date.
> [!NOTE:]

  
    
    

 **Resolution: Edit the rule definition so that the configuration is automatically repaired.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the Central Administration Home page, click **Monitoring**.
    
  
3. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
  
4. On the Health Analyzer Rule Definitions – All Rules page, in the **Category: Performance** section, click the name of the rule.
    
  
5. In the **Health Analyzer Rule Definitions** dialog box, click **Edit Item**.
    
  
6. Select the **Repair Automatically** check box, and then click **Save**.
    
  

# See also

#### 

 [Index Statistics](http://go.microsoft.com/fwlink/?LinkID=761157&amp;clcid=0x409)
  
    
    

  
    
    

