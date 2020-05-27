---
title: "Migration Manager FAQs"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
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
Answer: The logs are stored here:  C:\Users\<Username>\AppData\Roaming\Microsoft\SPMigration.

**Question:** When using the Migration Manager tool, is there a limit to the number of path characters you can enter?</br>
*Answer: Yes. When entering the **source path** into the text box, you are allowed a maximum of 255 characters.  However, during migration the **file path** can be up to 32,767 characters in length.  After it is migrated into SPO, the path is limited to 400 characters.

**Question:** Can I rename my temporary working folder?</br>
Answer: No, at this time the temporary working folder cannot be renamed.  It is  `%appdata%\Microsoft\SPMigration`. </br></br>

**Question:** Does Migration Manager work with non-English SharePoint sites?</br>
Answer: At this time, Migration Manager only supports English language SharePoint sites. </br></br>

**Question:** What happens when you "pause" a  task?</br>
Answer: Pausing a task does not release the agent to another task. The agent remains unavailable to accept a new task until the task is resumed and completed, or if the task is deleted. </br></br>

**Question:** How long does an agent stay connected to Migration Manager?</br>
Answer:  The connection between an agent and Migration Manager stays active as long as the computer is still running and the SharePoint admin credentials that were used to sign into the agent are still valid. If the agent does becomes disconnected, the agent holds the token to the Migration Manager for up to 7 days. After which the agent will need to be reinstalled.



