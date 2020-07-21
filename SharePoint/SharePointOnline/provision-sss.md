---
title: Overview of the SharePoint Success Site 
ms.reviewer: 
ms.author: Holland-ODSP
author: Holland-ODSP
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
description: "Overview of the SharePoint Success Site"
---

# Overview of the SharePoint Success Site 

The SharePoint Success Site is a ready to deploy and customizable SharePoint communication site that helps your organization maximize the adoption of SharePoint. The SharePoint Success Site is designed to support new SharePoint site owners in creating high-impact sites to meet the goals of your organization. Install the SharePoint Success Site in your tenant environment, customize the pre-populated training content, and make it available to end users.


### Why invest in a SharePoint Success Site?
The SharePoint Success Site helps site owners improve the quality and impact of the sites they build in SharePoint for internal audiences, while helping ensure they follow your organization’s site usage guidelines. 

Leverage the SharePoint Success Site to:

- **Get more out of SharePoint** - Teach new site owners how to utilize the power behind SharePoint's communication and collaboration features. 
- **Enable site owners to create high-impact sites** - Ensure site owners have the right information and support to create purposeful sites that are widely adopted by the intended audience. 
- **Ensure site owners follow site creation policies** - Customize the site creation policy page on your SharePoint Success site to communicate organizational policy expectations early.
- **Provide the most up-to-date content** - Equip site owners with SharePoint self-help content that is maintained by Microsoft and published as SharePoint evolves.


#### Summary of how to launch a SharePoint Success Site:

| Step 1      | Step 2       | Step 3  | Step 4
| :-------------- | :---------------|:-----------| :-----------|
| Meet the pre-requisites to provisioning the SharePoint Success Site      | Provision the SharePoint Success Site       | Customize the site design, playlists, content, and site creation guidelines |  Launch and share the site 


### SharePoint Success Site features
The SharePoint Success Site is designed to reduce the amount of work needed to plan, build, and manage new SharePoint sites for site owners and content authors in order to expedite your organization’s progress.

SharePoint Success Site features:

