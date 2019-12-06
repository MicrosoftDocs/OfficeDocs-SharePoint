---
title: "Sharing errors in SharePoint and OneDrive"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
search.appverid:
- SPO160
- MET150
description: "Find the solution to SharePoint and OneDrive sharing errors"
---

# Sharing errors in SharePoint and OneDrive

This article covers the different errors that you might encounter when sharing files or folders from SharePoint Online or OneDrive for Business in Office 365. You need to be a global or SharePoint admin in your organization to fix these errors. If you are not an administrator, contact your help desk and give them your error code.

Note that changing these settings changes the types of external sharing that are allowed in your organization. In some cases, these settings may have been set by someone in your organization for business reasons.

## OSE201

Error OSE201 indicates that external sharing is turned off for all of your SharePoint and OneDrive sites.

First, change the external sharing setting for your organization:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)    
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. In the left pane of the new SharePoint admin center, select **Policies** > **Sharing**.
5. Under **External sharing**, choose **Anyone** or **New and existing guests** for both SharePoint and OneDrive.
6. Select **Save**

Next, check the external sharing settings for the site that you want to share from.

### If you're sharing from a SharePoint site:

1. In the left pane of the new SharePoint admin center, select **Sites** > **Active sites**.
2. Select the site that you want to share from, and then select **Sharing**.
3. Make sure that either **New and existing guests** or **Anyone** is selected, and then click **Save** if you made changes.

Try sharing again.

### If you're sharing from OneDrive:

1. In the Microsoft 365 admin center, in the left pane, under **Users**, select **Active users**. 
2. Select the user, and then select the OneDrive tab. 
3. Select **Manage external sharing**.
4. Make sure **Let people outside your organization access your site** is turned on and **Allow sharing with anonymous guest links and authenticated users** or **Allow sharing to authenticated guest users with invitations** is selected. 

Try sharing again.

## OSE202

Error OSE202 indicates that you can only share with guests who are already in your directory. You can [add guests directly through Azure Active Directory](https://docs.microsoft.com/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or you can change the setting by doing the following:

First, change the external sharing setting for your organization.

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)    
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. In the left pane of the new SharePoint admin center, select **Policies** > **Sharing**.
5. Under **External sharing**, choose **Anyone** or **New and existing guests** for both SharePoint and OneDrive.
6. Select **Save**

Next, check the external sharing settings for the site that you want to share from.

### If you're sharing from a SharePoint site:

1. In the left pane of the new SharePoint admin center, select **Sites** > **Active sites**.
2. Select the site that you want to share from, and then select **Sharing**.
3. Make sure that either **New and existing guests** or **Anyone** is selected, and then click **Save** if you made changes.

Try sharing again.

### If you're sharing from OneDrive:

1. In the Microsoft 365 admin center, in the left pane, under **Users**, select **Active users**. 
2. Select the user, and then select the OneDrive tab. 
3. Select **Manage external sharing**.
4. Make sure **Let people outside your organization access your site** is turned on and **Allow sharing with anonymous guest links and authenticated users** or **Allow sharing to authenticated guest users with invitations** is selected. 

Try sharing again.

## OSE204

Error OSE204 indicates that sharing is turned off for the site that you're trying to share from. You can change the setting as follows:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)    
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. In the left pane of the new SharePoint admin center, select **Sites** > **Active sites**.
5. Select the site that you want to share from, and then select **Sharing**.
6. Make sure that either **New and existing guests** or **Anyone** is selected, and then click **Save**.

Try sharing again.

## OSE205

Error OSE205 indicates that you can only share the site with guests who are already in your directory. You can [add guests directly through Azure Active Directory](https://docs.microsoft.com/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or you can change the setting by doing the following:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)    
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. In the left pane of the new SharePoint admin center, select **Sites** > **Active sites**.
5. Select the site that you want to share from, and then select **Sharing**.
6. Make sure that either **New and existing guests** or **Anyone** is selected, and then click **Save**.

## OSE207

Error OSE207 indicates that external sharing is turned off for OneDrive. You can change this setting as follows:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.    
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)    
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. In the left pane of the new SharePoint admin center, select **Policies** > **Sharing**.
5. Under **External sharing**, choose **Anyone** or **New and existing guests** for OneDrive.
6. Select **Save**

Try sharing again.

## OSE208

