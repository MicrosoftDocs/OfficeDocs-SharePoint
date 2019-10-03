---
title: "Plan for multilingual sites in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 22d5dc9c-66bd-40d7-8c60-2a2a066db224
description: "Learn how to plan for multilingual sites in SharePoint Server and SharePoint Online."
---

# Plan for multilingual sites in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
SharePoint Server and SharePoint Online have features that enable you to support users in different regions or users who speak different languages. You can use these features to create websites in different languages, or to enable users to view sites in their preferred language.
  
For information about how to create multilingual sites, see [Choose the languages you want to make available for a site's user interface](https://go.microsoft.com/fwlink/p/?LinkId=307131) and [Create a multi-language website](https://go.microsoft.com/fwlink/p/?LinkId=307132). 
  
> [!IMPORTANT]
> This section does not apply to SharePoint Foundation 2013. 
  
## About SharePoint multilingual sites
<a name="BKMK_About"> </a>

The SharePoint Server multilingual sites feature enables you to work in multiple languages, to provide content to users in more than one language, or both. The multilingual sites feature, offers the following:
  
- Create, manage, and read content in different languages.
    
- Navigate a site in a preferred language.
    
- Collaborate with people in different regions, in different languages, in the same application.
    
- Manage personal sites by using a preferred language.
    
- Search and browse content across a company by using a preferred language.
    
There are three ways that you can provide multilingual sites for users:
  
1. **You can create sites in languages different from the one that was used to install SharePoint.**
    
    This option creates a site in which the site user interface appears in the language that is selected when the site is created. For example, if the English version of SharePoint is installed, but Japanese is selected when the site is created, the site user interface will appear in Japanese. This option only affects the site administration pages and user interface, and does not affect content created on the site. For more information, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) or [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md).
    
2. **You can use the multilingual user interface to enable users to view the site user interface in their preferred language.**
    
    This option creates a site in one language, but can show the site user interface in another language, based on the preferred language of the user. For example, if the site is created in English, but the user's preferred language is Spanish, and the Spanish language pack is installed and enabled for the site, the site user interface for that user appears in Spanish. This option only affects the site administration pages and user interface, and does not affect content created on the site. For information about the multilingual user interface, see [Plan for the multilingual user interface in SharePoint Server](plan-for-the-multilingual-user-interface.md).
    
3. **You can use the variations feature to make publishing content available in different languages on different sites.**
    
    > [!NOTE]
    > You can only use the variations feature on sites that you create with one of the Publishing site templates, or on a site where the SharePoint Server Publishing Infrastructure feature is activated. 
  
    This option creates a source variation site that is used to author content in one language, and then syncs that content to one or more target variation sites where it can be translated and consumed in other languages. For example, you can author and publish content in English for http<!-- nolink -->://contoso.com/en, and use variations to sync content to http<!-- nolink -->://contoso.com/fr, where you can translate it to French and publish it. Unlike the first two options, the variations feature does not affect site administration pages or the user interface; it affects only content. You can create the variation sites in different languages, and you can enable the multilingual user interface for users who create content for the variation sites. For information about variations, see [Variations overview in SharePoint Server](../administration/variations-overview.md).
    
> [!NOTE]
> Only options 1 and 2 require that language packs be installed. But if you want to create variation sites in other languages, or enable the multilingual user interface on variation sites, you must also install language packs for option 3. For information about language packs, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) or [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md). 
  
