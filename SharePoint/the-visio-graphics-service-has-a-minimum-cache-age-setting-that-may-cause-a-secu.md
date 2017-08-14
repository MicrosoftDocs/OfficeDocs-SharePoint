---
title: The Visio Graphics Service has a minimum cache age setting that may cause a security issue ((SharePoint Server 2016)
ms.prod: SHAREPOINT
ms.assetid: 4fcd074b-32b1-49b3-9910-5bb174894603
---


# The Visio Graphics Service has a minimum cache age setting that may cause a security issue ((SharePoint Server 2016)
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2016*  * **Topic Last Modified:** 2017-05-30* **Summary:** Learn how to resolve the SharePoint Health Analyzer rule "The Visio Graphics Service has a minimum cache age setting that may cause a security issue" for SharePoint Server 2016. **Rule Name:**    The Visio Graphics Service has a minimum cache age setting that may cause a security issue **Summary:**    Setting **Minimum Cache Age** to 0 minutes may leave the Visio Graphics Service open to a denial of service (DoS) attack. A value of 0 for this setting might lead to large processor and network load of the Visio Graphics Service and SharePoint Server 2016, decreasing the expected performance of both. However, increasing this value means that users will not see their data-connected diagrams refreshing as frequently. **Cause:**    The **Minimum Cache Age** setting was set to 0 minutes. **Resolution:   Increase the value of the Minimum Cache Age setting**
1. Verify that the user account that is performing this procedure is an administrator of the Visio Graphics Service service application.
    
  
2. In Central Administration, on the Home page, in the **Application Management** section, click **Manage service applications**.
    
  
3. On the Service Applications page, click the Visio Graphics service application.
    
  
4. On the Manage the Visio Graphics Service page, click **Global Settings**.
    
  
5. Ensure that the settings have the values that are listed in the following table. If they do not, type the value in the corresponding text box.
    
### 

Setting Value **Maximum Web Drawing Size** <br/> <= 25 (Megabytes)  <br/> **Minimum Cache Age** <br/> >= 5 (Minutes)  <br/> **Maximum Cache Age** <br/> <= 60 (Minutes)  <br/> **Maximum Recalc Duration** <br/> <= 60 (Seconds)  <br/> **Maximum Cache Size** <br/> >= 5120 (Megabytes)  <br/> 6. Click **OK**.
    
  

