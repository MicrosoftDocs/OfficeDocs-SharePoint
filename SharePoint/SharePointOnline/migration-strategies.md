---
title: "Migration strategies for moving to Microsoft Purview risk and compliance solutions from older information management and records management for SharePoint"
f1.keywords:
- NOCSH
ms.author: kyrachurney
author: kyracatwork
manager: roygles
ms.date: 5/16/2014
audience: Admin
ms.topic: overview
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- WSU150
- SPO160
- OSU150
- MET150
ms.assetid: 63a0b501-ba59-44b7-a35c-999f3be057b2
ms.collection:
- purview-compliance
- Tier3
ms.custom:
- seo-marvel-apr2020
description: "This article explains how to plan your migration, understand the modern solution, and decide which modern solution to use."
---

# Migration strategies for moving to Microsoft Purview risk and compliance solutions from older information management and records management for SharePoint 

Before you begin, it's important to plan your migration. You may need to interact with multiple stakeholders within your organization depending on the use case. It's important for you to carefully design your migration strategy. We've provided a few examples to help guide your next steps. 

## Prepare for using Purview risk and compliance solutions 

1. Review your existing older policies and decide which ones you need to recreate in the modern features. Confirm your goals for compliance and which of the features you’re using today to meet those needs. For example, you may have a business requirement to keep your content in some SharePoint sites for one year and are using Information Management policies today to accomplish this requirement. This review can also be an opportunity to audit your retention schedule and identify if there are any duplicate, outdated, or conflicting policies that you may not want to recreate. 

1. Use this guide to understand what you need to do, identify the older feature and behavior you’re migrating from, and decide which modern feature to use. It's also recommended to confirm that you have the applicable licenses for the modern features. Learn more about [licensing for Data Lifecycle Management and Records Management.](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

    You may be eligible for a free trial of Microsoft Purview risk and compliance solutions, including premium Data Lifecycle Management and Records Management features. See [free trial.](/purview/compliance-easy-trials) 

1. Configure your modern features. Implement the strategies defined in your plan and set up the modern features that meet your requirements. 

1. Verify that your new features are working as expected: 

    - Wait for the [applicable time period for your new features to take effect](/purview/retention?branch=main&branchFallbackFrom=pr-en-us-5917&tabs=table-overriden) 
    - [Confirm policies applied to a location using policy lookup](/purview/retention?tabs=table-overriden&branch=main) 
    - [Use activity explorer to review actions related to labeling content](/purview/data-classification-activity-explorer?branch=main)
    - [Use content explorer to review labeled items](/purview/data-classification-content-explorer?branch=main)
    - [Check the policy status for errors](/microsoft-365/troubleshoot/retention/identify-errors-in-retention-and-retention-label-policies)
    
## Older features and using Purview features instead 

### Record center site 