For information about how to decide whether to use multilingual user interface features, the variations feature, or both, see [Introduction to multilingual features](https://go.microsoft.com/fwlink/p/?LinkId=307134).
  
If your organization supports users in different regions or users who speak different languages, you must determine what your multilingual requirements are and plan for multilingual site deployment when you plan your overall site structure and navigation. To determine your multilingual requirements, you must do the following:
  
- Determine the languages and locales that you must support.
    
- Determine the language pack requirements for sites and users.
    
- Decide whether you want to use the variations feature.
    
> [!NOTE]
> Although Office SharePoint Server 2007 and Windows SharePoint Services 3.0 supported internationalized domain names (IDNs), SharePoint 2013, SharePoint Server 2016, and SharePoint Server 2019 don't. If you currently use IDNs with Office SharePoint Server 2007 or Windows SharePoint Services 3.0 and you plan to upgrade or migrate to either SharePoint 2013 or SharePoint Servers 2016 or 2019, you must stop using IDNs, delete any IDN settings, and set up a non-IDN environment before you upgrade or migrate to SharePoint Servers 2016 and 2019. 
  
## Determine language and locale requirements
<a name="BKMK_langreq"> </a>

The following reasons establish a need to create sites in multiple languages:
  
- You want to provide content to users in different regions or countries, and you want to provide content to each region or country in its specific language.
    
- You want to provide content to customers whose business spans many geographic areas.
    
- You are required by government regulation or organizational policy to provide content in more than one language.
    
Consult all potential site owners to determine your language requirements. Record the list of sites and the default language for each site in a spreadsheet. Be sure to list all languages that you might have to support in the future. It is easier to install language support during initial deployment instead of waiting to install language support when your servers are running in a full production environment. After a site is created for a specific language, the default language of the site cannot be changed. But a user who is logged on to the site can use the multilingual user interface to view the site in the user's preferred language. 
  
> [!NOTE]
> If users change their preferred language, some site elements, such as column names, might still appear in the default site language. 
  
Do not assume that you have to create a site collection or site in multiple languages only because a document library contains documents in multiple languages. A document library can contain documents in multiple languages without requiring you to create site collections or sites in multiple languages. For example, the document library for an English site collection can contain documents that are written in French, Spanish, and Japanese. For publishing sites, content can be created in any language. You do not have to create a site collection or site in a specific language to show pages that contain content in other languages.
  
When you plan multilingual sites, you should also consider which locales are necessary to support your sites. Locale is a regional setting that specifies the way numbers, dates, and times are shown on a site. But locale does not change the language in which the site is viewed. For example, selecting the **Thai** locale changes the default sort order of list items, and uses the Buddhist calendar instead of the default calendar. But it does not change the site user interface language to Thai. Locale is a setting that is configured independently of the language specified when a site is created. In your spreadsheet, record any locales that you want to use with specific languages. The site locale can be changed, but only until any of the lists on the site are indexed. 
  
## Determine language pack requirements
<a name="BKMK_langpack"> </a>

SharePoint language packs enable you to create site collections and sites in multiple languages without requiring separate installations of SharePoint Server. A farm administrator must install language packs on all web and application servers in the SharePoint farm before sites can be created in languages other than the default language. For more information, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) or [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md). When you create a site collection or a site and select a language, the user interface text that appears on the site collection or site is shown in the selected language. For example, when you create a site in French, the toolbars, navigation bars, lists, and column headings for that site appear in French. Likewise, if you create a site in Arabic, the site administration pages and user interface, such as toolbars, navigation bars, lists, and column headings for that site, appear in Arabic, and the default left-to-right orientation of the site changes to a right-to-left orientation to correctly show Arabic text.
  
If your site will have users who can't work in the default language that you plan to use for the site, you should install language packs that will enable users to work in their preferred language by using the multilingual user interface. If you do not provide support for additional languages, users might find it difficult to use site features in their non-native language. Language packs provide language-specific translation of user interface elements such as the following:
  
- Site administration pages
    
- Ribbon elements
    
- List and site column headers
    
- Site settings interface
    
- Templates for new lists, document libraries, and sites
    
- Managed metadata term sets and terms
    
For more information about what is supported by the multilingual user interface, see [Plan for the multilingual user interface in SharePoint Server](plan-for-the-multilingual-user-interface.md).
  
> [!NOTE]
> Language packs provide translation only of the user interface. They do not translate content that is created and shown in content pages or Web Parts. You can use the Machine Translation service to enable users to automatically translate documents. For more information, see [Turn on automated document translation in SharePoint Server](../administration/turn-on-automated-document-translation.md). 
  
The list of available languages that you can use to create a site collection or site, and which you can enable for the multilingual user interface, is generated by the language packs that are installed on the web and application servers of the server farm. By default, site collections and sites are created in the language in which SharePoint Server was installed. For example, if you install the Spanish version of SharePoint Server, the default language for site collections and sites is Spanish. If you must create site collections or sites in a language other than the default SharePoint Server language, you must first install the language pack for that other language on the web and application servers before you can select another language in which to create a site. For example, if you are running the French version of SharePoint Server and you want to create sites in French, English, and Spanish, you must install the English and Spanish language packs on the web and application servers before you can create the English and Spanish sites.
  
