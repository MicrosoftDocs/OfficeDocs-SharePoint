---
title: "Connect to Google with Migration Manager"
ms.date:  10/31/2023
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
mscollection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
search.appverid: MET150
ms.custom: admindeeplinkSPO
description: "Steps to connect to Google when using Migration Manager in the SharePoint Admin center."
---

# Step 1:  Connect to Google Workspace

Sign in to your Google account and add the Microsoft 365 migration app to your Google account custom apps. 

1. In the SharePoint admin center, select <a href="https://go.microsoft.com/fwlink/?linkid=2185075" target="_blank">**Migration center**</a>. 
2. Under **Google Workspace**, select **Get started**.
3. Select **Connect to Google Workspace**. 
4. On the *Install the migration app* page, select **Install and authorize** if you haven't already installed the Microsoft 365 migration app in the Google Workspace Marketplace. 
5. Sign in to the Google Workspace Marketplace with a super admin, groups admin, user management admin, or help desk admin account. 
6. Select **Domain Install**.
7. On the Domain-wide install screen, select **Continue**.
8. Agree to the terms of service and then select **Allow**. 
9. Select **Done** to complete the installation.
10. Return to the Migration Manager wizard screen. Select **Next**
11. Select **Sign in to Google Workspace**.
12. Choose an account to continue to Microsoft 365 Migration.
13. Select **Finish** to close the window.

![connected to google success screen](media/mm-google-connected-success.png)


### Grant access to Google forms

To ensure your Google forms are migrated, you must first grant access in the Google Marketplace.

1. Sign in with your Google admin credentials to [Google Marketplace](https://admin.google.com/ac/apps/gmail/marketplace/appdetails/888375727339).
2. Under **Drive**, verify that "See all your Google Forms" forms status shows **Granted**.  

  :::image type="content" source="media/mm-google-form-only-access.png" alt-text="google permissions granting for gsheet":::

3. If it hasn't been granted, select **Grant access** at the top of the page to grant access.



>[!Important]
>For security reasons, you have 10 minutes to complete the steps to connect to Google. After 10 minutes of inactivity, the session will expire.

## Go to [**Step 2: Scan and assess**](mm-Google-step2-scan-assess.md)