- **Fast provisioning:** Provision the SharePoint Success Site from the [Look book](https://lookbook.microsoft.com/) with just a few easy steps.
- **Easily customizable:** Edit the site layout, branding, and Microsoft-provided playlist content to align with how you have set up SharePoint in your tenant.
- **Comprehensive site owner training content:** Training on what makes an effective site and how to build and maintain the site.
- **Site creation guidelines:** Create SharePoint usage guidelines that fit compliancy requirements for your organization.
- **Create your own training playlists:** Add your own custom training content and playlists specific to your organization's desired business outcomes beyond SharePoint.



### What comes with a SharePoint Success Site 
The SharePoint Success Site comes with web parts and content to guide your users through the most up-to-date site creation training. There are several opportunities to customize the experience to better suit your organization’s goals, tenant configuration, and usage policy. 

#### SharePoint communication site 
The SharePoint Success Site is a SharePoint communication site that includes pre-populated pages, web parts, and site navigation. The site can be customized to incorporate your organization's existing branding, support, and community content.

![Image of the SharePoint Success Site landing page](./media/sss-landing.png)

#### Microsoft 365 learning pathways
When you provision the SharePoint Success Site, you will first be required to install [Microsoft 365 learning pathways](https://docs.microsoft.com/office365/customlearning/). M365 learning pathways connects to a Microsoft-maintained content repository that includes publicly available SharePoint help content. As the content repository is updated, M365 learning pathways will automatically display updated SharePoint content. With M365 learning pathways, you can also create targeted training playlists that meet the needs of your organization beyond SharePoint training by uploading custom playlists. 

![Image of the Microsoft 365 learning pathways solution](./media/m365-learning-pathways.png)

#### Microsoft-maintained content feed
The SharePoint Success Site’s up-to-date content feed includes a range of content that helps new users and existing site owners plan, build, and manage SharePoint sites:

- **Plan your site:** Guidance on how to plan a site, including what type of SharePoint site to use, access rights, and permission strategy.
- **Create your site:** Content that helps new site owners create their site, including how to brand and customize their site and how to add content.
- **Share and manage your site:** Guidance to help launch, share, and manage the new site.

#### Success stories
The success stories section is a gallery for organizations to showcase internal SharePoint site success stories that inspire others in the organization. Learn how to create a [Microsoft Form](https://support.microsoft.com/office/create-a-form-with-microsoft-forms-4ffb64cc-7d5d-402f-b82e-b1d49418fd9d#:~:text=%20Create%20a%20form%20with%20Microsoft%20Forms%20,names%20can%20contain%20up%20to%2090...%20More%20) to solicit success stories from site owners and authors, and publish on your SharePoint Success Site to inspire.

![Image of the Success Stories page](./media/sss-success-stories.png)

#### Site creation guidelines 
The site creation guidelines page provides a starting point to educate new site authors about [SharePoint creation policies](https://docs.microsoft.com/sharepoint/sites-usage-guidelines) for your organization. The guidelines include suggested usage policy topics and questions to prompt consideration of usage policies within your organization. Customize the content in your SharePoint Success Site site creation guidelines page to serve your organization’s governance needs.

![Image of the site creation guidelines page](media/sss-creation-guidelines.png)

## Step 1: Provision the SharePoint Success Site
An Office 365 tenant administrator can start the provisioning process for the SharePoint Success Site. Before getting started, make sure you've met the prerequisites for provisioning.

### Prerequisites
To successfully set up the SharePoint Success Site in your tenant you must install it using the [SharePoint Look book](https://lookbook.microsoft.com/). Meet the prerequisites for both the person provisioning and the tenant before you begin:

<br>

| Tenant admin role | +  | Collection owner of the App Catolog | +  |V4 or higher of M365 learning pathways | = | Ready to provision         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |:-------------:| :-------------:|


The **person** doing the provisioning must meet the following pre-requisites:
- Must be a tenant administrator of the tenant - also known as the Office 365 global administrator role - where the SharePoint Success Site will be provisioned. If you are not sure if you have been assigned the global administrator role, please see our troubleshooting steps.
- The person provisioning the SharePoint Success Site must be a site collection owner of the App Catalog. If the person provisioning the SharePoint Success Site is not a site collection owner of the App Catalog, [complete these instructions to continue](https://docs.microsoft.com/office365/customlearning/addappadmin).
	
The **tenant** must meet the following provisioning pre-requisites:
- A SharePoint App Catalog must be available within your tenant environment. If your organization does not have a SharePoint App catalog, refer to the [SharePoint Online documentation](https://docs.microsoft.com/sharepoint/use-app-catalog) to create one.
- Your tenant must have **version 4.0 or higher** of M365 learning pathways. If you need to [upgrade your version](https://docs.microsoft.com/office365/customlearning/custom_update) or determine what version of M365 learning pathways you have review the documentation. If you need to install M365 learning pathways go to the [M365LP solution page](https://docs.microsoft.com/office365/customlearning/custom_provision) and review documentation for set up and configuration. 

> [!IMPORTANT]
> If you need to create a SharePoint App Catalog, wait at least 30 minutes after creating before provisioning M365 learning pathways and the SharePoint Success Site. 


### Where to get started provisioning the SharePoint Success Site

![Image of the M365 decision tree](./media/sss-decision-tree-2.png)

#### Provision M365 learning pathways for the first time

If you **don’t already have** M365 learning pathways installed in your tenant, follow these instructions:

1. Go to the [Look book M365 learning pathways solution page.](https://lookbook.microsoft.com/details/3df8bd55-b872-4c9d-88e3-6b2f05344239)
2. Select **Add to your tenant**. If you aren't signed into to your tenant, the Provisioning Service will ask for your tenant admin credentials.
3. From the Permissions requested dialog box, select **Consent on behalf of your organization** and then select **Accept.**

![Image of the app catologue consent](./media/app-catolog-consent2.png)

> [!NOTE]
> By selecting **Consent on behalf of your organization** when adding the App Catalog, there is no overall impact on your tenant and these permissions are explicitly used for the purpose of the solution installation. You must accept these permissions to proceed with the installation.

4. Wait about 30 minutes for the App Catalog to finish provisioning before adding the SharePoint Success Site. 
5. Complete the fields on the provisioning information page as appropriate for your installation. At a minimum, enter the email address where you wish to get notifications about the provisioning process and the destination URL for your site to be provisioned to.
6. Select **Provision** when ready to install M 365 learning pathways into your tenant environment. The provisioning process can take up to 15 minutes. You will be notified via email when the site is ready.
7. Next, follow instructions for initializing the CustomConfig List

> [!NOTE]
> Make the destination URL for your site something friendly to your employees such as "/sites/MyTraining" or "/teams/LearnMicrosoft365".


#### Or, update your current version of M365 learning pathways to version 4.0 or higher

If using **version 3.0 or earlier** of M365 learning pathway, update your current version of to version 4.0 or higher using these instructions:

> [!NOTE]
> Version 4.0 of the M365 learning pathways solution is required to provision the SharePoint Success Site.


1. Verify your version of M365 learning pathways.

    Example of where to view version:

    Add image of version confirmation

2. 	If you need to, [update your M365 learning pathways solution](https://docs.microsoft.com/office365/customlearning/custom_update) to version 4.0

3. Once your M365 learning pathways is updated to version 4.0 or higher, proceed to provisioning the SharePoint Success Site.



### Provision the SharePoint Success Site to your tenant from the Admin success center

1. Navigate to [office.com](https://www.office.com/) or your organization’s sign-in location.
2. Sign in with your user name and password.
3. Navigate to the location of the site using the URL supplied by your tenant administrator or select SharePoint from the Office 365 Home page, and then select the M365 learning pathways site.
5. From the M365 learning pathways Home page, select **Get started with the Admin Success Center**.

Note for Holland - Add screen shot when available

> [!NOTE]
> Make the destination URL for your site user friendly for your colleagues, such as “/sites/SharePointSuccess” or “/teams/SharePointSites”.



#### Initialize the CustomConfig list
When SharePoint Success Site provisioning is complete, the tenant admin who provisioned the site receives an email from the SharePoint Provisioning Service that contains a link to the new site. 

1.	Select the link in the in the email and set up the site
2.	Go to <YOUR-SITE-COLLECTION-URL>sites/<YOUR-SITE-NAME>/SitePages/CustomLearningAdmin.aspx. 
<br>
Opening **CustomLearningAdmin.aspx** initializes the **CustomConfig** list item that sets up learning pathways for first use. You should see a page that looks like this:

![Image of the first use page](./media/m365-lp-custom-config.png)

#### Add owners to the M365 learning pathways site
Assign a few site owners to grant administrative privileges to customize the site and training content. This includes the ability to hide and show content and to build custom playlists through the learning pathways web part. 

Do the same instructions below apply to this section?

#### Add owners to the SharePoint Success Site
Assign a few site owners to grant administrative privileges to customize the site content, branding, navigation, web parts, and theme.

1. From the SharePoint **Settings** menu, select **Site permissions**
2. Select **Advanced Permission Settings**.
3. Select **SharePoint Success Site Owners**.
4. Select **New > Add Users to this group**, and then add the people you want to be site owners.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.

#### Site provisioning help

- Reference [troubleshooting](https://docs.microsoft.com/office365/customlearning/feedback) for provisioning help
- See M365 learning pathways [FAQs](https://docs.microsoft.com/office365/customlearning/faq)
- Share your [feedback](https://github.com/pnp/custom-learning-office-365/issues) with us





## Step 2: Customize the SharePoint Success Site 
The SharePoint Success Site is a ready to deploy, up-to-date, and customizable SharePoint communication site that helps your organization maximize the adoption of SharePoint. The SharePoint Success Site helps end users improve the quality and impact of the sites they build for internal audiences, while helping ensure they follow your organization’s site usage guidelines.
The SharePoint Success Site is pre-populated with web parts and content to guide your viewers through the most up-to-date site creation training. However, there are opportunities to customize the experience to better suit your organization’s goals and usage policy. 
<br>

**Before you publish your SharePoint Success Site, customize the following elements:**

- Training content in M365 learning pathways 
- The SharePoint Success Site template and web parts
- Content in the site usage guidelines and success story sections
- Branding details like the site logo and theme
- Adoption and awareness materials

![Image of the SharePoint Success Site landing page](./media/sss-landing.png)


#### How does the SharePoint Success Site work? 

The SharePoint Success Site consists of three parts:
1. **SharePoint communication site** - The site comes pre-populated with content and web parts that can be customized.
2. **Microsoft 365 learning pathways** - M365 learning pathways is a solution that enables you to leverage existing content produced by Microsoft, as well as the ability to create and upload your own training playlists.
3. **Up-to-date SharePoint training content feed** - Content in the SharePoint Success Site is updated as SharePoint evolves and is managed by Microsoft.

#### Summary of site requirements and permissions
Before getting started, ensure that the SharePoint Success Site has been set up by your SharePoint tenant administrator. You need to be a site owner for *both* M365 learning pathways and the SharePoint Success Site in order to have permission to make changes.

If you’re not sure, contact your SharePoint tenant administrator to verify that the SharePoint Success Site been provisioned and ask for the M365 learning pathways and SharePoint Success Site URLs. If you are the tenant administrator and M365 learning pathways has not been provisioned, see the provisioning guidance in step one.

*Who can provision the SharePoint Success Site?*
<br>
- Tenant administrator, also known as Office 365 global administrator
- SharePoint Site Collection Administrator with Owner permissions on the site
<br>

*Who has permissions to customize site template?*
- Site collection administrator
- SharePoint owner or member permissions
<br>

*Who can create custom playlists and hide/show content in M365 learning pathways?*
- Site collection administrator for M365 learning pathways
- SharePoint owner or member permissions for M365 learning pathways
<br>

*Who has permissions to use the SharePoint Success Site as a user?*
- Office 365 user permissions/SharePoint Site Visitor permissions or higher




### Get started with customization
Once you've ensured you have the necessary permissions to customize the site it's time to get started with the customization process.
The SharePoint Success Site is hosted in your Microsoft 365 tenant, so you'll need to sign into Microsoft 365 to navigate to the site. 

#### Sign in
1.	Open your Web browser and navigate to [office.com](https://www.office.com/) or your organization’s sign-in location.
2.	Sign in with your username and password.
3.	Navigate to the location of the site using the URL supplied by your tenant administrator or select SharePoint from the Microsoft 365 Home page, and then select the **SharePoint Success Site**.


### Explore and review the pre-populated training content
1.	Review the Plan, Build, Launch and manage, and Advanced playlist sections to see the full suite of Microsoft curated content available in the SharePoint Success Site.
2.	Select content categories and subcategories, and then navigate through the playlist to get a sense for how the SharePoint Success Site content is organized and displayed.

**Plan your site page**:
![Image of the SharePoint Success Site landing page, Plan your site](./media/sss-content-landing.png)

**Select a topic, and navigate through content using controls at the top of the article**:
![Image of the SharePoint Success Site landing page, Plan your site](./media/sss-content-module.png)

### Customize playlist content and add your own custom playlists

#### Show or hide sections to the playlist content



Select which content to display in your SharePoint Success Site by [hiding and showing](https://docs.microsoft.com/office365/customlearning/custom_hideshowsub) subcategories of content. For example, if you don’t want users to have access to advanced site creation, you can hide that subcategory it won't be visible to users. Decide which content is appropriate for the purpose of your SharePoint Success Site. 

![Image of the M365 learning pathways, SharePoint success site page](./media/m365-lp-sss.png)

#### Add your own custom playlists

With Microsoft 365 learning pathways, you can [create custom playlists](https://docs.microsoft.com/office365/customlearning/custom_createnewplaylist) that are tailored to the unique needs of your organization. For example, create a playlist for team site integration with Microsoft Teams.


### Customize the content and look of your SharePoint Success Site
The following sections of the SharePoint Success Site can be customized to meet your requirements, prior to sharing with end users:

#### SharePoint site template

There are several different ways you can make the SharePoint Success Site template your own. Customize the following elements of your site to fit the need of your organization:

- Update the SharePoint Success Site [branding](https://support.microsoft.com/office/customize-your-sharepoint-site-320b43e5-b047-4fda-8381-f61e8ac7f59b) to align with your organization
- Customize the [Hero web part](https://support.microsoft.com/office/use-the-hero-web-part-d57f449b-19a0-4b0d-8ce3-be5866430645) 
- [Add web parts](https://support.microsoft.com/office/using-web-parts-on-sharepoint-pages-336e8e92-3e2d-4298-ae01-d404bbe751e0) to your site
- Customize the [site navigation](https://support.microsoft.com/office/customize-the-navigation-on-your-sharepoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca)
- Customize the [page layout](https://support.microsoft.com/office/add-sections-and-columns-on-a-sharepoint-modern-page-fc491eb4-f733-4825-8fe2-e1ed80bd0899)
- Add [new pages or edit pages](https://support.microsoft.com/office/create-and-use-modern-pages-on-a-sharepoint-site-b3d46deb-27a6-4b1e-87b8-df851e503dec)

#### Customize specific web parts

- **Yammer web part** - Use a Yammer web part to connect new SharePoint site owners with extra support from SharePoint site owners and admins. Connect your Yammer account to the [ Yammer web part](https://support.microsoft.com/office/use-a-yammer-web-part-in-sharepoint-online-a53cfa0c-3d09-42c8-a286-1038a81c59da#conversations).
- **People web part** - Edit the [People web part](https://support.microsoft.com/office/show-people-profiles-on-your-page-with-the-people-web-part-7e52c5f6-2d72-48fa-a9d3-d2750765fa05) to display contact information so new site owner can reach out for help.




### Customize the Success stories page
The success stories section is a gallery for organizations to showcase internal SharePoint Online success stories that inspire others in the organization. 

Add image of success stories

If available, add SharePoint success stories to your portal. If there are no ready-to-publish success stories, consider working with internal partners to create SharePoint successes by building high priority sites that align with business outcomes. Highlighting these “early wins” will help inspire others in the organization on the possibilities for using SharePoint themselves to achieve important business outcomes. Learn more about how to [create a form](https://support.microsoft.com/office/create-a-form-with-microsoft-forms-4ffb64cc-7d5d-402f-b82e-b1d49418fd9d) using Microsoft Forms.


Note to administrators: Learn how to use the Microsoft Forms web part. See the example site success story below to develop questions for your form. Customize the content in this section to meet the needs of your organization.​​​​​​​ Delete this note before sharing with users. ​​​​​​​

Create your form
Add the Forms web part
Check form submissions
Post success stories on this page


### Customize the Site creation guidelines page
To ensure the proper use of SharePoint in your organization it is important to communicate your site usage guidelines to new and existing site owners. This should include guidelines for how people should create sites in your tenant, design standards, and how people should share information using SharePoint and Office 365. 

The Sites Usage Guidelines Checklist is not intended to be a final policy document. Once you have created your own unique usage guidelines, remove the webpart from the Site usage guidelines page and replace it with your organization’s usage guidelines. See how to [create and use modern pages](https://support.microsoft.com/office/create-and-use-modern-pages-on-a-sharepoint-site-b3d46deb-27a6-4b1e-87b8-df851e503dec?ui=en-us&rs=en-us&ad=us) on a SharePoint site. 
Create site usage guidelines that are appropriate for your organization by reviewing our [site usage guidelines checklist](https://docs.microsoft.com/sharepoint/sites-usage-guidelines) that will help you create guidelines that:

- Inspire discussion and consideration amongst your stakeholders on important site usage policies
- Provide links to resources that can help you better understand the options related to key policy decisions
- Provide sample text to get you started in creating your own policies

The template site usage guideline checklist is not intended to be a final policy document. Once you have created your own unique usage guidelines, remove the Text web part from the Site usage guidelines page and replace it with your organization’s usage guidelines. 

Note to administrators: Share your organization's site usage policies in this section. Include guidance for new site owners to follow when setting up and managing sites in your organization. Customize the content in this section to meet the needs of your organization. Delete this note before sharing with users. ​​​​​​​

​​​​​​​Here are some things to keep in mind as you plan, build, and manage your SharePoint site :

How to get a new SharePoint site
Guidelines for using site templates
Site design, branding, and customization
Rules for sharing and permissions
Capacity guidelines
Site lifecycle policy




#### Intranet team
If your organization has an Intranet team that will be supporting site owners, consider profiling the Intranet team members on the SharePoint Success Site homepage using the people web part. 
The **Plan your site** section in the SharePoint Success Site has a people web part you can use to add your own Intranet team. If you will not have a dedicated team supporting site owners, remove the current people web part.
Learn more about the [People web part](https://support.microsoft.com/office/show-people-profiles-on-your-page-with-the-people-web-part-7e52c5f6-2d72-48fa-a9d3-d2750765fa05?ui=en-us&rs=en-us&ad=us). 


## Step 3: Share the SharePoint Success Site with end-users
Partner with others in your organization to ensure the SharePoint Success Site is widely known and adopted. Key success factors to managing the SharePoint Success Site:

- Celebrate the launch of your SharePoint Success Site
- Create and post news announcing the new resource
- Ensure users have an outlet for questions and feedback
- Plan to review the SharePoint Success site as needed to ensure content and site usage policies are still relevant 
- Build culture and community by integrating a Yammer web part
- Integrate and customize your organization’s high-value training content

#### Adoption and awareness materials
To help build, grow, and sustain your SharePoint adoption efforts, its recommended to form a SharePoint user group community on Yammer.  Your SharePoint champions and power users can answer SharePoint related questions posted in the Yammer group and encourage site owners to share their successes and best practices. See the champions program guide for more information on how to build a successful champions program. To increase visibility and engagement within your portal champions community, integrate the Yammer group hosting your community into the SharePoint Success Site using the [Yammer conversations web part](https://support.microsoft.com/office/use-a-yammer-web-part-in-sharepoint-online-a53cfa0c-3d09-42c8-a286-1038a81c59da).

Adoption and awareness materials - I would split this out into two numbered point: 1. SharePoint user group community show them a screen grab of what it could look like on their site, 2) Awareness campaign - use sample SharePoint Success Site launch announcement to drive awareness. We will need to link to sample copy they can edit. <Note: will send mail to get most up to date copy">


### Measurement

### Feedback and support
	
### Frequently asked questions























