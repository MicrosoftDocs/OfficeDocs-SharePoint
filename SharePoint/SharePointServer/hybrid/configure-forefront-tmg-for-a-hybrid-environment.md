---
title: "Configure Forefront TMG for a hybrid environment"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/22/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- SPO_Content
localization_priority: Normal
ms.assetid: 46aecccb-6196-48b4-a889-cbd408354d56
description: "Learn how to configure Forefront TMG 2010 as a reverse proxy device in a SharePoint hybrid environment."
---

# Configure Forefront TMG for a hybrid environment

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
This article tells you how to set up Forefront Threat Management Gateway (TMG) 2010 for use as a reverse proxy for a hybrid SharePoint Server environment.
  
For complete information about Forefront Threat Management Gateway (TMG) 2010, see [Forefront Threat Management Gateway (TMG) 2010](/previous-versions/tn-archive/ff355324(v=technet.10)).
  
    
## Before you begin
<a name="byb"> </a>

Before you begin, there are a few things you need to know:
  
- TMG has to be deployed in an **edge configuration**, with at least one network adapter connected to the Internet and configured for the external network in TMG and at least one network adapter connected to the intranet network and configured for the internal network in TMG.
    
- The TMG server has to be a domain member in the Active Directory domain forest that contains your Active Directory Federation Services (AD FS) 2.0 server. The TMG server has to be joined to this domain to use SSL client certificate authentication, which is used for authenticating inbound connections from SharePoint in Microsoft 365.
    
    > [!SECURITY NOTE]
    > As a general best practice for edge deployments, you normally install Forefront TMG in a separate forest (rather than in the internal forest of your corporate network), with a one-way trust to the corporate forest. However, you can configure client certificate authentication only for users in the domain to which the TMG server is joined, so this practice cannot be followed for hybrid environments. > For more info about TMG network topology considerations, see [Workgroup and domain considerations](/previous-versions/tn-archive/dd897048(v=technet.10)). 
  
- Deploying TMG 2010 for use in a SharePoint Server hybrid environment in a back-to-back configuration is theoretically possible but has not been tested and may not work.
    
- TMG 2010 includes both diagnostic logging and a real-time logging interface. Logging plays an important role in troubleshooting issues with connectivity and authentication between SharePoint Server and SharePoint in Microsoft 365. Identifying the component that is causing a connection failure can be challenging, and TMG logs are the first place you should look for clues. Troubleshooting can involve comparing log events from TMG logs, SharePoint Server ULS logs, Windows Server event logs, and Internet Information Services (IIS) logs on multiple servers.
    
For more information on how to configure and use logging in TMG 2010, see [Using diagnostic logging](/previous-versions/tn-archive/dd897109(v=technet.10)).
  
For more information on general TMG 2010 troubleshooting, see [Forefront TMG Troubleshooting](/previous-versions/tn-archive/dd897100(v=technet.10)).
  
For more information on troubleshooting techniques and tools for SharePoint Server hybrid environments, see [Troubleshooting hybrid environments](/SharePoint/hybrid/hybrid).
  
## Install TMG 2010
<a name="install"> </a>

If you have not already installed TMG 2010 and configured it for your network, use this section to install TMG 2010 and prepare the TMG system.
  
 **Install TMG 2010**
  
1. Install Forefront TMG 2010 if it is not already installed. For more information on installing TMG 2010, see [Forefront TMG Deployment](https://go.microsoft.com/fwlink/p/?LinkId=403873).
    
2. Install all the available service packs and updates for TMG 2010. For more information, see [Installing Forefront TMG Service Packs](/previous-versions/tn-archive/ff717843(v=technet.10)).
    
3. Join the TMG server computer to the on-premises Active Directory domain if it is not already a domain member. 
    
    For more info about deploying TMG 2010 in a domain environment, see [Workgroup and domain considerations](/previous-versions/tn-archive/dd897048(v=technet.10)).
    
## Import the Secure Channel SSL certificate
<a name="cert"> </a>

You must import the Secure Channel SSL certificate into both the Personal store of the local computer account and the Personal store of the Microsoft Forefront TMG Firewall service account (fwsvc).
  
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)|The location of the **Secure Channel SSL certificate** is recorded in **Row 1** (Secure Channel SSL Certificate location and Filename) of **Table 4b: Secure Channel SSL Certificate**.  <br/> If the certificate contains a private key, you will need to provide the certificate password, which is recorded in **Row 4** (Secure Channel SSL Certificate password) of **Table 4b: Secure Channel SSL Certificate**.  <br/> |
   
 **Import the certificate**
  
