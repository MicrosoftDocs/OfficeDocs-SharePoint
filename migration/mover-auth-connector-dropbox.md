---
title: Setting up your migration from Dropbox to Office 365
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Setting up your migration from Dropbox to Office 365"
---
# Authorizing Dropbox Connector


## Dropbox FAQ

### What happens to my unmounted folders?

Dropbox supports a selective sync function which can cause problems when trying to transfer a shared folder that is *mounted* in a specific way in Dropbox's file system. These folders can not be transfered, but we can detect these folders upon request to help identify them.

### What about Dropbox Team folders?

For easy access, our app displays Team Folders in the root of your connector (among the users).

If you're editing the source or destination paths in our app, select the back button to find the root listing of users and team drives, and select the source/destination that you want.

If you're creating a user mapping via CSV, map your Accounting Team Folder as `/Accounting` which is different than your Accounting user `/accounting@company`.com.

### How does Dropbox manage sharing and permissions?

Dropbox restricts sharing based on files or folders already shared. For example, if you have shared a subfolder, Dropbox does not allow you to change the sharing permissions of the individual subfolders or files within that folder, nor are you allowed to modify the sharing scheme of the parent until you have unshared the subfolder.


## Authorizing Dropbox Business (Multi-User)

Authorizing **Dropbox Business** as an administrator is straightforward. To authorize or add a Multi-User Dropbox Business account as a connector, follow these steps.

>[!Important]
>You MUST be an Administrator. A non-administrator account does not work.

1. In the **Transfer Wizard**, select **Authorize New Connector**.</br>

![authorize dropbox connector](media/auth-dropbox-connector.png)</br>

2. In the **Connector** list, find **Dropbox**.
3. Select **Authorize**.

![authorize dropbox source connector](media/auth-dropbox-source-connector.png)</br>

4. A new window (tab) opens. Name your Connector <optional>.</br>

![Name new dropbox connector](media/name-new-dropbox-connector.png)</br>

5. Select **Authorize** again.

6. If you are not logged in, you can use either your Dropbox credentials or an SSO account to grant access.

![Sign in to Dropbox](media/dropbox-signin.png)</br>

7.  To grant our app access to your Dropbox Account, select **Allow**.</br>

![Grant access to Dropbox account](media/grant-access-dropbox-account.png)</br>

## Authorizing Microsoft 365

>[!Warning]
>To fully authorize the **Microsoft 365 Connector**, a Global Admin is required to grant permissions to the Microsoft 365 Mover app within the Azure portal.
>
>The Global Admin must grant these permissions *after* the **Microsoft 365 Connector** is authorized within the main Mover app.

The following instructions show you how to complete the authorization steps in the right order.

Some steps in the authorization process can be completed by a Global Admin or an SPO Admin. At the beginning of each step, we indicate who can complete it.

1. **Global Admin or SPO Admin**: Via app.mover.io, log into the main Mover app. In the **Transfer Wizard**, select **Authorize New Connector**.

>[!Note]
>Whether the **Microsoft 365 Connector** is your source or destination connector (or both), you must complete this authorization process.

![Authorize new connector](media/05-authorize-new-connector.png)

2. **Global Admin or SPO Admin**: In the **Connector** list, find **Microsoft 365**. Select **Authorize**.

![Authorize O365](media/authorize-o365.png)

3. **Global Admin or SPO Admin**: A window with an **Authorize** button appears. It prompts you to give your Microsoft 365 Connector a display name <optional>. Select **Authorize**.

![Authorize windows](media/authorize-window.png)

4. **Global Admin or SPO Admin**: Follow the on-screen instructions. You are redirected to a Microsoft login screen where you can log in with your Microsoft admin privileges and continue to authorize the connector.


>[!Warning]
>If you are a **Global Admin**, a slightly different login screen appears.  
>
>**DO NOT** select the option **Consent on behalf of your organization**. This option **must** remain unselected.

- ![global admin o365](media/permissions-o365-global-admin.png)


