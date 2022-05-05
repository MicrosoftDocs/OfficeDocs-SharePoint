---
title: "Install the previous OneDrive sync app"
ms.reviewer: garezni
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: one-drive
ms.localizationpriority: high
description: "In this article, you'll learn how to install the previous OneDrive sync app (Groove.exe) for use with SharePoint Server."
---

# Install the previous OneDrive sync app

If your organization still uses SharePoint Server 2016 or earlier, users can't use the new OneDrive sync app (OneDrive.exe) to sync files. They need to use the previous OneDrive for Business sync app (Groove.exe). This article helps you install Groove.exe. If your organization uses SharePoint Server 2019, users should use the new OneDrive sync app (OneDrive.exe). [Learn more](/sharepoint/install/new-onedrive-sync-client)

> [!IMPORTANT]
> Support for the previous OneDrive for Business sync app (Groove.exe) with Microsoft 365 ended on January 11, 2021. Groove.exe will continue to work for files in SharePoint Server. [Learn how to transition to the new sync app](transition-from-previous-sync-client.md)

## Install Groove.exe with Office 2016

The previous sync app (Groove.exe) is no longer installed by default with Office 2016 Click-to-run. You need to use a custom installation to extract OneDrive.

1. Download the [Office Deployment Tool](https://www.microsoft.com/download/details.aspx?id=49117), and then save the file to your desktop.
2. From your desktop, double-click **OfficeDeploymentTool.exe**, and then extract the files to your desktop. 
   The following files will be displayed on your desktop:

    - Setup.exe
    - Configuration.xml

3. Create a file named **AddODB.txt** as follows:

    a. Start Notepad, and then paste the following text into a new file:

    ```XML
        <Configuration>
          <Add SourcePath="http://officecdn.microsoft.com/pr/492350f6-3a01-4f97-b9c0-c7c6ddf67d60/" OfficeClientEdition="32" >
            <Product ID="O365BusinessRetail">
              <Language ID="en-us" />
              <ExcludeApp ID="Access" />
              <ExcludeApp ID="Excel" />
              <ExcludeApp ID="Lync" />
              <ExcludeApp ID="OneNote" />
              <ExcludeApp ID="Outlook" />
              <ExcludeApp ID="PowerPoint" />
              <ExcludeApp ID="Publisher" />
              <ExcludeApp ID="Word" />
            </Product>
          </Add>
          <Display Level="None" AcceptEULA="TRUE" />
        </Configuration>
    ```

   > [!NOTE]
   > This file will install the 32-bit US English edition of OneDrive. To install the 64-bit edition, change the value of OfficeClientEdition to 64. To install OneDrive in a different language, change the Language ID to a different language tag (ll-CC) by referring to the list of [Language identifiers](/DeployOffice/office2016/language-identifiers-and-optionstate-id-values-in-office-2016).

    b. Save the file to your desktop, and name it **AddODB**.

4. Open a command prompt as an administrator as follows:

    a. Select **Start**.

    b. In the **Start Search** box, enter **cmd**, and then press Ctrl+Shift+Enter.

    c. If the **User Account Control** dialog box appears, confirm that the action displayed is what you want, and then select **Continue**.

5. At the command prompt, navigate to the folder into which you extracted the Office Deployment tool.

    ```DOS
    cd /d %userprofile%\desktop
    ```
    
6. Run the following command.

    ```DOS
    setup.exe /configure AddODB.txt
    ```
   
    > [!NOTE]
   > The installation occurs silently in the background and can take 20 minutes or more to complete, depending on the speed of your Internet connection. Don't close the Command Prompt window during the installation. When the installation is completed, a new command line appears at the command prompt.

7. Select **Start**. In the **Start Search** box, type **OneDrive**, and then start OneDrive.

    > [!NOTE]
    > After you set up OneDrive, you might not see sync icons on files until you restart your computer.

8. Close the command prompt. You can now safely delete the following files from your desktop:

    - OfficeDeploymentTool.exe
    - Setup.exe
    - Configuration.xml
    - AddODB.txt

## Install Groove.exe with Office 2013

To install the previous OneDrive for Business sync app with Office 2013, follow these steps.

   > [!NOTE]
   > If you have Office Professional Plus 2013, Office 365 Enterprise E3, Office 365 Midsize Business, or Office 365 Small Business Premium, then you already have the OneDrive sync app installed.

1. Uninstall any earlier versions of the previous OneDrive for Business sync app.

2. Select one of the installer links below to download the installer for your language and system edition. If the 32-bit or 64-bit edition of Office is already installed, you must select the same edition for OneDrive.

|Language  |32-bit download link  |64-bit download link  |
|---------|---------|---------|
|Arabic             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ar-sa&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Bulgarian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=bg-bg&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=bg-bg&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Chinese (Simplified)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=zh-cn&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=zh-cn&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Chinese (Traditional)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=zh-tw&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=zh-tw&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Croatian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hr-hr&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hr-hr&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Czech             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=cs-cz&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=cs-cz&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Danish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=da-dk&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=da-dk&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Dutch            |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=nl-nl&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=nl-nl&amp;platform=]x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|English             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=en-us&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=en-us&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Estonian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=et-ee&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=et-ee&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Finnish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=fi-fi&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=fi-fi&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|French             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=fr-fr&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=fr-fr&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|German             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=de-de&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=de-de&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Greek             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=el-gr&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=el-gr&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Hebrew             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=he-il&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=he-il&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Hindi             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hi-in&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hi-in&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Hungarian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hu-hu&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=hu-hu&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Indonesian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=id-id&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=id-id&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Italian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=it-it&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=it-it&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Japanese             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ja-jp&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ja-jp&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Kazakh             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=kk-kz&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=kk-kz&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15g) |
|Korean             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ko-kr&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ko-kr&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Latvian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=lv-lv&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=lv-lv&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Lithuanian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=lt-lt&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=lt-lt&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Malay(Malaysia)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ms-my&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ms-my&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Norwegian(Bokmal)            |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=nb-no&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=nb-no&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Polish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pl-pl&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pl-pl&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Portuguese(Brazil)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pt-br&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pt-br&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Portuguese(Portugal)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pt-pt&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=pt-pt&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Romanian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ro-ro&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ro-ro&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Russian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ru-ru&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15gaa)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=ru-ru&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Serbian(Latin)             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sr-latn-cs&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sr-latn-cs&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Slovak             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sk-sk&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sk-sk&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Slovenian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sl-si&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sl-si&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Spanish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=es-es&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=es-es&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Swedish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sv-se&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15gaga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=sv-se&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Thai             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=th-th&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=th-th&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Turkish             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=tr-tr&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=tr-tr&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Ukrainian             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=uk-ua&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=uk-ua&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |
|Vietnamese             |[OneDrive for Business [32-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=vi-vn&amp;platform=x86&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga)  |[OneDrive for Business [64-bit]](https://c2rsetup.officeapps.live.com/c2r/download.aspx?productreleaseid=grooveretail&amp;language=vi-vn&amp;platform=x64&amp;token=3v9n8-w93cc-fqpb8-y9wvf-tvgj3&amp;taxregion=pr&amp;source=olsfcrequest&amp;version=o15ga) |

3. Run the downloaded file to start the Setup program.

4. Follow the instructions to complete the installation.

5. If you are asked to provide a license key, enter **3V9N8-W93CC-FQPB8-Y9WVF-TVGJ3**.

    > [!NOTE]
    > The OneDrive sync app ships together with two components that are not selected for installation by default. We recommend that you do not change these default settings.
