---
title: Drives are running out of free space (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 6ed5b73c-6403-46ea-9d56-f42d972e7748
---


# Drives are running out of free space (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Drives are running out of free space" for SharePoint Server 2016. **Rule Name:**   Drives are running out of free space. **Summary:**    Disk drives on one or more of the servers in the SharePoint Server farm are running out of disk space.
> [!NOTE:]

  
    
    

 **Resolution: Free disk space on the server**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Server Manager, click **Tools**, and then click **Disk Cleanup**.
    
  
 **Resolution: Decrease the number of days to store log files**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Reporting** section, click **Configure diagnostic logging**.
    
  
3. On the Diagnostic Logging page, in the **Trace Log** section, in the **Number of days to store log files** box, type a smaller number.
    
  
4. Click **OK**.
    
  

