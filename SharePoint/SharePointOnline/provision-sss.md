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

Before provisioning the SharePoint Success Site, meet the prerequisites for both the **person** provisioning and the **tenant.** Your tenant's configuration will determine what path you need to take to install the SharePoint Success Site. Start by reviewing the SharePoint Success Site prerequisites below to prepare your tenant. Use this decision tree to determine your tenant’s path to meeting prerequisites:

![Image of the M365 decision tree](media/sss-decision-tree-2.png)



<br>

#### The person doing the provisioning must meet the following pre-requisites:

The **person** doing the provisioning must be a Tenant administrator of the tenant (also known as the Microsoft 365 Global administrator role) where the SharePoint Success Site will be provisioned *and must also be* an Administrator of the tenant’s App Catalog.


| Tenant admin role | +  | Admin of the App Catalog | +  |V4 or higher of M365 learning pathways | = | Ready to provision         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |:-------------:| :-------------:|

**Are you a SharePoint Tenant administrator?**
- Yes - Next, confirm your tenant has already downloaded the App Catalog
- No – Work with your M365 Global administrator or SharePoint Tenant administrator to add you as a [SharePoint Tenant administrator](https://docs.microsoft.com/sharepoint/sharepoint-admin-role)
- Unsure – When you log into office.com, you’ll see an Admin center app icon next to your M365 apps if you have SharePoint tenant administrator credentials 

**Are you an Administrator of the App Catalog?**
- Yes - Next, confirm your tenant has M365 learning Pathways provisioned
- No - Next, ask your Global tenant administrator to add you as an [App Catalog administrator](https://docs.microsoft.com/office365/customlearning/addappadmin)

	
#### The tenant must meet the following provisioning pre-requisites:

The **tenant** where the site will be provisioned must have the [SharePoint App Catalog](https://docs.microsoft.com/sharepoint/use-app-catalog) installed *and* have the latest version of [M365 learning pathways](https://docs.microsoft.com/office365/customlearning/#:~:text=Microsoft%20365%20learning%20pathways%20is%20a%20customizable%2C%20on-demand,adoption%20of%20Microsoft%20365%20services%20in%20your%20organization.) installed. Your tenant must have **version 4.0 or higher** of M365 learning pathways.


**Does your tenant have the App Catalog installed?**
- Yes - Next, confirm you are an administrator of the App Catalog
- No - Next, [install the App Catolg](https://www.bing.com/videos/search?q=where+to+find+the+app+catogue+in+sharepoint&docid=608008189208497248&mid=99CF7FB554B328AC189899CF7FB554B328AC1898&view=detail&FORM=VIRE) (this will take about 30 minutes)
- Unsure - Navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see the **App Catalog**:

![Image active sites in the SharePoint admin center](media/sss-active-sites.png)


> [!IMPORTANT]
> If you need to create a SharePoint App Catalog, wait at least 30 minutes after creating before provisioning M365 learning pathways and the SharePoint Success Site. 
 
**Does your tenant have M365 learning pathways provisioned?**
- Yes - Next, confirm you are using version 4.0 or higher
- No - [Provision M365 learning pathways](https://docs.microsoft.com/office365/customlearning/) for the first time
- Unsure - Navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see **Microsoft 365 learning pathways**
 
**Is your tenant's version of learning pathways version 4.0 or higher?**
- Yes - You are ready to provision the SharePoint Success Site from the look book
- No - Update to version 4.0 and provision the SharePoint Success Site from the M365 learning pathways administration page
- Unsure - Navigate to your tenant's **M365 Learning Pathways administration page**:

![Image learning pathways admin page](media/sss-lp-version.png)

Then select the ellipsies **(...)** in the tool bar, then select **About web part**

![Image learning pathways admin page settings bar](media/sss-lp-elipses.png)

#### If you need to, update M365 learning pathways from version 3.0 to version 4.0

> [!IMPORTANT] 
> The person updating learning pathways must be an administrator of the tenant’s App Catalog. If the person provisioning learning pathways isn't a site collection owner of the App Catalog, [complete these instructions](https://docs.microsoft.com/office365/customlearning/addappadmin) and continue

In this step, you upload the learning pathways 4.0 web part to the SharePoint App Catalog, and then navigate to the learning pathways Administration page to start the update process.

**Upload the web part package**
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

- You are using *at minimum* SharePoint tenant administrator credentials
- Your tenant has the App Catalog installed
- You are an administrator of the App Catalog
- Your tenant has version 4.0 of the M365 learning pathways provisioned


#### Provision the SharePoint Success Site to your tenant from the Learning pathways administrative page

1.	Navigate to [office.com](https://www.office.com/) or your organization’s sign-in location.
2.	Sign in with your username and password.
3.	Navigate to the location of the site using the URL supplied by your tenant administrator or select SharePoint from the Microsoft 365 home page, and then select the **M365 learning pathways** site.
4.	From the learning pathways Home menu, select **Learning Pathways Administration**.

![Image of the M365 learning pathways admin page](media/sss-sss-admin.png)

5.	Select the ellipses **( … )** and then select **Add Content Pack**.

![Image of the content pack in the M365 learning pathways admin page](media/sss-content-pack.png)

6.	Select SharePoint Success Site to open the SharePoint Success Site provisioning page.
7.	Select **Add to your tenant**.
8.	Fill out the details and then select **Provision**.
9.	Select **Complete**.

10.	When you see Provisioning completed, select the **CustomLearningAdministration** tab as shown in the following image:

![Image of the M365 learning pathways solution tab](media/sss-m365lp-tab.png)

11.	Select **Complete** as shown in the following image:

![Image of the M365 learning pathways solution complete button](media/sss-m365lp-confirm2.png)

> [!IMPORTANT]
> Make sure to select **Complete** to complete the provisioning process.

12.	To confirm the SharePoint Success Site has been successfully provisioned, navigate to the site and select **Get Started > Plan your site**. You should see the web part on the page as shown in the following image:

![Image of the SharePoint Success Site landing page](media/sss-landing.png)

13. Next, follow the steps below to add site owners to the M365 learning pathways administration page *and* the SharePoint Success Site to grant access to others for site and content customizations. 


## Add Site owners to both sites

In order for others to customize M365 learning pathways playlists and SharePoint Success Site content, they will need Site owner permissions for *both sites*. 

#### Add Site owners to the M365 learning pathways site
Assign a few Site owners to grant administrative privileges to customize the site and training content. This includes the ability to hide and show content and to build custom playlists through the learning pathways web part. 

1. From the M365 learning pathways site menu select **Settings**, then select **Site permissions**
2. Select **Advanced Permission Settings**.
3. Select **SharePoint Success Site owners**.
4. Select **New > Add users to this group**, and then add the people you want to be Site owners.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.

#### Then, add Site owners to the SharePoint Success Site
Assign a few Site owners to grant administrative privileges to customize the site content, branding, navigation, web parts, and theme.

1. From the SharePoint Success Site's menu select **Settings**, then select **Site permissions**
2. Select **Advanced Permission Settings**.
3. Select **SharePoint Success Site owners**.
4. Select **New > Add Users to this group**, and then add the people you want to be Site owners.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.


### Site provisioning help

- Reference [troubleshooting](https://docs.microsoft.com/office365/customlearning/feedback) for provisioning help
- See M365 learning pathways [FAQs](https://docs.microsoft.com/office365/customlearning/faq)
- Share your [feedback](https://github.com/pnp/custom-learning-office-365/issues) with us


<br>

#### Next steps - customize the SharePoint Success Site

Share the URLs for the M365 learning pathways administration site and the SharePoint Success site with Site owners. Then, [customize](https://docs.microsoft.com/sharepoint/customize-sss#share-the-site-with-end-users) playlist content and the look and feel of your SharePoint Success Site to meet the needs of your organization.

<br>

#### Frequently asked questions

**Question: Can I provision the site from the look book?**
<br>
Answer:
Yes, follow guidance on how to [provision the SharePoint Success Site from the look book](https://docs.microsoft.com/sharepoint/provision-sss-lookbook)
<br>

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























