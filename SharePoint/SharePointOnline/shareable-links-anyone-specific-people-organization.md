---
ms.date: 09/12/2024
title: How shareable links work in OneDrive and SharePoint in Microsoft 365
ms.reviewer: 
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords: NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: Learn about how shareable links work in OneDrive and SharePoint in Microsoft 365.
---

# How shareable links work in OneDrive and SharePoint in Microsoft 365

When users share files and folders in Microsoft 365, a shareable link is created which has permissions to the item. There are three primary link types:

- *Anyone* links give access to the item to anyone who has the link. People using an *Anyone* link don't have to authenticate, and their access can't be audited.

  ![Diagram showing how anyone links can be passed from user to user.](media/DMC_SharePointSharingLinks_Anyone.png)
      
  An *anyone* link is a transferrable, revocable secret key. It's transferrable because it can be forwarded to others. It's revocable because by deleting the link, you can revoke the access of everyone who got it through the link. It's secret because it can't be guessed or derived. The only way to get access is to get the link, and the only way to get the link is for somebody to give it to you. *Anyone* links can't be used with files in a Teams shared channel site.


- *People in your organization* links work for only people inside your Microsoft 365 organization. (They don't work for guests in the directory, only members).  

  ![Diagram showing how people in my organization links can be passed from user to user inside the company.](media/DMC_SharePointSharingLinks_PeopleInYourOrganization.png)
  
  Like an *anyone* link, a *people in my organization* link is a transferrable, revocable secret key. Unlike an *anyone* link, these links only work for people inside your Microsoft 365 organization. When somebody opens a *people in my organization* link, they need to be authenticated as a member in your directory. If they're not currently signed-in, they're prompted to sign in. 

  Creating a *People in your organization* link doesn't make the associated file or folder appear in search results, be accessible via Copilot, or grant access to everyone within the organization. Simply creating this link doesn't provide organizational-wide access to the content. For individuals to access the file or folder, they must possess the link and it needs to be activated through redemption. A user can redeem the link by selecting it. Also, if the link is sent from the SharePoint or OneDrive Web UI, or as email in Outlook or chat message in Teams, it will be automatically redeemed for individual recipients, up to a limit of 100.  This feature is not supported for group recipients, or for messages posted in Teams channels. The link doesn't work for guests or other people outside your organization.
  
- *Specific people* links only work for the people that users specify when they share the item.  

  ![Diagram showing how specific people links only work for the people specified.](media/DMC_SharePointSharingLinks_Specific.png)

  A *specific people* link is a nontransferable, revocable secret key. Unlike *anyone* and *people in my organization* links, *specific people* links don't work if they're opened by anybody other than the person specified by the sender. In addition, unlike *anyone* or *people in my organization* links, *specific people* links makes the associated file or folder appear in search results and is accessible via Copilot for all user and security group members added to the sharing link.  
  
  *Specific people* links can be used to share with users in the organization and people outside the organization. In both cases, the recipient needs to authenticate as the user specified in the link. For files in a Teams shared channel site, *specific people* links can only be sent to others in the channel.

It's important to educate your users in how these sharing links work and which they should use to best maintain the security of your data. Send your users links to [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) and [Share SharePoint files or folders](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c), and include information about your organization's policies for sharing information.

## Related articles

[Change the default link type for a site](change-default-sharing-link.md)
