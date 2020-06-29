---
title: Add and customize the New Employee Onboarding hub
ms.reviewer: 
ms.author: hokavian
author: hokavian
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Learn how to add and customize the NEO hub to your tenant"
---

# Overview of the Microsoft New Employee Onboarding hub 
Microsoft has created an open source New Employee Onboarding (NEO) hub to help organizations improve their onboarding process and experience the benefits of a well-planned new employee onboarding process. The NEO hub helps organizations: 

- Provide new employee experiences and information
- Connect new employees to people & culture
- Help stakeholders easily contribute to new employee onboarding
- Measure effectiveness of new employee onboarding

### Why invest in a new employee onboarding site?
New employee onboarding (NEO) should be a strategic process that integrates new employees into an organization and its culture while providing the knowledge and tools needed to become fully contributing team members. 
NEO processes often fall short for both the new hires and the organization. Only 12% of employees strongly agree their organization does a great job of onboarding new employees.   An engaging and well organized NEO process can make all the difference in helping a new hire navigate through an exciting – but stressful -  career journey, and it can have major organizational benefits. 

Strategically planned NEO experience can:

**Improve new hire performance and time to productivity** -
Organizations with a standard onboarding process report 50% greater new-hire productivity.   

**Improve new employee retention** -
69% of employees are more likely to stay with a company for three years if they had a great onboarding experience. Employees who have a negative onboarding experience are twice as likely to look for new opportunities in the near future.    

### The NEO experience process:

| Provide new employee experiences and information      | Connect new employees to people and culture     | Help stakeholders easily contribute to new employee onboarding  | Measure effectiveness of new employee onboarding
| :------------------- | :------------------- |:----------------|
| Sense of place       | Pre-onboarding       | Departmental and team onboarding |  Value realization
| Onboarding journey   | Social connections and live events  | Easy to create and maintain compeling content experiences     | New employee surveying



### NEO hub features:

- **A fully configured and customizable set of new hire related sites built on SharePoint Online communication sites:** The NEO hub includes the sites, information architecture, design, user interface and features to help provide new hires with a great onboarding experience. The NEO hub can be customized to add your organization’s new hire content and to align with its look and feel. The NEO hub sites are responsive and work as they should on mobile. 
- **Onboarding journey:** Onboarding can be an overwhelming experience for new hires with everything the new hire is typically expected to do and learn in a short period of time. Avoid overwhelming your new employees by providing them a curated onboarding journey that paces the new hire through a configurable activity list of administrative, technology, culture, training, and connection related to-do’s. The onboarding journey comes with a pre-configured list of new employee onboarding activities for you to customize for your processes. 
- **Sample new hire site pages:** To inspire and provide design templates for arranging your content, the NEO hub includes sample inner site pages. Use these site pages as templates for your content. 
- **Easy provisioning:** Provision the NEO hub from the SharePoint look book with just a few steps.

### NEO hub sites: 
New employee onboarding involves multiple levels within an organization, including corporate onboarding, and departmental onboarding. Sometimes teams within a department also need a unique onboarding experience. Each onboarding level provides its own unique value, contributing to a comprehensive onboarding experience each new employee should experience. 
Research has shown pre-onboarding new hires, after they sign their acceptance letter but before they officially join the company, can lead to higher performance and better retention rates. 
To deliver a consistent and integrated new hire onboarding experience the Microsoft open source New Employee Onboarding hub consists of three types of SharePoint site templates, designed to work as one cohesive and familiar experience for new hires. 

![Image of the NEO hub content](media/neotimeline.png)

1.	**Pre-Onboarding site:** A site for new hires, who have yet to officially join the company, to learn more about the company they have joined and to get ready for their official start date. External guest access can be used for providing pre-start hires, with no corporate credentials, access to the pre-onboarding site only. 
2.	**Corporate onboarding site:** A place for new hires to visit to get the information they need and make the connections they want to successfully onboard to the organization. 
3.	**Departmental onboarding sites:** A place for new hires to visit to learn more about the department they are joining, its people, culture, and priorities. The new employee onboarding hub includes two departmental template sites, one for an engineering department and one for a sale department


