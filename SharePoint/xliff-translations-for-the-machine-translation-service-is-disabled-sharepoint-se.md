---
title: XLIFF translations for the Machine Translation Service is disabled (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: c145579b-fc8b-4ab4-bc80-95c3202deae2
---


# XLIFF translations for the Machine Translation Service is disabled (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "XLIFF translation for the Machine Translation Service is disabled" in SharePoint Server 2016. **Rule Name:**   XLIFF translation for the Machine Translation Service is disabled. **Summary:** There are several features in SharePoint Server 2016 that rely on the Machine Translation Service processing the XLIFF file format. If the .xlf extension is disabled, these features don't function correctly. **Cause:**   The .xlf file name extension is disabled for the Machine Translation Service. **Resolution: Enable the .xlf file name extension for the Machine Translation Service.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Manage Service Applications page, in the list of service applications, click **Machine Translation Service**.
    
  
4. In the **Enabled File Extensions** section, select the check box for the .xlf file name extension under the **XLIFF Parser**.
    
  
5. Click **OK**.
    
  

