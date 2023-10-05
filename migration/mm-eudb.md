---
title: "Migration Manager and the European Union Data Boundary (EUDB)"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection: 
- M365-collaboration
- SPMigration
- m365initiative-migratetom365
search.appverid: MET150
description: Learn about the changes to Migration Manager for the European Union Data Boundary.
---

# Migration Manager and the European Union Data Boundary (EUDB)

>[!Note]
>This article only applies to customers whose Microsoft 365 tenant exists within the boundaries of the European Union (EU). **Only customers who had existing migrations before April 1st** will see the US and EU projects listed in the UI.
>
>All migrated data will reside in the EU OneDrive-Sharepoint farm, regardless of this change.


>[!Important]
>Beginning April 1, 2023, all new European Union (EU) scans and migrations, will be processed in the EU.
>You may continue to run existing migrations, except for Steam, until September 30, 2023. Starting October 1, 2023, you will no longer have access to migration projects created in the United States (US).
>
>Stream migrations created before April 1, 2023 may continue to run in the US project until February 15, 2024.

The Migration Manager Platform (MMP) is the platform for Migration Manager, the tool that enables migrations from file share and cloud storage platform sources to Microsoft 365. 

The European Union Data Boundary (EUDB) is a geographically defined boundary within which Microsoft has committed to store and process customer data for our major commercial enterprise online services, including Azure, Dynamics 365, Power Platform, and Microsoft 365, subject to limited circumstances where customer data will continue to be transferred outside the EU Data Boundary.

MMP currently has one project based in the United States (US) farm, serving all global migration traffic. Starting April 1, 2023, a second project based in the European Union (EU) will be available for all migration projects except Stream. Stream's second project will be available starting April 15, 2023.

A phased implementation schedule for existing EU customers is listed below.

>[!Tip]
>Learn more about the Microsoft commitment to our European Union (EU) and European Free Trade Association (EFTA) customers to help them process and store customer data in their region:  [EU Data Boundary for the Microsoft Cloud](https://www.microsoft.com/en-us/trust-center/privacy/european-data-boundary-eudb)

## Timeline overview

|Date|Change|
|:-----------|:-----|
|April 1, 2023|The file share **Scans** tab becomes read only for US projects.|
|April 1, 2023|All new migrations will be processed in the EU. EU Admins, except for Stream admins, can choose to restart their projects in the EU project or continue their migration in the US project.|
|April 15, 2023|Stream EU admins can choose to restart their migrations in the EU project or continue with their migration in the US project.|
|September 30, 2023|With the exception of Steam, all active migrations must be in the US project must be completed.|
|October 1, 2023|Scans and migrations in the US project will no longer be accessible.|
|February 15, 2024|Stream migrations initiated in the US project must be completed. Migrations won't be accessible after this date.| 


## What does that mean for me?

>[!Important]
>- **Only customers who had existing migrations before April 1st** will see the US and EU projects listed in the UI.
>  
>- **No changes will be visible if you are a new customer or have never created a migration.** Migrations you create will be processed in the EU.
>
>- [**Microsoft 365 Multi-Geo**](/microsoft-365/enterprise/microsoft-365-multi-geo)  Capabilities Add-on that enables customers to expand their Microsoft 365 presence to multiple geographic regions or countries **isn't** in scope for the EU Data Boundary. 


|If you have...|Impact to you|Recommendation|
|:---------------|:-----|:-----|
|No existing migrations|None|No action required.|
|Active migrations*</br></br> (*except **Stream**)|You've until September 30, 2023 to complete active migrations. You can choose to restart your scans and migrations in the EU project starting April 1, 2023. As of October 1, 2023, you'll no longer have access to US projects. |We recommend completing existing US migration tasks or restart a new migration in the EU project at your earliest convenience.|
|File share Scans|File share scans in the US project can be accessed until April 1, 2023, at which point they become read only.|Start running new scans in the EU.|
|Active Stream migrations|Stream migrations created before April 1, 2023 may continue to run in the US project until February 15, 2024. After that date, the migrations will be removed. |Complete your Stream migration before February 15, 2024.|

## How to change the agent configuration for file share migrations

>[!Important]
>After April 1,  the **Scans** tab for File Share migrations becomes read-only for US projects. 

The state of File share Agents will automatically change as follows:

Under the **Agents** tabs:
- For **US projects** the agent state (status) will change from "Enabled' to "Cannot scan". 
- For **EU projects** agent state (status) will show "Enabled". You can only run scans in the EU project.

If running scan tasks in the US project is important for your business, you must configure each agent to connect to the US project. 

1. Open the **Task Manager** app and then select the **Services** tab.
2. Right-click **SharePoint Migration Service** and then select **Stop**.
3. **Open** this file:

    %AppData%\Microsoft\SPMigration\bin\Microsoft.SharePoint.Migration.ClientShared.dll.config

4. Under AppSettings, add the following:

```powershell 
 
<add key="UseUSScan" value="1" />

```

:::image type="content" source="media/mm-filesshare-scan-edit-eudb.png" alt-text="configure for us":::

5. Return to **Task Manager**. Right-click **SharePoint Migration Service** and then select **Start**
