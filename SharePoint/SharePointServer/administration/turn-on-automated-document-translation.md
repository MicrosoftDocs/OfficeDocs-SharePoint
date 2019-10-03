---
title: "Turn on automated document translation in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/10/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 5005124c-09d0-435c-99a4-1f2cb1fdae91

description: "Learn how to turn on the Machine Translation Service in SharePoint Server to let site owners automatically translate documents."
---

# Turn on automated document translation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
On a publishing site collection that uses variations, site owners can choose to export a file and have it translated by a person (human translation), or they can choose to have it be translated automatically (machine translation). By default, the Machine Translation Service is turned off. Turning it on is a two-step process:
  
- Step 1: Create a Machine Translation service application.
    
- Step 2: Configure the Machine Translation Service.
    
This article describes how to do both steps by using either the SharePoint Central Administration website or Microsoft PowerShell.
  
    
## Before you begin
<a name="begin"> </a>

Before you perform these procedures, review the following information about prerequisites:
  
- The App Management service application must be started in Central Administration. For more information, see [Configure an environment for apps for SharePoint Server](configure-an-environment-for-apps-for-sharepoint.md).
    
- If the Machine Translation Service is in one farm and the User Profile service is in another farm, you must configure server-to-server authentication.
    
- There must be a User Profile service application proxy in the default proxy group for the farm, and the User Profile service application must be started and configured by using Central Administration or by using PowerShell. For more information, see [Create a User Profile service applications in SharePoint Server](../install/create-a-user-profile-service-application.md).
    
- The server from which machine translations will be run must be able to connect to the Internet.
    
- If you plan to use Central Administration to create the service application, verify that you are a member of the Farm Administrators SharePoint group and the Administrators group on the computer that is running Central Administration.
    
- If you plan to use PowerShell to create the service application, you must have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance. 
    
  - **db_owner** fixed database role on all databases that are to be updated. 
    
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
## Supported file name extensions and maximum file sizes
<a name="supported"> </a>

The Machine Translation Service translates files up to a certain size, as shown in the following table.
  
**Table: Supported file types and maximum file size limits for machine translation**

|**File type**|**File extensions**|**Maximum file size**|
|:-----|:-----|:-----|
|Microsoft Word document parser  <br/> |.doc  <br/> .docm  <br/> .docx  <br/> .dot  <br/> .dotm  <br/> .dotx  <br/> .rtf  <br/> |524,288 KB  <br/> |
|HTML parser  <br/> |.aspx  <br/> .htm  <br/> .html  <br/> .xhtm  <br/> .xhtml  <br/> |15,360 KB  <br/> |
|Plain text parser  <br/> |.txt  <br/> |15,360 KB  <br/> |
|XLIFF parser  <br/> |.xlf  <br/> |15,360 KB  <br/> |
   
The maximum character count for Microsoft Word documents is 10,000,000.
  
## Step 1: Create a Machine Translation service application
<a name="step1"> </a>

The following two procedures describe how to create a Machine Translation Service application. One uses Central Administration, and the other uses PowerShell.
  
Refer to the following table in step 7 below.
  
**Table: Database section properties**

|**Item**|**Action**|
|:-----|:-----|
|**Database Server** <br/> |Type the name of the database server and SQL Server instance that you want to use in the format  _ServerName\Instance_. You can also use the default entry.  <br/> |
|**Database Name** <br/> |Type a unique name for the database.  <br/> |
|**Database Authentication** <br/> | Select the authentication that you want to use by doing one of the following:  <br/>  To use Windows authentication, leave this option selected. We recommend this option because Windows authentication automatically encrypts the password when it connects to SQL Server.  <br/>  To use SQL authentication, choose **SQL authentication**. In the **Account** box, type the name of the account that you want the service application to use to authenticate to the SQL Server database, and then type the password in the **Password** box.  <br/> **Note:** <br/>  The SQL authentication option sends a password that is not encrypted to SQL Server. We recommend that you use SQL authentication only if you force protocol encryption to SQL Server or encrypt network traffic by using IPsec.  <br/> |
   