5. **Global Admin or SPO Admin**: After authorizing the connector, you are redirected to the **Mover Transfer Wizard**, and an error appears, like the following. This means it is now time for a Global Admin in your tenant to grant permissions to the Microsoft 365 Mover app in the Azure portal.

If you're an **SPO Admin**: To grant permissions and finish the authorization process (Steps 6 – 9), point your Global Admin to **aka.ms/office365moverauth**.

If you're a **Global Admin**: Continue with Steps 6–9.

![Authorize error](media/authorize-error.png)

6. **Global Admin**: Log into the Azure Portal via **aka.ms/office365moverauth**. You'll see a list of **Enterprise applications**.

![Enterprise applications](media/enterprise-applications.png)

7. **Global Admin**: Find and select the **Microsoft 365 Mover** app. A page appears that provides an overview of our app.

![O365 Mover app](media/o365-mover-app.png)

8. **Global Admin**: In the left menu, find and open **Permissions**. Select **Grant admin consent for Mover**.

![o365 mover permissions](media/o365-mover-permissions.png)

9. **Global Admin**: A pop-up window appears that guides you through the rest of the permissions process. When complete, it closes automatically, and your **Microsoft 365 Connector** is fully authorized and ready to go.

## Troubleshooting a Microsoft 365 connector

### App access error

If you encounter an error on authorization, try signing out of any Microsoft accounts, and attempt to authorize the **Connector** in an Incognito Window.

### Provision global admin accounts

Your Global Admin user must have a Microsoft 365 account provisioned to administer other Microsoft 365 accounts. If you create a service account for our app, ensure you also assigned a Microsoft 365 license, and walked through the Microsoft 365 setup process.

### Provision users

Are your Microsoft 365 users provisioned? All Microsoft 365 users must log in to their Microsoft 365, and open Microsoft 365 for us to transfer into their accounts. You can also provision Microsoft 365 accounts via Windows PowerShell using the following commands (replace your URL and email appropriately):

`Connect-SPOService -Url https://example-admin.sharepoint.com -credential user@example.com`

`Request-SPOPersonalSite -UserEmails "neverloggedintest@example.onmicrosoft.com"`

### Microsoft 365 permission requirements

Our app requires a Global Admin for authorization. The following table lists the scopes we require.

|**Permission**|**(Details) Allows our app to...**|
|:-----|:-----|
|Create, edit, and delete items and lists in all your site collections|Create or delete document libraries and lists in all site collections on your behalf.|
|View your basic profile|See your basic profile (name, picture, user name).|
|Maintain access to data you have given it access to|See and update the data you gave it access to, even when you are not currently using our app. This does not give our app any additional permissions.|

## Connect your source Dropbox account

If you are not already connected after you have authorized your source, select **Dropbox**, and load the connector. An icon appears, and show you how many users you are migrating.

![execution select Dropbox source](media/execution-select-Dropbox-source.png)

## Connect your destination Microsoft 365 account

If you are not already connected after you have authorized your destination, select **Microsoft 365**, and load the connector. An icon appears and show you how many users you are migrating.

![Execution select Microsoft 365 destination](media/execution-select-office-365-destination.png)

## Create a new migration

Select **Continue Migration Setup**, and our app moves to the **Migration Manager**.

![Create migration](media/create-migration.png)

The next step is to create a user list of who is transfering.

From your newly created migration in the **Migration Manager**, there are two ways to add users:

- Select **Add Users**.

![Add users](media/add-users.png)

- Or, select **Migration Actions**, then select **Add to Migration**.

![Migration users](media/migration-users.png)

Select one of two options:

1. Auto Discover Users.
  - Select **Automatically Discover and Add Users**, and our app automatically finds your users and attempts to match them up.

2. Upload Migration CSV File.
  - Either drag a file into the designated space, or select **Choose a file to upload**, and add a customized CSV file for your migration.

![Add users menu](media/add-users-menu.png)

>[!Note]
>You still get to finalize your migration before any data moves!

## Creating a new migration from a CSV (optional)

