---
title: "Conditional access policies for SharePoint sites"
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

# Conditional access policies for SharePoint sites

With [Azure Active Directory authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps#configure-authentication-contexts), you can enforce more stringent access conditions when users access SharePoint sites. You can directly apply an authentication context to a SharePoint site by using the [Set-SPOSite](/powershell/module/sharepoint-online/set-sposite) PowerShell cmdlet.

In the following example, an authentication context called MFA is attached to the site.

```powershell
Set-SPOSite -Identity https://contoso.sharepoint.com/sites/research -ConditionalAccessPolicy AuthenticationContext -AuthenticationContextName "MFA"
```
Additionally, authentication contexts are used with sensitivity labels to connect [Azure AD conditional access policies](/azure/active-directory/conditional-access/overview) to labeled sites.

Note that this capability can't be applied to the root site in SharePoint (for example, https://contoso.sharepoint.com).

## Requirements

Some apps do not currently work with authentication contexts. If you have Office apps or third party apps, we recommend testing them on a site with authentication context enabled before broadly deploying this feature. Currently, the following apps and scenarios do *not* work with authentication contexts:

- Older version of Office apps (see the [list of supported versions](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites#more-information-about-the-dependencies-for-the-authentication-context-option))
- Yammer
- Teams web app
- OneNote app can't be added to channel if the associated SharePoint site has an authentication context
- Teams private channel won't provision a SharePoint if the main team site has an authentication context
- Teams channel meeting recording upload fails on sites with an authentication context
- SharePoint folder renaming in Teams fails if the site has an authentication context
- Teams webinar scheduling fails if OneDrive has an authentication context
- Workflows that use Power Apps or Power Automate fails to work for sites with an authentication context
- Third-party apps
- The OneDrive sync app won't sync sites with an authentication context
- Copy or Move files from Site-A(no policy) to Site-B(with policy) fails

Using authentication context with SharePoint sites requires at least one of the below licenses:
- Microsoft 365 E5
- Microsoft 365 E5 Compliance
- Microsoft 365 E5 Information Protection and Governance


## Setting up an authentication context

Setting up an authentication context for labeled sites requires these basic steps:

1. Add an authentication context in Azure Active Directory.

2. Create a conditional access policy that applies to that authentication context and has the conditions and access controls that you want to use.

3. Set a sensitivity label to apply the authentication context to labeled sites.

In this article, we'll look at the example of requiring guests to agree to a [terms of use](/azure/active-directory/conditional-access/terms-of-use) before gaining access to a sensitive SharePoint site. You can also use any of the other conditional access conditions and access controls that you might need for your organization.

### Add an authentication context

First, add an authentication context in Azure Active Directory.

To add an authentication context
1. In [Azure Active Directory Conditional Access](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade), under **Manage**, click **Authentication context (Preview)**.

2. Click **New authentication context**.

3. Type a name and description and select the **Publish to apps** check box.

    ![Screenshot of add authentication context UI](media/aad-add-authentication-context.png)

4. Click **Save**.

### Create a conditional access policy

Next, create a conditional access policy that applies to that authentication context and that requires guests to agree to a terms of use as a condition of access.

To create a conditional access policy
1. In [Azure Active Directory Conditional Access](https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/ConditionalAccessBlade), click **New policy**.

2. Type a name for the policy.

3. On the **Users and groups** tab, choose the **Select users and groups** option, and then select the **All guest and external users** check box.

4. On the **Cloud apps or actions** tab, under **Select what this policy applies to**, choose **Authentication context (Preview)**, and select the check box for the authentication context that you created.

    ![Screenshot of authentication context options in cloud apps or actions settings for a conditional access policy](media/aad-authentication-context-ca-policy-apps.png)

5. On the **Grant** tab, select the check box for the terms of use that you want to use, and then click **Select**.

6. Choose if you want to enable the policy, and then click **Create**.

### Update a sensitivity label

Next, update a sensitivity label (or create a new one) to use the authentication context.

To update a sensitivity label
1. In the [Microsoft Purview compliance portal](https://compliance.microsoft.com/informationprotection), on the **Information protection** tab, click the label that you want to update and then click **Edit label**.

2. Click **Next** until you are on the **Define protection settings for groups and sites** page.

3. Ensure that the **External sharing and Conditional Access settings** check box is selected, and then click **Next**.

4. On the **Define external sharing and device access settings page**, select the **Use Azure AD Conditional Access to protect labeled SharePoint sites** check box.

5. Select the **Choose an existing authentication context (preview)** option.

6. In the dropdown list, choose the authentication context that you want to use.

    ![Screenshot of Azure AD authentication context sensitivity label settings](media/aad-authentication-context-label-setting.png)

7. Click **Next** until you are on the **Review your settings and finish** page, and then click **Save label**.

Once the label has been updated, guests accessing a SharePoint site (or the **Files** tab in a team) with that label will be required to agree to the terms of use before gaining access to that site.

## See also

[Use sensitivity labels to protect content in Microsoft Teams, Microsoft 365 groups, and SharePoint sites](/microsoft-365/compliance/sensitivity-labels-teams-groups-sites)

[Conditional Access: Cloud apps, actions, and authentication context](/azure/active-directory/conditional-access/concept-conditional-access-cloud-apps)

[Microsoft 365 licensing guidance for security & compliance](/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)
