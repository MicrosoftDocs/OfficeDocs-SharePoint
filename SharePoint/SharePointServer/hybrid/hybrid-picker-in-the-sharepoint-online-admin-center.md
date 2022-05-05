---
title: "Hybrid picker in the SharePoint admin center"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 12/5/2017
audience: ITPro
f1.keywords:
- CSH
ms.topic: conceptual
ms.prod: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: dcac4cbf-7840-470a-9712-3b968c4f06d0
description: Learn how to use the Hybrid Picker wizard in the SharePoint admin center.

---

# Hybrid picker in the SharePoint admin center

[!INCLUDE[appliesto-2013-2016-2019-SUB-SPO-md](../includes/appliesto-2013-2016-2019-SUB-SPO-md.md)]

## What is the Hybrid Picker?

Hybrid Picker is a wizard that can be downloaded to your SharePoint Server from Microsoft 365. The wizard helps automate certain configuration steps needed to connect your on-premises SharePoint Server environment with SharePoint in Microsoft 365. The Hybrid Picker wizard is your assistant, designed to do some of the work for you.

Use the Hybrid Picker wizard to redirect OneDrive to Microsoft 365, leverage hybrid site features or app launcher, and add some extra integration between on-premises SharePoint Server and an extranet site made in Microsoft 365. Hybrid Picker also creates a Server-to-Server (S2S)/OAuth connection for your [SharePoint Hybrid features](sharepoint-hybrid-sites-and-search.md).

## Using the Hybrid Picker

First, you need to make sure you meet the prerequisites in your SharePoint Server on-premises farm, then you can run the Hybrid Picker wizard.

 **Prerequisites to run the Picker**