|Older feature  |Purview feature suggestion  |
|---------|---------|
|[Record Center site templates](https://support.microsoft.com/en-us/office/create-a-records-center-6bf1488b-62a8-486c-90dd-54b6bcce4b3a#:~:text=You%20need%20to%20take%20the%20following%20steps%20to,on%20the%20Records%20Center%20site.%20...%20See%20More.) helps organizations implement their records management and retention programs.    |<ul><li> [Create a communication site to replace the records center.](https://support.microsoft.com/en-us/office/create-a-team-or-communication-site-551e190a-8fbe-47ae-a88a-798b443c46b1)<li> Use Data Lifecycle Management for [retention policies that retain or delete content.](/purview/create-retention-policies?tabs=teams-retention)  <li> Use Records Management for retention labels that: <br><ul><li>[Apply by default](/purview/create-apply-retention-labels?tabs=manual-outlook%2Cdefault-label-for-sharepoint) to items within a library, folder, or document set.<li>[Auto-apply to content](/purview/apply-retention-labels-automatically)</li><li>[Classify contents as records](/purview/declare-records)</br></ul></li>  |

### Submit records to the record center 


|Older feature   |Purview feature suggestion   |
|---------|---------|
|[The record collection programmable interface](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) (commonly referred to as “send to” location) enables organizations to automatically submit files to a SharePoint site.      | Configure [PowerAutomate](/power-automate/getting-started) to [route records automatically to your new communication site.](/dynamics365/customer-service/routing-trigger-automatic)        |
 
### Content Organizer 

|Older feature   |Purview feature suggestion   |
|---------|---------|
|[Content Organizer](https://support.microsoft.com/en-us/office/configure-the-content-organizer-to-route-documents-b0875658-69bc-4f48-addb-e3c5f01f2d9a) automatically routes content to a location in a SharePoint site. |To route content, including records, to locations within your sites:<br><ul> <li> Configure [PowerAutomate](/power-automate/getting-started) to route content automatically to your sites.<li>[Create a rule in Syntex that moves or copies files in document libraries.](/microsoft-365/syntex/content-processing-create-rules)</li><li>Use [Audit (standard)](/purview/audit-solutions-overview?view=o365-worldwide&preserve-view=true) to maintain logs.</li><br></ul>       |

### Information Management policies 

|Older feature  |Purview feature suggestion  |
|---------|---------|
|[Information Management policies](intro-to-info-mgmt-policies.md) allow for schedules to be defined on a library and its folders, or to site content types. | <ul><li> Use Data Lifecycle Management for [retention policies that retain or delete content.](/purview/create-retention-policies?tabs=teams-retention%22%20%5Ct%20%22_blank)<li>Use Data Lifecycle Management or Records Management for:<br><ul> <li> [Retention labels](/purview/create-retention-labels-data-lifecycle-management) that are [applied by default to content in a folder or library.](/purview/create-apply-retention-labels?tabs=manual-outlook%2Cdefault-label-for-sharepoint)<li> [Automatically apply](/purview/apply-retention-labels-automatically) to specified [content types](/microsoft-365/community/auto-apply-retention-labels-in-office-365-using-content-types-and-metadata).<li>[Customizing what happens at the end of the retention period.](/purview/retention-label-flow)<li>[Managing single and multi-stage disposition of content.](/purview/disposition?view=o365-worldwide&preserve-view=true)</br></ul> </li><li>Use [PowerAutomate](/power-automate/getting-started) to [route content automatically using custom flow.](/dynamics365/customer-service/routing-trigger-automatic)<li>Use [Audit (standard).](/purview/audit-solutions-overview?view=o365-worldwide%22%20%5Cl%20%22audit-standard%22%20%5Ct%20%22_blank&preserve-view=true) to maintain logs of events and operations performed.<li>To include information on a file (policy labels), [create and publish sensitivity labels.](/purview/create-sensitivity-labels?view=o365-worldwide&preserve-view=true) that apply [content marking](/purview/sensitivity-labels-office-apps).</ul></li> 	       |

### Document deletion policies 


|Older feature  |Purview feature suggestion  |
|---------|---------|
|Document deletion policies permanently delete content from a site after a specified period of time.      |Use Data [Lifecycle Management](https://support.microsoft.com/en-us/office/create-a-document-deletion-policy-in-sharepoint-server-2016-4fe26e19-4849-4eb9-a044-840ab47458ff?ui=en-us&rs=en-us&ad=us) for [retention policies that retain or delete content.](/purview/create-retention-policies?tabs=teams-retention%22%20%5Ct%20%22_blank)          |


### In-place Records Management 


|Older feature  |Purview feature suggestion |
|---------|---------|
|[In-place records management](https://support.microsoft.com/en-us/office/configuring-in-place-records-management-7707a878-780c-4be6-9cb0-9718ecde050a#:~:text=If%20not%20already%20done%2C%20you%20need%20to%20activate,features%20%2C%20find%20In%20Place%20...%20See%20More) specifies restrictions on documents declared as records. [Vault abilities](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) allow administrators to prevent the direct tampering with records, track version changes, and audit actions.     |<ul><li>Use Records Management for retention labels that:<br><ul> <li> Are [published for users to manually apply.](/purview/create-apply-retention-labels?tabs=manual-outlook%2Cdefault-label-for-sharepoint&branch=main) <li>[Auto-apply to content.](/purview/apply-retention-labels-automatically?branch=main)<li>[Classify contents as records to prevent tampering and add additional audit actions.](/purview/declare-records?branch=main)<li>[Take action during and at the end of the content lifecycle.](/purview/file-plan-manager?branch=main)</br></ul></li><li>Use [Audit (standard)](/purview/audit-solutions-overview?view=o365-worldwide&preserve-view=true&branch=main) to maintain logs.</ul></li>|


