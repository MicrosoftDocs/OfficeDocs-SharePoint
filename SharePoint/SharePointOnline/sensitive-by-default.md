---
title: "Sensitive by default"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn how to block external sharing of newly uploaded files."
---

# Sensitive by default

When new files are added to SharePoint or OneDrive, it takes a while for them to be crawled and indexed. It takes additional time for the Office Data Loss Prevention (DLP) policy to scan the content and apply rules to help protect sensitive content. If external sharing is turned on, sensitive content may be accessed by guests before the Office DLP rule finishes processing. If you turn off external sharing to prevent this, you disable important collaboration scenarios.  

[Learn more about data loss prevention](/microsoft-365/compliance/data-loss-prevention-policies)

To address this issue, you can use a new PowerShell cmdlet to prevent guests from accessing newly added files until at least one Office DLP policy scans the content of the file. If the file has no sensitive content based on the DLP policy, then guests can access the file. But if the policy identifies sensitive content, then guests will not be able to access the file. 

> [!NOTE]
> This cmdlet applies to newly added files in all SharePoint sites. It doesn't block sharing if an existing file is changed, and it doesn't block sharing for files in OneDrive.

1. Make sure you have at least one DLP policy enabled in your organization for content located in SharePoint.

2. [Download the latest SharePoint Online Management Shell version](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall “SharePoint Online Management Shell.” <br>On the Download Center page, select your language and then click the Download button. You’ll be asked to choose between downloading a x64 and x86 .msi file. Download the x64 file if you’re running the 64-bit version of Windows or the x86 file if you’re running the 32-bit version. If you don’t know, see https://support.microsoft.com/help/13443/windows-which-operating-system. After the file downloads, run it and follow the steps in the Setup Wizard. 
    
3. Connect to SharePoint Online as a global admin or SharePoint admin in Office 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).
    
4. Run the following command:
  
    ```PowerShell
    Set-SPOTenant -MarkNewFilesSensitiveByDefault BlockExternalSharing 
    ```

To disable this feature, run `Set-SPOTenant -MarkNewFilesSensitiveByDefault AllowExternalSharing`. 



