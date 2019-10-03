---
title: "Plan for the multilingual user interface in SharePoint Server"
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
ms.assetid: ca5a0b10-4020-4f9e-8ecc-30e64c4b109f
description: "Learn about the multilingual user interface feature, how it works, and how to plan to use it in SharePoint Server and SharePoint Online."
---

# Plan for the multilingual user interface in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
The multilingual user interface (MUI) feature enables users to display the user interface of a SharePoint Server or SharePoint Online site in the language they prefer, instead of the default language that was selected when the site was created. This article describes the use and benefits of the MUI feature, explains how the feature works, and lists the other features and functionality that are supported by the feature. It also describes how to add and edit application content, and how to export and import content for translation. It explains how to use the MUI feature with managed metadata, and describes the limitations of the feature. Finally, this article describes how to plan for using the MUI feature in a SharePoint Server site solution.
  
For information about how to plan for multilingual sites, see [Plan for multilingual sites in SharePoint Server](plan-for-multilingual-sites.md).
  
    
## How the multilingual user interface works
<a name="MUIWorks"> </a>

By default, when a new site is created, it is created in the default language of the SharePoint Server installation on the server. A farm administrator must install language packs on all web and application servers in the SharePoint farm before sites can be created in languages other than the default language. For more information, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) and [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md).
  
After language packs are installed on the server, the **Language settings** link is added to the **Site Settings** page. Site collection administrators and site owners use the **Language Settings** page to specify which alternate languages the site will support. After the site collection administrator or site owner has enabled alternate languages for a site, the next time that a user logs on to the site, SharePoint Server uses one of the following rules to determine the language in which to display content to the user: 
  
