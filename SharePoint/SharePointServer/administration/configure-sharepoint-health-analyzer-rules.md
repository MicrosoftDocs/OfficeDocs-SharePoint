---
title: "Configure SharePoint Health Analyzer rules in SharePoint Server"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/18/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 937a136c-7cc1-4e61-8a2c-2161d484c13f

description: "Learn to configure SharePoint Server Health Analyzer rules by using Central Administration."
---

# Configure SharePoint Health Analyzer rules in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
## Before you begin
<a name="begin"> </a>

Because SharePoint Server runs as websites in Internet Information Services (IIS), administrators and users depend on the accessibility features that browsers provide. SharePoint Server supports the accessibility features of supported browsers. For more information, see the following resources:
  
- [Plan browser support](https://docs.microsoft.com/en-us/sharepoint/install/browser-support-planning-0)
    
- [Accessibility in SharePoint](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/accessibility-in-sharepoint)
    
- [Keyboard shortcuts](https://support.office.com/article/keyboard-shortcuts-in-sharepoint-online-466e33ee-613b-4f47-96bb-1c20f20b1015)
    
- [Touch](https://go.microsoft.com/fwlink/p/?LinkId=246506)
    
## Configuring SharePoint Health Analyzer rules
<a name="begin"> </a>

You can accept the default settings for each health rule, or you can change settings for a health rule by using Central Administration.
  
 **To configure health rules by using Central Administration**
  
1. Verify that the user account performing this procedure is a member of the Farm Administrators group. 
    
2. In Central Administration, on the home page, click **Monitoring**.
    
3. On the **Monitoring** page, under **Health Analyzer**, click **Review rule definitions**.
    
4. On the **Health Analyzer Rule Definitions** page, click the rule that you want to configure. 
    
5. In the **Health Analyzer Rule Definitions** dialog, click **Edit Item**.
    
6. Edit one or more rule fields, and then click **Save**.
    
    To leave the rule unchanged, either dismiss the dialog or click **Cancel**.
    
Each health rule has configurable fields, which are described in the following table.
  
**Configurable fields for SharePoint Health Analyzer rules**

|**Configurable field**|**Description**|
|:-----|:-----|
|Title  <br/> |The name of the health rule. You can rename a health rule to clarify its functionality. The title is the name of the rule as it appears in the **Health Rule Definitions** list in Central Administration.  <br/> Changing the title does not affect how the rule runs.  <br/> |
|Scope  <br/> |You can set a health rule to run against all servers or any server. If set to any server, the rule will run on the first available server that the system encounters.  <br/> |
|Schedule  <br/> |You can schedule a health rule to run hourly, daily, weekly, monthly, or on demand only.  <br/> |
|Enabled  <br/> |You can select or clear this check box to enable or disable a health rule.  <br/> |
|Repair Automatically  <br/> |You can specify whether a health rule automatically attempts to repair errors that it finds. If this option is selected, SharePoint Server will repair errors as soon as they are found, as defined by the rule.  <br/> > [!NOTE]> If no repair is specified by the rule, the system does not attempt to repair the problem.           |
|Version  <br/> |Version history enables you to track the changes performed on each rule. The version number is updated every time that the rule is saved. The version number does not affect how the rule works.  <br/> |
   
Each health rule has read-only fields, which are described in the following table.
  
**Read-only fields for SharePoint Health Analyzer rules**

|**Read-only field**|**Description**|
|:-----|:-----|
|Version  <br/> |The current version number of the rule.  <br/> |
|Created at  <br/> |The date and time that the rule was originally created and the user account that created the rule.  <br/> |
|Last modified at  <br/> |The date and time that the rule was last changed and the user account that created the rule.  <br/> |
   
For more information about SharePoint Server monitoring configuration, see [Configure monitoring in SharePoint Server 2016](configure-monitoring.md).
  
## See also
<a name="begin"> </a>

#### Concepts

[SharePoint Health Analyzer rules reference for SharePoint Server 2016](../technical-reference/sharepoint-health-analyzer-rules-reference.md)

