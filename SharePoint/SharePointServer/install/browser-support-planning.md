---
title: "Plan browser support in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/18/2017
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e09599f5-f900-48b3-9680-af1f1de3f65a
description: "Learn about how SharePoint supports Internet Explorer, Google Chrome, Mozilla Firefox, and Apple Safari."
---

# Plan browser support in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]. 
  
SharePoint 2013 supports several commonly used web browsers, such as ![Internet Explorer browser logo](../media/internetexplorersmall.png) Internet Explorer, ![Google Chrome browser logo](../media/chrome-small.jpg) Google Chrome, ![Mozilla Firefox browser logo](../media/firefox_small.png) Mozilla Firefox, and ![Apple Safari browser logo](../media/safari-small.png) Apple Safari. However, certain web browsers could cause some SharePoint 2013 functionality to be downgraded, limited, or available only through alternative steps. 
  
As you plan your deployment of SharePoint 2013, we recommend that you review the browsers used in your organization to guarantee optimal performance with SharePoint 2013.
  
    
## Key planning phase of browser support
<a name="section2"> </a>

Browser support is an important part of your SharePoint 2013 implementation. Before you install SharePoint 2013, make sure that you know the browsers that SharePoint 2013 supports. The information in this article describes browser support in the following sections:
  
- Browser support matrix
    
- Browser details
    
### Browser support matrix
<a name="supportmatrix"> </a>

The following table summarizes the support levels of typically used web browsers.
  
|**Browser**|**Supported**|**Not supported**|
|:-----|:-----|:-----|
|Microsoft Edge  <br/> |X  <br/> ||
|Internet Explorer 11  <br/> |X  <br/> ||
||||
|Internet Explorer 10  <br/> |X  <br/> ||
|Internet Explorer 9  <br/> |X  <br/> ||
|Internet Explorer 8  <br/> |X  <br/> ||
|Internet Explorer 7  <br/> ||X  <br/> |
|Internet Explorer 6  <br/> ||X  <br/> |
|Google Chrome (latest released version)  <br/> |X  <br/> ||
|Mozilla Firefox (latest released version)  <br/> |X  <br/> ||
|Apple Safari (latest released version)  <br/> |X  <br/> ||
   
### Browser details
<a name="browserdetail"> </a>

Review the details of the web browser that you have or plan to use in your organization to make sure that the web browser works with SharePoint 2013 and according to your business needs.
  
#### Supported Internet Explorer versions

The product group makes every effort to validate that SharePoint functionality works correctly with released versions of Internet Explorer. Customers who want a more deeply validated browser interaction experience should strongly consider Internet Explorer.
  
 **Microsoft Edge, Internet Explorer 11, Internet Explorer 10, Internet Explorer 9, Internet Explorer 8**
  
> [!NOTE]
> Internet Explorer 11  *edge mode*  is not supported. Add sites to the **Compatibility View** list to make some features work. 
  
> [!NOTE]
> Microsoft Edge is supported with the SharePoint Server 2013 December 2015 CU. For additional information about the December 2015 CU, see [December 8, 2015, update for SharePoint Foundation 2013 (KB3114352)](https://support.microsoft.com/en-us/kb/3114352)
  
#### Other supported browsers

- **Google Chrome (latest released version)**
    
- **Mozilla Firefox (latest released version plus immediate previous version)**
    
    For example, if the latest released version is 10, then version 9 would be supported.
    
- **Apple Safari (latest released version)**
    
#### ActiveX controls
<a name="activex"> </a>

Some functionality in SharePoint 2013 requires ActiveX controls. This produces limitations on browsers which do not support ActiveX. Currently only 32-bit versions of Internet Explorer support this functionality. All other browsers have the following limitations.
  
> [!NOTE]
> Internet Explorer 10 does not support Active X controls when in immersive mode. The functionality for the controls listed below should only be expected to work in desktop mode. 
  
||||||
|:-----|:-----|:-----|:-----|:-----|
|**Plugin name** <br/> |**DLL Filename** <br/> |**What it does** <br/> |**Supported browser version** <br/> |**Known limitations** <br/> |
|Digital Signature  <br/> |Dsigctrl.dll, dsigres.dll  <br/> | Digital signing takes place in both the InfoPath client and on the InfoPath Forms Services server. Make sure that the following conditions exist:  <br/>  Forms that are signed on the client can be verified on the server.  <br/>  Forms that are signed on the server can be verified on the client.  <br/> |Internet Explorer versions 8, 9 and 10  <br/> |An inability to verify a form produces an error that states that the form cannot be signed.  <br/> |
|NameCtrl  <br/> |Name.dll  <br/> |Enables a web page to display a contact card and presence status for people. Integrates through client-side APIs with Office 2016.  <br/> |Supported in Internet Explorer versions 8, 9, and 10.  <br/> Firefox, Google Chrome are also supported by using a plug-in.  <br/> Internet Explorer version 10 immersive mode is not supported.  <br/> ||
|TaskLauncher  <br/> |Nameext.dll  <br/> |Used to export items in a task list to Project Server if Project 2010 is installed on the client computer.  <br/> |All browsers  <br/> |If software requirements are not met, an error message states that you need to install Project Server.  <br/> |
|SpreadSheetLauncher  <br/> |Owssupp.dll  <br/> |Used to verify whether Excel is installed for Export to Excel feature.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> |If Excel is not installed, an error message states that a list cannot be imported because a compatible spreadsheet application is not installed or is not compatible with the browser.  <br/> |
|StssyncHandler  <br/> |Owssupp.dll  <br/> |Enables synchronization of lists of events and lists of contacts in SharePoint with a messaging application such as Outlook 2016.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> ||
|ExportDatabase  <br/> |Owssupp.dll  <br/> |Enables a user to use an application such as Access to create or open a database that contains SharePoint list data.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> |To export a list, the client computer must have a SharePoint compatible application.  <br/> |
|OpenDocuments  <br/> |Owssupp.dll  <br/> |Starts Office client applications so that a user can create a document or edit a document. Enables users to create documents that are based on a specified template, open documents as read-only, or open documents as read/write.  <br/> |All except Internet Explorer version 10 in immersive mode.  <br/> |If a compatible Office application or browser is not installed on a client, an error message states that the feature requires a SharePoint compatible application and web browser.  <br/> |
|UploadCtl  <br/> |Stsupld.dll  <br/> |Enables drag-and-drop in SharePoint 2013 visual mode "upload multiple files" dialog box.  <br/> |Internet Explorer versions 8 and 9.  <br/> ||
|CopyCtl  <br/> |Stsupld.dll  <br/> |Enables a user to copy a document on a SharePoint site to one or more locations on a server.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> |In Firefox, Google Chrome, and immersive mode of Internet Explorer version 10, the copy progress dialog box is not displayed.  <br/> |
|PPActiveX  <br/> |PPSLAX.dll  <br/> |Starts PowerPoint to open presentations from a slide library or publish individual slides to a slide library.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> |Does not work on Click-to-Run installations of Office and version of Office that run on Windows for ARM.  <br/> |
|BCSLauncher  <br/> |BCSLaunch.dll  <br/> |Starts the Visual Studio Tools for Office installer to install a Visual Studio Tools for Office package that has been generated on the server.  <br/> |Internet Explorer versions 8, 9, and 10  <br/> ||
   
## Mobile browser support
<a name="mobile"> </a>

To learn about the different mobile device browsers supported, see [Mobile device browsers supported in SharePoint 2013](../administration/supported-mobile-device-browsers.md)
  
## See also
<a name="mobile"> </a>

#### Other Resources

[Plan for SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc261834(v=office.14))

