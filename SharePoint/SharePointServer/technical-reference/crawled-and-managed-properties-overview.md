---
title: "Overview of crawled and managed properties in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
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

### Managed properties in SharePoint Server 2013 through 2019
  
|||||||||||
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|**Property name**  |**Type**  |**Multi-valued**  |**Queryable**  |**Searchable**  |**Retrievable**  |**Refinable**  |**Sortable**  |**Mapped crawled properties**  |**Aliases**  |
|AboutMe   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:AboutMe, ows_Notes   ||
|Account   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Name   ||
|AccountName   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:AccountName   ||
|acronym   |Text   |No   |No   |No   |Yes   |No   |No   |||
|acronymaggre   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |||
|acronymexpansion   |Text   |No   |No   |No   |Yes   |No   |No   |||
|acronymexpansionaggre   |Text   |No   |No   |No   |Yes   |No   |No   |||
|AnchorText   |Text   |No   |No   |Yes   |No   |No   |No   |Basic:28   ||
|AssignedTo   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_AssignedTo, ows_Assigned_x0020_To   ||
|AttachmentDescription   |Text   |No   |No   |No   |Yes   |No   |No   |ows_MediaLinkDescription   ||
|AttachmentType   |Integer   |No   |Yes   |No   |Yes   |Yes   |No   |ows_MediaLinkType   ||
|AttachmentURI   |Text   |No   |No   |No   |Yes   |No   |No   |ows_MediaLinkURI   ||
|Author   |Text   |Yes   |Yes   |Yes   |Yes   |No   |Yes   |MetadataExtractorAuthor, Author, MailFrom, Mail:6   |DocAuthor, urn:schemas-microsoft-com:office:office#Author   |
|BaseOfficeLocation   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |People:SPS-Location   ||
|BasicScope   |Binary Data   |No   |No   |No   |Yes   |No   |No   |||
|body   |Text   |No   |No   |Yes   |No   |No   |No   |||
|CategoryNavigationUrl   |Text   |No   |Yes   |No   |No   |No   |No   |Basic:CategoryUrlNavigation   ||
|CCAMetadata   |Text   |No   |No   |No   |Yes   |No   |No   |||
|charset   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|clickdistance   |Integer   |No   |No   |No   |No   |No   |Yes   |||
|CollapsingStatus   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|Colleagues   |Text   |Yes   |Yes   |No   |No   |No   |No   |People:Colleagues   ||
|CombinedName   |Text   |Yes   |No   |Yes   |Yes   |No   |No   |People:CombinedName   ||
|CombinedUserProfileNames   |Text   |No   |Yes   |No   |No   |Yes   |No   |||
|companies   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|contentclass   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |DAV:contentclass, DAV:contentclass, DAV:contentclass   |DAV:contentclass   |
|ContentModifiedTime   |Date and Time   |No   |No   |No   |Yes   |No   |No   |||
|Contents   |Text   |No   |No   |Yes   |No   |No   |No   |ows_VideoSetDescription, ows_DocumentSetDescription, Basic:19   ||
|ContentsHidden   |Text   |Yes   |Yes   |Yes   |No   |No   |No   |People:SPS-Location, People:Office, People:SPS-PastProjects   ||
|ContentSource   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|ContentType   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |Basic:5, ows_ContentType   |MimeType, DAV:getcontenttype   |
|ContentTypeId   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |ows_ContentTypeId   ||
|Created   |Date and Time   |No   |Yes   |No   |Yes   |Yes   |Yes   |Office:12, Basic:15   |DocCreatedTm, urn:schemas-microsoft-com:office:office#Created, DAV:creationdate   |
|CreatedBy   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Created_x0020_By   ||
|Date00   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date01   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date02   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date03   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date04   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date05   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date06   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date07   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date08   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Date09   |Date and Time   |No   |Yes   |No   |No   |No   |No   |||
|Decimal00   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal01   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal02   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal03   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal04   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal05   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal06   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal07   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal08   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|Decimal09   |Decimal   |No   |Yes   |No   |No   |No   |No   |||
|deeplinks   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|def   |Text   |No   |No   |No   |Yes   |No   |No   |||
|defaggre   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |||
|DefaultEncodingURL   |Text   |No   |No   |No   |Yes   |No   |No   |ows_VideoSetDefaultEncoding, ows_EncodedAbsUrl   ||
|definitioncontent   |Text   |No   |No   |No   |Yes   |No   |No   |||
|definitioncontentaggre   |Text   |No   |No   |No   |Yes   |No   |No   |||
|Department   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |People:Department, ows_Department   |urn:schemas-microsoft-com:sharepoint:portal:profile:Department   |
|Description   |Text   |No   |Yes   |No   |Yes   |No   |No   |Description, Office:6, DESCRIPTION   |urn:schemas.microsoft.com:fulltextqueryinfo:description   |
|DetectedLanguage   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_q_TEXT_TranslationLanguage   ||
|DetectedLanguageRanking   |Integer   |No   |No   |No   |No   |No   |Yes   |||
|DiscoveredTime   |Date and Time   |No   |No   |No   |Yes   |No   |No   |||
|DisplayAuthor   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |||
|DisplayDate   |Date and Time   |No   |Yes   |No   |Yes   |No   |No   |ows_ImageCreateDate, ows_Image_x0020_CreateDate   |DatePictureTaken, ImageCreateDate   |
|DMSDocAccessRight   |Text   |No   |Yes   |No   |Yes   |No   |Yes   |ows_DMSDocAccessRight   ||
|DMSDocAuthor   |Text   |No   |Yes   |Yes   |Yes   |Yes   |Yes   |ows_DMSDocAuthor   ||
|DMSDocTitle   |Text   |No   |Yes   |Yes   |Yes   |No   |Yes   |ows_DMSDocTitle   ||
|DMSLeaseTerm   |Text   |No   |No   |Yes   |Yes   |No   |No   |ows_DMSLeaseTerm   ||
|docacl   |Text   |No   |Yes   |No   |No   |No   |No   |||
|docaclmeta   |Text   |No   |No   |No   |Yes   |No   |No   |||
|DocComments   |Text   |No   |Yes   |No   |No   |No   |No   |Description, Office:6   ||
|DocId   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows__dlc_DocId   ||
|DocKeywords   |Text   |No   |Yes   |No   |No   |No   |No   |Office:5   |urn:schemas-microsoft-com:office:office#Keywords   |
|docrank   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|DocSignature   |Text   |No   |Yes   |No   |No   |No   |No   |Basic:6   |urn:schemas.microsoft.com:fulltextqueryinfo:docsignature   |
|DocSubject   |Text   |No   |Yes   |No   |Yes   |No   |No   |Subject, Office:3   ||
|DocumentSignature   |Integer   |Yes   |Yes   |No   |Yes   |No   |Yes   |||
|DocumentSummary   |Binary Data   |No   |No   |No   |Yes   |No   |No   |||
|DocumentSummarySize   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|docvector   |Text   |No   |No   |No   |Yes   |No   |No   |||
|domain   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|Double00   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double01   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double02   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double03   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double04   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double05   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double06   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double07   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double08   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|Double09   |Double precision float   |No   |Yes   |No   |No   |No   |No   |||
|DuplicateHash   |Integer   |Yes   |Yes   |No   |Yes   |No   |No   |||
|Duplicates   |Text   |No   |No   |No   |Yes   |No   |No   |||
|EduAssignmentCategory   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_EduAssignmentCategory   ||
|EduAssignmentFormat   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_EduAssignmentFormat   ||
|EduEntityId   |Text   |No   |No   |No   |Yes   |No   |No   |ows_EduEntityId   ||
|EduMaximumScore   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_EduMaximumScore   ||
|EndDate   |Date and Time   |No   |Yes   |No   |Yes   |No   |No   |ows_End_x0020_Date   ||
|EventRate   |Double precision float   |No   |No   |No   |No   |No   |Yes   |||
|ExcludeFromSummary   |Text   |No   |No   |No   |Yes   |No   |No   |EmbeddedContent, LINK.OFFICECHILD, Description   ||
|ExpirationTime   |Date and Time   |No   |Yes   |No   |No   |No   |Yes   |ows_Announcement_x0020_Expires, ows_Expires   ||
|ExternalMediaURL   |Text   |No   |No   |No   |Yes   |No   |No   |ows_VideoSetExternalLink   ||
|ExtractedAuthor   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|ExtractedDate   |Date and Time   |No   |Yes   |No   |Yes   |No   |No   |||
|fcocount   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|FileExtension   |Text   |No   |Yes   |No   |Yes   |Yes   |Yes   |FileExtension, ows_File_x0020_Type, ows_FileType   ||
|Filename   |Text   |No   |Yes   |Yes   |Yes   |No   |Yes   |Basic:10   |DAV:displayname   |
|FileType   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |FileType   ||
|FirstLevelColleagues   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |||
|FirstLevelMutualFollowings   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |||
|FirstName   |Text   |Yes   |Yes   |No   |Yes   |No   |Yes   |People:FirstName, People:SPS-PhoneticFirstName   ||
|FollowAllAnchor   |Text   |No   |Yes   |No   |No   |No   |No   |Basic:31   ||
|format   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |||
|FullPostBody   |Text   |No   |No   |No   |Yes   |No   |No   |ows_SearchContent   ||
|FullPostTitle   |Text   |No   |No   |No   |Yes   |No   |No   |ows_SearchTitle   ||
|GeneratedTitle   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |||
|Genre   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|HierarchyUrl   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:ProfileHierarchyViewUrl   ||
|HitHighlightedProperties   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|HitHighlightedSummary   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|HostingPartition   |Text   |No   |Yes   |No   |No   |Yes   |No   |||
|hwboost   |Integer   |No   |Yes   |No   |No   |No   |Yes   |||
|ImageDateCreated   |Date and Time   |No   |Yes   |No   |Yes   |No   |No   |ows_ImageCreateDate, ows_Image_x0020_CreateDate   ||
|importance   |Integer   |No   |Yes   |No   |Yes   |No   |Yes   |||
|Int00   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int01   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int02   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int03   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int04   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int05   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int06   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int07   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int08   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int09   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int10   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int11   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int12   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int13   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int14   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int15   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int16   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int17   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int18   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int19   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int20   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int21   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int22   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int23   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int24   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int25   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int26   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int27   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int28   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int29   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int30   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int31   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int32   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int33   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int34   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int35   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int36   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int37   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int38   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int39   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int40   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int41   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int42   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int43   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int44   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int45   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int46   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int47   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int48   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Int49   |Integer   |No   |Yes   |No   |No   |No   |No   |||
|Interests   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:SPS-Interests   ||
|InternalFileType   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|IsContainer   |Yes/No   |No   |Yes   |No   |Yes   |No   |No   |Basic:7   ||
|IsData   |Yes/No   |No   |Yes   |Yes   |Yes   |No   |No   |ows_IsData, IsData   ||
|IsDefaultView   |Yes/No   |No   |No   |No   |Yes   |No   |No   |ows_IsDefaultView   ||
|IsDocument   |Yes/No   |No   |Yes   |No   |Yes   |No   |No   |SharePoint:isdocument, SharePoint:isdocument, Basic:22   |urn:schemas.microsoft.com:sharepoint:portal:isdocument   |
|IsEmptyList   |Yes/No   |No   |No   |No   |Yes   |No   |No   |ows_IsEmptyList   ||
|IsListItem   |Yes/No   |No   |No   |No   |Yes   |No   |No   |ows_isItem   ||
|IsMyDocuments   |Yes/No   |No   |Yes   |No   |Yes   |No   |No   |ows_IsMyDocuments   ||
|IsPublishingCatalog   |Text   |No   |Yes   |No   |Yes   |No   |No   |IsPublishingCatalog   ||
|IsReport   |Yes/No   |No   |Yes   |Yes   |Yes   |No   |No   |ows_IsReport, IsReport   ||
|ItemCategoryText   |Text   |No   |No   |Yes   |No   |No   |No   |ProductCatalogItemCategory   ||
|JobTitle   |Text   |No   |Yes   |Yes   |Yes   |Yes   |No   |People:SPS-JobTitle, People:Title, ows_JobTitle   |urn:schemas-microsoft-com:sharepoint:portal:profile:Title   |
|Keywords   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Keywords   ||
|language   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ProductCatalogLanguageTag   ||
|languages   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |||
|LastAnalyticsUpdateTime   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|LastModifiedTime   |Date and Time   |No   |Yes   |No   |Yes   |Yes   |Yes   |LastSavedDateTime, Basic:14, Basic:16   |Write, FileWrite, DAV:getlastmodified   |
|LastName   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:LastName, People:SPS-PhoneticLastName   ||
|LevelsToTop   |Integer   |No   |No   |No   |Yes   |No   |Yes   |People:LevelsToTop   ||
|LikesCount   |Integer   |No   |No   |No   |Yes   |No   |No   |ows_LikesCount   ||
|ListID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ListID   ||
|ListItemID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ListItemID   ||
|ListUrl   |Text   |No   |Yes   |No   |Yes   |No   |No   |ListUrl   ||
|Location   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |ows_Location   ||
|ManagedProperties   |Text   |Yes   |Yes   |No   |No   |Yes   |No   |||
|MediaDuration   |Integer   |No   |Yes   |No   |Yes   |Yes   |No   |ows_MediaLengthInSeconds   ||
|Memberships   |Text   |Yes   |Yes   |Yes   |Yes   |No   |No   |People:QuickLinks   ||
|MetadataAuthor   |Text   |No   |Yes   |No   |Yes   |No   |No   |Author, MailFrom, Mail:6   ||
|MicroBlogType   |Integer   |No   |Yes   |No   |Yes   |No   |No   |ows_MicroBlogType   ||
|MobilePhone   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:CellPhone, ows_CellPhone, ows_Cell_x0020_Phone   ||
|ModifiedBy   |Text   |No   |Yes   |No   |Yes   |No   |Yes   |ows_ModifiedBy, ows_Modified_x0020_By, LastModifiedBy   ||
|NLCodePage   |Integer   |No   |Yes   |No   |No   |No   |No   |Web:4   ||
|Notes   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Note, ows_Notes   ||
|NumItemsInCollection   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|OfficeNumber   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:Office   ||
|OrgNames   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:OrganizationNames, ows_Company   |Company   |
|OrgParentNames   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:OrganizationParentNames   ||
|OrgParentUrls   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:OrganizationParentURLs   ||
|OrgUrls   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:OrganizationURLs   ||
|OriginalPath   |Text   |No   |No   |No   |Yes   |No   |No   |Basic:11, Basic:9, Web:2   ||
|OWS_ItemURL   |Text   |No   |No   |No   |Yes   |No   |No   |||
|OWS_URL   |Text   |No   |Yes   |No   |No   |No   |No   |ows_URL   ||
|owsmetadatafacetinfo   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |ows_MetadataFacetInfo   ||
|owstaxidmetadataalltagsinfo   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |ows_taxId_MetadataAllTagsInfo   ||
|owstaxIdProductCatalogItemCategory   |Text   |Yes   |Yes   |Yes   |Yes   |Yes   |No   |ows_taxId_ProductCatalogItemCategory   ||
|ParentLink   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ParentURL   ||
|PastProjects   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:SPS-PastProjects   ||
|Path   |Text   |No   |Yes   |No   |Yes   |No   |No   |Basic:11, Basic:9, Web:2   |DAV:href, VPath, DocAddress, ...   |
|People   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |ows_People, Author, MailFrom   ||
|PeopleInMedia   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |ows_PeopleInMedia   ||
|PeopleKeywords   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |People:SPS-Responsibility, People:SPS-Skills, People:SPS-Interests   ||
|PhoneNumber   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |||
|PictureHeight   |Integer   |No   |Yes   |No   |Yes   |No   |No   |ows_ImageHeight, ows_VideoHeightInPixels   |ImageHeight, urn:schemas-microsoft-com:office:office#ows_ImageHeight   |
|PictureThumbnailURL   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_AlternateThumbnailUrl, ows_EncodedAbsThumbnailUrl, ows_DMSCoverImage   ||
|PictureURL   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_PictureURL, People:PictureURL   |urn:schemas.microsoft.com:fulltextqueryinfo:PictureURL   |
|PictureWidth   |Integer   |No   |Yes   |No   |Yes   |No   |No   |ows_ImageWidth, ows_VideoWidthInPixels   |ImageWidth, urn:schemas-microsoft-com:office:office#ows_ImageWidth   |
|PopularSocialTags   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|PostAuthor   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |ows_PostAuthor   ||
|PreferredName   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:PreferredName   |urn:schemas-microsoft-com:sharepoint:portal:profile:PreferredName   |
|Priority   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Priority   ||
|PrivateColleagues   |Text   |Yes   |Yes   |No   |No   |No   |No   |People:ColleaguesNonPublic   ||
|processingtime   |Date and Time   |No   |Yes   |No   |Yes   |No   |Yes   |||
|ProductCatalogGroupNumberOWSTEXT   |Text   |No   |Yes   |No   |Yes   |No   |Yes   |ows_ProductCatalogGroupNumber   ||
|ProfileExpertise   |Text   |No   |Yes   |No   |No   |No   |No   |People:SPS-Responsibility, People:SPS-PastProjects, People:SPS-Skills   ||
|ProfileName   |Text   |No   |Yes   |No   |No   |No   |No   |People:PreferredName, People:FirstName, People:LastName   ||
|Pronunciations   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:FirstName, People:LastName, People:PreferredName   ||
|PublishingCatalogSettings   |Text   |No   |No   |No   |Yes   |No   |No   |PublishingCatalogSettings   ||
|PublishingImage   |Text   |No   |No   |No   |Yes   |No   |No   |||
|Purpose   |Text   |No   |Yes   |No   |No   |No   |No   |ows_Purpose   ||
|QueryTerms   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|Rank   |Integer   |No   |No   |No   |Yes   |No   |No   |urn:schemas.microsoft.com:fulltextqueryinfo:rank   ||
|RankDetail   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|RankingWeightHigh   |Text   |Yes   |Yes   |Yes   |No   |No   |No   |People:OrganizationNames, People:Department   ||
|RankingWeightLow   |Text   |Yes   |Yes   |Yes   |No   |No   |No   |People:SPS-Skills, People:SPS-Interests   ||
|RankingWeightName   |Text   |Yes   |Yes   |Yes   |No   |No   |No   |People:CombinedName, People:UserName, People:WorkEmail   ||
|Rating   |Double precision float   |No   |No   |No   |Yes   |No   |No   |||
|recommendedfor   |Text   |Yes   |Yes   |No   |No   |Yes   |Yes   |||
|RecsClickedLifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|RecsClickedRecent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|RefinableDate00   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate01   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate02   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate03   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate04   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate05   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate06   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate07   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate08   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate09   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate10   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate11   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate12   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate13   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate14   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate15   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate16   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate17   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate18   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDate19   |Date and Time   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal00   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal01   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal02   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal03   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal04   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal05   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal06   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal07   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal08   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDecimal09   |Decimal   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble00   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble01   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble02   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble03   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble04   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble05   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble06   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble07   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble08   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableDouble09   |Double precision float   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt00   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt01   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt02   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt03   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt04   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt05   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt06   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt07   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt08   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt09   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt10   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt11   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt12   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt13   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt14   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt15   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt16   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt17   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt18   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt19   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt20   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt21   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt22   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt23   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt24   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt25   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt26   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt27   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt28   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt29   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt30   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt31   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt32   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt33   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt34   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt35   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt36   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt37   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt38   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt39   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt40   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt41   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt42   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt43   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt44   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt45   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt46   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt47   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt48   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableInt49   |Integer   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString00   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString01   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString02   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString03   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString04   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString05   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString06   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString07   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString08   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString09   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString10   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString11   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString12   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString13   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString14   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString15   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString16   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString17   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString18   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString19   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString20   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString21   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString22   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString23   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString24   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString25   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString26   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString27   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString28   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString29   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString30   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString31   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString32   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString33   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString34   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString35   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString36   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString37   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString38   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString39   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString40   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString41   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString42   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString43   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString44   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString45   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString46   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString47   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString48   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString49   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString50   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString51   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString52   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString53   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString54   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString55   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString56   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString57   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString58   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString59   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString60   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString61   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString62   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString63   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString64   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString65   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString66   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString67   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString68   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString69   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString70   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString71   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString72   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString73   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString74   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString75   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString76   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString77   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString78   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString79   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString80   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString81   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString82   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString83   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString84   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString85   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString86   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString87   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString88   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString89   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString90   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString91   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString92   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString93   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString94   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString95   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString96   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString97   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString98   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|RefinableString99   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|ReplyCount   |Integer   |No   |No   |No   |Yes   |No   |No   |ows_ReplyCount   ||
|Responsibilities   |Text   |Yes   |Yes   |Yes   |Yes   |Yes   |No   |People:SPS-Responsibility   |Responsibility   |
|RobotsNoIndex   |Yes/No   |No   |Yes   |No   |No   |No   |No   |ows_RobotsNoIndex   ||
|RootPostID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_RootPostID   ||
|RootPostOwnerID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_RootPostOwnerID   ||
|RootPostUniqueID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_RootPostUniqueID   ||
|Schools   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:SPS-School   ||
|SecondaryFileExtension   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_FileType, ows_File_x0020_Type   ||
|SecondLevelColleagues   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |||
|SectionIndexes   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|SectionNames   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|ServerRedirectedEmbedURL   |Text   |No   |No   |No   |Yes   |No   |No   |ows_ServerRedirectedEmbedUrl   ||
|ServerRedirectedPreviewURL   |Text   |No   |No   |No   |Yes   |No   |No   |ows_ServerRedirectedPreviewUrl   ||
|ServerRedirectedURL   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ServerRedirectedUrl   ||
|ServiceApplicationID   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|SharedWithInternal   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |ows_SharedWithInternal   ||
|SipAddress   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:SPS-SipAddress   ||
|Site   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |urn:schemas.microsoft.com:fulltextqueryinfo:sitename   ||
|SiteClosed   |Yes/No   |No   |Yes   |No   |No   |No   |No   |||
|SiteDescription   |Text   |No   |No   |No   |Yes   |No   |No   |ows_SiteDescription   ||
|SiteID   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_SiteID   ||
|SiteLogo   |Text   |No   |No   |No   |Yes   |No   |No   |LogoURL   ||
|SitemapChangeFrequency   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|SitemapPriority   |Double precision float   |No   |No   |No   |Yes   |No   |No   |||
|SiteMembers   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|sitename   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |||
|SiteOwners   |Text   |Yes   |No   |No   |Yes   |No   |No   |||
|siterank   |Integer   |No   |No   |No   |No   |No   |Yes   |||
|SiteTitle   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_SiteName   |urn:schemas-microsoft-com:office:office#ows_SiteName   |
|Size   |Integer   |No   |Yes   |No   |Yes   |Yes   |Yes   |Basic:12, ows_ImageSize   |DAV:getcontentlength, PictureSize, ImageSize   |
|Skills   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |People:SPS-Skills   ||
|SocialTag   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |||
|SocialTagTextUrl   |Text   |Yes   |Yes   |No   |No   |No   |No   |People:SocialTagTextUrl   ||
|SPContentType   |Text   |No   |Yes   |No   |No   |Yes   |No   |ows_ContentType   ||
|SpellingTerms   |Text   |No   |No   |Yes   |No   |No   |No   |||
|SPSiteURL   |Text   |No   |Yes   |No   |Yes   |No   |Yes   |ows_SPSiteURL   ||
|SPVersion   |Integer   |No   |No   |No   |Yes   |No   |No   |ows_SPVersion   ||
|StartDate   |Date and Time   |No   |Yes   |No   |Yes   |No   |No   |ows_Start_x0020_date, ows_DMSReleaseDate   ||
|Status   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Issue_x0020_Status, ows_Task_x0020_Status   ||
|Tags   |Text   |Yes   |Yes   |No   |Yes   |Yes   |No   |ows_SearchTag1, ows_SearchTag2, ows_SearchTag3   ||
|teaser   |Text   |No   |No   |No   |Yes   |No   |No   |||
|Text1   |Text   |No   |No   |Yes   |No   |No   |No   |||
|Text2   |Text   |No   |No   |Yes   |No   |No   |No   |||
|Text3   |Text   |No   |No   |Yes   |No   |No   |No   |||
|Title   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |MetadataExtractorTitle, Office:2, ows_BaseName, Title   |DocTitle, urn:schemas.microsoft.com:fulltextqueryinfo:displaytitle   |
|tld   |Text   |No   |Yes   |No   |Yes   |No   |No   |||
|UniqueID   |Text   |No   |No   |No   |Yes   |No   |No   |ows_UniqueID   ||
|url   |Text   |No   |No   |No   |Yes   |No   |No   |ows_DMSDocAuthorURL   ||
|UrlDepth   |Integer   |No   |Yes   |No   |Yes   |Yes   |Yes   |||
|urlkeywords   |Text   |No   |Yes   |Yes   |No   |No   |No   |||
|urls   |Text   |Yes   |Yes   |No   |Yes   |No   |No   |||
|UsageAnalyticsId   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_ProductCatalogItemNumber   ||
|UsageEvent10LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent10Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent11LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent11Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent12LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent12Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent1LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent1Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent2LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent2Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent3LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent3Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent4LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent4Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent5LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent5Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent6LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent6Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent7LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent7Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent8LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent8Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent9LifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEvent9Recent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|UsageEventItemId   |Text   |No   |Yes   |No   |Yes   |Yes   |No   |ows_ProductCatalogItemNumber   ||
|UserEncodingURL   |Text   |No   |No   |No   |Yes   |No   |No   |ows_VideoSetUserOverrideEncoding   ||
|UserName   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:UserName, ows_FullName, ows_Full_x0020_Name   ||
|UserProfile_GUID   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:UserProfile_GUID   ||
|ViewsLast1Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast1DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast2Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast2DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast3Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast3DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast4Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast4DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast5Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast5DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast6Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast6DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast7Days   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLast7DaysUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths1   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths1Unique   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths2   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths2Unique   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths3   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLastMonths3Unique   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|ViewsLifeTime   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|ViewsLifeTimeUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|ViewsRecent   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|ViewsRecentUniqueUsers   |Integer   |No   |No   |No   |Yes   |No   |Yes   |||
|WebId   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_WebId   ||
|WebTemplate   |Text   |No   |Yes   |No   |No   |Yes   |No   |WebTemplate   ||
|WeightedMemberships   |Text   |Yes   |No   |No   |Yes   |No   |No   |People:WeightedMemberships   ||
|WikiCategory   |Text   |No   |Yes   |No   |Yes   |No   |No   |ows_Wiki_x0020_Page_x0020_Categories   ||
|WordCustomRefiner1   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordCustomRefiner2   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordCustomRefiner3   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordCustomRefiner4   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordCustomRefiner5   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordExactCustomRefiner   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartCustomRefiner1   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartCustomRefiner2   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartCustomRefiner3   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartCustomRefiner4   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartCustomRefiner5   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WordPartExactCustomRefiner   |Text   |Yes   |Yes   |No   |Yes   |Yes   |Yes   |||
|WorkEmail   |Text   |No   |Yes   |Yes   |Yes   |No   |No   |People:WorkEmail, ows_EMail, ows_EMail_x0020_   |urn:schemas-microsoft-com:sharepoint:portal:profile:WorkEmail   |
|WorkId   |Integer   |No   |No   |No   |Yes   |No   |No   |||
|WorkPhone   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:WorkPhone, ows_WorkPhone, ows_Work_x0020_Phone   |urn:schemas-microsoft-com:sharepoint:portal:profile:WorkPhone   |
|YomiDisplayName   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:SPS-PhoneticDisplayName   ||
   

