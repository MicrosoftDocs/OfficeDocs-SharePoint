---
title: Create a task in SharePoint Migration Tool (SPMT)
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: troubleshooting
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Learn now to create a migration task using the SharePoint Migration Tool (SPMT)."
---
# Step 2: Create a migration task with SPMT

When creating a migration task you can choose to simply migrate data files from your SharePoint Server document libraries or also modernize your site collection structure during migration. 

>[!Note]
>When you first launch SPMT, you are prompted for your Microsoft 365 username and password. The credentials you provide will be to the migration *destination*.

Choose how you want to create your task:

|How|Description|
|:-----|:-----|
|[Create a task that doesn't include all subsites](#create-a-task-that-doesn't-include-all-subsites)|If you plan on migrating only selected sites or document libraries, follow these steps|
|[Create a task that include all subsites](create-a-task-that-includes-all-subsites)|If you plan on including ALL your subsites in your migration, use this method.  It will prompt you for if and how you want to modernize your site structure (this feature is in public preview)|
|[Create a task using a CSV or JSON file](#create-a-task-using-a-csv-or-json-file)|This is the bulk upload method of creating a task. If you have a large number of sources you can enter them into a CSV or JSON file, and upload the file to SPMT|

### Create a task that doesn't include all subsites
  
1. Start SPMT, and then enter your Microsoft 365 username and password.
    
2. Select **Start your first migration**.
    
3. Select **SharePoint Server**.
    
4. Enter the SharePoint Server site URL where your content is located, and then select **Next**.
    
    > [!IMPORTANT]
    > Proxy connections are not supported. Using Proxy connections yields errors such as "SharePoint login fail" or "cannot load document library". 
  
5. Enter your username and password to the SharePoint Server site; it can be UserID or user email. Select **Sign in**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 

  
6. Select the document library where your files are located. The dropdown contains all your possible choices. If don't select a document library or list, the site will be migrated.If you want to include all subsites, select **Include all subsites**.    
7. Enter the URL of the SharePoint site where you want your files migrated.   
8. Select the document library to where your files will be copied.   
9. Select **Add**. This task is added to the list. If you want to select another set of data files to migrate, select **Add a source**.
    

### Create a task that includes all subsites

  
1. Start SPMT, and then enter your Microsoft 365 username and password.
    
2. Select **Start your first migration**.
    
3. Select **SharePoint Server**.
    
4. Enter the SharePoint Server site URL where your content is located, and then select **Next**.
    
    > [!IMPORTANT]
    > Proxy connections are not supported. Using Proxy connections yields errors such as "SharePoint login fail" or "cannot load document library". 
  
5. Enter your username and password to the SharePoint Server site; it can be UserID or user email. Select **Sign in**.
    
    > [!NOTE]
    > If you have already signed in to that site once while using this tool, you won't be prompted again for the same site. 

  
6. Select the document library where your files are located. The dropdown contains all your possible choices. If don't select a document library or list, the site will be migrated.If you want to include all subsites, select **Include all subsites**. 
    
7. Enter the URL of the SharePoint site where you want your files migrated.
    
8. Select the document library to where your files will be copied.
9. Select either **Keep the classic site structure** (make no changes to the site structure) or **Switch to modern site structure** to modernize your site structure during migration.

    ![choose your site structure ](media/spmt-site-structure-choice.png)

10.	If you chose **Switch to modern site structure**, select if you want the promoted level-one subsites associated with a hub. 

   ![select a site structure hub association](media/spmt-select-hub-association.png)

11. If you chose to associate with a hub, select if you want to register your destination as a hub or associate the sites with an existing hub.

    ![spmt-site-structure-associate-destination-register-hub](media/spmt-site-structure-associate-destination-as-hub.png)

12.  If you selected to associate the promoted level-one subsites with an existing hub, select the hub name from the dropdown list, and select **Next**.

   ![enter the name of an existing hub to associate your sites with](media/spmt-site-structure-associate-existing-hub.png)

13.	Review and edit destination URL for each subsite as needed.
    
14. Select **Add**. This task is added to the list. If you want to select another set of data files to migrate, select **Add a source**.




### Create a task using a CSV or JSON file

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
|Modified time of the source file is earlier than the modified time of the target file. |File will not be migrated. |
|Files or lists exist in the SharePoint target location. |Migration will skip those existing objects during scan.  |
|Time stamp on files or object in the source location is newer in the source <br/> |The newer files are migrated. |
|Source is a file share.|Validation for migration will be based on the file/folder path.  |
|Source is an on-premises SharePoint Server |Validation for migration will be based on list item GUID. Use the folder path as a fallback. |

## Next step

[**Step 3: Monitor and reporting status of migrations tasks**](using-the-sharepoint-migration-tool-reports.md)
