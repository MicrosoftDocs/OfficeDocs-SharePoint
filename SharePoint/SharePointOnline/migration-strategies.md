---
title: "Migration strategies for moving to Microsoft Purview risk and compliance solutions from older retention features for SharePoint and OneDrive"
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
description: Learn how to use Microsoft Purview risk and compliance solutions instead of the older information management and records management features in SharePoint and OneDrive.
---

# Migration strategies for moving to Microsoft Purview risk and compliance solutions from older retention features for SharePoint and OneDrive 

Before you begin, it's important to plan your migration. You may need to interact with multiple stakeholders within your organization depending on the use case. It's important for you to carefully design your migration strategy. We've provided a few examples to help guide your next steps.

## Prepare for using Purview risk and compliance solutions 

1. Plan your policies and decide which ones you need to recreate in the modern solution. Confirm your goals for compliance and which of the features you’re using today meet those needs. For example, you may have a business requirement to keep your content in some SharePoint sites for one year and are using Information Management policies today to accomplish this. This can also be an opportunity to audit your file plan and identify if there are any duplicate or conflicting policies that you may not want to recreate. 

1. Use this guide to understand what you need to do in the modern solution, identify the older feature and behavior you’re migrating from, and decide which modern feature to use. It's also recommended to confirm that you have the applicable licenses for the modern features. Learn more about [licensing for Data Lifecycle Management and Records Management.](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

    You may be eligible for a free trial of Microsoft Purview risk and compliance solutions, including premium Data Lifecycle Management and Records Management features. see [free trial.](/purview/compliance-easy-trials) 

1. Configure your modern features. Implement the strategies defined in your plan and set up the modern features that meet your requirements. 

1. Verify that your new features are working as expected: 

    - Wait for the [applicable time period for your new features to take effect](/purview/retention?tabs=table-overriden) 
    - [Confirm policies applied to a location using policy lookup](/purview/retention?tabs=table-overriden) 
    - [Use activity explorer to review actions related to labeling content](/purview/data-classification-activity-explorer)  
    - [Use content explorer to review labeled items](/purview/data-classification-content-explorer) 
    - [Check the policy status for errors](/microsoft-365/troubleshoot/retention/identify-errors-in-retention-and-retention-label-policies)
    
## Records Center features and using Purview features instead 

### Create a record center site 

[This older feature](https://support.microsoft.com/en-us/office/create-a-records-center-6bf1488b-62a8-486c-90dd-54b6bcce4b3a#:~:text=You%20need%20to%20take%20the%20following%20steps%20to,on%20the%20Records%20Center%20site.%20...%20See%20More.) helps organizations implement their records management and retention programs.
 
#### Purview feature suggestion 

- [Create a team or communication site](https://support.microsoft.com/en-us/office/create-a-team-or-communication-site-551e190a-8fbe-47ae-a88a-798b443c46b1) 

- Use Data Lifecycle Management for [retention policies that retain or delete content](/purview/create-retention-policies?tabs=teams-retention)  

- Use Records Management for retention labels that:
 
    - Are [published for users to manually apply](/purview/create-apply-retention-labels?tabs=manual-outlook%2Cdefault-label-for-sharepoint) 
    - [Auto-apply to content](/purview/apply-retention-labels-automatically) 
    - [Classify contents as records](/purview/declare-records)

### Submit records to the record center  

[This older feature](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) enables organizations to automatically submit files to a SharePoint site. 

#### Purview feature suggestion 

- Use [PowerAutomate](/power-automate/getting-started) to [route records automatically using custom flow.](/dynamics365/customer-service/routing-trigger-automatic)

### Content Organizer 

[This older](https://support.microsoft.com/en-us/office/configure-the-content-organizer-to-route-documents-b0875658-69bc-4f48-addb-e3c5f01f2d9a) feature automatically routes content to a location in a SharePoint site.

#### Purview feature suggestion 

To route document to different libraries or folders, upload all documents to a Drop Off Library, manage folder size, and manage duplicate submissions: 

- Use [PowerAutomate](/power-automate/getting-started) to [route records automatically using custom flow](/dynamics365/customer-service/routing-trigger-automatic)
- Use [Audit (standard)](/purview/audit-solutions-overview?view=o365-worldwide) to maintain logs 

### Vault abilities 

[This older](https://support.microsoft.com/en-us/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) feature allows administrators to prevent the direct tampering with records, tracking version changes, and auditing actions. 

#### Purview feature suggestion 

- Use Records Management for retention labels that: 

    - Are [published for users to manually apply](/purview/create-apply-retention-labels?tabs=manual-outlook%2Cdefault-label-for-sharepoint) 
    - [Auto-apply to content](/purview/apply-retention-labels-automatically)
    - [Classify contents as records](/purview/declare-records) 
    - [Take action during and at the end of the content lifecycle](/purview/file-plan-manager) 

- Use [Audit (standard)](/purview/audit-solutions-overview?view=o365-worldwide) to maintain logs 