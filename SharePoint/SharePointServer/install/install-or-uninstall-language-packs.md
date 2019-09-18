---
title: "Install or uninstall language packs for SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/27/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: b1926e3b-5263-46e0-ac35-433236dae704
description: "Learn how to download, install, and uninstall language packs for SharePoint."
---

# Install or uninstall language packs for SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
Language packs enable site owners and site collection administrators to create SharePoint sites and site collections in multiple languages without requiring separate installations of SharePoint 2013. You install language packs, which contain language-specific site templates, on web and application servers. When an administrator creates a site or a site collection that is based on a language-specific site template, the text that appears on the site or the site collection is displayed in the site template's language. Language packs are typically used in multinational deployments where a single server farm supports users in different locations, or when sites and web pages must be duplicated in one or more languages.
  
If users are accessing Project Server 2016 in the SharePoint farm and have to view their project data in another language, they will also have to install a corresponding Project Server 2016 language pack. For more information about Project Server 2016 language packs, see [Deploy language packs in Project Server 2013](/project/deploy-language-packs-in-project-server-2013)
  
Word breakers and stemmers enable you to search efficiently and effectively across content on SharePoint sites and site collections in multiple languages without requiring separate installations of SharePoint 2013. Word breakers and stemmers are automatically installed on web and application servers by Setup. 
  
> [!IMPORTANT]
> If you are uninstalling SharePoint 2013, you must uninstall all language packs before you uninstall SharePoint 2013. 
  
    
## About language IDs and language packs
<a name="section1"> </a>

Site owners or site collection administrators who create sites or site collections can select a language for each site or site collection.
  
The language that they select has a language identifier (ID). The language ID determines the language that is used to display and interpret text that is on the site or site collection. For example, when a site owner creates a site in French, the site's toolbars, navigation bars, lists, and column headings appear in French. Similarly, if a site owner creates a site in Arabic, the site's toolbars, navigation bars, lists, and column headings appear in Arabic. In addition, the default left-to-right orientation of the site changes to a right-to-left orientation to correctly display Arabic text. 
  
The language packs that are installed on the web and application servers determine the list of available languages that you can use to create a site or site collection. By default, sites and site collections are created in the language in which SharePoint 2013 was installed. For example, if you install the Spanish version of SharePoint 2013, the default language for sites, site collections, and web pages is Spanish. If someone has to create sites, site collections, or web pages in a language other than the default SharePoint 2013 language, you must install the language pack for that language on the web and application servers. For example, if you are running the French version of SharePoint 2013, and a site owner wants to create sites in French, English, and Spanish, you must install the English and Spanish language packs on the web and application servers.
  
By default, when a site owner creates a new web page in a site, the site displays text in the language that is specified by the language ID.
  
Language packs are not bundled into multilingual installation packages. You must install a specific language pack for each language that you want to support. Also, language packs must be installed on each web and application server to make sure that each web and application server can display content in the specified language.
  
> [!IMPORTANT]
> You cannot change an existing site, site collection, or web page from one language to another by applying different language-specific site templates. After you use a language-specific site template for a site or a site collection, the site or site collection always displays content in the language of the original site template. 
  
Only a limited set of language packs are available for SharePoint 2013.
  
Although a site owner specifies a language ID for a site, some user interface elements such as error messages, notifications, and dialog boxes do not display in the language that was specified. This is because SharePoint 2013 relies on several supporting technologies — for example, the Microsoft .NET Framework, Microsoft Windows Workflow Foundation, Microsoft ASP.NET, and SQL Server — some of which are localized into only a limited number of languages. If a user interface element is generated by any of the supporting technologies that are not localized into the language that the site owner specified for the site, the user interface element appears in English. For example, if a site owner creates a site in Hebrew, and the .NET Framework component displays a notification message, the notification message will not display in Hebrew because the .NET Framework is not localized into Hebrew. This situation can occur when sites are created in any language except the following: Chinese, French, German, Italian, Japanese, Korean, and Spanish.
  
