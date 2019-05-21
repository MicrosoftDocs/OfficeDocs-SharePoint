---
title: "Use a SharePoint Server records archive or manage records in place"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 3/1/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 30f4e254-0b00-49bb-84af-3ece619ad0e4
description: "Decide which records management approach to choose in SharePoint Server."
---

# Use a SharePoint Server records archive or manage records in place

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
In SharePoint Server you can manage records in an archive, or you can manage records in the same document repository as active documents. By using the SharePoint Server in-place approach, when you declare that a document has become a record, the record remains in place, but SharePoint Server now manages it as a record. For example, a document might get a different retention policy when it is declared to be a record, or users might be unable to edit it.
  
A hybrid approach is also possible. For example, you could keep records in place with active documents for two years, and then move records to a records archive when a project is completed.
  
As you think about whether to manage records in a separate Records Center site or in the same collaboration site in which the documents were created, consider the following questions:
  
- Is the governance of the collaboration site appropriate for managing records? Is your industry subject to regulatory requirements that mandate records be separated from active documents? Should the administrator of a collaboration site be trusted to manage a site that contains records? You might want to store records in a site that uses more restricted access than the collaboration site, or in a site that is backed up on a different schedule.
    
- How long will the collaboration site be in use? If records will have to be kept for longer than the project is ongoing, selecting an in-place records management strategy means that you will have to maintain the collaboration site even after it is no longer used.
    
- Will the project members need frequent access to the documents after the documents have become records? If you use an in-place approach, project members can access documents in the same manner regardless of whether the documents are active or are records.
    
- Are records managers in your organization responsible for only records, or are they responsible for all information, regardless of whether it is active or a record? If records managers are responsible only for official records, having a separate Records Center site might be easier for them. 
    
The following table describes differences between what you can do with records in a record center and with records that are managed in-place in a collaboration site. The differences are presented from the point of view of both records managers and employees collaborating on a project team. 
  
**Differences between a records archive and in-place records**

|**Factor**|**Records archive**|**In-place records**|
|:-----|:-----|:-----|
|Managing record retention  <br/> |The content organizer automatically puts new records in the correct folder in the archive's file plan, based on metadata.  <br/> |There may be different policies for records and active documents based on the current content type or location.  <br/> |
|Restrict which users can view records  <br/> |Yes. The archive specifies the permissions for the record.  <br/> |No. Permissions do not change when a document becomes a record. However, you can restrict which users can edit and delete records.  <br/> |
|Ease of locating records (for records managers)  <br/> |Easier. All records are in one location.  <br/> |Harder. Records are spread across multiple collaboration sites.  <br/> |
|Maintain all document versions as records  <br/> |The user must explicitly send each version of a document to the archive.  <br/> |Automatic, assuming versioning is turned on.  <br/> |
|Ease of locating information (for team collaborators)  <br/> |Harder, although a link to the document can be added to the collaboration site when the document becomes a record.  <br/> |Easier.  <br/> |
|Clutter of collaboration site  <br/> |Collaboration site contains only active documents.  <br/> |Collaboration site contains active and inactive documents (records), although you can create views to display only records.  <br/> |
|Ability to audit records  <br/> |Yes.  <br/> |Dependent on audit policy of the collaboration site.  <br/> |
|Administrative security  <br/> |A records manager can manage the records archive.  <br/> |Collaboration site administrators have permission to manage records and active documents.  <br/> |
   
The following table describes differences between the two records management approaches that might affect how you manage IT resources.
  
**Resource differences between a records archive and in-place records**

|**Factor**|**Records archive**|**In-place records**|
|:-----|:-----|:-----|
|Number of sites to manage  <br/> |More sites. That is,, there is a separate archive in addition to collaboration sites.  <br/> |Fewer sites.  <br/> |
|Scalability  <br/> |Relieves database size pressure on collaboration sites.  <br/> |Maximum site collection size reached sooner.  <br/> |
|Ease of administration  <br/> |Separate site or farm for records.  <br/> |No additional site provisioning work beyond what is already needed for the sites that have active documents.  <br/> |
|Storage  <br/> |Can store records on different storage medium.  <br/> |Active documents and records stored together.  <br/> |
   
## See also

#### Other Resources

[Introduction to Records Management and Compliance](https://go.microsoft.com/fwlink/?LinkId=397891)

