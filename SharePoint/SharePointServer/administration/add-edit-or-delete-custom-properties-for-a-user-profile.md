---
title: "Add, edit, or delete custom properties in SharePoint Server user profiles"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 3cfb2148-9d1a-4022-a55a-a6d2963bef0e
description: "Learn how to create, edit, and delete user profile properties in SharePoint Server."
---

# Add, edit, or delete custom properties in SharePoint Server user profiles

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
The **Manage Profile Service** page of a User Profile service application in SharePoint Server is a central location for managing available user profile properties and creating new properties. You need to be a member of the Farm Administrators SharePoint group or a Service Application Administrator for the User Profile service application to make changes. 
  
You can supplement default user profile properties with additional properties to track key information that is not otherwise available. Key business needs might encourage you to create new properties that associate users with important business processes. For example, a sales department can create a specific sales role property to share with a particular audience or audiences. Custom user profile properties can be edited to better suit business needs or they can be deleted when no longer needed.
  
    
## Add a user profile property
<a name="create"> </a>

Perform the following procedure to create a user profile property.
  
 **To create a new user profile property**
  
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link for the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.
    
4. On the **Manage User Profile Properties** page, click **New Property**.
    
5. On the **Add User Profile Property** page, in the **Property Settings** section, in the **Name** text box, type a name to be used by the User Profile service application for the user profile property. 
    
6. In the **Property Settings** section, in the **Display Name** box, type the user profile property name that will be displayed to all users. 
    
    > [!NOTE]
    > If you use multiple languages in your deployment, you can provide alternative display names for each language by clicking **Edit Languages**. In the dialog box, click **Add Language**, select a language from the menu, and then type the display name in the new language. You can add display names for any of the available languages. The display name that appears depends on the language of the operating system on the computer of the user who views the property. 
  
7. On the **Type** drop-down list, click the data type for the property. 
    
    > [!NOTE]
    > If you select **string (Multi Value)**, the property will be permanently set as a multivalued property. You cannot change this setting after you click **OK**. You can only delete the property and add it again as a new single value property. 
  
8. In the **Length** box, type the maximum number of characters that are allowed for values for this property. 
    
9. Click to select **Configure a Term Set to be used for this property** to associate the profile property with a managed metadata term set and select a term set from the drop-down list. 
    
10. In the **Sub-type of Profile** section, select the **Default User Profile Subtype** to associate the default user profile subtype with this user profile property. 
    
11. In the **User Description** section, in the **Description** box, type the instructions or information that is displayed to users about this user profile property. 
    
    > [!NOTE]
    > If you use multiple languages in your deployment, you can provide alternative display names for each language by clicking **Edit Languages**. In the dialog box, click **Add Language**, select a language from the menu, and then type the display name in the new language. You can add display names for any of the available languages. The display name that appears depends on the language of the operating system on the computer of the user who views the property. 
  
12. In the **Policy Settings** section, select the policy setting and default privacy setting that you want for this property. Click to select **User can override box** to enable users to override these settings. 
    
13. In the **Edit Settings** section, select whether users can edit values for this property. 
    
14. In the **Display Settings** section, specify if and how the property will be viewed by users. 
    
15. In the **Search Settings** section, select the **Alias** check box, the **Indexed** check box, or both, depending on the kinds of searches that you want to be associated with this user profile property. 
    
    > [!NOTE]
    > The **Alias** check box is unavailable unless the **Default Privacy Setting** is set to "Everyone". 
  
    > [!NOTE]
    > If you mark a property as indexed, a search for values of that property returns that user profile. For example, if the  _telephone number_ property is indexed, a search of telephone numbers finds the employee with that number. If you mark a property as aliased, the property is a suitable alias for this user. For example, if you search for all documents by John Kane, the result returns documents that were written by johnkane@contoso.com and Jonathan Kane if profile properties are marked with those values as aliases. 
  
16. In the **Property Mapping for Synchronization** section, click **Remove** to delete or change an existing mapping. 
    
17. In the **Add new Mapping** section, specify the source data connection, attribute, and synchronization direction for the mapping. When you are finished, click **Add**.
    
18. Click **OK**.
    
## Edit a user profile property
<a name="edit"> </a>

Perform the following procedure to edit a user profile property.
  
 **To edit a user profile property**
  
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link for the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.
    
4. On the **Manage User Profile Properties** page, in the **Property Name** column, select the user profile property that you want to change, and then, in the dropdown menu, click **Edit**.
    
5. On the **Edit User Profile Property** page, locate the element or elements of the user profile property that you want to change and edit them. 
    
6. When you are finished, click **OK**.
    
## Delete a user profile property
<a name="delete"> </a>

Perform the following procedure to delete a user profile property.
  
 **To delete a user profile property profile property by using Central Administration**
  
1. On Central Administration, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.
    
3. On the **Manage User Profile Properties** page, in the **Property Name** column, select the user profile property that you want to remove, and then, in the dropdown menu, click **Delete**.
    
4. In the dialog box, verify that you have selected the correct user profile property, and then click **OK**.
    
## See also
<a name="delete"> </a>

#### Concepts

[Administer the User Profile service in SharePoint Server](user-profile-service-administration.md)
  
[Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md)
  
[User Profile service overview](../install/user-profile-service-overview.md)
#### Other Resources

[Delegate administration of User Profile service applications or features in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee721057(v=office.14))

