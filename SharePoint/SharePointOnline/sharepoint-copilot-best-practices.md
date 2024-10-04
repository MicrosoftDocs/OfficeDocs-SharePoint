---
ms.date: 02/29/2024
title: Microsoft 365 Copilot - best practices with SharePoint
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
ROBOTS: NOINDEX, NOFOLLOW
f1.keywords:
- NOCSH
ms.topic: best-practice
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- m365copilot
- magic-ai-copilot
- Tier2

ms.localizationpriority: medium
search.appverid:
- MET150
description: "Learn about the best practices with SharePoint for content sharing when enabling Microsoft 365 Copilot."
---
# Microsoft 365 Copilot - best practices with SharePoint

Microsofts value by connecting Large Language Models (LLMs) to your organizational data. Microsoft 365 Copilot accesses content and context through [Microsoft Graph](/graph/overview) and can generate responses based on your organizational data. The data sources include user documents stored in SharePoint and OneDrive, emails, calendars, chats, meetings, and contacts. Microsoft 365 Copilot combines this content with the user’s working context, such as the meeting a user is in now, the email exchanges the user had on a topic, or the chat conversations the user had last week. Microsoft 365 Copilot uses this combination of content and context to help provide accurate, relevant, and contextual responses.

## How do SharePoint permissions affect your users’ Microsoft 365 Copilot experience?

Microsoft 365 Copilot only surfaces organizational data to which individual users have *at least view permissions*. It's important to use the permission models in SharePoint to ensure the right users or groups have the right access to the right content within your organization.
This article provides guidance and best practices that you, as a SharePoint administrator, can take control of the SharePoint permissions model before your organization [enable Microsoft 365 Copilot for your users](/microsoft-365-copilot/microsoft-365-copilot-enable-users).

## Before enabling Microsoft 365 Copilot

Organizations operate at various levels of maturity in governing SharePoint data. While some enterprises strictly monitor permissions and oversharing of content, others don't. The situation is further complicated because many enterprises have legitimate reasons to share "some" data widely within the organization.
Sometimes, end users in your organization make choices that result in the oversharing of SharePoint content. As an example, it's noticed that end users don't always pay attention to the permissions of the site/library/folder where they're uploading files. They may end up uploading or saving business critical content in locations where other users may have access and may include external users. It's also observed that some end users tend to prefer sharing files in SharePoint with large groups rather than with individuals. This practice can result in oversharing.  
Microsoft 365 Copilot utilizes all data that a user has access to, which may include broadly shared files that the user is unaware of. As a result, users might see Microsoft 365 Copilot as exposing content that was overshared.
To identify and remediate overshared content in SharePoint, follow these best practices.

> [!Note]
>
> - These steps are provided exclusively for SharePoint administrators.
> - Some of the following features require a SharePoint Advance Management license.

### Step 1: Review site-level sharing controls and remove "Everyone Except External Users" from people picker

- Educate site admins on the site-level controls they can use to [restrict members from sharing](/microsoft-365/solutions/microsoft-365-limit-sharing#sharing-with-specific-people). One key setting here ensures that Site Owners are the recipients of [access requests](https://support.microsoft.com/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3).  
- Consider hiding broad-scope permissions from your end users to reduce risks around accidental misuse. [This example](/powershell/module/sharepoint-online/set-spotenant#example-2) hides the "Everyone Except External Users" in the People Picker control so that no end user can use it.  
- Consider [adopting sharing best practices](/microsoft-365/solutions/microsoft-365-limit-sharing) like changing sharing link defaults from companywide sharing to specific people links.

### Step 2: Identify inactive sites, then restrict access or delete

Reduce your surface area for potentially overshared content by identifying SharePoint sites that have been inactive for a long time. See how you can easily do that via the [Inactive Site Policies](/sharepoint/site-lifecycle-management#create-an-inactive-site-policy) in SharePoint Advanced Management.
You can then lock down permissions on these sites via the Restricted Access Control policy. You can also consider deleting these sites.

### Step 3: Identify potentially overshared content

A SharePoint admin can run reports in the SharePoint Admin Center to discover broad sharing activity happening over the last month. [SharePoint Advanced Management’s](/sharepoint/advanced-management) new [data access governance reports](/sharepoint/data-access-governance-reports) can help here.  A SharePoint admin can run reports on:

- Usage of "Everyone Except External Users" in the last 28 days
- Usage of broad org-wide ["People in your organization" sharing links](/sharepoint/shareable-links-anyone-specific-people-organization) in the last 28 days
- Usage of "Anyone" sharing links in the last 28 days

These reports can be downloaded as CSV files. You can also build your own report by using [Microsoft Graph Data Connect for SharePoint](/graph/data-connect-datasets#onedrive-and-sharepoint-online).  

### Step 4: Take remediation actions to address oversharing

Once you have identified the SharePoint sites with potential oversharing issues, it's time to act. Your actions should consider several factors, including data sensitivity, the severity of the oversharing, and the need to maintain business operations. These actions include:

1. For content that has been overshared and needs immediate action:
   1. The SharePoint admin should configure [Restricted Access Control Policy](/sharepoint/restricted-access-control) for such sites. As a result, all existing access to the site is restricted to only the group of users configured by the admin. Accordingly, the content from this site is visible in the Microsoft 365 Copilot experience only for this restricted group of users. This policy works for both OneDrive and SharePoint.
   1. For high-profile instances, you may want to determine who/how/when the oversharing took place.  Use the [Change History](/sharepoint/change-history-report) feature to see what changes may have contributed to the oversharing.
1. For cases where SharePoint admin needs to consult with site owners/admins for action:
   1. The SharePoint admin can reach out to the owners of sites identified in data access governance reports. SharePoint admin can advise site owners on the overshared files/folders in that site and request them to act to manually remove unnecessary access.
   1. A new [SharePoint Advanced Management](/sharepoint/advanced-management) feature called "[Site Access Review](site-access-review.md)" allows a SharePoint admin to initiate a review from any 'Data Access Governance' report. Site owners will use a new Site Access Review UI to review broadly shared content on their side and either take remediation action to remove overly broad permissions or provide business justification to the SharePoint admin.

### Step 5: Set restricted access control and block file download policies on business-critical sites

- Use [Restricted Access Control](/sharepoint/restricted-access-control) to proactively protect against oversharing.  

- Consider blocking downloads from selected sites via [a block download policy](/sharepoint/block-download-from-sites). Or specifically block the download of [Teams meetings recordings](/microsoftteams/block-download-meeting-recording).

- Finally, consider applying encryption action with "extract rights" enforced on business-critical office documents. Learn more [here](/purview/ai-microsoft-purview).
