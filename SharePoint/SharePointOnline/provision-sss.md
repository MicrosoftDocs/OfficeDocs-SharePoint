---
title: Provision the SharePoint Success Site 
ms.reviewer: 
ms.author: hokavian
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
ROBOTS: NOINDEX, NOFOLLOW
description: "Provision the SharePoint Success Site"
---

# Provision the SharePoint Success Site 

Start the SharePoint Success Site provisioning process by understanding the prerequisites. Then, you can provision the site from the look book or Microsoft 365 learning pathways administration page. 
Microsoft 365 tenant administrator credentials (or higher) are required to start the provisioning process for the SharePoint Success Site. Before getting started, make sure you've met the prerequisites for provisioning. 


## Meet the prerequisites
Before provisioning the SharePoint Success Site, meet the prerequisites for both the **person** provisioning and the **tenant**:

<br>

| Tenant admin role | +  | Collection owner of the App Catalog | +  |V4 or higher of M365 learning pathways | = | Ready to provision         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |:-------------:| :-------------:|


The **person** doing the provisioning must meet the following pre-requisites:
- Must be a tenant administrator of the tenant - also known as the Microsoft 365 global administrator role - where the SharePoint Success Site will be provisioned.
- Must be an administrator of the tenant’s App catalog
	
The **tenant** must meet the following provisioning pre-requisites:
- A SharePoint App Catalog must be available within your tenant environment
- Your tenant must have **version 4.0 or higher** of M365 learning pathways

> [!IMPORTANT]
> If you need to create a SharePoint App Catalog, wait at least 30 minutes after creating before provisioning M365 learning pathways and the SharePoint Success Site. 


### Where to get started provisioning 

Your tenant's configuration will determine what path you need to take to install the SharePoint Success Site. Start by reviewing the SharePoint Success Site prerequisites check list below to prepare your tenant. Determine your tenant’s starting point and follow direction in the checklist. 

![Image of the M365 decision tree](media/sss-decision-tree-2.png)

#### Prerequisite checklist:

