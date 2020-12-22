---
title: "Disable "Get help" and "Send feedback" in OneDrive"
ms.reviewer: 
ms.author: 
author: 
manager: 
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
localization_priority: Normal
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- ODB160
- ODB150
- MET150
ms.assetid: 7d7168dd-9015-4245-a971-61b504f834d6
description: "This article contains information about the OneDrive sync app (onedrive.exe) when used for OneDrive for work or school in Microsoft 365 Business or Microsoft 365 Apps for business (when people sign in with a work or school account)."
---

# Disable "Get help" and "Send feedback" in OneDrive

> [!NOTE]
> To determine which OneDrive sync client you're using, see  [Which OneDrive app?](https://support.microsoft.com/en-us/office/which-onedrive-app-19246eae-8a51-490a-8d97-a645c151f2ba)

OneDrive for work or school lets people contact Microsoft directly from inside the application. People generate support tickets for OneDrive for work or school by selecting **Get help** and continuing to the **Contact support** link in the help pane. They may also send feedback to Microsoft through **Send feedback** and will occasionally be prompted with user satisfaction surveys.

:::image type="content" source="media/Img1-4717638" alt-text="":::

## Disable Get Help and Send Feedback
As an administrator, you may want to disable these support features to prevent people in your organization from contacting Microsoft directly.

Disabling support features will remove the option to contact support or send feedback through the help pane. Your users can still select **Get help** to view help and training topics, and **Feedback** will also be available to allow users to share ideas on the [User Voice](https://onedrive.uservoice.com/) page.

The screenshots below show the changes after you disable the support features: 

:::image type="content" source="media/Img2-4717638" alt-text="":::

:::image type="content" source="media/Img3-4717638" alt-text="":::

> [!IMPORTANT]
> Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, [back up the registry for restoration](https://support.microsoft.com/help/322756/how-to-back-up-and-restore-the-registry-in-windows) in case problems occur.

1. In Registry Editor, locate the following subkey: **HKEY_CURRENT_USER\Software\Microsoft\OneDrive**

2. Right-click **OneDrive**, select **New**, and then click **DWORD** Value.

3. Type **DisableReportProblemDialog** for the name.

4. Right-click the new registry key, type **1** for **Value data**, and then click **OK**.

Additionally, a SharePoint in Microsoft 365 tenant administrator can run the following cmdlet to enable or disable the "report a problem" feature for any Windows clients connecting to that tenant.

**Set-SPOTenantSyncClientRestriction -DisableReportProblemDialog $true**

**Set-SPOTenantSyncClientRestriction -DisableReportProblemDialog $false**

Contacting support can be disabled for Mac clients by adding a preference to defaults:

For Mac Standalone clients:
**defaults write com.microsoft.OneDrive DisableReportProblemDialog 1**

For Mac App Store clients:

**defaults write com.microsoft.OneDrive-mac DisableReportProblemDialog 1**

> [!NOTE]
> Disabling **Send feedback** and **Get help** only disables the capability for OneDrive for work or school to report an issue to Microsoft. This doesn't prevent people from selecting **Send feedback** if they use the sync app when signed in with a personal account.

