---
title: "Create an external business-sharing site in SharePoint Online"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/29/2018
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- Strat_OD_share
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- BSA160
- MET150
ms.assetid: c40d4670-7f6c-4719-9c6f-8dee36220a48
description: "Do you have a need to share and collaborate with a business partner outside of your company? With SharePoint Online you can quickly and easily create an extranet site. An extranet site is a site where anyone you choose outside of your company can have secure access to content you wish to share or collaborate on. The content is kept in one place and can be accessed anywhere using any device."
---

# Create an external business-sharing site in SharePoint Online

Do you have a need to share and collaborate with a business partner outside of your company? With SharePoint Online you can quickly and easily create an extranet site. An extranet site is a site where anyone you choose outside of your company can have secure access to content you wish to share or collaborate on. The content is kept in one place and can be accessed anywhere using any device.
  
The instructions in this article guide you step by step to create a site, set it up to have external access and invite users to your site. It also shows if they have accepted your invitation, as well as monitor any activity including viewing and editing the content.
  

## Set organization-level sharing settings

Before you create a site for external sharing, there are some organization-level sharing settings to configure.
  
1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. At the bottom of the page, select **Limit external sharing to specific security groups**.
  
6. Under **Sharing outside your organization**, ensure that either **Allow users to invite and share with authenticated external users** or **Allow sharing to authenticated external users and using anonymous access links** is selected. This will allow you to properly configure sharing on your extranet site once you create it. 
  
7. Under **Additional settings**, we recommend that you select the **External users must accept sharing invitations using the same account that the invitations were sent to** check box. This ensures that the users that you invite to your site are the users who accept the invitation. If you don't enable this setting, invitations that you send could be forwarded to other users. 
  
## Create a site for your extranet

To begin, create a site collection in SharePoint Online.
  
 **To create an extranet site**

On the Active sites page of the new SharePoint admin center, select **Create**, and then select **Team site**. 
    
Next, configure it to allow invited users outside of your company to be able to access the site.
  
**To set up external access**
  
1. On the Active sites page of the new SharePoint admin center, select the site you created, and then select **Sharing**.
    
2. Select **New and existing guests**.

3. At the bottom of the page, select **Limit external sharing to specific security groups**.
    
4. On the classic Sharing page, under **Allowing non-owners to invite new users**, select **Turn off sharing for non-owners on all sites in this site collection**.
    
Once you've set up external access, add any content that you want to the site for your External users to work on.
  
## Invite users to the site

Next, select someone in your own company to be the site owner, someone who will manage the site. It may be you or any other person internal to your organization.
  
 **To set a site owner**
  
1. Navigate to the site that you created.
    
2. Select **Share**.
    
3. Type the name of the user who you want to make a site owner.
    
4. Choose **SHOW OPTIONS**.
    
5. Under **Select a permission level** choose **[Full Control]**.
    
6. Select **Share**.
    
Once you have a site owner set up, have that owner invite External users to the site. Be sure your users have a [work or school account](https://support.office.com/article/37da662b-5da6-4b56-a091-2731b2ecc8b4) (an account that they can use to sign in to Office 365) or a [Microsoft account](https://support.microsoft.com/instantanswers/d18cc497-d839-cf50-dea8-f99c95f2bd16) (such as an Outlook.com or Hotmail account). You must send the invitation to one of these types of accounts. 
  
 **To invite users to the site**
  
1. On the site that you created, select **Share**.
    
2. Type the email addresses of the people who you want to share the site with.
    
3. Choose **SHOW OPTIONS**.
    
4. Confirm that **[Edit]** is selected under **Select a permission level**.
    
5. Select **Share**.
    
## External user access

When your external users receive invitations to access the site, they should do the following:
  
1. Accept the invitation.
    
2. Enter their Microsoft credentials (the credentials for the account that the invitation was sent to).
    
3. Bookmark the site so they can return as needed.
    
## Monitoring external user activity

You can monitor the activity of your external users to ensure that they're complying with your business practices. The Security and Compliance center in Office 365 offers a wide variety of options for auditing user activity. Here are a few examples.
  
 **Show who has been sent invitations to your extranet site and if they accepted**
  
1. Sign in to https://protection.office.com/?rfr=AdminCenter as a global admin or other admin who has permission to access the Security & Compliance admin center. (If you see a message that you don't have permission to access the page, you don't have necessary Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center, and under **Admin centers**, select **Security &amp; Compliance**.  
    
2. Under **Search &amp; investigation**, select **Audit log search**. 
    
3. In the **Activities** box, select **Accepted sharing invitation** and then select **Search**. 
    
 **Show what activities your external users have done on the site**
  
1. In the Security &amp; Compliance admin center, under **Search &amp; investigation**, select **Audit log search**. 
    
2. In the **Activities** box, select **show results for all activities** and then select **Search**. 
    
## Managing your site

When you are done collaborating with your external users, you can remove their ability to access the site by doing the following procedure.
  
 **Removing a user from having access to the site**
  
1. On the site, select **Settings** ![Settings icon.](media/a47a06c3-83fb-46b2-9c52-d1bad63e3e60.png), and then select **Site settings**. If you don't see **Site settings**, select **Site information**, and then select **View all site settings**.
    
2. On the Site Settings page, under **Users and Permissions**, select **People and Groups**.
    
3. On the People and Groups page, select the name of the group to which you added the user.
    
4. Select the check boxes next to the user who you want to remove, select **Actions**, and then select **Remove Users from Group**. 
    
5. In the confirmation window, select **OK**.
    

