---
title: Turn on automated document translation in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 5005124c-09d0-435c-99a4-1f2cb1fdae91
---


# Turn on automated document translation in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to turn on the Machine Translation Service in SharePoint Server 2016 to let site owners automatically translate documents.On a publishing site collection that uses variations, site owners can choose to export a file and have it translated by a person (human translation), or they can choose to have it be translated automatically (machine translation). By default, the Machine Translation Service is turned off. Turning it on is a two-step process:
- Step 1: Create a Machine Translation service application.
    
  
- Step 2: Configure the Machine Translation Service.
    
  
This article describes how to do both steps by using either the SharePoint Central Administration website or Microsoft PowerShell.In this article:
-  [Before you begin](#begin)
    
  
-  [Supported file name extensions and maximum file sizes](#supported)
    
  
-  [Step 1: Create a Machine Translation service application](#step1)
    
  
-  [Step 2: Configure the Machine Translation Service](#step2)
    
  
-  [Additional steps](#more)
    
  

## Before you begin
<a name="begin"> </a>

Before you perform these procedures, review the following information about prerequisites:
- The App Management service application must be started in Central Administration. For more information, see  [Configure an environment for apps for SharePoint Server](html/configure-an-environment-for-apps-for-sharepoint-server.md).
    
  
- If the Machine Translation Service is in one farm and the User Profile service is in another farm, you must configure server-to-server authentication.
    
  
- There must be a User Profile service application proxy in the default proxy group for the farm, and the User Profile service application must be started and configured by using Central Administration or by using PowerShell. For more information, see  [Create a User Profile service applications in SharePoint Server](html/create-a-user-profile-service-applications-in-sharepoint-server.md).
    
  
- The server from which machine translations will be run must be able to connect to the Internet.
    
  
- If you plan to use Central Administration to create the service application, verify that you are a member of the Farm Administrators SharePoint group and the Administrators group on the computer that is running Central Administration.
    
  
- If you plan to use PowerShell to create the service application, you must have the following memberships:
    
  - **securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  

## Supported file name extensions and maximum file sizes
<a name="supported"> </a>

The Machine Translation Service translates files up to a certain size, as shown in the following table.
### Table: Supported file types and maximum file size limits for machine translation

File type File extensions Maximum file size Microsoft Word document parser  <br/>  .doc <br/>  .docm <br/>  .docx <br/>  .dot <br/>  .dotm <br/>  .dotx <br/>  .rtf <br/> 524,288 KB  <br/> HTML parser  <br/>  .aspx <br/>  .htm <br/>  .html <br/>  .xhtm <br/>  .xhtml <br/> 15,360 KB  <br/> Plain text parser  <br/>  .txt <br/> 15,360 KB  <br/> XLIFF parser  <br/>  .xlf <br/> 15,360 KB  <br/> The maximum character count for Microsoft Word documents is 10,000,000.
## Step 1: Create a Machine Translation service application
<a name="step1"> </a>

The following two procedures describe how to create a Machine Translation Service application. One uses Central Administration, and the other uses PowerShell. **To create a Machine Translation service application by using Central Administration**
1. On the Central Administration home page, in the **Application Management** section, choose **Manage service applications**.
    
  
2. On the ribbon, choose **New**, and then choose **Machine Translation Service**.
    
  
3. In the **Create New Machine Translation Service Application** pane, type a name for the service application.
    
  
4. In the **Application Pool** section, do one of the following:
    
  - Choose **Use existing application pool**, and then select the application pool that you want to use from the drop-down list.
    
  
  - Choose **Create a new application pool**, type the name of the new application pool, and then under **Select a security account for this application pool**, do one of the following:
    
  - Choose **Predefined** to use a predefined security account, and then select the security account from the drop-down list.
    
  
  - Choose **Configurable** to specify a new security account to be used for an existing application pool. You can create an account by choosing the **Register new managed account** link.
    
  

    > [!IMPORTANT:]
      
5. If you'll provide hosting services for other sites, and the sites that use it have site subscriptions, select **Run in partitioned mode**.
    
  
6. Select **Add this service application's proxy to the farm's default proxy list**. If you have multiple web applications and want them to use different sets of services, clear this check box.
    
  
7. In the **Database** section, specify the database server, database name, and authentication method for the new service application as described in the following table. The database is used to hold the work items for the Machine Translation Service.
    
### Table: Database section properties

Item Action **Database Server** <br/> Type the name of the database server and SQL Server instance that you want to use in the format  *ServerName\\Instance*  . You can also use the default entry. <br/> **Database Name** <br/> Type a unique name for the database.  <br/> **Database Authentication** <br/>  Select the authentication that you want to use by doing one of the following: <br/>  To use Windows authentication, leave this option selected. We recommend this option because Windows authentication automatically encrypts the password when it connects to SQL Server. <br/>  To use SQL authentication, choose **SQL authentication**. In the **Account** box, type the name of the account that you want the service application to use to authenticate to the SQL Server database, and then type the password in the **Password** box. <br/> 
> [!NOTE:]

  
    
    

8. Choose **OK**.
    
  
9. Start the Machine Translation Service. For more information, see  [Start or stop a service in SharePoint Server](html/start-or-stop-a-service-in-sharepoint-server.md).
    
  
 **To create a Machine Translation service application by using PowerShell**
1. Open **SharePoint 2016 Management Shell**.
    
  
2. At the PowerShell command prompt, type the following syntax:
    
  ```
  
New-SPTranslationServiceApplication -Name "<ServiceApplicationName> " -DatabaseName "<DatabaseName> " -DatabaseServer "<DatabaseServer> " -ApplicationPool "<ApplicationPoolName> " -Default
  ```


    The following table describes the variables used in the **New-SPTranslationServiceApplication** cmdlet.
    
### Table: Variables used in the New-SPTranslationServiceApplication cmdlet

Variable name Description  *<ServiceApplicationName>*  <br/> The name of the new Machine Translation Service application.  <br/>  *<DatabaseName>*  <br/> The name of the database that will host the Machine Translation Service logs. To create a database, provide a new unique name.  <br/>  *<DatabaseServer>*  <br/> The name of the database server that will hold the work items for the Machine Translation Service.  <br/>  *<ApplicationPoolName>*  <br/> The name of an existing application pool in which the new Machine Translation Service should run.  <br/> 
> [!IMPORTANT:]

  
    
    


    **Example**
    


  ```
  
New-SPTranslationServiceApplication -Name "Machine Translation Service Application" -DatabaseName "MachineTranslationDB" -DatabaseServer "ContosoDBServer" -ApplicationPool "ContosoAppPool" -Default
  ```

3. Start the Machine Translation Service. For more information, see  [Start or stop a service in SharePoint Server](html/start-or-stop-a-service-in-sharepoint-server.md).
    
  
For more information, see **New-SPTranslationServiceApplication**.
## Step 2: Configure the Machine Translation Service
<a name="step2"> </a>

The following two procedures describe how to configure the Machine Translation Service. One uses Central Administration, and the other uses PowerShell.
> [!CAUTION:]

  
    
    

 **To configure the Machine Translation Service by using Central Administration**
1. On the Central Administration home page, in the **Application Management** section, choose **Manage service applications**.
    
  
2. On the **Manage Service Applications** page, choose the link that corresponds to the name of the Machine Translation service application.
    
  
3. On the **Machine Translation Service** page, in the **Enabled File Extensions** section, clear the check box for any file name extensions that you want to disable. By default, all file name extensions are enabled.
    
  
4. In the **Item Size Limits** section, do the following:
    
  - In the **Maximum file size for binary files in KB. Microsoft Word documents are binary files** box, type the maximum file size (100–524,288), in KB, for binary files. The default is 51,200. Files that exceed this limit won't be translated.
    
  
  - In the **Maximum file size for text files in KB. Plain-text, HTML, and XLIFF documents are text files** box, type the maximum file size (100–15,360), in KB, for text files. The default is 5,120. Files that exceed this limit won't be translated.
    
  
  - In the **Maximum character count for Microsoft Word documents** box, type the maximum character count (10,000–10,000,000) for Word documents. The default is 500,000.
    
  
5. In the **Online Translation Connection** section, do one of the following:
    
  - Choose **Use default internet settings**. This is the default.
    
  
  - Choose **Use the proxy specified**, and type a web proxy server and port number.
    
  

    > [!NOTE:]
      
6. In the **Translation Processes** section, type the number of translation processes (1–5). The default is 1.
    
    > [!NOTE:]
      
7. In the **Translation Throughput** section, do the following:
    
  - In the **Frequency with which to start translations (minutes)** box, type the frequency with which groups of translations are started, in minutes (1–59). The default is 15.
    
  
  - In the **Number of translations to start (per translation process)** box, type the number of translations (1–1,000) per process. This number represents the number of translations started per process every time translations are started. The default is 200.
    
  
8. In the **Maximum Translation Attempts** section, type the maximum number of times (1–10) a translation is tried before its status is set to **Failed**. The default is 2.
    
  
9. In the **Maximum Synchronous Translation Requests** section, type the maximum number of synchronous translation requests (0–300). The default is 10.
    
    > [!NOTE:]
      
10. In **Translation Quota** > **Maximum number of items which can be queued in a 24-hour period**, do one of the following:
    
  - Choose **No limit**. This is the default.
    
  
  - Choose **Limit per 24 hours**, and then type the maximum number of items (100–1,000,000) that can be queued in a 24-hour period.
    
  
11. If you'll provide hosting services for other sites, and the sites that use it have site subscriptions, in **Translation Quota** > **Maximum number of items which can be queued in a 24-hour period per site subscription**, do one of the following:
    
  - Choose **No limit**. This is the default.
    
  
  - Choose **Limit per 24 hours**, and then type the maximum number of items (100–1,000,000) that can be queued in a 24-hour period per site subscription.
    
  
12. In the **Completed Job Expiration Time** section, do one of the following:
    
  - Choose **Days**, and then type the number of days (1–1,000) completed jobs are kept in the job history log. The default is 7.
    
  
  - Choose **No expiration**.
    
  
13. In the **Recycled Threshold** section, type the number of documents (1–1,000) to be converted before the conversion process is restarted. The default is 100.
    
    > [!NOTE:]
      
14. In the **Office 97-2003 Document Scanning** section, specify whether to disable security scanning for Office 97–2003 documents. Only enable this setting if you trust the documents that will be converted. The default is **No**.
    
  
15. Choose **OK**.
    
  
16. If you changed any settings in steps 5, 6, 11, or 13 that require you to restart the Machine Translation Service, restart the service now. For more information, see  [Start or stop a service in SharePoint Server](html/start-or-stop-a-service-in-sharepoint-server.md).
    
  
 **To configure the Machine Translation Service by using PowerShell**
1. Open **SharePoint 2016 Management Shell**.
    
  
2. At the PowerShell command prompt, type the following syntax:
    
  ```
  
Set-SPTranslationServiceApplication -Identity "<ServiceApplicationName> " -EnableAllFileExtensions -UseDefaultlnternetSettings -TimerJobFrequency <TimerJobFrequency>  -MaximumTranslationAttempts <MaximumTranslationAttempts>  -JobExpirationDays <JobExpirationDays>  -MaximumSyncTranslationRequests <MaximumSyncTranslationRequests>  -RecycleProcessThreshold <RecycleProcessThreshold>  -DisableBinaryFileScan <DisableBinaryFileScan>
  ```


    The following table describes the variables used in the **Set-SPTranslationServiceApplication** cmdlet.
    
### Table: Variables used in the Set-SPTranslationServiceApplication cmdlet

Variable name Description  *<ServiceApplicationName>*  <br/> The name of the Machine Translation service application.  <br/>  *<TimerJobFrequency>*  <br/> The frequency, in minutes (1–59), with which groups of translations are started.  <br/>  *<MaximumTranslationAttempts>*  <br/> The maximum number of times (1–10) a translation is tried before its status is set to **Failed**. <br/>  *<JobExpirationDays>*  <br/> The number of days (1–1,000) completed jobs are kept in the job history log.  <br/>  *<MaximumSyncTranslationRequests>*  <br/> The maximum number of synchronous translation requests (0–300).  <br/>  *<RecycleProcessThreshold>*  <br/> The number of documents (1–1,000) to be converted before the conversion process is restarted.  <br/>  *<DisableBinaryFileScan>*  <br/> Either 0 (false) or 1 (true).  <br/> 
    **Example**
    


  ```
  
Set-SPTranslationServiceApplication -Identity "Machine Translation Service Application" -EnableAllFileExtensions -UseDefaultlnternetSettings -TimerJobFrequency 30 -MaximumTranslationAttempts 3 -JobExpirationDays 14 -MaximumSyncTranslationRequests 20 -RecycleProcessThreshold 300 -DisableBinaryFileScan 1
  ```

3. If you changed any of the following parameters, restart the service now: KeepAliveTimeout, MaximumTranslationTime, TotalActiveProcesses, RecycleProcessThreshold, WebProxyAddress, MachineTranslationAddress, or UseDefaultInternetSettings. For more information, see  [Start or stop a service in SharePoint Server](html/start-or-stop-a-service-in-sharepoint-server.md).
    
  
For more information, see **Set-SPTranslationServiceApplication**.
## Additional steps
<a name="more"> </a>


- If the account that is used by the application pool that was assigned to the Machine Translation service application differs from the one used by the User Profile service application, you must add it to the list of accounts that can use the User Profile service application and grant it Full Control permissions. For more information, see  [Restrict or enable access to a service application in SharePoint Server](html/restrict-or-enable-access-to-a-service-application-in-sharepoint-server.md).
    
  
- The Microsoft Translator Hub is an extension of Microsoft Translator and lets you build automatic language translation systems that integrate with your website. After you build a custom system, the **Test System** page on the **Projects** tab in the Microsoft Translator Hub displays a category ID. You can configure the Machine Translation Service to use the custom translation system by passing the category ID in theMachineTranslationCategory parameter. For more information about the Microsoft Translator Hub, see [About Microsoft Translator Hub](https://go.microsoft.com/fwlink/?LinkId=330174).
    
  

# See also

#### 

 [Variations overview in SharePoint Server](html/variations-overview-in-sharepoint-server.md)
  
    
    
 [Plan for variations in SharePoint Server](html/plan-for-variations-in-sharepoint-server.md)
  
    
    

  
    
    

