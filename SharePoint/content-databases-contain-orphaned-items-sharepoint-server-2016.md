---
title: Content databases contain orphaned items (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 636d25e9-be42-4b66-a354-9b9af570f907
---


# Content databases contain orphaned items (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Content databases contain orphaned items" for SharePoint Server 2016. **Rule Name:**   Content databases contain orphaned items. **Summary:**    The SharePoint Health Analyzer has detected some sites in a content databases that are not referenced in the configuration database. These sites may not be accessible. **Cause:**   A restore operation that was not completed can result in sites in a content database that are not referenced in the SharePoint configuration database. **Resolution: Decrease the number of days to store log files**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Monitoring**, in the **Health Analyzer** section, click **Review problems and solutions**.
    
  
3. On the Review problems and solutions page, click the alert for the failing rule, and then click **Fix Now**. Keep the dialog box open so you can run the rule again to confirm the resolution.
    
    > [!NOTE:]
      
4. After following the steps in the **Remedy** section, in the **Review problems and solutions** dialog box for the alert, click **Re-analyze Now** to confirm the resolution. If the problem is resolved, the rule is not flagged as a failing rule on the Review problems and solutions page.
    
  

