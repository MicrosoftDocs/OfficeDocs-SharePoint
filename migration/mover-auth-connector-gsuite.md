---
title: Authorizing the G Suite Connector
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
description: "Authorizing the G Suite Connector"
---
# Authorizing the G Suite Connector


## G Suite FAQ

### How is G Suite Drive different?

In Drive, content may exist in multiple locations based on how each user prefers to organize their files. This sharing paradigm in G Suite Drive differs from most other providers.

When a folder is shared to another user, it appears in their **Shared with Me** section. From there, it can be added to the user's **My Drive**, and then placed in any folder of their choosing, including other shared folders.

### G Suite Shared Drives

For easy access, our app displays **Shared Drives** (previously **Team Drives**) in the root of your connector (among the users).

If you're editing the source or destination paths in our app, simply select the back button to find the root listing of users and Shared Drives, and select the source/destination that you would like.

If you're creating a user mapping via CSV, you would map your Accounting Shared Drive as /Accounting, which is different than your Accounting user /accounting@company.com.

### G Suite Shared Drives permissions

Our app is not able to read or write permissions to Google Shared Drives. Shared Drives do not allow explicit folder level permissions. Rather, Shared Drive permissions are set based on the Shared Drive members.

### What's the difference between file versions and revision history?

Revision history for Google Docs, Sheets, and Slides is different than file versions in Google Drive. Revision history refers to the ability to see earlier versions of a file, and view who made specific edits to the document. During the migration, revision history is not transfered. Only the most recent version of a file is transfered.

![revision history](media/revision-history.png)

### What isn't transfered

#### What happens to Google Drawings, Forms, Sites, and Maps?

Google does not allow us to export Drawings, Forms, Sites, and Maps from Drive. These are not transfered.

#### What about Docs, Slides, and Sheets?

Google's proprietary formats are not compatible with anything other than G Suite Drive. When migrating from G Suite, our app converts to the Microsoft Office format from Google's format.

Any Google format that is larger than 10 MB when it is converted fails. This is a limitation Google has placed on their infrastructure. For more info, see https://developers.google.com/drive/api/v3/reference/files/export.

>[!Note]
>The only way to migrate/download a Google format file is to request that they [Google] convert it. Mover does not control the conversion process, and the forced limitations are strictly on Google's end.

![google format vs office format](media/google-format-versus-office-format.png)

#### Files marked as restricted

G Suite Drive enables owners to disable the ability for users to copy, download, or print a file on a per-file basis. This feature must be disabled on each file for which it has been enabled, in order for a migration to function properly, or you receive an error stating:

`Permissions issue: File marked as restricted or not copyable`

To disable this feature, see the **Sharing** settings for a file, and select **Advanced**. Check the checkbox for the owner of the file to **Disable options to download, print, and copy for commenters and viewers.**

![restricted file](media/restricted-file.png)

## Required pre-scan of G Suite Drive

Permissions and ownership of data in a G Suite Drive source can be complicated. To retain a similar directory structure and sharing scheme in the destination, our app must make some decisions on who owns what and where that data is best located.

*G Suite Drive allows files and folders to exist in different places for different users.*

When a folder is shared out to another user, it appears in their **/Shared with me** section. From there, it can be added to the user's /My Drive and then placed in any folder of their choosing, including their own folders, or other shared folders.

Microsoft 365 does not support this same nesting of shared data, which is why we've developed a solution.

##### Examples

See the following two examples for how users might create conflicting folder structures.

**Example 1**:
1. Mark shares a folder with Eric.
2. Eric views **Shared with me**, and selects **Add to My Drive** on this new shared folder.
3. In **My Drive**, Eric drags this new folder to a different folder.
4. There are now two conflicting subfolders that our app must make a decision on.

**Example 2**:
Any file or folder in a user's My Drive may be arbitrarily added to a new location. These files or folders will be viewable in multiple places. The *correct* location is now unclear.

