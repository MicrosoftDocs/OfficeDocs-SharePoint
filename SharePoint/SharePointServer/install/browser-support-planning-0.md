---
title: "Plan browser support in SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2018
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ff6c5b8c-59bd-4079-8f0b-de4f8b4e0a86
description: "Learn about how SharePoint Server supports Internet Explorer, Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge."
---

# Plan browser support in SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)]
  
SharePoint Servers 2016 and 2019 supports several commonly used web browsers, such as ![Internet Explorer browser logo](../media/internetexplorersmall.png) Internet Explorer, ![Google Chrome browser logo](../media/chrome-small.jpg) Google Chrome, ![Mozilla Firefox browser logo](../media/firefox_small.png) Mozilla Firefox, ![Apple Safari browser logo](../media/safari-small.png) Apple Safari, and Microsoft Edge. However, certain web browsers can cause some SharePoint Servers 2016 or 2019 functionality to be downgraded, limited, or available only through alternative steps. 
  
As you plan your deployment of SharePoint Servers 2016 or 2019, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint Servers 2016 and 2019.
  
    
## Key planning phase of browser support
<a name="section2"> </a>

Browser support is an important part of your SharePoint Servers 2016 or 2019 implementation. Before you install SharePoint Server 2016, make sure that you know the browsers that SharePoint Server 2016 supports. The information in this article describes browser support in the following sections:
  
- Browser support levels
    
- Browser details
    
### Browser support levels in SharePoint Server 2016
<a name="supportmatrix"> </a>

The following table summarizes the support levels of typically used web browsers.
  
|**Browser**|**Supported**|**Not supported**|
|:-----|:-----|:-----|
|Microsoft Edge  <br/> |X  <br/> ||
|Internet Explorer 11  <br/> |X  <br/> ||
|Internet Explorer 10  <br/> |X  <br/> ||
|Internet Explorer 9  <br/> ||X  <br/> |
|Internet Explorer 8  <br/> ||X  <br/> |
|Internet Explorer 7  <br/> ||X  <br/> |
|Internet Explorer 6  <br/> ||X  <br/> |
|Google Chrome (latest released version)  <br/> |X  <br/> ||
|Mozilla Firefox (latest released version plus immediate previous version)  <br/> |X  <br/> ||
|Apple Safari (latest released version)  <br/> |X  <br/> ||

### Browser support levels in SharePoint Server 2019
<a name="supportmatrix2019"> </a>

The following table summarizes the support levels of typically used web browsers.
  
|**Browser**|**Supported**|**Not supported**|
|:-----|:-----|:-----|
|Microsoft Edge  <br/> |X  <br/> ||
|Internet Explorer 11  <br/> |X  <br/> ||
|Internet Explorer 10  <br/> ||X  <br/> ||
|Internet Explorer 9  <br/> ||X  <br/> |
|Internet Explorer 8  <br/> ||X  <br/> |
|Internet Explorer 7  <br/> ||X  <br/> |
|Internet Explorer 6  <br/> ||X  <br/> |
|Google Chrome (latest released version)  <br/> |X  <br/> ||
|Mozilla Firefox (latest released version plus immediate previous version)  <br/> |X  <br/> ||
|Apple Safari (latest released version)  <br/> |X  <br/> ||
   
### Browser details
<a name="browserdetail"> </a>

Review the details of the web browser that you have or plan to use in your organization to make sure that the web browser works with SharePoint Server 2016 and according to your business needs.
  

 **Internet Explorer and older functionality**
  
> [!NOTE]
> Some older SharePoint functionality that relies on NPAPI or ActiveX will not work on browsers other than Internet Explorer. You can work around each of these issues by using Internet Explorer to perform these tasks. 
  
   
#### Using ActiveX controls in SharePoint Server
<a name="activex"> </a>

Some functionality in SharePoint Server requires ActiveX controls. This produces limitations on browsers which do not support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. In SharePoint Server 2016, all other supported browsers, including Microsoft Edge and the Immersive mode of Internet Explorer 10 have the following limitations. 

For SharePoint Server 2016 and 2019, browsers other than Internet Explorer 11 have the following limitations.
  
||||||
|:-----|:-----|:-----|:-----|:-----|
|**Plugin name** <br/> |**DLL file name** <br/> |**What it does** <br/> | |**Known limitations** <br/> |
|Digital Signature  <br/> |Dsigctrl.dll, dsigres.dll  <br/> | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Make sure that the following conditions exist:  <br/>  Forms that are signed on the client can be verified on the server.  <br/>  Forms that are signed on the server can be verified on the client.  <br/> | <br/> |An inability to verify a form produces an error that states that the form cannot be signed.  <br/> |
|NameCtrl  <br/> |Name.dll  <br/> |Enables a webpage to display a contact card and presence status for people. Integrates through client-side APIs with Office client and Skype for Business client.  <br/> | ||
|TaskLauncher  <br/> |Nameext.dll  <br/> |Used to export items in a task list to Project Server if Project client is installed on the client computer.  <br/> | |If software requirements are not met, an error message states that you need to install Project client.  <br/> |
|SpreadSheetLauncher  <br/> |Owssupp.dll  <br/> |Used to verify whether Excel is installed for Export to Excel feature.  <br/> | |If Excel is not installed, the user may be prompted to download the file "query.iqy" which can then be opened in Excel.  <br/> |
|StssyncHandler  <br/> |Owssupp.dll  <br/> |Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook. Non-IE clients may have an additional prompt to open the calendar in Outlook.  <br/> |||
|ExportDatabase  <br/> |Owssupp.dll  <br/> |Enables a user to use an application such as Access to create or open a database that contains SharePoint list data.  <br/> | |To export a list, the client computer must have a SharePoint compatible application.  <br/> |
|OpenDocuments  <br/> |Owssupp.dll  <br/> |Starts Office client applications so that a user can create a or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write.  <br/> | |If a compatible Office application or browser is not installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser.  <br/> |
|CopyCtl  <br/> |Stsupld.dll  <br/> |Enables a user to copy a document on a SharePoint site to one or more locations on a server.  <br/> | |In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog box is not displayed.  <br/> |
|PPActiveX  <br/> |PPSLAX.dll  <br/> |Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library.  <br/> | |Does not work on Click-to-Run installations of Office and version of Office that run on Windows for ARM.  <br/> |
|BCSLauncher  <br/> |BCSLaunch.dll  <br/> |Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server.  <br/> | ||

Other functionality, such as **Form settings** in **List settings** only function with Internet Explorer.
   
## Mobile browser support
<a name="mobile"> </a>

SharePoint Server 2016 supports the following versions:
  
- Internet Explorer and Microsoft Edge on Windows Phone 8.1 or later.
    
- Latest version of Chrome on Android 4.4 or later.
    
- Latest versions of Safari and Chrome on iOS 8 or later.

- For SharePoint Server 2019, Chrome or Safari on iOS10 or later
    