The Picker requires the [.NET Framework 4.6.2](https://www.microsoft.com/download/details.aspx?id=53321) in order to run. 

The following are the account requirements to run the Hybrid Picker. You must be:

- A member of the Farm Administrators group.

- A service application administrator (Full Control) for the User Profile Service.

- a Microsoft 365 Global Admin, either with or without multi-factor authentication (MFA) enabled for the account.

- Logged into Microsoft 365 and SharePoint Server from a server in your SharePoint Server farm.

- Able to launch the Hybrid Picker as a Farm Admin with elevated permissions.

> [!IMPORTANT]
> The Hybrid Picker wizard must be launched from an on-premises server with SharePoint Server 2013, SharePoint Server 2016, or SharePoint Server 2019 installed. Launch it in the environment you want to use for your SharePoint hybrid. 

## SharePoint hybrid features offered in the Hybrid Picker

Use the Hybrid Picker to either configure, or assist with the configuration of, hybrids that connect Microsoft 365 and your on-premises SharePoint environment. 

The Hybrid picker helps with or completes the setup of these hybrid features:

- **[Hybrid OneDrive](plan-hybrid-onedrive-for-business.md)** - Choosing this option will redirect on-premises My Sites/OneDrive sites to SharePoint in Microsoft 365 and OneDrive. After the wizard completes, any click of the OneDrive link from on-premises redirects to OneDrive in the cloud. Your redirection is complete and users can begin to migrate any files to their online OneDrive. This option also sets up hybrid user profiles. When users click to view a profile, they will be redirected to the profile in Microsoft 365. 

- **[Hybrid Sites Features](sharepoint-hybrid-sites-and-search.md)** - Choosing this option sets up hybrid sites features, a suite of site integration features, as well as OneDrive redirection. Selecting this option configures hybrid OneDrive and hybrid user profiles, hybrid site following, and the hybrid app launcher. 

- **[Hybrid App Launcher](the-extensible-hybrid-app-launcher.md)** - This hybrid feature further integrates Microsoft 365 with your on-premises SharePoint Server farm by placing tiles like Office 365 Delve and Video (as well as custom Microsoft 365 tiles you may have) on the on-premises SharePoint Server App Launcher. This option also sets up hybrid OneDrive with user profile redirection, and sites features. 

- **[Business-to-business (B2B) extranet sites](../../SharePointOnline/create-b2b-extranet.md)** - Choosing this option will install extra features you can integrate with an extranet site you create in Microsoft 365. With Microsoft 365 extranet, partners can connect directly to a members-only site in Microsoft 365 without access to the corporate on-premises environment or any other Microsoft 365 site. Choosing this option sets up OneDrive and user profile redirection, sites features, and hybrid app launcher. 

- **[Hybrid Taxonomy](plan-hybrid-sharepoint-taxonomy-and-hybrid-content-types.md)** - This feature allows a centralized taxonomy that's readable and writable in the Microsoft 365 Cloud, to be used as a read-only copy on-premises. This feature includes Hybrid Content type (June 2017 PU required) which will replicate the published content types in Microsoft 365 to on-premises. Choosing this option sets up OneDrive and user profile redirection, sites features, and hybrid app launcher. 

- **[Hybrid self-service site creation](hybrid-self-service-site-creation.md)** - This feature redirects the default self-service site creation page in SharePoint Server 2013, SharePoint Server 2016, or SharePoint Server 2019 (/_layouts/15/scsignup.aspx) to the SharePoint in Microsoft 365 Group Creation page. This setting can be configured independently for each web application in your farm. It helps your users create their sites in SharePoint in Microsoft 365 instead of SharePoint Server. 

- **[Cloud hybrid search](./learn-about-cloud-hybrid-search-for-sharepoint.md)** - Choosing this option creates a cloud Search service application in SharePoint Server and connects the cloud Search service application to your Microsoft 365 organization. This is one of the steps needed to set up cloud hybrid search, you must do the rest of the steps yourself (see the [roadmap](configure-cloud-hybrid-searchroadmap.md)). This option doesn't include set-up of other hybrid features.

> [!TIP]
> If the Hybrid Picker is run a second time with an enabled feature unchecked, this will not cause the feature to be uninstalled. Any additional selections will be installed and previously installed features will remain. 

For all options, the hybrid picker configures a server-to-server trust between your SharePoint Server farm and Microsoft 365.

Note that the hybrid picker does not uninstall features. If you run the hybrid picker and deselect a feature that you previously installed, it will remain installed.

To get started configuring hybrid features for your environment, choose from the following:

- [Configure hybrid OneDrive - roadmap](configure-hybrid-onedrive-for-businessroadmap.md)

- [Configure hybrid sites features - roadmap](configure-hybrid-sites-featuresroadmap.md)

- [Configure cloud hybrid search - roadmap](configure-cloud-hybrid-searchroadmap.md)

- [Configure hybrid SharePoint taxonomy and hybrid content types](configure-hybrid-sharepoint-taxonomy-and-hybrid-content-types.md)

## Hybrid Picker Prerequisite Checking

While running the Hybrid Picker, the wizard will check basic SharePoint farm settings that would otherwise block setup of essential hybrid building-blocks (such as OAuth/S2S Trust). This is why you should launch the Hybrid Picker from a server that will be part of your SharePoint hybrid. Some of the settings that are detected and checked while the configuration is run, include whether the:

- SharePoint Server farm exists

- Account is a farm administrator

- SharePoint farm is a version that can function in a hybrid configuration

- AppMangementServiceInstance is online

- AppMangementServiceApplication is online

- AppMangementServiceApplicationProxy is online

- UserProfileApplicationProxy is online

- The SPO365LinkSettings cmdlet (used to set the MySiteHostURL) is accessible on the server 

The results of this testing can be viewed as a report if any prerequisite isn't met. If all prerequisites are met you will see green check-marks beside all the prerequisites, and will be able to continue your hybrid configuration.

## Authentication realm update

As part of hybrid configuration, the hybrid picker updates the on-premises farm's authentication realm to match the Microsoft 365 organization context ID. After the authentication realm is changed, existing SharePoint in Microsoft 365 add-ins fail to authenticate. The hybrid picker will attempt to fix this issue automatically. If the hybrid picker is not able to fix this issue or if you choose to fix it manually, follow the steps in [Fix the HTTP 401 error with provider-hosted add-ins and issues with workflow and cross farm trust scenarios in SharePoint in Microsoft 365](https://support.microsoft.com/help/4010011).

## See also

#### Other Resources

[You receive the error "Value cannot be null. Parameter name: My site URL or team site URL from Discovery Service is null or empty" when you use the SharePoint Hybrid Picker](https://support.microsoft.com/kb/3204761)