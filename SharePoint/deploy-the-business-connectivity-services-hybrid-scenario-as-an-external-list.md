---
title: Deploy the Business Connectivity Services hybrid scenario as an external list
ms.prod: SHAREPOINT
ms.assetid: d7173fc7-65cd-4201-8095-7ad805f50c95
---


# Deploy the Business Connectivity Services hybrid scenario as an external list
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-06-22* **Summary:** Learn how to manually extract a Business Data Connectivity model, import the model into SharePoint Online, and manually create an external list to surface the on-premises data.The procedures in this article show you how to integrate external data by using an external list. Make sure you've already  [prepared your environment for the Business Connectivity Services hybrid scenario](html/prepare-your-environment-for-the-business-connectivity-services-hybrid-scenario.md) before you follow the procedures in this article.
## Manually extract an external content type to a BDCM file

The external content type that you configured must be manually extracted and saved as a file with a  *.bcdm*  extension. This is done by using Visual Studio 2012. Follow the procedure in [How to: Convert an App-Scoped External Content Type to Tenant-Scoped](https://go.microsoft.com/fwlink/?LinkId=290983) in the MSDN Library.You'll need the .bcdm file for the next procedure.
## Import the BDCM file into the SharePoint Online BDC Metadata Store

When you import the BDC Model file into SharePoint Online, you must be logged in to the SharePoint Online administrator site as a federated account (an account imported to Office 365 from On-Premise using Directory Sync). This federated account should also be given Global Administrator rights in Office 365. When importing the BDC Model to configure Hybrid BCS, certain calls are made to SharePoint Server that will require you use a federated user account. Be aware the account must also have a populated user profile in SharePoint Server. **To import a BDCM file into the SharePoint Online BDC Metadata Store**
1. Log on to your SharePoint Online tenancy by using an administrative account, and then open the SharePoint Online Administration Center.
    
  
2. In the Quick Launch, click **bcs**.
    
  
3. Under **business connectivity services**, click **Manage BDC Models and External Content Types**.
    
  
4. On the **Edit** tab, click **Import**.
    
  
5. Click **Browse**, and then browse to the .bdcm file that you exported.
    
  
6. Leave the default selections for **File Type** and **Advanced Settings**, and then click **Import**. During the import, BCS validates the XML in the model, queries the connection settings object, and connects to the on-premises OData source.
    
  
When you import a BDCM model into the BDC metadata service, you are creating an external content type. This external content type is available for tenant-wide use.
## Create an external list for the BCS hybrid scenario

The next step is to create the external list. **To create an external list for the BCS hybrid scenario**
1. Open the site that you prepared by using an account that has site owner permissions and is a federated account.
    
  
2. On the Quick Launch, click **Site Contents**, and then click **add an app**.
    
  
3. Click **External List**, and then provide a name for the list.
    
  
4. Click the **Select External Content Type** link next to the **External Content Type** box.
    
  
5. Select the external content type that you created, click **OK**, and then click **Create**.
    
  
6. Open the external list and confirm that your external data is displayed.
    
  
Once the list is created,  [validate the scenario](html/validate-the-business-connectivity-services-hybrid-scenario.md).
# See also

#### 

 [Deploy a Business Connectivity Services hybrid solution in SharePoint](html/deploy-a-business-connectivity-services-hybrid-solution-in-sharepoint.md)
  
    
    

  
    
    

