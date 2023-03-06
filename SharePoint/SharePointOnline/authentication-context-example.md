---
ms.date: 03/01/2023
title: "Conditional access policy for SharePoint sites and OneDrive"
ms.reviewer: samust
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
-  Adm_O365
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- M365-collaboration
search.appverid:
- MET150
description: "Learn about how to use Azure Active Directory conditional access and authentication context with SharePoint sites and sensitivity labels."
---

# Conditional access policy for SharePoint sites and OneDrive

[!INCLUDE[Advanced Management](includes/advanced-management.md)]

With [Azure Active Directory authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps#configure-authentication-contexts), you can enforce more stringent access conditions when users access SharePoint sites. 

You can use authentication contexts to connect an [Azure AD conditional access policy](/azure/active-directory/conditional-access/overview) to a SharePoint site. Policies can be applied directly to the site or via a sensitivity label.

Note that this capability can't be applied to the root site in SharePoint (for example, https://contoso.sharepoint.com).

## Requirements

Using authentication context with SharePoint sites requires one of the following licenses:

- Microsoft Syntex - SharePoint Advanced Management
- Microsoft 365 E5/A5/G5
- Microsoft 365 E5/A5/G5/F5 Compliance
- Microsoft 365 E5/F5 Information Protection and Governance
- Office 365 E5/A5/G5

## Limitations

Some apps don't work with authentication contexts. We recommend testing apps on a site with authentication context enabled before broadly deploying this feature.

The following apps and scenarios don't work with authentication contexts:

- Older version of Office apps (see the [list of supported versions](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites#more-information-about-the-dependencies-for-the-authentication-context-option))
- Yammer
- Teams web app
- OneNote app can't be added to channel if the associated SharePoint site has an authentication context
- Teams private channel won't provision a SharePoint site if the main team site has an authentication context
- Teams channel meeting recording upload fails on sites with an authentication context
- SharePoint folder renaming in Teams fails if the site has an authentication context
- Teams webinar scheduling fails if OneDrive has an authentication context
- Workflows that use Power Apps or Power Automate fails to work for sites with an authentication context
- Third-party apps
- The OneDrive sync app won't sync sites with an authentication context
- Copy or move files from a site with no authentication context to a site with an authentication context fails

## Setting up an authentication context

Setting up an authentication context for labeled sites requires these basic steps:

1. Add an authentication context in Azure Active Directory.

1. Create a conditional access policy that applies to that authentication context and has the conditions and access controls that you want to use.

1. Do one of the following:

    1. Set a sensitivity label to apply the authentication context to labeled sites.
    1. Apply the authentication context directly to a site

In this article, we'll look at the example of requiring guests to agree to a [terms of use](/azure/active-directory/conditional-access/terms-of-use) before gaining access to a sensitive SharePoint site. You can also use any of the other conditional access conditions and access controls that you might need for your organization.

### Add an authentication context

First, add an authentication context in Azure Active Directory.

To add an authentication context
1. In [Azure Active Directory Conditional Access](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade), under **Manage**, click **Authentication context**.

2. Click **New authentication context**.

3. Type a name and description and select the **Publish to apps** check box.

    ![Screenshot of add authentication context UI](media/aad-add-authentication-context.png)

4. Click **Save**.

### Create a conditional access policy

Next, create a conditional access policy that applies to that authentication context and that requires guests to agree to terms of use as a condition of access.

To create a conditional access policy
1. In [Azure Active Directory Conditional Access](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade), click **New policy**.

1. Type a name for the policy.

1. On the **Users and groups** tab, choose the **Select users and groups** option, and then select the **Guest or external users** check box.

1. Choose **B2B collaboration guest users** from the dropdown.

1. On the **Cloud apps or actions** tab, under **Select what this policy applies to**, choose **Authentication context**, and select the check box for the authentication context that you created.

    ![Screenshot of authentication context options in cloud apps or actions settings for a conditional access policy.](media/aad-authentication-context-ca-policy-apps.png)

1. On the **Grant** tab, select the check box for the terms of use that you want to use, and then click **Select**.

1. Choose if you want to enable the policy, and then click **Create**.

### Apply the authentication context directly to a site

You can directly apply an authentication context to a SharePoint site by using the [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) PowerShell cmdlet.

> [!NOTE]
> This capability requires a Microsoft 365 E5 or Microsoft Syntex - SharePoint Advanced Management license.

In the following example, we apply the authentication context we created above to a site called "research."

```powershell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/research -ConditionalAccessPolicy AuthenticationContext -AuthenticationContextName "Sensitive information - guest terms of use"
```

### Set a sensitivity label to apply the authentication context to labeled sites

If you want to use a sensitivity label to apply the authentication context, update a sensitivity label (or create a new one) to use the authentication context.

> [!NOTE]
> Sensitivity labels require Microsoft 365 E5 or Microsoft 365 E3 plus the Advanced Compliance license.

To update a sensitivity label
1. In the [Microsoft Purview compliance portal](https://compliance.microsoft.com/informationprotection), on the **Information protection** tab, click the label that you want to update and then click **Edit label**.

2. Click **Next** until you are on the **Define protection settings for groups and sites** page.

3. Ensure that the **External sharing and Conditional Access settings** check box is selected, and then click **Next**.

4. On the **Define external sharing and device access settings page**, select the **Use Azure AD Conditional Access to protect labeled SharePoint sites** check box.

5. Select the **Choose an existing authentication context** option.

6. In the dropdown list, choose the authentication context that you want to use.

    ![Screenshot of Azure AD authentication context sensitivity label settings](media/aad-authentication-context-label-setting.png)

7. Click **Next** until you are on the **Review your settings and finish** page, and then click **Save label**.

Once the label has been updated, guests accessing a SharePoint site (or the **Files** tab in a team) with that label will be required to agree to the terms of use before gaining access to that site.

## See also

[Use sensitivity labels to protect content in Microsoft Teams, Microsoft 365 groups, and SharePoint sites](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites)

[Conditional Access: Cloud apps, actions, and authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps)

[Microsoft 365 licensing guidance for security & compliance](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

