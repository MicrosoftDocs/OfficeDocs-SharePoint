---
title: "Automatically created managed properties in SharePoint Server"
ms.reviewer:
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 8/24/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 2496edef-5bc4-4bd5-8b14-076894374a3f
description: "Learn about the naming conventions for automatically created crawled properties and managed properties."
---

# Automatically created managed properties in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]

## How site columns become managed properties
<a name="BKMK_FromSiteColumnsToManagedProperties"> </a>

When you add columns to a SharePoint library or list, you can choose to add regular columns or site columns. For information about the difference between regular columns and site columns, see [Introduction to columns](/previous-versions/office/developer/sharepoint-2010/ms450825(v=office.14)). In SharePoint, only site columns that contain values will automatically become managed properties when they're crawled. Regular columns won't automatically become managed properties when they're crawled.

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

|Site column type|Crawled property name|Managed property name|Data format|
|:-----|:-----|:-----|:-----|:-----|
|Single line of text|ows_q_TEXT_SiteColumnName|SiteColumnNameOWSTEXT|As is.|
|Multiple lines of text|ows_r_MTXT_SiteColumnName|SiteColumnNameOWSMTXT|As is.|
|Choice|ows_q_CHCS_SiteColumnName|SiteColumnNameOWSCHCS|The text value of the choice.|
|Choice (allow multiple selections)|ows_q_CHCM_SiteColumnName|SiteColumnNameOWSCHCM|Selected values separated by semicolon and hash mark — for example, MultiValue 2;# MultiValue 4;#.|
|Number|ows_q_NMBR_SiteColumnName|SiteColumnNameOWSNMBR|Textual representation of the number. The value will use dot as a decimal symbol.  <br/> This format can't be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.|
|Currency|ows_q_CURR_SiteColumnName|SiteColumnNameOWSCURR|Textual representation of the number. The value will use dot as a decimal symbol.  <br/> This format can't be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.|
|Date and Time|ows_q_DATE_SiteColumnName|SiteColumnNameOWSDATE|Textual representation of the date in the format YYYY-MM-DDTHH:MM:SSZ. For example, December 25, 2012, 7 AM GMT is 2012-12-25T07:00:00Z.  <br/> This format can't be used in a greater than or less than comparison with other dates. It should only be used when querying for and displaying an exact date.|
|Yes/No|ows_q_BOOL_SiteColumnName|SiteColumnNameOWSBOOL|For true, use value 1. For false, use value 0.|
|Person or Group|ows_q_USER_SiteColumnName|SiteColumnNameOWSUSER|Email, Display name, or Encoded claim. For example, ellenk@contoso.com, Ellen Kessels, or i:0#.w&#x7c;contoso\ellenk|
|Hyperlink or Picture|ows_q_URLH_SiteColumnName|SiteColumnNameOWSURLH|URL, description. For example, https://www.contoso.com, Welcome to the home page of Contoso.|
|Publishing HTML|ows_r_HTML_SiteColumnName|SiteColumnNameOWSHTML|Html escaped enclosed in a paragraph tag. For example, \<p\>&amp;lt;div&amp;gt;&amp;lt;b&amp;gt;some html &amp;lt;/b&amp;&amp;lt;/div&amp;gt;\</p\>.|
|Publishing Image|ows_q_IMGE_SiteColumnName|SiteColumnNameOWSIMGE|Html image tag. For example, \<img alt="" src="/sites/pub/SiteCollectionImages/home.jpg" style="BORDER&amp;#58;0px solid;" \/>.|
|Publishing Link|ows_q_LINK_SiteColumnName|SiteColumnNameOWSLINK|Html link tag. For example, \<a href="http&amp;#58;//www.microsoft.com" target="_blank" title="mytooltip"\>Microsoft Website\</a\>.|
|Managed Metadata|ows_taxId_SiteColumnName|owstaxIdSiteColumnName|See "Data format for Managed Metadata" below.|
|Integer\*|ows_q_INTG_SiteColumnName|SiteColumnNameOWSINTG|Textual representation of the integer.  <br/> This format can't be used in a greater than or less than comparison with other integers. It should only be used when querying for and displaying an exact value.|
|GUID\*|ows_q_GUID_SiteColumnName|SiteColumnNameOWSGUID|Values separated by hyphens, enclosed in brackets. For example, {147C6BA1-709C-4401-964A-27AC36B62C54}.|
|Grid Choice\*|ows_q_CHCG_SiteColumnName|SiteColumnNameOWSCHCG|For each row, row name separated by semi-colon and hash mark, followed by the selected value.|
|ContentTypeIDFieldType\*|ows_q_CTID_SiteColumnName|SiteColumnNameOWSCTID|Name:#ContentTypeID;#|
|SPS average rating|ows_q_RAVG_SiteColumnName|SiteColumnNameOWSRAVG|Textual representation of the number. The value will use dot as a decimal symbol.|
|SPS rating count|ows_q_RCNT_SiteColumnName|SiteColumnNameOWSRCNT|Textual representation of the integer.|

