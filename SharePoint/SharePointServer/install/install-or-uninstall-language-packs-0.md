---
title: "Install or uninstall language packs for SharePoint Servers 2016 and 2019"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/24/2018
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SP2019
ms.assetid: 26c07867-0150-463d-b21a-a6d42aecf05a
description: "Learn how to download, install, and uninstall language packs for SharePoint Server."
---

# Install or uninstall language packs for SharePoint Servers 2016 and 2019

[!INCLUDE[appliesto-xxx-2016-2019-xxx-md](../includes/appliesto-xxx-2016-2019-xxx-md.md)] 
  
Language packs enable site owners and site collection administrators to create SharePoint sites and site collections in multiple languages without requiring separate installations of SharePoint Server. You install language packs, which contain language-specific site templates, on each SharePoint server in your farm. When an administrator creates a site or a site collection that is based on a language-specific site template, the text that appears on the site or the site collection is displayed in the site template's language. Language packs are typically used in multinational deployments where a single server farm supports users in different locations, or when sites and web pages must be duplicated in one or more languages.
  
Word breakers and stemmers enable you to search efficiently and effectively across content on SharePoint sites and site collections in multiple languages without requiring separate installations of SharePoint Server. Word breakers and stemmers are automatically installed on SharePoint servers by Setup. 
  
> [!IMPORTANT]
> If you are uninstalling SharePoint Server, you must uninstall all language packs before you uninstall SharePoint Server. 
  
    
## About language IDs and language packs
<a name="section1"> </a>

Site owners or site collection administrators who create sites or site collections can select a language for each site or site collection.
  
The language that they select has a language identifier (ID). The language ID determines the language that is used to display and interpret text that is on the site or site collection. For example, when a site owner creates a site in French, the site's toolbars, navigation bars, lists, and column headings appear in French. Similarly, if a site owner creates a site in Arabic, the site's toolbars, navigation bars, lists, and column headings appear in Arabic. In addition, the default left-to-right orientation of the site changes to a right-to-left orientation to correctly display Arabic text. 
  
The language packs that are installed on the SharePoint servers determine the list of available languages that you can use to create a site or site collection. By default, sites and site collections are created in the language in which SharePoint Server was installed. For example, if you install the Spanish version of SharePoint Server, the default language for sites, site collections, and web pages is Spanish. If someone has to create sites, site collections, or web pages in a language other than the default SharePoint Server language, you must install the language pack for that language on the SharePoint servers. For example, if you are running the French version of SharePoint Server, and a site owner wants to create sites in French, English, and Spanish, you must install the English and Spanish language packs on the SharePoint servers.
  
By default, when a site owner creates a new web page in a site, the site displays text in the language that is specified by the language ID.
  
Language packs are not bundled into multilingual installation packages. You must install a specific language pack for each language that you want to support. Also, language packs must be installed on each SharePoint server to make sure that each SharePoint server can display content in the specified language.
  
> [!IMPORTANT]
> You cannot change an existing site, site collection, or web page from one language to another by applying different language-specific site templates. After you use a language-specific site template for a site or a site collection, the site or site collection always displays content in the language of the original site template. For example, SharePoint can render the same site in multiple languages based on the preferred language of the user’s web browser.  But for this to work, the SharePoint language pack that matches the user’s preferred language must be installed on each server in the SharePoint farm.
  
Although a site owner specifies a language ID for a site, some user interface elements such as error messages, notifications, and dialog boxes do not display in the language that was specified. This is because SharePoint Server relies on several supporting technologies — for example, the Microsoft .NET Framework, Microsoft Windows Workflow Foundation, Microsoft ASP.NET, and SQL Server — some of which are localized into only a limited number of languages. If a user interface element is generated by any of the supporting technologies that are not localized into the language that the site owner specified for the site, the user interface element appears in English. For example, if a site owner creates a site in Hebrew, and the .NET Framework component displays a notification message, the notification message will not display in Hebrew because the .NET Framework is not localized into Hebrew. This situation can occur when sites are created in any language except the following: Chinese, French, German, Italian, Japanese, Korean, and Spanish.
  
