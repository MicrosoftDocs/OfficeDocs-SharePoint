---
title: "Export and import customized search configuration settings in SharePoint Server"
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
ms.assetid: 0112182a-6246-4d8a-8c07-39622be3c4a1
description: "Learn how to export and import customized search configuration settings."
---

# Export and import customized search configuration settings in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can export and import customized search configuration settings between site collections and sites. The settings that you export and import include all customized query rules, result sources, result types, ranking models, and site search settings. It is also possible to export customized search configuration settings from a Search service application and import the settings to site collections and sites, but you cannot import customized search configuration settings to a Search service application. You can't export the default search configuration settings, and you can't import customized search configurations from SharePoint Server to SharePoint Online, or the other way around.
  
You can use the following methods to export or import customized search configuration settings:
  
- To export or import customized search configuration settings at a site collection or site, use the **Site Settings** page or CSOM. 
    
- To export customized search configuration settings from a Search service application, use CSOM.
    
If you want to transfer all **Master Page Gallery** files, use the **Design Manager**. If you want to transfer a whole site, use **Save site as template**. If you want to export or import customized search settings programmatically, see [Exporting and importing search configuration settings in SharePoint](https://msdn.microsoft.com/library/dn205276.aspx) on MSDN. 
  
This article describes how to use the **Site Settings** page to export and import customized search configuration settings for site collections, and sites. 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the information in [Overview of customized search configuration settings that can be exported and imported](export-and-import-customized-search-configuration-settings.md#BKMK_2) and ensure: 
  
- That the search configuration file and the target for your import do not have settings with the same name, except for managed properties.
    
- That the source of your export does not include managed properties or aliases that contain the invalid characters listed in [Invalid characters causing the import to fail](export-and-import-customized-search-configuration-settings.md#BKMK_Invalid).
    
- That managed property names and aliases are unique within the combination of the search configuration file and the search configuration settings on the target site and its parent site collection.
    
> [!NOTE]
> Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources: 
>- [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)
>- [Accessibility for SharePoint 2013](/SharePoint/accessibility-guidelines)
>- [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)
>- [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)
>- [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
    
## Export customized search configuration settings from a site collection
<a name="proc2"> </a>

 **To export customized search configuration settings from a site collection**
  
1. Verify that the user account that is performing this procedure has **Full control** permission level at the site collection. 
    
2. In the site collection, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section click **Search Configuration Export**.
    
4. In the dialog box, click **Save**.
    
## Export customized search configuration settings from a site
<a name="proc3"> </a>

 **To export customized search configuration settings from a site**
  
1. Verify that the user account that is performing this procedure has **Full control** permission level at the site. 
    
2. On the site, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Search** section click **Configuration Export**.
    
4. In the dialog box, click **Save**.
    
## Import customized search configuration settings to a site collection
<a name="proc5"> </a>

 **To import customized search configuration settings to a site collection**
  
1. Verify that the user account that is performing this procedure has **Full control** permission level at the site collection. 
    
2. In the site collection, in the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Configuration Import**.
    
4. On the **Import Search Configuration** page, either type the name and location of the search configuration file to import, or click **Browse** and select the file name and location of the search configuration file to import, and then click **Import**.
    
5. On the **Search Config List** page, verify that: 
    
  - The search configuration file that you imported is in the list, and that its status is **Imported Successfully**.
    
    If the file has not imported successfully, the **Notes** column provides details about what happened. The **Notes** column also provides details, in some cases, when the file has imported successfully. For example if the file contains a managed property that has the same name as a managed property on the target, the **Notes** column indicates that this managed property already exists on the target. 
    
  - The **Scope** column shows that the settings you imported are at the correct level, that is, at the level you meant to import the files to. For example, if you imported your settings at the site collection level instead of at the site level, you would see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are site collection (SPSite) or site (SPWeb). 
    
## Import customized search configuration settings to a site
<a name="proc6"> </a>

 **To import customized search configuration settings to a site**
  
1. Verify that the user account that is performing this procedure has **Full control** permission level at the site. 
    
2. On the site, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Search** section click **Configuration Import**.
    
4. On the **Import Search Configuration** page, either type the name and location of the search configuration file to import, or click **Browse** and select the file name and location of the search configuration file to import, and then click **Import**.
    
5. On the **Search Config List** page, verify that: 
    
  - The search configuration file you imported is in the list, and that its status is **Imported Successfully**.
    
    If the file has not imported successfully, the **Notes** column provides details about what happened. The **Notes** column also provides details, in some cases, when the file has imported successfully. For example if the file contains a managed property that has the same name as a managed property on the target, the **Notes** column indicates that this managed property already exists on the target. 
    
  - The **Scope** column shows that the settings you imported are at the correct level, that is, at the level you meant to import the files to. For example, if you imported your settings at the site collection level instead of at the site level, you would see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are site collection (SPSite) or site (SPWeb). 
    
## Overview of customized search configuration settings that can be exported and imported
<a name="BKMK_2"> </a>

When you export customized search configuration settings, SharePoint Server creates a search configuration file in XML format. This search configuration file includes all exportable customized search configuration settings at the Search service application, site collection, or site level from where you start the export. A search configuration file for a site collection does not contain search configuration settings from the individual sites within the site collection.
  
When you import a search configuration file, SharePoint Server creates and enables each customized search configuration setting in the site collection or site from where you start the import.
  
This table shows the settings that you can export and import. For each setting, the table indicates any dependencies on other customized search configuration settings. If the customized search configuration settings depend on a customized search configuration setting at a different level, for example, if a site query rule depends on a result source at site collection level, you must export and import settings at all of the relevant levels.
  
|                  **Customized search configuration setting**                   | **Dependency on other customized search configuration settings** |
| :----------------------------------------------------------------------------- | :--------------------------------------------------------------- |
| Query rules. These include result blocks, promoted results, and user segments. | Result sources, result types, search schema, ranking model       |
| Result sources                                                                 | Search schema                                                    |
| Result types                                                                   | Search schema, result sources, display templates                 |
| Search schema                                                                  | None                                                             |
| Ranking model                                                                  | Search schema                                                    |
   
### Conditions that may cause the import to fail

- If the search configuration file and the target for your import have settings with the same name, the import of the search configuration file fails when it encounters this setting. Exceptions:
    
  - If you reimport a search configuration file, the settings that have the same name in the search configuration file and on the target do not cause the import to fail. 
    
  - Managed properties with the same name do not cause an import to fail if the individual managed property settings are the same on the property in the search configuration file and on the target property.
    
  - Managed properties with the same name do not cause an import to fail if the aliases and mappings to crawled properties are different on the managed property in the search configuration file and on the target managed property. The import adds the aliases and mappings on the managed property in the search configuration file to the aliases and mappings on the target managed property.
    
- If the search configuration file contains managed property names or aliases that contain invalid characters, the import fails when it encounters that managed property name or alias.
    
- The managed property names and aliases of a search schema must be unique for a site and its parent site collection. This means:
    
  - If your search configuration file has a managed property that has the same name as an alias for a managed property on your target site or the parent site collection of your target site, then the import fails.
    
  - If your search configuration file has a managed property with an alias that has the same name as a managed property on your target site or the parent site collection of your target site, then the import fails.
    
> [!NOTE]
> Customized search settings that SharePoint Server created and enabled before the import failed remain enabled. 
  
If the import fails, remove the condition that caused the failure and reimport the search configuration file. For example, if the **Notes** column states that there is already a query rule with the same name as the query rule that you are trying to import, then you should remove that query rule either from the target or from the import file, and then reimport the file. 
  
### Invalid characters causing the import to fail
<a name="BKMK_Invalid"> </a>

If managed properties or aliases contain any of the listed characters, the import of the customized search schema that contains these properties will fail.
  
| **Character** |       **Name**        |
| :------------ | :-------------------- |
|               | space                 |
| :             | colon                 |
| ;             | semicolon             |
| ,             | comma                 |
| (             | opening parenthesis   |
| )             | closing parenthesis   |
| [             | opening bracket       |
| ]             | closing bracket       |
| {             | opening brace         |
| }             | closing brace         |
| %             | percent               |
| $             | dollar sign           |
| _             | underscore            |
| +             | plus sign             |
| !             | exclamation point     |
| \*            | asterisk              |
| =             | equal sign            |
| &amp;         | ampersand             |
| ?             | question mark         |
| @             | at sign               |
| #             | number sign           |
| \             | backslash             |
| ~             | tilde                 |
| \<            | opening angle bracket |
| \>            | closing angle bracket |
| \|            | pipe                  |
| `             | grave accent          |
| ^             | caret                 |
| \'            | escape sequence       |
| \"            | escape sequence       |
   

