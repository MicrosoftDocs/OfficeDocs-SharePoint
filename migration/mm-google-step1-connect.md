---
title: "Connect to Google with Migration Manager"
ms.date:  01/21/2021
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
mscollection:
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Steps to connect to Google when using Migration Manager in the SharePoint Admin center."
---

# Step 1:  Connect your Google account to Microsoft 365 (preview)

>[!Note]
> Features described in this topic are part of a pending preview release. The content and the functionality may change and are not subject to the standard SLAs for support.


Sign in to your Google account and add the Microsoft 365 migration app to your Google account custom apps. 

1. From the [Migration page in the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern), under **Google**, select **Get started**.
2. Select **Connect to Google**. 
3. Sign in to Google Workspace. Sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization. Select **Next**.
4. Select **Go to Enterprise applications**. This step takes you to Azure.
5. Select the **Office 365 migration app**.
6. On the left-hand panel under *Security*, select **Permissions**.
7. Select **Grant admin consent** for your account. You may be prompted for your credentials again. Return to the Migration Manager wizard screen.  Select **Next**.
8. Select **Authenticate account**. 
9. Sign in to grant access to Google. Select **Authorize** and then **Grant access to Google**.
10. You're now connected to Google. Select **Finish** to close the window.

>[!Important]
>For security reasons, you have 10 minutes to complete the steps to connect to Google. After 10 minutes of inactivity, the session will expire.

[**Step 2: Scan and assess**](mm-Google-step2-scan-assess.md)


>[!NOTE]
>Migration Manager Google preview isn't available for users of Office 365 operated by 21Vianet in China. It's also not available for users of Microsoft 365 with the German cloud that use the data trustee *German Telekom*. It is supported for users in Germany whose data location isn't in the German datacenter.
>
> This feature is also not supported for users of the Government Cloud, including GCC, Consumer, GCC High, or DoD.