![file save in two places](media/file-saved-in-two-places-example.png)

#### The solution

In order to ensure your users still have access to all their important files, our app automatically makes an intelligent decision on which folder becomes the source of truth when multiple users have conflicting views.

Before your migration, our app can perform a pre-scan of all your source G Suite users. Users are ordered by priority, typically with administrators and department heads at the top. This determines the order of conflict resolution, with higher priority users winning over lower priority users.

The pre-scan process is fairly complicated; however, there are some basic rules:

1. When a folder in the root of a user's /My Drive conflicts with a folder in another user's /My Drive/subfolder, the subfolder always will win. Root folders never take priority over a subfolder during a conflict.
2. If a folder, which exists as a subfolder, is in different locations for different users, our app transfers ownership of the entire folder and all of its contents to the higher priority user, and shares it again with the user that lost the conflict.

Here is a visual guide to the pre-scan decision process:

![Pre-scan decision tree for G Suite](media/prescan-decision-tree-gsuite.png)

### Before and after

![G Suite Drive before and after](media/gsuite-before-after.png)

### Security concerns

Because of the nature of G Suite Drive's sharing model, it can open up some security concerns when migrating to Microsoft 365. The problem stems from the idea of negatively setting permissions, for example, sharing a parent folder, then removing permissions from some subfolders. All Microsoft 365 destination subfolders inherit their parent permissions, which could have unintended consequences when performing a migration.

![G Suite Drive perms concerns](media/gsuite-perms-security-concern.png)

In the previous scenario, our app would reapply collaborator permissions to the /Human Resources folder, and all subfolders inside it would inherit those permissions.

### Requirements

To perform a Google pre-scan, our engineers require the following:

- A fully set up migration in our app, with transfers created for all users you want to migrate
- A full list of all of your users in order of priority:
  - Single column list of all account emails on your source Google domain (.csv/.xlsx).
  - Includes all users you are migrating, even if they are non-priority.
  - Highest priority at the top, lowest priority at the bottom, for example:
    `ceo@email.com`
    `manager@email.com`
    `employee@email.com`

- The migration ID
  - To get the migration ID:
    - Find and select **Migration Actions**.
    - Select **Customize Columns**, and select **Migration ID**.
    - You'll now be able to see the migration ID appearing in each row. If you refresh the page, this info disappears unless you select **Save Column State**.

![add it customize column](media/add-id-customize-column.png)

>[!Important]
>The Google pre-scan must be run before the (counting) scan, otherwise the file counts will not be accurate. A Google pre-scan request could take up to one business day to be fielded, so provide all of the aforementioned info with at least 24 hours notice.


## Authorizing G Suite Drive (Administrator)

To authorize or add a **G Suite Drive** account as a **Connector**, follow these simple steps:

>[!Important]
>You must be a G Suite Administrator.

1. From your **Google Apps** dashboard, select our app's grid logo, and then select **Admin**.
2. Select **Apps**, and then select **Marketplace Apps**.
3. Near the top right, to add a new app, select **+**, and search for **Mover**.
>[!Important]
>When our app opens in a new tab/window, to verify that you are viewing the Marketplace using your admin Google account, at the top right, select the **account** icon.
4. Select **Domain Install**, and then select **Continue**.
5. Select the checkbox stating you agree to the **Terms of Use**, and then select **Accept**.
6. Select **Next**. To close the overlay window, select **Done**.
You should see our app installed amongst any other third-party apps you have. If it does not appear, simply refresh the page.

We now have access to your users and their data, so we can move on to **Connector** authorization.

![google marketplace](media/google_marketplace.gif)

7. After install, select **our app**, and ensure that you grant Data Access. This is an extra security step required by G Suite.

![grant data access g suite](media/grant-data-access-g-suite-admin.png)

8. In the **Transfer Wizard**, select **Authorize New Connector**.

![clear auth](media/clear_auth.png)

