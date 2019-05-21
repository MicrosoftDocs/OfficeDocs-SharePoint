---
title: "How to migrate your file share content to SharePoint Online using the Azure Data Box"
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
search.appverid: MET150
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
localization_priority: Normal
description: "Learn how to migrate your file share content to SharePoint Online using the Azure Data Box"
---

# Migrate your file share content to SharePoint Online using the Azure Data Box

Use the Azure Data Box and the SharePoint Migration Tool to easily migrate your file share content to SharePoint Online and OneDrive. By using the Data Box, you can remove dependency on your WAN link to transfer the data.  
The Microsoft Azure Data Box is a service that lets you order a device from the Microsoft Azure portal. You can then copy terabytes of data from your servers to the device. After shipping it back to Microsoft, your data is copied into Azure.  

## Requirements and costs

- Azure subscription:  Data Box is only available for Enterprise Agreement (EA), Cloud solution provider (CSP), or Pay-as-you-go subscription offers. If your subscription does not fall in any of the above types, contact Microsoft Support to upgrade your subscription or see [Azure subscription pricing](https://azure.microsoft.com/en-us/pricing/). 
- The minimum requirements for the SharePoint Migration Tool are here: [How to use the SharePoint Migration Tool](/sharepointmigration/how-to-use-the-sharepoint-migration-tool). 
- There is a nominal cost for the Azure Data Box.  For more information on the cost, see [Azure Data Box pricing](https://azure.microsoft.com/en-us/pricing/details/storage/databox/). 

## Workflow overview

1.	Order Azure Data Box. 
2.	Receive and configure Data Box.
3.	Copy your on-premises file share to Azure Data Box file share.
4.	Ship Data Box back per instructions and wait for the copy to complete.
5.	Create a VM in the Azure portal and mount the Azure file share on it.
6.	Install the SPMT tool on the Azure VM.
7.	Run the SPMT tool using the Azure file share as the SOURCE.
8.	Complete the final steps of the tool.
9.	Verify and confirm your data.


## Using the Azure Data Box
Once your receive your Azure Data Box, follow the instructions detailed here:  [Quickstart: Deploy Azure Data Box using the Azure portal](/azure/databox/data-box-quickstart-portal). They step you through how to set up and configure your Data Box and how to copy the content of your file shares to the device. Some things to keep in mind while doing this:
-	Only use the “StorageAccount_AzFile” share in the Data Box to copy the data. This is because you want the data to end up in an Azure file share, not in block blobs or page blobs.
-	The first level folder within this share corresponds to an Azure file share. Create a folder and then copy all your contents into it. This is the file share that you will mount on your VM in the next step.


## Migrating your data to SharePoint Online using SPMT
After you receive confirmation from the Azure data team that your data copy has completed, you can now proceed to migrate your data to SharePoint Online.  For best performance and connectivity, we recommend that you create an Azure Virtual Machine (VM).

1.	Sign into the Azure portal, and then create a virtual machine.  Learn how:  [Quickstart: Create Windows virtual machine in the Azure portal](/azure/virtual-machines/windows/quick-create-portal).
2.	[Mount the Azure file share onto that VM](/azure/storage/files/storage-how-to-use-files-windows).
3.	Download the SharePoint Migration tool and install it on your Azure VM. 
Download here: [SharePoint Migration Tool](http://spmtreleasescus.blob.core.windows.net/install/default.htm).
4.	Start the SharePoint Migration Tool.  Click Sign in and enter your Office 365 username and password.<br><br>![SharePoint Migration Tool](media/spmt-intro.png)

5.	When prompted “Where is your data?” select File share. Enter the path to your Azure file share where your data is located.
6.	Follow the remaining prompts as normal, including your target location. For more info see: [How to use the SharePoint Migration Tool](/sharepointmigration/how-to-use-the-sharepoint-migration-tool). 


> [!IMPORTANT]
> - The speed at which data is ingested into SharePoint Online is impacted by several factors, regardless if you have your data already in Azure. Understanding these factors will help you plan and maximize the efficiency of your migration.  For more info, read:  [SharePoint Online and OneDrive Migration Speed](/sharepointmigration/sharepoint-online-and-onedrive-migration-speed).
> - There is a risk of losing existing permissions on files when migrating the data to SharePoint Online. You may also lose certain metadata, such as “Created by” and “Date modified by”.

