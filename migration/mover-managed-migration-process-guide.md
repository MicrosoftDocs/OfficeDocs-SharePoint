---
title: "Managed migration process guide for use with Mover"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: A guide to help partners managing a customers migration project.
---
# Managed migration guide for use with Microsoft Mover 

This guide was created to share the process and best practices currently used by Microsoft when guiding a customer through a “managed migration”. A managed migration is a hands-on, high-touch service offered to customers who are wanting more guidance as they migrate from another cloud storage solution into Microsoft 365. The Mover application is used for this cloud to cloud migration.

Most migrations fall into regular phases as follows. Proven success factors for migration include planning, assessing and remediating, preparing your target environment, migrating, and onboarding your users.



> [!NOTE]
> The Mover Migration tool is a Microsoft owned migration tool available at no cost to subscribers of Microsoft 365.


   ![Migration process](media/migrationprocess-fileshare.png)

|**Migration planning**|**Assess and remediate**|**Prepare your OneDrive and SharePoint environment**|**Migrate**|**User onboarding**|
|:-----|:-----|:-----|:-----|:-----|
|What content goes where<br><br>Understanding permissions vs sharing<br><br>What to expect before and after<br><br>Migration and network performance considerations<br><br>Change management and communications|Assess key areas<br><br>Remediate issues|Pre-provision Microsoft 365 and users|Review migration offerings<br><br>Microsoft FastTrack services<br><br>Migration service providers|Send regular emails to users<br><br>Provide training<br><br>Let users know how they are impacted|