> [!NOTE]
> Every time that a language pack is installed, you must rerun the SharePoint Products Configuration Wizard, which stops and restarts Internet Information Services (IIS), the SharePoint Administration Service, and the SharePoint Timer Service. To minimize interruption of service to your users, you should plan to install all language packs before your sites go live. 
  
Based on the language requirements of your site collections or sites, determine the language packs that must be installed on every web and application server. In your spreadsheet, for each site, record the list of language packs that you want to make available as alternative languages. For information about which language packs are available, see [Language Packs for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57463), [Language Packs for SharePoint Server 2016](https://www.microsoft.com/en-us/download/details.aspx?id=51492) and [Language Packs for SharePoint Server 2013](https://www.microsoft.com/en-us/download/details.aspx?id=37140).
  
The following table lists when language packs are or are not required:
  
**Table: When language packs are required**

|**To do the following**|**Are language packs required?**|
|:-----|:-----|
|Create sites in different languages.  <br/> |Yes  <br/> |
|Enable the multilingual user interface on sites.  <br/> |Yes  <br/> |
|Use the variations feature to create multilingual content.  <br/> |No  <br/> |
|Create variation sites in different languages.  <br/> |Yes  <br/> |
|Enable the multilingual user interface on variation sites.  <br/> |Yes  <br/> |
   
Even though you specify a language for a site, some user interface elements such as error messages, notifications, or dialog boxes might not appear in the language that you choose. This is because SharePoint Server relies on several supporting technologies — such as the .NET Framework, Microsoft Windows Workflow Foundation, ASP.NET, and SQL Server — and some of these supporting technologies are localized into a limited number of languages. If a user interface element is generated by one of the supporting technologies, and if the supporting technology is not localized into the language that the site administrator specified for the site, the user interface element appears in English.
  
In addition, some text might originate from the original installation language, which can create a mixed-language experience. This type of mixed-language experience is typically seen only by content creators, site collection administrators, or site owners, and is not seen by site users.
  
> [!NOTE]
> Error logs that SharePoint Server stores on the server are always in English. 
  
For information about how to install language packs, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) and [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md).
  
## Decide whether to use site variations
<a name="BKMK_variations"> </a>

> [!NOTE]
> You can only use the variations feature on sites that you create with one of the Publishing site templates, or on a site where the SharePoint Server Publishing Infrastructure feature is activated. 
  
> [!NOTE]
> The variations feature is not available in SharePoint Foundation 2013. 
  
The SharePoint Server variations feature enables site owners to make the same content available to specific audiences across different sites by maintaining customizable copies of the content from the source variation site in each target variation site. For a multilingual site, you might want to use the primary language of your organization as the source variation site. You can create the target variation sites in the same language as the source variation site, or in the language the target variation site is intended to support. If you plan to create the target variation sites in other languages, verify that the corresponding language packs are installed. For more information about variations, see [Variations overview in SharePoint Server](../administration/variations-overview.md).
  
When you plan for multilingual sites, consider whether you have to create content that will be shared across sites, but must be changed to meet regional requirements or translated to meet language requirements. If you think there is a possibility that you might have to set up variations sites, you should plan for them beforehand. It is very difficult to integrate variations sites into a site collection after the site structure is implemented. The following factors can affect your ability to easily move to using variations sites later in the life of your site:
  
- **Custom code** Code that contains references to the location of the root variations site. 
    
- **Site customizations** Site navigation, Master Pages, and other customizations. 
    
- **Search** Search scopes must be created for each variation label, and the site properties of each variations site must be changed. 
    
If you plan to translate content on your variations sites, you must decide whether to use human translation or machine translation. If you plan to use machine translation, make sure that the language to which you want to translate content is available for the Machine Translation service. For more information about how to plan for variations, see [Plan for variations in SharePoint Server](../administration/plan-for-variations.md).
  
## See also
<a name="BKMK_variations"> </a>

#### Concepts

[Plan for the multilingual user interface in SharePoint Server](plan-for-the-multilingual-user-interface.md)
  
[Variations overview in SharePoint Server](../administration/variations-overview.md)

#### Other Resources

[Language Packs for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57463)

[Language Packs for SharePoint Server 2016](https://www.microsoft.com/en-us/download/details.aspx?id=51492)
  
[Language Packs for SharePoint Server 2013](https://www.microsoft.com/en-us/download/details.aspx?id=37140)
