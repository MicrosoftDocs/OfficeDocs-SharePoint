---
title: "Help users use the Discover view in OneDrive"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
ms.date: 06/7/2018
audience: Admin
f1.keywords:
- NOCSH
ms.topic: overview
ms.service: one-drive
localization_priority: Normal
search.appverid:
- ODB160
- MOE150
- MED150
- MBS150
- ODB150
- MET150
ms.assetid: effbf250-57c8-436d-9e0f-edd017a896b7
description: "Learn how to help users get the most out of the Discover view in OneDrive."
---

# Help users use the Discover view in OneDrive

This article is for IT administrators. If you're not an IT admin, see [Are my documents safe in the Discover view in OneDrive for Business?](https://support.office.com/article/98cbb291-71e7-4355-b130-ac5f2cfe3d35) for info about using the Discover view.
  
The more your users use OneDrive in Office 365 to work together, by viewing, editing and sharing each other's documents, the more useful the Discover view in OneDrive will be for everyone. Learn more about how you as an admin can help users get the most out of the Discover view.
  
The Discover view is powered by Office Delve, and both have a dependency on the Office Graph. It shows users the most relevant content based on who they work with and what they're working on. The information in the Discover view is tailored to each user. The Discover view doesn't change permissions and users will only see what they already have access to.
  
As an admin, you can make sure that you allow your organization to access the Office Graph, and that you have set up other Office 365 services that the Discover view uses, for instance SharePoint Online and Delve. You can also help people get started with the Discover view, and address questions that users might have.
  
## What you need to get the Discover view
<a name="WhatUNeed"> </a>

Discover view functionality is available to Office 365 users in OneDrive, which is available in the following subscription plans of Office 365:
  
- Office 365 Enterprise (E1, E3, and E4)

- Office 365 Education

- Office 365 Government (E1, E3 and E4)

- Microsoft 365 Business Basic

- Microsoft 365 Business Standard

Regardless of which of these Office 365 subscriptions you have, you need to activate the SharePoint service and assign users a SharePoint license before they can start using the Discover view.
  
