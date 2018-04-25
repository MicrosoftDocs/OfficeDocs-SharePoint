---
title: "Create an external business-sharing site in SharePoint Online"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 12/6/2017
ms.audience: Admin
ms.topic: article
ms.prod: office-online-server
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- Strat_OD_share
search.appverid:
- SPO160
- MOE150
- BSA160
ms.assetid: c40d4670-7f6c-4719-9c6f-8dee36220a48
description: "Do you have a need to share and collaborate with a business partner outside of your company? With SharePoint Online you can quickly and easily create an extranet site. An extranet site is a site where anyone you choose outside of your company can have secure access to content you wish to share or collaborate on. The content is kept in one place and can be accessed anywhere using any device."
---

# Create an external business-sharing site in SharePoint Online

Do you have a need to share and collaborate with a business partner outside of your company? With SharePoint Online you can quickly and easily create an extranet site. An extranet site is a site where anyone you choose outside of your company can have secure access to content you wish to share or collaborate on. The content is kept in one place and can be accessed anywhere using any device.
  
The instructions in this article guide you step by step to create a site, set it up to have external access and invite users to your site. It also shows if they have accepted your invitation, as well as monitor any activity including viewing and editing the content.
  
## Video demonstration

This video shows some of the options for configuring an extranet site in SharePoint Online.
  
****

> [!VIDEO https://www.microsoft.com/videoplayer/embed/30f3ddd4-aceb-441d-a7e5-6af9d9d3277c?autoplay=false]
  
## Set SharePoint Online sharing settings

Before you create a site for external sharing, there are some SharePoint Online sharing settings to configure.
  
In the SharePoint Online admin center, select the **sharing** tab. 
  
Under **Sharing outside your organization**, ensure that either **Allow users to invite and share with authenticated external users** or **Allow sharing to authenticated external users and using anonymous access links** is selected. This will allow you to properly configure sharing on your extranet site once you create it. 
  
Under **Additional settings**, we recommend that you select the **External users must accept sharing invitations using the same account that the invitations were sent to** check box. This ensures that the users that you invite to your site are the users who accept the invitation. If you don't enable this setting, invitations that you send could be forwarded to other users. 
  
## Create a site for your extranet

To begin, create a site collection in SharePoint Online.
  
 **To create an extranet site**
  
1. Log in to Office 365 as a SharePoint Administrator.
    
2. Navigate to the SharePoint admin center.
    
3. On the site collections page, click **New**, and then click **Private Site Collection**.
    
4. Type a title and a web site address.
    
5. Choose the **Team Site** template. 
    
6. Choose an Administrator, and then click **OK**.
    
Next, configure it to allow invited users outside of your company to be able to access the site.
  
 **To set up external access**
  
1. Select the check box for the site collection that you created, and click **Sharing**.
    
2. Under **Sharing outside your company**, choose **Allow external users who accept sharing invitations and sign in as authenticated users**.
    
3. Under **Allowing non-owners to invite new users**, click **Turn off sharing for non-owners on all sites in this site collection**.
    
Once you've set up external access, add any content that you want to the site for your External users to work on.
  
## Invite users to the site

Next, select someone in your own company to be the site owner, someone who will manage the site. It may be you or any other person internal to your organization.
  
 **To set a site owner**
  
1. Navigate to the site that you created.
    
2. Click **Share**.
    
3. Type the name of the user who you want to make a site owner.
    
4. Choose **SHOW OPTIONS**.
    
5. Under **Select a permission level** choose **[Full Control]**.
    
6. Click **Share**.
    
Once you have a site owner set up, have that owner invite External users to the site. Be sure your users have a [work or school account](https://support.office.com/article/37da662b-5da6-4b56-a091-2731b2ecc8b4) (an account that they can use to log in to Office 365) or a [Microsoft account](https://support.microsoft.com/instantanswers/d18cc497-d839-cf50-dea8-f99c95f2bd16) (such as an Outlook.com or Hotmail account). You must send the invitation to one of these types of accounts. 
  
 **To invite users to the site**
  
1. On the site that you created, click **Share**.
    
2. Type the email addresses of the people who you want to share the site with.
    
3. Choose **SHOW OPTIONS**.
    
4. Confirm that **[Edit]** is selected under **Select a permission level**.
    
5. Click **Share**.
    
## External user access

When your external users receive invitations to access the site, they should do the following:
  
1. Accept the invitation.
    
2. Enter their Microsoft credentials (the credentials for the account that the invitation was sent to).
    
3. Bookmark the site so they can return as needed.
    
## Monitoring external user activity

You can monitor the activity of your external users to ensure that they're complying with your business practices. The Security and Compliance center in Office 365 offers a wide variety of options for auditing user activity. Here are a few examples.
  
 **Show who has been sent invitations to your extranet site and if they accepted**
  
1. In Office 365, click **Admin**, and then **Admin Centers**.
    
2. Click **Security and Compliance** and then **Search &amp; investigation**. 
    
3. Click **Audit log search**. 
    
4. In the Activities box, select **Accepted Sharing Invitation** and then click **Search**. 
    
 **Show what activities your external users have done on the site**
  
1. In Office 365, click **Admin**, and then **Admin Centers**.
    
2. Click **Security and Compliance** and then **Search &amp; investigation**. 
    
3. Click **Audit log search**. 
    
4. In the activities box, select **show results for all activities** and then click **Search**. 
    
## Managing your site

When you are done collaborating with your external users, you can remove their ability to access the site by doing the following procedure.
  
 **Removing a user from having access to the site**
  
1. On your website or team site, click ** Settings **, and then click **Site settings**. 
    
2. On the Site settings page, under **Users and Permissions**, click **People and Groups**.
    
3. On the People and Groups page, click the name of the group to which you added the user.
    
4. Select the check boxes next to the user who you want to remove, click **Actions**, and then click **Remove Users from Group**. 
    
5. In the confirmation window, click OK.
    

