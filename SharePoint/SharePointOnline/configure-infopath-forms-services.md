---
title: "Configure InfoPath Forms Services"
ms.reviewer: 
ms.author: kaarins
author: kaarins
manager: pamgreen
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'SPOTACfgInfoPathWebSrvcPrx'
- 'SPOTACfgInfoPathSrvc'
ms.service: sharepoint-online
localization_priority: Normal
search.appverid:
- SPO160
- BSA160
- MET150
ms.assetid: a8609546-c0d7-4956-81b6-08e93eb4b290
description: "How to configure Infopath in SharePoint."
---

# Configure InfoPath Forms Services

InfoPath Forms Services in SharePoint lets you deploy your organization's forms to your sites, enabling users fill out these forms in a web browser. You can configure InfoPath Forms Services in any of several ways, depending on the needs of your organization.
  
> [!NOTE]
> InfoPath Forms Services 2013 is the last release of InfoPath Forms Services. Microsoft Power Apps is the recommended solution for creating and delivering custom forms for SharePoint lists. Create new forms with Power Apps from the command bar or the **Customize** button on SharePoint list forms. Support for InfoPath Forms Services will match the support lifecycle for SharePoint Server 2016.
  
## Overview
<a name="__toc336423362"> </a>

This article discusses settings that apply only to user form templates, which are form templates that are not deployed by a developer. User form templates don't require Full Trust, and they don't contain code or other business logic.
  
Form designers can publish user form templates to a list or a form library in a SharePoint site collection. Because user form templates can be deployed by many users, a server can potentially host thousands of user form templates. In large numbers, even form templates that contain no business logic can put a heavy load on the server.
  
## Configure browser-enabled user form templates
<a name="__toc336423363"> </a>

When form templates are published to a server that is running InfoPath Forms Services, the designer of the form template can choose to make the form template browser-enabled. This allows a user to fill out the form in a web browser.
  
As an administrator, you can configure the following template settings for browser-enabled user form templates:
  
- **Enable or disable publishing of browser-enabled form templates.** If you disable publishing, form designers can publish only form templates that are not browser-enabled. In this case, all browser-compatible features are disabled in the form template. 
    
- **Enable or disable rendering of browser-enabled form templates.** If you disable rendering, users cannot use a web browser to fill out the form and must use Microsoft InfoPath Filler 2013 to open the form. 
    
By default, browser-enabled user form templates can be published and rendered.
  
To configure browser-enabled user form templates
  
1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

2. Under **InfoPath**, select **Open**.
 
3. In the **User Browser-enabled Form Templates** section, specify how you want user form templates to be processed by InfoPath Forms Services by completing the following steps: 
    
    > [!NOTE]
    > These settings apply only to form templates published to form libraries. Workflow form templates and list forms are not affected. 
  
    1. Select the **Allow users to browser-enable form templates** check box to allow users to publish browser-enabled form templates. 
    
    > [!NOTE]
    > Clearing this check box disables browser-enabled form templates across the entire site collection. 
  
    2. Select the **Render form templates that are browser-enabled by users** check box to allow browser-enabled form templates that users publish to be rendered in a web browser. 
    
    > [!NOTE]
    > If this option is not selected, users can still publish browser-compatible form templates to form libraries, but these form templates cannot be filled out in a web browser. 
  
4. Select **OK**.
    
## Configure exempt user agents
<a name="__toc336423364"> </a>

To make indexing InfoPath forms faster and easier, you can specify which user agents to exempt from receiving an entire webpage to index. This means that when a user agent you've specified as exempt encounters an InfoPath form, the form will be returned as an XML file (which looks like a hierarchical text file) instead of an entire webpage. You can use the procedure below to select this option and populate the agent list.
  
1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true) and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

>[!NOTE]
>If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the More features page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the More features page.

3. Under **InfoPath**, select **Open**.
    
4. In the **Exempt User Agents** section, select the **Customize the list of exempt user agents** check box, and then do one of the following: 
    
5. To add a user agent to the exempt list, in the **Name** box, enter a name, and then select **Add**.
    
6. To remove a user agent from the list, select the name, and then select **Remove**.
    
7. Select **OK**.
    

