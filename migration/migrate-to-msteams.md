---
title: Migrating to Microsoft Teams using the SharePoint Migration Tool 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: troubleshooting
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Migrating to Microsoft Teams using the SharePoint Migration Tool "
---
# Migrating to Microsoft Teams using the SharePoint Migration Tool 

The SharePoint Migration Tool lets you migrate lists or files from your SharePoint on-premises document libraries or from your on-premises file shares and easily move them to either SharePoint, OneDrive or Microsoft Teams in Office 365. It is available to Office 365 users. 
Designed to be used for migrations ranging from the smallest set of files to a large scale enterprise migration, the SharePoint Migration Tool will let you bring your information to the cloud and take advantage of the latest collaboration, intelligence, and security solutions with Office 365. 

## Microsoft Teams and SharePoint File Storage 
With Microsoft Teams you can create a more open, digital environment.  Microsoft Teams is a chat-based workspace that brings together people, conversations, content and tools—creating a more open, digital environment. Threaded conversations make it easy to understand what each employee is referencing, and employees can co-author and collaborate on Word, Excel, PowerPoint, and OneNote documents without ever leaving the app. 

Both Teams and SharePoint team sites are organized by topic, project, organization, or some other focal point for a team of people. Hence, in any given organization, Teams and channels will often follow a similar structure to SharePoint team and project sites. 

In fact, this is inherent in the design. Every Microsoft Team automatically has a modern SharePoint team site associated with it; that's where channel documents are stored. Each channel is associated with a folder in the SharePoint site's document library. In addition, files sent between users outside of a Teams channel are stored in the sender's OneDrive for Business folder. 
Files are at the center of collaboration, using the SharePoint Migration Tool you can quickly and easily start taking advantage of Microsoft Teams through migrating your on-premises content to Microsoft Teams libraries and folders. 
 
## Migrating SharePoint 2013 documents to the Microsoft Teams Default Document Library 
1. Start the SharePoint Migration Tool, and then click Next. 
2. Enter your Office 365 username and password, and then click Sign in. 
3. Select Choose a source and destination. 
4. Select SharePoint Server (on-premises). 
5. Enter the SharePoint Server 2013 site URL where your data is currently located. Click Next. 
6. Enter your username and password to the SharePoint Server site; username must use the format of someone@example.com. Click Sign in. 
7. Choose the document library where your files are located. The drop-down list will contain all your possible choices. 
8. Enter the URL of the SharePoint Online site where you want your files migrated. 
9. Select the document library to where your files will be moved. 
10. Click Add. This task will be added to the list. If you want to select another set of data files to migrate, click Choose a source and destination. 


## Migrating File Shares to the Microsoft Teams Default Document Library 

1. Start the SharePoint Migration Tool, and then click Next. 
2. Enter your Office 365 username and password, and then click Sign in. 
3. Select Choose a source and destination. 
4. Select File share. 
5. Enter the path of the file share where your data is located. Click Next. 
6. Enter the URL of the SharePoint Online site where you want your files migrated, and then enter your username and password to the SharePoint Server site. Click Sign in. 
7. Choose the document library to where your files will be moved. 
8. Click Add. This task will be added to the list. If you want to select another set of data files to migrate, click Choose a source and destination. 
9. When you have finished selecting your sources, click Migrate. 
 
## Migrating File Shares, Home Directories, or SharePoint 2013 documents to Microsoft Teams to Channel Folders 

Using the SharePoint Migration Tool you can migrate content to the Microsoft Teams default document library as described in the previous steps, in addition to Microsoft Teams channels.  Migrating to Microsoft Teams channels requires using either the CSV or JSON bulk migration option with the SharePoint Migration Tool. 

### To use a JSON or CSV file for bulk migration 

1. Open the SharePoint Migration Tool, and then click Next. 
2. Enter your Office 365 username and password, and then click Sign in. 
3. Select JSON or CSV file for bulk migration. Enter the location of your file, or click Choose File to locate it. Click Add. 

Sample: 
Assuming a SharePoint on-premises migration to the General channel folder as illustrated earlier this example shows how it would appear in a .txt file. 
Source,SourceDocLib,SourceSubFolder,TargetWeb,TargetDocLib,TargetSubFolder 
C:\MigrationTests\testfiles,,,https://contoso.sharepoint.com/sites/Finance/,SharePoint Documents,General 
https://sharepoint2013.com/sites/contosoteamsite/,DocumentLibraryName,DocLibrarySubfolder_name,https://contoso.sharepoint.com/sites/Finance/,SharePoint Documents,General 
For more information on how to create a JSON or CSV file for data content migration, see How to format your JSON or CSV file for data content migration. 

4. If your JSON or CSV file is successfully added without errors, the job will be added to your list of sources and destinations. 
5. If you want to select another set of data files to migrate, click Choose a source and destination. 
6. When you have finished selecting your sources, click Migrate. 

Learn more about the SharePoint Migration Tool and the different ways it can help to accelerate success in Office 365 at https://aka.ms/spmt.  
 
 
 