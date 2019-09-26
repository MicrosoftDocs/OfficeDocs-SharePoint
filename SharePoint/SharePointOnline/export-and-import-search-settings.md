---
title: "Export and import customized search configuration settings"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- MET150
ms.assetid: b136a278-d302-4dc4-84b9-80287c59afdf
description: "Learn how to export and import customized search configuration settings between tenants, site collections, and sites."
---

# Export and import customized search configuration settings

As a global or SharePoint admin in Office 365, you can export and import customized search configuration settings between tenants, site collections, and sites. The settings that you export and import include all customized query rules, result sources, result types, ranking models and site search settings. It's also possible to export customized search configuration settings from a Search service application and import the settings to tenants, site collections, or sites. You can't export the default configuration settings. 
  
## Overview
<a name="__toc351540657"> </a>

When you export customized search configuration settings, SharePoint creates a search configuration file in XML format. This search configuration file includes all exportable customized search configuration settings at the tenant, site collection, or site level from where you start the export. A search configuration file for a site collection doesn't contain search configuration settings from the individual sites within the site collection. 
  
When you import a search configuration file, SharePoint Online creates and enables each customized search configuration setting in the tenant, site collection or site from where you start the import.
  
This table shows the settings that you can export or import. For each setting, you'll find dependencies on other customized search configuration settings. If the customized search configuration settings depend on a customized search configuration setting at a different level, for example, if a site query rule depends on a result source at site collection level, you must export and import settings at all of the relevant levels.
  
|**Customized search configuration setting**|**Dependency on other customized search configuration settings**|
|:-----|:-----|
|Query rules. These include result blocks, promoted results, and user segments.  <br/> |Result sources, result types, search schema, ranking model.  <br/> |
|Result sources  <br/> |Search schema  <br/> |
|Result types  <br/> |Search schema, result sources, display templates  <br/> |
|Search schema  <br/> |None  <br/> |
|Ranking model  <br/> |Search schema  <br/> |
   
### Conditions that can cause the import to fail
<a name="__toc351540658"> </a>

If the search configuration file and the target for your import have settings with the same name, the import of the search configuration file fails when it encounters this setting. There are exceptions however:
  
- If you reimport a search configuration file, the settings that have the same name in the search configuration file and on the target do not cause the import to fail.
    
- Managed properties with the same name do not cause an import to fail if the individual managed property settings are the same on the property in the search configuration file and on the target property.
    
- Managed properties with the same name do not cause an import to fail if the aliases and mappings to crawled properties are different on the managed property in the search configuration file and on the target managed property. The import adds the aliases and mappings on the managed property in the search configuration file to the aliases and mappings on the target managed property.
    
If the search configuration file contains managed property names or aliases that contain invalid characters, the import fails when it encounters that managed property name or alias.
  
The managed property names and aliases of a search schema must be unique for a site and its parent site collection. This means:
  
- If your search configuration file has a managed property that has the same name as an alias for a managed property on your target site or the parent site collection of your target site, then the import fails.
    
- If your search configuration file has a managed property with an alias that has the same name as a managed property on your target site or the parent site collection of your target site, then the import fails.
    
> [!NOTE]
>  Any customized search settings that were created and enabled by SharePoint before the import failed, remain enabled. 
  
