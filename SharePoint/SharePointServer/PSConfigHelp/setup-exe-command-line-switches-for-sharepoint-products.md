---
title: "Setup.exe command-line switches for SharePoint Products"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ROBOTS: NOINDEX
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e57e6d89-abdb-4920-875a-ec12afc2e81b

description: "Summary: Learn how to use the Setup.exe command-line switches in SharePoint Server."
---

# Setup.exe command-line switches for SharePoint Products

 **Summary:** Learn how to use the Setup.exe command-line switches in SharePoint Server. 
  
In SharePoint Server, the Setup.exe command-line tool is used for very few operations, and almost all of these are for IT administrators only.
  
In this article
  
- [How to use a Setup.exe command-line switch](#HowTo)
    
- [Available switches and parameters](#Switches)
    
- [Run Setup.exe with a Config.xml file at a command prompt](#Run)
    
## How to use a Setup.exe command-line switch
<a name="HowTo"> </a>

When you run Setup.exe from the command line, you can specify switches and parameters to provide specific instructions that give the program more information about how to execute the command. The table in the next section contains several examples of switches.
  
## Available switches and parameters
<a name="Switches"> </a>

In SharePoint products, Setup.exe recognizes the following command-line options:
  
|**Switch or parameter**|**Description**|
|:-----|:-----|
|**/config [path and file name]** <br/> |Specifies the configuration file that Setup.exe uses during the installation. By default, the Config.xml file stored in the core product folder directs Setup.exe to install that product. You can edit the Config.xml file to make additional customizations to the installation or you can point to a different configuration file.  <br/> Use **/config** on the Setup command line to point to the location of the default Config.xml file for a particular product or to point to a custom configuration file.  <br/> **Examples** <br/> To point to a customized config.xml file:  <br/> **\\server\share\setup.exe /config** <br/> **\\server\share\folder\Config.xml** <br/> where  _folder_ is the folder that contains the Config.xml file. Or, to point to a different configuration file:  <br/> **\\server\share\setup.exe /config** <br/> **\\server\share\configfiles\oserver-quiet.xml** <br/> **NOTE**: You must use a full path. Setup.exe does not recognize relative paths that contain **/config**.  <br/> |
|**/modify [** _ProductID_ **]** <br/> |Used with a modified Config.xml file to run Setup.exe in maintenance mode and make changes to an existing SharePoint installation, such as adding or removing features. Look up the value of [ _ProductID_] in the Setup.xml file for the product you want to modify. The Setup.xml file is located in the core product folder. In Setup.xml, [ _ProductID_] is equal to the value of the **Id** attribute of the **Setup** element. For example:  <br/> ```- <Setup Id="OServer" Type="Product" ProductCode="{40120000-110D-0000-0000-0000000FF1CE}">``` **Examples** <br/> **\\server\share\setup.exe /modify OServer /config** <br/> **\\server\share\folder\AddConfig.xml** <br/> |
|**/repair [** _ProductID_ **]** <br/> |Runs Setup.exe to repair the files that are needed for a specified product. Look up the value of [ _ProductID_] in the Setup.xml file for the product that you want to modify. Running Setup.exe in repair mode only affects the program files, and does not repair your server configuration or any sites.  <br/> **NOTE**: You should also run the SharePoint Products Configuration Wizard after you run **Setup.exe /repair** to complete the repair of the configuration. If you are using a stand-alone configuration, you can run **Psconfig.exe -setup** from a command line to repair the configuration instead of using the wizard. If you are in a server farm configuration, you should use the full wizard interface. For more information, see the Help for the SharePoint Products Configuration Wizard.  <br/> **Example** <br/> **\\server\share\setup.exe /repair OServer** <br/> |
|**/uninstall [** _ProductID_ **]** <br/> |Removes the specified product from the user's computer. Look up the value of [ _ProductID_] in the Setup.xml file for the product that you want to modify.  <br/> **Example** <br/> **\\server\share\setup.exe /uninstall OServer** <br/> |
   
## Run Setup.exe with a Config.xml file at a command prompt
<a name="Run"> </a>

Running Setup.exe with a configuration file enables you to specify configuration choices (such as a data location or server role) during a quiet installation.
  
For example, you can use the config.xml file for the following tasks: 
  
- Perform a silent installation.
    
- Install by using a common configuration across multiple servers. 
    
- Perform an automated or scripted install.
    
Use the following procedure to run Setup.exe with a configuration file (Config.xml file) at a command prompt. 
  
### To run Setup.exe with a configuration file

1. On the drive which contains the product DVD, change to the root directory to locate the Setup.exe file.
    
2. Run Setup.exe with the selected Config.xml file.
    
  ```
  setup /config <path and file name>
  ```

    > [!NOTE]
    > You can select one of the example files that is included in the SharePoint Server 2016 product DVD, or customize your own configuration file. 
  
3. Press **ENTER**. 
    

