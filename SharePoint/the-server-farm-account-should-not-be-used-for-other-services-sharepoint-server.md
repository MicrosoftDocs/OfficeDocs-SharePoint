---
title: The server farm account should not be used for other services (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 57592cbe-47c1-44c7-8f57-38fa192df4f7
---


# The server farm account should not be used for other services (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The server farm account should not be used for the other services" for SharePoint Server 2016. **Rule Name:**   The server farm account should not be used for the other services. **Summary:**   The account that is used to run the SharePoint Server 2016 Timer service and other system services in the SharePoint farm should not be used for other services in the farm. **Cause:**   The farm account, which is used for the SharePoint Server 2016 Timer service and the SharePoint Central Administration website, is highly privileged and should not be used for other services on any computers in the server farm. Services in the farm were found to use this account.
> [!NOTE:]

  
    
    

 **Resolution: Change the account that is used for other services.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. In Central Administration , in the **Security** section, click **Configure service accounts**.
    
  
3. On the Service Accounts page, in the **Credential Management** section, in the drop-down list, click the service that you want to update credentials.
    
  
4. In the **Select an account for this component** list, click the domain account that you want to associate with this service.
    
  
5. If you want to register the account that you selected on the SharePoint Server 2016 farm, click **Register new managed account**.
    
  
6. Click **OK**.
    
  
For more information, see  [Account permissions and security settings in SharePoint Server 2016](html/account-permissions-and-security-settings-in-sharepoint-server-2016.md).
