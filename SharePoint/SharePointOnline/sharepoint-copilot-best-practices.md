---
ms.date: 02/29/2024
title: SharePoint Copilot Best Practices
ms.reviewer: 
ms.author: ruihu
author: maggierui
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
description: "Learn about the best practices for content sharing when enabling Microsoft Copilot for Microsoft 365."
---
# How do SharePoint permissions impact your users’ Copilot for Microsoft 365 experience?

Microsoft Copilot for Microsoft 365 provides value by connecting Large Language Models (LLMs) to your organizational data. Copilot for Microsoft 365 accesses content and context through [Microsoft Graph](/graph/overview). It can generate responses anchored in your organizational data, such as user documents stored in SharePoint and OneDrive, emails, calendars, chats, meetings, and contacts. Copilot combines this content with the user’s working context, such as the meeting a user is in now, the email exchanges the user had on a topic, or the chat conversations the user had last week. Copilot uses this combination of content and context to help provide accurate, relevant, and contextual responses.

Copilot for Microsoft 365 only surfaces organizational data to which individual users have *at least view permissions*. It is important to use the permission models in SharePoint to ensure the right users or groups have the right access to the right content within your organization.
This article provides guidance and best practices that you, as a SharePoint administrator, can take control of the SharePoint permissions model before you [enable Copilot for Microsoft 365 for your users](/microsoft-365-copilot/microsoft-365-copilot-enable-users).


Recommended reading:

[Apply principles of Zero Trust to Microsoft Copilot for Microsoft 365](/security/zero-trust/zero-trust-microsoft-365-copilot)


## Before enabling Copilot for Microsoft 365

Organizations operate at various levels of maturity in governing SharePoint data. While some enterprises strictly monitor permissions and oversharing of content, this is not the case for all enterprises. Adding to the complexity, many enterprises have valid business cases to share “some” data broadly within the company.  
Sometimes, end users in your organization make choices that result in the oversharing of SharePoint content.  As an example, it is noticed that end users do not always pay attention to the permissions of the site/library/folder where they are uploading files. They may end up uploading or saving sensitive content in locations where other users may have access and may include external users. Similarly, it is also noticed that end users often find it easier to share files in SharePoint with a large group instead of individual people, which can lead to oversharing. 
Copilot for Microsoft 365 utilizes all data that a user has access to, which may include broadly shared files that the user is unaware of. As such, users may perceive Copilot as exposing content that has been overshared.
To identify and remediate overshared content in SharePoint, follow these best practices:

> [!Note]
> - These steps are provided exclusively for SharePoint administrators.
> - Some of the features mentioned below require a SharePoint Advance Management license.

### Step 1: Check for signs of oversharing

