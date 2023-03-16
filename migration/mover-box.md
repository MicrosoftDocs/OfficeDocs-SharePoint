---
ms.date: 05/26/2020
title: Mover migration - Setting up your Box source connector
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Setting up your Box source connector to migrate to Office 365."
---
# Setting up your source:  Box

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from external cloud sources has been fully integrated into Migration Manager.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and scheduled for release in Spring 2023.



## Box FAQ

### Role changes from Box to Office 365

When moving from Box to OneDrive for Business, user roles *on folders* will change. Mover does not explicitly set a user as an owner of data during a migration.

Ownership of files and folders is always implicitly set by virtue of copying data into a user in OneDrive for Business. 

![Box to OneDrive for Business role comparison chart](media/old-box-role-to-o365-role.png)

>[!Note]
>Mover only sets permissions on folders.

### Should we disable our Box accounts?
Disabling employee access to their Box accounts mitigates any risk of them accessing data after the migration takes place.

This practice:

1. Keeps their Box accounts for a few weeks before deleting them.
2. Keeps their Box data available in read-only format.

Think of your employees' needs and what works best for the team.

### What happens to Box Notes?

Our app will automatically convert Box Notes to Word Document.

### Locked files

We automatically unlock locked Box files and download them.

The file(s) remain unlocked after this process, so if you want to re-lock the files, you must do so from Box directly.

### Disable email notifications

In Box, there are settings to notify users when downloads occur for content they own. This can equate to spam during a migration because our app downloads all their files.

When logged in as a Box admin, disable this setting from:  https://app.box.com/master/settings/notification

![disable download box](media/disable-download-box.png)

### Box data reporting

We've found that Box occasionally has hiccups with reporting storage quotas in their service. If you discover that there is a discrepancy between what we are reporting and what Box's dashboard and/or reporting informs you, you must contact their support team and ask them to refresh/recalculate the storage quotas on your account (frequently, you need to escalate this beyond their first-level support).

For more info about this issue, see **here** and **here**.


## Authorizing Box (Co-Admin)

Authorizing Box as an Administrator or a Co-Administrator is straightforward. To authorize or add a Multi-User Box account as a connector, follow these simple steps:

1. Navigate to **[Add Mover as a Custom Application](https://app.box.com/master/custom-apps)**.

   ![Custom apps](media/box-custom-apps.png)
   
2. Select **Authorize New App**.

   ![Box coadmin auth](media/box_coad_auth_01.png)
   
3. Enter the API Key: `7ypzdr66s3m80h3hutop34u7yml8928x`

4. Select **Next**.

   ![Box co-admin authorization 2](media/box_coad_auth_02.png)
   
5. In the new window, select **Authorize** to authorize our app.

   ![Box co-admin authorization 3](media/box_coad_auth_03.png)
   
6. In the Mover app, return to the **Transfer Wizard**, and select **Authorize New Connector**.

   ![Clear auth](media/clear_auth.png)
   
7. In the **Connector** list, find **Box (Co-Admin)**.

8. Select **Authorize**.

   ![Box co-admin connector list](media/box_coadmin_connector_list_auth.png)
   
   A new window (tab) opens.
   
9. Name your **Connector** \<optional\>.
    
   ![Box co-admin name connector](media/name-connector-box-coadmin.png)
   
10. Select **Authorize** again.

11. If you are not logged in, to grant access, you can use either your Box credentials, or a SSO account.

    ![Log into grant access to box](media/log-in-to-grant-access-to-box.png)
    
12. To grant our app access to your Box account, select **Allow**.

    ![grant access to box](media/grant-access-to-box.png)</br></br>

You should now be connected to Box with Co-Admin authorization!

## Troubleshooting a Box (Co-Admin) connector

### **App Permissions**
 
Your organization may default all apps to disabled. See the following quick guide about how to ensure our app is enabled.

1. Under **Enterprise Settings**, navigate to **Apps**. Here is a shortcut link: https://app.box.com/master/settings/apps

   ![enterprise settings](media/box-admin-console.png)
   
2. In the **Recommended Apps** section, ensure "Enable for 3rd party apps that are Added by Default only" is checked.

   ![box third party settings](media/recommended-apps.png)
   
3. Under **Individual Application Controls**, navigate to our app.

4. Select **Available**.

   ![enterprise app available](media/mover-enterprise-app-available.png)

### Unable to sign in to Box

If you are unable to sign in to Box, you may have turned on the option to *Disable unpublished apps by default* without providing the two App IDs required. 


 1. Under Global app settings, look for the setting **Disable unpublished apps by default**.  By default, this setting is turned off.
![screen showing disable unpublished apps option default off](media/mover-disable-unpublished-apps.png)

2. If you have turned this setting on, you need to enter the following two App IDs in the **Except for** box.


    `7ypzdr66s3m80h3hutop34u7yml8928x` </br>
    `4zb2998onvpk5934brgh48hh5ji20rgz`

![screen showing disable unpublished apps option on](media/mover-disable-unpublished-apps-on.png)


 

## Box permission requirements
For authorization, our app requires an **Administrator** or **Co-Administrator**. The following table lists the scopes we require:

| Permission | (Details) Allows our app to... |
|:-----|:-----|
|Read and write all files and folders stored in Box    |Read, create, update, and overwrite data in Box.|
|Manage Enterprise    |Manage any data found in the authorized Box directory.|
|Admin can make calls on behalf of Users    |Grants permission for our app to contact Box servers on behalf of users' accounts.|
|Admin or co-admin can make calls for any content in their enterprise    |Grants our app permission to contact Box servers on behalf of administrators or co-administrators regarding any data found in your business's Box directory.|

## Removing app access
Deleting or disabling the account used to Authorize Box (Co-Admin) does not remove our app's access to Box.

To remove our app's access to Box:

1. On the **Box Admin Console**, under **Enterprise Settings**, navigate to the **Apps** panel.

   - Scroll down to **Custom Applications**.
   
   - Select **...**, and in the dropdown menu, select **Disable app authorization**.

   ![remove box access](media/remove-box-access.png)

   > [!Note]
   > To delete a custom app, you must contact Box.


## Connecting your source Box account

If you are not already connected after you have authorized your source, select **Box**, and load the connector. An icon appears, and shows you how many users you are migrating.

![execution select box source](media/execution-select-box-source.png)


