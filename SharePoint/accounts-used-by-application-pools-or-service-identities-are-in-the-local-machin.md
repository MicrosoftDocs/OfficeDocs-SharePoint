---
title: Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 5f0f9910-d851-4ffa-832b-f47558e4758c
---


# Accounts used by application pools or service identities are in the local machine Administrators group (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Accounts used by application pools or service identities are in the local machine Administrators group" for SharePoint Server 2016. **Rule Name:**   Accounts used by application pools or service identities are in the local machine Administrators group. **Summary:**   A user account that is used by application pools or services must have permissions of a domain user account and must not be a member of the Farm Administrators group or a member of the Administrators group on the local computer. Using highly privileged accounts for application pools or services poses a security risk to the farm, and could allow malicious code to execute. **Cause:**   Accounts that are used by application pools or services are members of the Administrators group on the local computer. **Resolution: Change the user account to a predefined account, or to a domain user account that is not a member of the Administrators group.**
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. On the Central Administration home page, in the **Security** section, click **Configure service accounts**.
    
  
3. On the Service Accounts page, in the **Select the component to update** list, click the application pool or service that uses the credentials of a member of the Administrators group on the local computer as its security account.
    
  
4. In the **Select an account** list, click an appropriate account for this component — for example, the predefined account  **Network Service**  — or click **Register new managed account**, and then on the Register Managed Account page, specify the credentials and the password change settings that you want.
    
  
5. Click **OK**.
    
  
For more information, see  [Account permissions and security settings in SharePoint Server 2016](html/account-permissions-and-security-settings-in-sharepoint-server-2016.md).
