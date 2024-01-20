---
ms.date: 09/08/2021
title: "View SharePoint files with File Explorer in Microsoft Edge"
ms.reviewer:
ms.author: jhendr
author: JoanneHendrickson
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:
- Strat_SP_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid:
- SPO160
- BSA160
- GSP150
- MET150
description: "Learn about SharePoint view in File Explorer for Edge."
---

# View SharePoint files with File Explorer in Microsoft Edge

Last year, we announced that Microsoft 365 apps and services would no longer support Internet Explorer 11 (IE 11). As a result, we no longer recommend View in File Explorer and encourage using the OneDrive sync client. The OneDrive sync client provides [Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e), which allows you to access all your files in SharePoint without using up local storage space. For info about using OneDrive to sync SharePoint files, visit [SharePoint file sync](sharepoint-sync.md).

By default, the View in File Explorer menu option will not be visible to you or users in the SharePoint modern document library interface. In certain cases, organizations may still need to use View in File Explorer to access modern document libraries. Starting in Microsoft Edge Stable version 93, you can enable the View in File Explorer capability on SharePoint for modern document libraries.

## Configure View in File Explorer with Edge

Follow the steps below to use View in File Explorer in Microsoft Edge:

1. Verify that devices are on Microsoft Edge build 93 or later using [Find out which version of Microsoft Edge you have](https://support.microsoft.com/en-us/microsoft-edge/find-out-which-version-of-microsoft-edge-you-have-c726bee8-c42e-e472-e954-4cf5123497eb).

2. Ensure that Windows instances are joined to a Microsoft Active Directory domain, Windows 10 Pro, or Enterprise instances that are enrolled for device management.

3. Enable the [ConfigureViewInFileExplorer](/deployedge/microsoft-edge-policies#configureviewinfileexplorer) policy for Microsoft Edge that allows URLs with the viewinfileexplorer: scheme to open WebDAV URLs in Windows File Explorer. 

Use the options below to enable View in File Explorer using group policy or Intune:

   - **To enable by using group policy**:

     1. Configure Microsoft Edge policy settings by following the steps at [Configure Microsoft Edge policy settings on Windows](/deployedge/configure-microsoft-edge).

     2. Make sure you've downloaded the Microsoft Edge administrative template at [Download and deploy Microsoft Edge for business](https://www.microsoft.com/edge/business/download) or you may not see the policy listed.

     3. Once the template is downloaded, open the Group Policy Object Editor. Right-click **Administrative Templates** in the Computer Configuration or User Configuration node and select **Add/Remove Templates** and browse to the downloaded template.

     4. When applying the policy, ensure you update the domain to your tenant domain or use **sharepoint.com** if you plan on visiting multiple SharePoint tenants.

     5. Enabling the group policy may require a refresh of client group policy settings. After changing the group policy settings, refresh the settings. From a Command Prompt, enter **GPUpdate.exe /force**.

        Example below with the Group Policy value:

        `[{"cookies": ["rtFa", "FedAuth"], "domain": "contoso.sharepoint.com"}]`

        :::image type="content" source="media/edgepolicy-adeejoseph.png" alt-text="Enable Configure the View in File Explorer feature for SharePoint pages in Microsoft Edge":::

        For more examples, see [ConfigureViewInFileExplorer](/deployedge/microsoft-edge-policies#configureviewinfileexplorer) on Microsoft Edge policy reference.

   - **To enable by using Intune**:

     Configure Microsoft Edge policy settings by following the steps at [Configure Microsoft Edge policy settings with Microsoft Intune](/deployedge/configure-edge-with-intune).

5. Verify the policy has been enabled by opening Microsoft Edge and navigating to Edge://policy/.

    :::image type="content" source="media/microsoft-edge-policy.png" alt-text="Snapshot of Microsoft Edge Policies page ":::

    > [!TIP]
    > You may need to close and re-open Microsoft Edge for the policy to appear.

6. As a tenant administrator, update your SharePoint Online tenant configuration via SharePoint Online Management Shell to allow the "View in File Explorer" option to be visible in the Microsoft Edge Browser interface with these steps:

    1. Connect to SharePoint Online Management Shell by running:

        ```PowerShell
        Connect-SPOService -Url https://contoso-admin.sharepoint.com
        ```

    1. Run the following cmdlet to show the "View in File Explorer" menu option:

        ```PowerShell
        Set-SPOTenant -ViewInFileExplorerEnabled $True
        ```

        > [!NOTE]
        > Ensure the management shell version is 16.0.21610.12000 or higher or the ViewInFileExplorerEnabled option will not be available.

7. **(Required)** _View in File Explorer_ requires persistent cookies to operate correctly; when you sign in, select **Yes** when the **Stay signed in?** prompt appears.

    You can locate the View in Explorer button by navigating to the **Library** >  Select the **Library View Menu** on the right-hand side > Select **View In File Explorer**.

    :::image type="content" source="media/view-in-file-explorer.png" alt-text="Menu for View in File Explorer":::

    > [!NOTE]
    > Once the tenant setting has been enabled, it may take up to 15 minutes for the View in Explorer button to appear in the SharePoint interface.

### Troubleshooting

**How can I confirm that the ConfigureViewInFileExplorer policy has been applied?**

You can verify that the policy has been applied by navigating to **edge://policy**.

**The error message _This policy is blocked - its value will be ignored_ appeared while checking to see if the policy was applied via edge://policy. What's wrong?**

This error will occur when you attempt to apply this policy to a non-domain joined device. Currently, the ConfigureViewInFileExplorer policy can only be applied to Windows instances that are joined to a Microsoft Active Directory domain, Windows 10 Pro, or Enterprise instances enrolled for device management.

:::image type="content" source="media/edge-error.png" lightbox="media/edge-error.png" alt-text="User interface of the 'This policy is blocked - its value will be ignored' error message.":::

**What happens if I have the policy applied without the tenant setting enabled?**

If you don't enable ViewInFileExplorerEnabled via [Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant?view=sharepoint-ps&preserve-view=true), the View in File Explorer button will not appear in the interface of the SharePoint site.

**What happens if the tenant setting is enabled without the Edge policy applied?**

If you have enabled ViewInFileExplorerEnabled, you may see the View In File Explorer button appear in your SharePoint library, however, clicking the button will result in a blank screen.

:::image type="content" source="media/edgepolicy-blank-screen.png" alt-text="Blank screen that appears when the tenant setting is enabled without the policy applied.":::

**When running Set-SPOTenant -ViewInFileExplorerEnabled $True I received the error "The requested operation is part of an experimental feature that is not supported in the current environment". What's wrong?**

You may receive this error if this functionality is not supported in your current environment. We are still rolling out functionality to all Production environments and will update this article once worldwide rollout has been completed.

## Learn More

- [Sync SharePoint and Team files with your computer](https://support.microsoft.com/office/sync-sharepoint-and-teams-files-with-your-computer-6de9ede8-5b6e-4503-80b2-6190f3354a88)
- [View and open SharePoint with File Explorer](https://support.microsoft.com/office/view-and-open-sharepoint-files-with-file-explorer-66b574bb-08b4-46b6-a6a0-435fd98194cc)
- [Troubleshoot View in File Explorer](/sharepoint/troubleshoot/lists-and-libraries/troubleshoot-issues-using-open-with-explorer)
- [Set-SPOTenant](/powershell/module/sharepoint-online/set-spotenant?view=sharepoint-ps&preserve-view=true)
- [OneDrive sync reports in the Apps Admin Center](/onedrive/sync-health)

