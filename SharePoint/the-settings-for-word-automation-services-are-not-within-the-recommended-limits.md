---
title: The settings for Word Automation Services are not within the recommended limits (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 45d9570f-59d7-4f6b-b8e1-18868b27b0bc
---


# The settings for Word Automation Services are not within the recommended limits (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The settings for Word Automation Services are not within the recommended limits", in SharePoint Server 2016. **Rule Name:**   The settings for Word Automation Services are not within the recommended limits. **Summary:** The throughput of Word Automation Services is limited by system resources on the application server. If the values for conversion processes and conversion throughput are set too high, the overall health of the application server can degrade, and other services on the computer can be affected. Additionally, Word Automation Services can experience decreased throughput and more conversion failures. **Cause:** The settings for Word Automation Services are incorrect. **Resolution: Change the settings for Word Automation Services.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, in the list of service applications, click **Word Automation Services**.
    
  
4. In the **Conversion Processes** section, type a value that ranges from 1 to 1000 in the **Conversion processes** text box. The default conversion processes is set at 1.
    
  
5. In the **Conversion Throughput** section, type a value that ranges from 1 to 59 in the **Frequency with which to start conversions (minutes)** text box, and a value that ranges from 1 to 1000 in the **Number of conversions to start (per conversion process)** text box, and then click **OK**. The default conversion throughput is set at 15.
    
  

