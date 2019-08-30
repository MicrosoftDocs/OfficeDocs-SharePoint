---
title: "Add or remove a file type from the search index in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/7/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 7d88430f-2f0f-4c83-863b-ad840bdbf696
description: "Learn how to add or remove a file type from the search index and how to start or stop including content from the file type, in the search index."
---

# Add or remove a file type from the search index in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Before you start, you may want to read [Default crawled file name extensions and parsed file types in SharePoint Server](../technical-reference/default-crawled-file-name-extensions-and-parsed-file-types.md). This article lists the file types that SharePoint Server by default includes in the search index.
  
If your SharePoint environment is hybrid and uses [cloud hybrid search](/SharePoint/hybrid/learn-about-cloud-hybrid-search-for-sharepoint), you can decide what types of files that are stored in SharePoint Server that you want to add or remove from the Office 365 index. Use the following procedures on the server that hosts the crawl component in the cloud Search service application. 
  
To add or remove a file type from the search index: 
  
1. Add or remove the file name extension from the list of file name extensions on the Manage File Types page. See [Add or remove file name extensions from the Manage File Types page](add-or-remove-a-file-type-from-the-search-index.md#proc1).
    
2. Run a full crawl for all content sources that this change might affect.
    
When the full crawl finishes, the search index will include or exclude properties from files of the type that you have either added or removed.
  
To start including content from a file type, in the search index:
  
1. On a server that hosts a content processing component in the Search service application, check whether the format of the file type is supported by a built-in format handler or a third-party filter-based format handler (iFilter). Built-in format handlers are the those that SharePoint Server has by default. See [View information about file formats that can be parsed](add-or-remove-a-file-type-from-the-search-index.md#ViewInformationFileFormats).
    
2. If the server does not have a format handler for the file type, install a third-party filter-based format handler on all servers hosting content processing components in the Search service application. Follow the installation guidance given by the manufacturer of the third-party format handler.
    
3. On all servers that host a content processing component in the Search service application, enable parsing of the format of the file and the file name extension. See [Enable or disable parsing of a file format](add-or-remove-a-file-type-from-the-search-index.md#EnbleParsing).
    
4. Run a full crawl for all content sources that this change might affect.
    
When the full crawl finishes, the search index will include content from files of the type that you enabled.
  
To stop including content from a file type, in the search index:
  
1. On a server that hosts a content processing component in the Search service application, check whether the format of the file type is supported by a built-in format handler or a third-party filter-based format handler (iFilter). Built-in format handlers are those that SharePoint Server has by default.
    
2. On all servers that host a content processing component in the Search service application, disable parsing of the format of the file and the file name extension. See [Enable or disable parsing of a file format](add-or-remove-a-file-type-from-the-search-index.md#EnbleParsing).
    
3. Run a full crawl for all content sources that this change might affect.
    
When the full crawl finishes, the search index will exclude content from files of the type that you disabled.
  
    
## Add or remove file name extensions from the Manage File Types page
<a name="proc1"> </a>

### 

 **To add a file name extension to the Manage File Types page**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the Application Management section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the Crawling section, click **File types**. The Manage File Types page appears.
    
5. Click **New File Type**.
    
6. In the **File extension** box, type the extension of the file type that you want to add. 
    
7. Click **OK**. 
    
8. **Verification:** make sure that the extension appears in the list of file types on the Manage File Types page. 
    
### 

 **To remove a file name extension from the Manage File Types page**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. In Central Administration, in the Application Management section, click **Manage Service Applications**.
    
3. On the Manage Service Applications page, in the list of service applications, click the Search service application.
    
4. On the Search Administration page, in the Crawling section, click **File types**. The Manage File Types page appears.
    
5. Point to the file type that you want to remove, click the arrow that appears and then click **Delete**. 
    
6. Click **OK** to confirm that you want to delete the file type. 
    
7. **Verification:** make sure that the extension no longer appears in the list of file types on the Manage File Types page. 
    
## View information about file formats that can be parsed
<a name="ViewInformationFileFormats"> </a>

To view information about the file formats that the content processing component has format handlers for, you have to use Windows PowerShell.
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on the server.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  Get-SPEnterpriseSearchFileFormat -SearchApplication $ssa
  
  ```

    The result is a list of all file formats that the content processing component in the Search service application referenced by  `$ssa` can parse. For each file format the list shows: 
    
  - The file name extension and mime type
    
  - The type of format handler that the content processing component uses to parse the format. The entry "BuiltIn:True" indicates a built-in format handler. The entry "BuiltIn:False" indicates a third-party filter-based format handler.
    
  - The parsing state of the format. The entry "Enabled:True" indicates that parsing is enabled. The entry "Enabled:False" indicates that parsing is disabled.
    
## Enable or disable parsing of a file format
<a name="EnbleParsing"> </a>

To enable or disable parsing of a file format, you have to use Windows PowerShell. 
  
### 

 **To enable parsing of a file format using a built-in format handler**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on the server that hosts the content processing component.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  Set-SPEnterpriseSearchFileFormatState -SearchApplication $ssa FormatID $TRUE
  ```

    Where:
    
    FormatID is the identity of the file format.
    
    $TRUE enables the format handler to parse the file type.
    
4. Restart the SharePoint Search Host Controller service to apply the changes:
    
  - Open a command prompt window on the server that hosts the content processing component. On the **Start** menu, click **All Programs**, click **Accessories**, right-click **Command Prompt** and then click **Run as administrator**.
    
  - To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
  - To restart the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
5. **Verification:** show the list of file name extensions and file formats that the content processing component can parse and make sure that the file name extension is there. See [View information about file formats that can be parsed](add-or-remove-a-file-type-from-the-search-index.md#ViewInformationFileFormats). 
    
### 

 **To disable parsing of a file format using a built-in format handler**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on the server that hosts the content processing component.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  Set-SPEnterpriseSearchFileFormatState -SearchApplication $ssa FormatID $FALSE
  ```

    Where:
    
    FormatID is the identity of the file format.
    
    $FALSE disables the format handler from parsing the file type.
    
4. Restart the SharePoint Search Host Controller service to apply the changes:
    
  - Open a command prompt window on the server that hosts the content processing component. On the **Start** menu, click **All Programs**, click **Accessories**, right-click **Command Prompt** and then click **Run as administrator**.
    
  - To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
  - To restart the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
5. **Verification:** show the list of file name extensions and file formats that the content processing component can parse and make sure that the file name extension is not there. See [View information about file formats that can be parsed](add-or-remove-a-file-type-from-the-search-index.md#ViewInformationFileFormats).
    
### 

 **To enable parsing of a file format using a third-party filter-based format handler**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on the server that hosts the content processing component.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  New-SPEnterpriseSearchFileFormat -SearchApplication $ssa FileNameExtension FileFormat application/FileApplication
  ```

    Where:
    
    FileNameExtension is the file name extension of the file type.
    
    FileFormat is the format of the file type. The format is often the name of the application.
    
    application/FileApplication is the mime type of the file type. The mime type must consist of a type and a subtype. In this example, application is the type and FileApplication is the subtype. For example, for Word files, the type is application and the subtype is msword. Together they form the complete mime type: application/msword.
    
4. Restart the SharePoint Search Host Controller service to apply the changes:
    
  - Open a command prompt window on the server that hosts the content processing component. On the **Start** menu, click **All Programs**, click **Accessories**, right-click **Command Prompt** and then click **Run as administrator**.
    
  - To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
  - To restart the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
5. **Verification:** show the list of file name extensions and file formats that the content processing component can parse and make sure that the file name extension is there. See [View information about file formats that can be parsed](add-or-remove-a-file-type-from-the-search-index.md#ViewInformationFileFormats). 
    
### 

 **To disable parsing of a file format using a third-party filter-based format handler**
  
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
2. Start a SharePoint Management Shell on the server that hosts the content processing component.
    
3. At the Microsoft PowerShell command prompt, type the following commands:
    
  ```
  $ssa = Get-SPEnterpriseSearchServiceApplication
  Remove-SPEnterpriseSearchFileFormat -SearchApplication $ssa -Identity FileNameExtension
  ```

    Where:
    
    FileNameExtension is the file name extension of the file type.
    
4. Restart the SharePoint Search Host Controller service to apply the changes:
    
  - Open a command prompt window on the server that hosts the content processing component. On the **Start** menu, click **All Programs**, click **Accessories**, right-click **Command Prompt** and then click **Run as administrator**.
    
  - To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
  - To restart the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
5. **Verification:** show the list of file name extensions and file formats that the content processing component can parse and make sure that the file name extension is not there. See [View information about file formats that can be parsed](add-or-remove-a-file-type-from-the-search-index.md#ViewInformationFileFormats).
    

