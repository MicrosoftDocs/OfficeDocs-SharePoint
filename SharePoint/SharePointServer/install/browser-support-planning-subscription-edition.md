---
ms.date: 03/13/2018
title: "Plan browser support in SharePoint Server Subscription Edition"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: interactive-tutorial
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ff6c5b8c-59bd-4079-8f0b-de4f8b4e0a86
description: "Learn about how SharePoint Server Subscription Edition supports Internet Explorer, Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge."
---

# Plan browser support in SharePoint Server Subscription Edition

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]
  
SharePoint Server Subscription Edition supports several commonly used web browsers, such as ![Microsoft Edge icon](../media/microsoft-edge-icon.png) Microsoft Edge, ![Google Chrome browser logo](../media/chrome-small.jpg) Google Chrome, ![Mozilla Firefox browser logo](../media/firefox_small.png) Mozilla Firefox, ![Apple Safari browser logo](../media/safari-small.png) Apple Safari, and ![Internet Explorer browser logo](../media/internetexplorersmall.png) Internet Explorer. However, certain web browsers can cause SharePoint Server Subscription Edition functionality to be downgraded, limited, or available only through alternative steps. 

> [!NOTE]
> Internet Explorer 11 and Edge IE compatibility mode are supported only in the SharePoint Central Administration site. 
> 
> Internet Explorer 11 and Edge IE compatibility mode are not supported in Team sites, OneDrive personal sites, or any other types of SharePoint content sites. Microsoft recommends exploring Microsoft Edge as the replacement for Internet Explorer 11.

As you plan your deployment of SharePoint Server Subscription Edition, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint Server Subscription Edition.
    
## Key planning phase of browser support
<a name="section2"> </a>

Browser support is an important part of your SharePoint Server Subscription Edition implementation. Before you install SharePoint Server, make sure that you know the browsers that SharePoint Server supports. The information in this article describes browser support in the following sections:
  
- Browser support levels
    
- Browser details
    
### Browser support levels in SharePoint Server Subscription Edition
<a name="supportmatrix"> </a>

The following table summarizes the support levels of typically used web browsers.
  
|**Browser**|**Supported**|**Not supported**|
|:-----|:-----|:-----|
|Microsoft Edge (Chromium) <br/> |X  <br/> ||
|Microsoft Edge (EdgeHTML - Legacy) <br/> ||X  <br/>|
|Internet Explorer 11  <br/> |X  <br/> ||
|Internet Explorer 10  <br/> ||X  <br/> |
|Internet Explorer 9  <br/> ||X  <br/> |
|Internet Explorer 8  <br/> ||X  <br/> |
|Internet Explorer 7  <br/> ||X  <br/> |
|Internet Explorer 6  <br/> ||X  <br/> |
|Google Chrome (latest released version)  <br/> |X  <br/> ||
|Mozilla Firefox (latest released version plus immediate previous version)  <br/> |X  <br/> ||
|Apple Safari (latest released version)  <br/> |X  <br/> ||
   
### Browser details
<a name="browserdetail"> </a>

Review the details of the web browser that you have or plan to use in your organization to ensure that the web browser works with SharePoint Server Subscription Edition, and according to your business needs.

 **Internet Explorer and older functionalities**
  
> [!NOTE]
> Some older SharePoint functionalities that rely on NPAPI or ActiveX will not work on browsers other than Internet Explorer. Since Internet Explorer 11 is no longer supported in all types of SharePoint Sites except Central Administration site, these old functionalities are deprecated as well. Although these functionalities still exist in SharePoint Server Subscription Edition, we recommend not to rely on them anymore.
  
   
#### Using ActiveX controls in SharePoint Server
<a name="activex"> </a>

Some functionalities in SharePoint Server require ActiveX controls. This imposes limitations on browsers that don't support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. Since Internet Explorer 11 isn't supported in all types of SharePoint sites except Central Administration site, all supported browsers (including Microsoft Edge) have the following limitations.
  
|Plugin name |DLL file name |What it does | &nbsp; |Known limitations |
|:-----|:-----|:-----|:-----|:-----|
|Digital Signature  <br/> |`Dsigctrl.dll`, `dsigres.dll`  <br/> | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Ensure that the following conditions exist:  <br/>  Forms that are signed on the client can be verified on the server.  <br/>  Forms that are signed on the server can be verified on the client.  <br/> | <br/> |An inability to verify a form produces an error that states that the form can't be signed.  <br/> |
|NameCtrl  <br/> |`Name.dll`  <br/> |Enables a webpage to display a contact card and presence status for people. Integrates through client-side APIs with Office client and Skype for Business client.  <br/> | 
|TaskLauncher  <br/> |`Nameext.dll` <br/> |Used to export items in a task list to Project Server if Project client is installed on the client computer.  <br/> | |If software requirements aren't met, an error message states that you need to install Project client.  <br/> |
|SpreadSheetLauncher  <br/> |`Owssupp.dll`  <br/> |Used to verify whether Excel is installed for Export to Excel feature.  <br/> | |If Excel isn't installed, the user may be prompted to download the file `query.iqy` which can then be opened in Excel.  <br/> |
|StssyncHandler  <br/> |`Owssupp.dll`  <br/> |Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook. Non-IE clients may have an additional prompt to open the calendar in Outlook.  <br/> |
|ExportDatabase  <br/> |`Owssupp.dll`  <br/> |Enables a user to use an application such as Access to create or open a database that contains SharePoint list data.  <br/> | |To export a list, the client computer must have a SharePoint compatible application.  <br/> |
|OpenDocuments  <br/> |`Owssupp.dll`  <br/> |Starts Office client applications so that a user can create or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write.  <br/> | |If a compatible Office application or browser isn't installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser.  <br/> |
|CopyCtl  <br/> |`Stsupld.dll`  <br/> |Enables a user to copy a document on a SharePoint site to one or more locations on a server.  <br/> | |In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog isn't displayed.  <br/> |
|PPActiveX  <br/> |`PPSLAX.dll`  <br/> |Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library.  <br/> | |Doesn't work on Click-to-Run installations of Office and version of Office that run on Windows for ARM.  <br/> |
|BCSLauncher  <br/> |`BCSLaunch.dll`  <br/> |Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server.  <br/> | 

Other functionality, such as **Form settings** in **List settings** only function with Internet Explorer.
   
## Mobile browser support
<a name="mobile"> </a>

SharePoint Server Subscription Edition supports the following versions:
  
- Internet Explorer and Microsoft Edge on Windows Phone 8.1 or later.
    
- Latest version of Microsoft Edge or Chrome on Android 4.4 or later.

- Microsoft Edge, Chrome or Safari on iOS10 or later