Each language pack that you install creates a folder at %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\LAYOUTS\Locale_ID that contains language-specific data. In each locale_ID folder, you must have only one HTML error file that contains the error information that is used when a file cannot be found. Anytime a file cannot be found for any site in that language, this file will be used. You can specify the file to use by setting the **FileNotFoundPage()** for each web application. 
  
In some cases, some text might originate from the original installation language, which can create a mixed-language experience. This kind of mixed-language experience is typically seen only by content creators or site owners and is not seen by site users.
  
## Downloading language packs
<a name="section2"> </a>

Follow these steps for each language that you want to support. If you decide to download more than one language, please be aware that a unique file that has a common name is downloaded for each language. Therefore, make sure that you download each language pack to a separate folder on the hard disk so that you do not overwrite a language pack of a different language.
  
> [!IMPORTANT]
> By default, the Microsoft PowerShell Help files are installed in English (en-us). To view these files in the same language as the operating system, install the language pack for the same language in which the operating system was installed. 
  
You can download language packs from the Microsoft Download Center for [SharePoint Server 2016](http://go.microsoft.com/fwlink/?LinkId=746633&amp;clcid=0x409) and [SharePoint Server 2019](https://www.microsoft.com/download/details.aspx?id=57463).
  
## Installing language packs on the SharePoint servers
<a name="section4"> </a>

Language packs are available as individual downloads (one download for each supported language). If you have a server farm environment and you are installing language packs to support multiple languages, you must install the language packs on each SharePoint server.
  
> [!IMPORTANT]
> The language pack is installed in its native language. The procedure that follows is for the English language pack. 
  
 **To install a language pack**
  
 Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
1. In the folder where you downloaded the language pack, run serverlanguagepack.exe.
    
2. On the **Read the Microsoft Software License Terms** page, review the terms, select the **I accept the terms of this agreement** check box, and then click **Continue**.
    
3. The Setup wizard runs and installs the language pack.
    
4. Rerun the SharePoint Products Configuration Wizard by using the default settings. If you do not run the SharePoint Products Configuration Wizard after you install a language pack, the language pack will not be installed correctly.
    
    The SharePoint Products Configuration Wizard runs in the language of the base installation of SharePoint Server, not in the language of the language pack that you just installed.
    
 **To rerun the SharePoint Products Configuration Wizard**
  
Verify that the user account that is performing this procedure is the Setup user account. For information about the Setup user account, see [Initial deployment administrative and service accounts in SharePoint Server](initial-deployment-administrative-and-service-accounts-in-sharepoint-server.md).
    
1. Click **Start**, point to **Microsoft SharePoint 2019 Products** folder, click **SharePoint Products Configuration Wizard**.
    
2. On the **Welcome to SharePoint Products** page, click **Next**.
    
3. Click **Yes** in the dialog box that alerts you that some services might have to be restarted during configuration. 
    
4. On the **Modify Server Farm Settings** page, click **Do not disconnect from this server farm**, and then click **Next**.
    
5. If the **Modify SharePoint Central Administration Web Administration Settings** page appears, do not change any of the default settings, and then click **Next**.
    
6. After you complete the Completing the **SharePoint Products Configuration Wizard**, click **Next**.
    
7. On the **Configuration Successful** page, click **Finish**.
    
8. After you install a new language pack and rerun the **SharePoint Products Configuration Wizard**, you must deactivate and then reactivate any language-specific features before you use the new language pack.
    
When you install language packs, the language-specific site templates are installed in the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\ _LanguageID_ directory, where  _LanguageID_ is the Language ID number for the language that you are installing. For example, the United States English language pack installs to the %COMMONPROGRAMFILES%\Microsoft Shared\Web Server Extensions\16\TEMPLATE\1033 directory. After you install a language pack, site owners and site collection administrators can create sites and site collections based on the language-specific site templates by specifying a language when they are creating a new SharePoint site or site collection. 
  
## Uninstalling language packs
<a name="section5"> </a>

If you no longer have to support a language for which you have installed a language pack, you can remove the language pack by using the Control Panel. Removing a language pack removes the language-specific site templates from the computer. All sites that were created that have those language-specific site templates will no longer work (the URL will produce a HTTP 500 - Internal server error page). Reinstalling the language pack will make the site functional again.
  
You cannot remove the language pack for the version of SharePoint Server that you have installed on the server. For example, if you are running the Japanese version of SharePoint Server, you cannot uninstall the Japanese language support for SharePoint Server.

## List of Languages

Each folder name has a language tag appended to it, in the form ll-cc. That tag identifies the language and culture. For example, U.S. English language folders are identified by the folder name extension en-us. 

Folders for the language-specific components are identified by the language tag that is shown in the table. The Windows operating system uses locale identifiers (LCIDs) to identify languages in the Windows registry.

SharePoint Servers 2016 and 2019 support the following languages:

|**Language**|**Language tag**|**LCID**
|:-----|:-----|:-----|:-----
Arabic <br/>|ar-sa  <br/> | 1025 <br/>
Azerbaijani <br/> |az-latn-az  <br/> |1068 <br/>
Basque <br/> |eu-es  <br/> |1069 <br/>||
Bosnian (Latin) <br/> |bs-latn-ba  <br/> |5146 <br/>
Bulgarian <br/> |bg-bg  <br/> |1026 <br/>||
Catalan <br/> |ca-es <br/> |1027 <br/>||
Chinese (Simplified) <br/> |zh-cn  <br/> |2052 <br/>
Chinese (Traditional) <br/> |zh-tw  <br/> |1028 <br/>||
Croatian <br/> |hr-hr  <br/> |1050 <br/>||
Czech <br/> |cs-cz  <br/> |1029 <br/>||
Danish <br/> |da-dk  <br/> |1026 <br/>||
Dari <br/> |prs-af  <br/> |1164 <br/>||
Dutch <br/> |nl-nl  <br/> |1043 <br/>||
English <br/> |en-us  <br/> |1033 <br/>||
Estonian <br/> |et-ee  <br/> |1061 <br/>||
Finnish <br/> |fi-fi  <br/> |1035 <br/>||
French <br/> |fr-fr  <br/> |1036 <br/>
Galician <br/> |gl-es  <br/> |1110 <br/>||
German <br/> |de-de  <br/> |1031 <br/>||
Greek <br/> |el-el  <br/> |1032 <br/>||
Hebrew <br/> |he-il  <br/> |1037 <br/>||
Hindi <br/> |hi-in  <br/> |1081 <br/>||
Hungarian <br/> |hu-hu  <br/> |1038<br/>||
Indonesian <br/> |id-id  <br/> |1057 <br/>||
Irish <br/> |ga-ie  <br/> |2108 <br/>||
Italian <br/> |it-it  <br/> |1040 <br/>||
Japanese <br/> |ja-jp  <br/> |1041 <br/>||
Kazakh <br/> |kk-kz  <br/> |1087 <br/>||
Korean <br/> |ko-kr  <br/> |1042 <br/>||
Latvian <br/> |lv-lv  <br/> |1062 <br/>
Lithuanian <br/> |lt-lt  <br/> |1063 <br/>||
Macedonian (FYROM) <br/> |mk-mk  <br/> |1071 <br/>||
Malay (Malaysia) <br/> |ms-my  <br/> |1086 <br/>||
Norwegian (Bokmål) <br/> |nb-no  <br/> |1044 <br/>||
Polish <br/> |pl-pl  <br/> |1045 <br/>
Portuguese (Brazil) <br/> |pt-br  <br/> |1046 <br/>||
Portuguese (Portugal) <br/> |pt-pt  <br/> |2070<br/>||
Romanian <br/> |ro-ro  <br/> |1048 <br/>||
Russian <br/> |ru-ru  <br/> |1049 <br/>||
Serbian (Cyrillic) <br/> |sr-cyrl-rs  <br/> |10266 <br/>||
Serbian (Latin) <br/> |sr-latn-rs  <br/> |9242 <br/>||
Slovak <br/> |sk-sk  <br/> |1051 <br/>||
Slovenian <br/> |sl-si  <br/> |1060 <br/>||
Spanish <br/> |es-es  <br/> |3082 <br/>||
Swedish <br/> |sv-se  <br/> |1053 <br/>||
Thai <br/> |th-th  <br/> |1054 <br/>||
Turkish <br/> |tr-tr  <br/> |1055 <br/>||
Ukrainian <br/> |uk-ua <br/> |1058<br/>||
Vietnamese <br/> |vi-vn  <br/> |1066 <br/>||
Welsh <br/> |cy-gb  <br/> |1106 <br/>||

