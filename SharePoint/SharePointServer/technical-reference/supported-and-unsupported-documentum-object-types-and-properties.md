---
title: "Supported and unsupported Documentum object types and properties in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: f753e138-04c2-4358-a12e-2a406a431ac9
description: "Learn which object types and properties the SharePoint Server Indexing Connector for Documentum supports or does not support."
---

# Supported and unsupported Documentum object types and properties in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The following sections list supported and unsupported object types and properties for the Indexing Connector for Documentum:
  
- [Supported Documentum container objects and properties](supported-and-unsupported-documentum-object-types-and-properties.md#BKMK_Section1)
    
- [Supported Documentum document objects and properties](supported-and-unsupported-documentum-object-types-and-properties.md#BKMK_Section2)
    
- [Unsupported Documentum object types](supported-and-unsupported-documentum-object-types-and-properties.md#BKMK_Section3)
    
- [Unsupported Documentum properties](supported-and-unsupported-documentum-object-types-and-properties.md#BKMK_Section4)
    
## Supported Documentum container objects and properties
<a name="BKMK_Section1"> </a>

The Indexing Connector for Documentum supports the following Documentum container objects and properties:
  
- cabinetpath
    
- dm_cabinet and subtypes
    
- dm_Folder and subtypes
    
- folderpath
    
- keywords
    
- object_name
    
- owner_name
    
- r_creation_date
    
- r_creator_name
    
- r_modifier
    
- r_modify_date
    
- r_object_type
    
- subject
    
- title
    
## Supported Documentum document objects and properties
<a name="BKMK_Section2"> </a>

The Indexing Connector for Documentum supports the following Documentum document objects and properties:
  
- a_content_type
    
- a_storage_type
    
- authors
    
- ContainerPath
    
- dm_document
    
- keywords
    
- i_retain_until
    
- log_entry
    
- object_name
    
- owner_name
    
- r_access_date
    
- r_creation_date
    
- r_creator_name
    
- r_current_state
    
- r_full_content_size
    
- r_lock_date
    
- r_modify_date
    
- r_lock_owner
    
- r_modifier
    
- r_object_type
    
- r_policy_id
    
- r_version_label
    
- subject
    
- title
    
- All custom properties
    
## Unsupported Documentum object types
<a name="BKMK_Section3"> </a>

The Indexing Connector for Documentum does not support the following Documentum object types:
  
- Temp cabinets
    
- Temp files
    
- Temp folders
    
## Unsupported Documentum properties
<a name="BKMK_Section4"> </a>

The Indexing Connector for Documentum does not support the following Documentum properties:
  
- a_application_type
    
- a_archive
    
- a_category
    
- a_compound_architecture
    
- a_controlling_app
    
- a_effective_date
    
- a_effective_flag
    
- a_effective_label
    
- a_expiration_date
    
- a_extended_properties
    
- a_full_text
    
- a_is_hidden
    
- a_is_signed
    
- a_is_template
    
- a_last_review_date
    
- a_link_resolved
    
- a_publish_formats
    
- a_retention_date
    
- a_special_app
    
- a_status
    
- acl_domain
    
- group_permit
    
- i_antecedent_id
    
- i_branch_cnt
    
- i_cabinet_id
    
- i_chronicle_id
    
- i_contents_id
    
- i_direct_dsc
    
- i_folder_id
    
- i_has_folder
    
- i_is_deleted
    
- i_is_reference
    
- i_is_replica
    
- i_latest_flag
    
- i_reference_cnt
    
- i_retainer_id
    
- i_vstamp
    
- language_code
    
- owner_permit
    
- r_alias_set_id
    
- r_aspect_name
    
- r_assembled_from_id
    
- r_component_label
    
- r_composite_id
    
- r_composite_label
    
- r_content_size
    
- r_frozen_flag
    
- r_frzn_assembly_cnt
    
- r_has_events
    
- r_has_frzn_assembly
    
- r_immutable_flag
    
- r_is_public
    
- r_is_virtual_doc
    
- r_link_cnt
    
- r_link_high_cnt
    
- r_lock_machine
    
- r_order_no
    
- r_page_cnt
    
- r_resume_state
    
- resolution_label
    
- world_permit
    
## See also
<a name="BKMK_Section4"> </a>

#### Concepts

[Configure and use the Documentum connector in SharePoint Server](../search/configure-and-use-the-documentum-connector.md)

