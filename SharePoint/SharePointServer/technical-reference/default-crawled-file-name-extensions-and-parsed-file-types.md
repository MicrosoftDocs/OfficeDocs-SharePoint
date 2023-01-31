---
title: "Default crawled file name extensions and parsed file types in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 3/8/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 19d553a7-7001-4b07-a03d-616b865b05ae
description: "Learn which file name extensions SharePoint Server and SharePoint in Microsoft 365 crawl by default and which file types it parses by default."
---

# Default crawled file name extensions and parsed file types in SharePoint Server and SharePoint in Microsoft 365

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)]

The crawl component of SharePoint Server can only crawl a file if the list on the Manage File Types page includes the file name extension. The content processing component can only parse the contents of a crawled file:

- When it has a format handler that can parse the file format.
- When it is enabled to use the format handler to parse files that have the file format and file name extension.

By default, SharePoint Server satisfies these requirements for many file types.

## Default crawled file name extensions and parsed file formats
<a name="Section1"> </a>

The following table shows all the file formats that SharePoint Server and SharePoint in Microsoft 365 have built-in format handlers for. The table shows one or several format ID and file name extensions for each file format. By default SharePoint Server and SharePoint in Microsoft 365 are enabled to parse files that have these file formats and file name extensions. For each file name extension the table also indicates whether the Manage File Types page by default includes the file name extension.

> [!NOTE]
>  SharePoint in Microsoft 365 also supports the following file name extensions: .one .xlt .xlc .xlb

| **File format** | **Format ID** | **File name extension** | **File name extension listed on the Manage File Types page by default** |
|-----|-----|-----|-----|
| Email message | eml | .eml | Yes |
| Email message | nws | .nws | Yes |
| HTML | html | .ascx | Yes |
| HTML | html | .asp | Yes |
| HTML | html | .aspx | Yes |
| HTML | html | .css | No |
| HTML | html | .hta | No |
| HTML | html | .htm | Yes |
| HTML | html | .html | Yes |
| HTML | html | .htw | No |
| HTML | html | .htx | No |
| HTML | html | .jhtml | No |
| HTML | html | .stm | No |
| MHTML document | mhtml | .mht | Yes |
| MHTML document | mhtml | .mhtml | Yes |
| Microsoft Excel | xlb | .xlb | No |
| Microsoft Excel | xlc | .xlc | No |
| Microsoft Excel | xls | .xls | Yes |
| Microsoft Excel | xlsb | .xlsb | Yes |
| Microsoft Excel | xlsm | .xlsm | Yes |
| Microsoft Excel | xlsx | .xlsx | Yes |
| Microsoft Excel | xlt | .xlt | No |
| Microsoft OneNote | one | .one | No |
| Microsoft PowerPoint | pot | .pot | No |
| Microsoft PowerPoint | ppa | .ppa | No |
| Microsoft PowerPoint | pps | .pps | No |
| Microsoft PowerPoint | ppt | .ppt | Yes |
| Microsoft PowerPoint | pptm | .pptm | Yes |
| Microsoft PowerPoint | pptx | .pptx | Yes |
| Microsoft Publisher | pub | .pub | Yes |
| Microsoft Word | doc | .doc | Yes |
| Microsoft Word | docm | .docm | Yes |
| Microsoft Word | docx | .docx | Yes |
| Microsoft Word | dot | .dot | Yes |
| Microsoft Word | dotx | .dotx | Yes |
| Microsoft XPS | xps | .xps | No |
| Open Document Chart | odc | .odc | Yes |
| Open Document Presentation | odp | .odp | Yes |
| Open Document Spreadsheet | ods | .ods | Yes |
| Open Document Text | odt | .odt | Yes |
| Outlook item | msg | .msg | Yes |
| Portable Document Format | pdf | .pdf | Yes |
| Rich Text Format | rtf | .rtf | No |
| Text | txt | .asm | Yes |
| Text | txt | .bat | No |
| Text | txt | .c | No |
| Text | txt | .cmd | No |
| Text | txt | .cpp | No |
| Text | txt | .csv | Yes |
| Text | txt | .cxx | Yes |
| Text | txt | .def | Yes |
| Text | txt | .h | No |
| Text | txt | .hpp | No |
| Text | txt | .lnk | No |
| Text | txt | .mpx | No |
| Text | txt | .php | No |
| Text | txt | .trf | No |
| Text | txt | .txt | Yes |
| Text | txt | .url | No |
| TIFF | tiff | .tif | No |
| TIFF | tiff | .tiff | No |
| Visio | vdw | .vdw | Yes |
| Visio | vdx | .vdx | Yes |
| Visio | vsd | .vsd | Yes |
| Visio | vsdm | .vsdm | Yes |
| Visio | vsdx | .vsdx | Yes |
| Visio | vss | .vss | Yes |
| Visio | vssm | .vssm | Yes |
| Visio | vssx | .vssx | Yes |
| Visio | vst | .vst | Yes |
| Visio | vstm | .vstm | Yes |
| Visio | vstx | .vstx | Yes |
| Visio | vsx | .vsx | Yes |
| Visio | vtx | .vtx | Yes |
| XML | xml | .jsp | Yes |
| XML | xml | .mspx | No |
| XML | xml | .rss | No |
| XML | xml | .xml | Yes |
| ZIP | zip | .zip | Yes |

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
