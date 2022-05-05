---
title: "Plan for OneDrive in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 7/27/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_OneDriveAdmin
- IT_OneDriveAdmin_Top
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c033a091-2c08-4d20-8d3f-783317d718fa
description: "Learn about things you need to consider when planning to set up OneDrive in a SharePoint Server on-premises environment."
---

# Plan for Microsoft OneDrive in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
    
## OneDrive - Microsoft 365 or SharePoint Server
<a name="section1"> </a>

One of the first planning considerations you should make is if you truly want to use Microsoft OneDrive in SharePoint Server, or if you would be better suited to use OneDrive. Many companies select to use OneDrive in an on-premises environment due to industry restrictions (for example, finance or government), or business rules that prohibit transmitting their data over the internet. If your company isn't restricted by either, you should also explore the possibility of using OneDrive. The key benefits in using OneDrive is that you only need an internet connection to use it, versus being connected to your network, and that user storage is provided by your Microsoft 365 service.
  
> [!NOTE]
> For more info about OneDrive, see [What is OneDrive?](https://support.office.com/article/187f90af-056f-47c0-9656-cc0ddca7fdc2)
  
## Setting up OneDrive
<a name="section2"> </a>

To make OneDrive in SharePoint Server available to your users, you need to configure the following services in SharePoint Server Central Administration:
  
|**Required Service**|**What does it do?**|
|:-----|:-----|
|Managed Metadata service  <br/> |Manages metadata across all sites in your organization.  <br/> |
|User Profile Service Application  <br/> |Stores information about users, and is required for My Sites.  <br/> |
|My Sites  <br/> |Provides a personal site for individual users in an organization, and is where the user's document library resides.  <br/> |
   
> [!NOTE]
> For detailed info about how to set up each service as required for OneDrive, see [Set up OneDrive in a SharePoint Server on-premises environment](set-up-onedrive-for-business.md).
  
## Using the OneDrive sync app
<a name="section3"> </a>

The OneDrive [sync apps](https://go.microsoft.com/fwlink/?LinkId=522308) give users the convenience of local storage of their files. Sync apps also enable users to take documents offline. Users then can use those documents when they're disconnected from SharePoint Server. Later, when the client computer or device reconnects to SharePoint Server, the files are synchronized.
  
In a SharePoint Server on-premises environment, you may have the option to save directly to your document library (for example, from Office 2016), which is where files are synchronized from your OneDrive local folder anyway. When the OneDrive sync app is used in an on-premises environment, it's primary benefit is for synchronizing files on laptops that are used while disconnected from your corporate network at times, such as when traveling.
  
The sync app also provides your users the added convenience of working with files directly from the local OneDrive sync folder. Work with and saving your files directly in the folder is more convenient than opening your My Sites document library.
  
> [!IMPORTANT]
> Use the [previous OneDrive for Business sync app (Groove.exe)](/onedrive/install-previous-sync-app) to sync files in SharePoint Server 2016 or earlier. The new OneDrive sync app (OneDrive.exe) is supported only in SharePoint Server 2019. [Configure the OneDrive sync app for SharePoint Server 2019](../install/new-onedrive-sync-client.md)
  
 **Changes in file location**
  
If a user wants to change the location on their computer or device to which data is synchronized, they must stop synchronizing the folder and then set up a new synchronization. Setting up a new synchronization allows them to choose a new location.
  
Similarly, if you change the URLs of your SharePoint Server My Site host, users must stop the synchronization to the old location and set up a new synchronization to the new URL.
  
Stopping a synchronization and starting a new one to the same OneDrive library won't cause the loss of any data in the OneDrive library. But users must re-synchronize all files to their local computer or device. This process may take some time and shouldn't be interrupted.
  
 **Network bandwidth considerations**
  
There are several situations in which OneDrive sync apps can cause unusually high network bandwidth usage:
  
- When you first roll out OneDrive and users are synchronizing all of their files for the first time.
    
- When you change the URL of the My Site host and users are required to re-synchronize their files.
    
Be mindful of the potential impact of these changes on your network. 
  
## Data security
<a name="section4"> </a>

Sync apps use the http:// or https:// protocol of the site that they're synchronizing with to transfer data. If the OneDrive site uses a Secure Socket Layer (SSL) connection (https://), then the data being transferred by the sync app is encrypted; otherwise, it's not.
  
Microsoft 365 uses SSL for OneDrive connections by default. If you're using SharePoint Server, we recommend configuring your My Site host to use SSL for any connections that will occur outside your corporate domain. If you're using Active Directory directory services, you can configure the Group Policy setting **Sync Only On Domain Network**. The setting requires an SSL connection for OneDrive clients that connect to SharePoint Server from outside the organization's intranet.
  
Data on local disks on both server and Windows client computers can be encrypted by using [Windows BitLocker Drive Encryption](https://go.microsoft.com/fwlink/p/?LinkId=163122).
  
 **Data on local devices**
  
Once a document library is synchronized with a computer or mobile device, the files continue to exist there. Files remain on the computer or device even if the user's My Site and their user account are deleted. In this situation, although the files remain on the computer or device, the user can't synchronize the files with SharePoint Server again.
  
If storing files on a client workstation is against your corporate policy, you can [remove synchronization functionality from document libraries](../sharepoint-server.yml) in SharePoint Server. 
  
## Moving to a hybrid environment
<a name="section5"> </a>

At a later time, you might explore the possibility of using OneDrive for various reasons, such as keeping your on-premises sites and customizations in their current state, but offloading the personal storage aspect of it to the cloud. This would also provide your users access to their business files while not connected to the corporate network.
  
> [!NOTE]
> For more info about configuring a hybrid environment for OneDrive in SharePoint Server, see [Configure hybrid OneDrive - roadmap](../hybrid/configure-hybrid-onedrive-for-businessroadmap.md). 
  
## Upgrading from OneDrive in SharePoint Server
<a name="section6"> </a>

If you are using OneDrive in SharePoint Server, you can upgrade to OneDrive in SharePoint Server as part of the upgrade process. You can do this as part of the process to upgrade your My Sites Host site collection, which allows you the option to also upgrade the My Sites personal site collections, which are used to store your OneDrive user files.
  
> [!NOTE]
> For more info, see [Upgrade the My Site Host site collection](../upgrade-and-update/upgrade-my-sites.md#UMSH). 
