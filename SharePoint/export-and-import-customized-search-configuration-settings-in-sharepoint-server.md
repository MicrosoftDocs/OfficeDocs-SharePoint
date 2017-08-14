---
title: Export and import customized search configuration settings in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 0112182a-6246-4d8a-8c07-39622be3c4a1
---


# Export and import customized search configuration settings in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-24* **Summary:** Learn how to export and import customized search configuration settings.You can export and import customized search configuration settings between site collections and sites. The settings that you export and import include all customized query rules, result sources, result types, ranking models, and site search settings. It is also possible to export customized search configuration settings from a Search service application and import the settings to site collections and sites, but you cannot import customized search configuration settings to a Search service application. You can't export the default search configuration settings, and you can't import customized search configurations from SharePoint Server to SharePoint Online, or the other way around.You can use the following methods to export or import customized search configuration settings:
- To export or import customized search configuration settings at a site collection or site, use the **Site Settings** page or CSOM.
    
  
- To export customized search configuration settings from a Search service application, use CSOM.
    
  
If you want to transfer all **Master Page Gallery** files, use the **Design Manager**. If you want to transfer a whole site, use **Save site as template**. If you want to export or import customized search settings programmatically, see [Exporting and importing search configuration settings in SharePoint 2013](https://msdn.microsoft.com/library/dn205276.aspx) on MSDN.This article describes how to use the **Site Settings** page to export and import customized search configuration settings for site collections, and sites.In this article:
-  [Before you begin](#begin)
    
  
-  [Export customized search configuration settings from a site collection](#proc2)
    
  
-  [Export customized search configuration settings from a site](#proc3)
    
  
-  [Import customized search configuration settings to a site collection](#proc5)
    
  
-  [Import customized search configuration settings to a site](#proc6)
    
  
-  [Overview of customized search configuration settings that can be imported and exported](#BKMK_2)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the information in  [Overview of customized search configuration settings that can be exported and imported](#BKMK_2) and ensure:
- That the search configuration file and the target for your import do not have settings with the same name, except for managed properties.
    
  
- That the source of your export does not include managed properties or aliases that contain the invalid characters listed in  [Invalid characters causing the import to fail](#BKMK_Invalid).
    
  
- That managed property names and aliases are unique within the combination of the search configuration file and the search configuration settings on the target site and its parent site collection.
    
  

> [!NOTE:]
>  [Plan browser support](https://go.microsoft.com/fwlink/p/?LinkId=246502)> **Accessibility for SharePoint 2013**>  [Accessibility features in SharePoint 2013 Products](https://go.microsoft.com/fwlink/p/?LinkId=246501)>  [Keyboard shortcuts](https://go.microsoft.com/fwlink/p/?LinkID=246504)>  [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
  
    
    


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
    
  
3. On the **Site Settings** page, in the **Search** section click ** Configuration Import**.
    
  
4. On the **Import Search Configuration** page, either type the name and location of the search configuration file to import, or click **Browse** and select the file name and location of the search configuration file to import, and then click **Import**.
    
  
5. On the **Search Config List** page, verify that:
    
  - The search configuration file you imported is in the list, and that its status is **Imported Successfully**.
    
    If the file has not imported successfully, the **Notes** column provides details about what happened. The **Notes** column also provides details, in some cases, when the file has imported successfully. For example if the file contains a managed property that has the same name as a managed property on the target, the **Notes** column indicates that this managed property already exists on the target.
    
  
  - The **Scope** column shows that the settings you imported are at the correct level, that is, at the level you meant to import the files to. For example, if you imported your settings at the site collection level instead of at the site level, you would see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are site collection (SPSite) or site (SPWeb).
    
  

## Overview of customized search configuration settings that can be exported and imported
<a name="BKMK_2"> </a>

When you export customized search configuration settings, SharePoint Server creates a search configuration file in XML format. This search configuration file includes all exportable customized search configuration settings at the Search service application, site collection, or site level from where you start the export. A search configuration file for a site collection does not contain search configuration settings from the individual sites within the site collection.When you import a search configuration file, SharePoint Server creates and enables each customized search configuration setting in the site collection or site from where you start the import.This table shows the settings that you can export and import. For each setting, the table indicates any dependencies on other customized search configuration settings. If the customized search configuration settings depend on a customized search configuration setting at a different level, for example, if a site query rule depends on a result source at site collection level, you must export and import settings at all of the relevant levels.
### 

Customized search configuration setting Dependency on other customized search configuration settings Query rules. These include result blocks, promoted results, and user segments.  <br/> Result sources, result types, search schema, ranking model  <br/> Result sources  <br/> Search schema  <br/> Result types  <br/> Search schema, result sources, display templates  <br/> Search schema  <br/> None  <br/> Ranking model  <br/> Search schema  <br/> 
## Conditions that may cause the import to fail


- If the search configuration file and the target for your import have settings with the same name, the import of the search configuration file fails when it encounters this setting. Exceptions:
    
  - If you reimport a search configuration file, the settings that have the same name in the search configuration file and on the target do not cause the import to fail. 
    
  
  - Managed properties with the same name do not cause an import to fail if the individual managed property settings are the same on the property in the search configuration file and on the target property.
    
  
  - Managed properties with the same name do not cause an import to fail if the aliases and mappings to crawled properties are different on the managed property in the search configuration file and on the target managed property. The import adds the aliases and mappings on the managed property in the search configuration file to the aliases and mappings on the target managed property.
    
  
- If the search configuration file contains managed property names or aliases that contain invalid characters, the import fails when it encounters that managed property name or alias.
    
  
- The managed property names and aliases of a search schema must be unique for a site and its parent site collection. This means:
    
  - If your search configuration file has a managed property that has the same name as an alias for a managed property on your target site or the parent site collection of your target site, then the import fails.
    
  
  - If your search configuration file has a managed property with an alias that has the same name as a managed property on your target site or the parent site collection of your target site, then the import fails.
    
  

> [!NOTE:]

  
    
    

If the import fails, remove the condition that caused the failure and reimport the search configuration file. For example, if the **Notes** column states that there is already a query rule with the same name as the query rule that you are trying to import, then you should remove that query rule either from the target or from the import file, and then reimport the file.
## Invalid characters causing the import to fail
<a name="BKMK_Invalid"> </a>

If managed properties or aliases contain any of the listed characters, the import of the customized search schema that contains these properties will fail.
### 

 **Character** **Name** <br/> space  <br/> :  <br/> colon  <br/> ;  <br/> semicolon  <br/> ,  <br/> comma  <br/> (  <br/> opening parenthesis  <br/> )  <br/> closing parenthesis  <br/> [  <br/> opening bracket  <br/> ]  <br/> closing bracket  <br/> {  <br/> opening brace  <br/> }  <br/> closing brace  <br/> %  <br/> percent  <br/> $  <br/> dollar sign  <br/> _  <br/> underscore  <br/> +  <br/> plus sign  <br/> !  <br/> exclamation point  <br/> *  <br/> Asterisk  <br/> =  <br/> equal sign  <br/> &amp;  <br/> Ampersand  <br/> ?  <br/> question mark  <br/> @  <br/> at sign  <br/> #  <br/> number sign  <br/> \\  <br/> Backslash  <br/> ~  <br/> Tilde  <br/> <  <br/> opening angle bracket  <br/> >  <br/> closing angle bracket  <br/> |  <br/> Pipe  <br/> `  <br/> grave accent  <br/> ^  <br/> Caret  <br/> \\'  <br/> escape sequence  <br/> \\"  <br/> escape sequence  <br/> 
