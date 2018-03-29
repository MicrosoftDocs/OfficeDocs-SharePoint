---
title: "Manage external sharing for your SharePoint Online environment"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 1/29/2018
ms.audience: Admin
ms.topic: article
f1_keywords:
- O365E_EnableSPExtlUser
- O365M_EnableSPExtlUser
- O365P_AddSPExtlUser
- o365p_enablespextluser
- quickshare
ms.service: o365-administration
localization_priority: Priority
ms.collection: Strat_OD_share
ms.custom: Adm_O365
ms.assetid: c8a462eb-0723-4b0b-8d0a-70feafe4be85

description: "Learn about the external sharing options in SharePoint Online."
---

# Manage external sharing for your SharePoint Online environment

If your organization performs work that involves sharing documents or collaborating directly with vendors, clients, or customers, then you can use the external sharing features of SharePoint Online to share content with people outside your organization. Or, if this is not the case, you may want to limit the use of external sharing in your organization. In this article, we look at the SharePoint Online sharing options and how to plan for them.
  
(If you want to get straight to setting up sharing, see [Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off-for-sharepoint-online). If you're trying to share a file or folder, see [Share OneDrive files and folders](https://support.office.com/article/9fcc2f7d-de0c-4cec-93b0-a82024800c07) or [Share SharePoint files or folders in Office 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c).)
  
Planning for external sharing should be included as part of your overall permissions planning for SharePoint Online.
  
Note that external sharing is turned on by default for your entire SharePoint Online environment and the site collections in it. You may want to [turn it off globally](turn-external-sharing-on-or-off-for-sharepoint-online.md) before people start using sites or until you know exactly how you want to use the feature. 
  
## What are the external sharing features of SharePoint Online?

SharePoint Online has both global (tenant-wide) and site collection settings for external sharing. The tenant-level settings override any settings at the site collection level, and also affect OneDrive.
  
For your SharePoint Online tenant and for each individual site collection, you can choose from the following basic sharing options:
  
- No external sharing - sites and documents can only be shared with internal users in your Office 365 subscription.
    
- Sharing only with external users in your directory - sites, folders, and documents can only be shared with external users who are already in your Office 365 user directory. For example, users who have previously accepted a sharing invitation or users who you have imported from another Office 365 or Azure Active Directory tenant.
    
- Sharing with authenticated external users - sites can be shared with external users who have a Microsoft account or a work or school account from another Office 365 subscription or an Azure Active Directory subscription. When folders or documents are shared, the user is not required to log in using a Microsoft Account or a Work or School Account - they are sent a one-time code that they can use to verify their identity.
    
- Sharing with anonymous users - documents and folders (but not sites) can be shared via an anonymous link where anyone with the link can view or edit the document, or upload to the folder.
    
The list above is in the order of most to least restrictive. Whichever option you choose, the more restrictive functionality is still available to you. For example, if you choose to allow sharing with anonymous users, you can still share with authenticated external users and users already in your directory, including internal users.
  
 **Sharing and security**
  
If you have confidential information that should never be shared with external users, consider having one or more site collections where external sharing is turned off where you keep your confidential information. Create additional site collections as needed to use for external sharing. This helps you to manage security risk by preventing external access to sensitive information.
  
## What is an external user?

An external user is someone from outside your Office 365 subscription to whom you have given access to one or more sites, files, or folders. There are two types of external users:
  
 **Authenticated users**
  
Authenticated users are users who have a Microsoft account or a work or school account from another Office 365 subscription. You can share sites and documents with these users in much the same way that you share sites and documents with your internal users. Permissions and groups work the same for authenticated external users as they do for internal users.
  
Because external users do not have a license to your Office 365 subscription, they are limited to basic collaboration tasks:
  
- An authenticated external user can perform tasks on a site consistent with the permission level that they are assigned. For example, if you add an external user to the Members group, they will have Edit permissions and they will be able to add, edit and delete lists; they will also be able to view, add, update and delete list items and documents.
    
- Authenticated external users can use Office Online for viewing and editing documents. If your plan includes Office Professional Plus, they cannot install the desktop version of Office on their own computers unless you assign them a license.
    
- Authenticated external users will be able to see other types of content on sites, depending on the permissions you give them. For example, they can navigate to different subsites within the site collection to which they were invited. They will also be able to do things like view site feeds.
    
If your authenticated external users need greater capability, you must assign them an appropriate Office 365 license. Do this in the same way that you would assign a license to an internal user.
  
 **Anonymous users**
  
Anonymous users are users who have a shareable link to a folder or document and can view or edit the document or upload to the folder (depending on the type of link) without having to log in with a username or password. Anonymous links can be freely passed around between users and are valid until you disable them or they expire (if you've set an expiration date).
  
Anonymous users cannot access sites, and you cannot assign them licenses. They can only view or edit the specific document or folder for which they have an anonymous access link.
  
## What happens when I share a site or document?

When you share a site, folder, or document, what happens behind the scenes depends on whether you choose to share with authenticated external users or anonymous users.
  
 **Sharing sites with authenticated external users**
  
When you share a site with an authenticated external user, an invitation is sent to them via email which contains a link to the site or document. When they click the link, they are asked to log in using the username and password of their Microsoft account or their work or school account. When they log in, they are added to the users list in your Office 365 subscription (you'll see them listed with **#EXT#** in their user name) and given access to the site or document. 
  
Once they are in the user list in your Office 365 subscription, you can grant them access to other sites or documents without sending them additional invitations. (You may need to send them a link to the site or document so they can find it.) You can also assign them an Office 365 license if you want.
  
You can discontinue sharing with an authenticated external user by removing their permissions from the site, or by removing them from the user list in Office 365.
  
 **Sharing files and folders with authenticated external users**
  
When you share a file or folder with an authenticated external user, an email is sent to them which contains a link to the site or document. Each time they access the file or folder using the link, they are sent a time-sensitive code via email that they can use to verify their identity. They must enter the code to access the file or folder.
  
You can [discontinue sharing with an authenticated external user](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323) by deleting the sharing link that was sent to them. 
  
 **Sharing with anonymous users**
  
When you share with anonymous users, you can allow them to edit or to view a document or upload to a folder. View and edit links are created separately and can be set to expire at a specified time. Once you have created these links, they can be reused and passed around freely. Anyone with the link can access the document.
  
Anonymous users are not added to the user list in Office 365. You can discontinue sharing with them by going to the document or folder that you shared and deleting the anonymous link.
  
## Collaborating with external business partners

If you have business partners or vendors with whom you need to collaborate or share documents, consider setting up a SharePoint Online extranet site. An extranet site is a dedicate site collection that you use for business-to-business collaboration with a particular partner or vendor. You can lock this site down so that only site owners can invite external users and only external users from specific domains can be invited.
  
SharePoint Online extranet sites are very easy to set up and much easier and less expensive to maintain than on-premises extranet sites. For details, see [Use Office 365 SharePoint Online as a business-to-business (B2B) extranet solution](use-office-365-sharepoint-online-as-a-business-to-business-b2b-extranet-solution).
  
## 

||
|:-----|
|![The short icon for LinkedIn Learning.](../media/7e5cb7c8-dc66-4c9a-a16d-a30f10a970bd.png) **New to Office 365?**         Discover free video courses for [Office 365 admins and IT pros](68cc9b95-0bdc-491e-a81f-ee70b3ec63c5), brought to you by LinkedIn Learning. |
   
## Related Topics

[Manage sharing with external users in Office 365 Small Business](https://support.office.com/article/2951a85f-c970-4375-aa4f-6b0d7035fe35)
  
[Set up and manage access requests](https://support.office.com/article/94b26e0b-2822-49d4-929a-8455698654b3)
  
[Searching for site content shared with external users](https://go.microsoft.com/fwlink/?LinkId=620778)
  
[Plan your permissions strategy](https://support.office.com/article/c6183e49-9287-4689-999e-0d3f817a41a3)
  