9. In the **Connector** list, find **G Suite (Administrator)**.
10. Select **Authorize**.
11. A new window (tab) opens. Name your Connector <optional>.

![name connector gdrive](media/name-connector-google-drive.png)

12. Select **Authorize** again.
13. If you are not logged in, to sign in, use your Google credentials.

![login to grant access to gdrive](media/log-in-to-grant-access-to-google-drive.png)

14. To grant our app access to your G Suite (Administrator) Account, select **Allow**.

![grant access to gdrive](media/grant-access-to-google-drive.png)

## Troubleshooting a G Suite (Administrator) connector

### App permissions

For us to be able to view and transfer data to and from G Suite Drive, you must have our app installed as per the instructions in **Connector Creation**. In some cases, you may have our app installed, but disabled. If you are having problems connecting, you should ensure our marketplace app is enabled for all users. To access your third-party app settings in **Google Apps**, follow the same steps.

### Google Drive permission requirements

Our app requires a Global Admin for authorization. The following table provides a detailed list of the scopes we require.

|**Permission**|**(Details) Allows our app to...**|
|:-----|:-----|
|See, edit, create, and delete all of your Google Drive files    |Permission to edit, create, overwrite, and organize data in your Google Drive.|
|View usage reports for your G Suite domain    |Grant permission to view reports about how users are using Google Apps within your G Suite domain.|
|View domains related to your customers    |View domain aliases and multi-domains (secondary domains) for your customers.|
|View and manage the provisioning of groups on your domain    |Provision and modify groups on your domain, as well as view and modify details and metadata of groups on your domain.|
|View users on your domain    |View basic details and metadata of users on your domain.|

## Authorizing Microsoft 365

>[!Warning]
>To fully authorize the **Microsoft 365 Connector**, a Global Admin is required to grant permissions to the Microsoft 365 Mover app within the Azure portal.
>
>The Global Admin must grant these permissions *after* the **Microsoft 365 Connector** is authorized within the main Mover app.

The following instructions show you how to complete the authorization steps in the right order.

Some steps in the authorization process can be completed by a Global Admin or an SPO Admin. At the beginning of each step, we indicate who can complete it.

1. **Global Admin or SPO Admin**: Log in to the main Mover app via **app.mover.io**. In the **Transfer Wizard**, select **Authorize New Connector**.

>[!Note]
>Whether the **Microsoft 365 Connector** is your source or destination connector (or both), you'll need to go through this authorization process.

![Authorize new connector]( media/05-authorize-new-connector.png)

2. **Global Admin or SPO Admin**: In the **Connector** list, find **Microsoft 365**. Select **Authorize**.

![authorize o365](media/authorize-o365.png)

3. **Global Admin or SPO Admin**: A window with an **Authorize** button appears. It prompts you to provide a display name <optional> for your **Microsoft 365 Connector**.  Select **Authorize**.

![Authorize window](media/authorize-window.png)

4. **Global Admin or SPO Admin**: Follow the on-screen instructions. You are redirected to a Microsoft login screen where you can log in with your Microsoft admin privileges and continue to authorize the connector.


>[!Warning]
>If you are a **Global Admin**, a slightly different login screen will display.  
>
>**DO NOT** select the option **Consent on behalf of your organization**. This option **must** remain unselected.

- ![global admin o365](media/permissions-o365-global-admin.png)



5. **Global Admin or SPO Admin**: After authorizing the connector, you are redirected to the **Mover Transfer Wizard**, and an error appears, like the following. This means it is now time for a Global Admin in your tenant to grant permissions to the Microsoft 365 Mover app in the Azure portal.

If you're an **SPO Admin**: To grant permissions and finish the authorization process (Steps 6–9), point your Global Admin to **aka.ms/office365moverauth**.

If you're a **Global Admin**: Continue with Steps 6–9.

![Authorize error](media/authorize-error.png)