1. Copy the certificate file from the location specified in the worksheet to a folder on the local hard disk.
    
2. On the reverse proxy server, open MMC, and add the **Certificate Management** snap-in for both the local **computer account** and the local **fwsrv service account**.
    
    > [!NOTE]
    > After TMG 2010 has been installed, the friendly name of the fwsrv service is the **Microsoft Forefront TMG Firewall** service. 
  
3. Import the Secure Channel SSL certificate to the **Personal** certificate store of the computer account. 
    
4. Import the Secure Channel SSL certificate to the **Personal** certificate store of the **fwsrv** service account. 
    
For more info about how to import an SSL certificate, see [Import a Certificate](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc754489(v=ws.11)).
  
## Configure TMG 2010
<a name="config"> </a>

In this section, you configure a **web listener** and a **publishing rule** that will receive inbound requests from SharePoint in Microsoft 365 and relay them to the primary web application of your SharePoint Server farm. The web listener and publishing rule work together to define the connection rules and to pre-authenticate and relay the requests. You configure the web listener to authenticate inbound connections using the Secure Channel certificate you installed in the last procedure. 
  
For more info about configuring publishing rules in TMG, see [Configuring Web publishing](/previous-versions//cc441546(v=technet.10)).
  
For more info about SSL bridging in TMG 2010, see [About SSL bridging and publishing](/previous-versions/tn-archive/cc995200(v=technet.10)).
  
Use the following procedure to create the publishing rule and web listener.
  
 **Create the publishing rule and web listener**
  
1. In the Forefront TMG Management Console, in the left navigation pane, right-click **Firewall Policy**, and then select **New**.
    
2. Select **SharePoint Site Publishing Rule**.
    
3. In the **New SharePoint Publishing Rule Wizard**, in the **Name** text box, enter the name of the publishing rule (for example, "Hybrid Publishing Rule"). Select **Next**.
    
4. Select **Publish a single Web site or load balancer**, and then select **Next**.
    
5. To use **HTTP** for the connection between TMG and your SharePoint Server farm, select **Use non-secured connection to connect the published Web server or server farm**, and then select **Next**.
    
    To use **HTTPS** for the connection between TMG and your SharePoint Server farm, select **Use SSL to connect the published Web server or server farm**, and then select **Next**.
    
    > [!NOTE]
    > If you use SSL, ensure that you have a valid certificate installed on the primary web application. 
  
6. In the **Internal Publishing Details** dialog box, in the **Internal site name** text box, enter the internal DNS name of the *bridging URL*, and then select **Next**. This is the URL that the TMG server will use to relay requests to the primary web application. 
    
    > [!NOTE]
    > Do not enter the protocol (http:// or https://). 
  
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)| The Bridging URL is recorded in one the following locations in the SharePoint Hybrid worksheet:  <br/>  If your primary web application is configured with a  *host-named site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5a: Primary web application (host-named site collection)**.  <br/>  If your primary web application is configured with a  *path-based site collection*  , use the value in **Row 1** (Primary web application URL) of **Table 5b: Primary web application (path-based site collection without AAM)**.  <br/>  If your primary web application is configured with a  *path-based site collection with AAM*  , use the value in **Row 5** (Primary web application URL) of **Table 5c: Primary web application (path-based site collection with AAM)**.  <br/> |
   
7. In the **Use a computer name or IP address to connect to the published server** box, optionally enter the IP address or the fully qualified domain name (FQDN) of the primary web application or network load balancer, and then select **Next**. 
    
    > [!NOTE]
    > If TMG can resolve the primary web application using the host name you provided in the previous step, you do not have to perform this step. 
  
8. In the **Public Name Details** dialog box, accept the default setting on the **Accept requests for** menu. In the **Public name** text box, enter the host name of your *External URL*  (for example, "sharepoint.adventureworks.com"), and then select **Next**. This is the host name in the external URL that SharePoint in Microsoft 365 will use to connect with your SharePoint Server farm.
    
    > [!NOTE]
    > Do not enter the protocol (http:// or https://). 
  
|||
|:-----|:-----|
|![Edit icon](../media/mod_icon_edit_m.png)|The External URL is recorded in **Row 3** (External URL) of **Table 3: Public Domain Info** in the SharePoint Hybrid worksheet. |
   
9. In the **Select a Web Listener** dialog box, select **New**.
    
10. In the **New Web Listener Wizard** dialog box, in the **Web listener name** text box, enter a name for the web listener, and then select **Next**.
    
11. In the Client Connection Security dialog box, select **Require SSL secured connections with clients**, and then select **Next**.
    
12. In the **Web Listener IP Addresses** dialog box, select **External \<All IP addresses\>**, and then select **Next**. 
    
    If you want to restrict the listener to listen only on a specific external IP address, select **Select IP Addresses**, and then in the **External Network Listener IP Selection** dialog box, select **Specified IP addresses on the Forefront TMG computer in the selected network**. To specify an IP address, select **Add**, and then select **OK**.
    
13. In the **Listener SSL Certificates** dialog box, select **Use a single certificate for this Web Listener**, and select the **Select Certificate** button. In the **Select Certificate** dialog box, select the **Secure Channel SSL certificate** you imported to the TMG computer, select **Select**, and then select **Next**.
    
14. In the **Authentication Settings** dialog box, select **SSL Client Certificate Authentication**, and then select **Next**. This setting enforces client certificate credentials for inbound connections using the Secure Channel certificate.
    
15. To bypass Forefront TMG single sign-on settings, select **Next**. 
    
16. Review the **New Listener** summary page, and select **Finish**. This returns you to the Publishing Rule Wizard in which your newly created web listener is automatically selected.
    
17. In the **Select Web Listener** dialog box, in the **Web Listener** dropdown, make sure the correct web listener is selected, and select **Next**.
    
18. In the **Authentication Delegation** dialog box, select **No delegation, but client may authenticate directly** from the dropdown, and then select **Next**.
    
19. In the **Alternate Access Mapping Configuration** dialog box, select **SharePoint AAM is already configured on the SharePoint server**, and then select **Next**.
    
20. In the **User Sets** dialog box, select the **All Authenticated Users** entry, and select **Remove**. Then select **Add**, and in the **Add Users** dialog box, select **All Users**, and then select **Add**. To close the **Add Users** dialog box, Select **Close**, and then select **Next**.
    
21. In the **Completing the New SharePoint Publishing Rule Wizard** dialog box, confirm your settings, and then select **Finish**.
    
There are several settings that you must now verify or change in the publishing rule you just created.
  
 **Finalize the publishing rule configuration**
  
1. In the Forefront TMG Management Console, in the left navigation pane, select **Firewall Policy**, and in the **Firewall Policy Rules** list, right-click the publishing rule you just created, and select **Configure HTTP**.
    
2. In the **Configure HTTP policy for rule** dialog box, on the **General** tab, under **URL Protection**, confirm that both **Verify normalization** and **Block high bit characters** are unchecked, and then select **OK**.
    
3. Right-click the publishing rule you just created again, and select **Properties**.
    
4. In the **\<rule name\> Properties** dialog box, on the **To** tab, clear the **Forward the original host header instead of the actual one** box. Under **Proxy requests to published site**, ensure that **Requests appear to come from the original client** is selected. 
    
5. On the **Link Translation** tab, ensure that the **Apply link translation to this rule** check box is set correctly: 
    
  - If the internal URL of your primary web application and the external URL are identical, clear the **Apply link translation to this rule** check box. 
    
  - If the internal URL of your primary web application and the external URL are different, check the **Apply link translation to this rule** check box. 
    
6. On the **Bridging** tab, under **Web server**, ensure that the correct **Redirect requests to \<HTTP port or SSL port\>** check box is checked and that the port in the text box corresponds to the port your internal site is configured to use. 
    
7. To save your changes to the publishing rule, select **OK**. 
    
8. In the Forefront TMG Management Console, on the top bar, to apply your changes to TMG, select **Apply**. It might take one or two minutes for TMG to process your changes. 
    
9. To validate your configuration, right-click the new publishing rule from the **Firewall Policy Rules** list, and select **Properties**.
    
10. In the **\<rule name\> Properties** dialog box, select the **Test Rule** button. TMG runs a series of tests to check for connectivity to the SharePoint in Microsoft 365 site, and displays the results of the tests in a list. For a description of the test and its results, select each configuration test. Fix any errors that appear. 
    
## See also
<a name="config"> </a>

#### Concepts

[Hybrid for SharePoint Server](hybrid.md)
  
[Configure a reverse proxy device for SharePoint Server hybrid](configure-a-reverse-proxy-device-for-sharepoint-server-hybrid.md)
#### Other Resources

[Configuring Web publishing](/previous-versions//cc441546(v=technet.10))
  
[Forefront Threat Management Gateway (TMG) 2010](/previous-versions/tn-archive/ff355324(v=technet.10))