## Step 1: Provision NEO hub
The New Employee Onboarding (NEO) hub can be provisioned from the [SharePoint look book](https://lookbook.microsoft.com/). With the SharePoint look book, an Office 365 Tenant Administrator can start the provisioning process with a few simple clicks. It is fast, easy, and takes only a few minutes to start the process. Before starting the provisioning process, make sure you have met the prerequisites for provisioning.


### Prerequisites
To successfully set up the NEO hub via the SharePoint look book, the person doing the provisioning must be a Tenant Administrator of the tenant where the NEO hub will be provisioned.


### Provision the NEO hub



1.	Go to the [NEO hub solution page](https://provisioning.sharepointpnp.com/details/3df8bd55-b872-4c9d-88e3-6b2f05344239).
2.	Select **Add to your tenant**. If you are not signed into to your tenant, the SharePoint look book will ask for your Tenant Admin credentials.
3.	From the permissions requested dialog box, select **Consent on behalf of your organization** and then select **Accept**.
The provisioning service requires these permissions to provision the site template. There is no overall impact on your tenant and these permissions are explicitly used for the purpose of the solution installation. You must accept these permissions to proceed with the installation.
4.	Complete the fields on the provisioning information page as appropriate for your installation. At a minimum enter the email address where you wish to get notifications about the provisioning process and the url prefix for your site to be provisioned to.

> [!NOTE]
> The provisioning of the NEO Hub will result in four separate site collections getting installed in your tenant: i) Pre-Onboarding site, ii) Corporate new hire site, iii) Engineering new hire site, and iv) Sales new hire site. To differentiate these four sites from each other in terms of the url’s that get assigned, you must confirm a url prefix that will get applied to each of the four sites – e.g., i) neo/preonboarding, ii) neo/corporate, iii) neo/engineering, and iv) neo/sales. Make the url prefix for your site something intuitive for your team members such as "/sites/MyTraining" or "/teams/LearnMicrosoft365".


6.	Select **Provision** when ready to install the NEO hub into your tenant environment. The provisioning process will take up to 15 minutes. You will be notified via email (to the notification email address you entered on the Provisioning page) when the site is ready for access.


### Add owners to the site
As the Tenant Admin, it's unlikely you'll be the person customizing the sites, so you'll need to assign a few site owners to the sites. Owners have administrative privileges on the site so they can modify site pages, content, and branding. 
1.	From the SharePoint **Settings** menu, select **Site Permissions**.
2.	Select **Advanced Permission Settings**.
3.	Select **Microsoft 365 learning pathways Owners**.
4.	Select **New > Add Users to this group**, and then add the people you want to be site owners.
5.	Include the site URL in the Share message, and then select **Share**.



## Step 2: Customize the onboarding experience 
The New Employee Onboarding (NEO) hub consists of four SharePoint site templates that can be customized to fit the needs of your users and organization. Many of the core pages are already built and pre-populated with content. Review content on sites and pages, then plan on customizing content, images, branding, web parts, and pages.

It’s important to make sure the right content is available to users at the right time. It’s also important to make new employees feel welcome before their first day. Organizations with a standardized onboarding process report 50% greater new-hire productivity.    Alternatively, employees who have a negative onboarding experience are twice as likely to look for new opportunities shortly after starting a new job.    

Before you customize content in the NEO experience, ensure you understand the needs of your users and the business objectives of your organization. New hires will need different kinds of support and resources depending on the onboarding phase and culture of your organization. Begin by signing into your account and reviewing pre-populated content. Then, customize content and prepare to share the site with new hires. 

### NEO hub contents:

![Image of the NEO hub content](media/neotimeline.png)
 
1.	**Pre-Onboarding site:** A site for new hires, who have yet to officially join the company, to learn more about the company they have joined and to get ready for their official start date. External guest access can be used for providing pre-start hires, with no corporate credentials, access to the pre-onboarding site only. 

