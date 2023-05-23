---
ms.date: 09/22/2020
title: "Control Microsoft Lists"
ms.reviewer: hasaladi
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
- MET150
ms.collection:
- M365-collaboration
description: "Control settings in the Lists app."
---

# Control settings for Microsoft Lists

As a Global Administrator or SharePoint Administrator in Microsoft 365, you can control settings for Microsoft Lists. You can:

- Disable the creation of personal lists (prevent users from saving new lists to "My lists").
- Disable built-in list templates that aren't relevant for your organization.

You control both of these settings by using Microsoft PowerShell.

## Disable creation of personal lists

If you change this setting, when users create a list, they must select a SharePoint site for saving the list. The "Save to" setting doesn't include the "My lists" option.

|Default|Personal list creation disabled|
|---|---|
|![The Save to setting includes the My lists option](media/save-my-lists.png) |![The Save to setting requires users to select a site](media/save-list-site.png)|

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

    ```PowerShell
    Set-SPOTenant -DisablePersonalListCreation $true
    ```

To re-enable the creation of personal lists, set the parameter to `$false`.

## Disable built-in list templates

Disabling these templates removes them from all places users create lists (the Lists app, Microsoft Teams, and SharePoint sites).

|Default|Built-in list templates disabled|
|---|---|
|![All built-in templates are available to users](media/list-templates-all.png) |Some templates disabled![Some templates are still available to users](media/list-templates-some.png) <br/> All templates disabled![Users see a message that templates have been turned off by the admin](media/list-templates-none.png)|

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

    ```PowerShell
    Set-SPOTenant -DisableModernListTemplateIds '<template ID>'
    ```

Where the template ID is:

- Issue tracker: 'C147E310-FFB3-0CDF-B9A3-F427EE0FF1CE'
- Employee onboarding: 'D4C4DAA7-1A90-00C6-8D20-242ACB0FF1CE'
- Event itinerary: '3465A758-99E6-048B-AB94-7E24CA0FF1CE'
- Asset manager: 'D2EDA86E-6F3C-0700-BE3B-A408F10FF1CE'
- Recruitment tracker: '3A7C53BE-A128-0FF9-9F97-7B6F700FF1CE'
- Travel requests: 'C51CF376-87CF-0E8F-97FF-546BC60FF1CE'
- Work progress tracker: 'B117A022-9F8B-002D-BDA8-FA266F0FF1CE'
- Content scheduler: '9A429811-2AB5-07BC-B5A0-2DE9590FF1CE'
- Incidents: 'E3BEEF0B-B3B5-0698-ABB2-6A8E910FF1CE'
- Patient care coordination: '0134C13D-E537-065B-97D1-6BC46D0FF1CE'
- Loans: '7C920B56-2D7A-02DA-94B2-57B46E0FF1CE'
- Gift ideas: '008F8143-9644-0238-B4B5-C03E4F0FF1CE'
- Recipe tracker: 'A1755E7D-8E3A-4141-89FC-6C77EB0FF1CE'
- Expense tracker: '96D6DBE5-D7C3-030A-867A-0B72EB0FF1CE'
- Travel requests with approvals: '4EB20749-6360-417C-83DD-06135C0FF1CE'
- Content scheduler with approvals: 'C381BD64-C1A1-4D9E-BE9C-0571900FF1CE'

To re-enable a built-in template, use the parameter `EnableModernListTemplateIds`.

## Disable additional features on a built-in template

Some built-in list templates include additional features such as automations and custom formatting. If you wish to keep only the base schema of a built-in list template but not the rest of its features included in that template:

1. Create a list from the built-in list template.
2. [Create a custom list template](lists-custom-template.md) based off of that list. The custom list template will not include any additional features by default.
3. [Disable the original built-in list template](#disable-built-in-list-templates). 

    > [!NOTE]
    > Users in your organization will see the custom list template on the **From your organization** tab rather than on the **From Microsoft** tab.

