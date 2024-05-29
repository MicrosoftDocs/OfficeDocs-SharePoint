---
ms.date: 01/17/2020
title: "Prevent guest access to files while DLP rules are applied"
ms.reviewer: samust
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: how-to
ms.service: sharepoint-online
ms.collection: 
- M365-collaboration
- essentials-compliance
ms.localizationpriority: medium
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn how to block external sharing of newly added SharePoint and OneDrive files while they're scanned for DLP rules."
---

# Prevent guest access to files while DLP rules are applied

When new files are added to SharePoint or OneDrive in Microsoft 365, it takes a while for [Microsoft Purview Data Loss Prevention (DLP) policy](/microsoft-365/compliance/dlp-learn-about-dlp) to scan the content and apply rules to help protect sensitive content. If external sharing is turned on, sensitive content could be shared and accessed by guests before the DLP rule finishes processing.

Instead of turning off external sharing entirely, you can mark the files in your organization as sensitive by default. This blocks guest access to new content until it's scanned for sensitive content and DLP policies that include content-based conditions are applied. Guests are notified that the file is being scanned if they attempt to access it during this time.

Once a file is crawled and no content that would block sharing per DLP rules is detected, guests can access the file. If the policy identifies sensitive content in the document that matches DLP rules, the normal behavior defined by those DLP rules is applied. 

This feature doesn't block access to a file if:

- the content has already been crawled and no sensitive content was found that matches the conditions in any DLP rules,
- or if the file has properties that match exemptions in DLP rules that allow it to be shared. 

This feature applies to newly added files in SharePoint and OneDrive. It doesn't block sharing if an existing file is changed.

## DLP rules are required for content to be shared with guests

When this feature is enabled, any content that isn't explicitly checked in a DLP policy is blocked from being externally accessed. In other words, for content to be shareable externally, it must be in a location that's covered by a DLP policy and the policies for that location must determine, after content has been crawled and identified, that the file doesn't match any rules that would prevent it from being shared. This helps prevent users from leaking sensitive files by placing them in a location not covered by DLP policies.

If you want to operate under the principle that only locations explicitly checked by DLP can be shared externally, no further action is necessary. 

If you want to enable external sharing in locations not currently covered by DLP policies, you can create a DLP rule that includes all SharePoint and OneDrive locations that contain at least one rule with the “content contains” condition (for any content), and that doesn't perform any action (such as limiting or blocking the content), trigger any alerts, or generates any notifications or reports. This policy must be moved to the top of the list and not have the *stop processing more rules* option set, so it's only effective for content that doesn't match any other DLP rule. As a result of such a rule, any file in any location that doesn’t match other DLP rules will be allowed for external sharing.

For information about how to create a DLP rule, see [Learn how to create and turn on a DLP policy](/microsoft-365/compliance/create-test-tune-dlp-policy).

## Mark files as sensitive by default

This feature is configured using PowerShell.

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

1. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

1. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault BlockExternalSharing 
    ```

    To disable this feature, run the following command:

    ```powershell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault AllowExternalSharing
    ```

> [!NOTE]
> It might take up to 60 minutes for this new setting to take effect.

