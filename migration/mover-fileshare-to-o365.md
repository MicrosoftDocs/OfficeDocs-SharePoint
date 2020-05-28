---
title: How to Migrate from On-premises file shares to Microsoft 365 
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
description: "How to Migrate from On-premises File Shares to Microsoft 365"
---
# How to migrate from on-premises file shares to Microsoft 365

## Introduction

Our purpose is to act as an intermediary between various web technologies that don't play nice together. We take your files from one place and copy them to another. No downloads and nothing to watch over—our web-hosted app does all the work!

Undertaking any corporate migration is a daunting task. When moving from File Servers to Microsoft 365, there are many things to consider. Our team has done this enough times to have learned a thing or two. We hope this guide helps you migrate successfully from File Servers to Microsoft 365.

If you experience any issues, do not hesitate to ask us questions!

>[!Tip]
> Need help? [Open a support request here](https://support.microsoft.com/en-us/supportforbusiness/productselection?sapId=c3fa6eba-e1f0-0715-4519-94a9740c5f2c)


### File processing summary

When we transfer a file, a temporary copy is downloaded from **File Servers** to a temporary server, and then uploaded to Microsoft 365. Upon successful upload, that file is deleted from the temporary server. When your migration is complete, that temporary server is eliminated. Any log data expires in 90 days and is never retained by us. We do not perform any actions beyond copying files and folders and sharing permissions. We never perform delete operations.

## Communicating with stakeholders

A migration is a significant undertaking for any organization. Trying to grasp the entire extent of all data and communicating with your employees is complicated. We sympathize!

Before, during, and after a migration, it is critically important to communicate clearly and effectively with your user base. We provide timely support and documentation to your transition team to help you communicate these changes with each stakeholder.

**Management** — Management needs succinct info about the how's and why's of the migration, such as costs, benefits, and expectations. You must paint a clear picture of what a successful migration should look like. Granular info is important when running a department.

For example, the Sales Manager needs to know how operations will be affected, such as *Can employees still work over the weekend if needed?*

**Users** — These are your bread-and-butter employees. They need to know when changes are taking place, and who to go to with questions or issues.

Key questions to address:

- Why are we migrating our data?
- How does it impact me?
- What are the benefits?
- How disruptive is this change going to be?

**Third parties** — If people outside your organization have access to collaborate on documents, this could potentially be interrupted and require resharing of data. We address best practices for this in this guide.

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

This scan is effectively a simulated dry-run migration, with no set destination which helps to identify any problematic files/folders before you begin migrating data.

>[!Note]
>The scan is available in the **Migration Manager** after you have first set up a migration.

Read through this guide to better understand the full migration process, or skip ahead to **Setting Up the Migration**. For detailed instructions about how to run the scan, see **Scanning.**

### Number of users to migrate

Each *user* is defined by a unique source and destination pairing.

For example:

- user01@example.com => user02@example.com
- user01@example.com => user03@example.com

These would be considered two separate *user licenses* because they have different destinations.

We also apply the term *user* to separate internal or external drives migrating to a single destination account.

For example:

- /C:\/Archive => user01@example.com
- /D:\/Sales => user01@example.com

These qualify as two separate *user licenses* because there are two separate sources going to the same destination.

Migrations are run on a per-user basis. Because of our app's scalable infrastructure, it is feasible to run dozens of users or thousands simultaneously. Any number of users can be migrated in whatever pre-defined order or grouping you desire.

**Collaborators-only**: Your fiscal budget need only include users that own data in File Servers. Anyone that strictly engages as a collaborator in File Servers (for example, they only share other users' content), do not have any data copied, and therefore do not incur a fee.

## Data distribution

Determining the distribution of data across the user base is an extremely important component of a migration because we copy data in a highly parallel manner, and our servers transfer data as fast as each cloud storage provider can handle. Both File Servers and Microsoft 365 have rate limits for how fast data can be downloaded and uploaded.

The more users simultaneously being transfered, the higher our throughput for your migration. **We highly recommend that users with very large data sets be broken into smaller accounts to facilitate faster transfers**.

>[!Note]
>To maximize throughput, users should not own greater than 5TB of data. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds.

For example:

- If one user owns 10 TB of data, we recommend dividing that between 10 users so that each one owns 1 TB.

If data cannot be broken up, this should not hinder other users from migrating. As a general rule, users with a lot of data require a lot of time to migrate.

### Amount of data to move

Knowing the total volume of data you are moving helps to create a more realistic timeline for your migration.

### Your migration team
Establish a migration team to lead your organization through the project. The team's role includes liaising with us, undergoing training, and notifying employees of each change during the migration process.

An IT Manager or the Head of IT is good choice for our point of contact because they understand the ins and outs of your organization's systems. To ensure a smooth, successful migration, we work closely together and are with you every step of the way.

## Timelines

### Be realistic

The amount of time required to plan, execute, and wrap up a migration depends on many factors. Organizational requirements, budget, security reviews, and support from management are just a few.

We typically see corporate transfers take a minimum of 30 days to plan and execute. Ensure you allot yourself enough time for each stage, which we cover later on in this guide.

### Evaluate your user base

It is critical that you plan which users are migrating and when. Ask yourself questions like these:

- *Is the entire organization migrating, or just a few users?*
- *Is everyone migrating at once, or are you splitting them into batches like department, office, or region? If so, why?*

>[!Note]
>Batching migrations this way increases potential for complications, and may extend your migration.

We recommend migrating during a slower organizational period, such as the weekend, to avoid work interruptions.

### Keep your accounts active

When migrating from File Servers to Microsoft 365, ensure all your users are active and accessible.

### Consider migration speed factors

We're the fastest way to migrate your data, but the speed of your migration may still be affected by bottlenecks. Speed bottlenecks include, but aren't limited to, the following:

- Number of files and folders being moved.
  - This is objectively the biggest speed limit on the Internet, as it determines the total number of operations required. Most providers rate limit their ingress to one file per second per user. This isn't universally true, but it's a baseline conservative metric you can use when estimating.
  - Our observable average across our customers is a 2.4 MB average file size.
  - Knowing file size is necessary to estimate transfer speed. If you are not able to determine exact numbers, most services can provide reports that illustrate individual or average file size.
- Total amount of data being moved.
  - Total data can affect speed, but it is ultimately overshadowed by the number of files.
- Server connections with the source or destination **Connector**.
- Complexity of permissions or sharing schemes, if applicable.

What may be surprising is how large of an impact factors other than the size of the data you are moving can have.

For example, it is common for there to be half a second of overhead per file being moved. If you are moving 200,000 files, this would be 200,000 seconds or more than two days' worth of overhead alone!

Suffice to say, we cannot give you exact estimates on time because there are too many factors at play at any given point. By the time you have read this section, we could have easily copied several files totaling many GB or a few hundred files equaling a small amount of data.

We are available to have a conversation with you about estimates.

### Notify stakeholders about the migration

Your employees have different needs with respect to their data, and it is paramount to know what those are. Take a shopping list of all departments, contact their managers, and identify key concerns in their processes and apps.

Keep in mind that while cloud storage is sometimes just a container for files, people might also be using it with third-party apps or for more advanced collaboration.

#### Example emails to send

**Subject**: ATTENTION: Decision to Migrate to Microsoft 365

**Message**: A few months ago, management decided we will transition to Microsoft 365. In Microsoft 365, all employees will have access to cloud storage and its included apps.

We will manage the migration to ensure all of our data gets transfered securely and efficiently. Let us know if you have any questions or concerns about the process.

**Subject**: ATTENTION: Important Info Regarding Cloud Data Migration**

**Message**: As you know from prior emails, we are moving to Microsoft 365 as our cloud storage provider.

To assist in this migration, we ask all employees to finish working and upload any last changes to files by 17:00 PT on Friday, April 7, 2020. Changes to files or data after this time will not be moved.

On Monday, April 10, 2020, all employees will be using Microsoft 365.

Questions and concerns can be directed to your immediate manager and/or our technical support staff via the usual channels.

## Connectors

### What is a connector?

A **Connector** is what we call our link to your cloud storage accounts.

To set up a transfer, you must grant us access to your cloud storage accounts. Without this link we are unable to communicate with them.

Creating a **Connector** may involve authenticating via OAuth or with normal username/password credentials. You only need to authenticate once per account.

Our authorization is lost when you delete the **Connector**, delete your account with us, or revoke our access through your cloud service's security settings.

### Which connector to use for each Microsoft service

|**Microsoft service**|**Which Mover connector to use**|
|:-----|:-----|
|Azure Blob Storage|Azure Blob Storage Connector|
|OneDrive Consumer|    OneDrive Consumer Connector|
|OneDrive for Business (Administrator)|    Microsoft 365 Connector|
|OneDrive for Business (User)|    OneDrive for Business (User) Connector|
|SharePoint Online|Microsoft 365 Connector|

## Deleting connectors

Deleting a **Connector** revokes our access to your cloud storage accounts. To confirm that we have been deauthorized, visit the security settings in your respective cloud service, and check for our app.

Using our app to remove our authorization with a particular cloud service is simple:

1. From the **Transfer Wizard**, select **Manage ▼** for the **Connector** type you want to delete.
2. To the right of **Connect**, select arrow ▼.
3. Select **Delete**.
4. Confirm you want to delete, and you're done!


![Delete connector](media/delete-connector.png)

>[!Note]
>Deleting a **Connector** is permanent and cannot be reversed. The **Connector** type disappears from the **Transfer Wizard**. To add a new **Connector**, select **Authorize New Connector**.

### Reauthorizing connectors

Reauthorizing a **Connector** is sometimes necessary if we lose authorization or access to your cloud storage accounts or web servers. It is also a good first step in trying to resolve most issues with your **Connectors**.

The process to authorize a **Connector** again is very simple:

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

Our app offers a source-to-destination delta. When you run a transfer, we compare the destination directory to the source, and only transfer new or modified files over. We call this our incremental feature.

We compare the timestamps of the files in both the source and destination and transfer the newest versions only. The incremental feature is always on.

Here are a few examples of how we deal with changes to files and folders.

**Content changes**: If a document is edited in your source or you have added a few new files, we copy them to your destination on the next incremental run, overwriting the previously existing file(s) in the destination.

**Name changes**: If the name of a file or folder changes in File Servers, we treat it as a brand new object. This can lead to duplicate files being migrated to Microsoft 365, or worse: entire folders worth of data being duplicated from the changed folder downwards.

**Example**: Changing the path `/Sales/Clients` to `/Global Sales/Clients` results in two copies of your `Sales` folder after the `Global Sales` folder is also copied during an incremental pass.

### Does Mover delete files?

We never delete your data from any source. Our app simply takes your data from one place and copies it to another—akin to *copy and paste* rather than *cut and paste.* We also don't retain any of your cloud storage data for any reasons.

### Can I rearrange content during a migration?

Not recommended. Any major changes in directory structure should happen before or after your migration. It is also not a best practice to use our app to rearrange content.

The risks that come with rearranging content during the migration are primarily in the form of data duplication; our incremental process sees all changes as new data. So, for example, if you change a folder name at the root, we detect that as a new folder, and all of the contents is re-transfered, including all subfolders.

When sharing permissions are transfered, both owners and collaborators receive duplicate data if content has been rearranged or renamed.

### What happens to external sharing links?

Our app does not recreate external sharing links. These must be set in the destination manually after migration.

### What about external collaborators?

We do not share content with external collaborators. This policy is in place to protect your organization, and industry best practice is to never automatically share sensitive internal data with external users.

### Does Mover preserve file versions?

We do not preserve file versions. During a migration, only the most recent version of a file is transfered from File Servers to Microsoft 365.

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

1. Log in. To visit your **Account** settings (**shortcut**), in the top right corner of our app, select your **account email**.
2. From the left-hand menu, select **Password**.
3. Under **Enable 2-Step Verification**, select **TURN ON**.

![2 factor screen](media/2_factor_screen.png)

>[!Note]
>You are automatically signed out of your account.

4. Log in to your email, and copy the verification code sent to you. If a verification code email does not appear in your inbox [or spam], just below the verification window in our app sign-in, select **Didn't get the code? Resend now**.

![Verification code](media/verification_code.png)

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

![Delete account](media/delete_account.png) 

### How do I edit my email notifications?

By default, you receive an email every time a transfer is completed. To edit your email notification settings:

1. Log in. To visit the account settings, in the top right of our app, select your email address.
2. Select **Preferences**.
3. You have the option to receive emails **On Completion** (default), **Never**, or **Only on Errors**.


### Can I change my account email?

Unfortunately, at this time, we do not allow you to change the email associated with your account.

You may, however, delete your account — losing the schedules, connector authorizations, and transfer history associated with it — and create a new account with the email you would prefer.

### How do I check my transfer usage?

Checking your usage of our app enables you to know the total amount of gigabytes you have transfered over the history of your account.

To check your transfer data usage, follow these steps.

1. Log in. To visit your **Account** settings, in the top right corner of our app, select **account email**.
2. By default, you are already in the **Plan** section.

## Agent FAQ

### Windows

The Windows Agent has two installers, one for the user-context and one for the service-context. The Windows Agent requires Microsoft .NET Framework 4.6.2 or greater.

The differences between Windows installers are as follows:

#### User-context installer

- **Select to download**.
- Installs and is run as the currently logged in Windows user.
- Automatically updates.
- Has access to local drives.
- Has access to mapped network drives.
- Is not available if the user logs out of Windows, or your remote desktop session expires.

#### Service-context installer

- **Select to download**.
- Installs and is run as a Windows service.
- Must be manually updated.
- Has access only to local drives.
- Is always available, even if the current user logs out, or your remote desktop session expires.


#### Command line agents

The following Agents operate using a command line interface versus a user interface.

### macOS

- **Select to download**.
- Navigate to the download location, and unzip the **Mover Agent**.
- Via the terminal, browse to the now unzipped `moveragent` folder, and run `./agent`.
- Copy the key from the line that reads `[1] INFO ocess.BifrostService: Bifrost service initialized with connector key: <key>`.
- Open our app, and in the **agent authorization** box, paste the key.

>[!Note]
>The minimum system requirements are macOS 10.12.

### Linux

- **Select to download**.
- Navigate to the download location, and unzip the Agent.
- Via the terminal, browse to the now unzipped `moveragent` folder and run `./agent`.
- Copy the key from the line that reads `[1] INFO ocess.BifrostService: Bifrost service initialized with connector key: <key>`.
- Open our app in your browser, and paste the key into the agent authorization box.

### Windows command line installer (beta)

- **Select to download**.
- Installs and is run as a command line executable.
- Must be manually updated.
- Built from the same code base as the Linux and macOS agents.

### How does the agent view users?

The Agent works with files and folders. All users who are separated into their own folders can easily be mapped to their new location in Microsoft 365.

A good example would be a large listing of home drives. Each home drive for a user could be transfered to their respective new user in Microsoft 365.

![Agent view users](media/windows-view-users.png)

### Troubleshooting the agent

#### Checking the agent version

To check which version of the Server Client you have installed, on the menu bar, select the **Help** tab.

![faq agent](media/agent_version.png)

If you are using the Mac or Linux version of our Agent, to find out the version you are using, follow these instructions: **Show Agent Version**.

#### Accessing server agent log

To access the **Agent Log**, navigate to the folder directory that you installed the desktop agent. A .log file appears that you can review, and send to our support team if an error should occur.

>[!Note]
>The agent .log file default location is `Windows\System(32/64)\config\systemprofile\AppData\Local\Mover`

![agent log](media/agent_log.png)

#### Commands for agent (Mac and Linux only)

Our Agent supports the following commands:

- Start the Agent
- Stop the Agent
- Show Agent Help
- Show Agent Version
- Check Agent Status
- Disconnect the Agent
- Connect the Agent
- Monitor Agent Activity


#### Start the agent

To start the Agent, use: </br>`./agent start`.

`$ ./agent start`</br>
`Mover Agent Starting`</br>
`Mover Agent Key:`</br> `0000000000000000000000000000000`</br>
`Ctrl-C To Stop`

#### Start the agent in the background

To start the Agent in the background, use:</br>`./agent start &`.

`$ ./agent start &[1] 8667`</br>
`$ Mover Agent Starting`</br>
`Mover Agent Key:`</br> `00000000000000000000000000000000`</br>
`Ctrl-C To Stop`

#### Stop the agent

If the Agent is running in the foreground of the terminal, to stop the Agent, press `Ctrl-C`.

`^CMover Agent Stopping`

If the Agent is running the background or in another terminal session, use:</br> `./agent Stop`.

`$ ./agent stop`</br>
`Connecting to Mover Agent`</br>
`Sending stop command`</br>
`Mover Agent Stopping`</br>
`Mover Agent stopped`</br>
`[1]+ Done ./agent start`

#### Show agent help

To get a list of commands and options, use:</br> `./agent -h`.

`$ ./agent -h`</br>
`Mover Agent 1.0.6968.0`</br>
`Usage: agent [options] [command]`

`Options:`</br>
`-? | -h | --help Show help information`</br>
`-v | --version Show version information`

`Commands:`

- `connect| Connect to a running instance of the Agent and issue a connect command`</br>
- `disconnect| Connect to a running instance of the Agent and issue a disconnect command`</br>
- `monitor| Connect to a running instance of the Agent and monitor agent activity`</br>
- `start| Start the Agent`</br>
- `status| Connect to a running instance of the Agent and retrieve the current status`</br>
- `stop| Stop the Agent`

For more info about a command, use `agent [command] --help`.

#### Show agent version

To show the Agent version, use:</br> `./agent -v`

`$ ./agent -v`</br>
`Mover Agent`</br>
`1.0.6968.0 (Unix 18.6.0.0)`

#### Check agent status

To check the status of the Agent, use:</br> `./agent status`

`$ ./agent status`</br>
`Connecting to Mover Agent`</br>
`Mover Agent Key:`</br> `00000000000000000000000000000000`</br>
`Mover Agent Status: online`

#### Disconnect the agent

To disconnect the Agent, use:</br> `./agent disconnect`

`$ ./agent disconnect`</br>
`Connecting to Mover Agent`</br>
`Sending disconnect command`</br>
`Mover Agent disconnected.`

`$ ./agent status`</br>
`Connecting to Mover Agent`</br>
`Mover Agent Key:`<br>
`00000000000000000000000000000000`</br>
`Mover Agent Status: offline`


#### Connect the agent

To connect the Agent, use:</br> `./agent connect`

`$ ./agent connect`</br>
`Connecting to Mover Agent`</br>
`Sending connect command`</br>
`Mover Agent connected.`

`$ ./agent status`</br>
`Connecting to Mover Agent`</br>
`Mover Agent Key:`<br>
`00000000000000000000000000000000`</br>
`Mover Agent Status: online`


#### Monitor agent activity

To monitor the Agent activity, use:</br> `./agent Monitor`. To stop monitoring Agent activity, use: `Ctrl-C`.

`$ ./agent monitor`</br>
`Connecting to Mover Agent`</br>
`Mover Agent Key:`<br> `00000000000000000000000000000000`</br>
`Connected to bifrost.mover.io on port 443.`</br>
`Ready to transfer!Browse: /`</br>
`Browse: /Users`</br>
`Browse: /Users/mover`</br>
`Browse: /Users/mover/AgentTestData`</br>
`Browse: /Users/mover/AgentTestData/TestDocuments`</br>
`Upload: /Users/mover/AgentTestData/TestDocuments/TestTextDocument.txt`</br>
`Upload: /Users/mover/AgentTestData/TestDocuments/file.txt`</br>
`Upload: /Users/mover/AgentTestData/TestDocuments/picture.jpg`</br>
`^C`

## Microsoft 365 FAQ

### Will there be unsupported files and characters?

We automatically process file and folder names to ensure they are accepted by Microsoft 365.

- Files larger than `15 GB` are not migrated.
- Files with a size of `0 bytes` (zero-byte files) are not migrated.
- The following characters in file or folder names are removed:
`" * : < > ? / \ |`
- Leading tildes (`~`) are removed.
- Leading or trailing whitespace is removed.
- Leading or trailing periods (`.`) are removed.
- For all invalid file or folder names and other Microsoft 365 limitations, see **here**.

In some possible circumstances with older sites, any file or folder ending in `_files` could fail. If you experience these errors, contact Support.

Microsoft currently has no file type limitations, meaning you can upload data with any file extension. For more info, see **here**.

#### Character limits for files and folders

File names may be up to 256 characters.
Folder names may have up to 250 characters.
Total path length for folder and file name combinations may be up to 400 characters. For more info, see **below**.

### What happens to long paths?

During a pre-scan, our app automatically detects and reports paths that are too long for OneDrive or SharePoint to accept. The current path length limit for Microsoft 365 is 400 characters. The path length is calculated when going in to Microsoft 365 and includes your tenant URL, user site, path, and any character encoding.

**Example**:

This path is 93 characters long despite "Documents/Old Docs" being only 18 characters.</br>
`https://example-my.sharepoint.com/personal/example_user /%2FDocuments%2FOld%20Docs`</br>
If a file exists that has a very long path, our app skips it, and reports it in your log files.

To save time and headaches, you are encouraged to shorten any identified long paths before you migrate.

![Turn this into this](media/turnthis-intothis.png)

### Are timestamps preserved?

The original timestamps from File Servers are preserved when migrating into Microsoft 365.

>[!Note]
>Timestamps are only applied to files/data transfered and not folders. Folders and Folder structure are created in the destination during migration, and reflect the date of the migration.

### Is file authorship preserved?

When migrating from File Servers into Microsoft 365, the *modified by* author is preserved. However, the *created by* is changed to the user.

### Does the Mover app interact with the sync client in OneDrive for Business?

We do not interact with the sync client in OneDrive for Business. We recommend disabling it before a migration. If you use it during a migration, it tries to sync all the migrating data.

### What happens to shared data?

Data shared with a user by another user appears in the **Shared with me** folder. Data owned by a user appears in the user's designated destination folder.

### What about notifications?

The Mover app silences notifications during the migration to prevent users from being spammed.

### What happens to data shared to Microsoft 365 Groups?

Data shared to a Microsoft 365 Group does not appear in the **Shared with me** section. Microsoft also does not notify users that they are now a member of a Microsoft 365 Group.

>[!Note]
>This is a limitation of Microsoft 365 Groups and cannot be changed on our end. The user must navigate to the appropriate group within either their Outlook Desktop Client, or by logging into their prefered email through **outlook.office.com**.

After the user has logged in:

- Navigate to the left-hand menu.
- Scroll down the folder listings to **Groups**.
  - If the available groups are not visible, to open the group directory, select the small arrow beside the **Groups** listing.
- Select the desired group.
From here, the left-hand menu should change, enabling you to open and edit **Files/Notes** within the selected Microsoft 365 Group.

### What SharePoint site formats are supported?

Both Modern and Classic sites are supported and appear the same in our app.

### What will my file paths look like in SharePoint?

During the migration setup (described later in this guide), you can edit the path(s) to specify where in SharePoint you would like your data to go. From the root level of SharePoint Online, you can go into **Site Collections**, and inside each **Site Collection**, you will find directories for **Site Contents** and **Subsites**.

**Site Contents** takes you to document libraries (for example, the **Documents** section), whereas **Subsites** takes you to the **Subsites** of that site collection. Navigating **Subsites** takes you through the same dichotomy.

Most cloud storage providers, G Suite Drive, for example, start the listing with a user, such as `/user@example.com/Marketing Folder`. SharePoint Online does not do this, so you would be looking at a path such as `/Marketing/Site Contents/Documents`.

![File paths in SPO](media/filepaths-in-sp.png)

### How does library permissions inheritance affect migration?

To set specific permissions on folders in a document library, inheritance must be disabled. Permissions inheritance is typically turned on by default, which makes all the data within the library subject to the permissions set on the library. This is similar behavior to team folders or team drives in other cloud services, whereby if users have access to the root level, they have access to everything contained within.

If inheritance is not disabled at the root, any permissions we try to set on individual folders are overridden by the library access permissions.

**To disable inheritance**:

In the Library settings, visit **Permissions for this document library**:

- Select **Stop Inheriting Permissions**.
  - This enables you to select the permissions you would like to remove:
   - Site members
   - Site visitors
- Select **Remove User Permissions**.

This prevents site members/visitors from inheriting permissions to all the data that we migrate into that library, allowing permissions only to those site members who we explicitly write to the folders themselves.

For more info about SharePoint Online permissions inheritance, see **here**.

### Does Mover support Microsoft Teams?

Microsoft Teams appears and operates the same as a SharePoint Online site.

### What is the item limit for SharePoint Online?

Many sites claim that SharePoint has a 5,000-item limit. This is not true. The SharePoint 5,000-item limit applies to how many items appear in a search list view: a maximum of 5,000.

SharePoint sites do have file size and number limits which are covered in detail here: **SharePoint Online limits**.

Some list view options may prevent search list views with more than 5,000 items from appearing.

## Setting up the migration

### Authorizing the desktop and server agent

To enable swift and painless copying of data from on-premise desktop and server hard drives, we provide a very tiny agent that any Windows operating system can install.

#### Compatibility

Windows XP is not supported.
All other versions of Windows require the .NET Framework 4.6 for the Agent to function.
Download and manually install .NET Framework 4.6 from this **link**.

#### Security

The Agent may only initiate outbound communication with our own servers. All communication is via encrypted TLS and no service other than ours is allowed to work with the agent.

#### Windows installation

For Mac and Linux, the Agent folder appears in your Downloads, and is run through **command line operations**.

1. Download the Agent .exe, and select **Run**.

![Download agent](media/download_agent.png)</br></br>
![Run agent](media/run_agent.png)

2. Agree to the **Terms of Use**, and select an install destination.

![Agent terms](media/agent_terms.png)
![Destination agent](media/destination_agent.png)

3. Navigate to the installed destination, and to run the desktop Agent, select the **Mover** icon.

![Open agent](media/open_agent.png)

4. To copy the Agent Key, in the dropdown menu, select **File** and **Copy Key**.

![Agent key](media/agent_key.png)

#### Authorizing the agent in our app

1. In the **Transfer Wizard**, select **Authorize New Connector**.

![Clear auth](media/clear_auth.png)

2. In the **Connector** list, find **Agent (Desktop or Server)**.
3. Select **Authorize**.

![Agent connector list authentication](media/agent_connector_list_auth.png)

4. A new window opens, and you are prompted to name your **Connector** <optional>.
5. Enter your required Key that you copied from the installed agent (found via the **File** > **Copy Key** action in the Agent).
6. Select **Authorize**.

![Name connector agent](media/name-connector-agent.png)

##### Additional screenshots

![Additional screenshots](media/additional-screenshots.png)

### Troubleshooting an agent connector

#### What operating systems are supported by the Mover agent?

The Mover Agent supports many operating systems:

- Windows Vista
- Windows 7
- Windows 8
- Windows 8.1
- Windows 10

#### Removing the Mover agent

You can stop using the Mover Agent.

To stop the Mover Agent from connecting to the Mover's servers, select **Disconnect from Mover**.

To completely uninstall the Mover Agent, use the Windows program manager.

### Authorizing Microsoft 365

>[!Warning]
>To fully authorize the **Microsoft 365 Connector**, a Global Admin is required to grant permissions to the Microsoft 365 Mover app within the Azure portal.
>
>The Global Admin must grant these permissions *after* the **Microsoft 365 Connector** is authorized within the main Mover app.

The following instructions show you how to complete the authorization steps in the right order.

Some steps in the authorization process can be completed by a Global Admin or an SPO Admin. At the beginning of each step, we indicate who can complete it.

1. **Global Admin or SPO Admin**: Log into the main Mover app via **app.mover.io**. In the **Transfer Wizard**, select **Authorize New Connector**.

>[!Note]
>Whether the **Microsoft 365 Connector** is your source or destination connector (or both), you must complete this authorization process.

![Authorize new connector](media/05-authorize-new-connector.png)

2. **Global Admin or SPO Admin**: In the **Connector** list, find **Microsoft 365**. Select **Authorize**.

![Authorize O365](media/authorize-o365.png)

3. **Global Admin or SPO Admin**: A window with an **Authorize** button appears. It prompts you to provide a display name <optional> for your **Microsoft 365 Connector**.  Select **Authorize**.

![Authorize windows](media/authorize-window.png)

4. **Global Admin or SPO Admin**: Follow the on-screen instructions. You will be redirected to a Microsoft login screen where you can log in with your Microsoft admin privileges, and continue to authorize the connector.


>[!Warning]
>If you are a **Global Admin**, a slightly different login screen will display.  
>
>**DO NOT** select the option **Consent on behalf of your organization**. This option **must** remain unselected.

- ![global admin o365](media/permissions-o365-global-admin.png)




5. **Global Admin or SPO Admin**: After authorizing the connector, you are redirected to the **Mover Transfer Wizard**, and an error appears, like the following. This means it is now time for a Global Admin in your tenant to grant permissions to the Microsoft 365 Mover app in the Azure portal.

If you're an **SPO Admin**: To grant permissions and finish the authorization process (Steps 6 – 9), point your Global Admin to **aka.ms/office365moverauth**.

If you're a **Global Admin**: Continue with Steps 6 – 9.

![Authorize error](media/authorize-error.png)

6. **Global Admin**: Log into the Azure portal via aka.ms/office365moverauth. A list of **Enterprise applications** appears.

![Enterprise applications](media/enterprise-applications.png)

7. **Global Admin**: Find and select the Microsoft 365 Mover app. A page appears that provides an overview of our app.

![O365 Mover app](media/o365-mover-app.png)

8. **Global Admin**: In the left menu, find and open **Permissions**. Select **Grant admin consent for Mover**.

![o365 mover permissions](media/o365-mover-permissions.png)

9. **Global Admin**: A pop-up window appears that guides you through the rest of the permissions process. When complete, it closes automatically, and your **Microsoft 365 Connector** is fully authorized and ready to go.

### Troubleshooting a Microsoft 365 Connector

#### App access error

If you encounter an error on authorization, try signing out of any Microsoft accounts, and in an Incognito window, attempt to authorize the Connector.

#### Global Admin account provisioning

Your Global Admin user must have a Microsoft 365 account provisioned to administer other Microsoft 365 accounts. If you create a service account for our app, ensure you are also assigned a Microsoft 365 license and walked through the Microsoft 365 setup process.

#### User provisioning

Are your Microsoft 365 users provisioned? All Microsoft 365 users need to have logged in to their Microsoft 365, and opened up Microsoft 365 for us to be able to transfer into their accounts. You can also provision Microsoft 365 accounts via Windows PowerShell using the following commands (replace your URL and email appropriately):

`Connect-SPOService -Url https://example-admin.sharepoint.com -credential user@example.com`

`Request-SPOPersonalSite -UserEmails "neverloggedintest@example.onmicrosoft.com"`

#### Microsoft 365 permission requirements

Our app requires a Global Admin for authorization. The following table lists the scopes we require:

|**Permission**|**(Details) Allows out app to...**|
|:-----|:-----|
|Create, edit, and delete items and lists in all your site collections|Create or delete document libraries and lists in all site collections on your behalf.|
|View your basic profile|See your basic profile (name, picture, username).|
|Maintain access to data you have given it access to|See and update the data you gave it access to, even when you are not currently using our app. This does not give our app any additional permissions.|
  a. Select **File**.
  b. Select **Save As**.
  c. From the **File Format** options, select **CSV**.

### Connect your source agent for Windows

If you are not already connected after you have authorized your source, select **Agent for Windows**, and load the connector. An icon appears showing you the folders you are migrating.

![Execution select agent source](media/execution-select-agent-source.png)

### Connect your destination Microsoft 365 account

If you are not already connected after you have authorized your destination, select **Microsoft 365**, and load the connector. An icon appears and show you how many users you are migrating.

![Execution select Microsoft 365 destination](media/execution-select-office-365-destination.png)

#### Create a new migration

Select **Continue Migration Setup**, and our app moves to the **Migration Manager**.

![Create migration](media/create-migration.png)

The next step creates a user list of who is transfering.

From your newly created migration in the **Migration Manager**, there are two ways to add users:

- Select **Add Users**.

![Add users](media/add-users.png)

- Or, select **Migration Actions**, then select **Add to Migration**.

![Migration users](media/migration-users.png)

Select one of two options:

1. Auto Discover Users:
  - Select **Automatically Discover and Add Users**, and our app automatically finds your users, and attempts to match them up.

2. Upload Migration CSV File:
  - Either drag a file into the designated space, or select **Choose a file to upload**, and add a customized CSV file for your migration.

![Add users menu](media/add-users-menu.png)

>[!Note]
>You still get to finalize your migration before any data moves!

#### Creating a new migration from a CSV (optional)

Sometimes you have thousands of users and a complicated directory schema that you want to import. In these cases, it's desirable to plan out your migration in a spreadsheet.

In these cases, we hope the CSV upload option is useful. This allows you to lay out all your users and directories and then give it to us in a .csv format for us to create your migration.

##### Paths to migrate

Your CSV file must follow this format:

A heading for the source and destination, followed by the paths, and optionally tags on each line.

`Source Path,Destination Path,Tags`</br>
`D:/Users/user1,user1@example.com,"Pilot, Home Folder"`</br>
`E:/Share/Marketing,Marketing Team Folder/subdir,"Pilot, Department"`</br>

>[!Note]
>Ensure your CSV has no spaces after each comma separated value. Values that require commas must be wrapped in quotation marks.

Download an example CSV here:

**Example_CSV_Map.csv**

#### Creating your CSV in Excel

If you are using an Excel spreadsheet to create your CSV:

1. Ensure you have two columns, one titled `Source Path`, and one `Destination Path`.
2. List the relative paths, domains, and usernames on the subsequent rows.
3. Export your spreadsheet as a CSV:
  a. Select **File**.
  b. Select **Save As**.
  c. From the **File Format** options, select **CSV**. 

#### Reviewing your users

##### Checking paths

Confirm that the users in the File Servers source match the users in the Microsoft 365 destination. Usually the emails/usernames match up, but it depends how you structure and name your users. *Be diligent during this step!*

#### Editing

Be aware that users can only be edited if they haven't been scanned, or had a transfer run.

To edit a user source entry:

1. To select a user row, on the left side of a row, select the respective checkbox.
2. On the right and directly above the user rows, find **User Actions**, or right-click the user row for which you want to edit the source path.
3. A new side panel opens, enabling you to edit the File Servers source path.
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

Download an example CSV here:</br>

[example_path_edit.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_path_edit.csv)

![Add ID customize column](media/add-id-customize-column.png)

4. After you've created your CSV file using these instructions and format, you can drag and drop the file into our app, or select **Choose a file to upload**. Changes to your user pairings are implemented immediately.

![Update migration](media/update-migration.png)

#### Adding

If you missed users in your original CSV upload, or simply want to add new user entries to the current migration, you can add them via CSV. All entries added in this manner are appended to the current migration, meaning this won't modify existing rows, and it is possible to create duplicate entries alongside the ones that already exist.

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

![migration finalize mover](media/migration-finalize-mover.png)

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

Afrer you select all users, select **Scan X Users**.

![scan users](media/scan-users.png)

After the scan has successfully completed, the users appear in green. The scan time varies depending on the data amount in the source.

After users appear in green, yellow, or red, on the top right side of your screen, select **Migration Actions**, and then select **Scan Report**.

>[!Note]
>If your scan encounters an error or crashes, our app automatically reruns the scan up to three times to attempt to resolve the issue.

![scan report migration](media/scan-report-migration.png)

The **Scan Report** is covered in-depth in the **Reports** subsection under the **Scan Report** section of this guide.

#### Migrating users

We recommend starting slowly. Test one user, then three to five. If all looks good, and you see data being downloaded and uploaded, start queuing everyone and stage the rest of your users.

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

The best way to resolve any issues with a transfer is to rerun it. This action checks over all the files in your destination, compares them to the source, and then transfers the new or modified files.

All transfers take advantage of our incremental feature and only transfer new or modified data differences between File Servers and Microsoft 365.

As long as a transfer is not running, to restart a transfer, you can re-queue a user.

To rerun or restart your transfer, complete the following steps:

1. Select the or user(s) you want to rerun.
2. To run the users again, at the top right, select **Start Migrating X Users**.

### Transfer status messages

The following table lists additional info about each transfer status message from the **Migration Manager**.

|**Status message**|**Definition**|
|:-----|:-----|
|Running pre-checks|    Our servers are checking a few items, and sending your transfer to the queue. Almost there!|
|Queued to start, please be patient|    Your transfer will run as soon as possible. You can close your browser, and receive an email upon completion. There is no limit to queued users.|
|Success. No files copied    |We have skipped all of your files without error, and have detected no new or modified files.|
|Success. Some unsupported files not transfered|    We have skipped all of your files without error, and have detected no new or modified files. Files unsupported by the source or destination were skipped over.|
|Some upload errors, please retry|    We were able to download everything from the source, or skip files that already existed in the destination, but some files didn't make it into the destination.|
|No files copied. Some upload errors, please retry|    We were able to download everything from the source, or skip files that already existed in the destination, but no files made it into the destination.|
|Some download errors, please retry|    We weren't able to download everything from the source, but some files made it into the destination successfully.|
|No files copied. Some download errors, please retry    |We weren't able to download anything from the source!|
|Some download and upload errors, please retry    |There were errors with both downloading and uploading files, although some incremental files may have been skipped successfully.|
|General failure, please retry|    We don't have a particular reason why your transfer failed - maybe we were having trouble connecting to your source or destination properly, for example.|
|Connector auth failed|    One of your connectors isn't authorized correctly.|
|Crashed, please retry|    We don't have a particular reason why your transfer failed, but generally this is due to server issues on our side, or with the source or destination connectors. If you encounter a crash, contact us.|

## Post-migration troubleshooting

### General troubleshooting

Follow these steps if your migration is having issues:

1. Rerun users. Select one or more users and to rerun them, on the top right of the **Migration Manager**, select **Start Migrating**.
2. To view your most recent transfer log, select the user row you want to view. This action opens the **Transfer Logs** sidebar. From here, select the **View Log** button for the most recent transfer.

![view logs](media/view_logs.png)

Alternatively, you can select multiple users, and from the **User Actions** dropdown menu, you can download their most recent collective logs in a zip file that provides them in both HTML and CSV formats.

3. Check if your failed/unsupported files are too large to go into Microsoft 365.
4. Ensure you have enough storage space in Microsoft 365 to accommodate the data you're moving in.
5. Think files are missing? Check out our list of **Unsupported Files per Connector**.

### Incremental feature

Our incrementals are delta operations which compare files in your File Servers to files in Microsoft 365. Using this comparison, we copy anything that is new or has changed. This enables us to keep Microsoft 365 data up to date when the final cutover of users occurs. These incremental passes are an important part of our process.

**Technical clarification**: We compare what you have in File Servers to what is in Microsoft 365, and we only transfer anything that doesn't already exist, or has a newer timestamp.

### 'Lost files'

During a transition where sharing paradigms change, there are many users who claim, "My files are lost!"

This is common if they are not in clear communication about how the sharing structure changes when they log in to Microsoft 365. This can be mitigated with a clear communication strategy.

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

1. Select the user row. The **Transfer Logs** sidebar appears. To view any previous transfer log for the user you selected, select **View Log**.

![view logs2](media/view_logs.png)

>[!Note]
>To open a transfer log in your web browser with built-in sorting and filter features, select **View Log**.

2. To select multiple users, from the **User Actions** dropdown menu or the **Actions** menu in the side tab, select **Download Logs (zip file)**. As the label implies, multiple log files are zipped together for download.

![multiple logs](media/multiple_logs.png)

>[!Note]
>The zipped file provides logs in both CSV and HTML formats for only the most recent transfer of each user.

View an example CSV log in your browser here:

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

![migration manager transfers](media/migration-manager-transfers.png)

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

The CSV report provides the following info for each user pairing:

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

Download an example CSV here: 

[example_migration_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_report.csv)

### Migration table report

The **Migration Table Report** generates an overview of your entire migration based on the custom designated columns you have set.

To edit report columns, in the **Migration Manager**, select **Migration Actions**, and select **Customize Columns**. Here you can set and reorganize which **Columns** you want to display when you download the CSV report.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Table Report**.

![migration table example](media/migration-table-example.png)

Download an example CSV here: 

[example_migration_table_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_table_report.csv)

### Migration error report

The **Migration Error Report** generates a simplified **Migration Report** that focuses on any problematic files, folders, permission errors, or general errors.

To download this as a CSV, at the top right of the **Migration Manager**, select the **gear** icon, and select **Migration Error Report**.

![migration error example](media/migration_error_example.png)

Download an example CSV here:

[xample_migration_error_report.csv](https://github.com/MicrosoftDocs/OfficeDocs-SharePoint/tree/live/migration/downloads/example_migration_error_report.csv)

## Post-migration tips

We are stewards of your data. Our approach in all things is to see you successfully cross the finish line. We provide full service support and are ready to solve any problem and communicate with you about any issue.

### Communication

Follow up with users after migration to ensure they know where to access their data.
Provide a link to set up their new Microsoft 365 accounts. Be prepared to answer any questions or concerns, as it is common for users to complain about a new system.

### Example email

**Subject**: ATTENTION: Log in to Microsoft 365

**Message**: Over the weekend, we migrated our team to Microsoft 365.

All files and folders were transfered without any issues. To set up your new Microsoft 365 account, follow this link.

Your username remains the same; however, you must create a new password.

From this point forward, log into your Microsoft 365 account.

If you have any questions or concerns, let us know.