### To create a Machine Translation service application by using Central Administration

1. On the Central Administration home page, in the **Application Management** section, choose **Manage service applications**.
    
2. On the ribbon, choose **New**, and then choose **Machine Translation Service**.
    
3. In the **Create New Machine Translation Service Application** pane, type a name for the service application. 
    
4. In the **Application Pool** section, do one of the following: 
    
  - Choose **Use existing application pool**, and then select the application pool that you want to use from the drop-down list.
    
  - Choose **Create a new application pool**, type the name of the new application pool, and then under **Select a security account for this application pool**, do one of the following:
    
  - Choose **Predefined** to use a predefined security account, and then select the security account from the drop-down list. 
    
  - Choose **Configurable** to specify a new security account to be used for an existing application pool. You can create an account by choosing the **Register new managed account** link. 
    
    > [!IMPORTANT]
    > The account that is used by the application pool must also have Full Control permissions to the User Profile service application. If you create an application pool and a new account, ensure that you add the account to the list of accounts that can use the User Profile service application, and grant Full Control permissions to the account. For more information, see [Restrict or enable access to a service application in SharePoint Server](restrict-or-enable-access-to-a-service-application.md). 
  
5. If you'll provide hosting services for other sites, and the sites that use it have site subscriptions, select **Run in partitioned mode**.
    
6. Select **Add this service application's proxy to the farm's default proxy list**. If you have multiple web applications and want them to use different sets of services, clear this check box.
    
7. In the **Database** section, specify the database server, database name, and authentication method for the new service application as described in the table before this procedure. The database is used to hold the work items for the Machine Translation Service. 
    
8. Choose **OK**.
    
9. Start the Machine Translation Service. For more information, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
### To create a Machine Translation service application by using PowerShell

Refer to the following table in step 2 below.
  
**Table: Variables used in the New-SPTranslationServiceApplication cmdlet**

|**Variable name**|**Description**|
|:-----|:-----|
| _\<ServiceApplicationName\>_ <br/> |The name of the new Machine Translation Service application.  <br/> |
| _\<DatabaseName\>_ <br/> |The name of the database that will host the Machine Translation Service logs. To create a database, provide a new unique name.  <br/> |
| _\<DatabaseServer\>_ <br/> |The name of the database server that will hold the work items for the Machine Translation Service.  <br/> |
| _\<ApplicationPoolName\>_ <br/> |The name of an existing application pool in which the new Machine Translation Service should run.  <br/> **Important:** The account that is used by the application pool must also have Full Control permissions to the User Profile service application. If you create an application pool and a new account, ensure that you add the account to the list of accounts that can use the User Profile service application, and grant it Full Control permissions. For more information, see [Restrict or enable access to a service application in SharePoint Server](restrict-or-enable-access-to-a-service-application.md).           |
   
1. Open SharePoint Management Shell.
    
2. At the PowerShell command prompt, type the following syntax:
    
  ```
  New-SPTranslationServiceApplication -Name "<ServiceApplicationName>" -DatabaseName "<DatabaseName>" -DatabaseServer "<DatabaseServer>" -ApplicationPool "<ApplicationPoolName>" -Default
  ```

    The table at the beginning of this procedure describes the variables used in the **New-SPTranslationServiceApplication** cmdlet. 
    
    **Example**
    
  ```
  New-SPTranslationServiceApplication -Name "Machine Translation Service Application" -DatabaseName "MachineTranslationDB" -DatabaseServer "ContosoDBServer" -ApplicationPool "ContosoAppPool" -Default
  ```

3. Start the Machine Translation Service. For more information, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
For more information, see [New-SPTranslationServiceApplication](/sharepoint/security-for-sharepoint-server/security-for-sharepoint-server).
  
## Step 2: Configure the Machine Translation Service
<a name="step2"> </a>

The following two procedures describe how to configure the Machine Translation Service. One uses Central Administration, and the other uses PowerShell.
  
