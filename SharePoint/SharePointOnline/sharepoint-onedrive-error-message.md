---
title: "Sharing errors in SharePoint and OneDrive"
ms.reviewer: srice
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.custom: admindeeplinkSPO
ms.localizationpriority: high
search.appverid:
- SPO160
- MET150
description: "Find the solution to SharePoint and OneDrive sharing errors"
---

# Sharing errors in SharePoint and OneDrive

This article covers the different errors that you might come across when sharing files or folders from SharePoint or OneDrive in Microsoft 365. You need to be a global or SharePoint admin in your organization to fix these errors. If you aren't an administrator, contact your help desk and give them your error code.

Note that changing these settings changes the types of external sharing that are allowed in your organization. In some cases, these settings may have been set by someone in your organization for business reasons.

## OSE201

Error OSE201 indicates external sharing is turned off for all of your SharePoint and OneDrive sites.

First, change the external sharing setting for your organization:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.
    
2. Under **External sharing**, for both SharePoint and OneDrive, select **Anyone** or **New and existing guests**.

3. Select **Save**.

Next, check the external sharing settings for the site that you want to share from.

### If you're sharing from a SharePoint site:

1. In the new SharePoint admin center, select **Sites** > <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites**</a>.

2. Select the site that you want to share from, and then select **Sharing**.

3. Make sure that either **New and existing guests** or **Anyone** is selected, and if you made changes, select **Save**.

Try sharing again.

### If you're sharing from OneDrive:

1. In the Microsoft 365 admin center, in the left pane, under **Users**, select **Active users**.

2. Select the user, and then select the **OneDrive** tab.

3. Select **Manage external sharing**.

4. Make sure **Let people outside your organization access your site** is turned on, and **Allow sharing with anonymous guest links and authenticated users** or **Allow sharing to authenticated guest users with invitations** is selected.

Try sharing again.

## OSE202

