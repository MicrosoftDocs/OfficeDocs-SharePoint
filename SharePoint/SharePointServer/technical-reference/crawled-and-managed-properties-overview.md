---
title: "Overview of crawled and managed properties in SharePoint Server"
ms.author: tlarsen
author: tklarsen
manager: pamgreen
ms.date: 9/8/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 6710f7e9-889d-4644-bfab-26f63b76ceaf
description: "Learn about the default managed properties, their settings and the default mapping between crawled and managed properties."
---

# Overview of crawled and managed properties in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
A  *crawled property*  is content and metadata that is extracted from an item, such as a document or a URL, during a crawl. A crawled property can be an author, title, or subject. To include the content and metadata of crawled properties in the search index, you map crawled properties to managed properties. Managed properties can have a large number of settings, or attributes. These attributes determine how the contents are shown in search results. The search schema contains the attributes on managed properties and the mapping between crawled properties and managed properties. For more information, see [Overview of the search schema in SharePoint Server](../search/search-schema-overview.md) and [Manage the search schema in SharePoint Server](../search/manage-the-search-schema.md).
  
## Managed properties overview

The following table lists the default managed properties and their attributes. For each managed property that by default is mapped to one or several crawled properties, these crawled properties are listed in the **Mapped Crawled Properties** column. 
  
