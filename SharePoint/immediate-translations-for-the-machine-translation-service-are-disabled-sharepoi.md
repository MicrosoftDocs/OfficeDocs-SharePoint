---
title: Immediate translations for the Machine Translation service are disabled (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 987f22e3-53cc-4e6a-93e7-0851af4f31db
---


# Immediate translations for the Machine Translation service are disabled (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Immediate translations for the Machine Translation service are disabled", in SharePoint Server 2016. **Rule Name:**   Immediate translations for the Machine Translation service are disabled. **Summary:** There are several features in SharePoint Server 2016 that rely on the Machine Translation Service synchronous translation mode. If immediate translations are disabled, these features don't function correctly. **Cause:**   Synchronous translations for the Machine Translation service are disabled. **Resolution: Enable synchronous translations for the Machine Translation service.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
  
4. In the **Maximum Synchronous Translation Requests** section, type a value that ranges from 1 to 1000 in the **Maximum number of synchronous translation requests (per server)** text box. A value of 0 indicates that synchronous translations are disabled.
    
  