### Managed Properties Added in SharePoint Server 2016
|||||||||||
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|**Property name**  |**Type**  |**Multi-valued**  |**Queryable**  |**Searchable**  |**Retrievable**  |**Refinable**  |**Sortable**  |**Mapped crawled properties**  |**Aliases**  |
|AADObjectID   |Text   |No   |Yes   |No   |Yes   |No   |No   |People:AboutMe, ows_Notes   ||
|AnalyticsPath |Text   |No   |Yes  |No |Yes  |No  |No  |People:msOnline-ObjectId||
|ChannelVersion |Text |No|No|No|Yes|No|No|ows_ChannelVersion||
|ClassificationConfidence|Integer|Yes|Yes|No|Yes|No|No||SensitiveMatchConfidence;ClassificationConfidenceCreditCardNumber;ClassificationConfidenceEUDebitCardNumber;ClassificationConfidenceUSSocialSecurityNumberSSN;ClassificationConfidenceUSIndividualTaxpayerIdentificationNumberITIN;ClassificationConfidenceCanadaSocialInsuranceNumber;ClassificationConfidenceUKNationalInsuranceNumberNINO;ClassificationConfidenceUKDriversLicenseNumber;ClassificationConfidenceGermanDriversLicenseNumber;ClassificationConfidenceGermanPassportNumber;ClassificationConfidenceUKNationalHealthServiceNumber;ClassificationConfidenceFranceSocialSecurityNumberINSEE;ClassificationConfidenceFranceDriversLicenseNumber;ClassificationConfidenceCanadaDriversLicenseNumber;ClassificationConfidenceUSDriversLicenseNumber;ClassificationConfidenceJapanDriversLicenseNumber;ClassificationConfidenceJapanResidentRegistrationNumber;ClassificationConfidenceJapanSocialInsuranceNumberSIN;ClassificationConfidenceJapanPassportNumber;ClassificationConfidenceJapanBankAccountNumber;ClassificationConfidenceFrancePassportNumber;ClassificationConfidenceUSUKPassportNumber;ClassificationConfidenceSWIFTCode;ClassificationConfidenceUSBankAccountNumber;ClassificationConfidenceABARoutingNumber;ClassificationConfidenceDrugEnforcementAgencyDEANumber;ClassificationConfidenceAustraliaMedicalAccountNumber;ClassificationConfidenceAustraliaTaxFileNumber;ClassificationConfidenceIsraelNationalID;ClassificationConfidenceNewZealandMinistryofHealthNumber;ClassificationConfidenceSpainSocialSecurityNumberSSN;ClassificationConfidenceSwedenNationalID;ClassificationConfidenceAustraliaBankAccountNumber;ClassificationConfidenceAustraliaDriversLicenseNumber;ClassificationConfidenceAustraliaPassportNumber;ClassificationConfidenceCanadaBankAccountNumber;ClassificationConfidenceCanadaPassportNumber;ClassificationConfidenceCanadaPersonalHealthIdentificationNumberPHIN;ClassificationConfidenceCanadaHealthServiceNumber;ClassificationConfidenceFranceNationalIDCardCNI;ClassificationConfidenceIPAddress;ClassificationConfidenceInternationalBankingAccountNumberIBAN;ClassificationConfidenceIsraelBankAccountNumber;ClassificationConfidenceItalyDriversLicenseNumber;ClassificationConfidenceSaudiArabiaNationalID;ClassificationConfidenceSwedenPassportNumber;ClassificationConfidenceUKElectoralRollNumber;ClassificationConfidenceFinlandNationalID;ClassificationConfidenceTaiwanNationalID;ClassificationConfidencePolandNationalIDPESEL;ClassificationConfidencePolandIdentityCard;ClassificationConfidencePolandPassport|
|ClassificationCount|Integer|Yes|Yes|No|Yes|No|No||SensitiveMatchCount;ClassificationCountCreditCardNumber;ClassificationCountEUDebitCardNumber;ClassificationCountUSSocialSecurityNumberSSN;ClassificationCountUSIndividualTaxpayerIdentificationNumberITIN;ClassificationCountCanadaSocialInsuranceNumber;ClassificationCountUKNationalInsuranceNumberNINO;ClassificationCountUKDriversLicenseNumber;ClassificationCountGermanDriversLicenseNumber;ClassificationCountGermanPassportNumber;ClassificationCountUKNationalHealthServiceNumber;ClassificationCountFranceSocialSecurityNumberINSEE;ClassificationCountFranceDriversLicenseNumber;ClassificationCountCanadaDriversLicenseNumber;ClassificationCountUSDriversLicenseNumber;ClassificationCountJapanDriversLicenseNumber;ClassificationCountJapanResidentRegistrationNumber;ClassificationCountJapanSocialInsuranceNumberSIN;ClassificationCountJapanPassportNumber;ClassificationCountJapanBankAccountNumber;ClassificationCountFrancePassportNumber;ClassificationCountUSUKPassportNumber;ClassificationCountSWIFTCode;ClassificationCountUSBankAccountNumber;ClassificationCountABARoutingNumber;ClassificationCountDrugEnforcementAgencyDEANumber;ClassificationCountAustraliaMedicalAccountNumber;ClassificationCountAustraliaTaxFileNumber;ClassificationCountIsraelNationalID;ClassificationCountNewZealandMinistryofHealthNumber;ClassificationCountSpainSocialSecurityNumberSSN;ClassificationCountSwedenNationalID;ClassificationCountAustraliaBankAccountNumber;ClassificationCountAustraliaDriversLicenseNumber;ClassificationCountAustraliaPassportNumber;ClassificationCountCanadaBankAccountNumber;ClassificationCountCanadaPassportNumber;ClassificationCountCanadaPersonalHealthIdentificationNumberPHIN;ClassificationCountCanadaHealthServiceNumber;ClassificationCountFranceNationalIDCardCNI;ClassificationCountIPAddress;ClassificationCountInternationalBankingAccountNumberIBAN;ClassificationCountIsraelBankAccountNumber;ClassificationCountItalyDriversLicenseNumber;ClassificationCountSaudiArabiaNationalID;ClassificationCountSwedenPassportNumber;ClassificationCountUKElectoralRollNumber;ClassificationCountFinlandNationalID;ClassificationCountTaiwanNationalID;ClassificationCountPolandNationalIDPESEL;ClassificationCountPolandIdentityCard;ClassificationCountPolandPassport|
|ClassificationLastScan|Date and Time|Yes|Yes|No|Yes|Yes|Yes||LastSensitiveContentScan|
|ClassificationType|Text|Yes|Yes|No|Yes|Yes|No||SensitiveType|
|ClientUrl|Text|No|Yes|No|Yes|No|No|ClientUrl||
|ContentDatabaseId|Text|No|Yes|No|Yes|No|No|ows_ContentDatabaseId||
|CreatedById|Text|No|Yes|No|Yes|No|No|ows_AuthorUserId||
|DlcDocId|Text|No|Yes|No|Yes|No|No|ows__dlc_DocId||
|HideFromDelve|Yes/No|No|Yes|No|No|No|No|ows_HideFromDelve||
|HtmlFileType|Text|No|Yes|No|Yes|No|No|ows_Html_x0020_File_x0020_Type||
|IRMProtected|Yes/No|No|Yes|No|Yes|Yes|Yes|ows_IRMProtected||
|IRMTemplateName|Text|No|Yes|No|Yes|Yes|Yes|ows_IRMTemplateName||
|IsExternalContent|Yes/No|No|Yes|No|Yes|Yes|Yes|IsExternalContent||
|IsInRecycleBin|Yes/No|No|Yes|No|Yes|No|No|InRecycleBin, ows_InRecycleBin||
|IsOneNotePage|Yes/No|No|Yes|No|Yes|No|No|ows_IsOneNotePage||
|ItemCategory|Text|No|Yes|No|Yes|No|No|ows_ItemCategory||
|LastSharedByTime|Date and Time|No|No|No|Yes|No|No|ows_LastSharedByTime||
|LastSharedByUser|Text|No|Yes|No|Yes|No|No|ows_lastSharedByUser||
|LinkingUrl|Text|No|Yes|No|Yes|No|No|ows_LinkingUrl||
|ModifiedById|Text|No|Yes|No|Yes|No|No|ows_q_USER_Editor||
|OfficeGraphEnabled|Yes/No|No|Yes|No|Yes|No|No|People:OfficeGraphEnabled||
|owstaxIdVideoPortalItemCategory|Text|Yes|Yes|Yes|Yes|Yes|No|ows_taxId|VideoCategory||
|PageAppId|Text|No|Yes|No|Yes|No|No|AppId||
|PageAuthorInitials|Text|No|No|No|Yes|No|No|AuthorInitials||
|PageID|Text|No|Yes|No|Yes|No|No|PageId||
|PageLastModifierInitials|Text|No|No|No|Yes|No|No|LastModifierInitials||
|PageLevel|Text|No|No|No|Yes|No|No|PageLevel||
|PageTags|Text|Yes|Yes|No|Yes|No|No|Tags||
|ParentId|Text|No|Yes|No|Yes|No|No|ows_ParentUniqueId||
|PolicyTags|Integer|Yes|Yes|No|No|No|No|||
|PrivacyIndicator|Text|No|Yes|No|Yes|No|No|||
|ProgID|Text|No|Yes|No|Yes|No|No|ows_ProgId||
|Restricted|Yes/No|No|Yes|No|Yes|Yes|Yes|ows_Restricted||
|SectionColor|Text|No|No|No|Yes|No|No|SectionColor||
|SharedWithDetails|Text|No|No|No|Yes|No|No|ows_SharedWithDetails||
|SiteGroup|Text|Yes|Yes|No|Yes|No|No|||
|SiteTemplate|Text|No|Yes|No|Yes|Yes|Yes|ows_SiteTemplate||
|SiteTemplateId|Integer|No|Yes|No|Yes|Yes|Yes|ows_SiteTemplateId||
|SpotlightVideos|Text|No|No|No|Yes|No|No|ows_SpotlightVideos||
|SPS-HideFromAddressLists|Integer|No|Yes|No|Yes|No|No|People:SPS-HideFromAddressLists||
|SPS-RecipientTypeDetails|Integer|No|Yes|No|Yes|No|No|People:SPS-RecipientTypeDetails||
|SPS-UserType|Integer|No|Yes|No|Yes|No|No|People:SPS-UserType||
|SPWebUrl|Text|No|No|No|Yes|No|No|ows_taxId_SPLocationSite||
|TileColor|Text|No|No|No|Yes|No|No|ows_TileColor||
|VideoProcessingStatus|Text|No|Yes|No|Yes|No|No|ows_VideoProcessingStatus||
|ViewableByAnonymousUsers|Yes/No|No|Yes|No|Yes|Yes|Yes|ows_ViewableByAnonymousUsers||
|ViewableByExternalUsers|Yes/No|No|Yes|No|Yes|Yes|Yes|ows_ViewableByExternalUsers||
|WebApplicationId|Text|No|Yes|No|Yes|No|No|ows_WebApplicationId||
|WebUrl|Text|No|Yes|No|Yes|No|No|No|WebUrl||
|XLDataConnCount|Decimal|No|No|No|Yes|No|No|XLDataConnCount||
|XLDataConnCountRngID|Integer|No|Yes|No|Yes|Yes|Yes|XLDataConnCountRngID||
|XLFormulaCount|Decimal|No|No|No|Yes|No|No|XLFormulaCount||
|XLFormulaCountRngID|Integer|No|Yes|No|Yes|Yes|Yes|XLFormulaCountRngID||
|XLLinkedWkbkCount|Decimal|No|No|No|Yes|No|No|XLLinkedWkbkCount||
|XLLinkedWkbkCountRngID|Integer|No|Yes|No|Yes|Yes|Yes|XLLinkedWkbkCountRngID||
|XLLinkedWorkbooksText|Text|Yes|Yes|No|Yes|No|No|XLLinkedWorkbooksText||
|XLUniqueFormulaSetCount|Integer|No|No|No|Yes|No|No|XLUniqueFormulaSetCount||
|XLUniqueFormulaSetCountRngID|Integer|No|Yes|No|Yes|Yes|Yes|XLUniqueFormulaSetCountRngID||
|XLWorksheetCount|Decimal|No|No|No|Yes|No|No|XLWorksheetCount||
|XLWorksheetCountRngID|Integer|No|Yes|No|Yes|Yes|Yes|XLWorksheetCountRngID||