Error OSE208 indicates that you can only share OneDrive files and folders with guests who are already in your directory. You can [add guests directly through Azure Active Directory](https://docs.microsoft.com/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or you can change the setting by doing the following:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Under **External sharing**, change the OneDrive setting to either **Anyone** or **New and existing external users**.

6. Select **Save**.

Try sharing again.

## OSE303

Error OSE303 indicates that the person sharing the file or folder is not a member of the security groups that are allowed to share with guests and by using Anyone links. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Select **Limit external sharing to specific security groups**.

6. Under **Who can share outside your organization**, note the security groups listed for **Let only users in selected security groups share with authenticated external users and using anonymous links**. You need to add the user to one of the listed security groups. (Alternatively, you can clear the check box and remove the sharing restriction.)

To add a user to a security group:

1. On the [Groups page of the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/groups), find the group you want to edit.
2. Select the group, and then on the Members tab, select **View all and manage members**.
3. Select **Add members**.
4. Enter the user's name in the search box, select the check box in the results list, and then click **Save**.
5. Click **Close** three times.

Try sharing again.

## OSE304

Error OSE304 indicates that the person sharing the file or folder is not a member of the security groups that are allowed to share with guests. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Select **Limit external sharing to specific security groups**.

6. Under **Who can share outside your organization**, note the security groups listed for **Let only users in selected security groups share with authenticated external users**. You need to add the user to one of the listed security groups. (Alternatively, you can clear the check box and remove the sharing restriction.)

To add a user to a security group:

1. On the [Groups page of the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/groups), find the group you want to edit.
2. Select the group, and then on the Members tab, select **View all and manage members**.
3. Select **Add members**.
4. Enter the user's name in the search box, select the check box in the results list, and then click **Save**.
5. Click **Close** three times.

Try sharing again.

## OSE401

Error OSE401 indicates that your organization-level setting lets you share with only people on specific domains. The person you're trying to share with is not on one of the listed domains. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Under **Advanced settings for external sharing**, select **Add domains**, add the domain that you want to share with to the list of allowed domains, and select **OK**. Alternatively, you can turn off domain filtering by clearing the **Limit external sharing by domain** check box.
6. Select **Save**.

Try sharing again.

## OSE402

Error OSE402 indicates that your organization-level setting blocks sharing with people on specific domains. The person you're trying to share with is on one of the listed domains. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  

2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.) 

3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center. 

4. In the left pane of the new SharePoint admin center, under **Policies**, select **Sharing**.

5. Under **Advanced settings for external sharing**, select **Add domains**, remove the domain from the list of blocked domains, and select **OK**. Alternatively, you can turn off domain filtering by clearing the **Limit external sharing by domain** check box.

6. Select **Save**.


Try sharing again.

## OSE403

Error OSE403 indicates that the site from which you're sharing lets you share with only people on specific domains. The person you're trying to share with is not on one of the listed domains. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. Select **Classic features**.
5. Select **More classic features**.
6. Under **Classic site collections page**, select **Open**.
7. Select the site that you're sharing from, and then click **Sharing** in the ribbon.
8. Under **Site collection additional settings**, add the domain that you want to share with to the list of allowed domains. Alternatively, you can turn off domain filtering by clearing the **Limit external sharing using domains** check box.
9. Click **Save**.

Try sharing again.

## OSE404

Error OSE404 indicates that the site from which you're sharing blocks sharing with people on specific domains. The person you're trying to share with is on one of the listed domains. To change this setting:

1. Sign in to https://admin.microsoft.com as a global or SharePoint admin. (If you see a message that you don't have permission to access the page, you don't have Office 365 administrator permissions in your organization.)
    
    > [!NOTE]
    > If you have Office 365 Germany, sign in at https://portal.office.de. If you have Office 365 operated by 21Vianet (China), sign in at https://login.partner.microsoftonline.cn/. Then select the Admin tile to open the admin center.  
2. In the left pane, under **Admin centers**, select **SharePoint**. (You might need to select **Show all** to see the list of admin centers.)
3. If the classic SharePoint admin center appears, select **Open it now** at the top of the page to open the new SharePoint admin center.
4. Select **Classic features**.
5. Select **More classic features**.
6. Under **Classic site collections page**, select **Open**.
7. Select the site that you're sharing from, and then click **Sharing** in the ribbon.
8. Under **Site collection additional settings**, remove the domain that you want to share with from the list of blocked domains. Alternatively, you can turn off domain filtering by clearing the **Limit external sharing using domains**. check box.
9. Click **Save**.

Try sharing again.
  
## See also

[External sharing overview](external-sharing-overview.md)

[Turn external sharing on or off for SharePoint Online](turn-external-sharing-on-or-off.md)

[Stop sharing files or folders or change permissions](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)
