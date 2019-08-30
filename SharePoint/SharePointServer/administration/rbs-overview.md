---
title: "Overview of RBS in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/9/2018
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: d359cdaa-0ebd-4c59-8fc5-002cba241b18
description: "Learn about how to use Remote BLOB Storage (RBS) in a SharePoint Server farm."
---

# Overview of RBS in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
This article describes how to use SharePoint Server together with Remote BLOB Storage (RBS) and SQL Server to optimize database storage resources.
  
Before you implement RBS, we highly recommend that you evaluate its potential costs and benefits. For more information and recommendations about how to use RBS in a SharePoint Server installation, see [Deciding to use RBS in SharePoint Server](rbs-planning.md).
  
> [!NOTE]
> Unless otherwise specified, the information in this article is specific to RBS using the FILESTREAM provider. For guidance specific to another provider, contact the provider manufacturer. 
  
    
## Introduction to RBS
<a name="Section2"> </a>

In SharePoint Server, a binary large object (BLOB) is a large block of data stored in a database that is known by its size and location instead of by its structure — for example a Office document or a video file. By default, these BLOBs, also known as unstructured data, are stored directly in the SharePoint content database together with the associated metadata, or structured data. Because these BLOBs can be very large, it might be better to store BLOBs outside the content database. BLOBs are immutable. Therefore, a new copy of the BLOB must be stored for each version of that BLOB. Because of this, as a database's usage increases, the total size of its BLOB data can expand quickly and grow larger than the total size of the document metadata and other structured data that is stored in the database. BLOB data can consume lots of space and uses server resources that are optimized for database access patterns. Therefore, it can be helpful to move BLOB data out of the SQL Server database, and onto commodity or content addressable storage. To do this, you can use RBS. 
  
RBS is a SQL Server library API set that is incorporated as an add-in feature pack that you can install when you install the following:
  
- SQL Server 2014 Service Pack 1 (SP1)
    
- SQL Server 2014
    
- SQL Server 2012
    
- SQL Server 2008 R2 Express
    
- SQL Server 2008 R2
    
- SQL Server 2008
    
The RBS feature enables applications, such as SharePoint Server, to store BLOBs in a location outside the content databases. Storing the BLOBs externally can reduce how much SQL Server database storage space is required. The metadata for each BLOB is stored in the SQL Server database and the BLOB is stored in the RBS store. 
  
SharePoint Server uses the RBS feature to store BLOBs outside the content database. SQL Server and SharePoint Server jointly manage the data integrity between the database records and contents of the RBS external store on a per-database basis.
  
RBS is composed of the following components: 
  
- **RBS client library**
    
    An RBS client library consists of a managed library that coordinates the BLOB storage with SharePoint Server, SQL Server, and RBS provider components.
    
