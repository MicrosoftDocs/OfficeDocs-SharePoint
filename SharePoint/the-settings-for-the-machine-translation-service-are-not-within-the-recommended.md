---
title: The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: eb5d2d46-8bf6-43d7-add0-e9d61290a4d0
---


# The settings for the Machine Translation Service are not within the recommended limits (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The settings for the Machine Translation Service are not within the recommended limits" for SharePoint Server 2016. **Rule Name:**   The settings for the Machine Translation Service are not within the recommended limits. **Summary:** The throughput of the Machine Translation Service is limited by system resources on the application server. If the values for translation processes and translation throughput are set too high, the overall health of the application server can decrease, and other services on the computer can be affected. Additionally, the Machine Translation Service can experience decreased throughput and more translation failures. **Cause:**   The settings for the Machine Translation Service are incorrect. **Resolution: Change the settings for the Machine Translation Service.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
  
4. In the **Translation Processes** section, type a value that ranges from 1 to 1000 in the **Translation processes** box. The default value for Translation processes is set at 1.
    
  

## 


