---
title: "Automatically created managed properties in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 8/24/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 2496edef-5bc4-4bd5-8b14-076894374a3f
description: "Learn about the naming conventions for automatically created crawled properties and managed properties."
---

# Automatically created managed properties in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
    
## How site columns become managed properties
<a name="BKMK_FromSiteColumnsToManagedProperties"> </a>

When you add columns to a SharePoint library or list, you can choose to add regular columns or site columns. For information about the difference between regular columns and site columns, see [Introduction to columns](https://msdn.microsoft.com/en-us/library/ms450825.aspx). In SharePoint, only site columns that contain values will automatically become managed properties when they are crawled. Regular columns will not automatically become managed properties when they are crawled. 
  
Before you can share content in a library or list with other site collections, you must share the library or list as a catalog, and then start a full crawl of the content. For more information, see "Share a library or list as a catalog" in [Configure cross-site publishing in SharePoint Server](../administration/configure-cross-site-publishing.md).
  
During the crawl of library content, the following actions are performed on the site columns:
  
1. A crawled property is created. Spaces are removed from the site column name, and then the following prefixes are added to the site column name to create the crawled property name:
    
  - For site columns of type **Publishing HTML** and **Multiple line of text**: ows_r_ _\<four letter code\>__
    
  - For site columns of type **Managed Metadata**: ows_taxId_
    
  - For all other site column types: ows_q_ _\<four letter code\>__
    
2. A managed property is created and mapped to the corresponding crawled property. Spaces are removed from the site column name, and the following items are added to the site column name to create the managed property name:
    
  - For all site columns of type **Managed Metadata**, the following prefix is added: owstaxId
    
  - For all other site column types, the following suffix is added: OWS _ \<four letter code\> _
    
> [!IMPORTANT]
> The four letter code represents the site column type, not the managed property type. All automatically created managed properties are of type Text. 
  
**Examples of automatically created crawled property names and managed property names for site columns without special characters**

|**Site column type**|**Site column name**|**Crawled property name**|**Managed property name**|**Data format**|
|:-----|:-----|:-----|:-----|:-----|
|Single line of text  <br/> | Site Column Name  <br/> |ows_q_TEXT_SiteColumnName  <br/> |SiteColumnNameOWSTEXT  <br/> |As is.  <br/> |
|Multiple lines of text  <br/> |Site Column Name  <br/> |ows_r_MTXT_SiteColumnName  <br/> |SiteColumnNameOWSMTXT  <br/> |As is.  <br/> |
|Choice  <br/> |Site Column Name  <br/> |ows_q_CHCS_SiteColumnName  <br/> |SiteColumnNameOWSCHCS  <br/> |The text value of the choice.  <br/> |
|Choice (allow multiple selections)  <br/> |Site Column Name  <br/> |ows_q_CHCM_SiteColumnName  <br/> |SiteColumnNameOWSCHCM  <br/> |Selected values separated by semicolon and hash mark — for example, MultiValue 2;# MultiValue 4;#.  <br/> |
|Number  <br/> |Site Column Name  <br/> |ows_q_NMBR_SiteColumnName  <br/> |SiteColumnNameOWSNMBR  <br/> |Textual representation of the number. The value will use dot as a decimal symbol.  <br/> This format cannot be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.  <br/> |
|Currency  <br/> |Site Column Name  <br/> |ows_q_CURR_SiteColumnName  <br/> |SiteColumnNameOWSCURR  <br/> |Textual representation of the number. The value will use dot as a decimal symbol.  <br/> This format cannot be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.  <br/> |
|Date and Time  <br/> |Site Column Name  <br/> |ows_q_DATE_SiteColumnName  <br/> |SiteColumnNameOWSDATE  <br/> |Textual representation of the date in the format YYYY-MM-DDTHH:MM:SSZ. For example, December 25, 2012, 7 AM GMT is 2012-12-25T07:00:00Z.  <br/> This format cannot be used in a greater than or less than comparison with other dates. It should only be used when querying for and displaying an exact date.  <br/> |
|Yes/No  <br/> |Site Column Name  <br/> |ows_q_BOOL_SiteColumnName  <br/> |SiteColumnNameOWSBOOL  <br/> |For true, use value 1. For false, use value 0.  <br/> |
|Person or Group  <br/> |Site Column Name  <br/> |ows_q_USER_SiteColumnName  <br/> |SiteColumnNameOWSUSER  <br/> |Email | Display | Name | EncodedClaim Claim. For example, "ellenk@contoso.com | Ellen Kessels | 693A30232E777C7265646D6F6E645C70696E676A i:0#.w|contoso\ellenk"  <br/> |
|Hyperlink or Picture  <br/> |Site Column Name  <br/> |ows_q_URLH_SiteColumnName  <br/> |SiteColumnNameOWSURHL  <br/> |URL, description. For example, http://www.contoso.com, Welcome to the home page of Contoso.  <br/> |
|Publishing HTML  <br/> |Site Column Name  <br/> |ows_r_HTML_SiteColumnName  <br/> |SiteColumnNameOWSHTML  <br/> |Html escaped enclosed in a paragraph tag. For example, \<p\>&amp;lt;div&amp;gt;&amp;lt;b&amp;gt;some html &amp;lt;/b&amp;&amp;lt;/div&amp;gt;\</p\>.  <br/> |
|Publishing Image  <br/> |Site Column Name  <br/> |ows_q_IMGE_SiteColumnName  <br/> |SiteColumnNameOWSIMGE  <br/> |Html image tag. For example, \<img alt="" src="/sites/pub/SiteCollectionImages/home.jpg" style="BORDER&amp;#58;0px solid;" /\>.  <br/> |
|Publishing Link  <br/> |Site Column Name  <br/> |ows_q_LINK_SiteColumnName  <br/> |SiteColumnNameOWSLINK  <br/> |Html link tag. For example, \<a href="http&amp;#58;//www.microsoft.com" target="_blank" title="mytooltip"\>Microsoft Website\</a\>.  <br/> |
|Managed Metadata  <br/> |Site Column Name  <br/> |ows_taxId_SiteColumnName  <br/> |owstaxIdSiteColumnName  <br/> |See "Data format for Managed Metadata" below.  <br/> |
|Integer\*  <br/> |Site Column Name  <br/> |ows_q_INTG_SiteColumnName  <br/> |SiteColumnNameOWSINTG  <br/> |Textual representation of the integer.  <br/> This format cannot be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.  <br/> |
|GUID\*  <br/> |Site Column Name  <br/> |ows_q_GUID_SiteColumnName  <br/> |SiteColumnNameOWSGUID  <br/> |Values separated by hyphens, enclosed in brackets. For example, {147C6BA1-709C-4401-964A-27AC36B62C54}.  <br/> |
|Grid Choice\*  <br/> |Site Column Name  <br/> |ows_q_CHCG_SiteColumnName  <br/> |SiteColumnNameOWSCHCG  <br/> |For each row, row name separated by semi-colon and hash mark, followed by the selected value.  <br/> |
|ContentTypeIDFieldType\*  <br/> |Site Column Name  <br/> |ows_q_CTID_SiteColumnName  <br/> |SiteColumnNameOWSCTID  <br/> |Name:#ContentTypeID;#  <br/> |
|SPS average rating  <br/> |Site Column Name  <br/> |ows_q_RAVG_SiteColumnName  <br/> |SiteColumnNameOWSRAVG  <br/> |Textual representation of the number. The value will use dot as a decimal symbol.  <br/> |
|SPS rating count  <br/> |Site Column Name  <br/> |ows_q_RCNT_SiteColumnName  <br/> |SiteColumnNameOWSRCNT  <br/> |Textual representation of the integer.  <br/> |
   
\*Column creation not available through user interface.
  
> [!NOTE]
>  Automatic creation of managed properties is not supported for the following site column types: >  Lookup >  Calculated >  Task outcome >  Summary Links data >  Rich media data for publishing 
  
 **Data format for Managed Metadata.**
  
To query for items tagged with a Managed Metadata field, you have to use the Unique Identifier for each label. You can find the Unique Identifier for each term in a term set in the Term Store Management Tool, on the **GENERAL** tab. In addition, the data format that is used in the query has to specify from which level in the term set the query should apply. This specification is set by adding one of the following prefixes to the Unique Identifier: 
  
- To query for all items that are tagged with a term: GP0|# 
    
- To query for all items that are tagged with a child of term: GPP|#
    
- To query for all items that are tagged with a term from a term set: GTSet|#
    
For example, let's say that you have a catalog of restaurants around the world. The catalog has a managed metadata site column named Location, which is tied to the term set named World. The term set has the following structure (the GUID for each term is shown in parentheses): 
  
- World (`fc01ae6d-8ed3-4872-9cef-d2199d52d61c`)
    
    - India (`c8a43f13-5ea1-45f2-b46d-3a1986a1cbd7`)
    
        - Mumbai (`ad491ed9-c21c-46d9-896c-c0d148957c60`)
    
        - Delhi (`c195b6e0-9062-446a-9af1-8ec1a642fede`)
    
    - France (`17587ed2-8433-45a4-9f4b-6825164fcd09`)
    
         - Paris (`01031cfe-2492-47f1-8723-45c63ef70ec9`)
    
         - Lyon (`3b2137a9-3c3a-4676-a50a-14f72ab29175`)
    
The catalog entries and examples of queries are shown in the following tables. 
  
**Catalog entries for restaurants and locations**

|**Restaurant**|**Location**|
|:-----|:-----|
|Restaurant 1  <br/> |Mumbai  <br/> |
|Restaurant 2  <br/> |Mumbai  <br/> |
|Restaurant 3  <br/> |Delhi  <br/> |
|Restaurant 4  <br/> |Paris  <br/> |
|Restaurant 5  <br/> |Lyon  <br/> |
   
**Query examples**

|**Query for**|**Data format**|**Query will return**|
|:-----|:-----|:-----|
|All restaurants in Mumbai  <br/> |GP0|#ad491ed9-c21c-46d9-896c-c0d148957c60  <br/> |Restaurant 1, Restaurant 2  <br/> |
|All restaurants in Delhi  <br/> |GP0|#c195b6e0-9062-446a-9af1-8ec1a642fede  <br/> |Restaurant 3  <br/> |
|All restaurants in India  <br/> |GPP|#c8a43f13-5ea1-45f2-b46d-3a1986a1cbd7  <br/> |Restaurant 1, Restaurant 2, Restaurant 3  <br/> |
|All restaurants in the World  <br/> |GTSet|#fc01ae6d-8ed3-4872-9cef-d2199d52d61c  <br/> |Restaurant 1, Restaurant 2, Restaurant 3, Restaurant 4, Restaurant 5  <br/> |
   
To display values by label — for example, Mumbai — you have to use the prefix L0|.
  
## Special characters and non-supported characters
<a name="BKMK_SpecialCharacters"> </a>

If a site column name contains diacritics, such as the German umlaut, or a non-supported character, such as #, these characters are included in the crawled property name, but not in the managed property name.
  
**Examples of automatically created crawled property names and managed property names for site columns with special or non-supported characters**

|**Site column name**|**Crawled property name**|**Managed property name**|
|:-----|:-----|:-----|
|Germanäö  <br/> |ows_q_TEXT_ Germanäö  <br/> |GermanOWSTEXT  <br/> |
|Site_Column#  <br/> |ows_q_TEXT_Site_Column#  <br/> |SiteColumnOWSTEXT  <br/> |
   
> [!NOTE]
> The following Unicode code blocks are considered non-supported characters: Unicode 0000-0021, Unicode 0080 - 00a1, Unicode 2000 - 2070, Unicode ff00 ff10, and Unicode ff1a ff20. 
  
## Default site columns for the Product Catalog content type
<a name="BKMK_DefaultSiteColumns"> </a>

The Product Catalog list in the Product Catalog site collection has six default site columns associated with its content type. The following table shows the names for these site columns and the names for their crawled properties and managed properties.
  
**Automatically created crawled property names and managed property names for site columns that belong to the Product Catalog content type**

|**Site column name**|**Crawled property name**|**Managed property name**|
|:-----|:-----|:-----|
|Title  <br/> |Title  <br/> |Title  <br/> |
|Item Number  <br/> |ows_q_TEXT_ProductCatalogItemNumber  <br/> |ProductCatalogItemNumberOWSTEXT  <br/> |
|Group Number  <br/> |ows_q_TEXT_ProductCatalogGroupNumber  <br/> |ProductCatalogGroupNumberOWSTEXT  <br/> |
|Language Tag  <br/> |ows_q_CHCS_ProductCatalogLanguageTag  <br/> |ProductCatalogLanguageTagOWSCHCS  <br/> |
|Item Category  <br/> |ows_taxId_ProductCatalogItemCategory  <br/> |owstaxIdProductCatalogItemCategory  <br/> |
|Rollup Image  <br/> |ows_r_IMGE_PublishingRollupImage  <br/> |PublishingImage  <br/> |
   