\* Column creation not available through user interface.

> [!NOTE]
> Automatic creation of managed properties is not supported for the following site column types: >  Lookup >  Calculated >  Task outcome >  Summary Links data >  Rich media data for publishing

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

|Restaurant|Location|
|:-----|:-----|
|Restaurant 1|Mumbai|
|Restaurant 2|Mumbai|
|Restaurant 3|Delhi|
|Restaurant 4|Paris|
|Restaurant 5|Lyon|

**Query examples**

|Query for|Data format|Query will return|&nbsp;|
|:-----|:-----|:-----|
|All restaurants in Mumbai|GP0|#ad491ed9-c21c-46d9-896c-c0d148957c60|Restaurant 1, Restaurant 2|
|All restaurants in Delhi|GP0|#c195b6e0-9062-446a-9af1-8ec1a642fede|Restaurant 3|
|All restaurants in India|GPP|#c8a43f13-5ea1-45f2-b46d-3a1986a1cbd7|Restaurant 1, Restaurant 2, Restaurant 3|
|All restaurants in the World|GTSet|#fc01ae6d-8ed3-4872-9cef-d2199d52d61c|Restaurant 1, Restaurant 2, Restaurant 3, Restaurant 4, Restaurant 5|

To display values by label — for example, Mumbai — you have to use the prefix L0|.

## Special characters and non-supported characters
<a name="BKMK_SpecialCharacters"> </a>

If a site column name contains diacritics, such as the German umlaut, or a non-supported character, such as #, these characters are included in the crawled property name, but not in the managed property name.

**Examples of automatically created crawled property names and managed property names for site columns with special or non-supported characters**

|Site column name|Crawled property name|Managed property name|
|:-----|:-----|:-----|
|Germanäö|ows_q_TEXT_ Germanäö|GermanOWSTEXT|
|Site_Column#|ows_q_TEXT_Site_Column#|SiteColumnOWSTEXT|

> [!NOTE]
> The following Unicode code blocks are considered non-supported characters: Unicode 0000-0021, Unicode 0080 - 00a1, Unicode 2000 - 2070, Unicode ff00 ff10, and Unicode ff1a ff20.

## Default site columns for the Product Catalog content type
<a name="BKMK_DefaultSiteColumns"> </a>

The Product Catalog list in the Product Catalog site collection has six default site columns associated with its content type. The following table shows the names for these site columns and the names for their crawled properties and managed properties.

**Automatically created crawled property names and managed property names for site columns that belong to the Product Catalog content type**

|Site column name|Crawled property name|Managed property name|
|:-----|:-----|:-----|
|Title|Title|Title|
|Item Number|ows_q_TEXT_ProductCatalogItemNumber|ProductCatalogItemNumberOWSTEXT|
|Group Number|ows_q_TEXT_ProductCatalogGroupNumber|ProductCatalogGroupNumberOWSTEXT|
|Language Tag|ows_q_CHCS_ProductCatalogLanguageTag|ProductCatalogLanguageTagOWSCHCS|
|Item Category|ows_taxId_ProductCatalogItemCategory|owstaxIdProductCatalogItemCategory|
|Rollup Image|ows_r_IMGE_PublishingRollupImage|PublishingImage|
