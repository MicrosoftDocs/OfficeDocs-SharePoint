---
title: "Synchronize user and group profiles in SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 144e5f6e-0c9c-4f01-9b1f-26190d527e85
description: "Learn how to synchronize user and group profile information by using the SharePoint Server 2013 profile synchronization method."
---

# Synchronize user and group profiles in SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Configuring profile synchronization (or profile sync) is a process that involves many steps. This article divides the process into shorter phases, both so that you can see progress and to reduce the number of steps through which you have to backtrack if you make an error. There are four phases to configuring profile synchronization. Depending on your situation, you might not have to perform all of the phases. This article also includes Phase 0, which contains instructions for configuring the prerequisites that are required before you can configure profile synchronization.
  
User profiles and groups are used by SharePoint Server 2013 through server-to-server authentication to access and request resources from one another on behalf of users. For more information about server-to-server authentication, see [Server-to-server authentication and user profiles in SharePoint Server](../security-for-sharepoint-server/server-to-server-authentication-and-user-profiles.md).
  
> [!IMPORTANT]
> This article applies to only SharePoint Server 2013. 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
  
As you configure profile synchronization, you will need information to answer questions in the user interface. You will also need accounts that have the appropriate permissions and a SharePoint Server 2013 farm that is already partly configured. The subsections within this section explain the prerequisites that you must have before you configure profile synchronization.
  
### Gather information
<a name="info"> </a>

Before you perform the procedures in this article, you should complete the [User profile properties and profile synchronization planning worksheets for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkID=268729). You will use the information that you record in the worksheets as you perform the procedures in this article.
  
- Connection planning worksheet: Contains details about each profile synchronization connection that you will create. The article [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md) contains instructions for filling out the worksheet. 
    
- User profile properties worksheet: Identifies user profile properties and how the properties are mapped to external data sources. The article [Plan user profiles in SharePoint Server](plan-user-profiles.md) explains how to complete most of the worksheet, and the article [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md) contains instructions on how to add the property mapping information. 
    
- Profile synchronization planning worksheet: Collects the information that you must have to create the User Profile service application and its prerequisites. If your farm already contains a User Profile service application, you can omit this worksheet.
    
