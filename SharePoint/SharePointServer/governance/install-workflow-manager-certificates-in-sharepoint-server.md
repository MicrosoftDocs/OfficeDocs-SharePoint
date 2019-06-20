---
title: "Install Workflow Manager certificates in SharePoint Server"
ms.reviewer: 
ms.author: toresing
author: tomresing
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: c0adc0b5-ea84-46ae-b2a1-9d8d05dbac03
description: "Learn how to configure SSL certificates for encrypted communication between Workflow Manager and SharePoint Server."
---

# Install Workflow Manager certificates in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
Secure Socket Layer (SSL) is an encrypted communication protocol which uses encryption certificates. Workflow Manager and SharePoint Server can communicate in a secure manor using SSL. This article describes the steps required to setup and configure SSL certificates.
  
## Configuration steps

The following sections provide instructions for configuring SSL communication with Workflow Manager and SharePoint Server.
  
### Enable SSL
<a name="appendix1"> </a>

Enable Secure Sockets Layer (SSL) in IIS Manager. For guidance on completing the configuration, see the following:
  
- [Configuring SSL in IIS Manager](/iis/manage/configuring-security/configuring-ssl-in-iis-manager)
    
- [How to Set Up SSL on IIS 7](/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
    
### Install Workflow Manager certificates in SharePoint
<a name="appendix2"> </a>

Under some circumstances, you must obtain and install Workflow Manager "issuer" certificates on SharePoint Server. Here are the circumstances where you must install Workflow Manager certificates:
  
1. If SSL is enabled either on SharePoint Server (which is not the default) or on Workflow Manager (which is the default), AND 
    
2. If SharePoint Server and Workflow Manager do not share a Certificate Authority, AND 
    
3. If Workflow Manager is configured to generate self-signed certificates (which is the default).
    
> [!NOTE]
> Product trial, workflow development, and troubleshooting are easier if SSL is not enabled. However, communication between SharePoint Server and Workflow Manager is not encrypted if SSL is not enabled. For this reason, SSL should be enabled for production configurations. 
  
 **To obtain and export certificates from the Workflow Manager server**
  
1. On a computer that has Workflow Manager installed, choose **IIS Manager**, **Sites**. Right-click **Workflow Management Site**, and then choose **Edit Bindings**.
    
2. Choose the **https** port, and then choose **Edit**. Choose the **View** button in the **SSL Certificate** section. 
    
3. To export the issuer certificate, do the following:
    
1. In the **Certificate** window, choose the **Certification path** tab. 
    
2. Select **root certification path** and choose **View**.
    
3. On the **Details** tab, choose **Export Certificate**, and take the default options in the export wizard.
    
4. Give the exported certificate file a friendly name.
    
 **To install certificates on SharePoint Server**
  
1. Copy the issuer certificate to your SharePoint Server computer.
    
2. Add the certificates to the Windows Certificate store.
    
3. For each certificate, do the following:
    
1. Double-click the file to open and view the certificate.
    
2. On the certificate, choose the **Install Certificate** button to start the installation wizard. 
    
3. In the wizard, choose **Place all certificates in the following store**, and then choose **Trusted Root Certification Authorities**.
    
4. Add the certificates to SharePoint Server by going to the SharePoint Management shell and running the **New-SPTrustedRootAuthority** cmdlet. Do this for each certificate file. 
    

