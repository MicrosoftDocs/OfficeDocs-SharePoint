---
title: Firewall client settings on the cache host are incorrect (SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: f8dcfd5c-aaec-46cd-b25e-94e14bf98c7d
---


# Firewall client settings on the cache host are incorrect (SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "Firewall client settings on the cache host are incorrect", in SharePoint Server 2016. **Rule Name:**   Firewall client settings on the cache host are incorrect. **Summary:**  Firewall rule settings for App fabric caching are disabled. **Cause:**   Firewall rule settings for App fabric caching are disabled. **Resolution: Enable the firewall rules for the AppFabric Caching service.**
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
  
2. On **Server Manager**, click **Tools**, and then select **Windows Firewall with Advanced Security**.
    
  
3. In the **Windows Firewall with Advanced Security** console tree, click **Inbound Rules**.
    
  
4. In the **Inbound Rules** list, right-click **AppFabric Caching Service (TCP-In)**, and then select **Enable Rule**.
    
  
5. In the **Windows Firewall with Advanced Security** console tree, click **Outbound Rules**.
    
  
6. In the **Outbound Rules** list, right-click **AppFabric Caching Service (TCP-Out)** and then select **Enable Rule**.
    
  
By default, the **Repair Automatically** option is enabled for this rule. You can restore the default setting for this rule by doing the following:
1. On the the SharePoint Central Administration website, click **Monitoring**.
    
  
2. On the Monitoring page, in the **Health Analyzer** section, click **Review rule definitions**.
    
  
3. On the Health Analyzer Rule Definitions – All Rules page, in the **Category: Configuration** section, click the name of the rule.
    
  
4. On the **Health Analyzer Rule Definitions** page, click **Edit Item**.
    
  
5. Select the **Repair Automatically** check box, and then click **Save**.
    
  

