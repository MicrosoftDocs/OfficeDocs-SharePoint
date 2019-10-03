---
title: "Maintain user profile synchronization settings in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/2/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 26f02074-af0b-4548-ab68-9d46dd05b8ff
description: "Learn how to maintain User Profile synchronization settings in SharePoint Server  after you configure User Profile synchronization."
---

# Maintain user profile synchronization settings in SharePoint Server

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Profile synchronization in SharePoint Server enables an administrator of an instance of the User Profile service to synchronize user and group profile information that is stored in the SharePoint Server profile store with profile information that is stored in directory services across the enterprise. After you have configured User Profile synchronization, you must complete tasks to maintain those settings. These tasks include, for example, removing users whose accounts are disabled or deleted, moving or renaming a server, and starting or stopping the User Profile Synchronization service. For more information, see [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md).
  
To run the PowerShell cmdlets in this article, verify that you have the following memberships:
  
- **securityadmin** fixed server role on the SQL Server instance. 
    
- **db_owner** fixed database role on all databases that are to be updated. 
    
- Administrators group on the server on which you are running the PowerShell cmdlets.
    
> [!IMPORTANT]
> Each section is noted as to the version of SharePoint Server it applies to.
  
    
## Rename users or change user domains
<a name="acctName"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013, 2016, and 2019.

SharePoint Server lets you handle several different user migration scenarios. The following are examples of the scenarios handled for Active Directory Domain Services (AD DS):
  
-  Account name ( **sAMAccountName**) changes in the AD DS where the user exists.
    
- Security Identifier (SID) changes.
    
- Distinguished name (DN) changes that include changes in the organizational unit (OU) container in the AD DS where the user account exists. For example, if a user's distinguished name is moved in AD DS from "User= EUROPE\John Smith, Manager=CN=John Rodman, OU=Users, DC=EMEA1, DC=corp, DC=contoso, DC=com" to "User= EUROPE\John Smith, Manager=CN=John Rodman, OU=Managers, DC=EMEA1, DC=corp, DC=contoso,DC=com", the **MigrateUser** command updates the user profile store for this user. The user profile for John Smith is updated when synchronizing user profiles from the EMEA1.corp.contoso.com AD DS to the SharePoint Server user profile store. 
    
 **To rename users or to change user domains**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer on which you installed the User Profile synchronization service.
    
2. If synchronization is in progress, open Central Administration and then click **Manage service applications** in the **Application Management** section. Select the appropriate User Profile service application from the list of service applications. On the **Manage service application** page, click **Stop Profile Synchronization**.
    
3. Disable the User Profile Incremental Synchronization timer job.
    
4. Ensure that user migration by using  `stsadm -o migrateuser` has succeeded.