2.	**Corporate onboarding site:** A place for new hires to visit to get the information they need and make the connections they want to successfully onboard to the organization. 

> [!NOTE]
> The corporate new hire site is a hub and the departmental site templates are associated sites. This creates a coherent and consistent experience for the new hire across the corporate and departmental new hire sites. [Learn more about SharePoint hub sites](https://support.microsoft.com/office/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f).


3.	**Departmental onboarding sites:** A place for new hires to visit to learn more about the department they are joining, its people, culture, and priorities. The new employee onboarding hub includes two departmental template sites, one for an engineering department and one for a sale department. Consider associating departmental onboarding sites with existing department portals if you have them.


### Get started - Sign into your Microsoft 365 account 

> [!NOTE]
> You need to be a site owner to customize and share the NEO sites. Work with your SharePoint administrator if you don’t already have access.


1.	Open your web browser and navigate to [office.com](office.com) or your organization’s sign-in location
2.	Sign in with your username and password
3.	Navigate to the location of the site using the URL supplied by your tenant administrator, or select SharePoint from the Microsoft 365 home page, and then select the site



### Explore and review pre-populated content
#### Pre-Onboarding site:
This is where new hire starts their onboarding journey. This site is for new hires who have accepted their job offer but have not officially joined the company yet. In this stage, new hires will be interested in learning more about the company, how to get ready for their official start date, and who to go to for questions. 

> [!NOTE]
> The NEO hub comes with many pre-built pages that can be identified in the site navigation with this symbol ">>." Determine which pages and content to keep, edit, or delete based on the needs of your organization. 

![Image the pre-onboarding site](media/preneo.png)
 
#### Pre-populated site content:
- **Home page** – This is the first site your user will see after they agree to accept the job. Use this landing page as an opportunity to highlight big concepts and get new employees excited about starting their new job. Provide content for topics like organization leaders, values, communities of interest, benefits, and career planning resources. 

> [!IMPORTANT]
> Plan to connect social media accounts to the [Hero web part](https://support.microsoft.com/office/use-the-hero-web-part-d57f449b-19a0-4b0d-8ce3-be5866430645) and the [Twitter web part](https://support.microsoft.comoffice/use-the-twitter-web-part-15db6b3b-d167-41dd-9875-2af64b44d820)

- **Welcome** – Give new hires a warm welcome and place to start understanding onboarding tasks and how to prepare for their first day. This is a good opportunity to include a video message from leadership. Use the [YouTube web part](https://support.microsoft.com/office/use-the-youtube-web-part-c14fa2c1-71dc-4e52-94b6-b4876742382f), or [Embed web part](https://support.microsoft.com/office/add-content-to-your-page-using-the-embed-web-part-721f3b2f-437f-45ef-ac4e-df29dba74de8) to display the video.
- **Contoso 101** – Provide high level information about the organization that engages and excites. Share more about leadership and values in Our leadership team and Our values pages.
- **Prepare for your first day** – Ensure new hires feel prepared and supported on their first day by providing details on what to bring and where to go. 
- **Help & Support** – Highlight where to go for support and customize questions and answers for the FAQ page.



#### Corporate new hire site:
This is the hub for the new employee onboarding experience and is designed to provide a high-level view of organizational goals, leadership, team structure, and resources. In this phase, users are looking for guidance, support, and clarity. Use this site to outline onboarding details and expectations during the first months of onboarding. Ensure users have access to support channels like [Yammer](https://support.microsoft.com/en-us/office/use-a-yammer-web-part-in-sharepoint-online-a53cfa0c-3d09-42c8-a286-1038a81c59da), write FAQs relevant to your organization, and customize the [onboarding checklist](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7) to include the activities you want all new hires to do in their first 30, 60, 90 days.

![Image the corporate onboarding site](media/neocorp.png)

##### Corporate new hire site navigation:

![Image of the NEO hub navigation](media/neohubnav.png)
 
#### Pre-populated hub contents:
- **Corporate onboarding (home page)** – Highlight key resources in hub navigation. Customize the [hub and site navigation](https://support.microsoft.com/office/customize-the-navigation-on-your-sharepoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca) to display major content categories to new hires.
- **Who we are** – Introduce users to more detail about the organization in the Our story, Our leadership, Our teams pages. Customize these pages and the Office locations page for your organization.
- **Help & Support** - Highlight where to go for support and customize questions and answers for the FAQ page.
- **Community** – Help new hires start building community right away and make sure new hires are aware of Employee resource groups and other connection channels.
- **Departmental onboarding** – Provide an entry point to departmental-level information from the hub navigation where users can access departmental onboarding sites. Templates for an Engineering and Sales onboarding site have been included. Use these site templates as both a source of inspiration of what your organization’s departmental onboarding sites could look like and to accelerate the creation of these sites for your organization.  	

##### Pre-populated site (Corporate new hire site) contents:
- **Home page** – Provide a high-level view of big concepts that will be relevant to new users. This is a great location to help new employees build their network and learn from more experienced and knowledgeable employees with [Microsoft Teams live events](https://docs.microsoft.com/microsoftteams/teams-live-events/what-are-teams-live-events#:~:text=Microsoft%20365%20live%20events%20bring%20live%20video%20streaming,community%20resides%2C%20using%20Microsoft%20Stream%2C%20Teams%2C%20or%20Yammer.)
- **Start here** – Specify what new hires should do in their first 30, 60, and 90 days of onboarding by creating an onboarding process in on the Start your journey here page. The new hire checklist found in this section comes pre-populated with a set of generic onboarding activities. Customize list content to meet your needs. [Learn more about working with SharePoint lists](https://support.microsoft.com/office/introduction-to-lists-0a1c3ace-def0-44af-b225-cfa8d92c52d7).


#### Departmental onboarding:
From the corporate onboarding hub, users can access specific resources for departmental onboarding. Here, users need to learn about departmental leadership, culture, goals, and resources. Use departmental sites to provide access to communication channels, training guides, and events relevant to new hires.The new employee onboarding hub includes two departmental template sites, one for an engineering department and one for a sale department. Consider associating departmental onboarding sites with existing department portals if you have them.

![Image of the NEO departmental site](media/neodepartmental.png)

##### Departmental site location in NEO hub navigation:

![Image of the NEO departmental site](media/neocorpnav.png)
 

##### Pre-populated site contents:
- **Home page** - Provide a high-level view of big concepts that will be relevant to new hires.
- **Getting started** – Help users quickly understand onboarding tasks, departmental procedures, and anything else that will help new hires be successful. 
- **Meet the team** – Introduce new hires to people, the organization structure and goals on the Leadership, The organization, and Our priorities pages.
- **Help and support** - Highlight where to go for support and consider creating a FAQ section.


**Next steps:** Customize place-holder content, edit the site navigation, add pages as needed, and hook up social media accounts in web parts.



### Customize the content and look of your NEO sites 
Now that you’ve reviewed the pre-built pages and pre-populated content, you are ready to customize the NEO experience for your organization. 

#### Navigation

Site navigation is important because it helps users immediately understand what can be accomplished on a given site. The most effective SharePoint sites help viewers find what they need quickly so that they can use the information to make decisions, learn about what is going on, access the tools they need, or engage with colleagues to help solve a problem. Edit the hub and site navigation for all three NEO site designs to meet the needs of your audience and organization. [Learn how to edit site navigation](https://support.microsoft.com/office/customize-the-navigation-on-your-sharepoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca). 

 
#### Web parts
Customize web parts with images, labels, links, and content that align with your organization’s mission. Keep images and descriptions simple and easy to understand for your new-hire audience.

- **Hero web part** - Bring focus and visual interest to your page with the [Hero web part](https://support.microsoft.com/office/use-the-hero-web-part-d57f449b-19a0-4b0d-8ce3-be5866430645). You can display up to five items in the Hero web part and use compelling images, text, and links to draw attention to each.
- **Text web part** - Use the [Text web part](https://support.microsoft.com/office/add-text-and-tables-to-your-page-with-the-text-web-part-729c0aa1-bc0d-41e3-9cde-c60533f2c801) to add paragraphs to your page. Formatting options like styles, bullets, indentations, highlighting, and links are available.
- **Image web part** – Use the [Image web part](https://support.microsoft.com/office/use-the-image-web-part-a63b335b-ad0a-4954-a65d-33c6af68beb2) to add an image to a page.
- **Quick links web part** – Organize and display links to other resources with the [Quick links web part](https://support.microsoft.com/office/use-the-quick-links-web-part-e1df7561-209d-4362-96d4-469f85ab2a82).
- **People web part** – Use the [People web part](https://support.microsoft.com/office/show-people-profiles-on-your-page-with-the-people-web-part-7e52c5f6-2d72-48fa-a9d3-d2750765fa05) to display profile photos, contact information, and organizational information for people at work.
- **Twitter web part** - Use the [Twitter web part](https://support.microsoft.com/office/use-the-twitter-web-part-15db6b3b-d167-41dd-9875-2af64b44d820) to highlight topics and conversations on SharePoint pages.
- **YouTube web part** - Use the [YouTube web part](https://support.microsoft.com/office/use-the-youtube-web-part-c14fa2c1-71dc-4e52-94b6-b4876742382f) to embed YouTube videos right on your page.

#### Site theme and branding
Edit the look of your SharePoint site to align with your organization's brand. Customize the site display name, logo, theme, header layout, navigation style, and more in the [Change the look panel](https://support.microsoft.com/office/customize-your-sharepoint-site-320b43e5-b047-4fda-8381-f61e8ac7f59b).

#### Hub site settings

SharePoint hub sites help connect and organize sites based on project, department, division, region, etc. making it easier to:

- Discover related content such as news and other site activities
- Apply common navigation, branding, and site structure across associated sites
- Search across all associated sites. 

Considering associating your departmental new hire sites to your existing departmental onboarding site. Learn how [hub site associations](https://support.microsoft.com/office/associate-a-sharepoint-site-with-a-hub-site-ae0009fd-af04-4d3d-917d-88edb43efc05) work and how to manage hub settings for your organization. Learn more about [SharePoint hub sites](https://support.microsoft.com/office/what-is-a-sharepoint-hub-site-fe26ae84-14b7-45b6-a6d1-948b3966427f).



#### More customization resources: 
- Add a [page to a SharePoint site](https://support.microsoft.com/office/add-a-page-to-a-communication-site-ce16986a-25ec-4907-b820-44d01ae8afb5)
- How to use [web parts on SharePoint pages](https://support.microsoft.com/office/using-web-parts-on-sharepoint-pages-336e8e92-3e2d-4298-ae01-d404bbe751e0)
- Use the [Events web part](https://support.microsoft.com/office/use-the-events-web-part-5fe4da93-5fa9-4695-b1ee-b0ae4c981909)
- Use the [News web part](https://support.microsoft.com/office/use-the-news-web-part-on-a-sharepoint-page-c2dcee50-f5d7-434b-8cb9-a7feefd9f165)



## Step 3: Share the NEO sites with end users

After customizing content, get ready to share the new onboarding experience with new hires. Different permissions will apply to the pre-onboarding site since users will be external guests. Once new hires start working, use internal permissions sharing instructions to give access to the corporate onboarding site. 

### Pre-onboarding site: External guest access 

> [!NOTE]
> If you are unable to add visitors to the pre-boarding site, work with your SharePoint administrator to [configure guest settings](https://docs.microsoft.com/sharepoint/change-external-sharing-site). 


<<<<<<<Need to validate guidance here>>>>>>>>>


### Corporate new hire site and departmental sites

1.	Select **Share site** from the right-hand corner
2.	In the **Share site** pane, enter the names of people or groups to add them to the site, or enter "Everyone except external users" to share the site with everyone in your organization.  
3.	Change the permission level (Read, Edit, or Full control) as needed.
4.	Enter an optional message to send to the person or clear the Send email box if you don't want to send an email.
5.	Select **Share**.




## Step 4: Measure the impact of your New Employee Onboarding hub

### Define NEO hub success metrics

Define site success metrics to measure and optimize your organization’s onboarding process. The following is an example of possible metrics for a new employee onboarding hub:

| Objective      | Business owner   | KPI measure | Data source   | KPI formula    | KPI baseline    | KPI target   |
| :------------------- | :------------------- |:----------------|:------------------- | :------------------- |:----------------| :----------------|
| Help onboard new employees more effectively   | Diego Siciliani   | New employee satisfaction  |  Survey data  |  Average score of new employee satisfaction with NEO Hub   |  N/A   | 4.25  
| Help onboard new employees more effectively   | Diego Siciliani   | NEO hub usage  |  Site usage report  |  Number of unique viewers and visits   |  N/A   | 500 unique viewers/month and 1,500 views/month
| Increase new employee retention  | Alexandre Levesque  | New employee retention  |  HR system retention data  |  % of new employee cohort that remain with the company after one year   |  75%   | 90%
| Improve new employee engagement  | Diego Siciliani    | New employee engagement score |  Survey data  |  Average score of new employee engagement question  |  3.75   | 4.25


### Leverage site usage data

As a SharePoint site owner, you can view site usage data that shows you how users are interacting with your site. For example, you can see the number of people who have visited the site, how many times people have visited the site, and a list of files that have received the most views. Site owners should utilize SharePoint’s built-in site usage reporting capabilities to measure the impact of the NEO hub. [Learn how to view usage analytics for your site](https://support.microsoft.com/office/view-usage-data-for-your-sharepoint-site-2fa8ddc2-c4b3-4268-8d26-a772dc55779e).

**Example of site usage data:**

![Image of SharePoint site analytics data](media/neositeusagereport.png)




## Step 5: Manage and maintain your NEO hub

The NEO Hub should present the most up to date content your organization has to offer, so you’ll need to commit to maintaining relevant content throughout the experience. Develop a plan to audit content and refresh web parts as needed to ensure contact information, FAQs, the onboarding checklist, and People web parts are up tp date. Learn more about [managing communication sites](https://support.microsoft.com/office/manage-your-sharepoint-communication-site-21761aac-f7f7-4499-b0ca-cf283477c32f). 

- Train site owners and authors. Make sure all site owners and authors have appropriate training and access to [maintain the site](https://support.microsoft.com/office/manage-your-sharepoint-communication-site-21761aac-f7f7-4499-b0ca-cf283477c32f).
- Update content in web parts. Keep web parts like the People web part updated to ensure you are leveraging the full value of the NEO Hub.
- Review previously established metrics after the launch. Use insights from [site analytics](https://support.microsoft.com/office/view-usage-data-for-your-sharepoint-site-2fa8ddc2-c4b3-4268-8d26-a772dc55779e) to promote content on the home page, update navigation, or re-write content for clarity.
- Establish a schedule to audit content. Plan when site owners should audit content in advance to make sure your sites are always up to date.
- Periodically review your site settings. Make [changes to the settings](https://support.microsoft.com/office/manage-your-sharepoint-site-settings-8376034d-d0c7-446e-9178-6ab51c58df42?ui=en-us&rs=en-us&ad=us), site information, and permissions for the site as needed.


## NEO hub FAQs

**Question**: What are the requirements for installing the New Employee Onboarding (NEO) Hub into my tenant environment?
**Answer**:
- SharePoint Online and Communication Sites enabled.
- The individual that will be provisioning CLO365 must be the tenant administrator of the target tenant for install.


**Question**: How long will it take to install the site in our tenant environment?
**Answer**: Based on our testing of the installation, it should take less than 15 minutes. This does not include time required to customize the site to your requirements.



**Sources**:

  - Gallup, State of the American Workplace, 2017
  - SHRM, Don't Underestimate the Importance of Good Onboarding, 2017
 -  Source: Digitate, Super CIO: What the CIO sees—that other people don’t, 2018






















