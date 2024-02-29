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

### Step 2: Take remediation action to fix the oversharing issue

Once you have identified the SharePoint sites with a potential oversharing issue, it is time to act. Your actions should consider several factors, including data sensitivity, the severity of the oversharing, and the need to maintain business operations. These actions include:
1. For sensitive data that has been overshared and needs immediate action:
   1. The SharePoint admin should configure [Restricted Access Control Policy](/sharepoint/restricted-access-control) for such sites. As a result, all existing access to the site will be restricted only to the group of users configured by the admin. Accordingly, the content from this site will be visible to CoPilot only for this restricted group of users. This policy works for both OneDrive and SharePoint. 
   1. For high-profile instances, you may want to determine who/how/when the oversharing took place.  Leverage the [Change History](/sharepoint/change-history-report) feature to see what changes may have contributed to the oversharing.
1. For cases where SharePoint admin needs to consult with site owners/admins for action:
   1. The SharePoint admin can reach out to the owners of sites identified in data access governance reports. SharePoint admin can advise site owners on the overshared files/folders in that site and request them to act to manually remove unnecessary access. 
   1. Soon from the spring of 2024, soon, we will be releasing a new SharePoint Advanced Management feature called “Site Access Review” that a SharePoint admin can initiate from any “Data Access Governance” report. Site owners will use a new Site Access Review UI to review broadly shared content in their side and either take remediation action to remove overly broad permissions or provide business justification to the SharePoint admin. 

### Step 3: Take preventive actions

- Train your staff on the range of sharing methods and options, particularly from their own OneDrive. Highlight the OneDrive [sharing report](/sharepoint/sharing-reports) to them. Remind SharePoint Site Owners and Team Owners that they are responsible for their content and highlight info on [sharing reports](/sharepoint/sharing-reports) to them, the [impact of inheritance](https://support.microsoft.com/office/customize-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782), and how to handle sensitive document types. Ensure that Site Owners are the recipients of [access requests](https://support.microsoft.com/office/set-up-and-manage-access-requests-94b26e0b-2822-49d4-929a-8455698654b3). Show site owners [how they can restrict members from sharing](/microsoft-365/solutions/microsoft-365-limit-sharing#sharing-with-specific-people).  

- Identify SharePoint sites that have been inactive for a long time. See how you can easily do that via [our new Inactive Site Policies](/sharepoint/site-lifecycle-management#create-an-inactive-site-policy). You can then lock down permissions on these sites via the [Restricted Access Control policy](/sharepoint/restricted-access-control). You can also consider archiving or deleting these sites.
 
- Consider hiding wide scope permissions from your end users to reduce risks around accidental misuse. [This example](/powershell/module/sharepoint-online/set-spotenant?view=sharepoint-ps#example-2) hides the "Everyone Except External Users" in People Picker control so that no end user can use it. 
•	Consider implementing Conditional Access policies for SharePoint and OneDrive. For example, a policy could require users visiting specific sites with sensitive data to access from a managed device or known network location. These restrictions are also honored by CoPilot. Learn more [here](/sharepoint/authentication-context-example). 

- Consider [adopting sharing best practices](/microsoft-365/solutions/microsoft-365-limit-sharing) like changing sharing link defaults from companywide sharing to specific people links. 

- Consider blocking downloads from selected sites via [a block download policy](/sharepoint/block-download-from-sites).

- Finally, consider applying encryption action with “extract rights” enforced on sensitive office documents. Learn more [here](/purview/ai-microsoft-purview). 