>[!NOTE]
>[Move-SPUser](https://docs.microsoft.com/en-us/powershell/module/sharepoint-server/move-spuser) can also be used to migrate users.
    
5. Ensure that the profile of the migrated user can be accessed by browsing to the My Site for that user, for example, http://mysite/person.aspx?accountname=\<new account name\>.
    
6. Run User Profile synchronization. For more information, see[Start profile synchronization manually in SharePoint Server](start-profile-synchronization-manually.md).
    
7. Recheck access to the profile of the migrated user by browsing to the My Site for that user.
    
8. Enable the User Profile Incremental Synchronization timer job.
    
## Exclude users whose accounts are disabled
<a name="disabledUsers"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013.

You can exclude users whose accounts are disabled in AD DS by using exclusion filters in SharePoint Server 2013. For the steps that are needed to exclude users whose accounts are disabled, see [Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md).
  
## Remove obsolete users and groups
<a name="RemoveObsUsers"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013, 2016, and 2019.

There are two reasons why obsolete users or groups can exist in the SharePoint Server user profile store:
  
- **Obsolete users**: The My Site cleanup timer job is not active. The User Profile Synchronization timer job marks for deletion users who have been deleted from the directory source. When the My Site cleanup job runs, it looks for all users marked for deletion and deletes their profiles. Respective My Sites are then assigned to the manager for the deleted user and an e-mail message notifies the manager of this deletion.
    
- **Obsolete users and groups**: Users and groups that were not imported by Profile Synchronization exist in the user profile store. This can occur, for example, if you upgraded from an earlier version of SharePoint Server and chose to only synchronize a subset of domains with SharePoint Server.
    
 **To find and remove obsolete users and groups by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - Execute permission on the **ImportExport_GetNonimportedObjects** and the **ImportExport_PurgeNonimportedObjects** stored procedures in the profile database. 
    
2. Start the SharePoint Management Shell.
    
3. At the PowerShell command prompt, do the following:
    
1. To get the User Profile Service application object, type the following command:
    
  ```
  $upa = Get-spserviceapplication <identity>
  ```

    Where  _\<identity\>_ is the GUID of the User Profile synchronization service application. 
    
2. To view the users and groups to delete, type the following command:
    
  ```
  Set-SPProfileServiceApplication $upa -GetNonImportedObjects $true
  ```

3. To delete the obsolete users and groups, type the following command:
    
    > [!CAUTION]
    > This action cannot be undone. 
  
  ```
  Set-SPProfileServiceApplication $upa -PurgeNonImportedObjects $true
  ```

For more information, see [Get-SPServiceApplication](/powershell/module/sharepoint-server/Get-SPServiceApplication?view=sharepoint-ps) and [Set-SPProfileServiceApplication](/powershell/module/sharepoint-server/Set-SPProfileServiceApplication?view=sharepoint-ps).
  
## Maintain profile schema changes
<a name="schemaChanges"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013.

Profile schema changes include things such as adding a new user profile property, changing a user profile property mapping, or changing a Profile Synchronization connection filter. When the profile schema changes, you must first perform a full nonrecurring synchronization before scheduling recurring profile synchronization. For the steps that are needed to perform full nonrecurring profile synchronization, see[Start profile synchronization manually in SharePoint Server](start-profile-synchronization-manually.md).
  
## Rename a server that is running the User Profile synchronization service
<a name="RenameServer"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013.

Use the following procedure to rename a profile synchronization server.
  
 **To rename a server that is running the User Profile synchronization service by using PowerShell**
  
1. Start the SharePoint Management Shell.
    
2. At the PowerShell command prompt, type the following command:
    
  ```
  Rename-SPServer <Identity> -Name <newName>
  ```

    Where:
    
  -  _Identity_ is the old name of the server. 
    
  -  _newName_ is the new name for the server. 
    
For more information about renaming a server by using Microsoft PowerShell, see [Rename-SPServer](/powershell/module/sharepoint-server/Rename-SPServer?view=sharepoint-ps).
  
## Move the User Profile Synchronization service to a new server
<a name="moveService"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013.

Use the following procedure to move the User Profile Synchronization service to a new server.
  
 **To move the User Profile Synchronization service to a new server by using Central Administration**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer on which you installed the User Profile synchronization service. This is required to start the User Profile Synchronization service. After the User Profile Synchronization service is started you can remove the farm account from the Administrators group.
    
2. On the server that is currently running the User Profile synchronization service, on the SharePoint Central Administration website, in the **System Settings** section, click **Manage services on Server**.
    
3. Next to the **User Profile Synchronization Service**, click **Stop** to stop the User Profile Synchronization service. 
    
4. On the new User Profile synchronization server, on the SharePoint Central Administration website, in the **System Settings** section, click **Manage services on Server**.
    
5. Next to the **User Profile Synchronization Service**, click **Start** to start the User Profile synchronization service. 
    
6. On the new User Profile synchronization server, on the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
7. On the **Service Applications** page, click the link for the name of the appropriate User Profile service application. 
    
8. On the **User Profile Service Application** page, in the **Synchronization** section, click **Start Profile Synchronization**.
    
9. On the **Start Profile Synchronization** page, select **Start Full Synchronization**, and then click **OK**.
    
## Restrict User Profile synchronization communication to a specific domain controller
<a name="restrictComm"> </a>

Use the following procedure to restrict profile synchronization communication to a specific domain controller.
  
 **To restrict User Profile synchronization communication to a specific domain controller by using Windows PowerShell**
  
1. Start the SharePoint Management Shell.
    
2. To get the User Profile service application object, type the following command:
    
  ```
  $upa=Get-SPServiceApplication <GUID>
  ```

    Where  _\<GUID\>_ is the GUID of the User Profile Synchronization Service application. 
    
3. To restrict profile synchronization communication to a specific domain controller, type the following command:
    
  ```
  Set-SPProfileServiceApplication $upa -UseOnlyPreferredDomainControllers $true
  ```

    > [!NOTE]
    > It may take five minutes for the changed property value to propagate to the SharePoint Central Administration website. Resetting IIS on the Central Administration server will force the new value to be loaded immediately. For more information about resetting IIS, see [IIS Reset Activity](https://go.microsoft.com/fwlink/p/?LinkId=179336). 
  
For more information, see Get-SPServiceApplication and Set-SPProfileServiceApplication.
  
## Adjust User Profile synchronization time-outs
<a name="timeouts"> </a>

> [!NOTE]
> This section applies to SharePoint Server 2013.

A time-out can occur on the following occasions:
  
- When trying to connect to the directory service server on the **Add/Edit a synchronization connection** page in Central Administration. 
    
- When trying to populate the list of containers on the **Add/Edit a synchronization connection** page in Central Administration. This will occur as a JavaScript time-out error in the status bar. 
    
- When clicking **OK** on the **Add/Edit a synchronization connection** page in Central Administration. This causes the following error message and occurs because of a time-out by the Forefront Identity Manager web service when creating or updating a User Profile synchronization connection: 
    
> "The request channel timed out while waiting for a reply after 00:01:29.9062626. Increase the timeout value passed to the call to Request or increase the SendTimeout value on the Binding. The time allocated to this operation may have been a part of a longer timeout." 

 **To adjust User Profile synchronization timeouts by using Windows PowerShell**
  
1. If you want to change the time-out value for connecting to the directory server, do the following:
    
1. Paste the following code into a text editor, such as Notepad:
    
  ```
  $upsAppProxy = Get-SPServiceApplicationProxy <UPSAppProxyGUID>
  $upsAppProxy.LDAPConnectionTimeout = <NewTimeout>
  $upsAppProxy.Update()
  ```

2. Replace  _\<UPSAppProxyGUID\>_ with the GUID of the User Profile service application proxy and  _\<NewTimeout\>_ with the new time-out value in seconds. The default time-out is 120 seconds. 
    
3. Save the file as an ANSI-encoded text file whose extension is .ps1.
    
2. If you want to change the time-out value for the Populate Containers control, do the following:
    
1. Paste the following code into a text editor, such as Notepad:
    
  ```
  $upsAppProxy = Get-SPServiceApplicationProxy <UPSAppProxyGUID>
  $upsAppProxy.ImportConnAsyncTimeout = <NewTimeout>
  $upsAppProxy.Update()
  ```

2. If you want to change the time-out value for calls into the Forefront Identity Manager web service, do the following:
    
    Replace  _\<UPSAppProxyGUID\>_ with the GUID of the User Profile service application proxy and  _\<NewTimeout\>_ with the new time-out value in seconds. The default time-out is 1,000 seconds (approximately 17 minutes). 
    
3. Paste the following code into a text editor, such as Notepad:
    
  ```
  $upsApp = Get-SPServiceApplication 
  <UPSAppGUID>
  $upsApp.FIMWebClientTimeOut = 
  <NewTimeout>
  $upsApp.Update()
  ```

4. Replace  _\<UPSAppGUID\>_ with the GUID of the User Profile service application and  _\<NewTimeout\>_ with the new time-out value in milliseconds. The default time-out is 300,000 milliseconds (5 minutes). 
    
5. Save the file as an ANSI-encoded text file whose extension is .ps1, such as AdjustProfileSyncTimeouts.ps1.
    
3. On the **Start** menu, click **All Programs**.
    
4. Click **Microsoft SharePoint 2013 Products**.
    
5. Click **SharePoint 2013 Management Shell**.
    
6. Change to the directory where you saved the file.
    
7. At the Microsoft PowerShell command prompt, type the following command to execute a script file:
    
  ```
  ./<file name>.ps1
  ```

    Where  _\<file name\>_ is the name of the file to execute. 
    
For more information, see Get-SPServiceApplicationProxy and Get-SPServiceApplication.
  

