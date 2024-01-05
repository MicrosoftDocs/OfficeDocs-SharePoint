---
ms.date: 01/04/2024
title: SharePoint Copilot Best Practices
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
description: "Learn about the best practices when using SharePoint Copilot."
---
# SharePoint Copilot best practices

Microsoft Copilot connects your Large Language Models (LLMS) to your organizational data, including documents stored in SharePoint, OneDrive, emails, calendar, chats, meetings, and contacts. Copilot combines this content with the user’s working context, such as the meeting a user is in now, the email exchanges the user had on an article, or the chat conversations the user had last week. Copilot uses this combination of content and context to help provide accurate, relevant, and contextual responses.

Microsoft Copilot only accesses organizational data that the individual user has at a minimum **view permissions**. It's important that you're using the permission models in SharePoint to help ensure the right users or groups have the right access to the right content within your organization.

## Before deploying Microsoft Copilot

Organizations have different levels of maturity in governing SharePoint data. While some enterprises strictly monitor permissions and report oversharing, this isn't the case for all businesses. Mature enterprises can also have valid business cases to share some data broadly within their company.  

When you upload a document, take time to understand the permissions set for that site or folder.

### Impact of oversharing

Have your ever decided to just share a link with everyone instead of identifying specific users? It's not uncommon. However, it's important to understand that what could seem like harmless oversharing, becomes an issue when using a powerful feature like Copilot. 

>[!Important]
> Copilot utilizes all data that a user has access to, which can include broadly shared files that the user may be unaware of.

## Best practices

### Hide wide scope permission settings

Consider hiding the ability to assign wide scope permissions to reduce accidental misuse.

This example hides the "Everyone Except External Users" (EEEU) in People Picker control so that no end user can use it.

```powershell
Set-SPOTenant -ShowEveryoneExceptExternalUsersClaim $false
```

### Run targeted reports on usage

Run targeted data access reports for SharePoint sites, specifically select that tracks **Everyone Except External Users** usage and broad company-wide sharing links.

These reports can reveal discrepancies in sharing patterns such as:

- The site is marked as *Confidential* but shared with the entire company.
- The site is marked as *Internal* but shared with guest users.

If you find discrepancies on these reports, apply *Restricted Access Control* to these sites and OneDrive. Talk with site owners to see if there's a business justification for the sharing and permission settings.

The new “Site access review” feature on the reports lets a SharePoint admin seek justification from site owners on oversharing.

Learn more about these reports: [Data access governance reports for SharePoint sites](/sharepoint/data-access-governance-reports#sharing-links-reports)

Learn how to restrict access to OneDrive and SharePoint sites by security groups. Using security groups prevents access to a limited known set of users for specific sites and OneDrive. Contents from these sites aren't available to Copilot or to users who previously had access before implementing the policy.

- [**Restrict OneDrive access by security group**](/sharepoint/limit-access)

- [**Restrict SharePoint site access to members of a group**](/sharepoint/restricted-access-control)


### Configure defaults and sensitivity labels

Configure defaults & sensitivity labels to best match your organization's needs

You can choose to change the default sharing link type for the entire tenant or selected sensitive sites. This lets specific people link or people with existing access link.

- [**Change the default sharing link for a site**](/sharepoint/change-default-sharing-link)

You can also prevent members of a site sharing directly requiring consent from the site owner before sharing any file/folder from that site.

- [**Limit sharing in Microsoft 365**](/microsoft-365/solutions/microsoft-365-limit-sharing?view=o365-worldwide#sharepoint-site)

You can also control the “default sharing link type” and “change how members can share” features using sensitivity labels. Doing so lets you scale across thousands of sites, and millions of documents.

- [**Use sensitivity labels to configure the default sharing link type**](/purview/sensitivity-labels-default-sharing-link)

### Train your users on sharing practices

Train your users on sharing features, especially for OneDrive accounts. Generate a OneDrive sharing report to help users understand how sharing is being used and if any files or folders are being shared with guests.

- [**Report on file and folder sharing in a SharePoint site**](https://learn.microsoft.com/en-us/sharepoint/sharing-reports)

Remind SharePoint site and team owners that they're responsible for their content. Advise them on how to review sharing reports, understand the impact of inheritance, and how to handle sensitive document types. Make sure that site owners are notified of all site access requests.

-  [**Understand the impact of inheritance**](/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782)

- [**Set up and manage access requests**](/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3).


### Apply sensitivity labels 

For enhanced protection, consider applying Sensitivity labels with encryption on Office files. This helps in scenarios where a user can have access to an entire site but still can’t access because of encryption. Copilot fully honors access and permissions as configured in the label attached to the file. 

Learn more about how encryption works in SharePoint and OneDrive. 
- [**Enable sensitivity labels for files in SharePoint and OneDrive**](/purview/sensitivity-labels-sharepoint-onedrive-files)

You can also make individual libraries secure with encryption:

- [**Configure a default sensitivity label for a SharePoint document library**](/purview/sensitivity-labels-sharepoint-default-label)

>[!Note]
>Copilot returns the files but doesn't summarize the content for files with these restrictions via encryption:
> - Extract restrictions (Don't forward emails, don't copy files, and other items with extract restrictions)
> - User-defined permissioned labeled files
> - DKE: Double Key Encryption (DKE) is intended for your most sensitive data that is subject to the strictest protection requirements. Copilot can't access this data.


### Implement conditional access for SharePoint and OneDrive

Learn more about conditional access support in SharePoint and OneDrive. 

- [**Microsoft Syntex - SharePoint Advanced Management overview**](/sharepoint/advanced-management)

### Searchability of documents

Consider the searchability of your documents. Users won't see any document appear in Copilot if that document isn't searchable in the first place.

>[!Note]
>Configuring "NoIndex" on a site should be considered and compared with [Restricted access Control (RAC)](/sharepoint/restricted-access-control). Using restricted access control makes the documents of the site available to Copilot and Search only for the selected set of users.

Identify specific sites or libraries that would benefit from being excluded from search results and exclude them as necessary. Evaluate the impact excluding sites would have on users and decide if this works for your organization.

- [**Exclude content from search results**](/office/enable-content-to-be-searchable-d7ba92db-8618-43fe-87ee-adf03d973062)
