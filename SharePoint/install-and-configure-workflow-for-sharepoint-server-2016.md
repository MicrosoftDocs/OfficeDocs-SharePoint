---
title: Install and configure workflow for SharePoint Server 2016
ms.assetid: b62b6690-a1a6-4163-bdb5-8abae968c5c8
---


# Install and configure workflow for SharePoint Server 2016
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Topic Last Modified:** 2017-05-30* **Summary:  ** Learn how to install and configure workflow platforms in SharePoint Server 2013.In this article:
-  [Overview](#section1)
    
  
-  [Before you begin](#section2)
    
  
-  [Install and configure SharePoint Server 2013](#section3)
    
  
-  [Install and configure Workflow Manager](#section4)
    
  
-  [Configure Workflow Manager to work with the SharePoint Server 2013 farm](#section5)
    
  
-  [Validate the installation](#section6)
    
  
-  [Troubleshooting](#section7)
    
  

> [!IMPORTANT:]

  
    
    


> [!NOTE:]

  
    
    


## Overview
<a name="section1"> </a>

A new option exists when you build a workflow for SharePoint Server 2016. This option is called **Platform Type**. The figure shows the **Platform Type** option when you are creating a new workflow by using SharePoint Designer 2013. **Figure: SharePoint 2013 includes three workflow platform options.**
  
    
    
![Three workflow platforms in SharePoint 2013.](images/)
  
    
    

  
    
    
The only platform available when you first install SharePoint Server 2016 is the SharePoint 2010 Workflow platform. The SharePoint 2013 Workflow platform and the Project Server platform require additional steps. The three workflow platforms are outlined in the following table.
### Workflow Platform types available in SharePoint Server 2016

Platform Type Platform Framework Requirements **SharePoint 2010 Workflow** <br/> Windows Workflow Foundation 3  <br/> Installs automatically with SharePoint 2013 Products.  <br/> **SharePoint 2013 Workflow** <br/> Windows Workflow Foundation 4  <br/> Requires SharePoint Server 2016 and Workflow Manager.  <br/> 
> [!NOTE:]

  
    
    

 **SharePoint 2013 Workflow – Project Server** <br/> Windows Workflow Foundation 4  <br/> Requires SharePoint Server 2016, Workflow Manager, and Project Server 2016.  <br/> 
  
    
    
To learn more about workflow development with SharePoint Designer 2013 and other aspects of workflow, see the  [Workflow in SharePoint 2013 Resource Center](http://technet.microsoft.com/sharepoint/jj556245).
## Before you begin
<a name="section2"> </a>

Before you begin installation, make sure that you have met all hardware and software requirements for both SharePoint Server 2016 and Workflow Manager. For more information, see  [Hardware and software requirements for SharePoint Server 2016](html/hardware-and-software-requirements-for-sharepoint-server-2016.md).
> [!NOTE:]

  
    
    


> [!IMPORTANT:]

  
    
    


## Install and configure SharePoint Server 2016
<a name="section3"> </a>

You must install and configure SharePoint Server 2016. To do so, see  [Install and deploy SharePoint 2013](http://technet.microsoft.com/en-us/sharepoint/fp142376.aspx).
> [!NOTE:]

  
    
    


## Install and configure Workflow Manager
<a name="section4"> </a>

You must install and configure Workflow Manager. To do so, see  [Installing and Configuring Workflow Manager 1.0](http://msdn.microsoft.com/en-us/library/jj193478.aspx).
## Configure Workflow Manager to work with the SharePoint Server 2016 farm
<a name="section5"> </a>

You must consider the following two key factors before configuring Workflow Manager to work with SharePoint Server 2016. 
- Is Workflow Manager installed on a server that is part of the SharePoint farm?
    
  
- Will communication between Workflow Manager and SharePoint Server 2016 use **HTTP** or **HTTPS** ?
    
  
These factors translate into four scenarios. Each scenario configures a SharePoint Server 2016 farm to communicate and function with the Workflow Manager farm. Follow the scenario that matches your circumstance.
### 

1: Workflow Manager is installed on a server that is part of the SharePoint 2013 farm. Communication takes place by using HTTP.  <br/> 2: Workflow Manager is installed on a server that is part of the SharePoint 2013 farm. Communication takes place by using HTTPS.  <br/> 3: Workflow Manager is installed on a server that is NOT part of the SharePoint 2013 farm. Communication takes place by using HTTP.  <br/> 4: Workflow Manager is installed on a server that is NOT part of the SharePoint 2013 farm. Communication takes place by using HTTPS.  <br/> 
  
    
    

> [!NOTE:]

  
    
    


> [!TIP:]

  
    
    

 **To configure Workflow Manager on a server that is part of the SharePoint 2013 farm and on which communication takes place by using HTTP**
1. Log on to the computer in the SharePoint Server 2016 farm where Workflow Manager was installed. 
    
  
2. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint 2013 Management Shell** and choosing **Run as administrator**.
    
  
3. Run the **Register-SPWorkflowService** cmdlet.
    
    **Example**:
    


  ```
  
Register-SPWorkflowService -SPSite "http://myserver/mysitecollection" -WorkflowHostUri "http://workflow.example.com:12291" -AllowOAuthHttp
  ```

4. Log on to each server in the SharePoint Server 2016 farm.
    
    Each server in the SharePoint Server 2016 farm must have the Workflow Manager Client installed. 
    
    > [!NOTE:]
      
5. Install the Workflow Manager Client on each server in the SharePoint farm.
    
    Download and install the Workflow Manager Client here:  [http://go.microsoft.com/fwlink/p/?LinkID=268376](http://go.microsoft.com/fwlink/p/?LinkID=268376)
    
  
 **To configure Workflow Manager on a server that is part of the SharePoint 2013 farm and on which communication takes place by using HTTPS**
1. Determine if you need to install Workflow Manager certificates in SharePoint.
    
    Under some circumstances, you have to obtain and install Workflow Manager certificates. If your installation requires that you obtain and install these certificates, you must complete that step before continuing. To learn whether you need to install certificates, and for instructions, see  [Install Workflow Manager certificates in SharePoint Server 2013](html/install-workflow-manager-certificates-in-sharepoint-server-2013.md).
    
  
2. Log into the computer in the SharePoint Server 2016 farm where Workflow Manager was installed. 
    
  
3. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint 2013 Management Shell** and choosing **Run as administrator**.
    
  
4. Run the **Register-SPWorkflowService** cmdlet.
    
    **Example**:
    


  ```
  
Register-SPWorkflowService -SPSite "https://myserver/mysitecollection" -WorkflowHostUri "https://workflow.example.com:12290"
  ```

5. Log on to each server in the SharePoint Server 2016 farm.
    
    Each server in the SharePoint Server 2016 farm must have the Workflow Manager Client installed. 
    
    > [!NOTE:]
      
6. Install the Workflow Manager Client on each server in the SharePoint farm.
    
    Download and install the Workflow Manager Client here:  [http://go.microsoft.com/fwlink/p/?LinkID=268376](http://go.microsoft.com/fwlink/p/?LinkID=268376)
    
  
 **To configure Workflow Manager on a server that is NOT part of the SharePoint 2013 farm and on which communication takes place by using HTTP**
1. Log on to each server in the SharePoint Server 2016 farm.
    
  
2. Install the Workflow Manager Client on each server in the SharePoint farm.
    
    Before you can run the workflow pairing cmdlet, you must install Workflow Manager Client on each of the servers in the SharePoint farm. 
    
    Download and install the Workflow Manager Client here:  [http://go.microsoft.com/fwlink/p/?LinkID=268376](http://go.microsoft.com/fwlink/p/?LinkID=268376)
    
  
3. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint 2013 Management Shell** command and choosing **Run as administrator**.
    
  
4. Run the **Register-SPWorkflowService** cmdlet. The cmdlet should be run only once and can be run from any of the servers in the SharePoint farm.
    
    **Example**:
    


  ```
  
Register-SPWorkflowService -SPSite "http://myserver/mysitecollection" -WorkflowHostUri "http://workflow.example.com:12291" -AllowOAuthHttp
  ```


    > [!IMPORTANT:]
      
 **To configure Workflow Manager on a server that is NOT part of the SharePoint 2013 farm and on which communication takes place by using HTTPS**
1. Determine whether you need to install Workflow Manager certificates in SharePoint 2013.
    
    Under some circumstances, you have to obtain and install Workflow Manager certificates. If your installation requires that you obtain and install these certificates, you must complete that step before continuing. To learn whether you need to install certificates, and for instructions, see  [Install Workflow Manager certificates in SharePoint Server 2013](html/install-workflow-manager-certificates-in-sharepoint-server-2013.md).
    
  
2. Log on to each server in the SharePoint Server 2016 farm.
    
  
3. Install the Workflow Manager Client on each server in the SharePoint farm.
    
    Before you can run the workflow pairing cmdlet, you must install Workflow Manager Client on each of the servers in the SharePoint farm. 
    
    Download and install the Workflow Manager Client here:  [http://go.microsoft.com/fwlink/p/?LinkID=268376](http://go.microsoft.com/fwlink/p/?LinkID=268376)
    
  
4. Open the SharePoint Management Shell as an administrator. This is accomplished by right-clicking the **SharePoint 2013 Management Shell** command and choosing **Run as administrator**.
    
  
5. Run the **Register-SPWorkflowService** cmdlet.
    
    **Example**:
    


  ```
  
Register-SPWorkflowService -SPSite "https://myserver/mysitecollection" -WorkflowHostUri "https://workflow.example.com:12290"
  ```


    > [!IMPORTANT:]
      

## Validate the installation
<a name="section6"> </a>

Use these steps to validate that you have successfully installed and configured the required components. **To validate the installation**
1. Add a user to your SharePoint site, and grant the user Site Designer permissions.
    
  
2. Install SharePoint Designer 2013 and create a workflow based on the SharePoint 2013 Workflow platform. For more information, see  [Creating a workflow by using SharePoint Designer 2013 and the SharePoint 2013 Workflow platform](http://msdn.microsoft.com/library/jj554671%28v=office.15%29).
    
  
3. Run this workflow from the SharePoint user interface.
    
  

## Troubleshooting
<a name="section7"> </a>

For security reasons, the Setup account cannot be used to create a workflow based on the SharePoint 2013 Workflow platform. If you try to create a workflow based on the SharePoint 2013 Workflow platform by using SharePoint Designer 2013, you receive a warning that the list of workflow actions do not exist, and the workflow is not created.The user who deploys and runs a workflow must be added to the User Profile service. Check the User Profile service application page in Central Administration to confirm that the user you are using to validate workflow installation is in the User Profile service. You can determine which ports SharePoint Server 2016 and Workflow Manager are using for both HTTP and HTTPS by using IIS Manager as shown in the figure. **Figure: Use IIS Manager to view the ports used by Workflow Manager**
  
    
    
![View ports in IIS Manager.](images/)
  
    
    
Workflow Manager communicates by using TCP/IP or Named Pipes. Make sure that the appropriate communication protocol is enabled on the SQL Server instance that hosts the Workflow Manager databases.The SQL Browser Service must be running on the SQL Server instance that hosts the Workflow Manager databases.The System Account cannot be used to develop a workflow.To troubleshoot SharePoint Server 2016, see **Troubleshooting SharePoint Server 2016**.
# See also

#### 

 [Installation and Deployment for SharePoint 2013 Resource Center](http://technet.microsoft.com/sharepoint/fp142376)
  
    
    
 [What's New in SharePoint 2013 Resource Center](http://technet.microsoft.com/sharepoint/fp142374)
  
    
    
 [Workflow Resource Center](http://technet.microsoft.com/sharepoint/jj556245)
  
    
    

  
    
    

