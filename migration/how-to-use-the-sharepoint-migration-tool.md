---
title: "How to use SharePoint Migration tool - SharePoint"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: The SharePoint Migration Tool copies your files from SharePoint on-premises document libraries or regular file shares to your SharePoint tenant.
---

# Using the SharePoint Migration Tool

The SharePoint Migration Tool (SPMT) is a tool that migrates your files from SharePoint on-premises document libraries or regular file shares and easily copies them to your SharePoint tenant. It is available to all Microsoft 365 users.
  

## Current and pre-release versions

Download and install SPMT using one of the links listed below.  


||**Public preview**|**First release**|**Rolling out**|**Full General Availability**|
|:-----|:-----|:-----|:-----|:-----|
|Last released build|[3.4.118.0](https://spmtreleasescus.blob.core.windows.net/betainstall/default.htm)  |[3.2.118.0](https://aka.ms/spmt-ga-page)|[3.2.118.0](https://aka.ms/spmt-ga-page) |[3.2.118.0](https://aka.ms/spmt-ga-page)|


  
## Before you begin

Review the system requirements, settings, and permissions behavior before beginning your migration.

- [SPMT Prerequisites](spmt-prerequisites.md)</br>
- [SPMT Settings](spmt-settings.md)</br>
- [Understanding permissions when using the SharePoint Migration Tool](understanding-permissions-when-migrating.md)</br>

 > [!IMPORTANT]
 > - The required permission at tenant level for the performer user is "SharePoint Admin".
 > - The required permission at site collection level for the performer user is "Admin".
 
#### Allow or prevent Custom Script (NoScript)</br>
In Microsoft 365, tenants you can control whether users can run custom script on personal sites and self-service created sites. 

During migration, some web parts require this setting set to **allow**.  Otherwise, the web part will not be migrated.

At least 24 hours before you start migration, do the following:

1.   From the SharePoint Admin Center, select **Settings**.
2.   Scroll down to **Custom Script**.
3.   Select both of the following:</br>
**Allow users to run custom script on personal sites**</br>
**Allow users to run customer script on self-service created sites**

Leave these settings in place for the duration of your migration.

 > [!NOTE]
 > Changes to this setting might take up to 24 hours to take effect.

For more info, see, [Allow or prevent custom script](https://docs.microsoft.com/sharepoint/allow-or-prevent-custom-script)</br>

#### Note about logging in
When you first launch the SharePoint Migration Tool (SPMT), you are prompted for your Microsoft 365 username and password. The credentials you provide will be to the migration *destination*.

### Authentication supported
SPMT supports the following authentication methods:

- NTLM
- Kerberos
- Forms
- ADFS
- Multi-factor authentication
- SAML-based claims
- Client certificate authentication

> [!IMPORTANT]
> If the on-premises server is configured to support multiple authentication providers, including Windows authentication, then Windows authentication **will not be supported**. If this describes your environment, use other authentication methods instead of Windows authentication. 

### Where is your data currently located?

Before you start using the SharePoint Migration Tool (SPMT), note where your data is located, and where you want those files located after migration. You will be prompted for the current location of your data files and the location of the SharePoint site collection where you want them copied. SPMT lets you select from two sources from which to migrate your data: from an on-premises SharePoint Server 2010 or 2013 site, or from a local file share or network path.
  
- **SharePoint on-premises:** If you select the SharePoint on-premises option, you are prompted to enter the name of the SharePoint Server site where your files are located and prompted for your credentials for that site. You will indicate what document library you wish to migrate. 
    
    > [!NOTE]
    > SPMT supports SharePoint Server 2010* and 2013.
  
- **File share:** If you select the file share option, you are prompted to enter the location of the file share, the URL of the SharePoint site, and the document library where they will be copied. The files are not deleted from the source.
    
## Using the SharePoint Migration tool

To install the current release download, go to: [SharePoint Migration Tool](https://spmtreleasescus.blob.core.windows.net/install/default.htm)
  
 **Migrating data files from SharePoint Server document libraries**
  
1. Start SPMT, and then enter your Microsoft 365 username and password.
    
2. Select **Start your first migration**.
    
3. Select **SharePoint Server**.
    
4. Enter the SharePoint Server site URL where your content is located, and then select **Next**.
    
    > [!IMPORTANT]
    > Proxy connections are not supported. Using Proxy connections yields errors such as "SharePoint login fail" or "cannot load document library". 
  
5. Enter your username and password to the SharePoint Server site; username must use the format of someone@example.com. Select **Sign in**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 

  
6. Select the document library where your files are located. The dropdown contains all your possible choices.
    
7. Enter the URL of the SharePoint site where you want your files migrated.
    
8. Select the document library to where your files will be copied.
    
9. Select **Add**. This task is added to the list. If you want to select another set of data files to migrate, select **Add a source**.
    
 **Migrating data files from a local file share**

1. Start SPMT, and then enter your Microsoft 365 username and password.
    
2. Select **Start your first migration**.
    
3. Select **File Share.**
    
4. Enter the source path of the file share where your content is located, and then select **Next**.
    
5. Enter the URL of the SharePoint site where you want your files migrated, and then select **Next**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 
  
6. Select the document library to where your files will be copied, and then select **Next**.

7. This task is added to the list. If you want to select another set of data files to migrate, select **Add another source**.
    
8. When you have finished selecting your sources, select **Next**.

9. Review your settings, and then select **Migrate**.
  </br></br>  

 
 **To use a JSON or CSV file for bulk migration**

If you have many sources to migrate, you can use either a JSON or CSV file to do a bulk migration. To learn more on how to create a JSON or CSV file for data content migration, see [How to format your JSON or CSV file for data content migration](how-to-format-your-csv-file-for-data-content-migration.md).
  
1. Start SPMT, and then enter your Microsoft 365 username and password.
    
2. Select **Start your first migration**.
    
3. Select **JSON or CSV file for bulk migration.**
    
4. Enter the full path of your .CSV or .JSON file where your content is located, and then select **Add**.
    
5. Enter the URL of the SharePoint site where you want your files migrated, and then select **Next**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 
    
6. Select **JSON or CSV file for bulk migration**. Enter the location of your file, or select **Choose File** to locate it. Select **Add**.
    
    If you are migrating files from an on-premises SharePoint Server, you are prompted for your username and password for that site unless you provided those credentials in previous steps. 
  
    If any errors appear in your file, it is detected on a line-by-line basis. The error indicates which line or lines contain(s) the errors. You cannot proceed until you correct the errors in your file. 
  
   > [!IMPORTANT]
   > We do not support proxy connections. Using Proxy connections yields errors, such as "SharePoint login fail" or "cannot load document library". 
  
7. If you want to select another set of data files to migrate, select **Add a source**; otherwise, select **Next**.
    
8. Review your settings, and the select **Migrate**.
    
## Monitoring and reporting status of migration jobs

After you select **Migrate**, the progress of your migration jobs appears. As they complete, you can view either detailed or summary reports of an individual job or a single summary report that includes all migration jobs submitted during this session. To learn more, see [Using the SharePoint Migration Tool Reports](using-the-sharepoint-migration-tool-reports.md).
 
## Resuming migration jobs

If you need to close SPMT before a submitted job has completed, you can restart the tool from any computer.
  
> [!NOTE]
> To resume a submitted migration job, it has to have been running  *at least* **5 minutes**. It pauses at the point you closed the SPMT. If your submitted job was running less than five minutes before the tool closed, you must resubmit the job.

**To resume migration jobs**
  
1. Launch SPMT. Using the same Microsoft 365 username and password you used when you originally submitted the job, select **Sign In**. 
    
2. After you sign in, a screen displays any paused migrations, providing details about what has been completed and what remains.
    
3. If you want to add additional migration tasks, select **Select new sources and destinations**; otherwise, select **Next**. Your migration jobs will be resumed. If you are migrating files from an on-premises SharePoint Server, you are prompted for your username and password for that site.
    
## Incremental migration

After a migration task has completed, you can save it to be rerun at a later date, allowing you to copy only those new or updated files in the source location. 

> [!NOTE]
> If you wish to make changes to this setting, do so before your initial migration job is submitted. This setting is global; it will apply to all subsequent tasks you submit. 
  
When this setting is on, an incremental check of the SharePoint target environment is performed. Files are evaluated as follows:
  
|**Status**|**Result**|
|:-----|:-----|
|Modified time of the source file is earlier than the modified time of the target file.  <br/> |File will not be migrated.  <br/> |
|Files or lists exist in the SPO target location.  <br/> |Migration will skip those existing objects during scan.  <br/> |
|Time stamp on files or object in the source location is newer in the source <br/> |The newer files are migrated.  <br/> |
|Source is a file share.  <br/> |Validation for migration will be based on the file/folder path.  <br/> |
|Source is an on-premises SharePoint Server/  <br/> |Validation for migration will be based on list item GUID. Use the folder path as a fallback.  <br/> |

## Availability  
> [!NOTE]
> Currently, the **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. </br></br> It is also not available for users of Microsoft 365 with the German cloud with the data trustee, *German Telekom*. However, we do support it for users in Germany whose data location is not in the German datacenter.

   
## Related Topics
<a name="BKMK_Settings"> </a>

[Introducing the SharePoint Migration Tool](introducing-the-sharepoint-migration-tool.md)
  
[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to format your JSON or CSV file for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint and OneDrive Migration Speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint Migration Tool Feedback and Support Forum](https://social.technet.microsoft.com/Forums/en-US/home?forum=SharePointMigrationTool)
  

