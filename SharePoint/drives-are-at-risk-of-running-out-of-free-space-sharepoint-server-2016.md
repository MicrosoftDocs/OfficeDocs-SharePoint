---
title: Drives are at risk of running out of free space (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: ac16bc32-f623-4658-8bc5-6e6b958629a4
---


# Drives are at risk of running out of free space (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Drives are at risk of running out of free space" for SharePoint Server 2016. **Rule Name:**   Drives are at risk of running out of free space. **Summary:**    This rule checks disk space as a proportion of the RAM that is installed on the SharePoint Server. Servers with large amounts of RAM are more likely to experience a failure of this rule. **Cause:**   When disk space is less than five times the RAM on the server, this health rule triggers a warning. For example, if your SharePoint Server has 16GB of RAM installed, the rule checks for 80GB of free space on the disk. **Resolution: Free disk space on the server**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On Server Manager, click **Tools**, and then click **Disk Cleanup**.
    
  
 **Resolution: Decrease the number of days to store log files**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.
    
  
3. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.
    
  
4. Click **OK**.
    
  