|||||||||||
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|**Property name** <br/> |**Type** <br/> |**Multi-valued** <br/> |**Queryable** <br/> |**Searchable** <br/> |**Retrievable** <br/> |**Refinable** <br/> |**Sortable** <br/> |**Mapped crawled properties** <br/> |**Aliases** <br/> |
|AboutMe  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:AboutMe, ows_Notes  <br/> ||
|Account  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Name  <br/> ||
|AccountName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:AccountName  <br/> ||
|acronym  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|acronymaggre  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|acronymexpansion  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|acronymexpansionaggre  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|AnchorText  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Basic:28  <br/> ||
|AssignedTo  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_AssignedTo, ows_Assigned_x0020_To  <br/> ||
|AttachmentDescription  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_MediaLinkDescription  <br/> ||
|AttachmentType  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_MediaLinkType  <br/> ||
|AttachmentURI  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_MediaLinkURI  <br/> ||
|Author  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |MetadataExtractorAuthor, Author, MailFrom, Mail:6  <br/> |DocAuthor, urn:schemas-microsoft-com:office:office#Author  <br/> |
|BaseOfficeLocation  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |People:SPS-Location  <br/> ||
|BasicScope  <br/> |Binary Data  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|body  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|CategoryNavigationUrl  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Basic:CategoryUrlNavigation  <br/> ||
|CCAMetadata  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|charset  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|clickdistance  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |||
|CollapsingStatus  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Colleagues  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |People:Colleagues  <br/> ||
|CombinedName  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:CombinedName  <br/> ||
|CombinedUserProfileNames  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |||
|companies  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|contentclass  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |DAV:contentclass, DAV:contentclass, DAV:contentclass  <br/> |DAV:contentclass  <br/> |
|ContentModifiedTime  <br/> |Date and Time  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Contents  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |ows_VideoSetDescription, ows_DocumentSetDescription, Basic:19  <br/> ||
|ContentsHidden  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |People:SPS-Location, People:Office, People:SPS-PastProjects  <br/> ||
|ContentSource  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ContentType  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Basic:5, ows_ContentType  <br/> |MimeType, DAV:getcontenttype  <br/> |
|ContentTypeId  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_ContentTypeId  <br/> ||
|Created  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Office:12, Basic:15  <br/> |DocCreatedTm, urn:schemas-microsoft-com:office:office#Created, DAV:creationdate  <br/> |
|CreatedBy  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Created_x0020_By  <br/> ||
|Date00  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date01  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date02  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date03  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date04  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date05  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date06  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date07  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date08  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Date09  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal00  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal01  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal02  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal03  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal04  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal05  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal06  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal07  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal08  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Decimal09  <br/> |Decimal  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|deeplinks  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|def  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|defaggre  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|DefaultEncodingURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_VideoSetDefaultEncoding, ows_EncodedAbsUrl  <br/> ||
|definitioncontent  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|definitioncontentaggre  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Department  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |People:Department, ows_Department  <br/> |urn:schemas-microsoft-com:sharepoint:portal:profile:Department  <br/> |
|Description  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Description, Office:6, DESCRIPTION  <br/> |urn:schemas.microsoft.com:fulltextqueryinfo:description  <br/> |
|DetectedLanguage  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_q_TEXT_TranslationLanguage  <br/> ||
|DetectedLanguageRanking  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |||
|DiscoveredTime  <br/> |Date and Time  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|DisplayAuthor  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |||
|DisplayDate  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ImageCreateDate, ows_Image_x0020_CreateDate  <br/> |DatePictureTaken, ImageCreateDate  <br/> |
|DMSDocAccessRight  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |ows_DMSDocAccessRight  <br/> ||
|DMSDocAuthor  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |ows_DMSDocAuthor  <br/> ||
|DMSDocTitle  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |ows_DMSDocTitle  <br/> ||
|DMSLeaseTerm  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_DMSLeaseTerm  <br/> ||
|docacl  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|docaclmeta  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|DocComments  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Description, Office:6  <br/> ||
|DocId  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows__dlc_DocId  <br/> ||
|DocKeywords  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Office:5  <br/> |urn:schemas-microsoft-com:office:office#Keywords  <br/> |
|docrank  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|DocSignature  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Basic:6  <br/> |urn:schemas.microsoft.com:fulltextqueryinfo:docsignature  <br/> |
|DocSubject  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Subject, Office:3  <br/> ||
|DocumentSignature  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|DocumentSummary  <br/> |Binary Data  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|DocumentSummarySize  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|docvector  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|domain  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Double00  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double01  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double02  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double03  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double04  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double05  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double06  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double07  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double08  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Double09  <br/> |Double precision float  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|DuplicateHash  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Duplicates  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|EduAssignmentCategory  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_EduAssignmentCategory  <br/> ||
|EduAssignmentFormat  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_EduAssignmentFormat  <br/> ||
|EduEntityId  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_EduEntityId  <br/> ||
|EduMaximumScore  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_EduMaximumScore  <br/> ||
|EndDate  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_End_x0020_Date  <br/> ||
|EventRate  <br/> |Double precision float  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |||
|ExcludeFromSummary  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |EmbeddedContent, LINK.OFFICECHILD, Description  <br/> ||
|ExpirationTime  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |ows_Announcement_x0020_Expires, ows_Expires  <br/> ||
|ExternalMediaURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_VideoSetExternalLink  <br/> ||
|ExtractedAuthor  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ExtractedDate  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|fcocount  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|FileExtension  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |FileExtension, ows_File_x0020_Type, ows_FileType  <br/> ||
|Filename  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Basic:10  <br/> |DAV:displayname  <br/> |
|FileType  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |FileType  <br/> ||
|FirstLevelColleagues  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|FirstLevelMutualFollowings  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|FirstName  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |People:FirstName, People:SPS-PhoneticFirstName  <br/> ||
|FollowAllAnchor  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Basic:31  <br/> ||
|format  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |||
|FullPostBody  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SearchContent  <br/> ||
|FullPostTitle  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SearchTitle  <br/> ||
|GeneratedTitle  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Genre  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|HierarchyUrl  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:ProfileHierarchyViewUrl  <br/> ||
|HitHighlightedProperties  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|HitHighlightedSummary  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|HostingPartition  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |||
|hwboost  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |||
|ImageDateCreated  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ImageCreateDate, ows_Image_x0020_CreateDate  <br/> ||
|importance  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|Int00  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int01  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int02  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int03  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int04  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int05  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int06  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int07  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int08  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int09  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int10  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int11  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int12  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int13  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int14  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int15  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int16  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int17  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int18  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int19  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int20  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int21  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int22  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int23  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int24  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int25  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int26  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int27  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int28  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int29  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int30  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int31  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int32  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int33  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int34  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int35  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int36  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int37  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int38  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int39  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int40  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int41  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int42  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int43  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int44  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int45  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int46  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int47  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int48  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Int49  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Interests  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-Interests  <br/> ||
|InternalFileType  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|IsContainer  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Basic:7  <br/> ||
|IsData  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_IsData, IsData  <br/> ||
|IsDefaultView  <br/> |Yes/No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_IsDefaultView  <br/> ||
|IsDocument  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |SharePoint:isdocument, SharePoint:isdocument, Basic:22  <br/> |urn:schemas.microsoft.com:sharepoint:portal:isdocument  <br/> |
|IsEmptyList  <br/> |Yes/No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_IsEmptyList  <br/> ||
|IsListItem  <br/> |Yes/No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_isItem  <br/> ||
|IsMyDocuments  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_IsMyDocuments  <br/> ||
|IsPublishingCatalog  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |IsPublishingCatalog  <br/> ||
|IsReport  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_IsReport, IsReport  <br/> ||
|ItemCategoryText  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |ProductCatalogItemCategory  <br/> ||
|JobTitle  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |People:SPS-JobTitle, People:Title, ows_JobTitle  <br/> |urn:schemas-microsoft-com:sharepoint:portal:profile:Title  <br/> |
|Keywords  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Keywords  <br/> ||
|language  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ProductCatalogLanguageTag  <br/> ||
|languages  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |||
|LastAnalyticsUpdateTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|LastModifiedTime  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |LastSavedDateTime, Basic:14, Basic:16  <br/> |Write, FileWrite, DAV:getlastmodified  <br/> |
|LastName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:LastName, People:SPS-PhoneticLastName  <br/> ||
|LevelsToTop  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |People:LevelsToTop  <br/> ||
|LikesCount  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_LikesCount  <br/> ||
|ListID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ListID  <br/> ||
|ListItemID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ListItemID  <br/> ||
|ListUrl  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ListUrl  <br/> ||
|Location  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_Location  <br/> ||
|ManagedProperties  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |||
|MediaDuration  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_MediaLengthInSeconds  <br/> ||
|Memberships  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:QuickLinks  <br/> ||
|MetadataAuthor  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Author, MailFrom, Mail:6  <br/> ||
|MicroBlogType  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_MicroBlogType  <br/> ||
|MobilePhone  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:CellPhone, ows_CellPhone, ows_Cell_x0020_Phone  <br/> ||
|ModifiedBy  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |ows_ModifiedBy, ows_Modified_x0020_By, LastModifiedBy  <br/> ||
|NLCodePage  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Web:4  <br/> ||
|Notes  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Note, ows_Notes  <br/> ||
|NumItemsInCollection  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|OfficeNumber  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:Office  <br/> ||
|OrgNames  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:OrganizationNames, ows_Company  <br/> |Company  <br/> |
|OrgParentNames  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:OrganizationParentNames  <br/> ||
|OrgParentUrls  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:OrganizationParentURLs  <br/> ||
|OrgUrls  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:OrganizationURLs  <br/> ||
|OriginalPath  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Basic:11, Basic:9, Web:2  <br/> ||
|OWS_ItemURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|OWS_URL  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |ows_URL  <br/> ||
|owsmetadatafacetinfo  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_MetadataFacetInfo  <br/> ||
|owstaxidmetadataalltagsinfo  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_taxId_MetadataAllTagsInfo  <br/> ||
|owstaxIdProductCatalogItemCategory  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_taxId_ProductCatalogItemCategory  <br/> ||
|ParentLink  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ParentURL  <br/> ||
|PastProjects  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-PastProjects  <br/> ||
|Path  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Basic:11, Basic:9, Web:2  <br/> |DAV:href, VPath, DocAddress, ...  <br/> |
|People  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_People, Author, MailFrom  <br/> ||
|PeopleInMedia  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_PeopleInMedia  <br/> ||
|PeopleKeywords  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |People:SPS-Responsibility, People:SPS-Skills, People:SPS-Interests  <br/> ||
|PhoneNumber  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|PictureHeight  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ImageHeight, ows_VideoHeightInPixels  <br/> |ImageHeight, urn:schemas-microsoft-com:office:office#ows_ImageHeight  <br/> |
|PictureThumbnailURL  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_AlternateThumbnailUrl, ows_EncodedAbsThumbnailUrl, ows_DMSCoverImage  <br/> ||
|PictureURL  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_PictureURL, People:PictureURL  <br/> |urn:schemas.microsoft.com:fulltextqueryinfo:PictureURL  <br/> |
|PictureWidth  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ImageWidth, ows_VideoWidthInPixels  <br/> |ImageWidth, urn:schemas-microsoft-com:office:office#ows_ImageWidth  <br/> |
|PopularSocialTags  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|PostAuthor  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_PostAuthor  <br/> ||
|PreferredName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:PreferredName  <br/> |urn:schemas-microsoft-com:sharepoint:portal:profile:PreferredName  <br/> |
|Priority  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Priority  <br/> ||
|PrivateColleagues  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |People:ColleaguesNonPublic  <br/> ||
|processingtime  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|ProductCatalogGroupNumberOWSTEXT  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |ows_ProductCatalogGroupNumber  <br/> ||
|ProfileExpertise  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |People:SPS-Responsibility, People:SPS-PastProjects, People:SPS-Skills  <br/> ||
|ProfileName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |People:PreferredName, People:FirstName, People:LastName  <br/> ||
|Pronunciations  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:FirstName, People:LastName, People:PreferredName  <br/> ||
|PublishingCatalogSettings  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |PublishingCatalogSettings  <br/> ||
|PublishingImage  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Purpose  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |ows_Purpose  <br/> ||
|QueryTerms  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Rank  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |urn:schemas.microsoft.com:fulltextqueryinfo:rank  <br/> ||
|RankDetail  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|RankingWeightHigh  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |People:OrganizationNames, People:Department  <br/> ||
|RankingWeightLow  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |People:SPS-Skills, People:SPS-Interests  <br/> ||
|RankingWeightName  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |People:CombinedName, People:UserName, People:WorkEmail  <br/> ||
|Rating  <br/> |Double precision float  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|recommendedfor  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |||
|RecsClickedLifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|RecsClickedRecent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|RefinableDate00  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate01  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate02  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate03  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate04  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate05  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate06  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate07  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate08  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate09  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate10  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate11  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate12  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate13  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate14  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate15  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate16  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate17  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate18  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDate19  <br/> |Date and Time  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal00  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal01  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal02  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal03  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal04  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal05  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal06  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal07  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal08  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDecimal09  <br/> |Decimal  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble00  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble01  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble02  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble03  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble04  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble05  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble06  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble07  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble08  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableDouble09  <br/> |Double precision float  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt00  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt01  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt02  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt03  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt04  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt05  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt06  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt07  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt08  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt09  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt10  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt11  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt12  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt13  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt14  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt15  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt16  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt17  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt18  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt19  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt20  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt21  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt22  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt23  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt24  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt25  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt26  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt27  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt28  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt29  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt30  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt31  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt32  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt33  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt34  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt35  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt36  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt37  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt38  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt39  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt40  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt41  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt42  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt43  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt44  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt45  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt46  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt47  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt48  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableInt49  <br/> |Integer  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString00  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString01  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString02  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString03  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString04  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString05  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString06  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString07  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString08  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString09  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString10  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString11  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString12  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString13  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString14  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString15  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString16  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString17  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString18  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString19  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString20  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString21  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString22  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString23  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString24  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString25  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString26  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString27  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString28  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString29  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString30  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString31  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString32  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString33  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString34  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString35  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString36  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString37  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString38  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString39  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString40  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString41  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString42  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString43  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString44  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString45  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString46  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString47  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString48  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString49  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString50  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString51  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString52  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString53  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString54  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString55  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString56  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString57  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString58  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString59  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString60  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString61  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString62  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString63  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString64  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString65  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString66  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString67  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString68  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString69  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString70  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString71  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString72  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString73  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString74  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString75  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString76  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString77  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString78  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString79  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString80  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString81  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString82  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString83  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString84  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString85  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString86  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString87  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString88  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString89  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString90  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString91  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString92  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString93  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString94  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString95  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString96  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString97  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString98  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|RefinableString99  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|ReplyCount  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ReplyCount  <br/> ||
|Responsibilities  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |People:SPS-Responsibility  <br/> |Responsibility  <br/> |
|RobotsNoIndex  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |ows_RobotsNoIndex  <br/> ||
|RootPostID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_RootPostID  <br/> ||
|RootPostOwnerID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_RootPostOwnerID  <br/> ||
|RootPostUniqueID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_RootPostUniqueID  <br/> ||
|Schools  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-School  <br/> ||
|SecondaryFileExtension  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_FileType, ows_File_x0020_Type  <br/> ||
|SecondLevelColleagues  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SectionIndexes  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SectionNames  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ServerRedirectedEmbedURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ServerRedirectedEmbedUrl  <br/> ||
|ServerRedirectedPreviewURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ServerRedirectedPreviewUrl  <br/> ||
|ServerRedirectedURL  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ServerRedirectedUrl  <br/> ||
|ServiceApplicationID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SharedWithInternal  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_SharedWithInternal  <br/> ||
|SipAddress  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-SipAddress  <br/> ||
|Site  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |urn:schemas.microsoft.com:fulltextqueryinfo:sitename  <br/> ||
|SiteClosed  <br/> |Yes/No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|SiteDescription  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SiteDescription  <br/> ||
|SiteID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SiteID  <br/> ||
|SiteLogo  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |LogoURL  <br/> ||
|SitemapChangeFrequency  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SitemapPriority  <br/> |Double precision float  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SiteMembers  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|sitename  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |||
|SiteOwners  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|siterank  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |||
|SiteTitle  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SiteName  <br/> |urn:schemas-microsoft-com:office:office#ows_SiteName  <br/> |
|Size  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |Basic:12, ows_ImageSize  <br/> |DAV:getcontentlength, PictureSize, ImageSize  <br/> |
|Skills  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-Skills  <br/> ||
|SocialTag  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|SocialTagTextUrl  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |No  <br/> |People:SocialTagTextUrl  <br/> ||
|SPContentType  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |ows_ContentType  <br/> ||
|SpellingTerms  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|SPSiteURL  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |ows_SPSiteURL  <br/> ||
|SPVersion  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_SPVersion  <br/> ||
|StartDate  <br/> |Date and Time  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Start_x0020_date, ows_DMSReleaseDate  <br/> ||
|Status  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Issue_x0020_Status, ows_Task_x0020_Status  <br/> ||
|Tags  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_SearchTag1, ows_SearchTag2, ows_SearchTag3  <br/> ||
|teaser  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|Text1  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Text2  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Text3  <br/> |Text  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|Title  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |MetadataExtractorTitle, Office:2, ows_BaseName, Title  <br/> |DocTitle, urn:schemas.microsoft.com:fulltextqueryinfo:displaytitle  <br/> |
|tld  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|UniqueID  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_UniqueID  <br/> ||
|url  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_DMSDocAuthorURL  <br/> ||
|UrlDepth  <br/> |Integer  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|urlkeywords  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |No  <br/> |||
|urls  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|UsageAnalyticsId  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_ProductCatalogItemNumber  <br/> ||
|UsageEvent10LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent10Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent11LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent11Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent12LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent12Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent1LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent1Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent2LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent2Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent3LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent3Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent4LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent4Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent5LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent5Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent6LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent6Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent7LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent7Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent8LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent8Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent9LifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEvent9Recent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|UsageEventItemId  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |ows_ProductCatalogItemNumber  <br/> ||
|UserEncodingURL  <br/> |Text  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_VideoSetUserOverrideEncoding  <br/> ||
|UserName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:UserName, ows_FullName, ows_Full_x0020_Name  <br/> ||
|UserProfile_GUID  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:UserProfile_GUID  <br/> ||
|ViewsLast1Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast1DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast2Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast2DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast3Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast3DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast4Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast4DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast5Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast5DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast6Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast6DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast7Days  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLast7DaysUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths1  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths1Unique  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths2  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths2Unique  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths3  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLastMonths3Unique  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|ViewsLifeTime  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|ViewsLifeTimeUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|ViewsRecent  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|ViewsRecentUniqueUsers  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |||
|WebId  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_WebId  <br/> ||
|WebTemplate  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |WebTemplate  <br/> ||
|WeightedMemberships  <br/> |Text  <br/> |Yes  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:WeightedMemberships  <br/> ||
|WikiCategory  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |ows_Wiki_x0020_Page_x0020_Categories  <br/> ||
|WordCustomRefiner1  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordCustomRefiner2  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordCustomRefiner3  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordCustomRefiner4  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordCustomRefiner5  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordExactCustomRefiner  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartCustomRefiner1  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartCustomRefiner2  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartCustomRefiner3  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartCustomRefiner4  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartCustomRefiner5  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WordPartExactCustomRefiner  <br/> |Text  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |||
|WorkEmail  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |Yes  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:WorkEmail, ows_EMail, ows_EMail_x0020_  <br/> |urn:schemas-microsoft-com:sharepoint:portal:profile:WorkEmail  <br/> |
|WorkId  <br/> |Integer  <br/> |No  <br/> |No  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |||
|WorkPhone  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:WorkPhone, ows_WorkPhone, ows_Work_x0020_Phone  <br/> |urn:schemas-microsoft-com:sharepoint:portal:profile:WorkPhone  <br/> |
|YomiDisplayName  <br/> |Text  <br/> |No  <br/> |Yes  <br/> |No  <br/> |Yes  <br/> |No  <br/> |No  <br/> |People:SPS-PhoneticDisplayName  <br/> ||
   