Occasionally, you have thousands of users and a complicated directory schema that you want to import. In these cases, it's desirable to plan out your migration in a spreadsheet.

In these cases, we trust the CSV upload option is useful. This allows you to lay out all your users and directories, and then provide it to us in a .csv format for us to create your migration.

### Users to migrate

Your CSV file must follow this format:

A heading for the source and destination, followed by the paths, and optional tags on each line.

`Source Path,Destination Path,Tags`
`user1@example.com,user__1@corp.example.com,"Pilot, IT"`</br>
`user2@example.com,user__2@corp.example.com,"Pilot, Sales"`</br>
`user3@example.com/src dir,user3@example.com/migrated,"Pilot, IT"`</br>
`Source Shared Drive,user4@example.com/Team Folder,"Pilot, Sales"`</br>
`https://TENANT02.sharepoint.com/sites/SiteName/Shared%20Documents,user5@example.com,"Marketing, Sales"`</br>

>[!Note]
>Ensure your CSV has no spaces after each comma-separated value. Values that require commas must be wrapped in quotation marks.

Download an example CSV:

**Example_CSV_Map.csv**

>[!Note]
>When URL mapping to SharePoint Online, you must remove everything after /Shared%20Documents; otherwise,the URL fails.

For example, this full URL won't work:
`https://TENANT01.sharepoint.com/sites/SiteName/Shared%20Documents/Forms/AllItems.aspx`

It should be changed to:
`https://TENANT01.sharepoint.com/sites/SiteName/Shared%20Documents`

### Creating your CSV in Excel

To use an Excel spreadsheet to create your CSV:

1. Ensure you have two columns, one titled `Source Path`, and one `Destination Path`.
2. List the relative paths, domains, and usernames on the subsequent rows.
3. Export your spreadsheet as a CSV:
  a. Select **File**.
  b. Select **Save As**.
  c. From the **File Format** options, select **CSV**.

## Reviewing your users

### Checking paths

Confirm that the users in the Dropbox source match the users in the Microsoft 365 destination. Usually the emails/usernames match up, but it depends how you structure and name your users. *Be diligent during this step!*

### Editing

Be aware that Users can only be edited if they haven't been scanned, or had a transfer run.

To edit a user source entry:

1. To select a user row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the source path.
3. A new side panel opens, enabling you to edit the Dropbox source path.
4. To select your parent source path, double-click it, and to complete your edit, select **Save**.

![Edit source user](media/edit-source-user.png)

To edit a user destination entry:

1. To select a user row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the destination path.
3. A new side panel opens, enabling you to edit the Microsoft 365 destination path.
4. To select your parent destination path, double-click it. To complete your edit, select **Save**.

![Edit destination user](media/edit-destination-user.png)

You can also choose to edit your user entries via CSV, though this is a fairly in-depth process. *If you are simply looking to make a handful of edits to your paths, we recommend using the previous method.*

To edit or update your current existing user pairings:

1. Near the top right of the **Migration Manager**, select **Migration Actions**.
2. Select **Update Migration**.
3. Upload your .csv file.</br>

Tips for creating the CSV:
  - The CSV needs to follow this format:
     - `ID, Source Path, Destination Path`</br>
     - `id12345, /first.last@example.com, /f.last@example.com`

  - The `ID` column is required to specify the existing row in the **Migration Manager**, whereas the source and destination path are optional - as in, you don't need to enter both if you only want to edit the destination path, for example - and leaving both of those columns blank mean no changes are made.
 
    - To get the ID for each row:</br>
      a. Find and select **Migration Actions**.</br>
      b. Select **Customize Columns**, and select **ID**.</br>
        
    You'll now be able to see the ID appearing in each row. If you refresh the page, this info disappears unless you select **Save Column State**.

Download an example CSV:

[example_path_edit.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_path_edit.csv)

![Add ID customize column](media/add-id-customize-column.png)

4. After you've created your CSV file using these instructions and format, you can drag and drop the file into our app, or select **Choose a file to upload**. Changes to your user pairings are implemented immediately.

