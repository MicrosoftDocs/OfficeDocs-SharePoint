---
title: Deciding to use RBS in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: c1f83b4f-a507-42f7-bd82-fed5404ed1ad
---


# Deciding to use RBS in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Outlines the costs and benefits of using Remote BLOB Storage (RBS) in a SharePoint Server 2016 and SharePoint Server 2013 environment.This article provides information to help you decide whether to use Remote BLOB Storage (RBS) in a SharePoint Server environment, and to understand the benefits and costs of using RBS.
> [!IMPORTANT:]

  
    
    

In SharePoint Server, a binary large object (BLOB) is a file, such as a Microsoft Office document or a video file. By default, these BLOBs, also named  *unstructured data*  , are stored inline in the SharePoint content database together with the metadata, or *structured data*  . Because BLOBs can be very large, it can be helpful to move BLOB data out of the SQL Server database, and onto commodity or content addressable storage. To do this, you can use RBS.
> [!NOTE:]

  
    
    

For more information about RBS including information about RBS providers, we highly recommend that you see  [Overview of RBS in SharePoint Server](html/overview-of-rbs-in-sharepoint-server.md).In this article:
-  [Limitations of RBS](#limitations)
    
  
-  [Optimal use of RBS](#optimal)
    
  
-  [Least effective use of RBS](#least_optimal)
    
  
-  [Implications of using RBS in different scenarios](#scenarios)
    
  
-  [Benefits and costs of using RBS](#benefits)
    
  
-  [Benefits and costs of using RBS with the FILESTREAM provider](#benefit_filestream)
    
  
-  [Implications of using RBS over the IT life cycle](#lifecycle)
    
  
-  [Evaluate provider options](#EvalProv)
    
  

## Limitations of RBS
<a name="limitations"> </a>

Each RBS provider has different capabilities and limitations. The FILESTREAM provider has the following limitations:
- RBS has specific content database size limits for specific scenarios. 
    
  
- Encryption is not supported on BLOBs, even if Transparent Data Encryption is enabled.
    
  
- RBS does not support using data compression.
    
  
- Support for database mirroring and log shipping is altered. For more information, see  [Evaluate provider options](#EvalProv) later in this article.
    
  
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
    
  
Under these conditions, even a content database that is less than 200 GB will produce a noticeable performance bottleneck as the small BLOBs are frequently accessed for writing. The bottleneck occurs because the database contains the metadata for the BLOBs. As the metadata is changed, new rows are added to the table in the database. This can cause the table to quickly become very large and large tables can decrease performance.Although the presence of many small BLOBs can decrease performance, the cost of storage is usually the most important consideration when you evaluate RBS. The predicted decrease in performance is usually an acceptable trade-off for the cost savings in storage hardware.
## Implications of using RBS in different scenarios
<a name="scenarios"> </a>

You should evaluate the implications of using RBS in different site scenarios. Because RBS was created to resolve specific problems, RBS might not perform equally well in all situations. The situations in the following sections are examples.
## Team sites

If you are considering using RBS with team sites or other highly-collaborative sites, and the sites typically contain documents smaller than 256 KB, you will not see significant gains by using RBS. Moreover, by using versioning, you can cause the content database to grow very quickly if documents are being revised frequently.
> [!IMPORTANT:]

  
    
    


## Record centers

RBS works well for record centers and other archive sites. Because these sites are mostly read-only and do not use versioning, you can store lots of data in the RBS store.
## Benefits and costs of using RBS
<a name="benefits"> </a>

This section discusses the benefits and costs of using RBS. These benefits and costs usually apply regardless of which provider you use. For more detailed information about how to use the FILESTREAM RBS provider, see  [Benefits and costs of using the FILESTREAM RBS provider](#benefit_filestream) later in this article. For more detailed information about how to use third-party RBS providers, contact the provider manufacturer.
## Benefits

RBS was designed to move the storage of BLOBs from databases on database servers to directories on commodity storage solutions. Therefore, under the specific environments that RBS was intended to be used in, you can experience performance or cost benefits. By using lower-priced storage instead of more expensive storage on a databases server, you can save on costs. RBS saves storage resources when there are fewer large BLOBs. When there are many smaller files, there is no benefit.
## Costs

RBS will increase operational costs because the IT staff must perform additional tasks when they back up or restore the content. Large RBS stores can slow down tasks such as backup or restore, updating the environment, upgrading to a newer version of SharePoint Server, or migrating the SharePoint sites to another environment. These costs should be considered when you evaluate whether to use RBS.
## Benefits and costs of using RBS with the FILESTREAM provider
<a name="benefit_filestream"> </a>

This section discusses the benefits and costs of using the FILESTREAM provider. These benefits and costs might not be relevant for another provider. For information about how to use third-party RBS providers, contact the provider manufacturer.
## Benefits

Microsoft currently supports only the FILESTREAM RBS provider with SharePoint Server. When you use this provider, the backup and restore features in SharePoint Server also back up and restore the BLOBs and the structured data in the content database without requiring you to do additional work. The FILESTREAM provider also supports Internet Small Computer System Interface (iSCSI) connected storage devices. For more information, see  [FILESTREAM Compatibility with Other SQL Server Features](http://go.microsoft.com/fwlink/p/?LinkID=733605&amp;clcid=0x409). 
## Costs

Using the FILESTREAM provider might increase operational costs because the IT staff must perform additional tasks. Large RBS stores can slow down tasks such as backup or restore, updating the environment, upgrading to a newer version of SharePoint Server, or migrating the SharePoint sites to another environment. These costs should be considered when you evaluate whether to use RBS.
## Implications of using RBS over the IT life cycle
<a name="lifecycle"> </a>

You should evaluate the implications of using RBS for the whole life cycle of the environment. What might be a good idea for normal operations, such as having large BLOB stores, might present challenges during backup and restore or during an upgrade. By evaluating the effects of using RBS and BLOB store size on the whole life cycle, you can avoid potential problems later.For example, using a remote RBS provider will require increased IT operations complexity and some cost increases. This is because the content database and the BLOB store must be backed up in synchronization to maintain references consistency.Another example is that in some cases upgrade operations will enumerate and possibly change each BLOB regardless of where the BLOBs are stored. 
## Setup

Using RBS can add some complexity to set up because you must install and configure the RBS provider on all Web servers in the farm. For more information about how to set up RBS, see  [Install and configure RBS with FILESTREAM in a SharePoint Server farm](html/install-and-configure-rbs-with-filestream-in-a-sharepoint-server-farm.md).
## Normal operations

You should consider the average file size and the kind of file access during normal operations. Although using RBS with files larger than 1 MB can improve I/O and processor performance, using RBS with files smaller than 256 KB might decrease overall performance. Storing the BLOBs inline in the content database is more efficient with smaller files.You should also consider how BLOB content will be used. If users will most frequently read the content but not revise it, RBS can provide performance gains. However, if users will frequently revise the content, using RBS will decrease performance. This is because extensive versioning will cause significant growth in both the metadata in the content database and the size of the BLOB store.You should weigh any storage cost benefits against potential operational cost increases.
## Monitoring and optimization

Using RBS also adds some operations overhead because there are several performance counters that are added to monitor RBS. Several options are available to tune RBS performance. For more information, see  [Maintain RBS in SharePoint Server](html/maintain-rbs-in-sharepoint-server.md).
## Database maintenance

You can achieve better efficiency and speed in database index defragmentation and statistics operations when you use RBS. Also regular consistency checks, such as DBCC checks, are also significantly faster when you use RBS.However, regular database maintenance will become more complex because you must configure and use the RBS Maintainer to maintain link-level consistency between the metadata and the BLOB store and to perform cleanup of orphaned BLOBs. For more information, see  [Maintain RBS in SharePoint Server](html/maintain-rbs-in-sharepoint-server.md).
## Backup and restore

If you use the local FILESTREAM provider with RBS, you can use built-in SharePoint tools to back up and restore. These operations back up and restore both the metadata and the BLOB store. If you use the remote RBS provider, you must carefully coordinate the backup and restore processes. This is because the backup and restore processes involve both the metadata and the BLOB store. You should take this into account when planning the RBS configuration. Not all RBS providers support backup and restore of BLOB data. You must check with the manufacturer of the provider to confirm support.You cannot use Microsoft System Center Data Protection Manager to back up and restore content that is stored in the RBS stores. 
## Upgrade and update

Under some circumstances, an upgrade, or even applying software updates, can enumerate and iterate through each object to include BLOB data regardless of where that data is stored. Therefore, upgrade operations will be similar in duration whether inline or remote BLOBs are used.
## Evaluate provider options
<a name="EvalProv"> </a>

RBS requires a provider that connects the RBS APIs and SQL Server. SQL Server 2014 Service Pack 1 (SP1), SQL Server 2008 Express and Microsoft SQL Server 2008 R2 Express include the FILESTREAM provider. 
> [!IMPORTANT:]

  
    
    

BLOBs can be kept on commodity storage such as direct-attached storage (DAS) or network attached storage (NAS), as supported by the provider. The FILESTREAM provider is supported by SharePoint Server 2016 when it is used on local hard disk drives or iSCSI drives only. You cannot use RBS with FILESTREAM on remote storage devices, such as NAS. The following list summarizes FILESTREAM benefits and limitations 
- SQL Server integrated backup and recovery of the BLOB Store works with the FILESTREAM provider. This works without the FILESTREAM provider, only if supported by the RBS provider that you are using.
    
  
- Scripted migration to BLOBs works with and without the FILESTREAM provider.
    
  
- Supports mirroring doesn't work with or without the FILESTREAM provider.
    
  
- Log shipping works with the FILESTREAM provider but doesn't work without the FILESTREAM provider.
    
  
- Database snapshots don't work with or without the FILESTREAM provider*.
    
  
- Geo replication works with the FILESTREAM provider but doesn't work without the FILESTREAM provider.
    
  
- Encryption works on NTFS only with the FILESTREAM provider. This works without the FILESTREAM provider, only if supported by the RBS provider that you are using.
    
  
- Local drives are supported with the FILESTREAM provider. This works without the FILESTREAM provider, with provider implementation.
    
  
- Network attached storage (NAS) works with the FILESTREAM provider but is only supported by SharePoint Server with iSCSI and if Time to First Byte is less than 20 milliseconds. This works without the FILESTREAM provider, with provider implementation.
    
  
- Direct attached storage (DAS) doesn't work with the FILESTREAM provider because it isn't supported by SharePoint Server. This works without the FILESTREAM provider, with provider implementation.
    
  
- Internet small computer system interface (iSCSI) works with the FILESTREAM provider. This works without the FILESTREAM provider, with provider implementation.
    
  
*If the RBS provider that you are using does not support snapshots, you cannot use snapshots for content deployment or backup. The FILESTREAM provider does not support snapshots.If the FILESTREAM provider is not practical for the environment, you can purchase a supported third-party provider. In this case, you should use the following criteria when you evaluate a provider:
- Backup and restore capability
    
  
- Tested disaster recovery
    
  
- Deployment and data migration
    
  
- Performance impact
    
  
- Long-term administrative costs
    
  

> [!IMPORTANT:]

  
    
    


# See also

#### 

 [Remote Blob Store (RBS) (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=733607&amp;clcid=0x409)
  
    
    
 [SQL Server Remote BLOB Store and FILESTREAM feature comparison](https://blogs.msdn.com/b/sqlrbs/archive/2009/11/18/sql-server-remote-blob-store-and-filestream-feature-comparison.aspx)
  
    
    

  
    
    

