---
title: Create and deploy a thesaurus in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: 44640e29-bd9c-4b6a-94e1-8d5d30e7fdd2
---


# Create and deploy a thesaurus in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-18* **Summary:** Learn how to create and deploy a thesaurus to expand queries with synonyms.Use a thesaurus file to specify synonyms for a single word or multiple words that occur in queries. The query is expanded based on the entries in the thesaurus. You create and maintain the thesaurus file in a system external to SharePoint Server before you import it into SharePoint Server to make the synonyms available to the search system.
> [!NOTE:]

  
    
    

In this article:
-  [Before you begin](#begin)
    
  
-  [Create a thesaurus](#proc1)
    
  
-  [Deploy a thesaurus](#proc2)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following information about prerequisites:
- Create a Search service application 
    
  

## Create a thesaurus
<a name="proc1"> </a>

To define the entries in your thesaurus, you enter terms and their corresponding synonyms in a comma separated (.csv) file. Optionally, you can also specify in which language the query should be written for a synonym to apply. If you want to define more than one synonym for one key, you have to create multiple entries in the thesaurus. Also, if you want the synonym to work both ways, for example, if you want the term "IE" to also return search results for "Internet Explorer" and you want the term "Internet Explorer" to also return results for "IE", you have to create two thesaurus entries. To create your thesaurus terms, you can use alphabetical Unicode characters such as a, ø, ü or é. Your terms can also include underscores (_), hyphens (-) and straight apostrophes (‘). Your terms can’t include non-alphabetical Unicode characters, such as hashtag (#), forward slash (/), back slash (\\) , punctuation (.) or question mark (?). You also can’t use abbreviations that include non-alphabetical Unicode characters, such as E.K.G or d\\r. The matching between the thesaurus keys and query terms is not case sensitive. When a query term matches a thesaurus key, the query is expanded with the synonym(s) for that key and the search results will contain results for the original query term as well as for the synonym. **To create a thesaurus**
1. Create a .csv file with the columns **Key**, **Synonym** and **Language**. Make sure you use a comma as the column separator. If the file contains non-ASCII characters such as diacritics, you must encode it in UTF-8. Save the file to a location that is accessible from the server from which you will run the Microsoft PowerShell cmdlet to deploy the thesaurus.
    
1. In the **Key** column, enter the term (single or multiple words) that you want to trigger a synonym for when the term occurs in a query. Make sure there are no leading or trailing spaces around the terms.
    
  
2. In the **Synonym** column, enter the synonym (single or multiple words) that you want to add to the query if the term specified in the **Key** column occurs in a query. Synonyms consisting of multiple words will be added as phrases to the query.
    
  
3. In the optional **Language** column, enter the abbreviation for the language for which the synonym should apply. See the table in [Linguistic search features in SharePoint Server](html/linguistic-search-features-in-sharepoint-server.md) for an overview of available languages and their code. If you leave this column empty, the query is expanded with the synonym regardless of the query language. Make sure there are no leading or trailing spaces around the language codes.
    
  
A thesaurus is commonly used to expand acronyms. But you can also use a thesaurus to automatically include variations of a search term into the query for specific terminology used in your organization. An example thesaurus file input could look like this: Key,Synonym,Language IE,Internet Explorer Internet Explorer,IE UN,United Nations,en UN,Vereinte Nationen,de BAM,billing and account management billing and account management,billing and accounts
## Deploy a thesaurus
<a name="proc2"> </a>

You create and maintain the thesaurus file in a file external to SharePoint Server before you import it into SharePoint Server to make the synonyms available to the search system. You can’t export a thesaurus from SharePoint Server. If you want to make changes to your synonyms, you have to update the thesaurus file and then redeploy it. 
> [!NOTE:]

  
    
    

 **To import a thesaurus file**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. Start the SharePoint 2016 Management Shell.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, and then click **SharePoint 2016 Management Shell**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, click **SharePoint 2016 Management Shell**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, and then click **SharePoint 2016 Management Shell**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://technet.microsoft.com/en-us/library/hh831491.aspx).
    
  
3. At the Windows PowerShell command prompt, type the following command:
    
  ```
  
$searchApp = Get-SPEnterpriseSearchServiceApplication
Import-SPEnterpriseSearchThesaurus -SearchApplication $searchApp -Filename <Path>

  ```


    Where:
    
  -  *<Path>*  specifies the full UNC path of the .csv file (the thesaurus) to be imported.
    
  

# See also

#### 

 [Linguistic search features in SharePoint Server](html/linguistic-search-features-in-sharepoint-server.md)
  
    
    

#### 

 **Import-SPEnterpriseSearchThesaurus**
  
    
    

  
    
    

