---
ms.date: 03/18/2021
title: "Migration Manager Dropbox FAQs"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Migration Manager Dropbox FAQs
---

# Frequently Asked Questions: Migration Manager Dropbox


**Question:**  **Is Migration Manager Dropbox available for GCC, GCCHigh, DoD tenants?**</br>
Answer.  No. Migration Manager Dropbox isn't available for any of the Government clouds.
</br>

**Question:**   **What gets transferred?**</br>
Answer: Only owned folders and the root files for each user are copied. If a user isn't the owner of data they can access, we don't copy it. Content may be automatically reshared after it's migrated so that each user has access to their content exactly as before.
</br>

**Question:**   **Does Migration Manager Dropbox sync files?**</br>
Answer: There's a source-to-destination delta; when you run a transfer, we compare the destination directory to the source, and only transfer new or modified files over. We call this our incremental feature. We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on.  Here are a few examples of how we deal with changes to files and folders.

- **Content changes**: If a document is edited in your source or you have added a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing file(s) in the destination.

- **Name changes**: If the name of a file or folder changes in Office 365, we treat it as a brand new object. This can lead to duplicate files being migrated to Office 365, or worse in that entire folders worth of data would be duplicated from the changed folder downwards.

- **Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.
</br>

**Question:**   **Does Migration Manager delete my files?**</br>
Answer: No. We never delete your data from any source. We simply take your data from one place and copy it to another; akin to *copy and paste* rather than *cut and paste.* We also don't retain any of your cloud storage data for any reasons. 

</br>

**Question:**   **Can I rearrange content during a migration?**</br>
Answer:  Not recommended. Any major changes in directory structure should happen before or after your migration. It's also not a good idea to use our app to rearrange content.  The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is retransferred, including all subfolders.  When sharing permissions are transferred, both owners and collaborators receive duplicate data if content has been rearranged or renamed.
</br>

**Question:**   **What happens to external sharing links?**</br>
Answer:  We don't recreate external sharing links. After migration, these have to be set in the destination manually.</br>

**Question:**   **What about external collaborators?**</br>
Answer:  We don't share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external users.</br>

**Question:**   **Does Migration Manager preserve file versions?**</br>
Answer:  No. During a migration, only the most recent version of a file is transferred.</br>

**Question:**   **Does Migration Manager automatically notify users?**</br>
Answer:  No.  We automatically suppress all emails to users so they aren't bombarded with excessive notifications about the data they now have access to.</br>