Each language pack that you install creates a folder at %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\15\LAYOUTS\Locale_ID that contains language-specific data. In each locale_ID folder, you must have only one HTML error file that contains the error information that is used when a file cannot be found. Anytime a file cannot be found for any site in that language, this file will be used. You can specify the file to use by setting the **FileNotFoundPage()** for each web application. 
  
In some cases, some text might originate from the original installation language, which can create a mixed-language experience. This kind of mixed-language experience is typically seen only by content creators or site owners and is not seen by site users.
  
## Downloading language packs
<a name="section2"> </a>

Follow these steps for each language that you want to support. If you decide to download more than one language, please be aware that a unique file that has a common name is downloaded for each language. Therefore, make sure that you download each language pack to a separate folder on the hard disk so that you do not overwrite a language pack of a different language.
  
> [!IMPORTANT]
> By default, the Microsoft PowerShell Help files are installed in English (en-us). To view these files in the same language as the operating system, install the language pack for the same language in which the operating system was installed. 
  
You can download language packs from the same location where you downloaded SharePoint 2013.
  
## Installing language packs on the web and application servers
<a name="section4"> </a>

After you install the necessary language files on the web and application servers, you can install the language packs. Language packs are available as individual downloads (one download for each supported language). If you have a server farm environment and you are installing language packs to support multiple languages, you must install the language packs on each web and application server. 
  
> [!IMPORTANT]
> The language pack is installed in its native language. The procedure that follows is for the English language pack. 
  
 **To install a language pack**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. In the folder where you downloaded the language pack, run setup.exe.
    
3. On the Read the Microsoft Software License Terms page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.
    
4. The Setup wizard runs and installs the language pack.
    
5. Rerun the SharePoint Products Configuration Wizard by using the default settings. If you do not run the SharePoint Products Configuration Wizard after you install a language pack, the language pack will not be installed correctly.
    
    The SharePoint Products Configuration Wizard runs in the language of the base installation of SharePoint 2013, not in the language of the language pack that you just installed.
    
 **To rerun the SharePoint 2013 Configuration Wizard**
  
1. Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
2. Click **Start**, point to **All Programs**, click **SharePoint 2013**, and then click **SharePoint 2013 Products Configuration Wizard**.
    
3. On the **Welcome to SharePoint Products** page, click **Next**.
    
4. Click **Yes** in the dialog box that alerts you that some services might have to be restarted during configuration. 
    
5. On the **Modify Server Farm Settings** page, click **Do not disconnect from this server farm**, and then click **Next**.
    
6. If the **Modify SharePoint Central Administration Web Administration Settings** page appears, do not change any of the default settings, and then click **Next**.
    
7. After you complete the Completing the SharePoint Products and Technologies Configuration Wizard, click **Next**.
    
8. On the **Configuration Successful** page, click **Finish**.
    
9. After you install a new language pack and rerun the Rerun the SharePoint 2013 Configuration Wizard, you must deactivate and then reactivate any language-specific features before you use the new language pack.
    
When you install language packs, the language-specific site templates are installed in the %COMMONPROGRAMFILES%\Microsoft Shared\Web server extensions\15\TEMPLATE\ _LanguageID_ directory, where  _LanguageID_ is the Language ID number for the language that you are installing. For example, the United States English language pack installs to the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\15\TEMPLATE\1033 directory. After you install a language pack, site owners and site collection administrators can create sites and site collections based on the language-specific site templates by specifying a language when they are creating a new SharePoint site or site collection. 
  
## Uninstalling language packs
<a name="section5"> </a>

If you no longer have to support a language for which you have installed a language pack, you can remove the language pack by using the Control Panel. Removing a language pack removes the language-specific site templates from the computer. All sites that were created that have those language-specific site templates will no longer work (It could cause many issues that is, the URL will produce a HTTP 500 - Internal server error page, broken layout, mixture of default, and uninstalled language.). Reinstalling the language pack will make the site functional again.
  
You cannot remove the language pack for the version of SharePoint 2013 that you have installed on the server. For example, if you are running the Japanese version of SharePoint 2013, you cannot uninstall the Japanese language support for SharePoint 2013.
  

