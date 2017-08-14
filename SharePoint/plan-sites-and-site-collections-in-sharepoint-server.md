---
title: Plan sites and site collections in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: cb6871cc-7fc5-4b54-9940-8c0ed51cb08f
---


# Plan sites and site collections in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Foundation 2013, SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-08-01* **Summary: ** Learn the critical decisions that you need to make in your SharePoint Server 2016 and SharePoint 2013 site planning process.Every SharePoint Server site belongs to only one site collection and a site collection is made up of one top-level site and all sites below it. As shown in the following figure, a site collection is the top level of organization in a SharePoint Server web application. The number of site collections you can have in a single web application depends on the capacity of your server infrastructure. For more information about SharePoint Server boundaries, see  [Software boundaries and limits for SharePoint Server 2016](html/software-boundaries-and-limits-for-sharepoint-server-2016.md). For more information about SharePoint Server site collections, see  [Overview of sites and site collections in SharePoint Server](html/overview-of-sites-and-site-collections-in-sharepoint-server.md). **Figure: Structure of a site collection in SharePoint Server**
  
    
    
![Diagram of a site collection](images/)
  
    
    
In this article:
-  [Sites and site collections planning principles](#section1)
    
  
-  [Methods of Site and Site Collection Organization](#section2)
    
  
-  [Inventory Your Farm](#section3)
    
  

## Sites and site collections planning principles
<a name="section1"> </a>

We recommend that you use these rules to plan your sites and site collections:
- Use one web application per farm to support all your site collections and sites.
    
  
- Keep your internally facing (intranet) SharePoint Server solution in a separate SharePoint Server farm from your externally facing (Internet) solution.
    
  
- Use host-named site collections instead of path-named site collections and place them in the default zone.
    
  
- Use path-named collections when you need to use alternate access mappings (AAMs).
    
  

## Methods of site and site collection organization
<a name="section2"> </a>

There are many ways your sites can be organized. Having a plan in place to help govern your site deployments will help you avoid random, unorganized site growth, enable better management of your SharePoint infrastructure, and provide a better user experience.
## Understand business needs

The first step in planning your site structure is to inventory the business problems and needs that you are using SharePoint Server 2016 to address. Then map your business needs to the site type best suited to meet them. This mapping will tell you the types of sites you will need. At the highest level, you will need sites that fall under the Collaboration category, the Enterprise category, the Publishing category, or the Custom category. For more information about the types of sites and how they are categorized, see  [Overview of sites and site collections in SharePoint Server](html/overview-of-sites-and-site-collections-in-sharepoint-server.md).
## Models for site collections

After you determine which types of sites your solution requires, the next step is to plan how these sites are implemented across site collections. A site collection is a hierarchical set of sites that can be managed together. Sites in a site collection have common features, such as: 
- Shared permissions
    
  
- Galleries for templates
    
  
- Content types
    
  
- Web Parts
    
  
- Often share a common navigation scheme
    
  
The main goal of site collection planning is to put a structure in place that your organization can grow in without creating unnecessary management overhead. Here is a generic model for an intranet SharePoint Server 2016 farm that will meet many needs. **Figure: Model of an intranet SharePoint Server farm**
  
    
    
![A suggested model for site collections](images/)
  
    
    
 **Internal Collaboration and Publishing**    You can create a site collection to host your internal team sites. These can be broken down into two major categories. One branch can be organized around your company’s internal hierarchy, with divisional portals hosting subsites for the individual long standing teams to use to store their content, collaborate, and publish their work out to the rest of the organization. Another peer branch can be for ad hoc or v-teams or project teams. These teams have members from across the long standing teams and need to have a collaboration and publishing space for a limited period of time. **Internal Enterprise Applications**    You can create a site collection to host sites and resources that everyone in your company will use. For example, your company intranet, enterprise search, My Sites, and records repositories. It is best practice to keep document center sites and records center sites in separate site collections. For more information, see [Configure My Sites and OneDrive for Business in SharePoint Server](html/configure-my-sites-and-onedrive-for-business-in-sharepoint-server.md). **Internet Presence**    It is best practice to place your company Internet presence in a separate SharePoint Server farm. Site collections of this type host resources that are available to anonymous users on the Internet. For example, you might use an Internet presence site to provide news articles or reviews that are tagged with metadata to categorize articles so that users can search or browse for information. For more information about how to design SharePoint Server for an Internet presence, see [Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server](html/overview-of-publishing-to-internet-intranet-and-extranet-sites-in-sharepoint-ser.md) and [Plan the logical architecture for cross-site publishing in SharePoint Server](html/plan-the-logical-architecture-for-cross-site-publishing-in-sharepoint-server.md).All sites in a site collection are stored together in the same SQL database. This can potentially affect site and server performance, depending on how your site collections and sites are structured, and depending on the purpose of the sites. Be aware of the following limits when you plan how to allocate your content across one or more site collections:
- Keep extremely active sites in separate site collections. For example, a knowledge base site on the Internet that allows anonymous browsing could generate lots of database activity. If other sites use the same database, their performance could be affected. By putting the knowledge base site in a separate site collection with its own database, you can free up resources for other sites that no longer have to compete with it for database resources.
    
  
- Because all content in a site collection is stored in the same content database, the performance of database operations — such as backing up and restoring content — depends on the amount of content across the site collection, the size of the database, the speed of the servers hosting the database, and other factors. Depending on the amount of content and the configuration of the database, you might have to divide a site collection into multiple site collections to meet service-level agreements for backing up and restoring, throughput, or other requirements. For more information, see  [Backup and restore best practices in SharePoint Server](html/backup-and-restore-best-practices-in-sharepoint-server.md).
    
  
- Creating too many sites below a top-level site in a site collection might affect performance and usability. The maximum recommended number of sites and subsites in a site collection is 250,000 sites. We recommend staying below 2,000 subsites per site collection. The maximum recommended number of site collections per farm is 500,000 Personal Sites plus 250,000 for all other site templates. For more information, see  [Site collection limits](software-boundaries-and-limits-for-sharepoint-server-2016.md#SiteCollection).
    
  
Once you have your site collection plan in place, you can move on to planning the organization of the sites in those site collections.
## Plan sites by organizational hierarchy
<a name="Section2a"> </a>

Plan the basic sites that you need based on the scale and structure of your organization. Some sites for larger divisions or projects can also combine information that is found on all the smaller subsites that are devoted to smaller long standing teams or v-teams that are responsible for time limited projects.Use the following guidelines when you plan sites that are based on your organizational structure: **Divisional or team sites**    Plan to create one site per team under a divisional rollup site. In large organizations, there might be several levels of sites, with each site focusing on the content that is created and managed at its level of the organization.You can design a site for members of your organization to collaborate on content related to your business or organizational goals. These can be self-contained or they can work with other sites as part of a publishing process. Often, these sites will have a mixture of collaborative content that is used internally and content that is intended for publication to an audience. **Rollup sites**    A rollup site surfaces content that is stored on other subsites. It makes it possible for users across divisions to find information, and experts. It often contains sites that are related to the overall organizational information architecture and that are usually mapped to the structure of the divisional or project sites.
## Plan application sites
<a name="Section2b"> </a>

An application site organizes team processes and provides mechanisms for running them. Application sites often include digital dashboards and other features to view and change data that is related to the site’s purpose. The information that is presented in an application site usually comes from diverse sources, such as databases or other SharePoint sites.For example, the human resources organization could design an application site to provide employees with:
- Access to general information, such as employee handbooks and career opportunities.
    
  
- Ways to do common tasks, such as submitting timecards and expense reports.
    
  
- Dashboards to view personalized information, such as an employee's salary and benefits history.
    
  
As another example, the internal technical support group in an organization could design a Help Desk application site to provide technical support to members of the organization. Features of the application site could include the following:
- Access to a knowledge base of past support incidents and best-practices documentation.
    
  
- Ways to do common tasks, such as starting a support incident or reviewing the status of an ongoing incident.
    
  
- Integration with communications features that support online meetings and discussions.
    
  
- Personalized views of data. For example, support managers could view dashboards that provide views of their team members' productivity and customer satisfaction ratings. Support engineers could view their current unresolved incidents.
    
  

## Plan publishing sites
<a name="Section2d"> </a>

By using a publishing site, authors can create and modify content in the form of web pages and documents, and they can use an approval process to make the content available to users who have the appropriate levels of viewing permissions. The publishing process involves creating content and then submitting it for approval. After content is approved, it is made available, or published, to the website for readers. This publishing occurs according to either a default schedule or a customized schedule, based on the needs of the project. Publishing sites can be used as intranet, extranet, or Internet sites, depending on the audience.For example, you might use a publishing site for an Internet site that publishes press releases. The public relations team creates press releases, uses the publishing workflow to approve new content, and specifies when it should be made available to consumers. As another example, you might use a publishing site for a corporate intranet site, where company news is made available to employees. Page authors can specify the target audience for their content, which makes the content viewable by only the members of the designated groups.You can use one of two ways to make published content available to users: author-in-place, or cross-site publishing. With the author-in-place method, you use a single site collection to author content and make it available to readers of your site. With the cross-site publishing method, you use one or more site collections to author content, and one or more site collections to control the design of the site and the display of the content. For more information, see  [Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server](html/overview-of-publishing-to-internet-intranet-and-extranet-sites-in-sharepoint-ser.md).
## Plan other sites
<a name="Section2e"> </a>

You can plan to make it possible for site users to create additional sites. For example, you can plan to give a My Site to each team member who uses a site. A My Site is a team site that is based on SharePoint Server and has public and private views. You can also make it possible for team members to create other sites, such as Document Workspace sites, when they collaborate on documents and other projects. Similarly, you can give users of an Internet site access to collaboration sites as part of a web-based service. For example, you can give them permissions to create Meeting Workspace sites and participate in online meetings as part of their experience of using your site.For information about the kinds of sites that you can create, see  [Overview of sites and site collections in SharePoint Server](html/overview-of-sites-and-site-collections-in-sharepoint-server.md).
## Inventory your farm
<a name="section3"> </a>

To help you with site and site collection planning, the Microsoft PowerShell command-line will inventory your entire SharePoint Server 2016 farm and get the properties of each site collection and site. It saves the results in a comma separated file (CSV). Use this inventory to identify what your site collection and site hierarchy are in each web application, and then plan where you want to add new sites. **To inventory a SharePoint farm by using Windows PowerShell**
1. Verify that you have the following memberships:
    
  - **Securityadmin** fixed server role on the SQL Server instance.
    
  
  - **db_owner** fixed database role on all databases that are to be updated.
    
  
  - Administrators group on the server on which you are running the PowerShell cmdlets.
    
  
  - In the Farm Administrators group
    
  

    An administrator can use the **Add-SPShellAdmin** cmdlet to grant permissions to use SharePoint Server cmdlets.
    
    > [!NOTE:]
      
2. Open the **SharePoint Management Shell**.
    
  
3. At the PowerShell command prompt, type the following command:
    
  ```
  
Get-SPWebApplication -IncludeCentralAdministration | Get-SPSite -Limit All | Get-SPWeb -Limit All | Select-Object URL, Title, Description, ParentWeb, AssociatedOwnerGroup, SiteAdministrators, WebTemplate, UIVersion, QuickLaunchEnabled, TreeViewEnabled, Language, Locale, Author, HasUniquePerm | Sort URL | export-csv <file location and name.csv>
  ```


    
    
    Where:
    
  -  *URL*  is the address of the site.
    
  
  -  *Title*  is name of the site as configured in site settings and displayed on the title bar of the site.
    
  
  -  *Description*  is the value in the description field in the sites properties.
    
  
  -  *ParentWeb*  is the site immediately above the inventoried site in the hierarchy.
    
  
  -  *AssociatedOwnerGroup*  is the group that owns the site.
    
  
  -  *Site Administrations*  are the current users who are listed as the sites primary and secondary site administrators.
    
  
  -  *Web Template*  is the type of site template that the site was created from.
    
  
  -  *UIVersion*  is the SharePoint Server version of the site.
    
  
  -  *QuickLaunchEnabled*  indicates if the site has the Quick Launch enabled in the vertical navigation.
    
  
  -  *TreeViewEnabled*  indicates if the site has the tree view enabled for the Quick Launch.
    
  
  -  *Language*  is the language the site was created in.
    
  
  -  *Locale*  is the locale of the site.
    
  
  -  *Author*  is who created the site.
    
  
  -  *HasUniquePerm*  indicates if the site inherits permissions from its parent site or implements unique permissions.
    
  
  -  *<file location and name.csv>*  is the location where you want to save the csv file and the name you want to give it. For example, 'C:\\FarmReports\\1.csv'.
    
  
For more information, see **Windows PowerShell for SharePoint Server 2016 reference**.
> [!NOTE:]

  
    
    


# See also

#### 

 [Software boundaries and limits for SharePoint Server 2016](html/software-boundaries-and-limits-for-sharepoint-server-2016.md)
  
    
    
 [Overview of publishing to Internet, intranet, and extranet sites in SharePoint Server](html/overview-of-publishing-to-internet-intranet-and-extranet-sites-in-sharepoint-ser.md)
  
    
    

  
    
    

