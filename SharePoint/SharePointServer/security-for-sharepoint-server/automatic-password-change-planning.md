---
title: "Plan automatic password change in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 8/23/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 3fae32fe-1a04-4854-9d21-cbfd93045202
description: "Learn about the automatic password changes and how to deploy them in SharePoint Server."
---

# Plan automatic password change in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
To simplify password management, the automatic password change feature enables you to update and deploy passwords without having to perform manual password update tasks across multiple accounts, services, and web applications. You can configure the automatic password change feature to determine whether a password is about to expire and reset the password using a long, cryptographically-strong random string. To implement the automatic password change feature, you have to configure managed accounts.
  
    
## Configure managed accounts
<a name="configure"> </a>

SharePoint Server supports how to create managed accounts to improve security and guarantee application isolation. By using managed accounts, you can configure the automatic password change feature to deploy passwords across all services in the farm. You can configure SharePoint web applications and services, running on application servers in a SharePoint farm, to use different domain accounts. You can create multiple accounts in Active Directory Domain Services (AD DS), and then register each of these accounts in SharePoint Server. You can map managed accounts to various services and web applications in the farm.
  
## Reset passwords automatically on a schedule
<a name="Reset"> </a>

Prior to the implementation of the automatic password change feature, updating passwords required resetting each account password in AD DS and then manually updating account passwords on all of the services that are running on all the computers in the farm. To do this, you had to run the Stsadm command-line tool or use the SharePoint Central Administration web application. By using the automatic password change feature, you can now register managed accounts and enable SharePoint Server to control account passwords. Users have to be notified about planned password changes and related service interruptions. However, the accounts that are used by a SharePoint farm, web applications, and various services can be automatically reset and deployed within the farm as necessary, based on individually configured password reset schedules.
  
## Detect password expiration
<a name="Detect"> </a>

IT departments typically impose a policy requiring that all domain account passwords be reset regularly, for example, every 60 days. SharePoint Server can be configured to detect imminent password expiration, and send an e-mail notification to a designated administrator. Even without requiring administrator intervention, SharePoint Server can be configured to generate and reset passwords automatically. The automatic password reset schedule is also configurable to guarantee that the impact of possible service interruptions during a password reset will be minimal.
  
## Reset the account password immediately
<a name="ResetImmediately"> </a>

You can always override any automatic password reset schedule and force an immediate service account password reset by using a specific password value. In this scenario, the password for the service account can also be changed in AD DS by SharePoint Server. The new password is then immediately propagated to other servers in the farm.
  
## Synchronize SharePoint Foundation account passwords with Active Directory Domain Services
<a name="Synchronize"> </a>

If AD DS and SharePoint Server account passwords are not synchronized, services in the SharePoint farm won't start. If an Active Directory administrator changes an Active Directory account password without coordinating the password change with a SharePoint administrator, there is a risk of service interruptions. In this scenario, a SharePoint administrator can immediately reset the password from the Account Management page using the password value that was changed in AD DS. The password is updated and immediately propagated to the other servers in the SharePoint farm.
  
## Reset all passwords immediately
<a name="ResetAllPwd"> </a>

If an administrator suddenly leaves your organization, or if the service account passwords need to be immediately reset for any other reason, you can quickly create a Microsoft PowerShell script that calls the password change cmdlets. You can use the script to generate new random passwords and deploy the new passwords immediately.
  
## Credential change process
<a name="Credentials"> </a>

When SharePoint Server changes the credentials for a managed account, the credential change process will occur on one server in the farm. Each server in the farm will be notified that the credentials are about to change and servers can perform critical pre-change actions, if they are necessary. If the account password has not yet been changed, then SharePoint Server will attempt to change the password using either a manually entered password, or a long, cryptographically-strong random string. The complexity settings will be queried from the appropriate policy (network or local), and the generated password will be equivalent to the detected settings. SharePoint Server will attempt to commit a password change. If it is unable to commit the password change, it will retry by using a new sequence, for a specified number of times. If the account password update process succeeds, it will proceed to the next dependent service, where it will again attempt to commit a password change. If it does not ultimately succeed, each dependent service will be notified that they can resume normal activity. Either success in committing a password change or failure to commit will result in the generation of an automated password change status notification that will be sent by e-mail to farm administrators. 
  
## Service impact when you change passwords
<a name="ServiceImpact"> </a>

 When an administrator performs a password change for the servers in the SharePoint search topology, there is an implied query downtime when the services are restarted. The query downtime is typically in the range of 3-5 minutes. 
  
## See also
<a name="ServiceImpact"> </a>

#### Concepts

[Configure automatic password change in SharePoint Server](../administration/configure-automatic-password-change.md)

