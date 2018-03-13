---
title: "Plan browser support in SharePoint Server 2016"
ms.author: kirks
author: Techwriter40
manager: pamgreen
ms.date: 2/23/2017
ms.audience: ITPro
ms.topic: interactive-tutorial
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: ff6c5b8c-59bd-4079-8f0b-de4f8b4e0a86
description: "Summary: Learn about how SharePoint Server 2016 supports Internet Explorer, Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge."
---

# Plan browser support in SharePoint Server 2016

 **Summary:** Learn about how SharePoint Server 2016 supports Internet Explorer, Google Chrome, Mozilla Firefox, Apple Safari, and Microsoft Edge. 
  
SharePoint Server 2016 supports several commonly used web browsers, such as ![Internet Explorer browser logo](../media/internetexplorersmall.png) Internet Explorer, ![Google Chrome browser logo](../media/chrome-small.jpg) Google Chrome, ![Mozilla Firefox browser logo](../media/firefox_small.png) Mozilla Firefox, ![Apple Safari browser logo](../media/safari-small.png) Apple Safari, and Microsoft Edge. However, certain web browsers can cause some SharePoint Server 2016 functionality to be downgraded, limited, or available only through alternative steps. 
  
As you plan your deployment of SharePoint Server 2016, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint Server 2016.
  
In this article:
  
- [Key planning phase of browser support](#section2)
    
- [Browser support levels in SharePoint Server 2016](#supportmatrix)
    
- [Browser details](#browserdetail)
    
- [Using ActiveX controls in Sharepoint Server 2016](#activex)
    
- [Mobile browser support](#mobile)
    
## Key planning phase of browser support
<a name="section2"> </a>

Browser support is an important part of your SharePoint Server 2016 implementation. Before you install SharePoint Server 2016, make sure that you know the browsers that SharePoint Server 2016 supports. The information in this article describes browser support in the following sections:
  
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
   
### Browser details
<a name="browserdetail"> </a>

Review the details of the web browser that you have or plan to use in your organization to make sure that the web browser works with SharePoint Server 2016 and according to your business needs.
  
#### Supported Internet Explorer versions

The product group makes every effort to test that SharePoint functionality works correctly with released versions of Internet Explorer and Microsoft Edge. Customers who want a more thoroughly tested browser interaction experience should strongly consider Internet Explorer. 
  
 **Internet Explorer 11, Internet Explorer 10, Microsoft Edge**
  
> [!NOTE]
> Microsoft Edge doesn't currently support some operations, like drag-and-drop editing, but it will do so in the near future. Also note that other SharePoint functionality that relies on NPAPI or ActiveX will not work on Microsoft Edge. > You can work around each of these issues by using Internet Explorer to perform these tasks. 
  
#### Other supported browsers in SharePoint Server 2016

- Google Chrome (latest released version) 
    
- Mozilla Firefox (latest released version plus immediate previous version)
    
    For example, if the latest released version is 40, version 39 would be supported.
    
- Apple Safari (latest released version)
    
#### Using ActiveX controls in Sharepoint Server 2016
<a name="activex"> </a>

Some functionality in SharePoint Server 2016 requires ActiveX controls. This produces limitations on browsers which do not support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. All other supported browsers, including Microsoft Edge and the Immersive mode of Internet Explorer 10 have the following limitations.
  
||||||
|:-----|:-----|:-----|:-----|:-----|
|**Plugin name** <br/> |**DLL file name** <br/> |**What it does** <br/> |**Supported browser version** <br/> |**Known limitations** <br/> |
|Digital Signature  <br/> |Dsigctrl.dll, dsigres.dll  <br/> | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Make sure that the following conditions exist:  <br/>  Forms that are signed on the client can be verified on the server.  <br/>  Forms that are signed on the server can be verified on the client.  <br/> |Internet Explorer 10  <br/> |An inability to verify a form produces an error that states that the form cannot be signed.  <br/> |
|NameCtrl  <br/> |Name.dll  <br/> |Enables a webpage to display a contact card and presence status for people. Integrates through client-side APIs with Office 2016.  <br/> |Supported in Internet Explorer 10.  <br/> Internet Explorer version 10 immersive mode is not supported.  <br/> ||
|TaskLauncher  <br/> |Nameext.dll  <br/> |Used to export items in a task list to Project Server if Project 2010 is installed on the client computer.  <br/> |All browsers  <br/> |If software requirements are not met, an error message states that you need to install Project Server.  <br/> |
|SpreadSheetLauncher  <br/> |Owssupp.dll  <br/> |Used to verify whether Excel is installed for Export to Excel feature.  <br/> |Internet Explorer 10  <br/> |If Excel is not installed, an error message states that a list cannot be imported because a compatible spreadsheet application is not installed or is not compatible with the browser.  <br/> |
|StssyncHandler  <br/> |Owssupp.dll  <br/> |Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook 2016.  <br/> |Internet Explorer 10  <br/> ||
|ExportDatabase  <br/> |Owssupp.dll  <br/> |Enables a user to use an application such as Access to create or open a database that contains SharePoint list data.  <br/> |Internet Explorer 10  <br/> |To export a list, the client computer must have a SharePoint compatible application.  <br/> |
|OpenDocuments  <br/> |Owssupp.dll  <br/> |Starts Office client applications so that a user can create a or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write.  <br/> |All except Internet Explorer version 10 in immersive mode.  <br/> |If a compatible Office application or browser is not installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser.  <br/> |
|CopyCtl  <br/> |Stsupld.dll  <br/> |Enables a user to copy a document on a SharePoint site to one or more locations on a server.  <br/> |Internet Explorer 10  <br/> |In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog box is not displayed.  <br/> |
|PPActiveX  <br/> |PPSLAX.dll  <br/> |Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library.  <br/> |Internet Explorer 10  <br/> |Does not work on Click-to-Run installations of Office and version of Office that run on Windows for ARM.  <br/> |
|BCSLauncher  <br/> |BCSLaunch.dll  <br/> |Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server.  <br/> |Internet Explorer 10  <br/> ||
   
## Mobile browser support
<a name="mobile"> </a>

SharePoint Server 2016 supports the following versions:
  
- Internet Explorer and Microsoft Edge on Windows Phone 8.1 or later.
    
- Latest version of Chrome on Android 4.4 or later.
    
- Latest versions of Safari and Chrome on iOS 8 or later.
    
## See also
<a name="mobile"> </a>

#### Other Resources

[Plan for SharePoint Server](http://technet.microsoft.com/library/0ed0b44c-d60d-4b85-87de-19065d968835%28Office.14%29.aspx)