You will have to know the name of the synchronization server. The synchronization server is the server on which the User Profile synchronization service will run. The [Plan for the synchronization server](plan-profile-synchronization-for-sharepoint-server-2013.md#server) section of [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md) contains guidance on how to select the synchronization server. 
  
### Grant account permissions
<a name="accounts"> </a>

To configure profile synchronization you will have to know the farm account and the farm account's password, and you will need a synchronization account for each directory service that you will synchronize with. The permissions that are required for each account are described in the [Plan account permissions](plan-profile-synchronization-for-sharepoint-server-2013.md#permission) section of [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md). If an account does not have the appropriate permissions, you might not know that the permissions are wrong until you have progressed part of the way through the configuration procedure.
  
> [!NOTE]
> Incorrect permissions are the most common cause of errors in configuring profile synchronization. 
  
### Install prerequisites
<a name="farmConfig"> </a>

To set up profile synchronization you will need SharePoint Server 2013 installed in a farm configuration.
  
You must have a full installation of SQL Server, not the Express edition. Profile synchronization will not work if you have installed SharePoint Server 2013 by following the instructions in [Install SharePoint 2013 on a single server with a built-in database](../install/single-server-with-a-built-in-database.md). 
  
## Phase 0: Configure the farm
<a name="Phase0"> </a>

During this phase, you configure the infrastructure for synchronizing profiles.
  
This phase involves the following tasks:
  
1. [Create a web application to host My Sites](configure-profile-synchronization.md#WebAppProc)
    
2. [Create a managed path for My Site](configure-profile-synchronization.md#ManagedPathProc)
    
3. [Create a My Site Host site collection](configure-profile-synchronization.md#MySiteHostProc)
    
4. [Create a User Profile service application](configure-profile-synchronization.md#UPSAProc)
    
5. [Enable NetBIOS domain names for user profile synchronization by using PowerShell](configure-profile-synchronization.md#
Proc)
    
6. [Start the User Profile service](configure-profile-synchronization.md#StartUPSProc)
    
To perform the tasks in this phase, you must be a member of the Farm Administrators SharePoint group and a member of the Administrators group on the computer that is running SharePoint Server 2013.
  
### Create a web application to host My Sites
<a name="WebAppProc"> </a>

In this procedure, you create the web application in which My Sites will reside. We recommend that My Sites be in a separate web application, although the web application may be in an application pool that is shared with other collaboration sites, or it may be in a separate application pool but in a shared IIS website. For more information about SharePoint Server 2013 sites, application pools, and IIS websites, see [Architecture design for SharePoint 2013 IT pros](/sharepoint/). For more detailed instructions about how to create a web application, see [Create a web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261875(v=office.14)).
  
 **To create a web application**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. In Central Administration, in the **Application Management** section, click **Manage web applications**.
    
3. On the ribbon, click **New**.
    
4. On the **Create New Web Application** page, in the **Authentication** section, select the authentication mode that will be used for this web application. 
    
5. In the **IIS Web Site** section, you can configure the settings for your new web application by selecting one of the following two options (see the Profile Synchronization Planning worksheet): 
    
  - Click **Use an existing web site**, and then select the website on which to install your new web application.
    
  - Click **Create a new IIS web site**, and then type the name of the website in the **Name** box. 
    
    You may also provide the port number, host header, or path for the new IIS website.
    
6. In the **Security Configuration** section, select an authentication provider, whether to allow anonymous access, and whether to use Secure Sockets Layer (SSL). 
    
7. In the **Application Pool** section, do one of the following: 
    
  - If the My Site application pool (see the Profile Synchronization Planning worksheet) is an existing application pool, click **Use existing application pool**, and then select the My Site application pool from the drop-down menu.
    
  - If the My Site application pool (see the Profile Synchronization Planning worksheet) is a new application pool, click **Create a new application pool**, type the name of the My Site application pool, and either select the account that the application pool will run under (see the Profile Synchronization Planning worksheet) or create a new managed account for the application pool to run under.
    
8. In the **Database Name and Authentication** section, select the database server, database name, and authentication method for your new web application. 
    
9. If you use database mirroring, in the **Failover Server** section, in the **Failover Database Server** box, type the name of a specific failover database server that you want to associate with a content database. 
    
10. In the **Service Application Connections** section, select the service application connections that will be available to the web application. 
    
11. In the **Customer Experience Improvement Program** section, click **Yes** or **No**.
    
12. Click **OK** to create the new web application. 
    
13. When the **Application Created** page appears, click **OK**.
    
Enter the name of the web application in the **My Site web application** row of the Profile Synchronization Planning worksheet. You will need this information later. 
  
### Create a managed path for My Site
<a name="ManagedPathProc"> </a>

If you want the My Site host and users' My Sites to be at a URL that does not already have a managed path, use the procedure in [Define managed paths in SharePoint Server](define-managed-paths.md) to create the My Site managed path in the My Site web application that you previously created. In most cases, the existing managed paths will be sufficient. 
  
### Create a My Site Host site collection
<a name="MySiteHostProc"> </a>

In this procedure, you create the site collection that will host users' My Sites. For more detailed instructions about how to create a site collection, see [Create a site collection in SharePoint Server](../sites/create-a-site-collection.md).
  
 **To create a My Site Host site collection**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. On Central Administration, in the **Application Management** section, click **Create site collections**. 
    
3. On the **Create Site Collection** page, in the **Web Application** section, select the My Site web application (see the Profile Synchronization Planning worksheet). 
    
4. In the **Title and Description** section, type the title and description for the site collection. 
    
5. In the **Web Site Address** section, select the path of the URL for the My Site host. In most cases, you can use the root directory (/). 
    
6. In the **Template Selection** section, click the **Enterprise** tab, and then select **My Site Host**.
    
7. In the **Primary Site Collection Administrator** section, type the user name (in the form  _\<DOMAIN\>_\ _\<user name\>_) for the user who will be the site collection administrator.
    
8. In the **Secondary Site Collection Administrator** section, type the user name for the secondary administrator of the site collection. 
    
9. If you are using quotas to manage storage for site collections, in the **Quota Template** section, click a template in the **Select a quota template** list. 
    
10. Click **OK**.
    
The **Top-Level Site Successfully Created** page will appear when the My Site Host site collection is created. Enter this URL in the **My Site Host site collection URL** row of the Profile Synchronization Planning worksheet. Although you can click the link to browse to the root of the site collection, doing this results in an error because the user profile cannot be loaded. This behavior is to be expected; user profiles are not imported at this point. 
  
### Create a User Profile service application
<a name="UPSAProc"> </a>

In this procedure, you create the User Profile service application through which you will manage profile synchronization.
  
For more detailed instructions about how to create a User Profile service application, see [Create a User Profile service application](../install/create-a-user-profile-service-application.md#createapp).
  
 **To create a User Profile Service application**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. On the **Manage Service Application** page, on the ribbon, click **New**, and then click **User Profile Service Application**.
    
4. In the **Name** section, type the User Profile service application name (see the Profile Synchronization Planning worksheet). 
    
5. In the **Application Pool** section, select the application pool that the User Profile service application will run in (if it exists), or create a new application pool. (See the Profile Synchronization Planning worksheet.) 
    
6. Accept the default settings for the profile database, the synchronization database, and the social tagging database (unless you want different names), and specify failover servers if you are using them.
    
7. In the **Profile Synchronization Instance** section, select the synchronization server (see the Profile Synchronization Planning worksheet). 
    
8. In the **My Site Host URL** section, enter the My Site Host site collection URL that you created in the previous step (see the Profile Synchronization Planning worksheet). 
    
9. In the **My Site Managed Path** section, enter the part of the path which, when appended to the My Site host URL, will give the path of users' My Sites (see the Profile Synchronization Planning worksheet). For example, if the My Site host URL is http://server:12345/ and you want each user's My Site to be at http://server:12345/personal/<user name>, enter /personal for the My Site managed path. The managed path that you enter is created automatically. There does not already have to be a managed path with the name that you provide. 
    
10. In the **Site Naming Format** section, select a naming scheme. 
    
11. In the **Default Proxy Group** section, select whether you want the proxy of this User Profile Service to be a part of the default proxy group on this farm. 
    
12. Click **Create**.
    
13. When the **Create New User Profile Service Application** page displays the message **Profile Service Application successfully created**, click **OK**.
    
To verify that the User Profile service application was created, refresh the **Manage Service Applications** page. You should see two entries whose value in the **Name** column is the name that you provided for the User Profile service application that you previously created. The first entry is the service application itself. The second entry is a connection (that is, a "proxy") to the service application. 
  
### Enable NetBIOS domain names for user profile synchronization by using PowerShell
<a name="NetBIOSProc"> </a>

If the NetBIOS name of any domain with which you are synchronizing differs from its fully-qualified domain name, you must enable NetBIOS domain names on the User Profile service application. If all NetBIOS names are the same as the domain names, you may skip this procedure.
  
 **To enable NetBIOS domain names for user profile synchronization by using PowerShell**
  
1. Verify that you have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running PowerShell cmdlets.
    
  - You must read [about_Execution_Policies](https://go.microsoft.com/fwlink/p/?LinkId=193050).
    
    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server 2013 cmdlets. 
    
    > [!NOTE]
    > If you do not have permissions, contact your Setup administrator or SQL Server administrator to request permissions. For additional information about PowerShell permissions, see Permissions and [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps). 
  
2. Paste the following code into a text editor, such as Notepad:
    
3. 
  ```
  $ServiceApps = Get-SPServiceApplication
  $UserProfileServiceApp = ""
  foreach ($sa in $ServiceApps)
    {if ($sa.DisplayName -eq "<UPSAName>") 
      {$UserProfileServiceApp = $sa}
    }
  $UserProfileServiceApp.NetBIOSDomainNamesEnabled = 1
  $UserProfileServiceApp.Update()
  ```

4. Replace  _\<UPSAName\>_ with the name of the User Profile service application. 
    
5. Save the file and add the .ps1 extension, such as EnableNetBIOS.ps1.
    
    > [!NOTE]
    > You can use a different file name, but you must save the file as an ANSI-encoded text file whose extension is .ps1. 
  
6. Start the SharePoint 2013 Management Shell.
    
7. Change to the directory where you saved the file.
    
8. At the PowerShell command prompt, type the following command:
    
  ```
  & .\EnableNetBIOS.ps1
  ```

> [!NOTE]
> We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions. 
  
### Start the User Profile service
<a name="StartUPSProc"> </a>

In this procedure, you start the User Profile service.
  
 **To start the User Profile service**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. On Central Administration, in the **System Settings** section, click **Manage services on server**.
    
3. On the **Services on Server** page, in the **Server** box, select the synchronization server (see the Profile Synchronization Planning worksheet). 
    
4. Find the row whose **Service** column value is **User Profile Service**. If the value in the **Status** column is **Stopped**, click **Start** in the **Action** column. 
    
## Phase 1: Start the User Profile synchronization service
<a name="Phase1"> </a>

During this phase, you start the User Profile synchronization service.
  
This phase involves the following tasks:
  
1. [Start the User Profile synchronization service](configure-profile-synchronization.md#StartUPSSProc)
    
2. [Remove unnecessary permissions](configure-profile-synchronization.md#RemovePermsProc)
    
3. [Reset IIS](configure-profile-synchronization.md#ResetIISProc)
    
To perform the tasks in this phase, you must be a member of the Farm Administrators SharePoint group and a member of the Administrators group on the computer that is running SharePoint Server 2013.
  
### Start the User Profile synchronization service
<a name="StartUPSSProc"> </a>

In this procedure, you start the User Profile synchronization service. The User Profile synchronization service interacts with Microsoft Forefront Identity Manager (FIM) to synchronize information with external systems.
  
 **To start the User Profile synchronization service**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. On Central Administration, in the **System Settings** section, click **Manage services on server**.
    
3. On the **Services on Server** page, in the **Server** box, select the synchronization server. 
    
4. Find the row whose **Service** column value is **User Profile Synchronization Service**. If the value in the **Status** column is **Stopped**, click **Start** in the **Action** column. 
    
5. On the **User Profile Synchronization Service** page, in the **Select the User Profile Application** section, select the User Profile service application. 
    
6. In the **Service Account Name and Password** section, the farm account is already selected. Enter the password for the farm account in the **Password** box, and enter it again in the **Confirm Password** box. 
    
7. Click **OK**.
    
The **Services on Server** page shows that the User Profile synchronization service has a status of **Starting**. When you start the User Profile synchronization service, SharePoint Server 2013 provisions FIM to participate in synchronization. This may take 10 minutes. To determine whether the User Profile synchronization service has started, refresh the **Services on Server** page. 
  
If the User Profile synchronization service does not start, confirm that the farm account has the necessary permissions on the synchronization server. For more information about which permissions are required, see the [Plan account permissions](plan-profile-synchronization-for-sharepoint-server-2013.md#permission) section of the article "Plan for profile synchronization." 
  
### Remove unnecessary permissions
<a name="RemovePermsProc"> </a>

After you start the User Profile synchronization service, for day to day operations, the farm account is not required to be a member of the Administrators group on the computer that is running the synchronization service. To improve the security of your SharePoint Server 2013 installation, remove the farm account from the Administrators group on the computer that is running the synchronization service. However, when you perform a backup of the User Profile application, the synchronization service provisions the User Profile application again. During the course of provisioning the User Profile application, the farm account must stop and start the synchronization service. To do this, the farm account must be a member of the Administrators group on the computer that is running the synchronization service. So, before you perform a backup, add the farm account to the Administrators group on the computer that is running the synchronization service. After the backup has finished running, you can remove the farm account from the Administrators group.
  
 **To grant the farm account the Remote Enable permission to Microsoft FIM 2010**
  
1. On the server that is running the synchronization service, click **Start**.
    
2. Click **Run**, type wmimgmt.msc, and then click OK. 
    
3. Right click **WMI Control**, and then click **Properties**.
    
4. In the **WMI Control Properties** dialog box, click the **Security** tab. 
    
5. Expand the **Root** list, and then select the Microsoft FIM 2010 namespace **MicrosoftIdentityIntegrationServer**.
    
6. Click the **Security** button. 
    
7. Add the farm account to the list of groups and users, and then in the **Permissions for Authenticated Users** box, select **Allow** for the **Remote Enable** permission. 
    
8.  Click **OK** to dismiss the **Security for ROOT\MicrosoftIdentityIntegrationServer** dialog box, and then click **OK** to dismiss the **WMI Control Properties** dialog box. 
    
### Reset IIS
<a name="ResetIISProc"> </a>

If the SharePoint Central Administration website and the User Profile synchronization service are running on the same server, you must reset IIS after the User Profile synchronization service starts. If they are running on different servers, you may skip this procedure.
  
 **To reset IIS**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. Start a Command Prompt with elevated privileges.
    
3. In the **User Account Control** dialog box, click **Yes**.
    
4. In the **Administrator: Command Prompt** window, type iisreset and then press ENTER. 
    
5. When the message **Internet services successfully restarted** is displayed, close the **Administrator: Command Prompt** window. 
    
> [!NOTE]
> After you reset IIS, pages of Central Administration will take several seconds to load. 
  
## Phase 2: Configure connections and import data from directory services
<a name="Phase2"> </a>

To import profiles, you must have at least one synchronization connection to a directory service. During this phase, you create a synchronization connection to each directory service that you want to import profiles from. You can synchronize after you create each connection, or you can synchronize one time, after you have created all of the connections. Synchronizing after each connection will take longer, but doing this makes it easier to troubleshoot any problems that you might encounter.
  
You must be a farm administrator or an administrator of the User Profile service application to perform these procedures. If you are not a farm administrator, start each procedure by using the **Manage Profile Service** page. 
  
This phase involves the following tasks:
  
1. [Create a synchronization connection to a directory service](configure-profile-synchronization.md#ConfigSyncProc)
    
2. [Define exclusion filters for a synchronization connection](configure-profile-synchronization.md#FiltersProc)
    
3. [Map user profile properties](configure-profile-synchronization.md#MapUserProc)
    
4. [Start profile synchronization](configure-profile-synchronization.md#StartSyncProc)
    
### Create a synchronization connection to a directory service
<a name="ConfigSyncProc"> </a>

In this procedure, you create a connection to a directory service. The connection identifies the items to synchronize and contains the credentials that are used to interact with the directory service. The information that you enter comes from the Connection Planning worksheet.
  
 **To create a Profile synchronization connection to a directory service**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or an administrator of the User Profile service application.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. If the user account that is performing this procedure is a farm administrator, complete these steps. Otherwise, if the user account is not a farm administrator go to the next step:
    
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, select the User Profile service application. 
    
3. On Central Administration, on the **Manage Profile Service** page, in the **Synchronization** section, click **Configure Synchronization Connections**.
    
4. On the **Synchronizations Connections** page, click **Create New Connection**.
    
5. On the **Add new synchronization connection** page, type the synchronization connection name in the **Connection Name** box. 
    
6. From the **Type** list, select the type of directory service to which you want to connect. 
    
7. Fill in the **Connection Settings** section according to the directory service to which you are creating a connection. 
    
    For Active Directory Domain Services (AD DS), follow these steps:
    
1. In the **Forest name** box, type the name of the forest. 
    
2. Do one of the following: 
    
  - If there is only one domain controller in the forest, click **Auto discover domain controller**.
    
  - If there are multiple domain controllers in the forest, click **Specify a domain controller** and type the domain controller name in the **Domain controller name** box. 
    
3. In the **Authentication Provider Type** box, select the type of authentication provider. 
    
4. If you select **Forms Authentication** or **Trusted Claims Provider Authentication**, select an authentication provider from the **Authentication Provider Instance** box. 
    
    The **Authentication Provider Instance** box lists only the authentication providers that are currently used by a web application. 
    
    > [!TIP]
    > You may have to select **Trusted Claims Provider Authentication** and then select **Forms authentication** in the **Authentication Provider Type** box before the list of authentication providers is displayed. 
  
5. In the **Account name** box, type the synchronization account. 
    
6. In the **Password** box, type the password for the synchronization account. 
    
7. In the **Confirm Password** box, type the password for the synchronization account again. 
    
8. In the **Port** box, enter the connection port. 
    
9. If a Secure Sockets Layer (SSL) connection is required to connect to the directory service, select **Use SSL-secured connection**.
    
    > [!IMPORTANT]
    > If you use an SSL connection, you must export the certificate of the domain controller from the Active Directory server and import the certificate into the synchronization server. 
  
    For Novell eDirectory, Sun Java System Directory Server, or IBM Tivoli Directory Server (ITDS), follow these steps:
    
1. In the **Directory Service Server Name** box, type the name of the directory service server. 
    
2. In the **Authentication Provider Type** box, select the type of authentication provider. 
    
3. In the **Authentication Provider Instance** box, select the authentication provider. 
    
    The **Authentication Provider Instance** box lists only the authentication providers that are currently used by a web application. 
    
    > [!TIP]
    > You may have to select **Trusted Claims Provider Authentication** and then select **Forms authentication** in the **Authentication Provider Type** box before the list of authentication providers is displayed. 
  
4. In the **Account name** box, type the synchronization account in LDAP format, for example, uid=username,ou=ouname,dc=yourcompany,dc=Com. 
    
5. In the **Password** box, type the password for the synchronization account. 
    
6. In the **Confirm Password** box, type the password for the synchronization account again. 
    
7. In the **Port** box, enter the connection port. 
    
8. Verify that the **Use SSL-secured connection** check box is not selected. SSL connections are not supported for these directory services. 
    
9. In the **Username attribute** box, type the name of the attribute in the directory service that serves as the unique identifier of each profile. 
    
8. In the **Containers** section, click **Populate Containers**, and then select the containers from the directory service that you want to synchronize.
    
9. Click **OK**.
    
### Define exclusion filters for a synchronization connection
<a name="FiltersProc"> </a>

In this procedure, you define filters for the connection to indicate which user profiles and which groups to exclude from synchronization. The information that you enter comes from the Connection Planning worksheet.
  
 **To define connection filters**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or an administrator of the User Profile service application.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. If the user account that is performing this procedure is a farm administrator, complete these steps. Otherwise, if the user account is not a farm administrator go to the next step: 
    
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, select the User Profile service application. 
    
3. On Central Administration, on the **Manage Profile Service** page, in the **Synchronization** section, click **Configure Synchronization Connections**.
    
4. On the **Synchronization Connections** page, right-click the connection for which you want to configure User Profile synchronization connection filters, and then click **Edit Connection Filters**.
    
5. On the **Edit connection filters** page, in the **Exclusion Filters for Users** section, select the operator to use to join the clauses of the filter. 
    
  - To specify that all of the clauses of the filter must be true, select **All apply (AND)**.
    
  - To specify that at least one of the clauses of the filter must be true, select **Any apply (OR)**.
    
6. In the **Attributes** list, select the directory service attribute to compare. 
    
7. In the **Operator** list, select the comparison operator to use. 
    
    > [!NOTE]
    > The operators that are available depend on the data type of the attribute that you selected. For a list of which operators are available for each data type, see [Connection filter data types and operators in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/hh227258(v=office.14)). 
  
8. In the **Filter** box, type the value to which you want to compare the attribute. 
    
9. Click **Add**.
    
    The clause that you added is displayed in the **Exclusion Filter for Users** area. 
    
10. To add clauses to the filter, repeat steps 5 through 9.
    
11. To filter which groups are synchronized, repeat steps 5 through 9, using the **Exclusion Filters for Groups** section of the page. 
    
12. When you have finished adding connection filters, click **OK**.
    
### Map user profile properties
<a name="MapUserProc"> </a>

In this procedure, you determine how the properties of SharePoint Server 2013 user profiles map to the user information that is retrieved from the directory service. You should have identified how you will map user profile properties on the **User profile properties** data sheet in the User Profile Properties worksheet. 
  
You will come back to this procedure in later phases to map user profile properties to information that is retrieved from business systems and to map how user profile properties in SharePoint Server 2013 can be used to write information back to the directory service. If you have not yet reached these phases, ignore the parts of the procedure that deal with business systems and exporting data.
  
 **To map user profile properties**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or an administrator of the User Profile service application.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. If the user account that is performing this procedure is a farm administrator, complete these steps. Otherwise, if the user account is not a farm administrator go to the next step: 
    
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, select the User Profile service application. 
    
3. On Central Administration, on the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.
    
4. On the **Manage User Properties** page, right-click the SharePoint Server 2013 property that you want to map to a directory service property, and then click **Edit**.
    
5. To remove an existing mapping, in the **Property Mapping for Synchronization** section, select the mapping that you want to remove, and then click **Remove**.
    
6. To add a new mapping, do the following: 
    
1. In the **Add New Mapping** section, in the **Source Data Connection** list, select the data connection that represents the external system to which you want to map the SharePoint Server 2013 property. 
    
2. In the **Attribute** list, select the name of the attribute in the external system to which you want to map the property. 
    
    > [!TIP]
    > You can only map a user profile property to an attribute of an external system if the data types are compatible. If an attribute that you want to map to a user profile is not listed when you try to create a new mapping, it might be due to a data type mismatch between the user profile property and the attribute. For more information about which data types are compatible, see [User profile property data types in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/hh227257(v=office.14)). 
  
3. In the **Direction** list, select the mapping direction. 
    
    A direction of **Import** means that the value of the attribute in the external system will be imported into SharePoint Server 2013 and used to set the value of the SharePoint Server 2013 property. A direction of **Export** means that the value of the property in SharePoint Server 2013 will be exported to the external system and used to set the value of the attribute in the external system. 
    
    > [!NOTE]
    > You cannot edit a mapping. To change the direction of a mapping, you must first remove the mapping with the old direction, and then create a mapping in the new direction and add the mapping. 
  
4. Click **Add**.
    
7. Click **OK**.
    
8. Repeat steps 4 through 7 to map additional properties.
    
### Start profile synchronization
<a name="StartSyncProc"> </a>

Use this procedure to synchronize profile information between SharePoint Server 2013 and external systems such as directory services or business systems.
  
 **To start profile synchronization**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or an administrator of the User Profile service application.
    
  - The user account that performs this procedure is a member of the Administrators group on the computer that is running SharePoint Server 2013.
    
2. If you have already imported users or created My Sites, and you have enabled NetBIOS domain names, you must disable the My Site cleanup timer job before you start profile synchronization. 

> [!NOTE] 
> For information about this timer job, please see the [Default timer jobs in SharePoint Server 2013](https://docs.microsoft.com/sharepoint/technical-reference/default-timer-jobs-in-sharepoint-2013). For information about the PowerShell cmdlets that you use to enable and disable this timer job, see [SharePoint Server cmdlet reference](https://docs.microsoft.com/powershell/module/sharepoint-server).
    
3. If the user account that is performing this procedure is a farm administrator, complete these steps. Otherwise, if the user account is not a farm administrator go to the next step: 
    
4. On Central Administration, in the **Application Management** section, click **Manage service applications**.

5.  On the **Manage Service Applications** page, select the User Profile service application. 

6.  On Central Administration, on the **Manage Profile Service** page, in the **Synchronization** section, click **Start Profile Synchronization**.
    
7.  On the **Start Profile Synchronization** page, select **Start Full Synchronization** if this is the first time that you are synchronizing or if you have added or changed any synchronization connections or property mappings since the last time that you synchronized. Select **Start Incremental Synchronization** to synchronize only information that has changed since the last time that you synchronized. 
    
8. Click **OK**.
    
    The **Manage Profile Service** page is displayed. 
    
9. If you intend to enable the My Site cleanup timer job, complete these additional steps before you enable the job:
    
10. Run profile synchronization again as described in this section.
    
11. After the second profile synchronization has finished running, on Central Administration, in the **Application Management** section, click **Manage service applications**.
    
12. Click the User Profile Service Application name, and then click **Manage User Profiles**.
    
13. On the **Manage Profile Service** page, in the **People** section, click **Manage User Profiles**.
    
14. Next to **View**, select **Profiles Missing from Import**.
    
15. In the **Find Profiles** box, type the domain for the profiles, and then click **Find**.
    
16. For each profile that is returned, check the originating directory service, such as Active Directory, for the status of that profile. If the status of any of the returned profiles in the directory is not disabled or is not deleted, do not enable the My Site cleanup timer job. Contact Microsoft support for more assistance. Otherwise, enable the My Site cleanup timer job. For information about the PowerShell cmdlets that you use to enable and disable this timer job, see the [SharePoint Server cmdlet reference](/powershell/module/sharepoint-server/?view=sharepoint-ps).
    
A full synchronization can take a long time. If you refresh the **Manage Profile Service** page, the right side of the page displays the progress of the synchronization job. Be aware that profile synchronization consists of several stages, and the profiles will not be imported immediately. The **Manage Profile Service** page is not refreshed automatically as synchronization progresses. 
  
## Phase 3: Configure connections and import data from business systems
<a name="Phase3"> </a>

You can import data from a business system, such as a personnel system or a financial system, and use that data to add properties to existing user profiles. You should already have created an external content type that brings the information from the external system into SharePoint Server 2013. For more information about how to create an external content type to synchronize with a business system, see [Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md). 
  
This phase is optional.
  
You must be a farm administrator, or an administrator of both the User Profile service application and the Business Data Connectivity service application, to perform these procedures. If you are not a farm administrator, start each procedure at the **Manage Profile Service** page. 
  
This phase involves the following tasks:
  
1. [Give the User Profile service application permission to use the external content type](configure-profile-synchronization.md#ECTPermProc)
    
2. [Configure a Business Data Connectivity synchronization connection](configure-profile-synchronization.md#BDCConnProc)
    
3. [Add or edit user profile properties](configure-profile-synchronization.md#addBDCmaps)
    
4. [Import data](configure-profile-synchronization.md#importBDCProc)
    
### Give the User Profile service application permission to use the external content type
<a name="ECTPermProc"> </a>

Use this procedure to give the farm account permission to execute operations on the external content type. For more information about how to set permissions on an external content type, see [Set permissions on an external content type](/previous-versions/office/sharepoint-server-2010/ee524076(v=office.14)#setpermissions).
  
> [!NOTE]
> Business Connectivity Services uses the permissions on the external content type and the permissions on the business system to determine authorization rules. You must make sure that the farm account also has permission to access the business system. For more information about authentication and permissions, see [Overview of Business Connectivity Services security tasks in SharePoint Server](security-tasks-overview.md). 
  
 **To give the User Profile service application permission to use the external content type**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or an administrator of the Business Data Connectivity service application.
    
  - The user account that performs this procedure has Set Permissions permission on the external content type with which you are synchronizing.
    
2. If the user account that is performing this procedure is a farm administrator, complete this step. Otherwise, if the user account is not a farm administrator go to the next step:
    
  - On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
3. On Central Administration, on the **Manage Service Applications** page, select the Business Data Connectivity service application. 
    
4. Select the check box of the external content type that represents the information with which you want to synchronize.
    
5. In the **Permissions** group, click **Set Object Permissions**.
    
6. In the box, type the farm account, and then click **Add**.
    
7. In the **Permissions for \<account\>** box, select **Execute**.
    
    > [!NOTE]
    > If the farm account is the only account that is listed in the **Permissions for \<account\>** box, you must also give the farm account Set Permissions to the external content type. At least one user, group, or claim in the external content type's access control list must have the Set Permissions permission. 
  
8. Click **OK**.
    
9. Verify that the **Propagate permissions to all methods of this external content type. Doing so will overwrite existing permissions.** check box is selected. 
    
10. Repeat these steps to set permissions on additional external content types.
    
### Configure a Business Data Connectivity synchronization connection
<a name="BDCConnProc"> </a>

In this procedure, you create a connection for each external content type. The connection specifies how the business system data relates to the profile properties. The information that you enter comes from the Connection Planning worksheet.
  
 **To create a User Profile synchronization connection**
  
1. Verify that the user account that is performing this procedure has the following credentials:
    
  - The user account that performs this procedure is a farm administrator or administrator of both the User Profile service application and the Business Data Connectivity service application.
    
2. If the user account that is performing this procedure is a farm administrator, complete these steps. Otherwise, if the user account is not a farm administrator go to the next step:
    
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, select the User Profile service application. 
    
3. On Central Administration, on the **Manage Profile Service** page, in the **Synchronization** section, click **Configure Synchronization Connections**.
    
4. On the **Synchronizations Connections** page, click **Create New Connection**.
    
5. On the **Add new synchronization connection** page, type a name for the synchronization connection in the **Connection Name** box. 
    
6. From the **Type** list, select **Business Data Connectivity**.
    
7. In the **Business Data Connectivity Entity** box, type the name of the external content type. 
    
    > [!TIP]
    > If you do not know the name of the external content type, click the **Select External Content Type** button to see all external content types. Select the external content type from the list, and then click **OK**. 
  
8. If each user profile maps to only one external content type instance, do the following:
    
1. Click **Connect User Profile Store to Business Data Connectivity Entity as a 1:1 mapping**.
    
2. In the **Return items identified by this profile property** list, select the user profile property that is used to match user profiles to external content type instances. The user profile property and the external content type identifier define the 1:1 relationship between the user profiles and the external content type, and are used to make sure that that the imported properties are applied to the correct user profile. 
    
    > [!TIP]
    > The **Return items identified by this profile property** list returns all user profile properties that have a similar data type to the external content type identifier. 
  
9. If a user profile can map to multiple external content type instances, do the following:
    
1. Click **Connect User Profile Store to Business Data Connectivity Entity as a 1:many mapping**.
    
2. In the **Filter items by** list, select the filter that is used to find the set of external content type instances that apply to a user profile. 
    
    > [!NOTE]
    > The **Filter items by** list displays all filters that are defined in the external content type. 
  
3. In the **Use this profile property as the filter value** list, select the user profile property that is used to match user profiles to external content type instances. 
    
10. Click **OK**.
    
11. Repeat steps 4 through 10 to add more connections.
    
### Add or edit user profile properties
<a name="addBDCmaps"> </a>

Before you can import the business system data, you must specify how the business system data maps to the user profile properties. The **User profile properties** data sheet in the User profile properties worksheet lists the business system properties that you want to import and how those properties map to the profile properties in the SharePoint Server 2013 profile store. 
  
Follow the procedure in the [Map user profile properties](configure-profile-synchronization.md#MapUserProc) section to map additional user profile properties. If the data maps to an existing user profile property, edit the property and add a new mapping. If the data does not map to an existing user profile property, add a new custom property and then map the property. 
  
### Import data
<a name="importBDCProc"> </a>

To import data from the business system, you must perform a full synchronization. Follow the procedure in the [Start profile synchronization](configure-profile-synchronization.md#StartSyncProc) section to start a full synchronization. 
  
## Phase 4: Configure connections and export data to directory services
<a name="Phase4"> </a>

In previous phases, you configured the profile synchronization connections that that you must have. To write profile information back to a directory service, you map the profile properties to attributes in the directory service by using a mapping direction of **Export**. The next time that profile synchronization runs, properties will be imported and exported according to the mappings that you configured.
  
> [!NOTE]
> Although you can import profile data from business systems by using the Business Connectivity Service, you cannot export profile data to business systems. 
  
This phase is optional.
  
You must be a farm administrator or an administrator of the User Profile service application to perform these procedures. If you are not a farm administrator, start each procedure by using the **Manage Profile Service** page. 
  
Do not create a new synchronization connection to export properties. To export properties to a directory service, use the same synchronization connection that you created to import properties from the directory service. You cannot use a synchronization connection only to export properties.
  
Follow the procedure to [Map user profile properties](configure-profile-synchronization.md#MapUserProc) again, this time selecting **Export** for the mapping direction. The properties that you map will be exported from SharePoint Server 2013 to the directory service whose connection you select. 
  
Follow the procedure to [Start profile synchronization](configure-profile-synchronization.md#StartSyncProc) again, this time selecting to do an incremental synchronization. The values of any SharePoint Server 2013 profile properties that were mapped to be exported to directory service attributes will be updated. 
  
> [!NOTE]
> For certain directory services, additional permissions may be required to write data back to the directory service. Review the information in the [Plan account permissions](plan-profile-synchronization-for-sharepoint-server-2013.md#permission) section of the "Plan for profile synchronization" article, and make sure that that the synchronization account has the necessary permissions. 
  
## Acknowledgements
<a name="Phase4"> </a>

The SharePoint Server 2013 Content Publishing team thanks Spencer Harbar, Enterprise Architect, for contributing to this article. His blog can be found at [http://www.harbar.net](https://go.microsoft.com/fwlink/p/?LinkId=202870).
  
## See also
<a name="Phase4"> </a>

#### Concepts

[Manage user profile synchronization in SharePoint Server](manage-profile-synchronization.md)
  
[Schedule profile synchronization in SharePoint Server](schedule-profile-synchronization.md)
  
[Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md)