**Are you a SharePoint tenant administrator?**
- Yes - Next, confirm your tenant has already downloaded the App Catalog
- No – Work with your M365 global administrator or SharePoint tenant administrator to add you as a [SharePoint tenant administrator](https://docs.microsoft.com/sharepoint/sharepoint-admin-role)
- Unsure – When you log into office.com, you’ll see an Admin center icon if you have SharePoint tenant administrator credentials 
 
**Does your tenant have the App Catalog installed?**
- Yes - Next, confirm you are an administrator of the App Catalog
- No - Next, [install the App Catolg](https://www.bing.com/videos/search?q=where+to+find+the+app+catogue+in+sharepoint&docid=608008189208497248&mid=99CF7FB554B328AC189899CF7FB554B328AC1898&view=detail&FORM=VIRE) (this will take about 30 minutes)
- Unsure - Navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see the **App Catalog**:

![Image active sites in the SharePoint admin center](media/sss-active-sites.png)
 
**Are you an administrator of the App Catalog?**
- Yes - Next, confirm your tenant has M365 learning Pathways provisioned
- No - Next, ask your Global tenant administrator to add you as an [App Catalog administrator](https://docs.microsoft.com/office365/customlearning/addappadmin)
 
**Does your tenant have M365 learning pathways provisioned?**
- Yes - Next, confirm you are using version 4.0 or higher
- No - [Provision M365 learning pathways](https://docs.microsoft.com/office365/customlearning/) for the first time
- Unsure - Navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see the **Microsoft 365 learning pathways**
 
**Is your tenant's version of learning pathways version 4.0 or higher?**
- Yes - You are ready to provision the SharePoint Success Site from the look book
- No - Update to version 4.0 and provision the SharePoint Success Site from the M365 learning pathways administration page
- Unsure - Navigate to your tenant's M365 Learning Pathways administration page

![Image learning pathways admin page](media/sss-lp-version.png)

Then select the three dots in the tool bar, then select **About web part**

![Image learning pathways admin page settings bar](media/sss-lp-elipses.png)

### Update M365 learning pathways from version 3.0 to version 4.0

> [!IMPORTANT] 
> The person updating learning pathways must be an administrator of the tenant’s App Catalog. If the person provisioning learning pathways isn't a site collection owner of the App Catalog, [complete these instructions](https://docs.microsoft.com/office365/customlearning/addappadmin) and continue

In this step, you upload the learning pathways 4.0 web part to the SharePoint App Catalog, and then navigate to the learning pathways Administration page to start the update process.

#### Upload the web part package
1.	Go to the [GitHub custom learning repository](https://docs.microsoft.com/office365/customlearning/manualcustomlearninginstall), select customlearning.sppkg and then download it to a local drive on your PC
2.	If you’re not already signed in, sign into your tenant with a Tenant Admin or Site Collection Admin account
3.	Select **Admin > Show All > SharePoint > More Features**
4.	Under Apps, select **Open**
5.	Select **App Catalog > Distribute Apps for SharePoint**
6.	Select **Upload > Choose Files**
7.	Select the customlearning.sppkg file you downloaded, then select **OK > Deploy**
8.	From the Learning Pathways site, select **Learning pathways administration** from the Home menu.
9.	You’ll see a prompt asking if you want to update, select **start**
10.	When the update is complete, select **Close**


## Provision the SharePoint Success Site

Once you’ve confirmed the following, you are ready to provision:

•	You are using *at minimum* SharePoint tenant administrator credentials
•	Your tenant has the App Catalog installed
•	You are an administrator of the App Catalog
•	Your tenant has version 4.0 of the M365 learning pathways provisioned


### Provision the SharePoint Success Site to your tenant from the look book
If you already have Learning Pathways 4.0 or greater provisioned on your tenant, you can provision Learning Pathways from the SharePoint Look book site. Make sure you have met the requirements as covered earlier in this documentation.

1.	Go to the [look book](https://provisioning-test.sharepointpnp.com/details/0b860749-56a0-4c4c-992c-536d56d9accf) and select **Add to your tenant**

![Image of the SharePoint Success Site look book page](media/sss-lookbook-add.png)

2.	Fill out the email and URL address sections and select **Provision**

![Image of the SharePoint Success Site look book page details](media/sss-lookbook-details.png)

3.	Select **Confirm**
4.	When provisioning is complete, you’ll see the following message:

![Image of the provisioning confirmation message](media/sss-sss-complete.png)

5.	Next, navigate to your tenant's Learning Pathways site
6.	Select **Home > Learning Pathways Administration**

![Image of the M365 learning pathways admin page](media/sss-sss-admin.png)

7.	Select the … (ellipse), then select **Add to Content Pack**
8.	Select **SharePoint Success Site**

![Image of the content pack in the M365 learning pathways admin page](media/sss-content-pack.png)

9.	You will see the SharePoint look book site appear in a new tab. You can close this tab and select the **CustomLearning Administration tab**

![Image of the M365 learning pathways solution tab](media/sss-m365lp-tab.png)

10.	Select **Complete** as shown in the following image:

![Image of the M365 learning pathways solution complete button](media/sss-m365lp-confirm2.png)

> [!IMPORTANT]
> Make sure to select **Complete** to complete the provisioning process.

11.	To confirm the SharePoint Success Site has been successfully provisioned, navigate to the site and select **Get Started > Plan your site**. You should see the web part on the page as shown in the following image:

![Image of the SharePoint Success Site landing page](media/sss-landing.png)

12. Next, follow the steps below to add site owners to the M365 learning pathways administration page and the SharePoint Success Site to grant access to others for site and content customizations. 



### Provision the SharePoint Success Site to your tenant from the Learning pathways administrative page

1.	Navigate to [office.com](https://www.office.com/) or your organization’s sign-in location.
2.	Sign in with your username and password.
3.	Navigate to the location of the site using the URL supplied by your tenant administrator or select SharePoint from the Microsoft 365 home page, and then select the **M365 learning pathways** site.
4.	From the learning pathways Home menu, select **Learning Pathways Administration**.

![Image of the M365 learning pathways admin page](media/sss-sss-admin.png)

5.	Select the … (ellipses) and then select **Add Content Pack**.

![Image of the content pack in the M365 learning pathways admin page](media/sss-content-packn.png)

6.	Select SharePoint Success Site to open the SharePoint Success Site provisioning page.
7.	Select **Add to your tenant**.
8.	Fill out the details and then select **Provision**.
9.	Select **Complete**.

> [!IMPORTANT]
> Make sure to select **Complete** to complete the provisioning process.

10.	When you see Provisioning completed, select the **CustomLearningAdministration** tab as shown in the following image:

![Image of the M365 learning pathways solution tab](media/sss-m365lp-tab.png)

11.	Select **Complete** as shown in the following image:

![Image of the M365 learning pathways solution complete button](media/sss-m365lp-confirm2.png)

12.	To confirm the SharePoint Success Site has been successfully provisioned, navigate to the site and select Get Started > Plan your site. You should see the web part on the page as shown in the following image:

![Image of the SharePoint Success Site landing page](media/sss-landing.png)

13. Next, follow the steps below to add site owners to the M365 learning pathways administration page and the SharePoint Success Site to grant access to others for site and content customizations. 


#### Add owners to the M365 learning pathways site
Assign a few site owners to grant administrative privileges to customize the site and training content. This includes the ability to hide and show content and to build custom playlists through the learning pathways web part. 

1. From the M365 learning pathways site menu select **Settings**, then select **Site permissions**
2. Select **Advanced Permission Settings**.
3. Select **SharePoint Success Site Owners**.
4. Select **New > Add Users to this group**, and then add the people you want to be site owners.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.

#### Add owners to the SharePoint Success Site
Assign a few site owners to grant administrative privileges to customize the site content, branding, navigation, web parts, and theme.

1. From the SharePoint Success Site's menu select **Settings**, then select **Site permissions**
2. Select **Advanced Permission Settings**.
3. Select **SharePoint Success Site Owners**.
4. Select **New > Add Users to this group**, and then add the people you want to be site owners.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.


## Site provisioning help

- Reference [troubleshooting](https://docs.microsoft.com/office365/customlearning/feedback) for provisioning help
- See M365 learning pathways [FAQs](https://docs.microsoft.com/office365/customlearning/faq)
- Share your [feedback](https://github.com/pnp/custom-learning-office-365/issues) with us

	
### Frequently asked questions

**Question: Who can provision the SharePoint Success Site?**
<br>
Answer:
- Tenant administrator, also known as Office 365 global administrator
- SharePoint Site Collection Administrator with Owner permissions on the site
<br>

**Question: Who has permissions to customize site template?**
<br>
Answer:
- Site collection administrator
- SharePoint owner or member permissions
<br>

**Question: Who can create custom playlists and hide/show content in M365 learning pathways?**
<br>
Answer:
- Site collection administrator for M365 learning pathways
- SharePoint owner or member permissions for M365 learning pathways
<br>

**Question: Who has permissions to use the SharePoint Success Site as a user?**
<br>
Answer:
- Office 365 user permissions/SharePoint Site visitor permissions or higher























