---
title: "New and improved features in SharePoint Server 2019 Public Preview"
ms.author: stevhord
author: bentoncity
manager: pamgreen
ms.date: 6/26/2018
ms.audience: ITPro
ms.topic: overview
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- Strat_SP_server
ms.custom: 
description: "Learn about the new features and updates to existing features in SharePoint Server 2019 Public Preview."
---

# New and improved features in SharePoint Server 2019 Public Preview

Learn about the new features and updates to existing features in SharePoint Server 2019 Public Preview.

To read more about the updated modern experience in SharePoint Server 2019 Public Preview, see [Differences between SharePoint Server 2016 and 2019 Public Preview](https://support.office.com/en-us/article/differences-between-sharepoint-server-2016-and-2019-ba84c8a3-3ce2-4252-926e-c67654ceb4a3). 

## Detailed description of new features

This section provides detailed descriptions of the new updated features in SharePoint Server 2019 Public Preview.

### Access Services 2013 now supports Send Email

The Access Services 2013 service application now supports the SendEmail action for sending email messages from apps. See [Introducing Send Email in Access 2013 web apps](https://blogs.office.com/2015/01/12/introducing-send-email-access-2013-web-apps/) for more details.

### Additional documentation links for Central Administration site

We've made it easier for farm administrators to reach the latest SharePoint administration documentation and find the latest Public Updates by adding links in the SharePoint Central Administration homepage.

- [SharePoint Server Documentation](https://go.microsoft.com/fwlink/?linkid=866977)
- [SharePoint Server Updates](https://go.microsoft.com/fwlink/?linkid=866978)

### Communication sites

Communication sites are a place to share news, showcase a story, or broadcast a message to other people. The new Hero web part can display up to five items with compelling images, text, and links to draw attention to your most important content. Users can easily create communication sites for themselves from SharePoint Home without needing to contact IT.

### Fast site creation

Fast site creation in SharePoint Server 2019 Public Preview allows users create new sites in a few seconds. Fast site creation is only supported with the following site templates:

- OneDrive personal site [SPSPERS#10]

- Team site (modern only) [STS#3]

- Communication site [SITEPAGEPUBLISHING#0]

Fast site creation is used when creating sites in the following entry points:

- OneDrive personal site auto-provisioning

- The Create Site button in SharePoint Home

- The New-SPSite PowerShell cmdlet with the -CreateFromSiteMaster switch parameter#

### Increased storage file size in SharePoint document libraries

We now support storing files up to 15 GB in SharePoint document libraries. This is up from 10 GB in SharePoint Server 2016.

### Modern lists and libraries

SharePoint Server 2019 Public Preview contains the modern experiences for lists and libraries in Team sites. This brings the experience up to date with that found in SharePoint Online.

### Modern sharing experiences

SharePoint Server 2019 Public Preview now supports modern sharing experiences with a simplified sharing UI. You can now easily share links to content with others in your organization. You can also be warned if you're sharing to a large group or sharing a large number of items.

### Modern Site Pages, modern web parts and authoring

SharePoint Server 2019 Public Preview users can now add modern site pages and modern web parts on team sites. Do this in the **Add a Page** in Site Actions or in the pages library by clicking **New** > **Site Page**.

### Modern search experience
SharePoint Server 2019 Public Preview now also offers a modern search experience. In the modern search experience, users see results before they start typing, and the results update as they type. The search results page shows a compelling overview of search results, grouped by type. It’s easy to expand to see all the results of each type, for example people or sites. On a people result, users can click the email address to quickly get started on an email to that person. The modern search experience is available from the SharePoint home page, modern sites, and modern document libraries.

Both experiences use the same search index to find results. Search settings that impact what's indexed, impact both experiences. The following settings do not impact modern search:
- Refinable
- Sortable
- Custom entity extraction
- Company name extraction 

Only the classic search experience is customizable, and some of the customization settings also affect modern search:
- Modern search also uses the default result source.
- When you remove search results temporarily by specifying URLs, the results are removed from both the classic and modern search results.
- When you create single promoted results at the Search service application level, users also see the promoted results in the modern search results page when:
    - They've searched across all of SharePoint
    - They've filtered the search results page to **All result types** (default filter)

### Modern Team sites

Modern team sites bring a fresh and responsive user experience to team collaboration. The redesigned homepage improves the discoverability of the most common collaboration tasks while putting your team’s news front and center. Users can easily create modern team sites for themselves from SharePoint Home without needing to contact IT.

SharePoint Server 2019 Public Preview will continue to support creating classic team sites.

### PDF Viewer

SharePoint Server 2019 Public Preview can now render PDF documents on the server. Users no longer need to rely on a PDF viewer client application.

### SharePoint using modern Internet Information Services (IIS) APIs

SharePoint has modernized its integration with IIS by removing all of our dependencies on the legacy IIS6 APIs.  SharePoint now uses the IIS7+ APIs to manage IIS, which are the latest and best supported APIs from the IIS team.  This allows us to more easily adopt new IIS features and stay compatible with future Windows Server releases.

As a result of this change, the following Windows Server features will no longer be installed by the SharePoint prerequisite installer:

- IIS 6 Management Compatibility (Web-Mgmt-Compat)

- IIS 6 Metabase Compatibility (Web-Metabase)

- IIS 6 Scripting Tools (Web-Lgcy-Scripting)

### SharePoint home page

The SharePoint home  page is a modern UI experience that gives users unified access to all of their sites—online and on-premises. It allows users to navigate seamlessly through their intranet, catch up with activity across their sites with just a glance, and provides a personalized view of all team news. 

The SharePoint home page is also the launching point for users to create new, modern sites on a self-service basis. 

You can reach the SharePoint home page by clicking on the "Sites" icon in the SharePoint app launcher. The SharePoint home page replaces the old sites.aspx experience.

### From the SharePoint home page, you can create sites in different web applications

The self-service site creation experience in the SharePoint home page now supports creating new sites in a different web application, regardless of whether the web application is hosted on the local farm or a remote farm. This is controlled by the When users select the Create site command, create setting on the Self-service Site Collection Management page in Central Administration.

To create sites in the same web application, select **This web application**.

To create sites in a different web application on the local farm, select **The following web application** and then select the web application from the drop-down field. Ensure self-service site creation is enabled in the target web application.

To create sites in a different web application on a remote farm, follow these steps:

1. In the local farm hosting the SharePoint home page, use the Map to External Resource feature in Alternate Access Mappings (AAM) to provide the URL of the web application you want to create sites in.

2. In the local farm hosting the SharePoint home page, on the Self-service Site Collection Management page for the web application hosting the SharePoint home page, select **The following web application**, and then select the remote web application from the drop-down field.

3. In the remote farm, use the Map to External Resource feature in Alternate Access Mappings (AAM) to provide the URL of the web application hosting the SharePoint home page.

4. In the remote farm, on the Self-service Site Collection Management page for the web application you want to create the sites in, ensure self-service site creation is enabled.

### Self-service site creation on the SharePoint home page now supports AAM zones

The self-service site creation experience on the SharePoint home page now fully supports non-Default Alternate Access Mapping (AAM) zones. When creating sites in a different web application on a remote farm, make sure that an external resource has been created in AAM on both the local farm and the remote farm. This applies to sites created in the same web application, sites created in a different web application on the local farm, and sites created in a different web application on a remote farm. 

SharePoint will treat the external resource as an external web application. The external resource on the local farm should be fully populated with the URLs and zones of the web application on the remote farm. And conversely, the external resource on the remote farm should be fully populated with the URLs and zones of the web application on the local farm. Be sure that the zones of the local web application and the remote web application are synchronized. For more information, see [Configure self-service site creation in SharePoint Server 2019 Public Preview](https://docs.microsoft.com/en-us/SharePoint/sites/configure-self-service-site-creation-in-sharepoint-server-2019).

### SMTP authentication when sending emails

SharePoint Server 2019 Public Preview now supports authenticating to SMTP servers when sending email messages. Authentication can be configured through the Central Administration website and through PowerShell. SharePoint Server 2019 Public Preview will still support anonymous connections to SMTP servers that don't require authentication. This makes it easier for customers to integrate SharePoint into highly secure environments where authentication is required to send emails. Customers no longer need to configure smart host relays for SharePoint in these environments. For more information, see [Plan outgoing email for a SharePoint Server farm](https://docs.microsoft.com/en-us/SharePoint/administration/outgoing-email-planning) and [Configure outgoing email for a SharePoint Server farm](https://docs.microsoft.com/en-us/SharePoint/administration/outgoing-email-configuration).

### Sync files with OneDrive sync client (NGSC)

Users can use the new OneDrive sync client (NGSC – Next Generation Sync Client) instead of Groove.exe to sync files in your SharePoint Server 2019 Public Preview team sites and personal sites with your devices. The OneDrive sync client supports advanced features such as Files On-Demand, push notification, and IRM protection, while still being easy to use. For more information, see [Deploy the new OneDrive sync client for Windows](https://support.office.com/en-us/article/deploy-the-new-onedrive-sync-client-for-windows-3f3a511c-30c6-404a-98bf-76f95c519668) and [Deploy and configure the new OneDrive sync client for Mac](https://support.office.com/en-us/article/deploy-and-configure-the-new-onedrive-sync-client-for-mac-eadddc4e-edc0-4982-9f50-2aef5038c307).

### Use of # and % characters in file and folder names

SharePoint Server 2019 Public Preview now supports # and % characters in file and folder names, completing our support for all valid Windows file and folder name characters. This makes it easier to sync to content from personal storage devices to SharePoint.

## Detailed description of new Microsoft PowerShell SharePoint Server cmdlets

This section lists the new PowerShell cmdlets for SharePoint Server 2019 Public Preview.

### New User Profile Synchronization PowerShell cmdlets

The "stsadm.exe -o sync" command has been converted into several PowerShell cmdlets:

- Get-SPContentDatabase - You can now use the Get-SPContentDatabase cmdlet with the optional parameter -DaysSinceLastProfileSync to return content databases that haven't been synchronized with User Profile for the past n days.
 
- Clear-SPContentDatabaseSyncData - The new Clear-SPContentDatabaseSyncData cmdlet clears User Profile synchronization information from the content databases in the farm that haven't been synchronized for the past n days.

- Update-SPProfileSync - The new Update-SPProfileSync cmdlet updates the User Profile synchronization settings to specify the main synchronization schedule, the sweep schedule to identify new users, and which web applications should be excluded from synchronization.

The "stsadm.exe -o sync" command will still be supported for backward compatibility.

### New Get-SPContentDatabaseOrphanedData PowerShell cmdlet

The "stsadm.exe -o enumallwebs" command has been converted into a PowerShell cmdlet. You can now use the new Get-SPContentDatabaseOrphanedData cmdlet to find orphaned objects within a content database. The "stsadm.exe -o enumallwebs" command will still be supported for backward compatibility.

### New Set-SPApplicationCredentialKey PowerShell cmdlet

The "stsadm.exe -o setapppassword" command has been converted into a PowerShell cmdlet. You can now use the new Set-SPApplicationCredentialKey cmdlet to set the application credential key on the local server for the SharePoint People Picker and SMTP authentication. The "stsadm.exe -o setapppassword" command will still be supported for backward compatibility.

### New Remove-SPApplicationCredentialKey PowerShell cmdlet

The new Remove-SPApplicationCredentialKey cmdlet allows you to remove the application credential key from the local server.
The impact level of this cmdlet is set to high, as removing the application credential key from the local server may degrade or block the functionality of features if they're configured to use the application credential key.  For example, the SharePoint People Picker or SMTP authentication.

## Detailed description of new SharePoint Health Analyzer rules

This section lists the new Health Analyzer rules for SharePoint Server 2019 Public Preview.

### People Picker health rule

SharePoint has added a new health analyzer rule for the People Picker. This health analyzer rule detects if servers in the farm are missing the encryption key needed to retrieve People Picker credentials, such as when the People Picker is configured to search for users in another forest or domain with a one-way trust to the SharePoint farm's domain. If so, it will notify the SharePoint farm administrator so that they can correct the problem. For more information, see [One or more servers can't retrieve People Picker credentials](https://docs.microsoft.com/en-us/SharePoint/technical-reference/one-or-more-servers-can-t-retrieve-people-picker-credentials).

### SMTP authentication health rule

SharePoint has added a new health analyzer rule for SMTP authentication. This health analyzer rule detects if servers in the farm are missing the encryption key needed to retrieve the credentials for authentication. If so, it will notify the SharePoint farm administrator so that they can correct the problem. For more information, see [One or more servers can't retrieve the outgoing email credentials](https://docs.microsoft.com/en-us/SharePoint/technical-reference/one-or-more-servers-can-t-retrieve-the-outgoing-email-credentials).

## Detailed description of improved features

This section provides detailed descriptions of the updated features in SharePoint Server 2019 Public Preview.

### Distributed Cache now uses background garbage collection by default

Distributed Cache will now configure AppFabric Velocity Cache to use background garbage collection. This helps provide a more reliable experience for features that depend on Distributed Cache.

### File path limit of 400 characters

SharePoint Server 2019 Public Preview has increased the maximum file path length limit from 260 characters to 400 characters. The file path is everything after the server name and port number in the URL. File path includes the name of the site and subsites, document library, folders, and the file itself.
This file path length limit increase makes it easier to sync deeply nested content from personal storage devices to SharePoint.

### Hybrid experiences improvements

- The "OneDrive by Default" experience for SharePoint Server 2013 is now available in SharePoint Server 2019 Public Preview. When enabled, any attempt to browse to the My Site Host welcome page will be redirected to Office 365.

- A SharePoint hybrid status bar was added to the top of Central Administration. The hybrid status bar will appear once the SharePoint Server 2019 Public Preview farm meets the minimum system requirements needed to enable hybrid, and will give you direct access to launch the SharePoint Hybrid Configuration Wizard.

- We've added and updated hybrid links throughout Central Administration to launch the SharePoint Hybrid Configuration Wizard. This lets you skip clicking through multiple pages in the SharePoint Online Admin Center just to get to the SharePoint Hybrid Configuration Wizard.

### Recycle Bin restore improvements

SharePoint Server 2019 Public Preview users can now restore items that they've deleted themselves, and also items that other users in the site have deleted. Users need edit permission on the deleted items so they're visible in their SharePoint recycle bin.

### Sharing email template

Sharing email notifications have been refreshed to use a modern template design. Customers can set the **SPWebApplication.SharingEmailUseSharePoint2016Templates** property to true if they want to continue using the previous sharing email template.

### Suite Navigation and App Launcher improvements

We've refreshed Suite Navigation and App Launcher in SharePoint Server 2019 Public Preview. The user interface now is closely aligned with what is seen in Office 365 so that SharePoint hybrid customers will have a seamless experience as they move between SharePoint Server 2019 Public Preview and SharePoint Online.

### Telemetry privacy experience

SharePoint Server 2019 Public Preview now has an updated telemetry management experience. When you first set up a farm or browse to the SharePoint privacy settings page in Central Administration, you can now provide an email address for the telemetry contact of your organization. This is in anticipation of future telemetry reporting capabilities that will allow customers to associate SharePoint Server and OneDrive Sync Client telemetry with their hybrid tenancy.

The email address provided is not sent outside of the SharePoint farm, not even to Microsoft. It is used in combination with other farm data to generate a unique hash value to represent your farm when uploading telemetry data to Microsoft. When customers want to associate telemetry with their hybrid tenancy, this email address will be part of the process to prove ownership of the telemetry data.

Customers can opt in and opt out of the telemetry experience at any time.

### Visio Services accessibility

 Visio Services is introducing several accessibility improvements for high contrast displays, keyboard navigation, and Narrator. Users will be able to access different panes with the following shortcuts:

1. Move focus to Comment pane = Alt + R
 
2. Move focus to Shape data pane = Alt + S
 
3. Move focus to Canvas = Alt + C

## Related Topics

[What is SharePoint?](https://support.office.com/en-us/article/What-is-SharePoint-97b915e6-651b-43b2-827d-fb25777f446f?ui=en-US&amp;rs=en-US&amp;ad=US)  
[New development capabilities for SharePoint 2019](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-2019-development-platform)
