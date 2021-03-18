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
localization_priority: Priority
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Learn now to create a migration task using the SharePoint Migration Tool (SPMT)."
---
# Step 2: Create a migration task with SPMT

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
    

**Next step:**  [**Step 3: Monitor and Report**]()