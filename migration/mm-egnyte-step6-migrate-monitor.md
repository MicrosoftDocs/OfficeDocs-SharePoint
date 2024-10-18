---
ms.date: 05/12/2020
title: "Step 6: Migrate and monitor Egnyte migration"
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
ms.collection: 
- m365solution-migratefileshares
- m365solution-migratetom365
- m365solution-scenario
- M365-collaboration
- SPMigration
- highpri
- m365initiative-migratetom365
search.appverid: MET150
ROBOTS: NOINDEX
description: "Step 6: Migrate and monitor Egnyte migration"
---
# Step 6:  Migrate and monitor your Egnyte migration

Once have reviewed the accounts, confirmed the destinations, correctly mapped identities, you're ready to migrate.

>[!Important]
>We strongly recommend that you do not rename or move migrated files before the final migration has been completed.  Doing so will result in files being overwritten.


1. Select the accounts to migrate.
2. Select **Migrate**.

![Select migrate button](media/mm-box-migrate-button.png) 

3. A confirmation step displays.  Select **Migrate**.  

>[!Note]
> Starting your migration only copies content from your Egnyte account to the location you have specified in Microsoft 365.  Make sure the destinations are correct, as once the migration starts, they cannot be modified.

4. Once the migration begins, monitor the migration status, and the table summary at the top.  Depending on how large your migration, this step can take hours or days.


## How many task rows can I run at once?

At a maximum, only 50 task rows can run simultaneously. This total includes both scanning and migrating.

If you select more than that total combined number and start scanning or migrating, only 50 randomly chosen rows run. The rest is queued.

As a task row completes, another from the queue starts migrating or scanning automatically. The maximum allowed is 50 task rows. However, if a migration experiences any slowdowns or back-off requests, it can drop lower than this number to keep the migration stable.

