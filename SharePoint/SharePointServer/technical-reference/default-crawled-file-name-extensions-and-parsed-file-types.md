---
title: "Default crawled file name extensions and parsed file types in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 19d553a7-7001-4b07-a03d-616b865b05ae
description: "Learn which file name extensions SharePoint Server crawls by default and which file types it parses by default."
---

# Default crawled file name extensions and parsed file types in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
The crawl component can only crawl a file if the list on the Manage File Types page includes the file name extension. The content processing component can only parse the contents of a crawled file:
  
- When it has a format handler that can parse the file format.
    
- When it is enabled to use the format handler to parse files that have the file format and file name extension.
    
By default, SharePoint Server satisfies these requirements for many file types.
  
## Default crawled file name extensions and parsed file formats
<a name="Section1"> </a>

The following table shows all the file formats that SharePoint Server has built-in format handlers for. The table shows one or several format ID and file name extensions for each file format. By default SharePoint Server is enabled to parse files that have these file formats and file name extensions. For each file name extension the table also indicates whether the Manage File Types page by default includes the file name extension.
  
> [!NOTE]
>  SharePoint Online supports the same file name extensions as in this table. In addition, SharePoint Online also supports the following: .one .xlt .xlc .xlb 
  
|||||
|:-----|:-----|:-----|:-----|
|**File format** <br/> |**Format ID** <br/> |**File name extension** <br/> |**File name extension listed on the Manage File Types page by default** <br/> |
|Email message  <br/> |eml  <br/> |.eml  <br/> |Yes  <br/> |
|Email message  <br/> |nws  <br/> |.nws  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.ascx  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.asp  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.aspx  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.css  <br/> |No  <br/> |
|HTML  <br/> |html  <br/> |.hta  <br/> |No  <br/> |
|HTML  <br/> |html  <br/> |.htm  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.html  <br/> |Yes  <br/> |
|HTML  <br/> |html  <br/> |.htw  <br/> |No  <br/> |
|HTML  <br/> |html  <br/> |.htx  <br/> |No  <br/> |
|HTML  <br/> |html  <br/> |.jhtml  <br/> |No  <br/> |
|HTML  <br/> |html  <br/> |.stm  <br/> |No  <br/> |
|MHTML document  <br/> |mhtml  <br/> |.mht  <br/> |Yes  <br/> |
|MHTML document  <br/> |mhtml  <br/> |.mhtml  <br/> |Yes  <br/> |
|Microsoft Excel  <br/> |xlb  <br/> |.xlb  <br/> |No  <br/> |
|Microsoft Excel  <br/> |xlc  <br/> |.xlc  <br/> |No  <br/> |
|Microsoft Excel  <br/> |xls  <br/> |.xls  <br/> |Yes  <br/> |
|Microsoft Excel  <br/> |xlsb  <br/> |.xlsb  <br/> |Yes  <br/> |
|Microsoft Excel  <br/> |xlsm  <br/> |.xlsm  <br/> |Yes  <br/> |
|Microsoft Excel  <br/> |xlsx  <br/> |.xlsx  <br/> |Yes  <br/> |
|Microsoft Excel  <br/> |xlt  <br/> |.xlt  <br/> |No  <br/> |
|Microsoft OneNote  <br/> |one  <br/> |.one  <br/> |No  <br/> |
|Microsoft PowerPoint  <br/> |pot  <br/> |.pot  <br/> |No  <br/> |
|Microsoft PowerPoint  <br/> |ppa  <br/> |.ppa  <br/> |No  <br/> |
|Microsoft PowerPoint  <br/> |pps  <br/> |.pps  <br/> |No  <br/> |
|Microsoft PowerPoint  <br/> |ppt  <br/> |.ppt  <br/> |Yes  <br/> |
|Microsoft PowerPoint  <br/> |pptm  <br/> |.pptm  <br/> |Yes  <br/> |
|Microsoft PowerPoint  <br/> |pptx  <br/> |.pptx  <br/> |Yes  <br/> |
|Microsoft Publisher  <br/> |pub  <br/> |.pub  <br/> |Yes  <br/> |
|Microsoft Word  <br/> |doc  <br/> |.doc  <br/> |Yes  <br/> |
|Microsoft Word  <br/> |docm  <br/> |.docm  <br/> |Yes  <br/> |
|Microsoft Word  <br/> |docx  <br/> |.docx  <br/> |Yes  <br/> |
|Microsoft Word  <br/> |dot  <br/> |.dot  <br/> |Yes  <br/> |
|Microsoft Word  <br/> |dotx  <br/> |.dotx  <br/> |Yes  <br/> |
|Microsoft XPS  <br/> |xps  <br/> |.xps  <br/> |No  <br/> |
|Open Document Chart  <br/> |odc  <br/> |.odc  <br/> |Yes  <br/> |
|Open Document Presentation  <br/> |odp  <br/> |.odp  <br/> |Yes  <br/> |
|Open Document Spreadsheet  <br/> |ods  <br/> |.ods  <br/> |Yes  <br/> |
|Open Document Text  <br/> |odt  <br/> |.odt  <br/> |Yes  <br/> |
|Outlook item  <br/> |msg  <br/> |.msg  <br/> |Yes  <br/> |
|Portable Document Format  <br/> |pdf  <br/> |.pdf  <br/> |Yes  <br/> |
|Rich Text Format  <br/> |rtf  <br/> |.rtf  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.asm  <br/> |Yes  <br/> |
|Text  <br/> |txt  <br/> |.bat  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.c  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.cmd  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.cpp  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.csv  <br/> |Yes  <br/> |
|Text  <br/> |txt  <br/> |.cxx  <br/> |Yes  <br/> |
|Text  <br/> |txt  <br/> |.def  <br/> |Yes  <br/> |
|Text  <br/> |txt  <br/> |.h  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.hpp  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.lnk  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.mpx  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.php  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.trf  <br/> |No  <br/> |
|Text  <br/> |txt  <br/> |.txt  <br/> |Yes  <br/> |
|Text  <br/> |txt  <br/> |.url  <br/> |No  <br/> |
|TIFF  <br/> |tiff  <br/> |.tif  <br/> |No  <br/> |
|TIFF  <br/> |tiff  <br/> |.tiff  <br/> |No  <br/> |
|Visio  <br/> |vdw  <br/> |.vdw  <br/> |Yes  <br/> |
|Visio  <br/> |vdx  <br/> |.vdx  <br/> |Yes  <br/> |
|Visio  <br/> |vsd  <br/> |.vsd  <br/> |Yes  <br/> |
|Visio  <br/> |vsdm  <br/> |.vsdm  <br/> |Yes  <br/> |
|Visio  <br/> |vsdx  <br/> |.vsdx  <br/> |Yes  <br/> |
|Visio  <br/> |vss  <br/> |.vss  <br/> |Yes  <br/> |
|Visio  <br/> |vssm  <br/> |.vssm  <br/> |Yes  <br/> |
|Visio  <br/> |vssx  <br/> |.vssx  <br/> |Yes  <br/> |
|Visio  <br/> |vst  <br/> |.vst  <br/> |Yes  <br/> |
|Visio  <br/> |vstm  <br/> |.vstm  <br/> |Yes  <br/> |
|Visio  <br/> |vstx  <br/> |.vstx  <br/> |Yes  <br/> |
|Visio  <br/> |vsx  <br/> |.vsx  <br/> |Yes  <br/> |
|Visio  <br/> |vtx  <br/> |.vtx  <br/> |Yes  <br/> |
|XML  <br/> |xml  <br/> |.jsp  <br/> |Yes  <br/> |
|XML  <br/> |xml  <br/> |.mspx  <br/> |No  <br/> |
|XML  <br/> |xml  <br/> |.rss  <br/> |No  <br/> |
|XML  <br/> |xml  <br/> |.xml  <br/> |Yes  <br/> |
|ZIP  <br/> |zip  <br/> |.zip  <br/> |Yes  <br/> |
   
 **NOTE:** The following folders are reserved names and search doesn't crawl them: 
  
- AUX
    
- COM1
    
- COM2
    
- COM3
    
- COM4
    
- COM5
    
- COM6
    
- COM7
    
- COM8
    
- COM9
    
- CON
    
- LPT1
    
- LPT2
    
- LPT3
    
- LPT4
    
- LPT5
    
- LPT6
    
- LPT7
    
- LPT8
    
- LPT9
    
- NUL
    
- PRN
    
- CLOCK$
    

