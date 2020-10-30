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
description: "Provision the SharePoint Success Site"
---

# Provision the SharePoint Success Site 

Start the SharePoint Success Site provisioning process by understanding the prerequisites. Then, you can provision the site from the look book or Microsoft 365 learning pathways administration page. 
Global administrator (formerly called the Tenant admin) credentials are required to start the provisioning process for the SharePoint Success Site. 

Before getting started, make sure you've met the requirements for provisioning. 


## Meet the requirements

Before provisioning the SharePoint Success Site, meet the requirements for both the **person** provisioning and the **tenant.** Your tenant's configuration will determine what path you need to take to install the SharePoint Success Site. Start by reviewing the SharePoint Success Site requirements below to prepare your tenant. 

| Tenant admin role requirements | +  | Tenant requirements |  = | Ready to provision         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |


#### Tenant admin requirements

The **person** doing the provisioning must be a Global admin (formerly called the Tenant admin) where the SharePoint Success Site will be provisioned *and must also be* an Administrator of the tenant’s App Catalog.

<br>

| Global admin role | +  | Admin of the App Catalog | = | Tenant admin requirements met         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |

**Are you a Global administrator?**
- **Yes** -  Next, confirm your tenant has already enabled the App Catalog.
- **No** -  Partner with your M365 Global admin to get the site provisioned. [Learn more about administrative roles in SharePoint](https://docs.microsoft.com/microsoft-365/admin/add-users/about-admin-roles?WT.mc_id=365AdminCSH&view=o365-worldwide).
<br>
<br>
If you are unsure, you can confirm your role by logging into office.com, you’ll see an Admin center app icon next to your M365 apps if you have SharePoint administrator credentials.

**Are you an Administrator of the App Catalog?**
- **Yes** - Next, confirm your tenant has M365 learning Pathways provisioned.
- **No** - Next, ask your Global admin to add you as an [App Catalog Administrator](https://docs.microsoft.com/office365/customlearning/addappadmin).

	
#### Tenant requirements

The **tenant** where the site will be provisioned must have the [App Catalog](https://docs.microsoft.com/sharepoint/use-app-catalog) installed *and* have the latest version of [M365 learning pathways](https://docs.microsoft.com/office365/customlearning/#:~:text=Microsoft%20365%20learning%20pathways%20is%20a%20customizable%2C%20on-demand,adoption%20of%20Microsoft%20365%20services%20in%20your%20organization.). installed. Your tenant must have **version 4.0 or higher** of M365 learning pathways.

<br>

| App Catalog installed | +  |M365 learning pathways 4.0 or higher installed | = | Tenant requirements met         |
| :----------------: | :----------------: |:-------------:|:----------------: | :----------------: |

<br>

Use this decision tree to determine your tenant’s path to meeting the **tenant** requirements.

![Image of the M365 decision tree](media/sss-decision-tree-2.png)

Ready to get started provisioning? Review the [provisioning instructions](https://docs.microsoft.com/sharepoint/provision-sss#provision-the-sharepoint-success-site-1). 


<br>

**Does your tenant have the App Catalog installed?**
- **Yes** - Next, confirm you are an administrator of the App Catalog.
- **No** - Next, [enable the App Catalog](https://www.bing.com/videos/search?q=where+to+find+the+app+catogue+in+sharepoint&docid=608008189208497248&mid=99CF7FB554B328AC189899CF7FB554B328AC1898&view=detail&FORM=VIRE) (this will take about 30 minutes).
<br>
<br>

If you are unsure, navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see the **App Catalog**

  ![Image active sites in the SharePoint admin center](media/sss-active-sites.png)


> [!IMPORTANT]
> If you need to create a App Catalog, wait at least 30 minutes after creating before provisioning M365 learning pathways and the SharePoint Success Site. 
 
**Does your tenant have M365 learning pathways provisioned?**
- **Yes** - Next, confirm you are using version 4.0 or higher.
- **No** - [Provision M365 learning pathways](https://docs.microsoft.com/office365/customlearning/) for the first time.
<br>

If you are unsure, navigate to the SharePoint admin center, then select **Sites > Active sites** and you will see **Microsoft 365 learning pathways**.
 
**Is your tenant's version of learning pathways version 4.0 or higher?**
- **Yes** - You are ready to [provision the SharePoint Success Site](https://docs.microsoft.com/sharepoint/provision-sss#provision-the-sharepoint-success-site-1).
- **No** - Update to version 4.0 or higher and then provision the SharePoint Success Site from the M365 learning pathways administration page.

If you are unsure, navigate to your tenant's **M365 Learning Pathways administration page** and select the the ellipses **(…)**

  ![Image learning pathways admin page](media/sss-lp-version.png)


Then, select **About web part** to confirm the current version.

  ![Image learning pathways admin page version](media/sss-lp-elipses.png)

<br>

#### If you need to, update M365 learning pathways from version 3.0 to version 4.0 or higher

> [!IMPORTANT]
> The person updating M365 learning pathways must be an Administrator of the tenant’s App Catalog. If the person provisioning M365 learning pathways isn't an Administrator of the App Catalog, [add an Administrator to the App Catalog](https://docs.microsoft.com/office365/customlearning/addappadmin) and continue.

In this step, you upload the M365 learning pathways 4.0 web part to the SharePoint App Catalog, and then navigate to the M365 learning pathways Administration page to start the update process.

**Upload the web part package:**

1. Go to the [GitHub custom learning repository](https://docs.microsoft.com/office365/customlearning/manualcustomlearninginstall), select customlearning.sppkg and then download it to a local drive on your PC.
2. If you’re not already signed in, sign into your tenant with a Global admin credentials.
3. Select **Admin > Show All > SharePoint > More Features**.
4. Under **Apps**, select **Open**.
5. Select **App Catalog > Distribute Apps for SharePoint**.
6. Select **Upload > Choose Files**.
7. Select the customlearning.sppkg file you downloaded, then select **OK > Deploy**.
8. From the Learning Pathways site, select Learning pathways administration from the Home menu.
9. You’ll see a prompt asking if you want to update, then select **Start**.
10. When the update is complete, select **Close**.

<br>


## Provision the SharePoint Success Site

Once you’ve confirmed the following, you are ready to provision:

- You are using Global admin (formerly called the Tenant admin) credentials.
- Your tenant has the App Catalog enabled.
- You are an Administrator of the App Catalog.
- Your tenant has version 4.0 or higher of M365 learning pathways provisioned.

### Provision the SharePoint Success Site to your tenant from the Learning pathways administrative page

1.  Navigate to [office.com](https://www.office.com/) or your organization’s sign-in location.
2.  Sign in with your username and password.
3.  Navigate to the location of the site using the URL supplied by your SharePoint administrator or select SharePoint from the Microsoft 365 home page, and then select the **M365 learning pathways** site.
4.  From the learning pathways Home menu, select **Learning Pathways Administration**.

    ![Image of the M365 learning pathways admin page](media/sss-sss-admin.png)

5.  Select the ellipses **(…)** and then select **Add Content Pack**.

    ![Image of the content pack in the M365 learning pathways admin page](media/sss-content-pack.png)

6.  Select SharePoint Success Site to open the SharePoint Success Site provisioning page.
7.  Select **Add to your tenant**.
8.  Fill out the email address and URL details and then select **Provision**.
9.  Select **Complete**.

10. When you see Provisioning completed, select the **CustomLearningAdministration** tab as shown in the following image:

    ![Image of the M365 learning pathways solution tab](media/sss-m365lp-tab.png)

11. Select **Complete** as shown in the following image:

![Image of the M365 learning pathways solution complete button](media/sss-m365lp-confirm2.png)

> [!IMPORTANT]
> Make sure to select **Complete** to complete the provisioning process.

12. To confirm the SharePoint Success Site has been successfully provisioned, go to the SharePoint site you provisioned, select **Get Started > Plan your site.** You should see the web part on the page as shown in the following image: 

![Image of the SharePoint Success Site landing page, Plan your site](media/sss-content-landing.png)


## Add Site owners 
Assign a few Site owners to grant administrative privileges to customize the site and training content. In order to hide, show, or enable playlists, users will need Site owner or Site member permissions to the M365 learning pathways site. In order to edit the look, navigation, and site content, users will need Site owner or Site member permissions to the SharePoint Success Site. 

**Add Site owners or members to both sites**

1. From the site select **Settings**, then select **Site permissions**.
2. Select **Advanced Permission Settings**.
3. Select **Site owners** or **Site members**
4. Select **New > Add users to this group**, and then add the people you want to be Site owners or Site members.
5. Include a link to **Explore the site** in the sharing message, and then select **Share**.


<br>

#### Next steps - customize the SharePoint Success Site

Share the URLs for the M365 learning pathways administration site and the SharePoint Success site with the Site owners and members who will be responsible for customizing the site. Then, [customize](https://docs.microsoft.com/sharepoint/customize-sss) M365 learning pathways playlist content and the look and feel of your SharePoint Success Site to meet the needs of your organization.

<br>

### Site provisioning help

- Reference [troubleshooting](https://docs.microsoft.com/office365/customlearning/feedback) for provisioning help
- See M365 learning pathways [FAQs](https://docs.microsoft.com/office365/customlearning/faq)
- Share your [feedback](https://github.com/pnp/custom-learning-office-365/issues) with us



#### Frequently asked questions

**Question: Can I provision from the look book?**
<br>
Answer: Yes, follow the guidance on how to provision from the [look book](https://docs.microsoft.com/sharepoint/provision-sss-lookbook).
<br>

**Question: Who has permission to provision the SharePoint Success Site?**
<br>
Answer: The Global admin (formerly called the Tenant admin) are required.
<br>

**Question: Who has permission to customize the site template?**
<br>
Answer: The Global admin (formerly called the Tenant admin) or Site owner permissions.
<br>

**Question: Who can create custom playlists and hide or show content in M365 learning pathways?**
<br>
Answer: The Site collection administrator and Site owner permissions of M365 learning pathways.
<br>

**Question: Who has permissions to use the SharePoint Success Site as a user?**
<br>
Answer: Microsoft 365 user permissions or SharePoint Site visitor permissions or higher.

