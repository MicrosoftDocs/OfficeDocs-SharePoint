---
title: Provision the SharePoint Success Site from the look book
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
description: "Provision the SharePoint Success Site from the look book."
---

# Provision the SharePoint Success Site from the look book

You can provision the SharePoint Success Site after you confirm that you *and* your tenant meet the following [prerequisites](https://docs.microsoft.com/sharepoint/provision-sss#meet-the-prerequisites):

- You're using global admin credentials.
- Your tenant has the App Catalog installed.
- You're an administrator of the App Catalog.
- Your tenant is provisioned with Microsoft 365 learning pathways version 4.0 or later.


## Start provisioning from the look book
If your tenant is already provisioned with Microsoft 365 learning pathways version 4.0 *or later*, you can provision the SharePoint Success Site from the look book. 

If you aren't sure what version of Microsoft 365 learning pathways is installed on your tenant, review the [prerequisites](https://docs.microsoft.com/sharepoint/provision-sss#meet-the-prerequisites). Then provision the SharePoint Success Site. 

1. Go to the [look book](https://lookbook.microsoft.com/details/0b860749-56a0-4c4c-992c-536d56d9accf), and then select **Add to your tenant**.

   ![Image of the SharePoint Success Site look book page. The "Add to your tenant" button is highlighted.](media/sss-lookbook-add.png)

2. Fill out the email and URL address sections, and then select **Provision**.

   ![Image of the SharePoint Success Site look book page details.](media/sss-lookbook-details.png)

3.	Select **Confirm**. When provisioning is complete, you see the following message:

    ![Image of the provisioning confirmation message.](media/sss-sss-complete.png)

5.	Go to your tenant's learning pathways site.

6.	Select **Home** > **Learning pathways administration**.

    ![Image of the Microsoft 365 learning pathways admin page. The "Learning pathways administration" menu item is highlighted.](media/sss-sss-admin.png)

7.	Select the **More actions** (…) button, and then select **Add to Content Pack**.

8.	Select **SharePoint Success Site**.

    ![Image of the content pack in the Microsoft 365 learning pathways admin page. The "SharePoint Success Site" selection is highlighted.](media/sss-content-pack.png)

9.	Go back to the Microsoft 365 learning pathways administration page.

10.	Select **Complete**, as the following image shows:

    ![Image of the Microsoft 365 learning pathways solution Complete button.](media/sss-m365lp-confirm2.png)

    > [!IMPORTANT]
    > Make sure to select **Complete** to finish the provisioning process.

11.	To confirm that the SharePoint Success Site is successfully provisioned, go to the site, and then select **Get Started** > **Plan your site**. You should see the web part on the page, as the following image shows:


    ![Image of the SharePoint Success Site landing page, named Plan your site.](media/sss-content-landing.png)


In the next section, you'll add site owners to the Microsoft 365 learning pathways administration page and the SharePoint Success Site. This setting grants privileges to [customize the site and content](https://docs.microsoft.com/sharepoint/customize-sss). 


## Add site owners 
Assign a few site owners to grant administrative privileges to customize the site and training content. To hide, show, or enable playlists, users need site-owner permissions or site-member permissions to the Microsoft 365 learning pathways site. To edit the look, navigation, and site content, users need site-owner permissions or site-member permissions to the SharePoint Success Site. 

To add owners or members to both sites:

1. On the site, select **Settings** > **Site permissions**.
2. Select **Advanced Permission Settings**.
3. Select **Site owners** or **Site members**.
4. Select **New** > **Add users to this group**. Then add the people who should be site owners or site members.
5. In the sharing message, include a link to **Explore the site**. Then select **Share**.


## Site provisioning help

- For provisioning help, see [troubleshooting](https://docs.microsoft.com/office365/customlearning/feedback). 
- See Microsoft 365 learning pathways [FAQs](https://docs.microsoft.com/office365/customlearning/faq).
- Share your [feedback](https://github.com/pnp/custom-learning-office-365/issues) with us.



## Frequently asked questions

**Can I provision from the Microsoft 365 learning pathways admin page?**

Answer: Yes. Follow the guidance in [Provision the SharePoint Success Site to your tenant from the learning pathways administrative page](https://docs.microsoft.com/sharepoint/provision-sss#provision-the-sharepoint-success-site-1).

**Who has permission to provision the SharePoint Success Site?**

Answer: The global admin (formerly called the tenant admin).

**Who has permission to customize the site template?**

Answer: The global admin (formerly called the tenant admin) or a user who has site-owner permissions.

**Who can create custom playlists and hide or show content in Microsoft 365 learning pathways?**

Answer: The site-collection administrator and users who have site-owner permissions for Microsoft 365 learning pathways.

**Who has permissions to use the SharePoint Success Site as a user?**

Answer: Users who have Microsoft 365 user permissions, SharePoint Site visitor permissions, or higher permissions.

## Next steps

Customize the SharePoint Success Site. You can [customize](https://docs.microsoft.com/sharepoint/customize-sss) playlist content and the look and feel of the site to meet the needs of your organization.