6. **Global Admin**: Log into the Azure Portal via **aka.ms/office365moverauth**. You'll see a list of **Enterprise applications**.

![enterprise applications](media/enterprise-applications.png)

7. **Global Admin**: Find and select the Microsoft 365 Mover app. A page appears that provides an overview of our app.

![O365 mover app](media/o365-mover-app.png)

8. **Global Admin**: In the left menu, find and open **Permissions**. Select **Grant admin consent for Mover**.

![o365 mover permissions](media/o365-mover-permissions.png)

9. **Global Admin**: A pop-up window appears that guides you through the rest of the permissions process. When complete, it closes automatically, and your **Microsoft 365 Connector** is fully authorized and ready to go.

## Troubleshooting a Microsoft 365 connector

### App access error

If you encounter an error on authorization, try signing out of any Microsoft accounts, and attempt to authorize the **Connector** in an Incognito Window.

### Global Admin account provisioning

Your Global Admin user must have a Microsoft 365 account provisioned in order to administer other Microsoft 365 accounts. If you create a service account for our app, ensure you also assigned a Microsoft 365 license, and walked through the Microsoft 365 setup process.

### User provisioning

Are your Microsoft 365 users provisioned? All Microsoft 365 users must log in to their Microsoft 365, and open Microsoft 365 for us to transfer into their accounts. You can also provision Microsoft 365 accounts via Windows PowerShell using the following commands (replace your URL and email appropriately):

`Connect-SPOService -Url https://example-admin.sharepoint.com -credential user@example.com`

`Request-SPOPersonalSite -UserEmails "neverloggedintest@example.onmicrosoft.com"`

### Microsoft 365 permission requirements

Our app requires a Global Admin for authorization. The following table lists the scopes we require:

|**Permission**|**(Details) Allows out app to...**|
|:-----|:-----|
|Create, edit, and delete items and lists in all your site collections|Create or delete document libraries and lists in all site collections on your behalf.|
|View your basic profile|See your basic profile (name, picture, user name).|
|Maintain access to data you have given it access to|See and update the data you gave it access to, even when you are not currently using our app. This does not give our app any additional permissions.|

## Connecting your source G Suite Drive account

If you are not already connected after you have authorized your source, select **G Suite Drive**, and load the connector. An icon appears, and shows you how many users you are migrating.

![execution select gdrive source](media/execution-select-google-drive-source.png)

## Connecting your destination Microsoft 365 account

If you are not already connected after you have authorized your destination, select **Microsoft 365**, and load the connector. An icon appears and show you how many users you are migrating.

![execution select o365 destination](media/execution-select-office-365-destination.png)

## Creating a new migration

Select **Continue Migration Setup**, and our app moves to the **Migration Manager**.

![create migration](media/create-migration.png)

The next step is to create a user list of those transfering.

From your newly created migration in the **Migration Manager**, there are two ways to add users:

- Select **Add Users**.

![add users](media/add-users.png)

- Or, select **Migration Actions**, then select **Add to Migration**.

![migration users](media/migration-users.png)

Select one of two options:

1. Auto Discover Users.
  - Select **Automatically Discover and Add Users**, and our app automatically finds your users and attempts to match them up.

2. Upload Migration CSV File.
  - Either drag a file into the designated space, or select **Choose a file to upload**, and add a customized CSV file for your migration.

![add users menu](media/add-users-menu.png)

>[!Note]
>You still get to finalize your migration before any data moves!

## Creating a new migration from a CSV (optional)

Sometimes you have thousands of users and a complicated directory schema that you want to import. In these cases, it's desirable to plan out your migration in a spreadsheet.

In these cases, we trust the CSV upload option is useful. This allows you to lay out all your users and directories, and then provide it to us in a .csv format for us to create your migration.

### Users to migrate

Your CSV file must follow this format:

A heading for the source and destination, followed by the paths, and optional tags on each line.

`Source Path,Destination Path,Tags`</br>
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

Change it to:
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