> [!CAUTION]
> Changing the default settings for the Machine Translation Service can potentially affect server performance. For example, increasing item size limits can result in the translation job taking longer to run, and increasing the number of processes will consume more resources on the server. Carefully consider any possible server effects before you change these settings. 
  
### To configure the Machine Translation Service by using Central Administration

1. On the Central Administration home page, in the **Application Management** section, choose **Manage service applications**.
    
2. On the **Manage Service Applications** page, choose the link that corresponds to the name of the Machine Translation service application. 
    
3. On the **Machine Translation Service** page, in the **Enabled File Extensions** section, clear the check box for any file name extensions that you want to disable. By default, all file name extensions are enabled. 
    
4. In the **Item Size Limits** section, do the following: 
    
  - In the **Maximum file size for binary files in KB. Microsoft Word documents are binary files** box, type the maximum file size (100-524,288), in KB, for binary files. The default is 51,200. Files that exceed this limit won't be translated. 
    
  - In the **Maximum file size for text files in KB. Plain-text, HTML, and XLIFF documents are text files** box, type the maximum file size (100-15,360), in KB, for text files. The default is 5,120. Files that exceed this limit won't be translated. 
    
  - In the **Maximum character count for Microsoft Word documents** box, type the maximum character count (10,000-10,000,000) for Word documents. The default is 500,000. 
    
5. In the **Online Translation Connection** section, do one of the following: 
    
  - Choose **Use default internet settings**. This is the default.
    
  - Choose **Use the proxy specified**, and type a web proxy server and port number.
    
    > [!NOTE]
    > If you change this setting, you must stop and restart the Machine Translation Service after you configure it. 
  
6. In the **Translation Processes** section, type the number of translation processes (1-5). The default is 1. 
    
    > [!NOTE]
    > If you change this setting, you must stop and restart the Machine Translation Service after you configure it. 
  
7. In the **Translation Throughput** section, do the following: 
    
  - In the **Frequency with which to start translations (minutes)** box, type the frequency with which groups of translations are started, in minutes (1-59). The default is 15. 
    
  - In the **Number of translations to start (per translation process)** box, type the number of translations (1-1,000) per process. This number represents the number of translations started per process every time translations are started. The default is 200. 
    
8. In the **Maximum Translation Attempts** section, type the maximum number of times (1-10) a translation is tried before its status is set to **Failed**. The default is 2.
    
9. In the **Maximum Synchronous Translation Requests** section, type the maximum number of synchronous translation requests (0-300). The default is 10. 
    
    > [!NOTE]
    > You can also set this value to 0 so that no synchronous jobs are accepted. 
  
10. In **Translation Quota** > **Maximum number of items which can be queued in a 24-hour period**, do one of the following:
    
  - Choose **No limit**. This is the default.
    
  - Choose **Limit per 24 hours**, and then type the maximum number of items (100-1,000,000) that can be queued in a 24-hour period.
    
11. If you'll provide hosting services for other sites, and the sites that use it have site subscriptions, in **Translation Quota** > **Maximum number of items which can be queued in a 24-hour period per site subscription**, do one of the following:
    
  - Choose **No limit**. This is the default.
    
  - Choose **Limit per 24 hours**, and then type the maximum number of items (100-1,000,000) that can be queued in a 24-hour period per site subscription.
    
12. In the **Completed Job Expiration Time** section, do one of the following: 
    
  - Choose **Days**, and then type the number of days (1-1,000) completed jobs are kept in the job history log. The default is 7.
    
  - Choose **No expiration**.
    
13. In the **Recycled Threshold** section, type the number of documents (1-1,000) to be converted before the conversion process is restarted. The default is 100. 
    
    > [!NOTE]
    > If you change this setting, you must stop and restart the Machine Translation Service after you configure it. 
  
14. In the **Office 97-2003 Document Scanning** section, specify whether to disable security scanning for Office 97-2003 documents. Only enable this setting if you trust the documents that will be converted. The default is **No**.
    
15. Choose **OK**.
    
