---
title: "Migration Manager FAQs"
recommendations: true
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
- M365-collaboration
- SPMigration
search.appverid: MET150
description: Migration Manager FAQs
---

# Frequently Asked Questions: Migration Manager

**Question:** Can I migrate content from SharePoint Server? </br>
Answer:   At this time, Migration Manager only supports the migration of **file shares**.  It does not support the migration of content from SharePoint Server.

**Question:** Can I run the SharePoint Migration Tool (SPMT) on the same computer that I have the Migration Manager agent installed?</br>
Answer:   Yes.

**Question:** Does the file share I am migrating need to be on a Windows computer?</br>
Answer:    No.  As long as you can access the file share from the migration agent, you can migrate it.

**Question:** Is multi-factor authentication supported by Migration Manager?</br>
Answer:    Microsoft multi-factor authentication is supported; however third party multi-factor authentication is not.

**Question:** Can I manually assign a task to a migration agent I have set up?</br>
Answer:   No. Migration Manager does it for you by automatically distributing tasks to the next available agent.

**Question:** Where are local Migration Manager logs stored?</br>
Answer: The logs are stored here:  `C:\Users\<Username>\AppData\Roaming\Microsoft\SPMigration`.

**Question:** When using the Migration Manager tool, is there a limit to the number of path characters you can enter?</br>
*Answer: Yes. When entering the **source path** into the text box, you are allowed a maximum of 255 characters.  However, during migration the **file path** can be up to 32,767 characters in length.  After it is migrated into SPO, the path is limited to 400 characters.

**Question:** Can I rename my temporary working folder?</br>
Answer: No, at this time the temporary working folder cannot be renamed.  It is  `%appdata%\Microsoft\SPMigration`.

**Question:** Can Migration Manager migrate content to non-English SharePoint sites?</br>
Answer: Yes, Migration Manager can migrate content to non-English sites as long as the site title doesn’t include non-EN characters.

**Question:** What happens when you "pause" a task?</br>
Answer: Pausing a task does not release the agent to another task. The agent remains unavailable to accept a new task until the task is resumed and completed, or if the task is deleted. 

**Question:** How long does an agent stay connected to Migration Manager?</br>
Answer:  The connection between an agent and Migration Manager stays active as long as the computer is still running and the SharePoint admin credentials that were used to sign into the agent are still valid. If the agent does becomes disconnected, the agent holds the token to the Migration Manager for up to 7 days. After which the agent will need to be reinstalled.

**Question:**  Is Migration Manager available for Government clouds?</br>
Answer:  Yes. Here's how you configure it: [Government cloud settings](https://docs.microsoft.com/sharepointmigration/mm-gov-cloud)

**Question:**   What’s the retention policy for the blog storage?</br>
Answer:  When using the Migration API, the customers/ISVs can either use the [SPO provided blob containers/queues](https://docs.microsoft.com/sharepoint/dev/apis/migration-api-azure-container-and-queue) or their containers/queues created within their Azure subscriptions. If you choose to use the SPO provided ones, you will get [SAS URIs](https://docs.microsoft.com/azure/storage/common/storage-sas-overview) to access those, which are valid for three days from creation for containers and 21 days for queues. After the SAS expiry, the content in the blob containers/queues will not be accessible. SPO backend jobs will delete the content in the container/queues within 30 to 90 days of the creation.
 
**Question:**  Is the data in the SPO provided containers encrypted?</br>
Answer: Yes. We mandate that the data uploaded to SPO provided containers must be encrypted using AES CBC to ensure the data is secure. To learn more, see: [OneDrive for Business and SharePoint Online Migration API encryption](Mhttps://docs.microsoft.com/sharepoint/dev/apis/migration-api-encryption).

**Question:**  Will my migration succeed if the temporary storage expires before content migration is complete?</br>
Answer: Yes. If your migration task was successful, your data will be migrated to SPO even if the temporary storage has expired.

**Question:**  Does running a migration slow down the tenant or impact SharePoint site performance while migrating? </br> 
Answer:  In general, site performance should not be impacted by running a migration.  There are many factors that prevent this from happening:
- Migration runs as a background activity and does not compete with end-user traffic
- SharePoint and OneDrive infrastructure has built-in throttling rules that project the reliability and availability of the system. To learn more about migration throughput and factors that affect migration speed, learn more at:  [General migration performance guidance](https://docs.microsoft.com/sharepointmigration/sharepoint-online-and-onedrive-migration-speed)

