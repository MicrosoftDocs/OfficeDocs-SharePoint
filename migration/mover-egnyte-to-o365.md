---
title: Migrating to Office 365 from Egnyte
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
description: "How to Migrate from Egnyte to Office 365"
---

# How to migrate from Egnyte to Office 365

## Introduction

Our purpose is to act as an intermediary between various web technologies that don't play nice together. We take your files from one place and copy them to another. No downloads and nothing to watch over—our web-hosted app does all the work!

Undertaking any corporate migration is a daunting task. When moving from Egynte to Office 365, there are many things to consider. Our team has done this enough times to have learned a thing or two. We hope this guide helps you migrate successfully from Egynte to Office 365.

If you experience any issues, please do not hesitate to ask us questions!

>[!Tip]
> Need help? [Open a support request here](https://support.microsoft.com/en-us/supportforbusiness/productselection?sapId=c3fa6eba-e1f0-0715-4519-94a9740c5f2c)



### File processing summary

When we transfer a file, a temporary copy is downloaded from **Egynte** to a temporary server and then uploaded to Office 365. Upon successful upload, that file is deleted from the temporary server. When your migration is complete, that temporary server is eliminated. Any log data expires in 90 days and is never retained by us. We do not perform any actions beyond copying files and folders and sharing permissions. We never perform delete operations.

## Communicating with stakeholders

A migration is a significant undertaking for any organization. Trying to grasp the entire extent of all data and communicating with your employees is complicated. We sympathize!

Before, during, and after a migration, it is critical to communicate clearly and effectively with your user base. We provide timely support and communication materials to your transition team to help you communicate these changes with each stakeholder.

**Management** — Management needs succinct info about the how's and why's of the migration, such as costs, benefits, and expectations. You must paint a clear picture about what a successful migration should look like. Granular info is important when running a department.

For example, the Sales Manager needs to know how operations will be affected, such as *Can employees still work over the weekend, if needed?*

**Users** — These are your bread-and-butter employees. They need to know when changes are taking place and who to go to with questions or issues.

Key questions to address:

- Why are we migrating our data?
- How does it impact me?
- What are the benefits?
- How disruptive is this change going to be?
- What are the differences between Egnyte and Office 365, and how do I reconcile them?

**Third parties** — If people outside your organization have access to collaborate on documents, this could potentially be interrupted and require resharing of data. We describe best practices for this event in our guide.

**IT Helpdesk/Support staff** — If your organization is large enough to have specific support staff for other employees, they must understand each step of the migration.

## Planning

Planning is the most difficult part of a migration. It is also one of the most critical phases to get correct. To have a smooth and stress-free migration, you must gather relevant organizational info, determine project timelines, and mitigate any surprises that may appear.

### Gathering info

Before migration, it is important to gather all the info you need to run the migration smoothly. Make sure you have confirmed the info from the following checklist.

**Migration info checklist**

- Number of users to migrate
- Data ownership
- Data distribution
- Amount of data to move
- Number of files to move
- Individual file sizes and/or file sizes on average
- Who is your migration team?
- Who is your designated contact with us?
- Who is our point of contact with you?

### Scanning

To help with your planning, we offer a scanning feature. Our scan identifies how many users own data and how much there is to move.

This scan is effectively a simulated dry-run migration, with no set destination, which helps to identify any problematic files/folders before you begin migrating data.

>[!Note]
>The scan is available in our **Migration Manager** after you have first set up a migration.

Read through this guide to better understand the full migration process, or skip ahead to **Setting Up the Migration**. For detailed instructions about how to run the scan, see **Scanning.**

### Number of users to migrate

Each *user* is defined by a unique source and destination pairing.

For example:

- user01@example.com => user02@example.com
- user01@example.com => user03@example.com

These would be considered two separate *user licenses* because they have different destinations.

This also applies for separate **Egnyte Shared & private Folders** migrating to a single destination user account.

For example:

- /Shared/Sales => user01@example.com
- /Shared/clients => user01@example.com
- /Private/User01 => user01@example.com
- /Private/User02 => user01@example.com

This qualifies as three separate *User Licenses*, even though they are all going to the same destination. Egnyte's /Shared folder is considered one source, while every /Private folder is considered a separate source.

Migrations are run on a per-user basis. Because of our app's scalable infrastructure, it is feasible to run dozens of users or thousands simultaneously. Any number of users can be migrated in whatever pre-defined order or grouping you desire.

**Collaborators-only**: Your fiscal budget need only include users that own data in Egnyte. Anyone that strictly engages as a collaborator in Egnyte (for example, they only share other users' content), do not have any data copied, and therefore do not incur a fee.

**Setting permissions is free**. Users that strictly collaborate in Egnyte receive equivalent sharing permissions in Office 365 for free.

### Data ownership

You must consider data ownership. If a user has only shared data, and absolutely no owned data, we transfer no files from Egnyte to Office 365 for that particular individual.

Definitions:

- **Shared data** are files and folders that are not owned by the user. When permissions are applied in Office 365 after transfering, folders are shared again with the appropriate users.
- **Owned data** are files and folders that are owned by the user. Data almost always needs to have an owner within your organization. This is the only data that we actually transfer.
- **Ownership** is typically determined by who created the file or folder, but in some cases it can depend on the owner or creator of the parent (upper or top-level) folder.

## Data distribution

Determining the distribution of data across the user base is an extremely important component of a migration because we copy data in a highly parallel manner, and our servers transfer data as fast as each cloud storage provider can handle. Both Egnyte and Office 365 have rate limits for how fast data can be downloaded and uploaded.

The more users simultaneously being transfered, the higher our throughput for your migration. **We highly recommend that users with very large data sets be broken into smaller accounts to facilitate faster transfers.**

>[!Note]
>To maximize throughput, users should not own greater than 5TB of data. The more users you have, and the smaller the amounts of data they own, the faster your migration goes.

For example:

- If one user owns 10 TB of data, we recommend dividing that between 10 users so that each one owns 1 TB.

If data cannot be broken up, this should not hinder other users from migrating. As a general rule, users with a lot of data require a lot of time to migrate.

### Amount of data to move

Knowing the total volume of data you are moving helps to create a more realistic timeline for your migration.

### Your migration team

Establish a migration team to lead your organization through the project. The team's role includes liaising with us, undergoing training, and notifying employees of each change during the migration process.

An IT Manager or the Head of IT is a good choice for our point of contact because they understand the ins and outs of your organization's systems. To ensure a smooth, successful migration, we work closely together and be with you every step of the way.

## Timelines

### Be realistic

The amount of time required to plan, execute, and wrap up a migration depends on many factors. Organizational requirements, budget, security reviews, and support from management are just a few.

We typically see corporate transfers take a minimum of 30 days to plan and execute. Ensure you allot yourself enough time for each stage, which we cover later on in this guide.

### Evaluate your user base

It is critical that you plan which users are migrating and when. Ask yourself questions like these:

- *Is the entire organization migrating, or just a few users?*
- *Is everyone migrating at once, or are you splitting them into batches like department, office, or region? If so, why?*

>[!Note]
>Batching migrations this way increases complication and may extend your migration.

We recommend migrating during a slower organizational period, such as the weekend, to avoid work interruptions.

### Keep your accounts active

When migrating from Egnyte to Office 365, you need to ensure all your users are active and accessible. Knowing exactly when your Egnyte may shut down or expire is key to safely planning enough time to migrate.

### Consider migration speed factors

We're the fastest way to migrate your data, but the speed of your migration may still be affected by bottlenecks. Speed bottlenecks include, but aren't limited to, the following:

- Number of files and folders being moved
  - This is objectively the biggest speed limit on the Internet, as it determines the total number of operations required. Most providers rate limit their ingress to 1 file per second per user. This isn't universally true, but it's a baseline conservative metric you can use when estimating.
  - Our observable average across our customers is a 2.4 MB average file size.
  - Knowing file size is necessary to estimate transfer speed. If you are not able to determine exact numbers, most services can provide reports that illustrate individual or average file size.
- Total amount of data being moved
  - Total data can affect speed, but it is ultimately overshadowed by the number of files.
- Server connections with the source or destination **Connector**.
- Complexity of permissions or sharing schemes (if applicable).

What may be surprising is how large of an impact factors other than the size of the data you are moving can have.

For example, it is common for there to be half a second of overhead per file being moved. If you are moving 200,000 files, this would be 200,000 seconds or more than two days' worth of overhead alone!

Suffice to say, we cannot give you exact estimates on time because there are too many factors at play at any given point. By the time you have read this section, we could have easily copied several files totalling many GB, or a few hundred files equaling a small amount of data.

We are always happy to have a conversation with you about estimates.

### Notify stakeholders about the migration

Your employees have different needs with respect to their data, and it is paramount to know what those are. Take a shopping list of all departments, contact their managers, and identify key concerns in their processes and apps.

Keep in mind that while cloud storage is sometimes just a container for files, people might also be using it with third-party apps or for more advanced collaboration.

#### Example emails to send

**Subject**: ATTENTION: Decision to Migrate from Egnyte to Office 365

**Message**: A few months ago, management decided we will be leaving Egnyte and transition to Office 365. In Office 365, all employees will have access to cloud storage and its included apps.

We manage the migration to ensure all of our data gets transfered securely and efficiently. Let me know if you have any questions or concerns about the process.
</br>

**Subject**: ATTENTION: Important Info Regarding Cloud Data Migration

**Message**: As you know from prior emails, we are moving from Egnyte to Office 365 as our cloud storage provider.

To assist in this migration, we ask all employees to finish working and upload any last changes to files in Egnyte by 17:00 PT on Friday, April 7, 2020. Changes to files or data in Egnyte after this time are not moved.

On Monday, April 10, 2020, all employees will be using Office 365.

Questions and concerns can be directed to your immediate manager and/or our technical support staff via the usual channels.

## Connectors

### What is a connector?

A **Connector** is what we call our link to your cloud storage accounts.

To set up a transfer, you must grant us access to your cloud storage accounts. Without this link, we are unable to communicate with them.

Creating a **Connector** may involve authenticating via OAuth or with normal username/password credentials. You only need to authenticate once per account.

Our authorization is lost when you delete the **Connector**, delete your account with us, or revoke our access through your cloud service's security settings.

### Which connector to use for each Microsoft Service

|**Microsoft service**|**Which Mover connector to use**|
|:-----|:-----|
|Azure Blob Storage|Azure Blob Storage Connector|
|OneDrive Consumer|    OneDrive Consumer Connector|
|OneDrive for Business (Administrator)|    Office 365 Connector|
|OneDrive for Business (User)|    OneDrive for Business (User) Connector|
|SharePoint Online|Office 365 Connector|

## Deleting connectors

Deleting a **Connector** revokes our access to your cloud storage accounts. To confirm that we have been deauthorized, visit the security settings in your respective cloud service and check for our app.

Using our app to remove our authorization with a particular cloud service is simple:

1. From the **Transfer Wizard**, and for the **Connector** type you want to delete, select **Manage ▼**.
2. To the right of **Connect**, select arrow ▼.
3. Select **Delete**.
4. Confirm you want to delete, and you're done!

![Delete connector](media/delete-connector.png)

>[!Note]
>Deleting a **Connector** is permanent and cannot be reversed. The **Connector** type disappears from the **Transfer Wizard**. To add a new **Connector**, select **Authorize New Connector**.

### Reauthorizing connectors

Reauthorizing a **Connector** is sometimes necessary if we lose authorization or access to your cloud storage accounts or web servers. It is also a good first step in trying to resolve most issues with your **Connectors**.

The process to authorize a Connector again is very simple:

1. Find the **Connector** type you want to reauthorize.
2. Select **Manage ▼**.
3. For other **Connector** options, next to **Connect**, select ▼.
4. Select **Reauthorize**.
5. Follow the same steps you performed when you first created the **Connector** to renew the authorization tokens/permissions.

>[!Note]
>You are unable to change the display name of the **Connector**. If you want to rename it, you must delete and re-add the **Connector**.

**Connectors** are deauthorized automatically if they haven't transfered any data in the last 90 days. If you try to load a deauthorized **Connector** in the **Transfer Wizard**, an error message appears, along with a prompt to reauthorize the **Connector**.

## Migration FAQ

### What gets transfered?

Only owned folders and the root files for each user are copied. If a user is not the owner of data they can access, we do not copy it. Content may be automatically re-shared after it is migrated so that each user has access to their content exactly as before.

### Does Mover sync files?

Our app offers a source-to-destination delta—when you run a transfer, we compare the destination directory to the source, and only transfer new or modified files over. We call this our incremental feature.

We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on.

Here are a few examples of how we deal with changes to files and folders.

**Content changes**: If a document is edited in your source or you have added a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing file(s) in the destination.

**Name changes**: If the name of a file or folder changes in Egnyte, we treat it as a brand new object. This can lead to duplicate files being migrated to Office 365, or worse: entire folders worth of data being duplicated from the changed folder downwards.

**Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.

### Does Mover delete files?

We never delete your data from any source. Our app simply takes your data from one place and copies it to another—akin to *copy and paste* rather than *cut and paste.* We also don't retain any of your cloud storage data for any reasons.

We strive to keep your users' experience as similar as possible between Egynte and Office 365.

### How are permissions affected?

When moving from Egnyte to Office 365, user roles *on folders* change.

During a migration, we do not explicitly set a user as an owner of data.

In Office 365, ownership of files and folders is always implicitly set by virtue of copying data into a user.

#### Translating permissions

![Translating Egnyte permissions](media/old-egynte-role-new.png)

>[!Note]
>Our app only sets permissions on folders.

### Can I rearrange content during a migration?

Not recommended. Any major changes in directory structure should happen before or after your migration. It is also not a good idea to use our app to rearrange content.

The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is re-transfered including all subfolders.

When sharing permissions are transfered, both owners and collaborators receive duplicate data if content has been rearranged or renamed.

### What happens to external-sharing links?

Our app does not recreate external-sharing links. After migration, these have to be set in the destination manually.

### What about external collaborators?

We do not share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external users.

### Does Mover preserve file versions?

We do not preserve file versions. During a migration, only the most recent version of a file is transfered from Egnyte to Office 365.

### Does Mover notify users?

We automatically suppress all emails to users so they are not bombarded with excessive notifications about the data they now have access to.

## Account FAQ

### How do I reset my password?

**From the sign in screen**

To change your account password from the login screen, follow these steps.

1. Select **Forgot password**.
2. On the next screen, enter your account email, and select **Reset Password**.
3. Follow the steps we send to your account email and you're done!

**From your account panel**

If you are already logged in to our app, you can change your password there too.

1. Log in. To visit your **Account** settings (**shortcut**), in the top right corner of our app, select **account email**.
2. From the left-hand menu, select **Password**.
3. Select **Reset Password**.
4. Follow the steps we send to your account email and you're done!

![reset password](media/reset_password.png)

### How do I enable multi-factor authentication?

To enable multi-factor authentication, follow these steps.

1. Log in. To visit your **Account** settings (**shortcut**), in the top right corner of our app, and select your account email.
2. From the left-hand menu, select **Password**.
3. Under **Enable 2-Step Verification**, select **TURN ON**.

![2 factor screen](media/2_factor_screen.png)

>[!Note]
>You are automatically signed out of your account.

4. Log in to your email, and copy the verification code sent to you. If a verification code email does not appear in your inbox [or spam], just below the verification window in our app sign-in, select **Didn't get the code? Resend now**.

![verification code](media/verification_code.png)

5. Enter the **Verification Code**. You now have 2-Step verification enabled.

![activate 2 factor](media/activate_2_factor.png)

6. To turn off 2-Step verification, return to the **Password** tab, and under Enable 2-Step Verification, select **TURN OFF**.

![Disable 2 factor](media/disable_2_factor.png)

### How do I delete my account?

Deleting your account deletes all your scheduled transfers, multi-user migrations, and authorized connectors.

To close your account, follow these steps.

1. Log in. To visit your **Account** settings (**shortcut**), in the top right corner of our app, select **account email**.
2. On the left hand side, select **Leave Mover**.
3. Read all of the text on that page.
4. If you are ready, enter your current password, and select **Delete Account**.
5. A prompt appears. Select **OK**.

To reiterate:

**Deleting your account:**

- Deletes all scheduled transfers.
- Deletes all connector authorizations.
- Deletes any subscriptions associated with your account.
- Deletes your Mover account.


**This does not:**

- Delete your transfer history. We retain these for security and compliance.
- Remove any trace that your account once existed with Mover.

>[!Important]
>Deleting your account is **not** reversible.

![delete account](media/delete_account.png)

### How do I edit my email notifications?

By default, you receive an email every time a transfer is completed. To edit your email notification settings:

1. Log in. To visit the account settings, in the top right of our app, select your email address.
2. Select **Preferences**.
3. You have the option to receive emails **On Completion** (default), **Never**, or **Only on Errors**.

### Can I change my account email?

Unfortunately at this time, we do not allow you to change the email associated with your account.

You may, however, delete your account — losing the schedules, connector authorizations, and transfer history associated with it — and create a new account with the email you would prefer.

### How do I check my transfer usage?

Checking your usage of our app lets you know the total amount of gigabytes you have transfered over the history of your account.

To check your transfer data usage, follow these steps.

1. Log in. To visit your **Account** settings, in the top right corner of our app, select **account email**.
2. By default, you are already in the **Plan** section.

## Egnyte FAQ

### What is different about Egnyte?

Unlike other cloud storage providers, Egnyte has a `Shared` folder and a `Private` folder. When migrating from Egnyte, our app defaults to the **Private** folders when auto-completing the user to user migration setup.

### How will my paths look when Egnyte is my source?

During the migration setup (described later in this guide), you can edit the path(s) to specify where in Egnyte you want the data to go. From the root level of Egnyte, you can go into `/Private` which lists the individual users and their data, or `/Shared` which is the main shared data repository.

Most cloud storage providers, Egynte, for example, start the listing with a user such as `/user@example.com/marketing data`. Egnyte does not do this, so you would be looking at a path such as `/Shared/marketing data` if it's a Shared folder, or `/Private/example/marketing data` if it's a Private folder.

## Office 365 FAQ

### Will there be unsupported files and characters?

We automatically process file and folder names to ensure they are accepted by Office 365:

- Files larger than `15 GB` are not migrated.
- Files with a size of `0 bytes` (zero-byte files) are not migrated.
- The following characters in file or folder names are removed:
`" * : < > ? / \ |`
- Leading tildes (`~`) are removed.
- Leading or trailing whitespace is removed.
- Leading or trailing periods (`.`) are removed.
- See all invalid file or folder names and other Office 365 limitations **here**.

In some possible circumstances with older sites, any file or folder ending in `_files` could fail. If you experience these errors, contact Support.

Microsoft currently has no file type limitations, meaning you can upload data with any file extension. For more info, see **here**.

#### Character limits for files and folders

Filenames can have up to 256 characters.
Folder names may have up to 250 characters.
Total path length for folder and filename combinations can have up to 400 characters. For more info, see **below**.

### What happens to long paths?

During a pre-scan, our app automatically detects and reports paths that are too long for OneDrive or SharePoint to accept. The current path length limit for Office 365 is 400 characters. The path length is calculated when going in to Office 365 and includes your tenant URL, user site, path, and any character encoding.

**Example**:

This path is 93 characters long despite *Documents/Old Docs* being only 18 characters:</br>

https://example-my.sharepoint.com /personal /example_user /%2FDocuments%2FOld%20Docs</br>

If a file exists that has a very long path, our app skips it, and reports it in your log files.

To save time and headaches, before you migrate, you are encouraged to shorten any identified long paths.

![Turn this into this](media/egynte-turn-this-into-this.png)

### Are timestamps preserved?

The original timestamps from Egynte are preserved when migrating into Office 365.

>[!Note]
>Timestamps are only applied to files/data transfered, and not folders. Folders and folder structure are created in the destination during migration, and reflect the date of the migration.

### Is file authorship preserved?

When migrating from Egnyte into Office 365, the *modified by* author is preserved. However, the *created by* is changed to the user.

### Does the Mover app interact with the sync client in OneDrive for Business?

We do not interact with the sync client in **OneDrive for Business**. Before a migration, We recommend disabling it. If you use it during a migration, it tries to sync all the migrating data.

### What happens to shared data?

Data shared with a user by another user appears in the **Shared with me** folder. Data owned by a user appears in the user's designated destination folder.

### What about notifications?

To prevent users from being spammed, the Mover app silences notifications during the migration.

### What happens to data shared to Office 365 Groups?

Data shared to an Office 365 Group does not appear in the **Shared with me** section. Microsoft also does not notify users that they are now a member of an Office 365 Group.

>[!Note]
>This is a limitation of Office 365 Groups and cannot be changed on our end. The user must navigate to the appropriate group within either their Outlook Desktop Client, or by logging into their prefered email through **outlook.office.com**.

After the user has logged in:

1. Navigate to the left hand menu.
2. Scroll down the folder listings to **Groups**. If the available groups are not visible, to open the group directory, select the small arrow beside the **Groups** listing.
3. Select the desired group.
From here, the left-hand menu should change, enabling you to open and edit **Files/Notes** within the selected Office 365 Group.

### What SharePoint site formats are supported?

Both Modern and Classic sites are supported, and appear the same in our app.

### What will my file paths look like in SharePoint?

During the migration setup (described later in this guide), you can edit the path(s) to specify where in SharePoint you would like your data to go. From the root level of SharePoint Online, you can go into **Site Collections**, and inside each **Site Collection**, directories for **Site Contents** and **Subsites** appear.

**Site Contents** takes you to document libraries (for example, the **Documents** section), whereas **Subsites** takes you to the **Subsites** of that site collection. Navigating **Subsites** takes you through the same dichotomy.

Most cloud storage providers, G Suite Drive for example, start the listing with a user such as `/user@example.com/Marketing Folder`. SharePoint Online does not do this, so you would be looking at a path such as `/Marketing/Site Contents/Documents`.

![File paths in SPO](media/filepaths-in-sp.png)

### How does library permissions inheritance affect migration?

To set specific permissions on folders in a document library, inheritance must be disabled. Permissions inheritance is typically turned on by default, which makes all the data within the library subject to the permissions set on the library. This is similar behavior to team folders or team drives in other cloud services, whereby if users have access to the root level, they have access to everything contained within.

If inheritance is not disabled at the root, any permissions we try to set on individual folders are overridden by the library access permissions.

**To disable inheritance:**

In the Library settings, visit **Permissions for this document library**:

1. Select **Stop Inheriting Permissions**. This enables you to select the permissions you would like to remove:
   - Site members
   - Site visitors
2. Select **Remove User Permissions**.

This prevents site members/visitors from inheriting permissions to all the data that we migrate into that library, while allowing permissions to only those site members who we explicitly write to the folders themselves.

For more info about SharePoint Online permissions inheritance, see **here**.

### Does Mover support Microsoft Teams?

Microsoft Teams appears and operates the same as a SharePoint Online site.

### What is the item limit for SharePoint Online?

Many sites claim that SharePoint has a 5,000-item limit. This is not true. The SharePoint 5,000-item limit applies to how many items appear in a search list view: a maximum of 5,000.

SharePoint sites do have file size and number limits, which are covered in detail here: **SharePoint Online limits**.

Some list view options may prevent search list views with more than 5,000 items from appearing.

## Setting up the migration

### Authorizing Egnyte (Multi-User)

Authorizing **Egnyte** as an administrator is straightforward. To authorize or add a Multi-User Egnyte account as a connector, follow these steps.

>[!IMPORTANT]
>You MUST be an Administrator. A non-administrator does not work.

1. In the **Transfer Wizard**, select **Authorize New Connector**.</br>

![Clear auth](media/clear_auth.png)

2. In the **Connector** list, find **Egnyte**.
3. Select **Authorize**.

![Egnyte connector list auth](media/egnyte_connector_list_auth.png)

4. A new window (tab) opens. Name your Connector <optional>.</br>

5. Provide the Egnyte domain, for example, if your Egnyte domain is companyname.egnyte.com, enter "companyname".

![Name connector Egnyte](media/name-connector-egnyte.png)

6. Select **Authorize**.

7. If you are not already logged in, you can use either your Egnyte credentials or an SSO account.

![Log into grant access to Egynte](media/log-in-to-grant-access-to-egnyte.png)

8. To grant our app access to your Egnyte Account, select **Allow Access**.

![Grant access to Egnyte](media/grant-access-to-egnyte.png)

### Egnyte permission requirements

Our app requires an **Administrator** for authorization. The following table lists the scopes we require:

|**Permission**|**(Details) Allows our app to...**|
|:-----|:-----|
|Create and manage bookmarks    |Access and migrate bookmark data.|
|View and manage folder permissions|Access and create folder permission.|
|View and manage groups|View all groups under in the available Egnyte Directory.|
|View and manage users|View, edit, and manage users under the available Egnyte Directory.|
|Generate audit reports    |Generate and view reports available in the Egnyte Report Center.|
|Create and manage links|Create and manage internal links.|
|Read and write all files and folders|View, edit, copy and paste all data from within the Egnyte-available Directories.|

### Authorizing Office 365

>[!Warning]
>To fully authorize the **Office 365 Connector**, a Global Admin is required to grant permissions to the Office 365 Mover app within the Azure portal.
>
>The Global Admin must grant these permissions *after* the **Office 365 Connector** is authorized within the main Mover app.

To complete the authorization steps in the right order, see the following instructions.

A Global Admin or an SPO Admin can complete some steps in the authorization process. At the beginning of each step, we indicate who can complete it.

1. **Global Admin or SPO Admin**: Via app.mover.io, log into the main Mover app. In the **Transfer Wizard**, select **Authorize New Connector**.

>[!Note]
>Whether the **Office 365 Connector** is your source or destination connector (or both), you must complete this authorization process.

![Authorize new connector]( media/05-authorize-new-connector.png)

2. **Global Admin or SPO Admin**: In the **Connector** list, find **Office 365**, and select **Authorize**.

![Authorize O365](media/authorize-o365.png)

3. **Global Admin or SPO Admin**: A window with an **Authorize** button appears. It prompts you to give your Office 365 Connector a display name <optional>. Select **Authorize**.

![Authorize window](media/authorize-window.png)

4. **Global Admin or SPO Admin**: Follow the on-screen instructions. You are redirected to a Microsoft login screen where you can log in with your Microsoft admin privileges, and continue to authorize the connector.


>[!Warning]
>If you are a **Global Admin**, a slightly different login screen will display.  
>
>**DO NOT** select the option **Consent on behalf of your organization**. This option **must** remain unselected.

- ![global admin o365](media/permissions-o365-global-admin.png)



5. **Global Admin or SPO Admin**: After authorizing the connector, you are redirected to the **Mover Transfer Wizard**, and an error aapears, like the following. This means it is now time for a Global Admin in your tenant to grant permissions to the Office 365 Mover app in the Azure portal.

If you're an **SPO Admin**: To grant permissions and finish the authorization process (Steps 6 – 9), point your Global Admin to **aka.ms/office365moverauth**.

If you're a **Global Admin**: Continue with Steps 6–9.

![authorize error](media/authorize-error.png)

6. **Global Admin**: Log into the Azure Portal via **aka.ms/office365moverauth**. A list of **Enterprise applications** appears.

![Enterprise applications](media/enterprise-applications.png)

7. **Global Admin**: Find and select the **Office 365 Mover** app. A page appears that provides an overview of our app.

![O365 Mover app](media/o365-mover-app.png)

8. **Global Admin**: In the left menu, find and open **Permissions**. Select **Grant admin consent for Mover**.

![o365 mover permissions](media/o365-mover-permissions.png)

9. **Global Admin**: A pop-up window appears that guides you through the rest of the permissions process. When complete, it closes automatically, and your **Office 365 Connector** is fully authorized and ready to go.

### Troubleshooting an Office 365 connector

#### App access error

If you encounter an error on authorization, try signing out of any Microsoft accounts, and attempt to authorize the **Connector** in an Incognito Window.

#### Global Admin account provisioning

Your Global Admin user must have an Office 365 account provisioned to administer other Office 365 accounts. If you create a service account for our app, ensure you also assigned an Office 365 license, and walked through the Office 365 setup process.

#### User provisioning

Are your Office 365 users provisioned? All Office 365 users must log in to their Office 365, and open Office 365 for us to transfer into their accounts. You can also provision Office 365 accounts via Windows PowerShell using the following commands (replace your URL and email appropriately)::

`Connect-SPOService -Url https://example-admin.sharepoint.com -credential user@example.com`

`Request-SPOPersonalSite -UserEmails "neverloggedintest@example.onmicrosoft.com"`

#### Office 365 permission requirements

Our app requires a Global Administrator for authorization. The following table lists the scopes we require.

|**Permission**|**(Details) Allows our app to...**|
|:-----|:-----|
|Create, edit, and delete items and lists in all your site collections|Create or delete document libraries and lists in all site collections on your behalf.|
|View your basic profile|See your basic profile (name, picture, user name).|
|Maintain access to data you have given it access to|See and update the data you gave it access to, even when you are not currently using our app. This does not give our app any additional permissions.|

### Connecting your source Egnyte account

If you are not already connected after you have authorized your source, select **Egnyte**, and load the connector. An icon appears, and show you how many users you are migrating.

![execution select gdrive source](media/execution-select-egnyte-source.png)

### Connecting your destination Office 365 account

If you are not already connected after you have authorized your destination, select **Office 365**, and load the connector. An icon appears and show you how many users you are migrating.

![execution select o365 destination](media/execution-select-office-365-destination.png)

#### Creating a new migration

Select **Continue Migration Setup**, and our app moves to the **Migration Manager**.

![create migration](media/create-migration.png)

The next step is to create a user list of who is transfering.

From your newly created migration in the **Migration Manager**, there are two ways to add users:

- Select **Add Users**.

![add users](media/add-users.png)

- Or, select **Migration Actions**, then select **Add to Migration**.

![migration users](media/migration-users.png)

Select one of two options:

1. Auto Discover Users.
  - For our app to automatically find your users and attempt to match them up, select **Automatically Discover and Add Users**.

2. Upload Migration CSV File.
  - To add a customized CSV file for your migration, either drag a file into the designated space, or select **Choose a file to upload**.

![Add users menu](media/add-users-menu.png)

>[!Note]
>You still get to finalize your migration before any data moves!

#### Creating a new migration from a CSV (optional)

Occasionally, you have thousands of users and a complicated directory schema that you want to import. In these cases, it's desirable to plan out your migration in a spreadsheet.

In these cases, we trust the CSV upload option is useful. This allows you to lay out all your users and directories, and then provide it to us in a .csv format for us to create your migration.

##### Users to migrate

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

#### Creating your CSV in Excel

To use an Excel spreadsheet to create your CSV:

1. Ensure you have two columns, one titled `Source Path`, and one `Destination Path`.
2. List the relative paths, domains, and usernames on the subsequent rows.
3. Export your spreadsheet as a CSV:
  a. Select **File**.
  b. Select **Save As**.
  c. From the **File Format** options, select **CSV**.

#### Reviewing your users

##### Checking paths

Confirm that the users in the Egnyte source match the users in the Office 365 destination. Usually the emails/usernames match up, but it depends how you structure and name your users. *Be diligent during this step!*

#### Editing

Be aware that Users can only be edited if they haven't been scanned, or had a transfer run.

To edit a user source entry:

1. To select a User row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the source path.
3. A new side panel opens, enabling you to edit the Egnyte source path.
4. To select your parent source path, double-click it, and to complete your edit, select **Save**.

![edit source user](media/edit-source-user.png)

To edit a user destination entry:

1. To select a user row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the destination path.
3. A new side panel opens, enabling you to edit the Office 365 destination path.
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

![Add id customize column](media/add-id-customize-column.png)

4. After you've created your CSV file using these instructions and format, you can drag and drop the file into our app, or select **Choose a file to upload**. Changes to your user pairings are implemented immediately.

![update migration](media/update-migration.png)

#### Adding

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

#### Duplicating

At any time, you may duplicate a user in the **Migration Manager** list. To duplicate a user entry:

1. To choose a user row, on the left side of a row, select the respective checkbox. You may select more than one entry at a time.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row you want to duplicate.
3. In the context menu, select **Duplicate # User**.
4. Select **OK**.</br>

A new user entry appears. From here, you can change the directory, schedule, or even the entire user.

![duplicate user](media/duplicate-user.png)

#### Scheduling

You can set an hourly, daily, weekly, or monthly schedule for each user, even after they have been run.

To create or edit a schedule:

1. Select the user pairing(s) you want to schedule.
2. Select the **User Actions** dropdown menu.
3. Select **Schedule # Users**.
4. Configure your Hourly, Daily, Weekly, or Monthly setup, including the timing and day of the week (where applicable).
5. Select **Apply Schedules to X Users**.

##### Deleting

Be aware that users can only be deleted if they haven't been scanned, or had a transfer run.

To delete a user entry:

1. To choose a user row, on the left side of a row, select the respective checkbox. You can select more than one entry at a time.
2. On the right and directly above the user rows, select **User Actions**, or right-click the user row you want to delete.
3. In the context menu, select **Delete User**.

>[!Important]
>This is permanent and cannot be undone unless you create a new entry.

![delete user](media/delete-user.png)

### Reviewing your permission map

The permission map is a critical part of your migration.

When a user is migrated, we transfer files and folders and share any required data. We already know who is copying data, but we also need to know who might have content shared with them, even if they don't copy data.

To stay organized, we provide a secondary list of your users, called a permission map. This list includes everyone who could possibly receive sharing permissions to any files or folders that might be migrated. This even includes users who are not migrating data.

Another important consideration is that usernames and emails aren't always consistent across platforms, and the permission map helps us line up everyone.

**Example**:  `jane@example.com` is actually `j.smith@example.com`

We automatically detect users and handle perfect matches. Any inconsistencies must be manually reconciled. The permission map can be continually updated, because with each incremental pass of the migration, permissions are reapplied.

1. To view your permission map, in the top right of the **Migration Manager**, select **Migration Actions**, and then, from the dropdown menu, select **Edit Permission Map**.

![edit permission map](media/edit-permission-map.png)

You may either auto-discover or upload a permission map file. We automatically pair perfect matches. If a user or group in Egnyte does not have a perfect match in Office 365, you can correct it in our interface.

2. Select **Auto-discover Users**.

![permission map auto discover users](media/permission-map-auto-discover-users.png)

3. At any time, you may view and edit your permission map.

![permission map](media/permission-map.png)

>[!Note]
>A blank destination entry automatically cancels any permission sharing for that user or group.
>
>[!Note]
>Adding a new line for a specific users - for example, user01@gmail.com to user01@hotmail.com - that perfectly matches auto-discovered permissions by the domain - for example, `@gmail.com` to `@hotmail.com` - is automatically removed. Our app marks these as redundant entries.

### Uploading a permission map (optional)

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

#### Exporting a permission map

You can export a permission map in CSV format.

1. Select **File**.
2. Select **Save As**.
3. From the **File Format** options, select **CSV**.

![excel save as csv](media/excel-save-as-csv.png)

### Migration Manager overview

The **Migration Manager** is the key part of our app. It is the primary screen for interacting during the data migration process.

![migration main mover](media/migration-main-mover.png)

#### Migration Manager dashboard

Use the **Migration Manager** dashboard for a summary of your overall migration. This is covered in depth **here**.

#### Main menu bar

Use our app's main navigation bar to switch between the **Migration Manager**, **Transfer Wizard**, and your **Account** details, as well as contact support if you run into any issues during your migration.

![migration top mover](media/migration-top-mover.png)

#### Migration selection

Use the **Migration Selection** bar to navigate between separate multi-user migrations, as well as individual normal transfers.

Here, you are also able to edit and personalize the names of each multi-user migration.

![migration edit mover](media/migration-edit-mover.png)

#### Migration actions

Use the **Migration Actions** menu to access things such as: the migration reports, the columns displayed, and the overall layout of your migration to best suit your personal needs.

![migration action mover](media/migration-action-mover.png)

#### Filters

Use the **Active Filters** bar to search your migration for specific key terms or custom tags you have applied.

![migration filter](media/migration-filter.gif)

You can also view more in-depth instructions by selecting the info button directly to the right of the **Active Filters** search bar, or by viewing the **Active Filter** list.

![migration filter info](media/migration-filter-info.png)

#### User display

The user display is the central focus of the **Migration Manager**, and displays all the users in the current migration.

This section of our app provides you with a column-by-column breakdown of each individual user in a migration. Here, you can also duplicate and edit source/destination paths of a user, as well as view the logs of any scanned or completed transfers.

![migration users mover](media/migration-users-mover.png)

#### User actions and finalization

This area of the screen contains the **User Actions** dropdown menu, the **Scan User** and **Start Migrating Users** buttons.

![migration final mover](media/migration-final-mover.png)

**User Actions** opens a new dropdown menu enabling you to interact with a selected transfer.

![migration actions mover](media/migration-actions-mover.png)

**Scan # Users** performs a scan of the selected users. This helps identify any problematic files, folders, or connectors.

**Start # Migrating Users** opens a side tab enabling you to finalize and begin the migration.

![migration actions mover](media/migration-finalize-mover.png)

## Running the migration

### Scanning

Scanning your source data is key to running a smooth and stress-free migration. For the full list of key data necessary for a smooth migration, see this **checklist**.

>[!Note]
>Scanned data is marked as *Skipped* as scanning does not transfer data; it simply counts the data that we would normally transfer from the source.
>
>After a transfer is scanned, the source/destination are effectively *locked in.* Be sure to double-check that they are correct, and not left blank.

### Running the scan

You now have a list of users appearing in the migration, complete with destination set up.

To start the scanning source data process:

- Select all user(s). At the top of navigation bar, select the checkbox.

After you select all users, select **Scan X Users**.

![scan users](media/scan-users.png)

After the scan has successfully completed, the users appear in green. The scan time varies depending on the data amount in the source.

After users appear in green, yellow, or red, on the top right side of your screen, select **Migration Actions**, and then select **Scan Report**.

>[!Note]
>If your scan encounters an error or crashes, our app automatically reruns the scan up to three times to attempt to resolve the issue.

![scan report migration](media/scan-report-migration.png)

The **Scan Report** is covered in-depth in the **Reports** subsection under the **Scan Report** section of this guide.

#### Migrating users

We recommend starting slow. Test one user, then three to five. If it looks good, and you see data being downloaded and uploaded, start queuing everyone and stage the rest of your users.

1. To select a user(s), check their row's respective checkbox.
2. Select **Start Migrating X Users.**
3. Review your migration summary. This informs you which user is being copied, where they are transfering from, and where to, as well as when the transfer will begin.
4. Review and agree to our terms and conditions, and then select **Continue**. Your users are immediately queued for migration.

![start migration](media/start_migration.png)

>[!Note]
>If your transfer encounters an error or crashes, our app automatically reruns the transfer up to three times to attempt to resolve the issue.

#### Canceling users

To cancel a currently running transfer:

1. Find the transfer(s) you want to cancel, and select them. A running transfer is in blue and have a status of **Running** or **Queued**.
2. For multiple users, select the **User Actions** dropdown, or right-click on a single user.
3. Select ***Cancel X Transfers**.

This action stops the transfer as soon as possible (usually within a few seconds).

#### Rerunning users

The best way to resolve any issues with a transfer is to rerun it. This action checks over all the files in your destination, compares them to the source, and then transfers over the new or modified files.

All transfers take advantage of our incremental feature, and only transfer new or modified data differences between Egnyte and Office 365.

As long as a transfer is not running, to restart a transfer, you can re-queue a user.

To rerun or restart your transfer, complete the following steps:

1. Select the or user(s) you want to rerun.
2. To run the users again, at the top right, select **Start Migrating X Users**.

### Transfer status messages

The following table lists additional info about each transfer status message from the **Migration Manager**.

|**Status message**|**Definition**|
|:-----|:-----|
|Running pre-checks|    Our servers checking a few things and sending your transfer to the queue. Almost there!|
|Queued to start, please be patient|    Your transfer will run as soon as possible. You can close your browser, and receive an email on completion. There is no limit to queued users.|
|Success. No files copied    |We have skipped all of your files without error, and have detected no new or modified files.|
|Success. Some unsupported files not transferred|    We have skipped all of your files without error, and have detected no new or modified files. Files unsupported by the source or destination were skipped over.|
|Some upload errors, please retry|    We were able to download everything from the source, or skip files that already existed in the destination, but some files didn't make it into the destination.|
|No files copied. Some upload errors, please retry    |We were able to download everything from the source, or skip files that already existed in the destination, but no files made it into the destination.|
|Some download errors, please retry|    We weren't able to download everything from the source, but some files made it into the destination successfully.|
|No files copied. Some download errors, please retry    |We weren't able to download anything from the source!|
|Some download and upload errors, please retry    |There were errors with both downloading and uploading files, although some incremental files may have been skipped successfully.|
|General failure, please retry|    We don't have a particular reason why your transfer failed - maybe we were having trouble connecting to your source or destination properly, for example.|
|Connector auth failed|    One of your connectors isn't authorized correctly.|
|Crashed, please retry|    We don't have a particular reason why your transfer failed, but generally this is due to server issues on our side or with the source or destination connectors. Contact us if you encounter a crash.|

## Post-migration troubleshooting

### General troubleshooting

Follow these steps if your migration is having issues:

1. Rerun users. Select one or more users and to rerun them, on the top right of the **Migration Manager**, select **Start Migrating**.
2. To view your most recent transfer log, select the user row you want to view. This action opens the **Transfer Logs** sidebar. From here, select the **View Log** button for the most recent transfer.

![view logs](media/view_logs.png)

Alternatively, you can select multiple users, and from the **User Actions** dropdown menu, you can download their most recent collective logs in a zip file that provides them in both HTML and CSV formats.

3. Check if your failed/unsupported files are too large to go into Office 365.
4. Ensure you have enough storage space in Office 365 to accommodate the data you're moving in.
5. Think files are missing? Check out our list of **Unsupported Files per Connector**.

### Incremental feature

Our incrementals are delta operations which compare files in your Office 365 to files in Office 365. Using this comparison, we copy anything that is new or has changed. This enables us to keep Office 365 data up to date when the very final cutover of users occurs. These incremental passes are an important part of our process.

**Technical clarification**: We compare what you have in Egnyte to what is in Office 365, and we only transfer anything that doesn't already exist, or has a newer timestamp.

### 'Lost files'

During a transition where sharing paradigms change, there are many users who claim, "My files are lost!"

This is common if they are not in clear communication about how the sharing structure changes when they log in to Office 365. This can be mitigated with a clear communication strategy.

### Waiting for Microsoft

After all your files have been uploaded to Microsoft, the status of the transfer changes from *Running* to *Waiting for Microsoft*. We must wait for Microsoft to complete their processing.

It is normal for this process to take a few hours, and ultimately depends on how much data there is to process.

### Document parser error

Large HTML or XML documents (256MB+) fail to transfer if the **Document Parser** is enabled for the destination site during the migration.

The following error appears:

`File too large for Microsoft Doc Parser. Please contact Microsoft support and request the Doc Parser be disabled for this site.`

If this error message appears, you must contact Microsoft support directly to disable the **Document Parser** on the target site for the duration of the migration.

If you require assistance with your communication strategy, ask us for help.

## Transfer logs

### Viewing your logs

Viewing your logs is an excellent way to troubleshoot transfer issues. They inform you about each action we performed on each file and folder. If we run into any problems, you receive an error message next to the file with a description about what happened.

During a migration, a file sometimes fails to download or upload. All failures are fully logged so you may address them.

>[!Note]
>We attempt to copy a file three times before considering it a failure. We only log a failure if we are unable to properly transfer it after three attempts.

You can view a user's transfer logs by doing one of the following:

1. Select the user row. This action opens the **Transfer Logs** sidebar. From here, select **View Log** on any previous transfer log for the selected user.

![view logs](media/view_logs.png)

>[!Note]
>To open a Transfer log in your web browser with built-in sorting and filter features, select **View Log**.

2. To select multiple users, from the **User Actions** dropdown menu or the **Actions** menu in the side tab, select **Download Logs (zip file)**. As the label implies, multiple log files are zipped together for download.

![multiple logs](media/multiple_logs.png)

>[!Note]
>The zipped file provides logs in both CSV and HTML formats for only the most recent transfer of each user.

View an example CSV log or in your browser:

[User log for DropboxAdmin to BoxAdmin transfer_ tRanSacTionID.html](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/User log for DropboxAdmin to BoxAdmin transfer_ tRanSacTionID.html)

### Interpreting a log file

- **Status**: Whether an action was a success or a failure.
- **Size**: File size in bytes, or that it's a folder being created/operated on.
- **Name**: File, folder, or action being acted upon.
- **Additional Info**: More info about the particular action performed. For more info, see the following table.

|**Message**|**Definition**|
|:-----|:-----|
|Failed to download file successfully    |An issue occured with the Source Connector.|
|Failed to upload file successfully    |An issue occured with the Destination Connector.|
|Unknown error of type 400    |A 'bad request' error. It could be a problem with the Source (File Download) or Destination (File Upload). Typically, this means that something has changed client-side or server-side and could be resolved the next time you run the transfer.|
|Unknown error of type 404    |This is a *server not found* error. Typically, this means that the Source (File Download) or Destination (File Upload) server is down or experiencing a temporary outage.|
|Auth failure: attempt to renew authentication successful|    Authorization is failing either on the Source (File Download) or Destination (File Upload) Connector.|
|Backoff used: #|    Generally seen after an action listed as 'throttle.' This means we've made too many requests of that Connector, and must wait before trying whatever action we were trying to complete again.|
|Folder Already Exists|    We attempted to create the folder, but we've already created it in a previous transfer, or it already exists in the destination.|
|Skipping because of incremental    |Not an error by definition; it's just our incremental process at work.|
|Scanned|    Not an error by definition; it's just our scanner counting your data.|

## Reports

### Dashboard overview

The dashboard statistics given at the top of the **Migration Manager** provide a visual summary of your overall migration. This includes the number of users in the current selected migration, the number of files scanned or transfered, and the amount of data scanned or transfered; as well as any issues, errors, or failures that may have occured.

![migration manager dash](media/migration-manager-dash.png)

#### Transfers

The **Transfers** section of the **Migration Manager** dashboard provides a brief rundown of all user transfers and scans.

- **New**: Number of individual users that have yet to be scanned or transfered.
- **Running**: Number of users that are currently running either a scan or a transfer.
- **Complete**: Number of users that have successfully completed scans or transfers.
- **Issues**: Number of users that encountered errors during a scan or a transfer.
- **Failures**: Number of users that failed to scan or transfer.

>[!Note]
>The total **Transfers** tally is from all users regardless of status.

![migration manager dash](media/migration-manager-transfers.png)

#### Files

The **Files** section of the **Migration Manager** dashboard provides a total of all files scanned and transfered across all users in a migration.

- **Complete**: Number of files that have successfully scanned or transfered.
- **Issues**: Number of files that have encountered issues and failed to scan or transfer.

>[!Note]
>The total number of **Files** is from both scanned and transfered users. Be aware that scanned files are marked as *Skipped* as they have yet to be transfered.

![migration manager files](media/migration-manager-files.png)

#### Data

The **Data** section of the **Migration Manager** dashboard shows the total of all data scanned and transfered across all users in a migration.

- **Complete**: Amount of data that has been successfully scanned and transfered.
- **Issues**: Amount of data that encountered issues and has failed to scan or transfer.

>[!Note]
>The total amount of **Data** is from both scanned and transfered users. Be aware that scanned data is marked as *Skipped* as it has yet to be transfered.

![migration manager data](media/migration-manager-data.png)

### Active filter list

This provides the list of all current **Filters** that you can apply to the **Active Filter** search bar.

>[!Note]
>Applying the filters changes the statistic shown in the **Migration Manager** dashboard.

|**Filter label**|**Label effect**|
|:-----|:-----|
|Status|    Filters by status [for example, Failed, Success, User Does Not Exist, and so on.]|
|Files|    Filters based on files transfered, failed, and skipped.|
|Data    |Filters based on data that has transfered, failed, or skipped.|
|Success|    Displays all successful Data and Files transfered.|
|Failed    |Displays all Data and Files that have failed to transfer.|
|Skipped    |Displays all data and files that were skipped.|
|Schedule    |Displays all users with scheduled transfers [for example, Hourly, Daily, Weekly, Monthly].|
|Path    |Filters for specific source or destination path [for example, path:username].|
|Destination|    Filters for specific destination path [for exaample, path:@domain<spam><spam>.com].|
|Source|    Filters for specific source path [for example, path:foldername].|
|Destination path    |Functions the same as **Destination**.|
|Source path    |Functions the same as **Source**.|
|Tags     |Lists transfers with previously implemented custom tags.|
|Notes    |Filters by keywords in previously implemented custom notes.|
|Code|    Filters for specific status codes.|
|Destination name|    Displays transfers with a specific destination name.|
|Source name|    Displays transfers with a specific source name.|

### Scan report

For more info about the scanning process, see the **Scanning** section.

After the scan report is downloaded and opened, look for these key items:

- Users with a failed status. We recommend rerunning the scan for these user(s).
- Users with one file or less. **Note**: Sharing permissions are still transfered.
- Users with the most data. Use this info to decide about a data distribution strategy that suits your needs. For more info about data distribution, see **here**.

![scan report example](media/scan-report-example.png)

### Migration report

The **Migration Report** provides an in-depth overview of your entire migration, including (but not limited to) speed and time statistics, totals for files and data transfered, and info relating to the latest run.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Report**.

The CSV report provides the following info for each user pairing.

|**Header/Statistic**|**Definition**|
|:-----|:-----|
|Schedule ID|    Our internal reference unique to the user pairing created.|
|Source|    Source directory path.|
|Destination    |Destination directory path.|
|Tags    |If you have used our tags feature, you'll see them here. Use tags to differentiate operational departments, to flag specific users, and so on.|
|Notes|    If you have added Notes to user pairings in the **Migration Manager**, they'll appear here, for example, *Remind me to check the logs on this user* or *Weird folder problem - ask support*.|
|First Run Start|    When the first transfer for this user pairing began.|
|Files Transfered    |Total files transfered.|
|MB Transfered    |Total data (MB) transfered.|
|Times run|    Total number of times this user pairing has been run.|
|Total Duration    |Total duration of each time this user pairing has been run.|
|Average File Velocity (files/hour)|    Files transfered, divided by the total duration.|
|Average Data Velocity (MB/hour)    |Data (MB) transfered, divided by the total duration.|
|Last Status|    Last status of the user pairing.  This is also reflected by the color of each row in the **Migration Manager**. Examples include *Success*, *Some Problems*, *Failure*.|
|Last Status Code|    Internal reference number refering to the last status of the user pairing.|
|Last Skipped|    Number of skipped files in the last run.|
|Last Files|    Number of files transfered in the last run.|
|Last MB    |Volume of data (MB) transfered in the last run.|
|Last MB Skipped    |Volume of data (MB) skipped in the last run.|
|Last Failed Files    |Number of files that failed to transfer in the last run.|
|Last Folders Listed    |Number of folders that we opened/created in the last run.|
|Last Folders Failed    |Number of folders that we failed to open/create in the last run.|
|Last Run Start    |When the latest transfer on this user pairing began.|
|Last Run End    |When the latest transfer on this user pairing finished.|
|Last Run Duration    |How long the latest transfer for this user pairing took to complete.|
|Last File Velocity (files/hour)    |Files transfered, divided by the total duration for the last run.|
|Last Data Velocity (MB/hour)|    Data (MB) transfered, divided by the total duration for the last run.|

Download an example CSV:

[example_migration_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_report.csv)

### Migration table report

The **Migration Table Report** generates an overview of your entire migration based on the custom designated columns you have set.

To edit report columns, in the **Migration Manager**, select **Migration Actions**, and select **Customize Columns**. Here you can set and reorganize which **Columns** you want to display when you download the CSV report.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Table Report**.

![migration table example](media/migration-table-example.png)

Download an example CSV:

[example_migration_table_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_table_report.csv)

### Migration error report

The **Migration Error Report** generates a simplified **Migration Report** that focuses on any problematic files, folders, permission errors, or general errors.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Error Report**.

![migration error example](media/migration_error_example.png)

Download an example CSV:

[example_migration_error_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_error_report.csv)

## Post-migration tips

We are stewards of your data. Our approach in all things is to see you successfully cross the finish line. We provide full service support and are ready to solve any problem and communicate with you about any issue.

### Communication

Follow up with users after migration to ensure they know where to access their data.
Provide a link to set up their new Office 365 accounts. Be prepared to answer any questions or concerns, as it is common for users to complain about a new system.

### Example email

**Subject**: ATTENTION: Login to Office 365*

**Message**: Over the weekend, we migrated our team from Egnyte to Office 365.

All files and folders were transfered without any issues. To set up your new Office 365 account, follow this link..

Your username remains the same; however, you must create a new password.

From this point forward, log into your Office 365 account rather than your old Egnyte account.

Let us know if you have any questions or concerns.

## User migration guides

This User Migration Guide is intended to be distributed to users via their migration management team. Feel free to customize messaging to best serve users.

For more info about your upcoming Office 365 migration, see the following sections.

### Timeline

- This migration happens behind the scenes. Your work day should not be interrupted.
- Files and folders are migrated. Any root folders or files you own in Egynte are copied.
- A final cutover is planned after all users in your group have been migrated.

### Dos and don'ts

**Do** continue working in Egynte as usual!

**Don't** start using Office 365 until you have been notified the final cutover is complete!

**Don't** make any major changes to file or folder names! Your files and folders are continually copied from Egynte to Office 365, but changes to file names or folders can result in duplicated data.

### Filenames

Files and folders are automatically processed to ensure they are compatible with Office 365.

### What happens to External Sharing links?

Our app does not recreate external sharing links. After migration, these must be set in the destination manually.

### Your migration team

If you need more help with Office 365, shortening paths, or just want to say thanks. e-mail <your end-user support email>.
