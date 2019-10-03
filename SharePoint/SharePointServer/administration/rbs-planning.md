---
title: "Deciding to use RBS in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/2/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c1f83b4f-a507-42f7-bd82-fed5404ed1ad
description: "Outlines the costs and benefits of using Remote BLOB Storage (RBS) in a SharePoint Server environment."
---

# Deciding to use RBS in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article provides information to help you decide whether to use Remote BLOB Storage (RBS) in a SharePoint Server environment, and to understand the benefits and costs of using RBS.
  
> [!IMPORTANT]
> RBS does **not** increase the storage limits of content databases. All limitations still apply to RBS-enabled content databases. RBS is intended to lower storage costs by allowing you to store large read-intensive BLOBs on less expensive drives. For example, if you have 150 GB of RBS data and you have a content database that is 70 GB, this still exceeds the limits. 
  
In SharePoint Server, a binary large object (BLOB) is a file, such as a Microsoft Office document or a video file. By default, these BLOBs, also named unstructured data, are stored inline in the SharePoint content database together with the metadata, or structured data. Because BLOBs can be very large, it can be helpful to move BLOB data out of the SQL Server database, and onto commodity or content addressable storage. To do this, you can use RBS.
  
> [!NOTE]
> Unless otherwise specified, the information in this article is specific to RBS using the FILESTREAM provider. For guidance specific to another provider, contact the provider manufacturer. 
  
For more information about RBS including information about RBS providers, we highly recommend that you see [Overview of RBS in SharePoint Server](rbs-overview.md).
  
    
## Limitations of RBS
<a name="limitations"> </a>

Each RBS provider has different capabilities and limitations. The FILESTREAM provider has the following limitations:
  
