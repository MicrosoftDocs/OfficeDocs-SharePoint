---
title: "Mark new files as sensitive by default"
ms.reviewer: samust
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn how to block external sharing of newly added files."
---

# Mark new files as sensitive by default

When new files are added to SharePoint or OneDrive in Microsoft 365, it takes a while for them to be crawled and indexed. It takes time for the [Microsoft Purview Data Loss Prevention (DLP) policy](/microsoft-365/compliance/dlp-learn-about-dlp) to scan the content and apply rules to help protect sensitive content. If external sharing is turned on, sensitive content could be shared and accessed by guests before the Office DLP rule finishes processing.

Instead of turning off external sharing entirely, you can address this issue by using a PowerShell cmdlet to block external access to new content. However, this doesn't work if external sharing is explicitly authorized in a DLP rule and the lack of sensitive content that goes against the policy rules has been verified. The setting enabled by this cmdlet prevents external users from accessing newly added files until at least one Office DLP policy scans the content and determines that the document doesn't contain any sensitive information that's against the rules defined in the policy. If the file has been indexed and scanned and it has no sensitive content that's against the rules in the DLP policy, then guests can access the file. If the policy identifies sensitive content in the document, or if there's no DLP rule explicitly authorizing access to the file, then guests won't be able to access the file, and they'll receive the following access denied error message: "This file is being scanned right now. Please try again in a few minutes. If you still don't have access, contact the file owner."


> [!NOTE]
> This cmdlet applies to newly added files in all SharePoint sites and OneDrive accounts where a DLP policy is in place. It doesn't block sharing if an existing file is changed.

1. Since any content that isn't explicitly checked in a DLP policy will not be blocked from being externally accessed after this setting is enabled, you must ensure any content that needs to be shared externally is covered by at least one DLP policy. If you prefer to require explicit authorization in a DLP policy for a site to be shareable, no further action is needed after this setting is enabled. If not all locations with content that needs to be shared externally are already covered by an existing DLP policy, you must add them to at least one policy. The easiest way to do this is to create a DLP policy that includes all SharePoint or OneDrive locations, that has any “content contains” condition selected, and that specifies no actions, no alerts, no notifications and no reports. Also, make sure the rule doesn’t use the option to stop processing more DLP rules. [Learn how to create and turn on a DLP policy](/microsoft-365/compliance/create-test-tune-dlp-policy)

    > [!IMPORTANT]
    > Any content not in the scope of DLP policies would not be blocked for external access.

2. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

3. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
4. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault BlockExternalSharing 
    ```

    To disable this feature, run the following command:

    ```powershell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault AllowExternalSharing
    ```

> [!NOTE]
> It might take up to 60 minutes for this new setting to take effect.
