---
ms.date: 01/03/2024
title: SharePoint CoPilot Best Practices
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- Tier2
ms.custom:
- seo-marvel-apr2020
ms.localizationpriority: medium
search.appverid:
- MET150
description: "Learn about the best practices when using SharePoint CoPilot."
---
# SharePoint CoPilot best practices


## Before deploying CoPilot

Organizations belong to various levels of maturity in governing SharePoint data. While some enterprises strictly monitor permissions and reports oversharing, this is not the case for all enterprises. Also, for mature enterprises there are valid business cases to share “some” data broadly within the company.  

### Understand your permission set

When you upload a document, take time to understand the permissions that have been set for that site or folder.  Why?

### Impact of oversharing

Ever decided to just share a link with everyone instead of just identifying specific users?  If you have you are like many of us.  However, its important that what may have seemed like harmless oversharing, becomes an issue when we introducing a powerful feature like CoPilot. 

Copilot will utilize all data that a user has access to, which may include broadly shared files that the user is unaware of. 

## Best practices

### Hide wide scope permission setting

Consider hiding wide scope permissions from your end users to reduce risks around accidental misuse. This example hides the "Everyone Except External Users" aka EEEU in People Picker control so that no end user can use it. Set-SPOTenant (Microsoft.Online.SharePoint.PowerShell)[Example](/powershell/module/sharepoint-online/set-spotenant?view=sharepoint-ps#example-2)

## Run report that tracks “Everyone Except External Users” usage and usage of “broad company wide sharing links"
If you find discrepancies in sharing patterns from these reports, then apply “Restricted Access Control” to such sites and OneDrive and initiate conversations with Site Owners on business justification. We have a new feature called “Site access Review” that a SharePoint admin can initiate from the report and seek justification from site owners on oversharing.  Examples of discrepancies in sharing pattern can be:
1.	The site is marked as Confidential but shared with the entire company.
2.	The site is marked as Internal but shared with guest users.

Learn more about these reports: [Data access governance reports for SharePoint sites](/sharepoint/data-access-governance-reports#sharing-links-reports)

Learn how to restrict access to OneDrive and SharePoint sites by security groups.  This will prevent access to a limited known set of users for specific sites and ONEDRIVE. Consequently, contents from these sites will not be available to CoPilot as well for users who had access to the site but not anymore because of this policy.

[Restrict OneDrive access by security group](/sharepoint/limit-access)

[Restrict SharePoint site access to members of a group](/sharepoint/restricted-access-control)


### Configure defaults & sensitivity labels to best match your organization's needs


You may want to change the default sharing link type for the entire tenant or selected sensitive sites to specific people link or people with existing access link.

[Change the default sharing link for a site](/sharepoint/change-default-sharing-link)

You can also prevent members of a site sharing directly and would need consent from site owner before sharing any file/folder from that site.

[Limit sharing in Microsoft 365](/microsoft-365/solutions/microsoft-365-limit-sharing?view=o365-worldwide#sharepoint-site)

Additionally you can control “default sharing link type” and “change how members can share” features via sensitivity labels that gives scale across thousands of sites and millions of documents. 

[Use sensitivity labels to configure the default sharing link type](/purview/sensitivity-labels-default-sharing-link)

### Train your staff on various Sharing aspects specially from their own OneDrive

Highlight the OneDrive sharing report to them. [Sharing report](https://learn.microsoft.com/en-us/sharepoint/sharing-reports)

Remind SharePoint Site Owners and Team Owners that they are responsible for their content and highlight to them / remind them about the sharing reports, [the impact of inheritance](/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782), how to handle sensitive document types. Ensure that the Site Owners are the recipients of [access requests](/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3).


### For enhanced protection, consider applying Sensitivity Labels with encryption on Office files. This will help in scenarios where a user may have access to the entire site but still can’t access because of encryption. CoPilot fully honors access & permissions as configured in the label attached to the file. 


Learn more about how encryption works in SharePoint and OneDrive. 
Enable sensitivity labels for files in SharePoint and OneDrive | Microsoft Learn

You can make individual libraries secure with encryption.

https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files



 Configure a default sensitivity label for a SharePoint document library | Microsoft Learn 

Note: Copilot will return the files but not summarize the content for files with the following restrictions via encryption:
 
- Extract restrictions (Do not forward emails, do not copy files, and other items with extract restrictions). 

- User-defined permissioned labeled files

- DKE: Because Double Key Encryption (DKE) is intended for your most sensitive data that is subject to the strictest protection requirements, Copilot can't access this data. 


### Implement Conditional access for SharePoint and OneDrive

Learn more about conditional access support in SharePoint and OneDrive. Microsoft Syntex - SharePoint Advanced Management overview - SharePoint in Microsoft 365 | Microsoft Learn

### Consider the searchability of your documents. Users will not see any document appear in CoPilot if that document is not searchable in the first place.

Note: This feature, i.e. configuring NoIndex against a site should be considered vs. other restrictive feature called [Restricted access Control](/sharepoint/restricted-access-control); This later control still makes the documents of the site available to CoPilot and Search only for the selected set of users. 

Identify specific sites or libraries which would benefit from being [excluded from search results](/office/enable-content-to-be-searchable-d7ba92db-8618-43fe-87ee-adf03d973062) and exclude as necessary. In doing so balance the impact this would have on site users.