### Managed Properties Added in SharePoint Server 2019
|||||||||||
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
|**Property name**  |**Type**  |**Multi-valued**  |**Queryable**  |**Searchable**  |**Retrievable**  |**Refinable**  |**Sortable**  |**Mapped crawled properties**  |**Aliases**  |
|AppVersion   |Text   |No   |No   |No   |Yes   |No   |No   |ows_AppVersion  ||
|AutoTagClassificationId|Text|No|Yes|No|Yes|Yes|No|||
|ClassificationContext|Text|Yes|No|No|Yes|No|No|||
|Color|Text|No|No|No|Yes|No|No|ThemePrimary||
|ComplianceAssetId|Text|No|Yes|No|Yes|No|No|ows_ComplianceAssetId||
|ComplianceTag|Text|No|Yes|No|Yes|Yes|Yes|ows__ComplianceTag||
|ComplianceTagWrittenTime|Date and Time|No|Yes|No|Yes|Yes|Yes|ows__ComplianceTagWrittenTime||
|CultureName|Text|No|No|No|Yes|No|No|ows_CultureName||
|DefaultSectionNames|Text|No|Yes|No|Yes|No|No|ows_DefaultSectionNames||
|DepartmentId|Text|No|Yes|No|Yes|Yes|No|ows_DepartmentId||
|FirstPublishedDate|Date and Time|No|Yes|No|Yes|Yes|Yes|ows_FirstPublishedDate||
|FolderType|Text|No|No|No|Yes|No|No|ows_FolderType||
|GeoLocation|Text|No|Yes|No|Yes|Yes|No|ows_GeoLocation||
|GroupId|Text|No|Yes|No|Yes|No|No|ows_GroupId||
|Has_Leader_Only_SectionGroup|Yes/No|No|No|No|Yes|No|No|ows_Has_Leader_Only_SectionGroup||
|Has_Teacher_Only_SectionGroup|Yes/No|No|No|No|Yes|No|No|ows_Has_Teacher_Only_SectionGroup||
|Is_Collaboration_Space_Locked|Yes/No|No|No|No|Yes|No|No|ows_Is_Collaboration_Space_Locked||
|IsAllDayEvent|Yes/No|No|Yes|No|Yes|No|No|ows_fAllDayEvent||
|IsClassificationProcessingLimitExceeded|Yes/No|No|Yes|No|Yes|No|No|||
|IsHubSite|Yes/No|No|Yes|No|Yes|No|No|ows_IsHubSite||
|LastModifiedTimeForRetention|Date and Time|No|Yes|No|Yes|Yes|Yes|ows_Modified||
|Leaders|Text|Yes|No|No|Yes|No|No|ows_Leaders||
|MediaServiceAutoTags|Text|No|Yes|Yes|Yes|No|No|ows_MediaServiceAutoTags||
|MediaServiceLocation|Text|No|Yes|Yes|Yes|No|No|ows_MediaServiceLocation||
|MediaServiceMetadata|Text|No|Yes|No|Yes|No|No|MediaServiceMetadata||
|Member_Groups|Text|Yes|No|No|Yes|No|No|ows_Member_Groups||
|Members|Text|Yes|No|No|Yes|No|No|ows_Members||
|NotebookType|Text|No|Yes|No|Yes|No|No|ows_NotebookType||
|ObjectEmbeddings|Text|Yes|Yes|No|Yes|No|No|NumberOfTables, NumberOfCharts, NumberOfSmartArt||
|Owner|Text|No|No|No|Yes|No|No|ows_Owner||
|PartitionKey|Text|No|Yes|No|Yes|No|No|||
|policyacl|Text|No|Yes|No|No|No|No|||
|policyacl2|Text|No|Yes|No|No|No|No|||
|PromotedState|Integer|No|Yes|No|Yes|No|Yes|ows_PromotedState||
|PublishingPageImageOWSIMGEX|Text|No|No|No|Yes|No|No|ows_r_IMGE_PublishingPageImage|PublishingPageImageOWSIMGE|
|PublishingRollupImageOWSIMGEX|Text|No|No|No|Yes|No|No|ows_r_IMGE_PublishingRollupImage|PublishingRollupImageOWSIMGE|
|RefinableDateInvariant00|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateInvariant01|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateSingle00|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateSingle01|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateSingle02|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateSingle03|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableDateSingle04|Date and Time|No|Yes|No|Yes|Yes|Yes|||
|RefinableString100|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString101|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString102|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString103|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString104|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString105|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString106|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString107|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString108|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString109|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString110|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString111|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString112|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString113|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString114|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString115|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString116|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString117|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString118|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString119|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString120|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString121|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString122|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString123|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString124|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString125|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString126|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString127|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString128|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString129|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString130|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString131|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString132|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString133|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString134|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString135|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString136|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString137|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString138|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString139|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString140|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString141|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString142|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString143|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString144|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString145|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString146|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString147|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString148|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString149|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString150|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString151|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString152|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString153|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString154|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString155|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString156|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString157|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString158|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString159|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString160|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString161|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString162|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString163|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString164|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString165|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString166|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString167|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString168|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString169|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString170|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString171|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString172|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString173|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString174|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString175|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString176|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString177|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString178|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString179|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString180|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString181|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString182|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString183|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString184|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString185|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString186|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString187|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString188|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString189|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString190|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString191|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString192|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString193|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString194|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString195|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString196|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString197|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString198|Text|Yes|Yes|No|Yes|Yes|Yes|||
|RefinableString199|Text|Yes|Yes|No|Yes|Yes|Yes|||
|SharedWithUsersOWSUSER|Text|No|Yes|No|Yes|No|No|ows_q_USER_SharedWithUsers||
|Student_Groups|Text|Yes|No|No|Yes|No|No|ows_Student_Groups||
|Students|Text|Yes|No|No|Yes|No|No|ows_Students||
|TagEventDate|Date and Time|No|Yes|No|Yes|No|No|ows_TagEventDate||
|Teachers|Text|Yes|No|No|Yes|No|No|ows_Teachers||
