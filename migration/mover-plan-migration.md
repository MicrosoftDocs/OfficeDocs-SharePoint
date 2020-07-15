---
title: Mover Migration Tools overview and planning
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
description: "Overview and planning to the Mover Migration tools"
---

# Mover Cloud Migration 

## Introduction

Our purpose is to act as an intermediary between various web technologies that don't play nice together. We take your files from one place and copy them to another. No downloads and nothing to watch over—our web-hosted app does all the work!

Undertaking any corporate migration is a daunting task. When moving your data to the cloud, there are many things to consider.


>[!Tip]
> Need help? [Open a support request here](https://support.microsoft.com/en-us/supportforbusiness/productselection?sapId=c3fa6eba-e1f0-0715-4519-94a9740c5f2c)

### File processing summary

When we transfer a file, a temporary copy is downloaded from **Office 365** to a temporary server and then uploaded to Office 365. Upon successful upload, that file is deleted from the temporary server. When your migration is complete, that temporary server is destroyed. Any log data expires in 90 days and is never retained by us. We do not perform any actions beyond copying files and folders and sharing permissions. We never perform delete operations.

## Communicating with stakeholders

A migration is a significant undertaking for any organization. Trying to grasp the entire extent of all data and communicating with your employees is complicated. We sympathize!

Before, during, and after a migration, it is critical to communicate clearly and effectively with your user base. We provide timely support and communication materials to your transition team to help you communicate these changes with each stakeholder.

**Management** — Management needs succinct info about the how’s and why’s of the migration, such as costs, benefits, and expectations. You must paint a clear picture about what a successful migration should look like. Granular info is important when running a department.

For example, the Sales Manager needs to know how operations will be affected, such as *Can employees still work over the weekend, if needed?*

**Users** — These are your bread-and-butter employees. They need to know when changes are taking place and who to go to with questions or issues.

Key questions to address:

- Why are we migrating our data?
- How does it impact me?
- What are the benefits?
- How disruptive is this change going to be?

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

Mover allows up to 5 users to simultaneously transfer.


## Data distribution

Determining the distribution of data across the user base is an extremely important component of a migration because we copy data in a highly parallel manner, and our servers transfer data as fast as each cloud storage provider can handle. Office 365 has rate limits for how fast data can be downloaded and uploaded.

The more users simultaneously being transferred, the higher our throughput for your migration. **We highly recommend that users with very large data sets be broken into smaller accounts to facilitate faster transfers.**

>[!Note]
>To maximize throughput, users should not own greater than 5TB of data. The more users you have, and the smaller the amounts of data they own, the faster your migration proceeds.

For example:

- If one user owns 10 TB of data, we recommend dividing that between 10 users so that each one owns 1 TB.

If data cannot be broken up, this should not hinder other users from migrating. As a general rule, users with a lot of data require a lot of time to migrate.

### Amount of data to move

Knowing the total volume of data you are moving helps to create a more realistic timeline for your migration.

### Your migration team

Establish a migration team to lead your organization through the project. The team’s role includes liaising with us, undergoing training, and notifying employees of each change during the migration process.

An IT Manager or the Head of IT is a good choice for our point of contact because they understand the ins and outs of your organization's systems. To ensure a smooth, successful migration, we work closely together and are with you every step of the way.

## Timelines

### Be realistic

The amount of time required to plan, execute, and wrap up a migration depends on many factors. Organizational requirements, budget, security reviews, and support from management are just a few.

We typically see corporate transfers take a minimum of 30 days to plan and execute. Ensure you allot yourself enough time for each stage, which we cover later on in this guide.

### Evaluate your user base

It is critical that you plan which users are migrating and when. Ask yourself questions like these:

- *Is the entire organization migrating, or just a few users?*
- *Is everyone migrating at once, or are you splitting them into batches like department, office, or region? If so, why?*

>[!Note]
>Batching migrations this way increases complication, and may extend your migration.

We recommend migrating during a slower organizational period, such as the weekend, to avoid work interruptions.

### Keep your accounts active

When migrating from Office 365 to Office 365, you need to ensure all your users are active and accessible. Knowing exactly when your Office 365 may shut down or expire is key to safely planning enough time to migrate.

### Consider migration speed factors

We're the fastest way to migrate your data, but the speed of your migration may still be affected by bottlenecks. Speed bottlenecks include, but aren't limited to, the following:

- Number of files and folders being moved
  - This is objectively the biggest speed limit on the Internet, as it determines the total number of operations required. Most providers rate limit their ingress to one file per second per user. This isn't universally true, but it's a baseline conservative metric you can use when estimating.
  - Our observable average across our customers is a 2.4 MB average file size.
  - Knowing file size is necessary to estimate transfer speed. If you are not able to determine exact numbers, most services can provide reports that illustrate individual or average file size.
- Total amount of data being moved.
  - Total data can affect speed, but it is ultimately overshadowed by the number of files.
- Server connections with the source or destination **Connector**.
- Complexity of permissions or sharing schemes, if applicable.

What may be surprising is how large of an impact factors other than the size of the data you are moving can have.

For example, it is common for there to be half a second of overhead per file being moved. If you are moving 200,000 files, this would be 200,000 seconds or more than two days' worth of overhead alone!

Suffice to say, we cannot give you exact estimates on time because there are too many factors at play at any given point. By the time you have read this section, we could have easily copied several files totaling many GB, or a few hundred files equaling a small amount of data.

We are available to have a conversation with you about estimates.

### Notify stakeholders about the migration

Your employees have different needs with respect to their data, and it is paramount to know what those are. Take a shopping list of all departments, contact their managers, and identify key concerns in their processes and apps.

Keep in mind that while cloud storage is sometimes just a container for files, people might also be using it with third-party apps or for more advanced collaboration.

#### Example emails to send

**Subject**: ATTENTION: Decision to Migrate from Office 365 to Office 365

**Message**: A few months ago, management decided we will leaving Office 365 and transition to a new Office 365 domain. In the new Office 365, all employees will have access to cloud storage and its included apps.

We will manage the migration to ensure all of our data gets transferred securely and efficiently. If you have any questions or concerns about the process, let me know.
</br>

**Subject**: ATTENTION: Important Info Regarding Cloud Data Migration

**Message**: As you know from prior emails, we are moving from Office 365 to a new Office 365 domain as our cloud storage provider.

To assist in this migration, we ask all employees to finish working and upload any last changes to files in the source Office 365 by 17:00 PT on Friday, April 7, 2020. Changes to files or data in the source Office 365 after this time will not be moved.

On Monday, April 10, 2020, all employees will be using our new Office 365 domain.

Questions and concerns can be directed to your immediate manager and/or our technical support staff via the usual channels.

