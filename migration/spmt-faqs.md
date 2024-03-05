---
ms.date: 12/14/2023
title: "SharePoint Migration tool FAQs"
ms.reviewer: zhaosu
ms.author: heidip
author: MicrosoftHeidi
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


**Question:** Can the SharePoint Migration tool (SPMT) migrate content from one SharePoint tenant to another SharePoint tenant?</br>
Answer:  No. SPMT can migrate content from SharePoint on-premises Server, but not from another SharePoint Online tenant. However, a cross-tenant migration solution for SharePoint and OneDrive is available. Learn more at [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).

**Question:** How can I use SPMT to migrate a large amount of data to Microsoft 365?</br>
Answer: First, you need to install SPMT on physically different Windows computers or virtual machines. Then create bulk migration jobs on each SPMT instance, and then run them in parallel to achieve the maximum migration throughput. If you want to reach high throughput by orchestrating migration jobs automatically, use Migration Manager. 

**Question:** Where are local SPMT logs stored?</br>
Answer: SPMT logs are stored here: *C:\Users\<Username>\AppData\Roaming\Microsoft\MigrationTool*

**Question:** Is SPMT available for Government clouds?</br>
Answer: Yes. Learn how to configure your settings: [Government cloud settings](spmt-settings.md#government-cloud-support)

**Question**: Can I migrate only Site Pages?
Answer: Yes, However, site pages can only be migrated by uploading a CSV or JSON file.

**Question**: What authentication methods does SPMT support connecting to SharePoint Online?
Answer: SPMT only supports username & password.

**JSON Example**
>>>>>>> main


```javascript
{
  "Tasks": [
    {
      "SourcePath": http://source_path/sitename,
      "TargetPath": https://destination_path/sitename,
      "Items": {
        "Lists": [
          {
            "SourceList": "Site Pages",
            "TargetList": "Site Pages"
          }
        ],
        "SubSites": []
      },
      "MigrationType": "Content"
    }
  ]
}
```

**Question**: How can I preserve existing web parts on a destination site in site incremental migration?
Answer: Under the setting "Migration of web parts and pages", select "Don’t migrate to skip webpart migration" in incremental migration. Learn more: [**SharePoint Migration Tool Settings**](/sharepointmigration/spmt-settings#sharepoint).

**Question**: What features are not supported by SPMT for SharePoint on-premises Server migrations?
Answer: See items listed in table.

|Not supported|Description|
| -------- | -------- |
|Structure only migration|Users can't migrate a site without content.|
|Setting modern site template for destination|Users can't set the template for destination site. SPMT decides the destination site template based on the character of source site and destination site.|
|Migrate master pages|Master pages in a site or site collection migration can’t be migrated.|
|InfoPath forms|InfoPath forms can't be migrated.|
|Customer New/Edit/View forms|Customer New/Edit/View forms of a list or library can't be migrated along with its content.|