![Update migration](media/update-migration.png)

### Adding

If you missed users in your original CSV upload, or simply want to add new user entries to the current migration, add them via CSV. All entries you add in this manner are appended to the current migration, meaning this won't modify existing rows and it is possible to create duplicate entries alongside the ones that already exist.

To add new users:

1. Near the top right of the **Migration Manager**, select the **gear** icon.
2. Select **Add to Migration**.
3. Upload your .csv file.</br>

Tips for creating the CSV:
  - CSV needs to follow this format:</br>
    `Source Path, Destination Path`</br>
    `/first.last@example.com, /flast@example.com`
  - **CSV is created the same way you would if you initially created the migration with a CSV**.
4. After you've created your CSV file using these instructions and format, drag and drop the file into our app, or select **Choose a file to upload**. Changes to your user pairings are implemented immediately.

![Add to Migration](media/add-to-migration.png)

### Duplicating

At any time, you may duplicate a user in the **Migration Manager** list. To duplicate a user entry:

1. To choose a user row, on the left side of a row, select the respective checkbox. You may select more than one entry at a time.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row you want to duplicate.
3. In the context menu, select **Duplicate # User**.
4. Select **OK**.</br>

A new user entry appears. From here, you can change the directory, schedule, or even the entire user.

![duplicate user](media/duplicate-user.png)

### Scheduling

You can set an hourly, daily, weekly, or monthly schedule for each user, even after they have been run.

To create or edit a schedule:

1. Select the user pairing(s) you want to schedule.
2. Select the **User Actions** dropdown menu.
3. Select **Schedule # Users**.
4. Configure your Hourly, Daily, Weekly, or Monthly setup, including the timing and day of the week (where applicable).
5. Select **Apply Schedules to X Users**.

#### Deleting

Be aware that users can only be deleted if they haven't been scanned, or had a transfer run.

To delete a user entry:

1. To choose a user row, on the left side of a row, select the respective checkbox. You can select more than one entry at a time.
2. On the right and directly above the user rows, select **User Actions**, or right-click the user row you want to delete.
3. In the context menu, select **Delete User**.

>[!Important]
>This is permanent and cannot be undone unless you create a new entry.

![delete user](media/delete-user.png)

## Reviewing your permission map

The permission map is a critical part of your migration.

When a user is migrated, we transfer files and folders and share any required data. We already know who is copying data, but we also need to know who might have content shared with them, even if they don't copy data.

To stay organized, we provide a secondary list of your users, called a permission map. This list includes everyone who could possibly receive sharing permissions to any files or folders that might be migrated. This even includes users who are not migrating data.

Another important consideration is that usernames and emails aren't always consistent across platforms, and the permission map helps us line up everyone.

**Example**: `jane@example.com` is actually `j.smith@example.com`

We automatically detect users and handle perfect matches. Any inconsistencies must be manually reconciled. The permission map can be continually updated, because with each incremental pass of the migration, permissions are reapplied.

1. To view your permission map, in the top right of the **Migration Manager**, select **Migration Actions**, and then, from the dropdown menu, select **Edit Permission Map**.

![permission map](media/edit-permission-map.png)

You may either auto-discover or upload a permission map file. We automatically pair perfect matches. If a user or group in Dropbox does not have a perfect match in Microsoft 365, you can correct it in our interface.

2. Select **Auto-discover Users**.

![permission map](media/permission-map-auto-discover-users.png)

3. At any time, you may view and edit your permission map.

![permission map](media/permission-map.png)

>[!Note]
>A blank destination entry automatically cancels any permission sharing for that user or group.

>[!Note]
>Adding a new line for a specific users - for example, user01@gmail.com to user01@hotmail.com - that perfectly matches auto-discovered permissions by the domain - for example, `@gmail.com` to `@hotmail.com` - is automatically removed. Our app marks these as redundant entries.

## Uploading a permission map (optional)

You can upload a permission map in CSV format. This overwrites any existing permission map, so use caution. In an ideal world, all users are matched. If there are a few unmatched users, from the web interface, you can manually add names to the **Destination** field.

