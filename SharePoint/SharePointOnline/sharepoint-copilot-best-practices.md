---
ms.date: 02/29/2024
title: Microsoft Copilot for Microsoft 365 best practices with SharePoint
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
description: "Learn about the best practices with SharePoint for content sharing when enabling Microsoft Copilot for Microsoft 365."
---
# Microsoft Copilot for Microsoft 365 Best Practices with SharePoint

Microsoft Copilot for Microsoft 365 provides value by connecting Large Language Models (LLMs) to your organizational data. Copilot for Microsoft 365 accesses content and context through [Microsoft Graph](/graph/overview) and can generate responses based on your organizational data. The data sources include user documents stored in SharePoint and OneDrive, emails, calendars, chats, meetings, and contacts. Copilot for Microsoft 365 combines this content with the user’s working context, such as the meeting a user is in now, the email exchanges the user had on a topic, or the chat conversations the user had last week. Copilot for Microsoft 365 uses this combination of content and context to help provide accurate, relevant, and contextual responses.

## How do SharePoint permissions affect your users’ Copilot for Microsoft 365 experience?

Copilot for Microsoft 365 only surfaces organizational data to which individual users have *at least view permissions*. It's important to use the permission models in SharePoint to ensure the right users or groups have the right access to the right content within your organization.
This article provides guidance and best practices that you, as a SharePoint administrator, can take control of the SharePoint permissions model before your organization [enable Copilot for Microsoft 365 for your users](/microsoft-365-copilot/microsoft-365-copilot-enable-users).


## Before enabling Copilot for Microsoft 365

Organizations operate at various levels of maturity in governing SharePoint data. While some enterprises strictly monitor permissions and oversharing of content, others don't. The situation is further complicated because many enterprises have legitimate reasons to share "some" data widely within the organization.
Sometimes, end users in your organization make choices that result in the oversharing of SharePoint content. As an example, it's noticed that end users don't always pay attention to the permissions of the site/library/folder where they're uploading files. They may end up uploading or saving sensitive content in locations where other users may have access and may include external users. It's also observed that some end users tend to prefer sharing files in SharePoint with large groups rather than with individuals. This practice can result in oversharing.  
Copilot for Microsoft 365 utilizes all data that a user has access to, which may include broadly shared files that the user is unaware of. As a result, users might see Copilot for Microsoft 365 as exposing content that was overshared.
To identify and remediate overshared content in SharePoint, follow these best practices:

> [!Note]
>
> - These steps are provided exclusively for SharePoint administrators.
> - Some of the following features require a SharePoint Advance Management license.

### Step 1: Check for signs of oversharing

A SharePoint admin can run reports in the SharePoint Admin Center to discover broad sharing activity happening over the last month. [SharePoint Advanced Management’s](/sharepoint/advanced-management) new [data access governance reports](/sharepoint/data-access-governance-reports) can help here.  A SharePoint admin can run reports on:

- Usage of "Everyone Except External Users" in last 28 days
- Usage of 'broad companywide sharing links' in last 28 days
- Usage of "Everyone" sharing links in last 28 days

These reports can be downloaded as csv files. You can also build your own report by using [Microsoft Graph Data Connect for SharePoint](/graph/data-connect-datasets#onedrive-and-sharepoint-online).  


### Step 2: Take remediation actions

Once you have identified the SharePoint sites with potential oversharing issues, it's time to act. Your actions should consider several factors, including data sensitivity, the severity of the oversharing, and the need to maintain business operations. These actions include:

1. For sensitive data that has been overshared and needs immediate action:
   1. The SharePoint admin should configure [Restricted Access Control Policy](/sharepoint/restricted-access-control) for such sites. As a result, all existing access to the site is restricted to only the group of users configured by the admin. Accordingly, the content from this site is visible in the Copilot for Microsoft 365 experience only for this restricted group of users. This policy works for both OneDrive and SharePoint.
   1. For high-profile instances, you may want to determine who/how/when the oversharing took place.  Use the [Change History](/sharepoint/change-history-report) feature to see what changes may have contributed to the oversharing.
1. For cases where SharePoint admin needs to consult with site owners/admins for action:
   1. The SharePoint admin can reach out to the owners of sites identified in data access governance reports. SharePoint admin can advise site owners on the overshared files/folders in that site and request them to act to manually remove unnecessary access.
   1. Soon from the spring of 2024, soon, we'll be releasing a new [SharePoint Advanced Management](/sharepoint/advanced-management) feature called "Site Access Review" that a SharePoint admin can initiate from any 'Data Access Governance' report. Site owners will use a new Site Access Review UI to review broadly shared content in their side and either take remediation action to remove overly broad permissions or provide business justification to the SharePoint admin.

### Step 3: Take preventive actions

- Train your staff on the range of sharing methods and options, particularly from their own OneDrive. Highlight the OneDrive [sharing report](/sharepoint/sharing-reports) to them. Remind SharePoint Site Owners and Team Owners that they're responsible for their content. Highlight info on [sharing reports](/sharepoint/sharing-reports), the [impact of inheritance](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782), and how to handle sensitive document types. Ensure that Site Owners are the recipients of [access requests](https://support.microsoft.com/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3). Show site owners [how they can restrict members from sharing](/microsoft-365/solutions/microsoft-365-limit-sharing#sharing-with-specific-people).  

- Identify SharePoint sites that have been inactive for a long time. See how you can easily do that via [our new Inactive Site Policies](/sharepoint/site-lifecycle-management#create-an-inactive-site-policy). You can then lock down permissions on these sites via the [Restricted Access Control policy](/sharepoint/restricted-access-control). You can also consider archiving or deleting these sites.

- Consider hiding wide scope permissions from your end users to reduce risks around accidental misuse. [This example](/powershell/module/sharepoint-online/set-spotenant?#example-2) hides the "Everyone Except External Users" in People Picker control so that no end user can use it.
• Consider implementing Conditional Access policies for SharePoint and OneDrive. For example, a policy could require users visiting specific sites with sensitive data to access from a managed device or known network location. Copilot for Microsoft 365 also honors these restrictions. Learn more [here](/sharepoint/authentication-context-example).

- Consider [adopting sharing best practices](/microsoft-365/solutions/microsoft-365-limit-sharing) like changing sharing link defaults from companywide sharing to specific people links.

- Consider blocking downloads from selected sites via [a block download policy](/sharepoint/block-download-from-sites).

- Finally, consider applying encryption action with "extract rights" enforced on sensitive office documents. Learn more [here](/purview/ai-microsoft-purview).
