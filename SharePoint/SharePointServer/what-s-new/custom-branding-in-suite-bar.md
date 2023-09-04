---
title: "Custom branding in Suite Navigation Bar"
ms.reviewer: 
ms.author: v-smandalika
author: v-smandalika
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: overview
ms.date: 08/31/2023
ms.service: sharepoint-server-itpro
ms.localizationpriority: high
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the Custom Branding feature which is one of the newly introduced features in SharePoint Server Subscription Edition Version 23H2."
---

# Custom branding in Suite Navigation Bar

[!INCLUDE[appliesto-xxx-xxx-xxx-SUB-xxx-md](../includes/appliesto-xxx-xxx-xxx-SUB-xxx-md.md)]

This article describes the "Custom branding in Suite Navigation Bar" feature, which is one of the new features introduced in the SharePoint Server Subscription Edition Version 23H2 feature update.

## Custom branding in the Suite Navigation Bar

The SharePoint Server modern UX provides a powerful yet intuitive user interface that scales from desktop to mobile devices. However, the architecture of the modern UX limited the opportunities for organizations to apply custom branding to the Suite Navigation Bar, which is the global navigation bar that provides access to the App Launcher, contextual settings menu, and user welcome control in SharePoint sites.

SharePoint Server Subscription Edition Version 23H2 introduces the ability for organizations to apply custom branding in the Suite Bar to better align with their branding standards. SharePoint farm administrators can specify and update the following attributes of the Suite Navigation Bar: 

- **SuiteNavAllowOverwrite**: Determines whether the Suite Navigation Bar settings of the web application can be overridden at the site-collection level. The default value is **false**, meaning any attempt to customize the Suite Navigation Bar at the site collection-level will be ignored. When this attribute's value is set to **true**, the web application-level Suite Navigation Bar settings apply to all site collections, except those collections to which explicit customizations have been made.

- **SuiteNavBrandingText**: Specifies the branding text of the Suite Navigation Bar.

- **SuiteNavBrandingLogoUrl**: Specifies a URL location that points to your logo. Ensure that the logo is from within the web application. The logo can be in the BMP, JPG, JPE, JPEG, PNG, GIF, or SVG format.

- **SuiteNavBrandingLogoTitle**: Specifies the title of your logo.

- **SuiteNavBrandingLogoNavigationUrl**: Specifies the URL to which users will navigate when they select the branding text or the logo.

- **SuiteBarBackground**: Sets a color to use for the background of the Suite Navigation Bar. The Suite Navigation Bar appears at the top on every page of your web application. The color value should be in the form #AARRGGBB, #RRGGBB, or #RGB as hex values.

- **SuiteBarText**: Sets a color to use for the text and icons on the Suite Navigation Bar.

- **SuiteNavAccentColor**: Sets a color to use for the background color of buttons on the Suite Navigation Bar when you hover on them.

### Example 1

1. Set **IsTAPCustomer farm-level** property to **1**.

   ```$farm = Get-SPFarm
      $farm.Properties["IsTAPCustomer"] = "1"
      $farm.Update()
   ```

2. Set the feature release preference for the farm to **early** by running the following command:

   `Set-SPFeatureReleasePreference -FeatureReleaseRing Early`

3. Run the SharePoint Configuration Wizard to ensure the two changes (implemented in Steps 1 and 2) are applied.

4. Enable a web application to allow custom branding by setting the **SuiteNavAllowCustom** web app-level property to **true**. This property must be set to **true** for any of the other properties to take effect.

   ```$webapp = Get-SPWebApplication http://spwfe
      $webapp.SuiteNavAllowCustom = $true
      $webapp.Update()
   ```

5. Set all the options, as shown in the following command-syntax example:

   ```$webapp.SuiteNavBrandingText = "Suite Bar Branding"
      $webapp.SuiteNavBrandingLogoUrl = "http://spwfe/Photos/IMG_5004-1-scaled.jpg"
      $webapp.SuiteNavBrandingLogoTitle = "Logo Branding"
      $webapp.SuiteNavBrandingLogoNavigationUrl = "https://www.microsoft.com/"
      $webapp.SuiteBarBackground = '#eed5b7'           
      $webapp.SuiteNavAccentColor = '#7fffd4'
      $webapp.SuiteBarText = '#000000'
      $webapp.update()
   ```

The site page prior to the custom branding being applied is as shown in the following screenshot:

:::image type="content" source="../media/site-page-prior-to-custom-branding.png" alt-text="Screenshot that shows the site page prior to the custom branding being applied." lightbox="../media/site-page-prior-to-custom-branding.png":::

The site page after applying the custom branding feature is as shown in the following screenshot:

:::image type="content" source="../media/site-page-after-custom-branding.png" alt-text="Screenshot that shows the site page after applying the custom branding feature." lightbox="../media/site-page-after-custom-branding.png":::

### Example 2

1. Allow the custom branding by running the following command-syntax:

   ```$webapp = Get-SPWebApplication http://spwfe 
      $webapp.SuiteNavAllowCustom = $true 
      $webapp.Update()
   ```

2. Set all the options by running the following command-syntax:\

   ```$webapp.SuiteNavBrandingText = "Contoso Bass Adventures" 
      $webapp.SuiteNavBrandingLogoUrl = "http://spwfe/Photos/bass-illustration.svg" 
      $webapp.SuiteNavBrandingLogoTitle = "Contoso Logo" 
      $webapp.SuiteNavBrandingLogoNavigationUrl = "https://www.contoso.com/" 
      $webapp.SuiteBarBackground = '#999966'            
      $webapp.SuiteNavAccentColor = '#006600' 
      $webapp.SuiteBarText = '#000000' 
      $webapp.update()
   ```

   :::image type="content" source="../media/applying-custom-branding.png" alt-text="Screenshot that shows the site page after the custom branding feature has been applied." lightbox="../media/applying-custom-branding.png":::




