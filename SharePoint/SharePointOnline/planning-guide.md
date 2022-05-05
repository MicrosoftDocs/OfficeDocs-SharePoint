---
title: "SharePoint planning guide"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
ROBOTS: NOINDEX
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom: admindeeplinkSPO
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
ms.assetid: abacd1bb-295d-4235-afdd-15f5e4cc2e6c
description: "Learn important details that a SharePoint admin should consider when planning to build out, configure, and manage SharePoint sites."
---

# SharePoint planning guide
    
Here's an overview of important details you should consider when planning how to build out, configure, and manage your SharePoint environment. 
     
## Plan the sites you need to create
<a name="__toc346712635"> </a>

A site (previously called site collection) has the same owner and shares administrative settings, such as permissions. We recommend creating a separate site for each unit of work, and connecting them by using hub sites. To learn more, see [Planning your SharePoint hub sites](planning-hub-sites.md). 
  
### Plan your site details

 If you figure out a few basic details — for example, what a site will be used for, and which users need to have access to it — then this will help you make decisions about what type of site template to use, how much storage to allocate, and how many sites you might need to create. If you need to review your storage limits or the number of sites that are supported for your plan, see [SharePoint Limits](/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits). 
  
| If you want to determine this: | Ask this: |
|:-----|:-----|
|What type of site should I create?  <br/> For info about the new site templates and the variety of classic templates available in SharePoint, see [Using templates to create different kinds of SharePoint sites](https://support.office.com/article/449eccec-ff99-4cf3-b62e-dcfee37e8da4). | Do you want to connect a group of people for collaboration, or do you want to broadcast content to a larger audience?  <br/>  Will the site fill a specialized purpose? |
|How many sites do we need?  <br/>Some sites are automatically created for you when you sign up for Microsoft 365.|  How many divisions does your organization have and how much content do you need to promote across your organization. See [Plan an intelligent SharePoint intranet](plan-intranet.md) |
|How much storage do we need?  <br/> When your organization purchases the SharePoint service, it's allocated a pool of storage based on the subscription and number of licenses. For more information, see [Manage site storage limits](manage-site-collection-storage-limits.md). | How much content do you have and how much do users collaborate on files?  <br/>  How much storage comes with your subscription? |
|Do we need multi-language support?  <br/> The Multilingual User Interface (MUI) feature allows users to view sites or web pages in a language other than the default set on the site. The MUI feature is not a translation tool; it just changes the display language for certain default interface elements. For more info about multilingual sites, see [Introduction to multilingual features](https://support.office.com/article/53411469-53e3-4570-95e2-3651f166174f). | Do any sites need to be created in specific languages? |
   
### Plan to keep sites manageable

Governance is the set of policies, roles, responsibilities, and processes that control how your organization cooperates to achieve business goals. These goals center on the service you provide and the management of intellectual property your employees create. As you plan your sites, you should also build a plan for how to govern them. 
  
When you think about how to structure and govern your sites, consider the answers to these questions.
  
| If you want to achieve this: | Ask this: |
|:-----|:-----|
|An effective site consists of groups of individuals and teams that share common goals. |Does the structure of your sites add to your organization's effectiveness? |
|A secure site that is open to those who need the info, but where info is blocked from those who should not see it. |Does the structure allow the information architecture to meet regulatory requirements, privacy needs, and security goals? |
|A permissions model that allows read access, write access, or both. |What type of access will users need to the content? |
|Authorization for guests on only those sites that need it. For more info about allowing guests access to your sites, see [External sharing overview](external-sharing-overview.md). |Do users from outside the company need to have access? |
|A managed plan for sites that are well maintained. |Who will be allowed to create and manage sites? |
|Locations for specific actions and applications, such as sandbox solutions. |What features and functionality will be enabled for users? |
|A site where the content is useful to those sharing the site. |Will the content found in search results be relevant to those sharing the site? |
|A solution that is manageable and easy to upgrade. |How much customization will you allow? |
   
### Delete and restore sites
<a name="metadata"> </a>

As a SharePoint admin, you can delete and restore sites by using the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>. For info, see [Delete a site](delete-site-collection.md) and [Restore a deleted site](restore-deleted-site-collection.md).
  
## Manage permissions and help secure content
<a name="__toc349560423"> </a>

An important consideration when setting up and deploying a site is permission and security. Managing your user base and securing the content and data needs to be considered for a successful site. For info about the SharePoint admin role in Microsoft 365, and about the tasks of a SharePoint admin, see [About the SharePoint admin role in Microsoft 365](sharepoint-admin-role.md). 
  
### Allow guests access to your internal sites
<a name="__plan_for_user"> </a>

SharePoint provides the capability for site users to invite people outside the organization (that is, users who do not have a license to your Microsoft 365 subscription) to view or edit content on sites. External sharing is a powerful collaboration feature that can support your organization's needs to collaborate with external vendors, customers, or clients. However, it is important to manage external sharing carefully to ensure that any content that you do not want shared is adequately protected. For info, see [External sharing overview](external-sharing-overview.md).
  
External sharing is enabled by default for your SharePoint environment (tenant) and the sites in it. You might want to turn it off globally before people start using sites or until you know exactly how you want to use the feature. After you turn it on globally, you can allow external sharing for specific sites, while keeping it turned off for site collections that will store content that is sensitive for your business. You should give thoughtful consideration to where you enable external sharing and what level of external sharing you allow.
  
For info about how users can share content, see [Share SharePoint files or folders in Microsoft 365](https://support.office.com/article/1fe37332-0f9a-4719-970e-d2578da4941c).
  
### Protect content with Information Rights Management (IRM)
<a name="__protect_content_with"> </a>

SharePoint IRM uses Microsoft Azure Active Directory Rights Management Services (RMS), an information protection technology in Microsoft 365. Information Rights Management (IRM) protection can be applied to files in SharePoint lists and libraries. To learn more, see [What is Microsoft Azure Active Directory Rights Management?](/azure/information-protection/what-is-azure-rms)
  
When IRM has been enabled for a list or library, files are encrypted so that only authorized people can view them or take specific actions on them. Each rights-managed file also contains an issuance license that imposes restrictions on the people who view the file. Typical restrictions include making a file read-only, disabling the copying of text, preventing people from saving a local copy, and preventing people from printing the file. Client programs that can read IRM-supported file types use the issuance license within the rights-managed file to enforce these restrictions. This is how a rights-managed file retains its protection even after it is downloaded.
  
By default, IRM is disabled when you sign up with Microsoft 365. Before you turn on the IRM service using the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>, the Microsoft 365 global admin needs to first install the Microsoft PowerShell module for Rights Management and then connect to the Rights Management service. For more info, see [Set up Information Rights Management (IRM) in SharePoint admin center](/office365/securitycompliance/set-up-irm-in-sp-admin-center) and [Apply Information Rights Management (IRM) to a list or library](https://support.office.com/article/3bdb5c4e-94fc-4741-b02f-4e7cc3c54aa1).
  
## Manage user profiles
<a name="__plan_for_personal"> </a>

Whether you manage your user accounts in Microsoft 365 only or sync on-premises directory objects, if there's information you want to add to user profiles, but no field for it, then you might consider creating a SharePoint user profile property. For info, see [Manage user profiles in the SharePoint admin center](manage-user-profiles.md). Keep in mind that these properties are specific to SharePoint and this info will not be replicated to Microsoft 365. 
  
If you want to help owners of classic sites target content to specific groups of people, you might want to use audiences. For info, see [Manage audiences](manage-user-profiles.md#manageaudiences).
  
## Evaluate business needs to help plan feature configuration
<a name="__toc349560425"> </a>

There are some features that can be configured or managed globally from the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>. To help you plan time and resources, it is useful to evaluate whether your organization has a business need for specific features. 
  
### Determine subject matter experts and partners

This step will help you determine where you may need to engage subject matter experts in your organization to help partner with admin staff in planning the configuration of these features. For example, to gather the necessary requirements for configuring features like the Term Store, or Records Management features like the Content Organizer, you may need to partner with the people in your organization who are responsible for corporate taxonomy, records management, or content management.
  
| Do you need these capabilities? | To learn more about setting this up, go here: |
|:-----|:-----|
|You need to configure Search for your SharePoint environment. |[SharePoint search administration overview](manage-search-the-admin-center.md) |
|You want to create and use taxonomies to classify and organize information on sites. | You can use the Term Store Management Tool to create, import, and manage hierarchical collections of centrally managed terms (called term sets).  <br/> [Introduction to managed metadata](managed-metadata.md) |
|You need to work with business data that is stored in external applications, and you want to be able to integrate that data into SharePoint sites. | You can use Business Connectivity Services to connect to data sources such as SQL Azure databases or Windows Communication Foundation web services (also known as WCF).  <br/> [Introduction to external data](https://support.office.com/article/676e60e7-d99f-463f-a173-65e9d63538c0) <br/> [Manage Business Connectivity Service Applications](manage-business-connectivity-service-applications.md) <br/> [Create or edit a Secure Store Target Application](create-or-edit-secure-store-target-application.md) <br/> [Create an external list](https://support.office.com/article/6e2d601d-b02f-41e7-ba87-e70297ec6665) <br/> [Make an External List from a SQL Azure table with Business Connectivity Services and Secure Store](make-external-list.md) |
|You need to automatically route content to specified locations based on records management or document management criteria. |[Configure Send To connections for records management](https://support.office.com/article/d3bdb395-3824-49ed-9de4-c479a4bc71ea) |
|You want to provide users with the ability to find and install internally-developed business apps or third-party apps to customize and extend sites. |[Plan customizations, solutions, and apps for SharePoint](extend-and-develop.md) <br/> [Use the App Catalog to make custom business apps available for your SharePoint environment](use-app-catalog.md) <br/> [Configure settings for the SharePoint Store](configure-sharepoint-store-settings.md)  <br/> [Monitor apps for your SharePoint environment](monitor-apps.md) |
   
## Evaluate partner solutions
<a name="__configure_infopath_forms"> </a>

As part of your planning, you should evaluate whether your organization has specific business needs that might require you to use third-party services or applications to customize SharePoint. For example, your organization might need to migrate a large volume of content or a large number of users to your SharePoint site. Or you might have business processes that require support for email-enabled lists. If you think that your organization might benefit from third-party services or applications, please explore the professional services and applications available from partners in the [Microsoft Partner Center](https://go.microsoft.com/fwlink/?linkid=839525). You can find experts to help you deploy in the cloud or tailor Microsoft 365 for the needs of your business. It is a good idea to explore and research available third-party services and solutions at the beginning of your planning process. 