- RBS has specific content database size limits for specific scenarios. For more information about these limitations, see the "Content database limits" section in [Software boundaries and limits for SharePoint 2013](../install/software-boundaries-and-limits.md) and [Content database limits](../install/software-boundaries-and-limits-0.md#ContentDB).
    
- Encryption is not supported on BLOBs, even if Transparent Data Encryption is enabled.
    
- RBS does not support using data compression.
    
- Support for database mirroring and log shipping is altered. For more information, see [Evaluate provider options](#EvalProv) later in this article. 
    
To determine the capabilities and limitations of third-party providers, contact the provider manufacturer.
  
## Optimal use of RBS
<a name="optimal"> </a>

Because RBS is a solution created for a specific set of conditions, there is point at which the benefits of using RBS outweigh the costs. The optimal environment for using RBS is one in which the following conditions are true:
  
- You want to store fewer large BLOBs (256 KB or larger) for read-intensive or read-only access.
    
- The resources on the computer that is running SQL Server might become a performance bottleneck.
    
- The expense of high-cost drive space is greater than the expense of increased IT operational complexity that the use of RBS might be introduce.
    
## Least effective use of RBS
<a name="least_optimal"> </a>

RBS is not a good solution for all environments because, in specific environments, the costs will outweigh the benefits. The least beneficial environment for using RBS is one where the following conditions are true:
  
- You want to store many small BLOBs (256 KB or less) for write-intensive access.
    
- The resources on the computer that is running SQL Server are not a performance bottleneck.
    
- The expense of increased IT operational complexity that the use of RBS might introduce is greater than high-cost drive space.
    
Under these conditions, even a content database that is less than 200 GB will produce a noticeable performance bottleneck as the small BLOBs are frequently accessed for writing. The bottleneck occurs because the database contains the metadata for the BLOBs. As the metadata is changed, new rows are added to the table in the database. This can cause the table to quickly become very large and large tables can decrease performance.
  
Although the presence of many small BLOBs can decrease performance, the cost of storage is usually the most important consideration when you evaluate RBS. The predicted decrease in performance is usually an acceptable trade-off for the cost savings in storage hardware.
  
## Implications of using RBS in different scenarios
<a name="scenarios"> </a>

You should evaluate the implications of using RBS in different site scenarios. Because RBS was created to resolve specific problems, RBS might not perform equally well in all situations. The situations in the following sections are examples.
  
### Team sites

If you are considering using RBS with team sites or other highly-collaborative sites, and the sites typically contain documents smaller than 256 KB, you will not see significant gains by using RBS. Moreover, by using versioning, you can cause the content database to grow very quickly if documents are being revised frequently.
  
> [!IMPORTANT]
> The use of RBS-enabled content databases larger than 200GB with collaboration sites is not supported. You cannot upload any document larger than 2GB to an RBS-enabled content database. For more information about RBS limits, see the "Content database limits" section in [Software boundaries and limits for SharePoint 2013](../install/software-boundaries-and-limits.md) and [Content database limits](../install/software-boundaries-and-limits-0.md#ContentDB). 
  
### Record centers

RBS works well for record centers and other archive sites. Because these sites are mostly read-only and do not use versioning, you can store lots of data in the RBS store.
  
## Benefits and costs of using RBS
<a name="benefits"> </a>

This section discusses the benefits and costs of using RBS. These benefits and costs usually apply regardless of which provider you use. For more detailed information about how to use the FILESTREAM RBS provider, see [Benefits and costs of using RBS with the FILESTREAM provider](#benefit_filestream) later in this article. For more detailed information about how to use third-party RBS providers, contact the provider manufacturer. 
  
### Benefits

RBS was designed to move the storage of BLOBs from databases on database servers to directories on commodity storage solutions. Therefore, under the specific environments that RBS was intended to be used in, you can experience performance or cost benefits. By using lower-priced storage instead of more expensive storage on a databases server, you can save on costs. RBS saves storage resources when there are fewer large BLOBs. When there are many smaller files, there is no benefit.
  
### Costs

RBS will increase operational costs because the IT staff must perform additional tasks when they back up or restore the content. Large RBS stores can slow down tasks such as backup or restore, updating the environment, upgrading to a newer version of SharePoint Server, or migrating the SharePoint sites to another environment. These costs should be considered when you evaluate whether to use RBS.
  
## Benefits and costs of using RBS with the FILESTREAM provider
<a name="benefit_filestream"> </a>

This section discusses the benefits and costs of using the FILESTREAM provider. These benefits and costs might not be relevant for another provider. For information about how to use third-party RBS providers, contact the provider manufacturer.
  
### Benefits

Microsoft currently supports only the FILESTREAM RBS provider with SharePoint Server. When you use this provider, the backup and restore features in SharePoint Server also back up and restore the BLOBs and the structured data in the content database without requiring you to do additional work. The FILESTREAM provider also supports Internet Small Computer System Interface (iSCSI) connected storage devices. For more information, see [FILESTREAM Compatibility with Other SQL Server Features](http://go.microsoft.com/fwlink/p/?LinkID=733605&amp;clcid=0x409). 
  
### Costs

Using the FILESTREAM provider might increase operational costs because the IT staff must perform additional tasks. Large RBS stores can slow down tasks such as backup or restore, updating the environment, upgrading to a newer version of SharePoint Server, or migrating the SharePoint sites to another environment. These costs should be considered when you evaluate whether to use RBS.
  
## Implications of using RBS over the IT life cycle
<a name="lifecycle"> </a>

You should evaluate the implications of using RBS for the whole life cycle of the environment. What might be a good idea for normal operations, such as having large BLOB stores, might present challenges during backup and restore or during an upgrade. By evaluating the effects of using RBS and BLOB store size on the whole life cycle, you can avoid potential problems later.
  
For example, using a remote RBS provider will require increased IT operations complexity and some cost increases. This is because the content database and the BLOB store must be backed up in synchronization to maintain references consistency.
  
Another example is that in some cases upgrade operations will enumerate and possibly change each BLOB regardless of where the BLOBs are stored. 
  
### Setup

Using RBS can add some complexity to set up because you must install and configure the RBS provider on all Web servers in the farm. For more information about how to set up RBS, see [Install and configure RBS with FILESTREAM in a SharePoint Server farm](install-and-configure-rbs.md).
  
### Normal operations

You should consider the average file size and the kind of file access during normal operations. Although using RBS with files larger than 1 MB can improve I/O and processor performance, using RBS with files smaller than 256 KB might decrease overall performance. Storing the BLOBs inline in the content database is more efficient with smaller files.
  
You should also consider how BLOB content will be used. If users will most frequently read the content but not revise it, RBS can provide performance gains. However, if users will frequently revise the content, using RBS will decrease performance. This is because extensive versioning will cause significant growth in both the metadata in the content database and the size of the BLOB store.
  
You should weigh any storage cost benefits against potential operational cost increases.
  
### Monitoring and optimization

Using RBS also adds some operations overhead because there are several performance counters that are added to monitor RBS. Several options are available to tune RBS performance. For more information, see [Maintain RBS in SharePoint Server](maintain-rbs.md).
  
### Database maintenance

You can achieve better efficiency and speed in database index defragmentation and statistics operations when you use RBS. Also regular consistency checks, such as DBCC checks, are also significantly faster when you use RBS.
  
However, regular database maintenance will become more complex because you must configure and use the RBS Maintainer to maintain link-level consistency between the metadata and the BLOB store and to perform cleanup of orphaned BLOBs. For more information, see [Maintain RBS in SharePoint Server](maintain-rbs.md).
  
### Backup and restore

If you use the local FILESTREAM provider with RBS, you can use built-in SharePoint tools to back up and restore. These operations back up and restore both the metadata and the BLOB store. If you use the remote RBS provider, you must carefully coordinate the backup and restore processes. This is because the backup and restore processes involve both the metadata and the BLOB store. You should take this into account when planning the RBS configuration. Not all RBS providers support backup and restore of BLOB data. You must check with the manufacturer of the provider to confirm support.
  
You cannot use Microsoft System Center Data Protection Manager to back up and restore content that is stored in the RBS stores. 
  
### Upgrade and update

Under some circumstances, an upgrade, or even applying software updates, can enumerate and iterate through each object to include BLOB data regardless of where that data is stored. Therefore, upgrade operations will be similar in duration whether inline or remote BLOBs are used.
  
## Evaluate provider options
<a name="EvalProv"> </a>

RBS requires a provider that connects the RBS APIs and SQL Server. SQL Server 2014 Service Pack 1 (SP1), SQL Server 2008 Express and Microsoft SQL Server 2008 R2 Express include the FILESTREAM provider. 
  
> [!IMPORTANT]
> RBS can be run on the local computer that is running SQL Server 2014 (SP1), SQL Server 2008 R2, SQL Server 2008 or SQL Server 2008 R2 Express. To run RBS on a remote server, you must be running SQL Server 2008 R2 Enterprise. SharePoint Server 2016 requires you to use the version of RBS that is included with the SQL Server 2014 (SP1). Earlier versions of RBS will not work with SharePoint Server 2016. 
  
> [!IMPORTANT]
> SharePoint Server 2013 requires you to use the version of RBS that is included with the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2. Earlier versions of RBS will not work with SharePoint 2013. In addition, RBS is not supported in SQL Server 2005. 
  
BLOBs can be kept on commodity storage such as direct-attached storage (DAS) or network attached storage (NAS), as supported by the provider. The FILESTREAM provider is supported by SharePoint Server 2016 when it is used on local hard disk drives or iSCSI drives only. You cannot use RBS with FILESTREAM on remote storage devices, such as NAS. 
  
The following table summarizes FILESTREAM benefits and limitations. 
  
|**Operational requirement**|**With the FILESTREAM provider**|**Without the FILESTREAM provider**|
|:-----|:-----|:-----|
|SQL Server integrated backup and recovery of the BLOB Store  <br/> |Yes  <br/> |Only if supported by the RBS provider that you are using.  <br/> |
|Scripted migration to BLOBs  <br/> |Yes  <br/> |Yes  <br/> |
|Supports mirroring  <br/> |No  <br/> |No  <br/> |
|Log shipping  <br/> |Yes  <br/> |Yes, with provider implementation  <br/> |
|Database snapshots  <br/> |No<sup>\*</sup> <br/> |No<sup>\*</sup> <br/> |
|Geo replication  <br/> |Yes  <br/> |No  <br/> |
|Encryption  <br/> |NTFS only  <br/> |Only if supported by the RBS provider that you are using.  <br/> |
|Local drives supported  <br/> |Yes  <br/> |Yes, with provider implementation  <br/> |
|Network attached storage (NAS)  <br/> |Only supported by SharePoint Server with iSCSI and if Time to First Byte is less than 20 milliseconds.  <br/> |Yes, with provider implementation  <br/> |
|Direct attached storage (DAS)  <br/> |Not supported by SharePoint Server  <br/> |Yes, with provider implementation  <br/> |
|Internet small computer system interface (iSCSI)  <br/> |Yes  <br/> |Yes, with provider implementation  <br/> |
   
<sup>\*</sup>If the RBS provider that you are using does not support snapshots, you cannot use snapshots for content deployment or backup. The FILESTREAM provider does not support snapshots.
  
If the FILESTREAM provider is not practical for the environment, you can purchase a supported third-party provider. In this case, you should use the following criteria when you evaluate a provider:
  
- Backup and restore capability
    
- Tested disaster recovery
    
- Deployment and data migration
    
- Performance impact
    
- Long-term administrative costs
    
> [!IMPORTANT]
> We do not recommend that you develop a provider unless you are an independent software vendor (ISV) that has significant development experience in designing storage solutions. 
  
## See also
<a name="EvalProv"> </a>

#### Other Resources

[Remote Blob Store (RBS) (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=733607&amp;clcid=0x409)
  
[SQL Server Remote BLOB Store and FILESTREAM feature comparison](https://blogs.msdn.com/b/sqlrbs/archive/2009/11/18/sql-server-remote-blob-store-and-filestream-feature-comparison.aspx)