1. If the User Profile service application is started on the SharePoint Server farm, the language preferences stored in the user profile are used. For information about how to add a list of languages to user profile settings in SharePoint Server, see [Add, edit, or delete custom properties in SharePoint Server user profiles](https://docs.microsoft.com/sharepoint/administration/add-edit-or-delete-custom-properties-for-a-user-profile). For information about how to add a list of languages to user profile settings in SharePoint Online Administration Center, see [Add and edit user profile properties](https://docs.microsoft.com/sharepoint/add-and-edit-user-profile-properties).
    
2. If no language preference is defined in the user profile, the language preferences stored in the user's language settings for the site collection are used.
    
3. If no language preference is defined in the user's site collection language settings, the language preferences stored in the user's web browser are used.
    
4. If no language preference is defined in the user's web browser, the default site language is used.
    
The MUI feature only displays site's user interface elements in a user's preferred language. It does not translate content or display content such as documents or list items in an alternate language. To translate webpage content, you use the variations feature in SharePoint Server or SharePoint Online.
  
SharePoint Server provides three methods that you can use to change certain application content, such as list or library titles and descriptions: by using the user interface, by exporting and importing translations for a site, and by using the **SPUserResource** class in the **Microsoft.SharePoint** namespace. Not all user interface elements can be changed directly in the user interface. For example, user actions and commands can be changed only by using the **SPUserResource** class. For more information, see [SPUserResource class](https://go.microsoft.com/fwlink/p/?LinkId=307141).
  
For information about how to install language packs, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md). For information about how to let individual users change the language that is used to display their site's user interface, see [Choose the languages that you want to make available for a site's user interface](https://go.microsoft.com/fwlink/p/?LinkId=307142).
  
## Use and benefits of the multilingual user interface feature
<a name="MUIBene"> </a>

The MUI feature enables users to collaborate in a single site by using another language that they prefer, regardless of which language was selected when the site was created. For example, the default language for a site could be English, and a user whose preferred language is French will view the site in French, whereas a user whose preferred language is Spanish will view the site in Spanish. 
  
When you create a site and install language packs on all the web and application servers, you can specify the default site language. The site will use that language to display the site's user interface, such as site navigation and administrative pages. If you want to enable site users to view the site's user interface in a preferred language, you can use the **Language Settings** page to specify alternate languages that you want to make available to users. When a user logs on to the site, the users preferred language is used to display the site's user interface. All sites within that domain name are displayed in the user's preferred language. This does not change the default site language. Other users who view the site see the site's user interface displayed either in the default site language or in their preferred language. The site's user interface is changed only for those users who have specified a preferred language in which to view the site. 
  
The MUI feature, lets team members work on documents and projects in a shared language while they view the site and perform tasks in their preferred language. In addition to team collaboration, the MUI feature enables farm, site collection administrators, and site owners to perform administrative tasks in their preferred language. For example, farm administrators can view the administrative links and instructions on the SharePoint Central Administration website in their preferred language.
  
The MUI feature also enables users to change new and existing application content — such as list or library titles and descriptions — and it enables users to have those changes be reflected in the user interface for users of other languages. For example, a team member who uses English as the preferred language creates a new document library named "Team Reports." Another team member, who has the preferred language set to German, logs on to the site and changes the library title to "Mannschaftsberichte." The next time that users who have their preferred language set to German logs on to the site, the name of the document library is displayed as "Mannschaftsberichte." But users who have their preferred language set to English still see the document library name displayed as "Team Reports."
  
## What is supported by the multilingual user interface
<a name="supported"> </a>

When a user views a site in a preferred language, certain elements of the user interface are displayed in the preferred language. Generally, most user interface elements can be displayed in the preferred language, but user-created content cannot be. The following list includes examples of items that are supported by the MUI feature:
  
- Settings pages, such as those in the _layouts and the _admin virtual directories.
    
- SharePoint Help.
    
- Application content, such as menus, controls, site actions, site title and description, list or library titles and descriptions, top link bar links, Quick Launch links, local breadcrumbs, site and list content types, and site and list columns.
    
- Developer content, such as features and solutions.
    
- List views.
    
- Web Part titles, descriptions, custom properties, and import error messages.
    
- The Blog site template. 
    
Not all user interface elements are displayed in the preferred language. The following list includes examples of items that aren't supported by the MUI feature:
  
- Global breadcrumbs.
    
- User-created content, such as list item data, documents and web pages in libraries, custom permission levels, and groups.
    
For more detailed information about the user interface elements that are not supported by the MUI feature, see [Limitations of the multilingual user interface](#MUILimits).
  
## Managing application content
<a name="appcontent"> </a>

Application content includes content such as menus, controls, site actions, site title and description, list or library titles and descriptions, top link bar links, Quick Launch links, local breadcrumbs, site and list content types, and site and list columns. The MUI feature enables users to add or edit application content either in the default site language or in one or more alternate languages. You can also choose to export and import application content for bulk translation.
  
### Adding and editing application content

When users add or edit application content, the following rules apply:
  
- **When users view a site in the default site language, any new application content that they create is displayed in the default site language, even when the site is viewed in another language.**
    
    For example, if the default site language is English, when a user views the site in English and creates a new document library named "Team Documents," the library title is still displayed as "Team Documents" when the user views the site in French.
    
- **When users view a site in another language, any new application content that they create is displayed in that language, even when the site is viewed in the default site language, or in any other language.**
    
    For example, if the default site language is English, and a user views the site in German and adds a document library named "Mannschaftsdokumente," the library title is displayed as "Mannschaftsdokumente" even when the site is viewed in English. To translate application content, such as a document library title into the default site language or into an alternate language, users must first change the language preference either in their user profile, or in their web browser settings, to display the site in the language they want to use, and then change the user interface string. The exception to this behavior is if the **Overwrite Translations** option is enabled. For more information, see [Overwriting translated application content](#Overwrite).
    
When a site is displayed in a user's preferred language, any changes that are made to existing application content strings are changed for that language only. The strings that are associated with specific application content in the default site language and any alternate languages remain unchanged. To translate application content strings, such as a document library title into the default site language or into any alternate languages, the user must change the language preferences in the browser or user profile to display the site in the default or switch language, and then make the change to the user interface strings.
  
<a name="Overwrite"> </a>
### Overwriting translated application content

The **Language Settings** page contains an **Overwrite Translations** option that affects how changes to existing application content are made to other languages for the site. If the **Overwrite Translations** option is enabled, any changes that are made to the user interface in the default site language will overwrite any changes that were made to those same user interface elements in switch languages. 
  
By default, when a user views a site in the default site language, any changes that are made to existing application content are changed for the default site language only. The strings that are associated with specific application content in the alternate languages remain unchanged. If the **Overwrite Translations** option is enabled, the strings that are associated with that application content for every language are replaced with the new default site language string. For example, if the default site language is English and a user changes the title of the "Shared Documents" library to "Team Documents," by default, the title is changed only for the default site language. If the **Overwrite Translations** option is enabled, the title is changed to "Team Documents" for every alternate language, and it must be re-translated. 
  
### Exporting and importing translated application content
<a name="Export"> </a>

The MUI feature lets you export and import application content for bulk translation. Instead of translating application content one item at a time, you can export the strings for any new or changed application content in the default site language or in one of the alternate languages. To export content, you use the **Export Translations** link on the **Site Settings** page. When you export application content for an alternate language, you can choose to export all content or only content that has not been translated. 
  
When the application content is exported, it is saved as a .resx file, which can be opened by using a text editor or any third-party tool that can open resource files. For more information, see [Resources in .resx File Format](https://go.microsoft.com/fwlink/?linkid=845132). After the resource strings are translated, you use the **Import Translations** link on the **Site Settings** page to import the .resx file. 
  
## Using the multilingual user interface with managed metadata
<a name="UseMUI"> </a>

You can create multilingual managed metadata to use with a SharePoint Server solution. Use the Term Store Management Tool, to create a term set and associate multiple labels, one for each language that you want to support, with each term in the set. When a user views the site in the user's preferred language, the terms are displayed by using the labels that correspond to the preferred language. 
  
<a name="MUILimits"> </a>
## Limitations of the multilingual user interface

As mentioned previously, some user interface elements are not MUI-enabled — that is, they are not supported by the MUI feature. This section describes additional limitations that apply when you use the MUI feature with shared components and site templates.
  
### Shared components
<a name="sharedcomponents"> </a>

Shared components, such as lists and permissions, appear across all site templates. Their functionality is centrally defined, and their behavior is consistent regardless of the site template in which they appear.
  
 **Lists**
  
List views are MUI-enabled, but list items are not because they are user-created content. List items will continue to display the values that were entered when they were created, regardless of the user's preferred language.
  
 **Permissions**
  
The following properties that are associated with permissions are not MUI-enabled. They are always displayed in the default site language or the language in which they were created: 
  
- **Permission group names** These include default permission group names and any custom permission groups that were created by a user. 
    
- **Custom permission level names and descriptions** These include any custom permission levels that were created or changed by a user. 
    
- **User information** User information such as About Me, Title, and Department. 
    
### Search site templates
<a name="sitetemplates"> </a>

Many of the Search site limitations are not actually related to MUI features, but are architectural designs that affect the user interface. The following limitations are a mix of MUI and architectural limitations for Search sites:
  
- **Search** Search indexes content in the default language of the SharePoint Server installation. Even if content is provided in alternate languages, that content is only searchable by using the default site language. For example, if your preferred language is German, and the default site language is English, a search for "Freigegebene Dokumente" returns no results. A search for "Shared Documents" does return results. 
    
- **Search Web Part properties** Title, description, and custom properties are MUI-enabled. But if the default search prompt for the search box is customized, its customized value will be displayed for all languages. 
    
- **Refinement Panel Web Part** The Refinement Panel Web Part is not MUI-enabled. Term store labels that are displayed in the Refinement Panel Web Part are always displayed from the search index, which only stores items in the default site language. For example, if your preferred language is Italian, and the default site language is English, and you have a document that uses term store labels that contain values for both languages, the Refinement Panel Web Part will display only the English label. 
    
    > [!NOTE]
    > This does not apply to the Taxonomy Refinement Panel Web Part, which displays the same language labels as the ones used in managed navigation. 
  
## Plan to use the multilingual user interface
<a name="PlanMUI"> </a>

Planning to use the MUI feature with a SharePoint Server site involves the following tasks:
  
- Determine site language requirements.
    
- Plan to install Public Update.
    
- Plan to translate application content.
    
### Determine site language requirements
<a name="section1"> </a>

Before you can use the MUI feature in SharePoint Server sites, the farm administrator must install language packs on all web and application servers so that they are available to use on sites. Decide which language packs are needed, and when they will be installed on the server. Site collection administrators or site owners must configure the language settings for individual sites to make specific languages available to site users. You must decide which languages are needed for each site, and plan to have the site collection administrators or site owners enable specific languages for the sites that they manage. For information about how to plan multilingual sites, see [Plan for multilingual sites in SharePoint Server](plan-for-multilingual-sites.md). For information about how to install language packs, see [Install or uninstall language packs for SharePoint Servers 2016 and 2019](../install/install-or-uninstall-language-packs-0.md) and [Install or uninstall language packs for SharePoint 2013](../install/install-or-uninstall-language-packs.md).
  
### Plan to install Public Update
<a name="section3"> </a>

If language packs are updated as part of a public update for SharePoint Server, you must update the language packs on the servers when the public update is installed. You should plan to coordinate with the farm administrator to monitor the release of public update and any associated language packs so that you know about updated language packs that must be installed for users.
  
### Plan to translate application content
<a name="section2"> </a>

If you plan to enable the MUI feature on your site to provide users a way to collaborate while they use their preferred language, you must decide whether the default MUI feature is sufficient, or whether application content must also be translated. If you have application content that must be translated, you should consider the following questions:
  
- **How will new and existing application content be translated?** Will individual team members translate application content directly in the user interface as it is needed, or will you export resource files in the languages that are needed for the site, and have them all translated at the same time? If users create new application content in an alternate language, you must plan for who will translate that content into the default site language and for each alternate language. If you plan to create complex pages, such as new menu pages, or develop custom solutions, such as features that create lists, you must plan to use the object model to provide translations in alternate languages. 
    
- **Who will translate the application content?** Will resource files be translated by someone within your organization, or will you have a third-party translate them for you? 
    
- **How will updates to the application content be handled?** Will changes to the user interface be translated as changes are made, or will changes be made on a periodic schedule? This might depend on the size and scale of the sites and the content that is included. 
    
- **How should translation overwrites be handled?** Do you want changes in the default site language to overwrite string values in alternate languages? If so, then you must enable the **Overwrite Translations** option on the **Language Settings** page. 
    
- **What column names must be changed?** What column names must be translated, and for which languages? Will the column names be at the list level or at the site level? 
    
## See also
<a name="SeeUI"> </a>

#### Concepts

[Plan for multilingual sites in SharePoint Server](plan-for-multilingual-sites.md)
  
[Variations overview in SharePoint Server](../administration/variations-overview.md)
  
[Plan for variations in SharePoint Server](../administration/plan-for-variations.md)
#### Other Resources

[Language Packs for SharePoint Server 2019](https://www.microsoft.com/en-us/download/details.aspx?id=57463)

[Language Packs for SharePoint Server 2016](https://www.microsoft.com/en-us/download/details.aspx?id=51492)
  
[Language Packs for SharePoint Server 2013](https://www.microsoft.com/en-us/download/details.aspx?id=37140)

