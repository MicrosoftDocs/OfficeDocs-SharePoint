---
title: Verify each User Profile service application has a My Site host configured (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 2689bb6a-fd05-4273-87eb-daac5b2722f3
---


# Verify each User Profile service application has a My Site host configured (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Verify each User Profile service application has a My Site Host configured" in SharePoint Server 2016. **Rule Name:**    Verify each User Profile service application has a My Site Host configured. **Summary:**    Without a My Site host, end-users are not able to use personal sites or people profiles. Therefore, we recommend that if you create a User Profile Service service application, you also create a My Site host for the User Profile Service. **Symptoms:**    My Sites and other people profile features are not available to users. **Cause:**    The administrator who created the User Profile Service service application did not also create a My Site host. **Resolution:   Verify that a My Site site collection has been created**
- For information about setting up a My Site site collection, see  [Configure My Sites in SharePoint Server](html/configure-my-sites-in-sharepoint-server.md).
    
  
 **Resolution:   Associate the My Site host with a User Profile Service service application by using Microsoft PowerShell**
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2016 cmdlets.
    
    > [!NOTE:]
      
2. Start the SharePoint 2016 Management Shell.
    
    For Windows Server 2012 R2, on the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    For more information about how to interact with Windows Server 2012 R2, see  [Common Management Tasks and Navigation in Windows](http://go.microsoft.com/fwlink/?LinkID=715712&amp;clcid=0x409).
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Set-SPProfileServiceApplication [-Name <UserProfileServiceApplicationName> ] -MySiteHostLocation <URL>
  ```


    
    
    Where:
    
  -  *<UserProfileServiceApplicationName>*  is the friendly name of the User Profile Service service application. If you only have one User Profile Service service application, you do not need to specify the name.
    
  
  -  *<URL>*  is URL of an empty site collection that has no templates associated with it.
    
  