A SharePoint tenant admin can run reports in the SharePoint Admin Center to discover broad sharing activity happening over the last month. SharePoint Advanced Management’s new [data access governance reports](/sharepoint/data-access-governance-reports) can help here.  A SharePoint tenant admin can run reports on: 
- Usage of “Everyone Except External Users” in last 28 days
- Usage of “broad companywide sharing links” in last 28 days
- Usage of “Everyone” sharing links in last 28 days
These reports can be downloaded as csv files. You can also build your own report by using [Microsoft Graph Data Connect for SharePoint](/graph/data-connect-datasets#onedrive-and-sharepoint-online).  


```powershell
Set-SPOTenant -ShowEveryoneExceptExternalUsersClaim $false
```

### Step 2: Take remediation action to fix oversharing issue

Once you have identified the SharePoint sites with a potential oversharing issue, it is time to act. Your actions should consider several factors, including data sensitivity, the severity of the oversharing, and the need to maintain business operations. These actions include:
1. For sensitive data that has been overshared and needs immediate action:
   1. The SharePoint admin should configure [Restricted Access Control Policy](/sharepoint/restricted-access-control) for such sites. As a result, all existing access to the site will be restricted only to the group of users configured by the admin. Accordingly, the content from this site will be visible to CoPilot only for this restricted group of users. This policy works for both OneDrive and SharePoint. 
   1. For high-profile instances, you may want to determine who/how/when the oversharing took place.  Leverage the [Change History](/sharepoint/change-history-report) feature to see what changes may have contributed to the oversharing.
1. For cases where SharePoint admin needs to consult with site owners/admins for action:
   1. The SharePoint admin can reach out to the owners of sites identified in data access governance reports. SharePoint admin can advise site owners on the overshared files/folders in that site and request them to act to manually remove unnecessary access. 
   1. Soon from the spring of 2024, soon, we will be releasing a new SharePoint Advanced Management feature called “Site Access Review” that a SharePoint admin can initiate from any “Data Access Governance” report. Site owners will use a new Site Access Review UI to review broadly shared content in their side and either take remediation action to remove overly broad permissions or provide business justification to the SharePoint admin. 


Learn more about these reports: 

- [**Data access governance reports for SharePoint sites**](/sharepoint/data-access-governance-reports#sharing-links-reports)

Learn how to restrict access to OneDrive and SharePoint sites by security groups. Using security groups prevents access to a limited known set of users for specific sites and OneDrive. Contents from these sites aren't available to Copilot or to users who previously had access before implementing the policy.

- [**Restrict OneDrive access by security group**](/sharepoint/limit-access)

- [**Restrict SharePoint site access to members of a group**](/sharepoint/restricted-access-control)


### Configure defaults and sensitivity labels

Configure defaults & sensitivity labels to best match your organization's needs

You can choose to change the default sharing link type for the entire tenant or selected sensitive sites. This lets specific people link or people with existing access link.

- [**Change the default sharing link for a site**](/sharepoint/change-default-sharing-link)

You can also prevent members of a site sharing directly requiring consent from the site owner before sharing any file/folder from that site.

- [**Limit sharing in Microsoft 365**](/microsoft-365/solutions/microsoft-365-limit-sharing?view=o365-worldwide#sharepoint-site)

You can also control the “default sharing link type” and “change how members can share” features using sensitivity labels. Doing so lets you scale across thousands of sites, and millions of documents. https://learn.microsoft.com/en-us/purview/ai-microsoft-purview#microsoft-purview-strengthens-information-protection-for-copilot

- [**Use sensitivity labels to configure the default sharing link type**](/purview/sensitivity-labels-default-sharing-link)

### Train your users on sharing practices

Train your users on sharing features, especially for OneDrive accounts. Generate a OneDrive sharing report to help users understand how sharing is being used and if any files or folders are being shared with guests.

- [**Report on file and folder sharing in a SharePoint site**](https://learn.microsoft.com/en-us/sharepoint/sharing-reports)

Remind SharePoint site and team owners that they're responsible for their content. Advise them on how to review sharing reports, understand the impact of inheritance, and how to handle sensitive document types. Make sure that site owners are notified of all site access requests. Also adding sensitivity label to files, even without encryption, adds protection.

-  [**Understand the impact of inheritance**](/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782)

- [**Set up and manage access requests**](/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3).


### Implement conditional access for SharePoint and OneDrive

Learn more about conditional access support in SharePoint and OneDrive. 

- [**Microsoft Syntex - SharePoint Advanced Management overview**](/sharepoint/advanced-management)

### Searchability of documents

Consider the searchability of your documents. Users won't see any document appear in Copilot if that document isn't searchable in the first place.

>[!Note]
>Configuring "NoIndex" on a site should be considered and compared with [Restricted access Control (RAC)](/sharepoint/restricted-access-control). Using restricted access control makes the documents of the site available to Copilot and Search only for the selected set of users.

Identify specific sites or libraries that would benefit from being excluded from search results and exclude them as necessary. Evaluate the impact excluding sites would have on users and decide if this works for your organization.

- [**Exclude content from search results**](/office/enable-content-to-be-searchable-d7ba92db-8618-43fe-87ee-adf03d973062)