![permission map overview](media/permission-map-overview.png)

Ensure that your permission map follows this strict format:

A heading for the source and destination, followed by domain names, groups, usernames, or emails.

`Source User, Destination User`</br>
`example.com, example.com`</br>
`corp.example.com, example.com`</br>
`user@example.com, differentuser@example.com`</br>
`group, group`</br>

Permission maps should have two specific entries:

1. Any domain names that are wildcard matched, (for example, `example.com, example.com` or `contoso.com, corp.contoso.com`). This instructs our app to match any users with those domain names in their source email to their new destination email domain.
2. Imperfect matches. Users that are differently named between the source and destination domains need to be explicitly listed, (for example, `firstname@contoso.com, firstname_lastname@contoso.com`).
3. Groups can also be included for most connectors. These are explicitly required and are not matched with a domain wildcard, (for example, `Sales Team, Global Sales Team`).
4. We strip all leading and trailing spaces from each path value, unless it is wrapped in quotation marks.

Download an example CSV:

[example_permission_map.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_permission_map_box.csv)

## Creating your CSV in Excel

If you are using an Excel spreadsheet to create your CSV:

- Ensure you have two columns, one titled `Source User`, and one `Destination User`. Check the spelling on the domains, usernames, and groups listed.

For example:

`Source User, Destination User`</br>
`example.com, example.com`</br>
`eric@example.com, ewarnke@example.com`</br>
`joshua@example.com, jbadach@example.com`</br>
`Sales Team,Global Sales Team`

![excel overview](media/excel-overview.png)

## Exporting a permission map

You can export a permission map in CSV format.

1. Select **File**.
2. Select **Save As**.
3. From the **File Format** options, select **CSV**.

![excel save as csv](media/excel-save-as-csv.png)

## Migration Manager overview

The **Migration Manager** is the key part of our app. It is the primary screen for interacting during the data migration process.

![migration main mover](media/migration-main-mover.png)

### Migration Manager dashboard

Use the **Migration Manager** dashboard for a summary of your overall migration. This is covered in depth **here**.

### Main menu bar

Use our app's main navigation bar to switch between the **Migration Manager**, **Transfer Wizard**, and your **Account** details, as well as contact support if you run into any issues during your migration.

![migration top mover](media/migration-top-mover.png)

### Migration selection

Use the **Migration Selection** bar to navigate between separate multi-user migrations, as well as individual normal transfers.

Here, you are also able to edit and personalize the names of each multi-user migration.

![migration edit mover](media/migration-edit-mover.png)

### Migration actions

Use the **Migration Actions** menu to access things such as: the migration reports, the columns displayed, and the overall layout of your migration to best suit your personal needs.

![migration action mover](media/migration-action-mover.png)

### Filters

Use the **Active Filters** bar to search your migration for specific key terms or custom tags you have applied.

![migration filter](media/migration-filter.gif)

You can also view more in-depth instructions by selecting the info button directly to the right of the **Active Filters** search bar, or by viewing the **Active Filter** list.

![migration filter info](media/migration-filter-info.png)

### User display

The user display is the central focus of the **Migration Manager**, and displays all the users in the current migration.

This section of our app provides you with a column-by-column breakdown of each individual user in a migration. Here, you can also duplicate and edit source/destination paths of a user, as well as view the logs of any scanned or completed transfers.

![migration users mover](media/migration-users-mover.png)

### User actions and finalization

This area of the screen contains the **User Actions** dropdown, the **Scan User** and **Start Migrating Users** buttons.

![migration final mover](media/migration-final-mover.png)

**User Actions** opens a new dropdown menu enabling you to interact with a selected transfer.

![migration actions mover](media/migration-actions-mover.png)

**Scan # Users** performs a scan of the selected users. This helps identify any problematic files, folders, or connectors.

**Start # Migrating Users** opens a side tab enabling you to finalize and begin the migration.

![migration finalize mover](media/migration-finalize-mover.png)