Error OSE202 indicates you can share with only those guests who are already in your directory. You will be able to [add guests directly through Azure Active Directory](/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or change the setting by doing the following:

First, change the external sharing setting for your organization.

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Under **External sharing**, select **Anyone** or **New and existing guests** for both SharePoint and OneDrive.

3. Select **Save**.

Next, check the external sharing settings for the site that you want to share from.

### If you're sharing from a SharePoint site:

1. In the left pane of the new SharePoint admin center, select **Sites** > <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites**</a>.

2. Select the site that you want to share from, and then select **Sharing**.

3. Make sure that either **New and existing guests** or **Anyone** is selected, and if you made changes, select **Save**.

Try sharing again.

### If you're sharing from OneDrive:

1. In the Microsoft 365 admin center, in the left pane, under **Users**, select **Active users**.

2. Select the user, and then select the **OneDrive** tab.

3. Select **Manage external sharing**.

4. Make sure **Let people outside your organization access your site** is turned on, and **Allow sharing with anonymous guest links and authenticated users** or **Allow sharing to authenticated guest users with invitations** is selected.

Try sharing again.

## OSE204

Error OSE204 indicates sharing is turned off for the site that you're trying to share from. In such a scenario, change the setting as follows:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.
    
2. Select the site that you want to share from, and then select **Sharing**.

3. Make sure that either **New and existing guests** or **Anyone** is selected, and then select **Save**.

Try sharing again.

## OSE205

Error OSE205 indicates you can share the site with only those guests who are already in your directory. You can [add guests directly through Azure Active Directory](/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or change the setting by doing the following:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185220" target="_blank">**Active sites** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Active sites page.
    
2. Select the site that you want to share from, and then select **Sharing**.

3. Make sure that either **New and existing guests** or **Anyone** is selected, and then select **Save**.

## OSE207

Error OSE207 indicates external sharing is turned off for OneDrive. In such a scenario, change this setting as follows:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.
    
2. Under **External sharing**, select **Anyone** or **New and existing guests** for OneDrive.

3. Select **Save**.

Try sharing again.

## OSE208

Error OSE208 indicates you can share OneDrive files and folders with only those guests who are already in your directory. You can [add guests directly through Azure Active Directory](/azure/active-directory/b2b/b2b-quickstart-add-guest-users-portal), or change the setting by doing the following:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Under **External sharing**, change the OneDrive setting to either **Anyone** or **New and existing external users**.

3. Select **Save**.

Try sharing again.

## OSE303

Error OSE303 indicates the person sharing the file or folder isn't a member of the security groups that are allowed to share with guests and by using Anyone links. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Select **Limit external sharing to specific security groups**.

3. Under **Who can share outside your organization**, note the security groups listed for **Let only users in selected security groups share with authenticated external users and using anonymous links**. You need to add the user to one of the listed security groups. (Instead, you can clear the check box and remove the sharing restriction.)

To add a user to a security group:

1. On the [Groups page of the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/groups), find the group you want to edit.

2. Select the group, and then on the **Members** tab, select **View all and manage members**.

3. Select **Add members**.

4. Enter the user's name in the search box, select the check box in the results list, and then select **Save**.

5. Select **Close** three times.

Try sharing again.

## OSE304

Error OSE304 indicates the person sharing the file or folder isn't a member of the security groups that are allowed to share with guests. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Select **Limit external sharing to specific security groups**.

3. Under **Who can share outside your organization**, note the security groups listed for **Let only users in selected security groups share with authenticated external users**. You need to add the user to one of the listed security groups. (Instead, you can clear the check box and remove the sharing restriction.)

To add a user to a security group:

1. On the [Groups page of the Microsoft 365 admin center](https://admin.microsoft.com/Adminportal/Home#/groups), find the group you want to edit.

2. Select the group, and on the **Members** tab, select **View all and manage members**.

3. Select **Add members**.

4. Enter the user's name in the search box, select the check box in the results list, and then select **Save**.

5. Select **Close** three times.

Try sharing again.

## OSE401

Error OSE401 indicates your organization-level setting lets you share with only people on specific domains. The person you're trying to share with isn't on one of the listed domains. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Under **Advanced settings for external sharing**, select **Add domains**, add the domain that you want to share with to the list of allowed domains, and select **OK**. Instead, you can turn off domain filtering by clearing the **Limit external sharing by domain** check box.

3. Select **Save**.

Try sharing again.

## OSE402

Error OSE402 indicates your organization-level setting blocks sharing with people on specific domains. The person you're trying to share with is on one of the listed domains. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185222" target="_blank">**Sharing** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the Sharing page.

2. Under **Advanced settings for external sharing**, select **Add domains**, remove the domain from the list of blocked domains, and select **OK**. Instead, you can turn off domain filtering by clearing the **Limit external sharing by domain** check box.

3. Select **Save**.

Try sharing again.

## OSE403

Error OSE403 indicates the site from which you're sharing lets you share with only people on specific domains. The person you're trying to share with isn't on one of the listed domains. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

2. Under **Classic site collections page**, select **Open**.

3. Select the site that you're sharing from, and in the ribbon, select **Sharing**.

4. Under **Site collection additional settings**, add the domain that you want to share with to the list of allowed domains. Instead, you can turn off domain filtering by clearing the **Limit external sharing using domains** check box.

5. Select **Save**.

Try sharing again.

## OSE404

Error OSE404 indicates the site from which you're sharing blocks sharing with people on specific domains. The person you're trying to share with is on one of the listed domains. To change this setting:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185077" target="_blank">**More features** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    >[!NOTE]
    >If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

2. Under **Classic site collections page**, select **Open**.

3. Select the site that you're sharing from, and in the ribbon, select **Sharing**.

4. Under **Site collection additional settings**, remove the domain that you want to share with from the list of blocked domains. Instead, you can turn off domain filtering by clearing the **Limit external sharing using domains** check box.

5. Select **Save**.

Try sharing again.
  
## See also

[External sharing overview](external-sharing-overview.md)

[Manage sharing settings](turn-external-sharing-on-or-off.md)

[Stop sharing files or folders or change permissions](https://support.office.com/article/0a36470f-d7fe-40a0-bd74-0ac6c1e13323)