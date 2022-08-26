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

Instead of turning off external sharing entirely, you can address this issue by using a PowerShell cmdlet to block external access to new content until it has been scanned for sensitive content and DLP policies that include content-based conditions can be properly evaluated. This feature, named Sensitive by Default, will not block access to a document if the content in it has already been crawled and identified by the online service, but no sensitive content was found that matches the conditions in any DLP rules, or if the file has properties that match exemptions in DLP rules that allow it to be shared. Sensitive by Default will only block access to files that are subject to content-based DLP rules while the content is still being analyzed. Once a file has been crawled and no sensitive content that's against the rules in any DLP policy that would block sharing has been detected, guests can access the file. If the policy identifies sensitive content in the document that matches DLP rules, the normal behavior defined by those DLP rules will be applied. While the file is still being crawled for sensitive content, users will be prevented from accessing the file but instead of being told a rule has prevented access to the file, they will receive the following error message: "This file is being scanned right now. Please try again in a few minutes. If you still don't have access, contact the file owner."

> [!NOTE]
> This cmdlet applies to newly added files in all SharePoint sites and OneDrive accounts where a DLP policy is in place. It doesn't block sharing if an existing file is changed.

1. An additional impact of Sensitive by Default being enabled is that any content that isn't explicitly checked in a DLP policy will be blocked from being externally accessed. In other words, for content to be shareable externally, it will need to be in a location that’s covered by a DLP policy AND the policies for that location must determine, after content has been crawled and identified, that the file doesn’t match any rules that would prevent it from being shared. As a result, any location not checked by DLP policies will be non-shareable once this setting is enabled. If you want to operate under the principle that only locations explicitly checked by DLP can be shared externally, no further action is necessary. This is a good general principle since otherwise users are allowed to leak sensitive files as long as they put them in a location not covered by any DLP policies. On the other hand, if you prefer to only monitor and control sharing through specific locations while content can be shared in other locations without any sort of DLP-based control, you will need to create a “default” DLP rule that includes all SharePoint and OneDrive locations, that contains at least one rule with the “content contains” condition (for any content), and that doesn’t perform any action such as limiting or blocking the content, triggers any alerts, or generates any notifications or reports. This policy should be moved to the top of the list and not have the “stop processing more rules” option set, so it is only effective for content that doesn’t match any other DLP rule. As a result of such a rule, any file in any location that doesn’t match other DLP rules will be allowed for sharing. If you don’t create such a rule, any file that is not in a location covered by a DLP rule will be blocked from external sharing. [Learn how to create and turn on a DLP policy](/microsoft-365/compliance/create-test-tune-dlp-policy).

    > [!IMPORTANT]
    > Any content not in the scope of DLP policies would not be blocked for external access.

2. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

3. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

4. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault BlockExternalSharing 
    ```

    To disable this feature, run the following command:

    ```powershell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault AllowExternalSharing
    ```

> [!NOTE]
> It might take up to 60 minutes for this new setting to take effect.