Confirm that the users in the G Suite Drive source match the users in the Microsoft 365 destination. Usually the emails/usernames match up, but it depends how you structure and name your users. *Be diligent during this step!*

### Editing

Be aware that Users can only be edited if they haven't been scanned, or had a transfer run.

To edit a user source entry:

1. To select a User row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the source path.
3. A new side panel opens, enabling you to edit the G Suite Drive source path.
4. To select your parent source path, double-click it, and to complete your edit, select **Save**.

![edit source user](media/edit-source-user.png)

To edit a user destination entry:

1. To select a user row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the destination path.
3. A new side panel opens, enabling you to edit the Microsoft 365 destination path.
4. To select your parent destination path, double-click it. To complete your edit, select **Save**.

![edit destination user](media/edit-destination-user.png)

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

![add id customize column](media/add-id-customize-column.png)

4. After you've created your CSV file using these instructions and format, you can drag and drop the file into our app, or select **Choose a file to upload**. Changes to your user pairings are implemented immediately.

![update migration](media/update-migration.png)

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

![Add to migration](media/add-to-migration.png)

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

### Deleting

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

**Example**:  `jane@example.com` is actually `j.smith@example.com`

We automatically detect users and handle perfect matches. Any inconsistencies must be manually reconciled. The permission map can be continually updated, because with each incremental pass of the migration, permissions are reapplied.

1. To view your permission map, in the top right of the **Migration Manager**, select **Migration Actions**, and then, from the dropdown menu, select **Edit Permission Map**.

![edit permission map](media/edit-permission-map.png)

You may either auto-discover or upload a permission map file. We automatically pair perfect matches. If a user or group in G Suite Drive does not have a perfect match in Microsoft 365, you can correct it in our interface.

2. Select **Auto-discover Users**.

![permission map auto discover users](media/permission-map-auto-discover-users.png)

3. At any time, you may view and edit your permission map.

![permission map](media/permission-map.png)

>[!Note]
>A blank destination entry automatically cancels any permission sharing for that user or group.
>
>[!Note]
>Adding a new line for a specific users - for example, user01@gmail.com to user01@hotmail.com - that perfectly matches auto-discovered permissions by the domain - for example, `@gmail.com` to `@hotmail.com` - is automatically removed. Our app marks these as redundant entries.

### G Suite Drive caveats

>[!Note]
>The G Suite Drive requires any groups in your permission map to use the group email address, and not the group name.

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
3. Groups can also be included for most connectors. These are explicitly required and are not matched with a domain wildcard, (for example, `Sales Team, Global Sales Team`). For G Suite, the group email is used instead of the group name (for example, `salesteam@example.com, globalsalesteam@example.com`).
4. We strip all leading and trailing spaces from each path value, unless it is wrapped in quotation marks.

Download an example CSV:

[example_permission_map.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_permission_map.csv)

### Creating your CSV in Excel

If you are using an Excel spreadsheet to create your CSV:

- Ensure you have two columns, one titled `Source User`, and one `Destination User`. Check the spelling on the domains, usernames, and groups listed.

For example:

`Source User, Destination User`</br>
`example.com, example.com`</br>
`eric@example.com, ewarnke@example.com`</br>
`joshua@example.com, jbadach@example.com`</br>
`Sales Team,Global Sales Team`

![excel overview](media/excel-overview.png)

### Exporting a permission map

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

This area of the screen contains the **User Actions** dropdown menu, the **Scan User** and **Start Migrating Users** buttons.

![migration final mover](media/migration-final-mover.png)

**User Actions** opens a new dropdown menu enabling you to interact with a selected transfer.

![migration actions mover](media/migration-actions-mover.png)

**Scan # Users** performs a scan of the selected users. This helps identify any problematic files, folders, or connectors.

**Start # Migrating Users** opens a side tab enabling you to finalize and begin the migration.

![migration actions mover](media/migration-finalize-mover.png)


