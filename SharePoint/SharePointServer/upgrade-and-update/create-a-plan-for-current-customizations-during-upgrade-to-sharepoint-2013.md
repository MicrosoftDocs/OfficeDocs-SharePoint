---
title: "Create a plan for current customizations during upgrade to SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/26/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c18cc4e9-6942-47a6-a110-6b9ab0b9a236
description: "Identify all customizations in your environment and determine what to change or remove as you upgrade to SharePoint 2013."
---

# Create a plan for current customizations during upgrade to SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
If you have extensively customized your sites based on SharePoint 2010 Products, you must determine how you want to handle your customizations when you upgrade to SharePoint 2013. Your approach will vary based on the extent of the customizations, the kind of customization, the complexity of your site, and your goals for upgrading. Before you upgrade, you must identify and then evaluate the customizations in your environment and determine whether you will upgrade them, and how.
  
## Identify customizations in your environment
<a name="Identify"> </a>

As part of an upgrade testing process, you should create an inventory of the server-side customizations in your environment (solutions, features, Web Parts, event handlers, master pages, page layouts, CSS files, and so on). For more information about how to identify customizations, see [Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14)). 
  
## Evaluate the customizations
<a name="Evaluate"> </a>

After you have identified the customizations, think about the potential upgrade effect of each one. The following table describes types of customizations and the kind of effect they can have during upgrade.
  
|**Category of customization**|**Types of customizations**|**Potential effect on upgrade**|
|:-----|:-----|:-----|
|Visually-affecting  <br/> |Master pages  <br/> Themes  <br/> Web Pages  <br/> Web Parts  <br/> Custom JavaScript  <br/> Custom CSS files  <br/> |Should not affect database upgrade.  <br/> For site upgrades: likely to work well in 2010 mode, but need changes to work in 2013 mode.  <br/> Test carefully in both modes.  <br/> |
|Data structure affecting  <br/> |Content types  <br/> List types  <br/> Web templates  <br/> Site definitions  <br/> |Can affect database upgrade if content or list type names conflict with new content or list types in the product, or if templates or definitions are missing.  <br/> |
|Non-visually affecting  <br/> |Web services  <br/> Windows services  <br/> HTTP handler  <br/> HTTP module  <br/> |Might not be compatible with SharePoint 2013. Test carefully to determine effect. Be prepared to remove or replace.  <br/> |
   
Now that you know what customizations that you have, and what type that they are, you can decide what to do about them. The following questions can help you evaluate the customizations:
  
- Is the customization still valuable? 
    
  - Does it serve a useful business need?
    
  - Is it widely deployed and used?
    
  - Does it do something that you cannot do with standard features in the product?
    
- Is the customization well-designed?
    
  - Is it built on supported, predefined site definitions?
    
  - Does it follow best practices for customizations? 
    
  - Is it a supported kind of customization, or does it introduce risk into your environment?
    
As you evaluate every customization, you can also think about your overall approach for customizations. You can choose from among these options:
  
- **Keep the customizations, don't upgrade the sites** You can continue to run the site in 2010 mode in the upgraded environment. Although you can use this approach to keep the same functionality, you will be unable to take advantage of the features and capabilities that are available in the new version. Use this approach only temporarily - eventually you must address the issue (such as before an upgrade to the next version of the product). 
    
- **Replace or redo the customizations** If you want to use new functionality, plan to redesign your sites, or are significantly changing the information architecture, the upgrade is your opportunity to start over with new features, a new look, or a new organization. When you replace or redo customizations, you can take advantage of the new capabilities, change your design slightly if you want, or move to a more manageable design. 
    
- **Discard the customizations** Replace the customizations by using default functionality. You can reset pages to the default site definitions and remove any Web Parts or features that you no longer want to support. In fact, the site collection health-checker checks for unghosted pages and can reset the pages to the default versions. If you decide to discard any customizations, you must fix any issues that result from removing the customizations in the sites that used them. You can use your customizations inventory to determine which sites require this kind of attention before or after upgrade. 
    
## Considerations for specific customizations
<a name="Considerations"> </a>

In addition to your overall decision about how to treat customizations in your environment during upgrade, you must examine specific types of customizations to determine whether you must perform any additional actions to make them work in the upgraded environment.
  
The following table lists some common customizations and a recommendation for addressing that kind of customization.
  