>[!Tip]
>Before starting a managed migration, we highly recommend reading and reviewing the current Mover documentation. This content provides valuable knowledge on how to understand the Mover tool for running migrations from various cloud storage platforms.
> See [Mover migration content](https://docs.microsoft.com/en-us/sharepointmigration/mover-plan-migration)



## Planning
The initial engagement is a fact-finding exchange between Partners and the customer. Both parties will be seeking to obtain as much information as possible from each other.

 Our role is to gain clarity on their project and provide guidance and confidence in our ability to deliver on customer needs. 

After your initial contact with your customer about migration, the next step is to arrange an “initial engagement” meeting to establish what the customer wants to achieve and the best practices to make that happen.

One of the first points to cover is whether the Mover tool can do the migration.  At present, our application  can migrate content from the  following cloud storage providers:

![mover connectors](media/mover-supported-connectors.png)

### Determine project scope

It is a considerable undertaking for customers to migrate their users, data, and files from their current cloud storage provider into Microsoft 365. Regardless of the company's size, customers look for experts to assist them in their migration project.

This guide helps you deliver the migration on their behalf with minimal effort and direct involvement on their part. 


Migrations come in all shapes and sizes. On our initial engagement with a customer, we focus on discovering the fundamental elements of their project. 

**Number of users to migrate**
Customers might have a relative idea of how many users are in their source domain and how many they plan to migrate. 
 
These are good initial stats to garner, but we still perform an inventory scan to obtain a more accurate count of a customer's user base. 
The scan results tell us how many users are in the domain and determine who owns the data, among other factors.

**Data ownership**
Much of a customer's userbase is shared data.  Mover only copies owned folders and the root files for each user.
 
If a user is not the owner of the data, we do not copy it.  Content can be automatically re-shared after it is migrated so that each user can access their content the same as before.
 
The Inventory Scan also helps determine who owns what. 

### Data distribution

Determining how a customer's data is distributed is also important. Usually, in the initial discussion, customers might not clearly see how their data is distributed.  The Inventory Scan will aid in obtaining that information.
 
As a rule, if a user that either owns more than 400,000 files/items or their storage size exceeds 5 TB, we recommend that those users be split into smaller service accounts. The data split between those and mapped accordingly between Source and Destination.  
 
Limiting the size of the users' accounts impacts processing and speed during migration.   

### Amount of files/data to migrate
Amount of files/data to Migrate
 
The number of files and data to migrate is closely associated with how the data is distributed. Customers may have an idea of many files or how much data they have in their source. However, sometimes reports provided by cloud storage providers on the exact numbers can be misleading. Content in the trash or externally shared data may be included in the count and give an inaccurate assessment. 
 
To obtain accurate totals for the number files and size of data owned, performing an  Inventory Scan is essential.
 
It is important to understand that Mover only copies files/folders/data owned by users within the Source tenant. 
The Mover tool does NOT migrate external shared data, email or items residing in the trash.
 
Migrations vary in size and adjustments need to be made accordingly.  Suppose a migration is over 100TB in size. We have processes to ensure that the migration will receive the best possible performance when migrating into Microsoft 365. 
 
### Migration Speeds
 
The most common question from customers is, "How long will the migration take?" It is hard to provide an accurate answer as to the time required to complete.
 
While using the Mover tool is one of the fastest ways to migrate data, the migration speed may still be affected by bottlenecks. These include, but aren't limited to:
 
#### The number of files and folders being moved.
The total number of files being moved has the biggest speed limit as it determines the total number of operations required. 
Most cloud storage providers limit their processing rate to one file per second per user. Though this is not entirely accurate, you can provide a useful baseline metric to your customer to estimate how long it might take.

#### File size 
Knowing file size is necessary to estimate transfer speed.  We have found that large file migration is substantially quicker than having to migrate lots of small files.
 
A transfer for a single user that owns 5 TB of data consisting of mostly large files will, on average, migrate faster than a user that owns 1 TB of data but has 1000s of small files.  The reason is that for each file, an API call is made against both the source and the destination. The greater the number of files, the greater number of calls, and will take longer than a handful of large files.

#### Total amount of data being moved

Though total data can affect speed, it is ultimately overshadowed by the number of files.  Many customers you encounter may be driven by how much data we are migrating on a daily basis but it is good to set expectations on how many files we are migrating in a day rather than data.

#### Server connections with the source or destination
Both Source and Destination connectors will have rate limits and we are beholden to how fast they allow us to download, upload and process data between the two.

#### Complexity of permissions or sharing of data
Applying permissions as part of the migration is another factor that can influence speed.  We are again making numerous API calls to apply permissions, which will increase the time it takes to migrate the data.

## Assessment & Remediation
## Prepare your environment
## Migrate process
## User onboarding

Best practices that will be discussed in this document include:

- Inventory scan:  Carrying out an initial inventory scan of source content.
- Data distribution:  Encouraging separation of large file/data owners for balanced Data Distribution.
- Customized destination folders:  Creation of specific destination upload folders for housing all migrated data.
- User and Permissions mappings:  Creating accurate User and Permission Mappings.
- Who Identifying who you need to migrate (users who owned data vs those that do not)
- Managing Customer Expectations for the Migration.
- Migration Transfer concurrency.
- How to troubleshoot the Migration.
- Customer Reporting via Scan Reports, Migration Reports and Migration Error Reports.

## Customer engagement

## Communication engagement
After the initial meeting with a prospective customer, it is essential to maintain a rhythm of business for moving forward. Customers will have many questions regarding various aspects of the migration process and providing them with clear and open communication channels is a must.

We recommend setting up a weekly meeting to discuss topics and to make forward progress on the migration. Tailor the types of communication that the customers may want to provide for their userbase to make them aware of the migration, timelines, and dos and don'ts during the process.
 
Establishing email threads and Microsoft Teams channels for the duration of the migration is also encouraged.
 
### Customer migration team

Who is the customer's migration team?  It is essential to establish the points of contact with the customer. 
Sometimes it may just be one person, but most large companies have dedicated people for the migration project.  Clearly defining and understanding each of their roles will aid in a smoother migration experience.
 
Provide the customer their primary point of contact is on our end and highlight any other representatives who may be assisting with the migration.
 
### Customer Reporting
When running a managed migration, it is important to note that Partners, MCS, and FastTrack will be running the migration.  The customer will not have direct access to the Mover tools during the migration.
 
By restricting access to Mover, you are ensuring that the migration is run by nominated people, and limits any potential customer interference during the process.

Though the customer might not have access that does not mean that they are not informed of status, potential issues and progress made.

We provide a daily Migration Report to keep them fully informed and the details of this report 


## Migration Considerations and Caveats PLANNING
Before starting any migration there are some considerations and caveats to consider.
General Migration planning

What gets transferred?
Only owned folders and the root files for each user will be copied. If a user is not the owner of the data they can access, the tool will not copy it.  

Content may be automatically reshared once it is migrated so that each user has access to their content exactly as before.

Does Mover sync files?

Mover offers a source-to-destination comparison, when you run a transfer, we compare the destination directory to the source and only transfer new or modified files over. We call this our incremental feature.
We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on.
Here are a few examples of how the tool deals with changes to files and folders.
Content changes: If a document is edited in your source or you have added a few new files, we will copy them to your destination on the next incremental run, overwriting the previously existing file(s) in the destination.
Name changes: If the name of a file or folder changes in Box, we will treat it as a brand new object. This can lead to duplicate files being migrated to Office 365, or worse: entire folders worth of data being duplicated from the changed folder downwards.
Example: Changing the path /Sales/Clients to /Global Sales/Clients will result in two copies of your Sales folder once the Global Sales folder is also copied during an incremental pass.

Does the Tool delete files?
The tool never deletes any data from any source. The tool simply takes a copy of the data from one place and copies it to another—akin to "copy and paste" rather than "cut and paste." The tool also does not retain any customer cloud storage data for any reason.

How data is handled.
When we transfer a file, via the tool, a temporary copy is downloaded from the Source connector (e.g. Box, GSuite) to a temporary server and then uploaded to Office 365.

Upon successful upload, the file is then deleted from the temporary server.  When the full migration is complete, that temporary server is decommissioned.  Any log data expires after 90 days and is never retained by Microsoft.

The tool does not perform any actions beyond copying files, folders and sharing permissions.  The tool does not have the ability to perform any kind of delete operations on either Source or Destination.

Transfer Management
When you start generating your transfer mappings it is best practice to only ever have 1 transfer for every user, team folder or shared drive.

You should NOT create duplicate transfers as this can lead to data duplication in the Destination.

Common practice should be a ratio of 1:1 for all transfers.

Example:
Source                                   Destination
username@company.com > [username]@company.com/[Upload Folder]

If a customer is splitting up large data owner accounts into multiple service accounts then each Source Service Account should have a corresponding Destination Service Account.

Example:
After an inventory scan user xyz@company.com owns over 500,000 files.

We would advise the customer to split this large user into 5 individual service accounts (100k files per account) for both Source and matching on the Destination (N.B. usually going into Office 365 we encourage customers to create SharePoint sites for this split data)

New Source Service Accounts          New Destination Service Accounts
Serviceaccount1-xyz@company.com >                Serviceaccount1-xyz@company.com/[Upload Folder]
Serviceaccount2-xyz@company.com >                Serviceaccount2-xyz@company.com/[Upload Folder]
Serviceaccount3-xyz@company.com >                Serviceaccount3-xyz@company.com/[Upload Folder]
Serviceaccount4-xyz@company.com >                Serviceaccount4-xyz@company.com/[Upload Folder]
Serviceaccount5-xyz@company.com >                Serviceaccount5-xyz@company.com/[Upload Folder]

OR
New Source Service Accounts         New Destination SharePoint Sites
Serviceaccount1-xyz@company.com >   https://company.sharepoint.com/sites/[Library1]/[Upload Folder]
Serviceaccount2-xyz@company.com >   https://company.sharepoint.com/sites/[Library2]/[Upload Folder]
Serviceaccount3-xyz@company.com >   https://company.sharepoint.com/sites/[Library3]/[Upload Folder]
Serviceaccount4-xyz@company.com >   https://company.sharepoint.com/sites/[Library4]/[Upload Folder]
Serviceaccount5-xyz@company.com >   https://company.sharepoint.com/sites/[Library5]/[Upload Folder]

**Destination Upload Folder**

When migrating into the Destination it is an essential practice to map an upload/destination folder for uploading the migrating data into.

The standard naming convention for an upload folder tends to be /From [connector type] (e.g. /From Box or /From GSuite). 

Example:
xyz@company.com > xyz@company.com/FromBox 

This clearly identifies where the data came from and ensures that it is separate from any other data that may already exist in the Office 365 Destination.

Also, by having an upload folder this ensures that permissions will be applied correctly for each user and on each SharePoint team site.

For SharePoint team sites and libraries, we are unable able to write permissions at the / level of the team site, so including this upload folder is a requirement.

Example:
xyz@company.com > https://company.sharepoint.com/sites/Library/FromBox

Once these mappings are created and we create and run the transfers then the upload folder (/From Box) is automatically created in the Destination.  The customer does not need to manually create these upload folders.

Two other considerations to impart to the customer is in naming the upload folder we want to keep the folder name short and succinct.  Due to the Microsoft character path limits we do not want to be adding unnecessary characters to the destination path.

Prior to starting and during the migration it should be clearly communicated to the customers userbase that users should not move, delete or rename any of the contents within the upload folder.

If users do so, then we run the risk of creating duplicate data when rerunning the transfers during incremental passes.

**Rearranging content during a migration**
We do not recommended customer rearranging or moving content during a migration.

Any major changes in directory structure should happen before or after the migration.
The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process will see all changes as new data. So, for example, if you change a folder name at the root, we will detect that as a new folder and all of the contents will be re-transferred including all subfolders.
When sharing permissions are transferred, both owners and collaborators will receive duplicate data if content has been rearranged or renamed.

**External Sharing Links**
The tool does not recreate external sharing links. These will need to be set manually in the Office 365 Destination by the customer after the migration completes.

**External Collaborators**
The tool does not share content with external collaborators. This policy is in place to protect the customers organization, and industry best practice is to never automatically share sensitive internal data with external users.

**File Versions**
The tool does not preserve file versions. Only the most recent version of a file will be migrated to Office 365 during a migration.
