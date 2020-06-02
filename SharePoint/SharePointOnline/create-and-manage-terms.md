---
title: "Create and manage terms in a term set"
ms.reviewer: vrchowdh
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 5/28/2020
audience: End User
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- M365-collaboration
search.appverid:
- SPO160
- MET150
ms.assetid: 549070a7-41c2-4210-9e9c-5fad22bd8748
description: "Learn how to use the SharePoint Term Store Management Tool to create and edit terms in a term store for managed metadata."
---

# Create and manage terms in a term set

You can use the Term Store Management Tool to create terms in a term set, or manage a term such as copy it or move it. If you have many terms that you want to add, it might be more practical to import all the terms in the term set instead of adding the terms individually. For info about how to import terms, see [Import term sets](https://support.office.com/article/168fbc86-7fce-4288-9a1f-b83fc3921c18). 
  
> [!IMPORTANT]
>  To create and manage terms in the Term Store Management Tool, you must be a Contributor, a Group Manager, or a Term Store admin. 
  
![You can select a group name in the Term Store Management Tool to open a menu that lets you add terms to a term set](media/create-manage-term-sets.png)
  
To create a term in a term set, follow these steps.
  
> [!NOTE]
>  If you are adding a term to a local term set, you must start this procedure from the site to which the term set belongs. If you are updating a global term set, you can open the Term Store Management Tool from any site. 
  
1. Open the Term Store Management Tool. To learn how, see [Open the Term Store Management Tool](open-term-store-management-tool.md).
    
2. In the tree-view pane, expand the groups to find the term set to which you want to add a term.
    
3. Point to the term set where you want to add a term, select the **More options** (vertical ellipsis icon), and then select **Add term**.
    
4. In the tree view, enter the name that you want to use as the default label for the newly created term.
    
5. To edit the term **name** panel, specify the following info about the new term: 
    
    - Under the **General** tab, to add languages, translations, and synonyms, select **Add**. The **Add translation and synonyms** panel appears. Select your language, translation, description, and add synonyms. Select **Save**.

    - Under the **Usage settings** tab, to make the term available to the users and content editors of sites consuming this term set, select **Edit**. The **Available for tagging** panel appears. By default, the term is enabled for tagging. To disable, select the **Enable** checkbox. Select **Save**.

    - Under the **Advanced** tab, to use shared or local custom properties to store additional data about a term sets, select **Edit**. The **Edit shared custom properties** panel appears. Add property names and values. Select **Save**. 

  
## Take another action with terms
<a name="__toc327965090"> </a>

There are several actions that you can take on terms that will help you build and manage term sets as the business needs of your organization evolve. 
  
To take any of the following actions, first [Open the Term Store Management Tool](open-term-store-management-tool.md), and then point to the term that you want to use for the action.
  
### Rename term
<a name="__rename_the_term"> </a>

- Select **Rename term**. This action renames the \<original term name\>. 
    
    
### Copy term
<a name="__copy_the_term"> </a>

- Select **Copy term**. This action shows the name of the new term as **Copy of \<original term name\>**. No child terms for the source term are copied. 
    
### Move term
<a name="__move_a_term"> </a>

1. Select **Move term**. The **Move to** panel appears.
    
2. Select the target term set or term. 
    
3. Select **Move**.
    
### Delete term
<a name="__delete_a_term"> </a>

1. Select **Delete term**. A warning dialog box appears stating *If you delete this term, any terms below it will also be deleted. Terms that are shared with other term sets will be placed in the Orphaned terms term set under System*. 
    
2. Select **Delete**.
    
### Pin term
<a name="__pin_term_to"> </a>

1. Select **Pin term**. The **Pin term to** panel appears.

2. Select the target term set or term where you want to pin the term. 
    
3. Select **Pin**.

Pinning a term makes linked copies of the term and its children available at the destination. You can only create or edit the children of a pinned term at the source and the changes will reflect everywhere the term is used.
    
### Reuse term
<a name="__reuse_a_term"> </a>

1. Select **Reuse term**. The **Reuse term to** panel appears.
    
2. Select the target term set or term where you want to reuse the term. 
    
3. Select the term, and then select **Reuse**.

Reusing a term makes linked copies of the term and its children available at the destination. You can create children for a reused term anywhere it is used but will exist only in the term set they were created.
    

### Merge term
<a name="__merge_a_term"> </a>

1. Select **Merge term**. The **Merge to** panel appears.
    
2. Select the target term set or term where you want to merge the term. 
    
3. Select **Merge**.

Merging this term with another will collapse its synonyms, translations and custom properties into the other term.
    
### Deprecate term
<a name="__deprecate_a_term"> </a>

- Select **Deprecate term**. This action makes any instances of this term in any term set to which it belongs unavailable for tagging. Child terms of the term are not deprecated. 
