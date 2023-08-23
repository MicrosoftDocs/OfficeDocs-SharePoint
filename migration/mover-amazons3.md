---
title: Authorizing the Amazon S3 Connector
author: JoanneHendrickson
ms.author: jhendr
manager: serdars
recommendations: true
audience: ITPro
ms.date: 6/22/2020
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
description: "Authorizing the Amazon S3 Connector"
---

# Authorizing the Amazon S3 Connector

>[!Important]
>**Mover is now retired for all Admin led migrations**. The ability to migrate from Google Drive, Box, Dropbox, and Egnyte has been fully integrated into Migration Manager. For full details see: [Mover retirement timeline](mover-retirement-timeline.md).  Migration Manager does not support the migration of Amazon S3 or Azure blob storage.
>
>All FastTrack-led migrations have transitioned to Migration Manager.
>
>**Tenant to tenant migration**. Cross-tenant OneDrive migration is now available outside of Migration Manager. Learn more here: [Cross-tenant OneDrive migration](/microsoft-365/enterprise/cross-tenant-onedrive-migration).  
>
>A cross tenant migration solution for SharePoint is currently being developed and in private preview.  To learn more, see [How to participate in the Cross-tenant SharePoint migration preview](/microsoft-365/enterprise/cross-tenant-sharepoint-migration).



## Authorizing Amazon S3

Authorizing Amazon S3 is straightforward. To authorize or add an Amazon S3 account as a Connector, follow these steps:

1. In the Transfer Wizard, click Authorize New Connector.

   ![Auth New Connector](media/clear_auth.png)

2. Find Amazon S3 in the Connector list.
3. Click **Authorize.**

   ![Amazon S3 Connector List](media/mover-auth-source-connector.png)

4. A new window (tab) will open. Name your Connector (Optional).
5. Enter your Access Key ID and Secret Access Key.

   ![Amazon S3 name connector](media/name_connector_amazon_s3.png)

6. Click **Authorize** again.

## Troubleshooting an Amazon S3 Connector

**Authorization:** If you're having trouble creating or adding an Amazon S3 connector, here are some things to try:

- Double check that you're entering in your Access Key ID and Secret Key correctly - these are both long alphanumeric strings prone to mistakes if entered manually. If copy and pasting, ensure that your computer is accurately performing that task.
- Hover over your existing Amazon S3 integration in the Connector selection screen and select Reauthorize. This will take you through the Connector creation steps again in order to refresh the token/permissions that we have with your Amazon S3 account.
- Open up private browsing or incognito mode and try again.

**Transfer from Amazon S3 source:** If you're having trouble transferring from Amazon S3:

- Select your finished transfer and click Start Migrating on the top right of the Migration Manager to rerun the transfer.
- View your most recent transfer log by selecting the transfer and clicking View Log from the User Actions dropdown menu. Check if there are any error messages you can act on.

**Using Amazon S3 via IAM:** With Amazon S3, by default we should have no trouble accessing your buckets. Here's how to connect to S3 via IAM:

- From the AWS dashboard, go to the Services menu, then Administration & Security, and then IAM.
- Then you'll want to create a user if you haven't already.
- Next you'll need to go into Policies and hit Create Policy, and then pressCreate Your Own Policy so we can make a custom policy.
- Name this policy something you'll easily find - perhaps Example+IAM or something along those lines - you can also include a description of what it is. You'll then need to copy and paste the following into the Policy Document field:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
  
      {
        "Effect": "Allow",
        "Action": "s3:ListAllMyBuckets",
        "Resource": "*"
      },
      {
        "Effect": "Allow",
        "Action": "s3:*",
        "Resource": "arn:aws:s3:::MyBucket"
  
      },
      {
        "Effect": "Allow",
        "Action": "s3:*",
  
        "Resource": "arn:aws:s3:::MyBucket/*"
      }
    ]
  }
  ```

- You'll need to go back to the Users menu, click on the user you'd like to add the policy to, and then press Attach Policy. From here, you can search for the custom policy you've created, select it, and then hit the Attach Policy button at the bottom right of the screen.
