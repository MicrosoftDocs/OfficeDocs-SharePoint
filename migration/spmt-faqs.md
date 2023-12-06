---
ms.date: 12/05/2023
title: "SharePoint Migration tool FAQs"
ms.reviewer: zhaosu
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- CSH
ms.topic: article
ms.service: microsoft-365-migration
mscollection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.localizationpriority: medium
search.appverid: MET150
description: "Learn more about what is frequently asked about the SharePoint Migration tool."
---

# Frequently asked questions:  SharePoint Migration tool (SPMT)


**Question:** Can the SharePoint Migration tool (SPMT) migrate content from one SharePoint tenant to another SharePoint tenant?
Answer:  No. SPMT can migrate content from SharePoint on-premises Server, but not from another SharePoint Online tenant. However, a cross-tenant migration solution for SharePoint and OneDrive is available. Learn more at [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).

**Question:** How can I use SPMT to migrate a large amount of data to Microsoft 365?
Answer: You need to install SPMT on physically different Windows computers or virtual machines. Then create bulk migration jobs on each SPMT instance, and then run them in parallel to achieve the maximum migration throughput. If you want to reach high throughput by orchestrating migration jobs automatically, use Migration Manager. 

**Question:** Where are local Migration Manager logs stored?
Answer: The logs are stored here: **C:\Users\<Username>\AppData\Roaming\Microsoft\MigrationTool**

**Question:** Is Migration Manager available for Government clouds?
Answer: Yes. Here's how you configure it: [Government cloud settings](spmt-install-issues#government-cloud-support)
