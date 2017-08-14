---
title: Plan enterprise search architecture in SharePoint Server 2016
ms.prod: SHAREPOINT
ms.assetid: 2b2c3b2a-49f3-4c96-9efd-0d557f0332db
---


# Plan enterprise search architecture in SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2016-12-30* **Summary:** Learn how to plan an enterprise search architecture.Before you set up your enterprise search architecture, there are quite a few things that require careful planning. Step by step, we’ll help you to plan a small, a medium, large, or an extra large-size enterprise search architecture.Are you familiar with the components of the search system in SharePoint Server 2016, and how they interact? By reading  [Overview of search architecture in SharePoint Server](html/overview-of-search-architecture-in-sharepoint-server.md) and [Search architectures for SharePoint Server 2016](https://download.microsoft.com/download/2/0/8/2081E053-4E56-4B87-87A4-9380D042B95D/SP_2016_Search_Architecture_Model.pdf) before you get going, you’ll become familiar with search architecture, search components, search databases, and the search topology. When planning a search architecture, here are some suggestions about what to consider:
1.  [Step 1: How much content do I have?](#BKMK_Step1)
    
  
2.  [Step 2: What size search architecture for how much content?](#BKMK_Step2)
    
  
3.  [Step 3: Which hardware requirements should I be aware of?](#BKMK_AssignHW)
    
  -  [Choose to run the servers physically or virtually](#BKMK_ChoosePhysicalVirtual)
    
  
  -  [Choose hardware resources for the host servers](#BKMK_ChooseHWResources)
    
  
  -  [Plan storage performance](#BKMK_Storage_performance)
    
  
  -  [Choose how your search architecture supports high availability](#BKMK_HiAvail)
    
  
4.  [Step 4: How to check that my search architecture performs well?](#BKMK_ConfirmTestPerf)
    
  -  [Test the storage I/O subsystem](#BKMK_TestIOSystem)
    
  
  -  [Test the search performance](#BKMK_TestSearchPerf)
    
  

## Step 1: How much content do I have?
<a name="BKMK_Step1"> </a>

The volume of content that you have in your search index affects what resources you need to host the farm. Work out approximately the number of items that you plan on making searchable. Here are some examples of items: documents, web pages, SharePoint list entries, and images. Remember that each entry in a SharePoint list counts as one item.When you have established a figure, multiply it by what you think the expected growth of that content will be over the next 12 months.For example, if you’re starting out with 12,000 indexed items, and you expect the volume of that content to triple over the next 12 months. You should plan for 36,000 searchable items.
## Step 2: What size search architecture for how much content?
<a name="BKMK_Step2"> </a>

It’s not always easy to assess how big or small to make your search architecture. The size of your search architecture depends on the volume of your content, the crawl rate, the query throughput, and the level of high availability that you require. There are sample search architectures that we advise using as a basis to plan your own farm. The sample search architecture that you choose depends on how much content has to be searchable:
### 

Volume of contentSample search architecture0-20 million items  <br/> Small search farm  <br/> 0-80 million items  <br/> Medium search farm  <br/> 0-200 million items  <br/> Large search farm  <br/> 0-500 million items  <br/> Extra large search farm  <br/> Although these sample search architectures use virtual machines, you can use both physical servers and virtual machines according to the strategy of the overall SharePoint Server 2016 solution of your search architecture.
## Small search farm
<a name="SmallFarmDescription"> </a>

If you have up to 20 million items, the small search farm will probably be the most suitable farm for you. We've estimated that this search architecture can crawl 50 documents per second, and serve in the order of 10 queries per second. With a crawl rate of 50 documents per second, it takes search 110 hours to crawl 20 million items in the first full crawl.
  
    
    
![Diagram of the servers and search components in the small enterprise search architecture sample](images/)
  
    
    

  
    
    

  
    
    

## Medium search farm
<a name="MediumFarmDescription"> </a>

If you have between 20 and 80 million items, the medium search farm will probably be the most suitable farm for you. We've estimated that this search architecture can crawl 100 documents per second, and serve in the order of 10 queries per second. With a crawl rate of 200 documents per second, it takes search 280 hours to crawl 80 million items in the first full crawl.
  
    
    
![Diagram of the servers and search components in the medium enterprise search architecture sample](images/)
  
    
    

  
    
    

  
    
    

## Large search farm
<a name="LargeFarmDescription"> </a>

If you have between 80 and 200 million items, the large search farm will probably be the most suitable farm for you. We've estimated that this search architecture can crawl 200 documents per second, and serve in the order of 10 queries per second. With a crawl rate of 200 documents per second, it takes search 280 hours to crawl 200 million items in the first full crawl.
  
    
    
![Diagram of the servers and search components in the large enterprise search architecture sample](images/)
  
    
    

  
    
    

  
    
    

## Extra large search farm
<a name="LargeFarmDescription"> </a>

If you have up to 500 million items, a farm similar to the extra large search farm is a good starting point. Microsoft tested this search architecture and measured that it can crawl 300-500 documents per second, and serve in the order of 10 queries per second. With a crawl rate of 500 documents per second, it takes search about 300 hours to crawl 500 million items in the first full crawl.Creating a search farm of this size requires you to carefully plan and tune the farm to get the performance you want. You might find it advantageous to seek expert guidance. It’s also important to plan how to back up and restore a search farm of this size, and how to recover the farm if your data center has a major outage. We recommend that you practice backup, restore and recovery.
  
    
    
![Diagram of the servers and search components in the extra large enterprise search sample.](images/)
  
    
    

  
    
    

  
    
    

## Step 3: Which hardware requirements should I be aware of?
<a name="BKMK_AssignHW"> </a>

Now that you’ve determined the volume of your content and chosen a sample search architecture, the next step is to plan the hardware you’ll need, as described in this section:
-  [Choose to run the servers physically or virtually](#BKMK_ChoosePhysicalVirtual)
    
  
-  [Choose hardware resources for the host servers](#BKMK_ChooseHWResources)
    
  -  [Plan general storage for the host servers](#BKMK_GenStorage)
    
  
  -  [Minimum hardware resources for the small search farm](#BKMK_MinHWSmall)
    
  
  -  [Minimum hardware resources for the medium search farm](#BKMK_MinHWMedium)
    
  
  -  [Minimum hardware resources for the large search farm](#BKMK_MinHWLarge)
    
  
  -  [Minimum hardware resources for the extra large search farm](#BKMK_MinHWExtraLarge)
    
  
-  [Plan storage performance](#BKMK_Storage_performance)
    
  -  [Choose storage](#BKMK_ChooseStoragePerf)
    
  -  [Search component IOPS requirements](#BKMK_SearchCompIOPS)
    
  
  -  [Search database IOPS requirements](#BKMK_SearchDBIOPS)
    
  
-  [Choose how your search architecture supports high availability](#BKMK_HiAvail)
    
  

## Choose to run the servers physically or virtually
<a name="BKMK_ChoosePhysicalVirtual"> </a>

If you’re using one of the small, medium or large-size architectures that we’ve tested for you, then you’ll be running your search architecture on virtual machines. Note also that although a virtual environment is easier to manage, its performance level can sometimes be slightly lower than that of a physical environment. A physical server can host more search components on the same server than a virtual server. You’ll find useful guidance in **Overview of farm virtualization and architectures for SharePoint 2013**.It’s also possible to run your search architecture on physical servers. In the sample farm architectures, just move the search components from the virtual machines to the host server and take away the virtual machines. Each physical server can host up to four index components, but only one of each type of the other search components. If you for example change the medium sample search architecture to use physical servers, you’ll find that you have two content processing components on Host E. The solution is to take away one of the content processing components. This works because crawling, processing of content, and processing of analytics depend on the amount of resources that are available, not the number of content processing components.
  
    
    
![Choose to run the servers physically or virtually](images/)
  
    
    

  
    
    

  
    
    

## Choose hardware resources for the host servers
<a name="BKMK_ChooseHWResources"> </a>

Each search component and search database requires a minimum amount of hardware resources from the host server to perform well. But, the more hardware resources you have, the better the performance of your search architecture will be. So it’s a good idea to have more than the minimum amount of hardware resources. The resources each search component requires depends on the workload, mostly determined by the crawl rate, the query rate, and the number of indexed items.For example, when hosting virtual machines on Windows Server 2008 R2 Service Pack 1 (SP1), you can’t use more than four CPU cores per virtual machine. With Windows Server 2012 or newer, you use eight or more CPU cores per virtual machine. Then you can scale out with more CPU cores for each virtual machine instead of scaling up with more virtual machines. Set up servers or virtual machines that host the same search components, with the same hardware resources. Let’s use the index component as an example. When you host index partitions on virtual machines, the virtual machine with the weakest performance determines the performance of the overall search architecture.
#### General storage
<a name="BKMK_GenStorage"> </a>

Make sure that each host server has enough disk space for the base installation of the Windows Server operating system and for the SharePoint Server 2016 program files. The host server also needs free hard disk space for diagnostics such as logging, debugging, and creating memory dumps, for daily operations, and for the page file. Normally, 80 GB of disk space is enough for the Windows Server operating system and for the SharePoint Server 2016 program files.Add storage for the SQL log space for each database server. If you don’t set the database server to back up the databases often, the SQL log space uses lots of storage. For more information about how to plan SQL databases, see  [Storage and SQL Server capacity planning and configuration (SharePoint Server)](html/storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md) .The minimum storage that the analytics reporting database requires can vary. This is because the amount of storage depends on how users interact with SharePoint Server 2016. When users interact frequently, there usually are more events to store. Check the amount of storage your current search architecture uses for the analytics database, and assign at least this amount for your redesigned topology.
#### Minimum hardware resources for the small search farm
<a name="BKMK_MinHWSmall"> </a>

This table shows the minimum amount of hardware resources that each application server or database server needs.
### 

ServerOn hostStorageRAMProcessor1Network bandwidthApplication server that has query processing and index components.  <br/> A, B  <br/> 500 GB2 <br/> 32 GB2 <br/> 1.8 GHz 8x CPU cores2 <br/> 1 Gbps  <br/> Application server that has crawl, search administration, analytics and content processing components.  <br/> A, B  <br/> 200 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Database server that has all search databases.  <br/> C, D  <br/> 100 GB  <br/> 16 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> 1The number of CPU cores is specified here, not the number of CPU threads.2You can use four CPU cores,16 GB RAM, and 300 GB storage, but then each index component can maximum hold 10 million items. That reduces the number of items this search farm can hold by two. 
#### Minimum hardware resources for the medium search farm
<a name="BKMK_MinHWMedium"> </a>

This table shows the minimum amount of hardware resources that each application server or database server needs.
### 

ServerOn hostStorageRAMProcessor1Network bandwidthApplication server that has query processing and index components.  <br/> A, B, C, D  <br/> 500 GB2 <br/> 32 GB2 <br/> 1.8 GHz 8x CPU cores2 <br/> 1 Gbps  <br/> Application server that has an index component.  <br/> A, B, C, D  <br/> 500 GB2 <br/> 32 GB2 <br/> 1.8 GHz 8x CPU cores2 <br/> 1 Gbps  <br/> Application server that has analytics and content processing components.  <br/> E, F  <br/> 300 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Application server that has crawl, search administration, and content processing components.  <br/> E, F  <br/> 100 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Database server that has all search databases.  <br/> G, H  <br/> 400 GB  <br/> 16 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> 1The number of CPU cores is specified here, not the number of CPU threads.2You can use four CPU cores,16 GB RAM, and 300 GB storage, but then each index component can maximum hold 10 million items. That reduces the number of items this search farm can hold by two. 
#### Minimum hardware resources for the large search farm
<a name="BKMK_MinHWLarge"> </a>

This table shows the minimum amount of hardware resources that each application server or database server needs.
### 

ServerOn hostStorageRAMProcessor1Network bandwidthApplication server that has query processing and index components.  <br/> A, B, C, D, E, G, H  <br/> 500 GB2 <br/> 32 GB2 <br/> 1.8 GHz 8x CPU cores2 <br/> 1 Gbps  <br/> Application server that has an index component.  <br/> A, B, C, D, E, F, G, H, I, J  <br/> 500 GB2 <br/> 32 GB2 <br/> 1.8 GHz 8x CPU cores2 <br/> 1 Gbps  <br/> Application servers that have analytics and content processing components  <br/> K, L, M, N  <br/> 300 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Application servers that have crawl and search administration components  <br/> K, L  <br/> 100 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Database server that have search databases  <br/> O, P, Q, R  <br/> 500 GB  <br/> 16 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> 1The number of CPU cores is specified here, not the number of CPU threads.2You can use four CPU cores,16 GB RAM, and 300 GB storage, but then each index component can maximum hold 10 million items. That reduces the number of items this search farm can hold by two. 
#### Minimum hardware resources for the extra large search farm
<a name="BKMK_MinHWExtraLarge"> </a>

This table shows the minimum amount of hardware resources that each application server or database server needs.
### 

ServerOn hostStorageRAMProcessor1Network bandwidthApplication server that has index components.  <br/> A-X  <br/> 500 GB  <br/> 32 GB  <br/> 1.8 GHz 8x CPU cores  <br/> 1 Gbps  <br/> Application server that has query processing and index components.  <br/> Y, Z  <br/> 500 GB  <br/> 32 GB  <br/> 1.8 GHz 8x CPU cores  <br/> 1 Gbps  <br/> Application servers that have crawl, search administration, or content processing components  <br/> AA-AF  <br/> 100 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Application servers that have analytics processing components  <br/> AG, AH  <br/> 800 GB  <br/> 8 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> Database servers that have search databases  <br/> AI-AL  <br/> 500 GB  <br/> 16 GB  <br/> 1.8 GHz 4x CPU cores  <br/> 1 Gbps  <br/> 1The number of CPU cores is specified here, not the number of CPU threads.
## Plan storage performance
<a name="BKMK_Storage_performance"> </a>

The speed of the storage affects the search performance. Make sure that the storage you have is fast enough to handle the traffic from the search components and databases. Disk speed is measured in I/O operations per second (IOPS).The way you decide to distribute data from the search components and from the operating system across your storage, has an impact on search performance. It's a good idea to:
- Split the Windows Server operating system files, the SharePoint Server 2016 program files, and diagnostics logs across three separate storage volumes or partitions with normal performance.
    
  
- Store the search component data on a separate storage volume or partition with high performance.
    
    > [!NOTE:]
      

#### Choose storage
<a name="BKMK_ChooseStoragePerf"> </a>

For an overview of storage architectures and disk types, see  [Storage and SQL Server capacity planning and configuration (SharePoint Server)](html/storage-and-sql-server-capacity-planning-and-configuration-sharepoint-server.md). The servers that host the index or analytics processing components, or search databases, require storage that can maintain low latency, while providing sufficient I/O operations per second (IOPS). The following tables show how many IOPS each of these search components and databases require.If you deploy shared storage like SAN/NAS, the peak disk load of one search component typically coincides with the peak disk load of another search component. To get the number of IOPS search requires from the shared storage, you need to add up the IOPS requirement of each of these components.
##### Search component IOPS requirements

### 

Component nameComponent detailsIOPS requirementsUse of separate storage volume/partitionIndex component  <br/> Uses storage when merging the index and when handling and responding to queries.  <br/>  300 IOPS for 64 KB random reads. <br/>  100 IOPS for 256 KB random writes. <br/>  200 MB/s for sequential reads. <br/>  200 MB/s for sequential writes. <br/> Yes  <br/> Analytics component  <br/> Analyzes data locally, in bulk processing.  <br/> No  <br/> Yes  <br/> Crawl component  <br/> Stores downloaded content locally, before it sends it to a content processing component. Storage is limited by network bandwidth.  <br/> No  <br/> Yes  <br/> 
##### Search database IOPS requirements

### 

Database nameIOPS requirementsTypical load on I/O subsystem.Crawl database  <br/> Medium to high IOPS  <br/> 10 IOPS per 1 document per second (DPS) crawl rate.  <br/> Link database  <br/> Medium IOPS  <br/> 10 IOPS per 1 million items in the search index.  <br/> Search administration database  <br/> Low IOPS  <br/> Not applicable.  <br/> Analytics reporting database  <br/> Medium IOPS  <br/> Not applicable.  <br/> 
## Choose how your search architecture supports high availability
<a name="BKMK_HiAvail"> </a>

If you aren’t familiar with high availability strategies, here's an article that will get you started:  [Create a high availability architecture and strategy for SharePoint Server](html/create-a-high-availability-architecture-and-strategy-for-sharepoint-server.md). Your search architecture supports high availability when you host redundant search components and databases on separate fault domains. All of the sample search architectures host redundant search components on independent servers.For each redundant host server in your search architecture, you should plan to install:
1. Redundant networking
    
  
2. Redundant power supplies with independent wiring or an uninterruptable power supply (UPS).
    
  

## Step 4: How to check that my search architecture performs well?
<a name="BKMK_ConfirmTestPerf"> </a>

Before you deploy your search architecture to a production environment, you'll need to check that it performs well. Here's a checklist of what to do:
1. Test that the index components use a storage I/O subsystem that has enough IOPS. See  [Test the storage I/O subsystem](#BKMK_TestIOSystem).
    
  
2. Deploy the search architecture to a pilot environment. Make sure that the pilot environment is representative of the production environment.
    
  
3. Test the search performance of the pilot environment. See  [Test the search performance](#BKMK_TestSearchPerf)
    
  
For an overview of testing in general in SharePoint , see **Performance testing for SharePoint Server 2013**.
## Test the storage I/O subsystem
<a name="BKMK_TestIOSystem"> </a>

To test the storage I/O subsystem, run the most important disk operations and measure the IOPS. You can use the SQLIO tool to run these tests. See  [SQLIO Disk Subsystem Benchmark Tool](https://www.microsoft.com/downloads/details.aspx?familyid=9a8b005b-84e4-4f24-8d65-cb53442d9e19).
#### Set up the test environment
<a name="BKMK_SetTestEnvironment"> </a>

You don’t need to set up the whole search architecture, or install SharePoint Server 2016. It's enough to set up a test environment that produces a realistic workload for the storage I/O subsystem.Let's consider the case for local storage. For example, if host A in the medium search farm uses a local disk, you need to install the two virtual machines and run the disk operation tests on both virtual machines at the same time.You need a different set-up for shared storage. If for example the workload from all the index components in the medium search farm plus other unrelated workloads share the same storage, you need to:
1. Install the eight virtual machines in host A, B, C, and D, and set up the sources of the unrelated workloads.
    
  
2. Make sure that the unrelated workload is applied to the shared storage at the same time as you run simultaneous disk operation tests on all the virtual machines in host A, B, D, and D.
    
  

#### Create a test file
<a name="BKMK_CreateTestFile"> </a>


1. Create a 1 GB test file by using the command sqlio.exe -t32 -s1 -b256 1g. This command creates a file named "1g".
    
  
2. Save the test file on the storage device that you want to test. For example: on the hard disk of Host A in the medium farm.
    
  
3. Concatenate the test file to a sufficiently large test file. For example: 256 GB, with the command copy 1g+1g+1g+...+1g testfile.
    
  
4. Restart the server. This will ensure that caching does not skew the test results.
    
  

#### Run tests
<a name="BKMK_CreateTestFile"> </a>

It's a good idea to measure:
- The performance of medium sized random accesses (see test number one and two below).
    
  
- Read and write throughput for large transfers (see test number three and four below).
    
  
The table below shows the SQLIO commands that you should use to run each test. All the commands assume that the "testfile" exists in the current directory. Each test runs for 300 seconds.
### 

Test numberScopeCommand1  <br/> 64 KB read [IOPS]  <br/> sqlio.exe -kR -t4 -o25 -b64 -frandom -s300 testfile  <br/> 2  <br/> 256 KB write [IOPS]  <br/> sqlio.exe -kW -t4 -o25 -b256 -frandom -s300 testfile <br/> 3  <br/> 100 MB read [MB/s]  <br/> sqlio.exe -kR -t1 -o1 -b100000 -frandom -s300 testfile  <br/> 4  <br/> 100 MB write [MB/s]  <br/> sqlio.exe -kW -t1 -o1 -b100000 -frandom -s300 testfile <br/> 
##### Example results for local disk storage
The sample results in the table below show a deployment where at least 50 percent of the disk subsystem capacity was in use before adding the test file.The disk controller and the spindles of the disk strongly influence these results.If you test on empty disks, you’ll get elevated results because the test file will be in the most optimal tracks across all spindles (short stroking). This can increase performance by up to two or three times. You’ll get unrealistically high results if you test a hard disk that optimizes away accesses on uninitialized storage space, or storage containing all zeros, for example dynamic VHD/VHDX files. In this case, use a very large test file that contains real data, rather than generating a synthetic test file using SQLIO commands.
### 

Disk layout  <br/> Test 1  <br/> Test 2  <br/> Test 3  <br/> Test 4  <br/>  <br/> Recommended minimum IOPS during ordinary operations  <br/> 300  <br/> 100  <br/> 200  <br/> 200  <br/>  <br/> 4x 1 TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size)  <br/> 1181  <br/> 206  <br/> 284  <br/> 296  <br/>  <br/> 8x 1TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size)  <br/> 2082  <br/> 337  <br/> 610  <br/> 645  <br/>  <br/> 16x 1TB 7200 RPM NLSAS in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size)  <br/> 3763  <br/> 595  <br/> 1173  <br/> 1181  <br/>  <br/> 16x 1TB 7200 RPM NLSAS in RAID50 (2x8) on Dell H710 RAID controller (64kB stripe size, 64kB block size)  <br/> 3613  <br/> 545  <br/> 1139  <br/> 1164  <br/>  <br/> 16x 1TB 7200 RPM NLSAS in RAID10 on Dell H710 RAID controller (256kB stripe size, 64kB block size)  <br/> 4030  <br/> 1146  <br/> 970  <br/> 775  <br/>  <br/> 4x SmartStorage Optimus 800GB SSDs in RAID5 on Dell H710 RAID controller (64kB stripe size, 64kB block size)  <br/> 32385  <br/> 3781  <br/> 1714  <br/> 1319  <br/>  <br/> 4x SmartStorage Optimus 800GB SSDs in RAID0 on Dell H710 RAID controller (256kB stripe size, 64kB block size)  <br/> 31747  <br/> 7149  <br/> 1643  <br/> 1798  <br/>  <br/> 
## Test the search performance
<a name="BKMK_TestSearchPerf"> </a>

Here’s a checklist of what to do to test your search architecture:
1.  [Choose content to run tests on](#BKMK_ChooseContentTests)
    
  
2.  [Choose terms and phrases to test query performance](#BKMK_ChooseTerms)
    
  
3.  [Measure search performance](#BKMK_MeasureSearchPerf)
    
  

#### Choose content to run tests on
<a name="BKMK_ChooseContentTests"> </a>

Choose content that represents your production content well. If you choose content that’s only there for test purposes, make sure you’ve got different types of items, not just one item that you’ve duplicated many times. The reason for this is that the query processor will spend time detecting duplicated items, which will affect search performance, and your results won’t be representative of a production environment.Set up one or more content sources to crawl the content. Verify that you have the required user account and network access.
#### Choose terms and phrases to test query performance
<a name="BKMK_ChooseTerms"> </a>

The number of results you get for a query is called the recall.To test query performance, you’ll first need to create a set of terms and phrases to use as queries. Alternatively, collect queries from an existing installation. Make sure that the set contains terms and phrases that have low recall and high recall, and that the terms and phrases are relevant to your environment.
##### Examples

- If you search for a product number in a product catalog, it’s likely that there’s only one number for one product. Therefore, you’ll get your search results fast. This is low recall.
    
  
- If you search for a common term like "presentation" on a company intranet, it’s likely that you’ll get many results, and it may take longer to get them. This is high recall.
    
  
- If, for example, your content is related to human resources, use search terms that relate to this area.
    
  

#### Measure search performance
<a name="BKMK_MeasureSearchPerf"> </a>

SharePoint Server 2016 collects search performance measurements in the Crawl Health Reports and Query Health Reports. You can find these reports in Central Administration, under Search Administration.It's a good idea to measure search performance first with a synthetic load, and then with a small set of live users, and live content. When you use live users and live content, you can observe how the search architecture is performing. If your content increases faster than you intended, it might be worth considering using the next size search architecture. Or, if your users are more active than anticipated, then we suggest that you increase the amount of storage space of the analytics database.