16. If you changed any settings in steps 5, 6, 11, or 13 that require you to restart the Machine Translation Service, restart the service now. For more information, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
### To configure the Machine Translation Service by using PowerShell

Refer to the following table in step 2.
  
**Table: Variables used in the Set-SPTranslationServiceApplication cmdlet**

|**Variable name**|**Description**|
|:-----|:-----|
| _\<ServiceApplicationName\>_ <br/> |The name of the Machine Translation service application.  <br/> |
| _\<TimerJobFrequency\>_ <br/> |The frequency, in minutes (1-59), with which groups of translations are started.  <br/> |
| _\<MaximumTranslationAttempts\>_ <br/> |The maximum number of times (1-10) a translation is tried before its status is set to **Failed**.  <br/> |
| _\<JobExpirationDays\>_ <br/> |The number of days (1-1,000) completed jobs are kept in the job history log.  <br/> |
| _\<MaximumSyncTranslationRequests\>_ <br/> |The maximum number of synchronous translation requests (0-300).  <br/> |
| _\<RecycleProcessThreshold\>_ <br/> |The number of documents (1-1,000) to be converted before the conversion process is restarted.  <br/> |
| _\<DisableBinaryFileScan\>_ <br/> |Either 0 (false) or 1 (true).  <br/> |
   
1. Open SharePoint Management Shell.
    
2. At the PowerShell command prompt, type the following syntax:
    
  ```
  Set-SPTranslationServiceApplication -Identity "<ServiceApplicationName>" -EnableAllFileExtensions -UseDefaultlnternetSettings -TimerJobFrequency <TimerJobFrequency> -MaximumTranslationAttempts <MaximumTranslationAttempts> -JobExpirationDays <JobExpirationDays> -MaximumSyncTranslationRequests <MaximumSyncTranslationRequests> -RecycleProcessThreshold <RecycleProcessThreshold> -DisableBinaryFileScan <DisableBinaryFileScan>
  ```

    The table at the beginning of this procedure describes the variables used in the **Set-SPTranslationServiceApplication** cmdlet. 
    
    **Example**
    
  ```
  Set-SPTranslationServiceApplication -Identity "Machine Translation Service Application" -EnableAllFileExtensions -UseDefaultlnternetSettings -TimerJobFrequency 30 -MaximumTranslationAttempts 3 -JobExpirationDays 14 -MaximumSyncTranslationRequests 20 -RecycleProcessThreshold 300 -DisableBinaryFileScan 1
  ```

3. If you changed any of the following parameters, restart the service now:  `KeepAliveTimeout`,  `MaximumTranslationTime`,  `TotalActiveProcesses`,  `RecycleProcessThreshold`,  `WebProxyAddress`,  `MachineTranslationAddress`, or  `UseDefaultInternetSettings`. For more information, see [Start or stop a service in SharePoint Server](start-or-stop-a-service.md).
    
For more information, see [Set-SPTranslationServiceApplication](/powershell/module/sharepoint-server/Set-SPTranslationServiceApplication?view=sharepoint-ps).
  
## Additional steps
<a name="more"> </a>

- If the account that is used by the application pool that was assigned to the Machine Translation service application differs from the one used by the User Profile service application, you must add it to the list of accounts that can use the User Profile service application and grant it Full Control permissions. For more information, see [Restrict or enable access to a service application in SharePoint Server](restrict-or-enable-access-to-a-service-application.md).
    
- The Microsoft Translator Hub is an extension of Microsoft Translator and lets you build automatic language translation systems that integrate with your website. After you build a custom system, the **Test System** page on the **Projects** tab in the Microsoft Translator Hub displays a category ID. You can configure the Machine Translation Service to use the custom translation system by passing the category ID in the  `MachineTranslationCategory` parameter. For more information about the Microsoft Translator Hub, see [About Microsoft Translator Hub](https://go.microsoft.com/fwlink/?LinkId=330174).
    
## See also
<a name="more"> </a>

#### Concepts

[Variations overview in SharePoint Server](variations-overview.md)
  
[Plan for variations in SharePoint Server](plan-for-variations.md)