|**Customization type**|**Recommendation**|
|:-----|:-----|
|Site definition  <br/> |Migrate sites to a supported, predefined site definition, then apply custom features by using solution deployment.  <br/> You can also continue to use a custom site definition. You do not have to create a new site definition that is based on SharePoint 2013.  <br/> However, if you must perform custom upgrade actions for the definition, you might have to create an upgrade definition file for that site definition. For more information, see [Upgrade Definition Files](https://go.microsoft.com/fwlink/p/?LinkId=182339) on MSDN.  <br/> |
|Custom site templates  <br/> |If you have custom site templates (a site template that has been customized and saved as a WSP template) that you want to continue to use after you upgrade to SharePoint 2013, you must plan to recreate them in 2013 mode before you upgrade your site collection. You have to create them again because custom site templates apply to specific versions and don't always look or work the same way in subsequent versions. Furthermore, if you used a template to make various 2010 sites, they could all require manual adjustments to ensure that they work and render properly in SharePoint 2013.  <br/> |
|"Fabulous 40" application templates  <br/> |Microsoft is not creating new versions of these templates. Environments that contain sites based on these templates can be upgraded as long as the templates are installed. But there might be issues when you try to upgrade the site collections. Make sure that you test each site before you upgrade the production environment. For more information, see [Troubleshoot database upgrade issues in SharePoint 2013](/previous-versions/office/sharepoint-server-2010/cc262967(v=office.14)).  <br/> |
|Feature  <br/> |Evaluate, then redesign or redeploy if it is necessary.  <br/> |
|Workflows and server controls  <br/> |Depends on the solution. Contact the vendor to discover whether there is an updated solution. If a workflow is compatible with the new version, redeploy.  <br/> |
|Event handler  <br/> |Most event handlers will continue to work without changes. However, if the code for the event handler makes calls to APIs which were deprecated, you will have to rewrite it, and then redeploy it as a feature.  <br/> |
|Managed paths (inclusions/exclusions)  <br/> |Re-create inclusions to make sure that you can access all site collections under those paths.  <br/> Exclusions were not used in SharePoint 2010 Products. If you had any remaining from an earlier version, they do not have to be re-created.  <br/> |
|Themes  <br/> |Re-create your themes following the SharePoint 2013 theming guidance, or select a new theme available in SharePoint 2013.  <br/> For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).  <br/> |
|Master pages and CSS files  <br/> |Rework to accommodate the new user experience. For more information, see [Branding issues that may occur when upgrading to SharePoint 2013 [Migrated]](/SharePoint/upgrade-and-update/branding-issues-that-may-occur-when-upgrading-to-sharepoint-2013).  <br/> |
|JavaScript  <br/> |Test to determine whether any actions are required. In some cases, you might have to adjust the scripts to work with the new page model. Verify that it works in both 2010 and 2013 modes.  <br/> |
|Search provider or security trimmer  <br/> |Test to determine whether any actions are required.  <br/> |
|Web Parts  <br/> |Test to determine whether any actions are required. You might have to adjust the Web Parts to work with strict XHMTL mode.  <br/> Test to verify that there have not been changes to any object models or Web services that you call from the Web Part.  <br/> If a Web Part is located on a page but not in a Web Part Zone (so that it is, basically, HTML code embedded directly in a page), it will not work if you reset the page to the default template. There is a site collection health rule that will identify files in this status inside a site collection. There is a link from that rule to the page where they can reset to template.  <br/> |
|Services  <br/> |Test to determine whether any actions are required. Redesign or adjust code, as needed.  <br/> |
|Authentication providers  <br/> |Test to determine whether any actions are required. Redeploy the provider with the same provider name (exactly. This includes the letter case) on a test farm and make sure that it works correctly.  <br/> |
|Custom search solutions that use SQL syntax  <br/> |Rework to use FQL syntax and KQL syntax.  <br/> Custom search solutions in SharePoint 2013 do not support [SQL syntax](https://msdn.microsoft.com/en-us/library/ee558869). Search in SharePoint 2013 supports FQL syntax and KQL syntax for custom search solutions. You cannot use SQL syntax in custom search solutions using any technologies. This includes the query server object model, the client object model, and the Search REST service. Custom search solutions that use SQL syntax with the index server object model and the Query web service that were created in SharePoint Server 2010 will not work when you upgrade them to SharePoint 2013. Queries submitted via these applications will return an error. For more information about how to use FQL syntax and KQL syntax, see [Keyword Query Language (KQL) syntax reference](https://msdn.microsoft.com/library/ee558911%28v=office.15%29) and [FAST Query Language (FQL) syntax reference](https://msdn.microsoft.com/library/ff394606%28v=office.15%29).  <br/> |
   
While you are reviewing customizations in your environment, you should also make sure that the environment is not using any features or elements that are deprecated. For example, Web Analytics from SharePoint 2010 Products are not available in SharePoint 2013 and you should turn them off before upgrading. Also, SQL Server Search queries are not available in SharePoint 2013. For more information, see [Changes from SharePoint 2010 to SharePoint 2013](/previous-versions/office/sharepoint-server-2010/ff607742(v=office.14)).
  
Some methods of deploying customizations might require additional steps in SharePoint 2013. The following table lists issues that you might encounter for specific methods of deploying customizations.
  
|**Deployment method**|**Recommendation**|
|:-----|:-----|
|Customizations deployed as MSI files  <br/> |Contact the vendor for updated files. Most likely, you will have to get a replacement file compatible with SharePoint 2013.  <br/> |
|Manually deployed features, files, or changes  <br/> |You can re-deploy them to the equivalent directory in SharePoint 2013. However, consider packaging them into a deployable solution package for easier administration.  <br/> |
|Sandboxed solutions  <br/> |No special steps. Sandboxed solutions are upgraded with the content databases.  <br/> |
|Solution packages  <br/> |Deploy to SharePoint 2013 again. Make sure that you deploy it to the appropriate directory (/14 or /15), depending on the version.  <br/> Note that you can no longer add partial trust solution packages to the \bin directory. Any files deployed to the \bin directory must be full trust. Be sure to test any such solutions to make sure that deploying them in full trust does not introduce security vulnerabilities. Also, update any deployment scripts to make sure that they specify the correct trust level.  <br/> For more information, see [Install-SPSolution](/powershell/module/sharepoint-server/Install-SPSolution?view=sharepoint-ps).  <br/> |
|Administrator-deployed form templates  <br/> |You must extract them from SharePoint Server 2010 and redeploy them to SharePoint 2013. For more information, see [Upgrade service applications to SharePoint 2013](upgrade-service-applications-to-sharepoint-2013.md).  <br/> |
   
The following kinds of customizations are not supported. If you have any of these customizations in your environment, you must replace them by using a supported kind of customization before you can upgrade. Otherwise, you might experience upgrade issues that cannot be fixed: 
  
- Predefined files, features, or site definitions that were changed.
    
    > [!CAUTION]
    > Some predefined file types — such as document icons or actions — can be carried forward in a supportable way, although this does not occur automatically. Do not copy over the old version files as that can cause other issues, instead, make the same changes to the new version file Modifications to other predefined files, such as server-side ASPX pages, will be lost during upgrade if you reset to the site template or if you don't make the same changes in the new version files. Depending on the files that were changed and the extent of these changes, the upgrade experience can vary significantly. 
  
- SharePoint databases that were changed, either by directly changing data or changing the schema. This includes adding or removing triggers, tables, views, or indexes.
    
If you have any of these kinds of customizations, remove them and replace them with supported customizations before you attempt to upgrade. This is a best practice for helping to make sure that not only your current upgrade will work, but any future upgrades will go more smoothly. Changing predefined files and databases will remain unsupported.
  
## Ensure that future customizations follow best practices
<a name="BestPrac"> </a>

Ensure that your environment performs well and follows best practices. Deploy only those customizations that follow the best practices as described on the following page on MSDN: [Developer Best Practices Resource Center](https://msdn.microsoft.com/en-us/sharepoint/ff660756.aspx).
  
## See also
<a name="BestPrac"> </a>

#### Other Resources

[Best practices for upgrading from SharePoint 2010 to SharePoint 2013](best-practices-for-upgrading-from-sharepoint-2010-to-sharepoint-2013.md)
  
[Use a trial upgrade to SharePoint 2013 to find potential issues](/previous-versions/office/sharepoint-server-2010/cc262155(v=office.14))
  
[Deploy custom features to upgraded site collections in SharePoint Server 2013](/SharePoint/upgrade-and-update/deploy-custom-features-to-upgraded-site-collections-in-sharepoint-server-2013)

