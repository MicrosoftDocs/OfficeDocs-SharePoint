---
title: Built-in accounts are used as application pool or service identities (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 5ed9fe7c-48c5-4511-aab4-aa58a440954d
---


# Built-in accounts are used as application pool or service identities (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Built-in accounts are used as application pool or service identities" for SharePoint Server 2016. **Rule Name:**   Built-in accounts are used as application pool or service identities. **Summary:**    Built-in or local computer accounts are used as an application pool identity or service identity. **Cause:**   Using built-in accounts as application pool identities or as service identities is not supported in a farm configuration. Build-in accounts include Network Service, Local Service, and Local System. **Resolution: Change the identity that is used for the service or application pool**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the SharePoint Central Administration website, click **Security**.
    
  
3. On the Security page, in the **General Security** section, click **Configure service accounts**.
    
  
4. On the Service Accounts page, in the **Credential Management** section, in the upper drop-down list, click the service or application pool for which you want to change the identity.
    
  
5. In the **Select an account for this component** list, click the domain user account that you want to associate with the service or application pool.
    
    If you want to register the account that you selected on the SharePoint Server 2016 farm, click **Register new managed account**.
    
  
6. Click **OK**.
    
  

