---
title: "Configure refiners and faceted navigation in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/11/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: b12bff2c-0486-41e2-be81-d0a8122ed1f9
description: "Learn how to map a crawled property to a refinable managed property, enable a managed property as a refiner, and configure refiners for faceted navigation."
---

# Configure refiners and faceted navigation in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]

You can add refiners to a page to help users quickly browse to specific content. Refiners are based on managed properties from the search index. To use managed properties as refiners, the managed properties must be enabled as refiners, or crawled properties must be mapped to managed properties that are enabled as refiners.
  
Faceted navigation is the process of browsing for content by filtering on refiners that are tied to category pages. Faceted navigation lets you specify different refiners for category pages, even when the underlying page displaying the categories is the same. For information about category pages, see "Category pages and catalog item pages" in [Overview of cross-site publishing in SharePoint Server](overview-of-cross-site-publishing.md).
  
> [!IMPORTANT]
> You can apply faceted navigation only to publishing sites that use [Overview of managed navigation in SharePoint Server](overview-of-managed-navigation.md), and for lists or libraries that have been [Share a library or list as a catalog](configure-cross-site-publishing.md#BKMK_Share_library_list_as_catalog). 
  
    
## Before you begin
<a name="BKMK_Before"> </a>

Review the information in "Plan refiners and faceted navigation" in [Plan search for cross-site publishing sites in SharePoint Server 2016](plan-search-for-sharepoint-cross-site-publishing-sites.md).
  
### About configuring refiners for different data types

When a catalog is crawled, SharePoint Server automatically creates managed properties for all site columns that contain values. These automatically created managed properties use the Text data type. To make sure that refiners that use the Number, Currency, Integer, and Date and Time data types are displayed in the correct format, you can do one of the following:
  
1. Use the procedure that is described in [Map a crawled property to a refinable managed property in SharePoint site collection administration](configure-refiners-and-faceted-navigation.md#BKMK_MapCPtoRefinableMP). This procedure can be performed by site collection administrators. We recommend that you use this procedure for all data types. 
    
2. Create a managed property, add the type code to the property name, and then enable it as a refiner. This procedure can only be performed by an administrator of the Search service application. 
    
3. Add JavaScript to the page where the refiners are displayed. For more information, see [Add JavaScript to a page to display refiners in the correct format ](configure-refiners-and-faceted-navigation.md#BKMK_AddJavaScript).
    
## Map a crawled property to a refinable managed property in SharePoint site collection administration
<a name="BKMK_MapCPtoRefinableMP"> </a>

Site collection administrators can configure refiners because the search schema has many managed properties that are enabled as refiners by default. These managed properties are listed in the following table. Before site collection administrators can use these managed properties as refiners on their web pages, they must map the appropriate crawled property to the managed property that is enabled as a refiner. To make it easier to work with these properties when doing additional refiner configuration in Term Store Management, you can specify a user-friendly alias name for the managed property.
  
For an overview of managed properties that are enabled as refiners by default, see [Managed properties that are enabled as refiners by default](configure-refiners-and-faceted-navigation.md#BKMK_DefaultRefiners).
  
> [!NOTE]
> This procedure is performed on the authoring site collection. 
  
 **To map a crawled property to a refinable managed property**
  
1. Verify that the user account that performs this procedure is a site collection administrator on the authoring site collection.
    
2. On the authoring site collection, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Collection Administration** section, click **Search Schema**.
    
4. On the **Managed Properties** page, in the **Managed property** filter box, type the name of a refinable managed property — for example, RefinableString00 — and then click the arrow. 
    
5. In the **Property Name** column, click the refinable managed property that you want to edit. 
    
6. To specify an alias of the refinable managed property to use when you configure refiners for faceted navigation, on the **Edit Managed Property** page, type a user-friendly name in the **Alias** box. 
    
    > [!IMPORTANT]
    > For properties that use the data type Managed Metadata, the alias must consist of the type code,  *owstaxId*  , followed by the property name. For example, for a property named  *Color*  that uses the Managed Metadata data type, the alias for the refinable managed property must be  *owstaxIdColor*  . 
  
7. In the **Mappings to crawled properties** section, click **Add a Mapping**.
    
8. In the **Crawled property selection** dialog box, find the crawled property that you want to map to the refinable managed property in the list, or search for it by typing the name of the crawled property in the box, and then clicking **Find**.
    
    > [!IMPORTANT]
    > When you search for a crawled property, you may find two crawled properties that represent the same content. For example, a site column of type Text named  *Color*  will during crawl discover two crawled properties:  *ows_Color*  and  *ows_q_TEXT_Color*  . Crawled properties that begin with either  *ows_r\<four letter code\>*  ,  *ows_q\<four letter code\>*  , or  *ows_taxId*  are automatically created crawled properties. When you select a crawled property to map to a refinable managed property, make sure that you don't map the automatically created crawled property. Instead, always map the crawled property that begins with  *ows_*  . > For more information about automatically created crawled properties, see [Automatically created managed properties in SharePoint Server](../technical-reference/automatically-created-managed-properties-in-sharepoint.md). 
  
9. Click **OK**.
    
10. On the **Edit Managed Property** page, click **OK**.
    
> [!NOTE]
> To configure refiners in Web Parts or in Term Store Management, you must start a full crawl of the content source that contains the refinable managed properties. For more information, see [Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search). 
  
## Enable automatically created managed properties as refiners in SharePoint Central Administration
<a name="BKMK_EnableInCA"> </a>

All automatically created managed properties use the Text data type. To make sure that the refiners are displayed in the correct format, you should only enable an automatically created managed property as a refiner if it is based on a site column that uses the data type Text, Managed Metadata, or Person or Group. For other data types, you must create a managed property, add the type code to the property name, and enable the managed property as a refiner.
  
For more information about automatically created managed properties, see [Automatically created managed properties in SharePoint Server](../technical-reference/automatically-created-managed-properties-in-sharepoint.md).
  
 **To enable an automatically created managed property as a refiner**
  
1. Verify that the user account that performs this procedure is an administrator of the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. On the **Manage Service Applications** page, click the Search service application in which you want to enable the managed property as a refiner. 
    
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
5. On the **Managed Properties** page, in the **Managed property** filter box, type the name of the managed property that you want to enable as refiner, and then click the arrow. 
    
6. In the **Property Name** column, click the managed property that you want to edit. 
    
7. On the **Edit Managed Property** page, in the **Refinable** section, select either **Yes - active** or **Yes - latent**. If you select **Yes - latent**, you can switch the refiner to active later without having to do a full crawl.
    
8. Click **OK**.
    
> [!NOTE]
> To configure refiners in Web Parts or in Term Store Management, you must complete a full crawl of the content source that contains the refinable managed properties. For more information, see [Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search). 
  
 **To create a managed property, add type code to the name, and enable a managed property as a refiner**
  
1. Verify that the user account that performs this procedure is an administrator of the Search service application.
    
2. In Central Administration, in the **Application Management** section, click **Manage service applications**.
    
3. On the **Manage Service Applications** page, click the Search service application in which you want to create a managed property. 
    
4. On the Search Administration page, in the Quick Launch, under **Queries and Results**, click **Search Schema**.
    
5. On the **Managed Properties** page, click **New Managed Property**.
    
6. On the **New Managed Property** page, in the **Property name** box, in the **Name and description** section, type the name of the new managed property, followed by the appropriate type code. For an overview of type codes, see [Type codes](configure-refiners-and-faceted-navigation.md#BKMK_TypeCodes).
    
7. In the **Type** section, select the appropriate data type. 
    
8. In the **Main characteristics** section, set the following selections: 
    
  - **Queryable**
    
  - **Refinable: Yes - active** or **Yes - latent**
    
    You can also specify additional settings in this section.
    
9. In the **Mappings to crawled properties** section, click **Add a mapping**.
    
10. In the **Crawled property selection** dialog box, find the crawled property that you want to map to the managed property in the list, or search for it by typing the name of the crawled property in the box, and then clicking **Find**.
    
    > [!IMPORTANT]
    > When you search for a crawled property, you may find two crawled properties that represent the same content. For example, a site column of type Date and Time named  *Created*  will during crawl discover two crawled properties:  *ows_Created*  and  *ows_q_DATE_Created*  . Crawled properties that begin with either  *ows_r\<four letter code\>,*  *ows_q\<four letter code\>*  or  *ows_taxId*  are automatically created crawled properties. When you select a crawled property to map to a managed property, make sure that you don't map the automatically created crawled property. Instead, always map the crawled property that begins with  *ows_.* 
  
11. Click **OK**.
    
> [!NOTE]
> To configure refiners in Web Parts or in Term Store Management, you must complete a full crawl of the content source that contains the refinable managed properties. For more information, see [Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search). 
  
## Configure refiners for faceted navigation
<a name="BKMK_EnableInCA"> </a>

Before you start the procedures in this section, verify the following:
  
- On the authoring site, a library or list is shared as a catalog, as described in [Share a library or list as a catalog](configure-cross-site-publishing.md#BKMK_Share_library_list_as_catalog).
    
- The required managed properties are enabled as refiners, as described in [Map a crawled property to a refinable managed property in SharePoint site collection administration](configure-refiners-and-faceted-navigation.md#BKMK_MapCPtoRefinableMP) and [Enable automatically created managed properties as refiners in SharePoint Central Administration](configure-refiners-and-faceted-navigation.md#BKMK_EnableInCA).
    
- A full crawl was completed for the content source that contains the refinable managed properties, as described in [Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search).
    
### Enable a term set for faceted navigation
<a name="BKMK_EnableATermSetForFacetedNavigation"> </a>

To configure refiners for faceted navigation, you must first enable the relevant term set for faceted navigation. This procedure is performed on the authoring site collection.
  
 **To enable a term set for faceted navigation**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the authoring site collection.
    
2. On the authoring site collection, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.
    
4. In the **TAXONOMY TERM STORE** section, click to select the term set that you want to enable for faceted navigation. 
    
5. Click the **INTENDED USE** tab, and then select **Use this Term Set for Faceted Navigation**.
    
6. Click **Save**.
    
### Add refiners to a term set
<a name="BKMK_AddRefinersToATermSet"> </a>

When configuring refiners for faceted navigation, you can add refiners to all terms in a term set or to specific terms in a term set. This procedure is performed on the authoring site collection.
  
 **To add refiners to all terms in a term set**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the authoring site collection. 
    
2. On the authoring site collection, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.
    
4. In the **TAXONOMY TERM STORE** section, click the term set that you have enabled for faceted navigation. 
    
5. Click the **FACETED NAVIGATION** tab, and then click **Customize refiners**.
    
6. On the **Refinement Configuration** page, in the **Available refiners** section, use the buttons to select which refiners should be added to the term set, and also to specify the order in which you want the refiners to appear. If you have specified an alias for a refinable managed property, this alias is displayed in the **Configuration** section. 
    
7. In the **Configuration for** section, specify how you want each refiner to appear. 
    
8. Click **OK** to close the **Refinement Configuration** page, and then click **Save**.
    
 **To add refiners to specific terms in a term set**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the authoring site collection.
    
2. On the authoring site collection, on the **Settings** menu, click **Site settings**.
    
3. On the **Site Settings** page, in the **Site Administration** section, click **Term store management**.
    
4. In the **TAXONOMY TERM STORE** section, click the term set that you have enabled for faceted navigation, and then click the term to which you want to add term-specific refiners. 
    
5. Click the **FACETED NAVIGATION** tab, and then click **Stop inheriting**.
    
6. Click **FACETED NAVIGATION** tab, and then click **Customize refiners**.
    
7. On the **Refinement Configuration** page, in the **Available refiners** section, use the buttons to select which refiners should be added to the term set, and also to specify the order in which you want the refiners to appear. If you have specified an alias for a refinable managed property, this alias is displayed in the **Configuration** section. 
    
8. In the **Configuration for** section, specify how you want each refiner to appear. 
    
9. Click **OK** to close the **Refinement Configuration** page, and then click **Save**.
    
### Set intervals for refiner values
<a name="BKMK_SetIntervalsForRefinerValues"> </a>

For refiners that contain numeric values, you can present the numeric values within different intervals. For example, if you want end-users to be able to refine based on price, it would be useful to specify different price ranges instead of showing all available prices as separate refiners. This procedure is performed in the authoring site collection.
  
 **To set ranges for refiner values**
  
1. Add refiners to a term set as described in [Add refiners to a term set](configure-refiners-and-faceted-navigation.md#BKMK_AddRefinersToATermSet) earlier in this article. 
    
2. On the **Refinement Configuration** page, in the **Selected refiners** section, click the refiner that you want to set ranges for. 
    
3. In the **Configuration for** section, for **Intervals**, select **Custom**, and then type the ranges in the **Thresholds** box. 
    
4. Click **OK** to close the **Refinement Configuration** page, and then click **Save**.
    
### Additional steps
<a name="BKMK_SetIntervalsForRefinerValues"> </a>

To show refiners on a page, you must add a Refinement Panel Web Part to the page where you want the refiners to appear. For more information, see [Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md).
  
## Add JavaScript to a page to display refiners in the correct format
<a name="BKMK_AddJavaScript"> </a>

To make sure that refiners that use the Number, Currency, Integer, and Date and Time data types are displayed in the correct format, you can add JavaScript to the page where the refiners are displayed. You can add the JavaScript by adding a **Content Editor Web Part**, which you then hide from being displayed on the page.
  
Note that there are two methods depending on whether you are using the default display template, **Filter_Default**, or another display template in your Refinement Web Part.
  
 **To add JavaScript to a page to display refiners in the correct format when you are using the default display template**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where the refiners are displayed.
    
3. Click the **Settings** menu, and then click **Edit page**.
    
4. In a Web Part Zone, click **Add a Web Part**.
    
5. In the **Categories** list, click **Media and Content**.
    
6. In the **Parts** list, click **Content Editor**, and then click **Add**.
    
7. In the Web Part, click **Click here to add new content**, and type one of the following two code strings:
    
  ```
  # To ensure correct refiner formatting by using type code:
  Srch.ValueInfo.overrideRenderingForProperty( "<ManagedPropertyName>", "Property<TypeCode>" );
  # To ensure correct refiner formatting by using a managed properties that is enabled as a refiner by default:
  Srch.ValueInfo.overrideRenderingForProperty("<ManagedPropertyName>", "<DefaultRefinableManagedProperty>");
  ```

    Where:
    
  -  *\<ManagedPropertyName\>*  is the name of the managed property that is enabled as a refiner, for example  *CreatedOWSDATE*  . 
    
  - <TypeCode> is a seven letter code indicating the data type, for example  *OWSDATE*  . For an overview of type codes, see [Type codes](configure-refiners-and-faceted-navigation.md#BKMK_TypeCodes).
    
  - <DefaultRefinableManagedProperty> is the name of a managed property that is enabled as a refiner by default, for example  *RefinableDate00*  . For an overview of managed properties that are enabled as refiners by default, see [Managed properties that are enabled as refiners by default](configure-refiners-and-faceted-navigation.md#BKMK_DefaultRefiners).
    
8. In the Web Part, click the **Content Editor Web Part Menu** arrow, and then click **Edit Web Part**.
    
9. In the Web Part tool pane, expand the **Layout** section, and then select the check box **Hidden**.
    
10. Click **OK**.
    
 **To add JavaScript to a page to display refiners in the correct format when you are not using the default display template**
  
1. Verify that the user account that performs this procedure is a member of the Designers SharePoint group on the publishing site collection.
    
2. Browse to the page where the refiners are displayed.
    
3. Click the **Settings** menu, and then click **Edit page**.
    
4. In a Web Part Zone, click **Add a Web Part**.
    
5. In the **Categories** list, click **Media and Content**.
    
6. In the **Parts** list, click **Content Editor**, and then click **Add**.
    
7. In the Web Part, click **Click here to add new content**, and then type the following code strings:
    
  ```
  # To ensure correct refiner formatting by using type code:
  Srch.ValueInfo.overrideRefinementTemplateForProperty("<ManagedPropertyName>", "Property<TypeCode>", "~sitecollection/<PathToDisplayTemplate>" );
  # To ensure correct refiner formatting by using a managed properties that is enabled as a refiner by default:
  Srch.ValueInfo.overrideRefinementTemplateForProperty("<ManagedPropertyName>", "<DefaultRefinableManagedProperty>", "~sitecollection/<PathToDisplayTemplate>" );
  
  ```

    Where:
    
  -  *\<ManagedPropertyName\>*  is the name of the managed property that is enabled as a refiner, for example  *CreatedOWSDATE*  . 
    
  - <TypeCode> is a seven letter code indicating the data type, for example  *OWSDATE*  . For an overview of type codes, see [Type codes](configure-refiners-and-faceted-navigation.md#BKMK_TypeCodes).
    
  - <DefaultRefinableManagedProperty> is the name of a managed property that is enabled as a refiner by default, for example  *RefinableDate00*  . For an overview of managed properties that are enabled as refiners by default, see [Managed properties that are enabled as refiners by default](configure-refiners-and-faceted-navigation.md#BKMK_DefaultRefiners).
    
  -  *\<PathToDisplayTemplate\>*  is the path of the display template that you are using in the Refinement Web Part, for example  *catalogs\masterpage\Display Templates\Filters\MyDisplayTemplate.js*  . 
    
8. In the Web Part, click the **Content Editor Web Part Menu** arrow, and then click **Edit Web Part**.
    
9. In the Web Part tool pane, expand the **Layout** section, and then select the check box **Hidden**.
    
10. Click **OK**.
    
## Reference tables
<a name="BKMK_RefTables"> </a>

### Managed properties that are enabled as refiners by default
<a name="BKMK_DefaultRefiners"> </a>

****

|**Managed property name**|**Data type for mapping.**|
|:-----|:-----|
|RefinableDate00 - RefinableDate19  <br/> |Values contain dates.  <br/> |
|RefinableDecimal00 - RefinableDecimal09  <br/> |Values contain numbers with maximum three decimals.  <br/> |
|RefinableDouble00 - RefinableDouble09  <br/> |Values contain numbers with more than three decimals.  <br/> |
|RefinableInt00 - RefinableInt49  <br/> |Values are whole numbers.  <br/> |
|RefinableString00 - RefinableString99  <br/> |Values are strings. This includes values that use the data type Text, Person or Group, Managed Metadata, Choice and Yes/No  <br/> |
   
### Type codes
<a name="BKMK_TypeCodes"> </a>

|**Site column type**|**Type code**|**Example of managed property name with type code**|
|:-----|:-----|:-----|
|Number  <br/> |OWSNMBR  <br/> |ManagedPropertyNameOWSNMBR  <br/> |
|Currency  <br/> |OWSCURR  <br/> |ManagedPropertyNameOWSCURR  <br/> |
|Date and Time  <br/> |OWSDATE  <br/> |ManagedPropertyNameOWSDATE  <br/> |
|Integer\*  <br/> |OWSINTG  <br/> |ManagedPropertyNameOWSINTG  <br/> |
   
\*Column creation not available through user interface.
  
## See also
<a name="BKMK_RefTables"> </a>

#### Concepts

[Automatically created managed properties in SharePoint Server](../technical-reference/automatically-created-managed-properties-in-sharepoint.md)
  
[Configure Search Web Parts in SharePoint Server](configure-search-web-parts.md)
#### Other Resources

[Blog post: Configure refiners for faceted navigation](https://blogs.technet.com/b/tothesharepoint/archive/2013/06/19/stage-14-configure-refiners-for-faceted-navigation.aspx)
  
[Configure search for cross-site publishing](configure-cross-site-publishing.md#BKMK_Configure_search)