If the import fails, remove the condition that caused the failure and reimport the search configuration file. For example, if the Notes column states that there is already a query rule with the same name as the query rule that you are trying to import, then you should remove that query rule either from the target or from the import file, and then reimport the file. See [Invalid characters causing your import to fail](export-and-import-search-settings.md#__toc351540665) later in this article. 
  
## Export customized search configuration settings from a tenant
<a name="__toc351540659"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  
    
2. In the left pane of the admin center, under **Admin centers**, select **SharePoint** to open the SharePoint admin center. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
 
3. In the left pane of the new SharePoint admin center, select **Classic features**.
 
4. Under **Search**, select Open.
    
5. Select **Export Search Configuration**.
    
6. In the dialog box, select **Save**.
    
## Export customized search configuration settings from a site
<a name="__toc351540660"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Search** section, select **Configuration Export**.
    
3. In the dialog box, select **Save**.
    
## Export customized search configuration settings from a site collection
<a name="__toc351540661"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Site Collection Administration** section, select **Search Configuration Export**.
    
3. In the dialog box, select **Save**.
    
## Import customized search configuration settings to a tenant
<a name="__toc351540662"> </a>

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin to open the Microsoft 365 admin center. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the **Admin** tile to open the admin center.  

In the left pane of the admin center, under **Admin centers**, select **SharePoint** to open the SharePoint admin center. (You might need to select **Show all** to see the list of admin centers.) If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
 
3. In the left pane of the new SharePoint admin center, select **Classic features**.
 
4. Under **Search**, select Open.
   
5. On the **Import Search Configuration** page, browse to the file you want to import. 
    
6. Select **Import**.
    
7. On the **Search Config List** page verify that: 
    
8. The search configuration file you imported is in the list, and that its status is **Imported Successfully**.
    
    If the file hasn't been imported successfully, then the **Notes** column provides more details about what happened. 
    
9. The **Scope** column shows that the settings you imported are at the right level, that is, at the level you meant to import the file to. For example, if you imported your settings at the site collection level instead of at the site level, you'd see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are: tenant (Tenant), site collection (SPSite), or site level (SPWeb). 
    
## Import customized search configuration settings to a site
<a name="__toc351540663"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Search** section, select **Configuration Import**.
    
3. On the **Import Search Configuration** page, browse to the file you want to import. 
    
4. Select **Import**.
    
5. On the **Search Config List** page, verify that: 
    
6. The search configuration file you imported is in the list, and that its status is **Imported Successfully**.
    
    If the file hasn't imported successfully, then the **Notes** column provides more details about what happened. 
    
7. The **Scope** column shows that the settings you imported are at the right level, that is, at the level you meant to import the file to. For example, if you imported your settings at the site collection level instead of at the site level, you'd see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are: tenant (Tenant), site collection (SPSite), or site level (SPWeb). 
    
## Import customized search configuration settings to a site collection
<a name="__toc351540664"> </a>

1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the **Site Settings** page, in the **Site Collection Administration** section, select **Search Configuration Import**.
    
3. On the **Import Search Configuration** page, browse to the file you want to import. 
    
4. Select **Import**.
    
5. On the **Search Config List** page, verify that: 
    
6. The search configuration file you imported is in the list, and its status is **Imported Successfully**. 
    
    If the file hasn't imported successfully, then the **Notes** column provides more details about what happened. 
    
7. The **Scope** column shows that the settings you imported are at the right level, that is, at the level you meant to import the file to. For example, if you imported your settings at the site collection level instead of at the site level, you'd see this information in the **Scope** column. The **Scope** column shows at which level the search configuration settings were enabled. The levels are: tenant (Tenant), site collection (SPSite), or site level (SPWeb). 
    
## Invalid characters causing your import to fail
<a name="__toc351540665"> </a>

If managed properties or aliases contain any of the listed characters, the import of the customized search schema that contains these properties will fail.
  
|**Character**|**Name**|
|:-----|:-----|
||space  <br/> |
|:  <br/> |colon  <br/> |
|;  <br/> |semicolon  <br/> |
|,  <br/> |comma  <br/> |
|(  <br/> |opening parenthesis  <br/> |
|)  <br/> |closing parenthesis  <br/> |
|[  <br/> |opening bracket  <br/> |
|]  <br/> |closing bracket  <br/> |
|{  <br/> |opening brace  <br/> |
|}  <br/> |closing brace  <br/> |
|%  <br/> |percent  <br/> |
|$  <br/> |dollar sign  <br/> |
|_  <br/> |underscore  <br/> |
|+  <br/> |plus sign  <br/> |
|!  <br/> |exclamation point  <br/> |
|\*  <br/> |asterisk  <br/> |
|=  <br/> |equal sign  <br/> |
|&amp;  <br/> |ampersand  <br/> |
|?  <br/> |question mark  <br/> |
|@  <br/> |at sign  <br/> |
|#  <br/> |number sign  <br/> |
|\  <br/> |backslash  <br/> |
|~  <br/> |tilde  <br/> |
|\<  <br/> |opening angle bracket  <br/> |
|\>  <br/> |closing angle bracket  <br/> |
|\|  <br/> |pipe  <br/> |
|`  <br/> |grave accent  <br/> |
|^  <br/> |caret  <br/> |
|\'  <br/> |escape sequence  <br/> |
|\"  <br/> |escape sequence  <br/> |
