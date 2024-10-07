---
title: Allow or prevent custom script
ms.reviewer: lucaband
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
ms.date: 07/10/2024
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'O365M_NoScript'
- 'O365E_NoScript'
- 'seo-marvel-apr2020'
- admindeeplinkSPO
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- ODB160
- ODB150
- BSA160
- MET150
ms.assetid: 1f2c515f-5d7e-448a-9fd7-835da935584f
description: Learn how global and SharePoint admins can change the custom script setting for SharePoint sites in the organization.
---

# Allow or prevent custom script

As a [SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365, you can allow custom script as a way of letting users change the look, feel, and behavior of sites and pages to meet organizational objectives or individual needs. If you allow custom script, all users who have _Add and Customize Pages_ permission to a site or page can add any script they want. (By default, users who create sites are site owners and therefore have this permission.) 
  
> [!NOTE]
> For simple ways to change the look and feel of a site, see [Change the look of your SharePoint site](https://support.office.com/article/06bbadc3-6b04-4a60-9d14-894f6a170818). 
  
By default, script is not allowed on most sites that admins create using the SharePoint admin center as well as all sites created using the New-SPOSite PowerShell command. Same applies to OneDrive, sites users create themselves, modern team and communication sites, and the root site for your organization. For more info about the security implications of custom script, see [Security considerations of allowing custom script](security-considerations-of-allowing-custom-script.md).
  
> [!IMPORTANT]
> If SharePoint was set up for your organization before 2015, your custom script settings might still be set to _Not Configured_ even though in the SharePoint admin center they appear to be set to prevent users from running custom script. In this case, users won't be able to copy items between SharePoint sites and between OneDrive and SharePoint. On the <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">Settings page in the SharePoint admin center</a>, to accept the custom script settings as they appear, select **OK**, and enable cross-site copying. For more info about copying items between OneDrive and SharePoint, see [Copy files and folders between OneDrive and SharePoint sites](https://support.office.com/article/67a6323e-7fd4-4254-99a8-35613492a82f). 
  
## To allow custom script on OneDrive or user-created sites

> [!NOTE]
> This feature will be removed during H1 calendar year 2024. Once removed, it will no longer be possible to allow custom script on OneDrive sites.

In the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>, you can choose to allow users to run custom script on OneDrive (referred to as _personal sites_) or on all classic team sites they create. For info about letting users create their own sites, see [Manage site creation in SharePoint](manage-site-creation.md).
  
> [!CAUTION]
> Before you allow custom script on sites in your organization, make sure you understand the [security implications](security-considerations-of-allowing-custom-script.md). 
  
1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](./sharepoint-admin-role.md) for your organization.

    > [!NOTE]
    > If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the **Settings** page.

2. At the bottom of the page, select **classic settings page**.

3. Under **Custom Script**, select:

    - **Allow users to run custom script on personal sites**.

    - **Allow users to run custom script on self-service created sites**.

    :::image type="content" alt-text="Screenshot of custom script section of settings page in SharePoint admin center." source="media/a96d5c23-6389-4343-81cb-7f055617f6e8.png" lightbox="media/a96d5c23-6389-4343-81cb-7f055617f6e8.png":::
  
    > [!NOTE]
    > Because self-service site creation points to your organization's root site by default, changing the Custom Script setting allows custom script on your organization's root site. For info about changing where sites are created, see [Manage site creation in SharePoint](manage-site-creation.md). 
  
4. Select **OK**. It can take up to 24 hours for the change to take effect.

## To allow custom script on other SharePoint sites

> [!CAUTION]
> Before you allow custom script on sites in your organization, make sure you understand the [security implications](security-considerations-of-allowing-custom-script.md). 
  
To allow custom script on a particular site (previously called _site collection_) immediately, follow these steps:

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall **SharePoint Online Management Shell**.

2. Connect to SharePoint as a [SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command.

    ```PowerShell
    Set-SPOSite <SiteURL> -DenyAddAndCustomizePages 0
    ```
    or by means of the PnP.PowerShell cmdlet [Set-PnPSite](https://pnp.github.io/powershell/cmdlets/Set-PnPSite.html)
    
    ```PowerShell
    Set-PnPSite -Identity <SiteURL> -NoScriptSite $false
    ``` 

If you change this setting for a classic team site, it will be overridden by the Custom Script setting in the admin center within 24 hours.

> [!NOTE]
> You cannot allow or prevent custom scripts to an individual user's OneDrive.
  
## Manage custom script from SharePoint admin center

> [!NOTE]
> If you do not see the new options in SharePoint tenant admin center, the feature is not enabled in your tenant yet. Every customer will have this new set of capabilities enabled by end of June 2024

Tenants administrators have a set of tools available in SharePoint tenant administration to manage custom script within their organization. Specifically, tenant administrators can do the following:

- verify custom script status 
- change custom script settings 
- persist custom script settings

### Verify custom script status

A new **Custom script** column is now available in the **Active sites** page under **Sites**.

:::image type="content" alt-text="Screenshot of active sites view with custom script column visible." source="media/232a2283-7f38-4f77-b32d-e076bbcbbb01.png" lightbox="media/232a2283-7f38-4f77-b32d-e076bbcbbb01.png":::

The column can be added to any view. A new **Custom script allowed sites** is also available to provide an easy access to all the sites where custom script is enabled:

:::image type="content" alt-text="Screenshot of the list of default views, which includes the 'custom script allowed sites' view." source="media/e19f29a8-601a-416a-b8fd-2f128461b52c.png":::

### Change custom script settings

In the **Active sites** page, upon selecting a site, under **settings**, a **Custom scripts** setting is available for administrators:

:::image type="content" alt-text="Screenshot of the 'Custom scripts' setting." source="media/7a9c6b79-db8b-4577-9a8c-978f011196a9.png":::

Administrators can control custom script settings for a specific site; deciding if they want to allow or block custom script on a specific site:

:::image type="content" alt-text="Screenshot of 'Custom scripts' values." source="media/05b24a6e-7dec-4b50-80e8-f09fe18e7dd4.png" lightbox="media/05b24a6e-7dec-4b50-80e8-f09fe18e7dd4.png":::

By default, any changes to custom script settings for a specific site only last for a maximum of 24 hours. After that time, the setting will reset to its original value for that specific site.

### Persist custom script settings

To prevent SharePoint in resetting custom script settings to its original value to the whole tenant follow these steps:

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell."

2. Connect to SharePoint as a [SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command.

    ```PowerShell
    Set-SPOTenant -DelayDenyAddAndCustomizePagesEnforcement $True
    ```

> [!NOTE]
> This setting affects all sites. There are no options to preserve changes to custom script settings only on some specific sites. This parameter will be available until November 2024. After that date, it will no longer be possible to prevent SharePoint in resetting custom script settings to its original value for all sites.
> Running the command where [Multi-Geo capabilities on OneDrive and SharePoint](/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365) are configured, will only affect the current geo from which you ran the command. To persist custom script settings across the entire tenant you must run the command on each geo.

## Features affected when custom script is blocked

When users are prevented from running custom script on OneDrive or the classic team sites they create, site admins and owners won't be able to create new items such as templates, solutions, themes, and help file collections. If you allowed custom script in the past, items that were already created will still work.
  
The following site settings are unavailable when users are prevented from running custom script:
  
| Site feature | Behavior | Notes |
|:-----|:-----|:-----|
|Save Site as Template |No longer available in Site Settings |Users can still build sites from templates created before custom script was blocked. |
|Save document library as template |No longer available in Library Settings  |Users can still build document libraries from templates created before custom script was blocked.  |
|Save list as template  |	No longer available in List Settings  |Users can still build lists from templates created before custom script was blocked.  |
|Solution Gallery  |No longer available in Site Settings  |Users can still use solutions created before custom script was blocked.  |
|Theme Gallery  |No longer available in Site Settings  |Users can still use themes created before custom script was blocked.  |
|Help Settings  |No longer available in Site Settings  |Users can still access help file collections available before custom script was blocked.  |
|Sandbox solutions  |Solution Gallery is no longer available in Site Settings  |Users can't add, manage, or upgrade sandbox solutions. They can still run sandbox solutions that were deployed before custom script was blocked.  |
|SharePoint Designer  |Pages that are not HTML can no longer be updated.  <br/> Handling List: **Create Form** and **Custom Action** will no longer work.  <br/> Subsites: **New Subsite** and **Delete Site** redirect to the **Site Settings** page in the browser.  <br/> Data Sources: **Properties** button is no longer available.  |Users can still open some data sources. To open a site that does not allow custom script in SharePoint Designer, you must first open a site that does allow custom script.  |
|Uploading files that potentially include script  |The following file types cannot open from a library  <br/> .asmx  <br/> .ascx  <br/> .aspx  <br/> .htc  <br/> .jar  <br/> .master  <br/> .swf  <br/> .xap  <br/> .xsf  |Existing files in the library are not impacted.  |
|Uploading Documents to Content Types  |Access denied message when attempting to attach a document template to a Content Type. |We recommend using Document Library document templates. |
|Publishing of SharePoint 2010 Workflows |Access denied message when attempting to publish a SharePoint 2010 Workflow. | |
   
The following web parts and features are unavailable to site admins and owners when you prevent them from running custom script.
  
| Web part category | Web part |
|:-----|:-----|
|Business Data  |Business Data Actions  <br/> Business Data Item  <br/> Business Data Item Builder  <br/> Business Data List  <br/> Business Data Related List  <br/> Excel Web Access  <br/> Indicator Details  <br/> Status List  <br/> Visio Web Access  |
|Community  |About This Community  <br/> Join  <br/> My Membership  <br/> Tools  <br/> What's Happening  |
|Content Rollup  |Categories  <br/> Project Summary  <br/> Relevant Documents  <br/> RSS Viewer  <br/> Site Aggregator  <br/> Sites in Category  <br/> Term Property  <br/> Timeline  <br/> WSRP Viewer  <br/> XML Viewer  |
|Document Sets  |Document Set Contents  <br/> Document Set Properties  |
|Advanced |Embed |
|Forms  |HTML Form Web Part  |
|Media and Content  |Content Editor  <br/> Script Editor  <br/> Silverlight Web Part  <br/> Page Viewer (can't set web page URL) |
|Search  |Refinement  <br/> Search Box  <br/> Search Navigation  <br/> Search Results  |
|Search-Driven Content  |Catalog-Item Reuse  |
|Social Collaboration  |Contact Details  <br/> Note Board  <br/> Organization Browser  <br/> Site Feed  <br/> Tag Cloud  <br/> User Tasks  |
|Master Page Gallery  |Can't create or edit master pages  |
|Publishing Sites  |Can't create or edit master pages and page layouts  |

Furthermore, SharePoint Framework web parts that have the _requiresCustomScript_ value set to **true**, will behave as following:   

- the web part is not available in the web part picker
- every instance of the web part that was added to the page while custom scripts that were allowed to run, will no longer surface in those pages. Author will still be able to remove them while editing the page 

## Best practice for communicating script setting changes to users

Before you prevent custom script on sites where you previously allowed it, we recommend communicating the change well in advance so users can understand the impact of it. Otherwise, users who are accustomed to changing themes or adding web parts on their sites will suddenly not be able to and will see the following error message.
  
:::image type="content" alt-text="Screenshot of the Error message that's displayed when scripting is disabled on a site." source="media/1c7666a0-9538-484f-a691-6e424c5db71a.png":::
  
Communicating the change in advance can reduce user frustration and support calls.