OneDrive in Office 365 is designed to work with the current or immediately previous version of Internet Explorer or Firefox, or the latest version of Chrome or Safari. For more info, see [Office 365 system requirements](https://go.microsoft.com/fwlink/p/?LinkID=797594&amp;clcid=0x409).
  
## Introducing the Discover view in your organization
<a name="IntroDisView"> </a>

Here are some resources that you can use to get your organization started with the Discover view.
  
### Before you announce the Discover view

SharePoint and OneDrive are the primary sources of content in the Discover view. How you and users manage permissions on documents and sites affects what users see in the Discover view. Check out [Overview: best practices for managing how people use your team site](https://support.office.com/article/95e83c3d-e1b0-4aae-9d08-e94dcaa4942e) and [Plan your permissions strategy](/sharepoint/plan-your-permissions-strategy) for more information.
  
### Using the Discover view on a day-to-day basis

You can point users to the Discover view help article: [Are my documents safe in the Discover view in OneDrive for Business?](https://support.office.com/article/98cbb291-71e7-4355-b130-ac5f2cfe3d35)
  
## Help users troubleshoot the Discover view
<a name="HelpTS"> </a>

Use the information in this section to help troubleshoot issues in the Discover view.
  
- [Users don't see user pictures in the Discover view](help-users-use-discover-view.md#Nopics)
    
- [Users see very little or no content in their Discover view](help-users-use-discover-view.md#NoCont)
    
- [Users are concerned that private or sensitive documents are available in the Discover view](help-users-use-discover-view.md#UsersConcern)
    
### Users don't see user pictures in the Discover view
<a name="Nopics"> </a>

The user pictures in the Discover view are from the SharePoint user profiles. If there's no picture for a user in his or her SharePoint user profile, the Discover view has no picture to show.
  
 **Solution(s)**
  
Make sure that users upload their user profile picture to SharePoint. For more information, point users to [View and update your profile in Office Delve](https://support.office.com/article/4e84343b-eedf-45a1-aeb9-8627ccca14ba) (the Discover view is powered by Delve).
  
### Users see very little or no content in their Discover view
<a name="NoCont"> </a>

The content in the Discover view comes from different content sources across Office 365 such as SharePoint and OneDrive.
  
If users don't have any recently modified or viewed content in these content sources, and they don't have access to other users' content, the Discover view may have very little or no content to show. Users also need to have licenses to Office 365 services and access to the Office Graph to see content in the Discover view.
  
 **Solution(s)**
  
- Encourage your users to store and share documents in SharePoint and OneDrive. For more information, see [Store your documents where Office Delve can get to them](https://support.office.com/article/49a0db49-5e6c-4dda-816e-e11dd77de49d) (the Discover view is powered by Delve).

- Check the permission settings on the SharePoint sites to make sure that the user has access to the correct sites and their content.

- Check that the user is in the Active Directory and that he or she is a member of the correct Active Directory groups. To verify, go to **Microsoft 365 admin center** \> **Users** \> **Active Users**.

- As an admin, you can allow your organization to access the Office Graph. This makes sure the Discover view shows the most relevant content to users. See [Control access to the Office Graph](/sharepoint/delve-for-office-365-admins) for more information.

- Make sure that you've assigned users a license to access to the Office 365 services that you've activated.

### Users are concerned that private or sensitive documents are available in the Discover view
<a name="UsersConcern"> </a>

Any document that a user can view or edit in Office 365, can also appear in the Discover view. The Discover view doesn't change any permissions and users will only see documents they already have access to. Sometimes, though, you may want to prevent a document from appearing in the Discover view.
  
 **Solution(s)**
  
- Check the permission settings for the documents, sites and libraries and make sure that only the intended users have access to the content.

- If you want to prevent specific documents from appearing in the Discover view, follow the steps in [Manage the search schema in SharePoint Online](/sharepoint/manage-search-schema). You can keep storing the documents in Office 365, and people can still find them through search - they just won't show up in the Discover view or Delve.
    
## About the Office Graph
<a name="AboutOG"> </a>

The Discover view is powered by the Office Graph. The Office Graph stores data representations about all Office 365 items as nodes in a graph index. The Office Graph data is stored in the customer's partition of the SharePoint and Exchange environments, and has the same data protection and security as other customer data stored in the same cloud services.
  
The Office Graph uses rich relationships to describe connections between items of different types. In addition, the Office Graph uses advanced analytics and machine learning techniques to create inferred rich relationships - what we call insights.
  
To present the most relevant content in different contexts, in the Discover view or in Delve for example, the Office Graph uses a two-step analysis. First, it calculates which users in the Office Graph are most relevant to the current context. Second, it retrieves the most relevant content associated with these users. The content is tailored to each user, and users only see what they already have access to.
  
For developers, the Office Graph insights and rich relationships are exposed through the Microsoft Graph, a single REST API endpoint (https://graph.microsoft.com) that exposes multiple APIs from Microsoft cloud services. For more information, see Office Graph.
  
### What is the effect of allowing or not allowing access to the Office Graph?

If you don't allow access to the Office Graph, you affect the relevance of the content displayed in the Discover view and in experiences elsewhere in Office 365, for example on the SharePoint start page. Allowing and not allowing access to the Office Graph will also affect Delve functionality.
  
> [!NOTE]
> For more information, see [Office Delve for Office 365 admins](/sharepoint/delve-for-office-365-admins).
  
## Additional resources
<a name="AddRes"> </a>

End users
  
- [Are my documents safe in the Discover view in OneDrive for Business?](https://support.office.com/article/98cbb291-71e7-4355-b130-ac5f2cfe3d35)
    
- [What is Office Delve?](https://support.office.com/article/1315665a-c6af-4409-a28d-49f8916878ca)
    
- [How does Office Delve know what's relevant to me?](https://support.office.com/article/048d502e-80a7-4f77-ac5c-f9d81733c385)
    
- [What is OneDrive for Business?](https://support.office.com/article/187f90af-056f-47c0-9656-cc0ddca7fdc2)
    
- [Should I save my documents to OneDrive for Business or a team site?](https://support.office.com/article/d18d21a0-1f9f-4f6c-ac45-d52afa0a4a2e)
    
- [Upload a folder or files to a document library](https://support.office.com/article/eb18fcba-c953-4d45-8d90-8da66edeacdb)
    
Admins
  
- [Office Delve for Office 365 admins](/sharepoint/delve-for-office-365-admins)