- **Remote BLOB Storage provider**
    
    An RBS provider consists of a managed library and, optionally, a set of native libraries that communicate with the BLOB store.
    
    An example of an RBS provider is the SQL FILESTREAM provider. The SQL FILESTREAM provider is an add-in feature of SQL Server 2014 Service Pack 1 (SP1) that enables storage of and efficient access to BLOB data by using a combination of SQL Server 2014 (SP1) and the NTFS file system. For more information about FILESTREAM, see [FILESTREAM (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717991&amp;clcid=0x409) For information about how to enable and configure FILESTREAM, see [Enable and Configure FILESTREAM](http://go.microsoft.com/fwlink/p/?LinkID=717992&amp;clcid=0x409).
    
- **BLOB store**
    
    A BLOB store is an entity that is used to store BLOB data. This can be a content-addressable storage (CAS) solution, a file server that supports Server Message Block (SMB), or a SQL Server database.
    
## RBS providers
<a name="providers"> </a>

RBS uses a provider to connect to any dedicated BLOB store that uses the RBS APIs. SharePoint Server supports a BLOB storage implementation that accesses BLOB data by using the RBS APIs through such a provider. There are two kinds of RBS providers, local and remote. 
  
The location in which an RBS provider stores the BLOB data depends on the provider that you use. In the case of the FILESTREAM provider, the data is not stored in the .mdf file. Instead, it is stored in another folder that is associated with the database.
  
### Local RBS provider

A local provider stores the BLOBS outside the database but on the same server that is running SQL Server. You can conserve resources by using the local RBS FILESTREAM provider to put the extracted BLOB data on a different (that is, less resource-intensive) local disk. Because the BLOBs are stored in the same Filegroup as the metadata, SharePoint Server features, such as backup and restore in Central Administration, can be used.
  
The RBS FILESTREAM provider is available as an add-in when you install SQL Server 2014 Service Pack 1 (SP1). The RBS FILESTREAM provider uses the SQL Server FILESTREAM feature to store BLOBs in an additional resource that is attached to the same database and stored locally on the server. The FILESTREAM feature manages BLOBs in a SQL database by using the underlying NTFS file system. 
  
> [!IMPORTANT]
> The local FILESTREAM provider is supported only when it is used on local hard disk drives or an attached Internet Small Computer System Interface (iSCSI) device. You cannot use the local RBS FILESTREAM provider on remote storage devices such as network attached storage (NAS). 
  
### Remote RBS provider

A remote RBS provider stores the BLOBs on a separate server. This is typically on a separate volume on the same network as the database server.
  
Because the BLOBs are not stored in the same Filegroup with the metadata, some SharePoint Server features — for example, backup and restore in Central Administration — cannot be used with remote RBS providers. The metadata and the BLOBs must be managed separately. For more information about what features can be used with the provider, contact the provider manufacturer.
  
## Using RBS together with SharePoint Server
<a name="Section3"> </a>

SharePoint Server 2016 supports the FILESTREAM provider that is included in SQL Server 2014 (SP1). This version of RBS is included on the SQL Server installation media, but is not installed by the SQL Server Setup program..
  
SharePoint 2013 supports the FILESTREAM provider that is included in the SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2, SQL Server 2012, and SQL Server 2014. These versions of RBS are available at the following locations:
  
- [Microsoft SQL Server 2008 R2 Feature Pack](https://go.microsoft.com/fwlink/p/?LinkID=177388)
    
- [Microsoft SQL Server 2012 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=29065)
    
- [Microsoft SQL Server 2014 Feature Pack](https://www.microsoft.com/en-us/download/details.aspx?id=42295)
    
Be aware that SQL Server Remote BLOB Store installation package for SQL Server 2014 is the only version of RBS that is supported by SharePoint Server 2016. SQL Server Remote BLOB Store installation package from the Feature Pack for SQL Server 2008 R2 and later are the only versions of RBS that are supported by SharePoint 2013. Earlier versions are not supported. Third-party RBS providers can also be used with the RBS APIs to create a BLOB storage solution that is compatible with SharePoint Server.
  
In SharePoint Server, site collection backup and restore and site import or export will download the file contents and upload them back to the server regardless of which RBS provider is being used. This process is known as a deep copy. However, the FILESTREAM provider is the only provider that is currently supported for SharePoint Server farm database backup and restore operations.
  
To use RBS, you must install an RBS provider on each server where SharePoint Server is installed and on each database server in the topology. The provider includes a set of DLLs that implement methods for the RBS APIs and perform the actual operation of externalizing the BLOBs.
  
> [!NOTE]
> If Visio web services runs on SharePoint Server application servers that do not have an RBS provider installed, a Visio error occurs when you attempt to open a Visio diagram from this server. You must install an RBS client on SharePoint Server servers that run the Visio Graphics Service if you want to open Visio diagrams on that server. 
  
 **SharePoint Server 2016:** To run RBS on a remote server, you must be running SQL Server 2014 (SP1) Enterprise on the server that is running SQL Server where the metadata is stored in the database. 
  
If you plan to store BLOB data in an RBS store that differs from your SharePoint Server 2016 content databases, you must run SQL Server 2014 (SP1). This is true for all RBS providers.
  
 **SharePoint Server 2013:** To run RBS on a remote server, you must be running SQL Server 2008 R2, SQL Server 2012, or SQL Server 2014 Enterprise on the server that is running SQL Server where the metadata is stored in the database. 
  
If you plan to store BLOB data in an RBS store that differs from your SharePoint 2013 content databases, you must run SQL Server 2008 with SP1 and Cumulative Update 2, SQL Server 2012, or SQL Server 2014. This is true for all RBS providers.
  
The FILESTREAM provider that is recommended for upgrading from stand-alone installations of Windows SharePoint Services 3.0 that have content databases that are over 4 gigabytes (GB) to SharePoint 2013 associates data locally with the current content database, and does not require SQL Server Enterprise. 
  
> [!IMPORTANT]
> Although RBS can be used to store BLOB data externally, accessing or changing those BLOBs is not supported using any tool or product other than SharePoint Server. All access must occur by using SharePoint Server only. 
  
## See also
<a name="Section3"> </a>

#### Other Resources

[Binary Large Object (Blob) Data (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=733604&amp;clcid=0x409)
  
[FILESTREAM (SQL Server)](http://go.microsoft.com/fwlink/p/?LinkID=717991&amp;clcid=0x409)
  
[Remote BLOB Store Provider Library Implementation Specification](http://go.microsoft.com/fwlink/p/?LinkID=166066&amp;clcid=0x409)
  
[Install and configure RBS with SharePoint 2013 and SQL Server 2012](http://blogs.technet.com/b/bogdang/archive/2014/12/04/install-and-configure-rbs-with-sharepoint-2013-and-sql-server-2012.aspx)

