# Knowledge check questions

## Which of the following scenarios is a common use case for a version control system? 

1. Deleting earlier versions of a project or file, so you know you are working only with the most current file or data.
2. **Making experimental changes to your project in an isolated branch.**
3. Gathering feature requirements for a large project and communicating them to stakeholders.

## What is another name for a version control system? 

1. Version management software (VMS)
2. Software control management (SCM) system
3. **Software configuration management (SCM) system**

## What’s the difference between Git and GitHub? 

1. **Git lets you work with one or more local branches and push changes to a remote repository. GitHub acts as the remote repository, which is accessed through a website or command-line tools.**
2. Git is a distributed version control system (DVCS) that runs in the cloud. GitHub is an interface layer that provides access to Git technology.
3. Git is used by an individual contributor. GitHub is used by multiple contributors to simplify group development work.

## What Git command gives information about how to use Git? 

1. git init
2. git status
3. **git help**

## What's the difference between GitHub organization accounts and GitHub personal/user accounts? 

1. **Organizational accounts are shared accounts, while personal/user accounts are for individuals.**
2. You pay more for organization accounts versus personal/user accounts.
3. They're exactly the same.
4. Personal/user accounts have more access than organization accounts.

## What's the best reason to decide to upgrade to the GitHub Enterprise product? 

1. Because you want to use GitHub Actions and Codespaces.
2. Because your VP needs to use GitHub Insights.
3. **Because you want to centrally manage users and repositories across multiple organizations.**
4. Because you want to use the team pull request reviewers feature.

##What's the purpose of a team? 
1. A team allows you to manage an organization account.
2. A team allows you to control permission levels for an enterprise.
3. A team allows a single user to sign in using different accounts credentials.
4. **A team is intended to reflect a company or group's structure. It's used to provide cascading access permissions and make it easy to notify all team members via mentions.**

## What's a function you can execute on GitHub Mobile? 

1. Check out branches with pull requests and view CI statuses.
2. Compare changed image.s
3. Add and clone repositories.
4. ** Manage, triage, and clear notifications from github.com.**

## What is GitHub Copilot? 

1. **GitHub Copilot is an AI pair programmer that you can use to get code suggestions.**
2. GitHub Copilot is OpenAI Codex, a new AI system that OpenAI created.
3. GitHub Copilot is a JavaScript public repository and is one of the best-supported languages.
4. GitHub Copilot can write a comment that describes logic, and you can add your suggested code to implement the solution.

## What are the supported IDE extensions for GitHub Copilot? 

1. VS Code and Visual Studio
2. GitHub.com, VS Code, Visual Studio, Neovim, and JetBrains
3. **VS Code, Visual Studio, Neovim, and JetBrains**
   Although GitHub.com is supported, it doesn't need an extension.

## What is the difference between GitHub Copilot Business and GitHub Copilot Enterprise? 

1. GitHub Copilot Enterprise has code completions, whereas GitHub Copilot Business doesn't.
2. GitHub Copilot Enterprise has chat in IDE and mobile, whereas GitHub Copilot Business doesn't.
3. **GitHub Copilot Enterprise has an extra layer of personalization. Organizations use their own codebase to train GitHub Copilot.**
4. GitHub Copilot Enterprise has an extra layer of security, with IP indemnity and enterprise-grade security, safety, and privacy.

## Which directory is the clone placed in after creating a Codespace? 

**/workspaces directory**

/temp directory

~/.bashrc directory

Linux directory

## What's the maximum number of Codespaces that you can create per repository or branch? 

You can only create two Codespaces.

You can create a total of 10 Codespaces.

You can create a total of 30 Codespaces.

**You can create an unlimited number of Codespaces per repository or branch, depending upon available space. When you reach an upper amount of resources, a message displays that an existing Codespace needs to removed/deleted before a new Codespace can be created.**

## What happens when Codespace loses internet connectivity? 

**If the connection to the internet is lost while working in a Codespace, you aren't able to access your Codespace.**

Codespace doesn't require an internet connection. I can access my Codespace regardless if I lose connectivity.

If you lose internet connection while working on your Codespace, your changes aren't saved.

## What defines the beginning of a Codespace's lifecycle? 

**A Codespace's lifecycle begins when you create a Codespace and ends when you delete it.**

A Codespace's lifecycle begins immediately when GitHub is opened and ends when the software is closed.

A Codespace's lifecycle begins when a repository is created and ends when you delete it.

## What Project descriptor automatically saves when you change it? 

**Project name**

Project description

Project README

## What does an iteration field help you do in Projects? 

Allows you to keep track of the various changes made to an issue or pull request.

Allows you to reverse the changes you made to your Project.

**Allows you to create sequential phases of your project and group issues and pull requests based on the phase.**

***An iteration field helps you and your team organize your Project into different phases. The value of the field allows you to prioritize what comes first. Setting priorities allows you to implement timelines to keep you on track and accomplish your goals.***

## What field can you use in order to make a Priority grouping like High, Medium, and Low in your Project? 

Date

**Single select**
***The Single select field allows you to create multiple groups like Priority grouping in order to help you organize and prioritize your Project.***

Iteration field

## What is the easiest way to add automation to your Project? 

GraphQL API

**Built-in Automation**
***Built-in automation built within Projects allows you a simple way to automate your Project.***

GitHub Actions

## What is the name of the section where you can change the visibility of your Project, close your Project, or delete your Project? 

Red zone

Visibility and Access

**Danger zone**

## Which of the following Markdown snippets produces the text Hello, world! in bold italics? 

\*Hello, \*world\*!\*

\*\*Hello, \*world\*!\*\*

\*\*\*Hello, world!\*\*\*

***Hello, world!***
**bold** is produced with two asterix on either side of the word and *italics* with one on each side. You can also use underscores (_) instead of asterisks if you prefer.

\#\#\# Hello, world!

## How do you print certain characters, like asterisks (*) and underscores (_), literally on your output? 

Use three in a row, like *** or ___.

**Escape them with a backslash, like \* or \_.**
You can also escape other reserved characters, including { and #, using backslashes.

Unfortunately, this isn't supported at this time.

## Suppose there's an HTML snippet that you want to include on your GitHub Pages web site, but Markdown doesn't offer a way to render it. What should you do? 

**Just add the HTML inline.**
Markdown isn't a complete replacement for HTML. You might need to add HTML to get the final results you're looking for.

Cut the content. If it's not supported in Markdown, then it's probably not worth including.

Open an issue that requests Markdown support for your specialized scenario.

## You want to grant a user the permissions required to add and remove organization members to and from a team. Which permission would you need to grant that user? 

The admin permission on a repository

The maintain permission on a repository

Organization billing manager

**Team maintainer**
As a team maintainer, the user can add and remove organization members to and from a team.

## As an organization owner, you want to ensure that everyone who is signed in to your corporate network can access the GitHub website without requiring a second sign-in. Which technology would you enable to accomplish this? 

**Single sign-on**
Single sign-on is the right technology to allow network users to access the GitHub website without extra sign-ins.

Two-factor authentication

Personal Access Tokens

SSH keys

## What's the appropriate repository permission level for contributors who need to actively push changes to your repository? 

Admin

**Write**
The write permission is the appropriate permission level.

Triage

Maintain

## What is not a good reason to create a pull request? 

You would like to receive feedback on prospective changes before merging your feature branch into main.

You want to merge your bug fix branch into main, but don't have permission.

**Your branch can't be merged into main due to upstream changes made since you created it. Creating a pull request lets the other contributor know they need to pull their changes out so you can put yours in.**
Pull requests don't work this way. Also, the etiquette is for you to be sure your branch can be cleanly merged into the base before creating a pull request.


## How can you ensure that pull requests for a given area of the repository, aren't merged unless certain users or teams approve? 

Clearly explain the pull request policy in CONTRIBUTING.md.

**Use a CODEOWNERS file and enable required reviews.**
A CODEOWNERS file enables you to assign users or teams as required reviewers using the same syntax as .gitignore files.


Add a table that maps directory paths to required users in SECURITY.md.

## You're requested to review a pull request. As you read through it, you notice several minor coding errors and typos. How should you handle the review? 

**Start a review and fix obvious typos inline. Add comments in places that require further discussion or offer educational value. Complete the review with changes requested.**
Contributors always appreciate when reviewers show an interest in getting their code merged.

Leave single comments for each issue you come across, but don't change the code. For typos, include the correct spelling of the word as a reference. Approve the pull request if you trust the author to implement your suggestions.

Reject the pull request. We can't risk any bugs accidentally being merged into an important branch.

## How does GitHub's top-level search bar differ from the search options available on repository tabs? 

Other than being located in different parts of the user interface, they are otherwise the same.

They support different filter syntax options.

**The top-level search bar supports searching everything across all of GitHub, whereas the repository tab searches are scoped to cover specific types in the current repository.**
The top-level search allows the most flexibility, whereas the scoped tab searches provide popular filter dropdowns for easier refinement.

## What does git blame do? 

It creates a bug assigned to the last person who committed changes to the specified file.

**It displays the commit history of the file.**
Despite the accusatory name, git blame is just a command to display commit history.

It reverts the effects of a git praise command.

## Suppose a bug issue is reported on your project, and you know which pull request introduced the problem. Which of the following options is not a cross-linking best practice? 

**Do not create cross-links when the root cause of the issue is already known.**
It's a good practice to always add cross-links in case you or someone else needs the context later on.

Add a comment to the bug report that includes the pull request's author by using an @mention.

Add a comment to the bug report that links the pull request to it using the #ID syntax.

## How does GitHub Copilot work? 

**GitHub Copilot uses prompts and natural language text that you type to provide coding suggestions.**
GitHub Copilot is trained on billions of lines of code. It turns natural language prompts into coding suggestions across dozens of languages.

GitHub Copilot uses lights, that you type, and it provides suggestions based on what you type.

GitHub Copilot uses radio language, that you type, and it provides suggestions based on what you type.

## What are some GitHub Copilot Free features? 

It's a free unrestrticted AI tool that works independent of code editors.

**It provides several suggestions and chats per month directly in your IDE and on github.com.**
 It also supports multi-file editing and and switching models!

An option to enable slower responses, preservering your Copilot Pro quota.

## How can you accept GitHub Copilot's suggestions? 

**Press the Tab key.**
Copilot offers you a suggestion, which appears as grey code if you use black as your text color. To accept the suggestion, you need to press the Tab key.

Press the F1 key.

Press the F4 key.

## Identify which statement is valid and select the correct answer: 

A prompt, which is our output, is a collection of songs that tells our copilot what to generate.

**A prompt, which is our input, is a collection of instructions or guidelines that tell our copilot what to generate.**
A prompt is crucial in eliciting specific responses from Copilot. The prompt might be a comment that steers Copilot to generate code on your behalf or writing code that Copilot autocompletes.

A prompt, which is our document, is a collection of laptops that tells our Copilot what to generate.

## What does the quality of the output from GitHub Copilot depend on? 

Your code editor.

How well your extensions were installed.

**How well you crafted your prompt.**
Designing an effective prompt is, therefore, crucial in ensuring we achieve our desired outcomes. You need to detail your prompt as much as possible.

## GitHub Action workflows are triggered by events. Which of these are valid events that GitHub Actions support? (Choose two.)

A new member has been added to the repository

A change is made to the repository settings

A new vulnerability has been detected in a dependency

**A commit is pushed to a branch**

**A pull request is opened**

[💡Hint](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#about-events-that-trigger-workflows)

## What are the possible statuses for a pull request review? (Choose three.)

**Approve**

Close

**Comment**

**Request Changes**

Deny

Applaud

[💡Hint](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews#about-pull-request-reviews)

## What are the different available options for adding issues and pull requests to a GitHub Project board?

**Individually, automatically, or in bulk.**

Only individually or in bulk

Only manually, one at a time.

Only automatically using project workflows

[💡Hint](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#adding-issues-and-pull-requests-to-a-project)

## What feature is unique to GitHub Desktop compared to github.com?

View repository insights

**Visualize branch histories in a graphical interface**

Create new repositories

Clone repositories to local machine

[💡Hint](https://docs.github.com/en/desktop/making-changes-in-a-branch/viewing-the-branch-history-in-github-desktop)
[💡💡Hint2](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-the-activity-view-to-see-changes-to-a-repository)

GitHub Desktop provides a graphical interface for visualizing branch histories, which is unique compared to the website

## What is a repository in GitHub?

A repository in GitHub is a chat room where developers can discuss code-related issues.

**It's a place where you can store your code, your files, and each file's revision history.**

It's a place where you can store your Docker images or NPM packages.

It's a visual code editor that allows you to edit your source code in the browser.

[💡Hint](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)

## Which of the GitHub features best serves as a simple way to share small code snippets with others?

Issues

Projects

Wikis

**Gists**

[💡Hint](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)

## What is a GitHub Codespace deep link?

It's a link to the most recent GitHub Codespace that was created for the repository

It's a link between the GitHub Codespace and the repository which keeps the Codespace in sync with the changes in the repository

It's a link to the most recent GitHub Codespace that you have used in any repository

**It's a link that points to a specific GitHub.com Page that allows you to create a new GitHub Codespace and select specific configuration**

[💡Hint](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/setting-up-your-repository/facilitating-quick-creation-and-resumption-of-codespaces#configuring-more-options)

## Why would a repository owner want to use milestones? (Choose two.)

**To associate issues and pull requests with specific project phases**

To communicate that the repository is in a stable state

**To have an overview of how much work is left to complete a project phase**

To list the repository contributors

To track the repository dependencies

To bring automation to the repository

[💡Hint](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)

## What is CodeQL?

**A code analysis tool**

A programming language

A version control system

A text editor

[💡Hint](https://codeql.github.com/)

## What are the different forms of two-factor or multi-factor authentication supported by GitHub? (Choose five.)

Email

Phone call

**Passkey**

**Text message**

**Security key**

**Time-based one-time password (TOTP)**

**GitHub mobile**

[💡Hint](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/accessing-github-using-two-factor-authentication)

## What are some actions you can do in regards to Project Templates in your organization? (Choose three.)

Publish your templates in GitHub Marketplace for anyone to use

**Create a new template to be used as a base for new projects**

**With write permission, set an existing project as a template**

**With admin or write permissions, copy an existing project as a template**

Configure recommended templates to your organization's members

[💡Hint](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-your-project/managing-project-templates-in-your-organization)

## What is the role of an organization security manager?

Security managers are organization members who can manage the billing settings for your organization, such as payment information.

Security managers are organization members who have complete access to the organization.

**Security managers are organization members who can view security alerts and manage settings for code security across your organization, as well as read permissions for all repositories in the organization.**

Security managers are organization members who, in addition to their permissions as members, are allowed to block and unblock non-member contributors, set interaction limits, and hide comments in public repositories owned by the organization.

[💡Hint](https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/roles-in-an-organization)

Security manager: Grants the ability to manage security policies, security alerts, and security configurations for an organization and all its repositories.

## Which of these GitHub features serves the purpose of an adaptable spreadsheet, task board and a roadmap that integrates with issues and pull requests on GitHub to plan and track your work effectively?

**GitHub Project**

GitHub Copilot

GitHub Repository

GitHub Organization

## What is GitHub Desktop?

It's an online editor that allows you to work on your repository in the browser.

It's a GitHub pricing plan for personal accounts that offers additional features in addition to the free plan.

**It's a GUI Application for working with Git and GitHub on your computer.**

It's a self hosted version of GitHub that you can install on your own servers or personal computer.
[💡Hint](https://docs.github.com/en/desktop)

## What are the use cases for labels?

Assigning them to releases so that they are included in the release notes

**Categorizing issues and pull requests**

Assigning labels to repository contributors to indicate their role and permissions in the project

Categorizing files in the repository

[💡Hint](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)

## Where can you disable repository features such as issues, wikis or projects on a repository that you own?

In your account settings

These features cannot be disabled

In the .github/settings.yml configuration file

**In the repository settings**

[💡Hint](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository)

## What is a fork in GitHub?

A fork is a branch that is not up to date with the default branch of the repository.

A fork is the place where a branch splits off into at least two other branches.

**A fork is a personal copy of another user's repository that lives on your account.**

A fork is the state of a repository when it is not up to date with the remote repository.

[💡Hint](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks)

## Which information can be found in the Pulse section in the Insights tab of a repository? (Choose four)

List of unresolved conversations

**Summary of repository activity**

**Pull requests open/merged ratio**

**List of issue discussions**

Amount of code line additions and deletions

Amount of forks of the repo

[💡Hint](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity)

![pulse](https://github.com/codess-aus/GitHub-Foundations/blob/a0aa68ed03b2af986119ebffb216e4d6abd01889/images/pulse.jpg)

You can use Pulse to see an overview of a repository's pull request, issue, and commit activity. Pulse includes a list of open and merged pull requests, open and closed issues, and a graph showing the commit activity for the top 15 users who committed to the default branch of the project in the selected time period. If you want to see a detailed history of changes to a repository, you can use the activity view. The activity view displays all pushes, merges, force pushes, and branch changes, and associates these changes with commits and authenticated users.

## How can you start using GitHub Copilot after activating the GitHub Copilot subscription?

**Setup GitHub Copilot in one of the supported IDE's such as Visual Studio Code or JetBrains and start coding**

You need to edit the repository settings and enable GitHub Copilot for the repository

GitHub Copilot will automatically start giving suggestions on pull requests and issues in your repository

You need to setup a GitHub Action that will setup GitHub Copilot on your repository

[💡Hint](https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot)

## What is the effect of adding a line Closes #11 to the pull request's description?

That pull request will be automatically merged on the 11th of that month.

Once that pull request is merged, the #11th branch will be deleted automatically.

That pull request will be automatically merged once the issue #11 is closed.

Once that pull request is merged, the pull request #11 will be deleted automatically.

**Once that pull request is merged, the issue #11 will be closed automatically.**

[💡Hint](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests#linking-a-pull-request-to-an-issue)

## What is the name of GitHub's continuous integration and continuous delivery (CI/CD) platform?

GitHub Pipelines

GitHub Workflows

**GitHub Actions**

GitHub Projects

[💡Hint](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)

## You want to merge changes from branch feature-a into main and you are creating a pull request. Which branch should be the base branch and which branch should be the compare branch?

feature-a is the base branch and main is the compare branch.

**main is the base branch and feature-a is the compare branch.**

[💡Hint](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-comparing-branches-in-pull-requests)

When you want to merge changes from branch feature-a into main and you are creating a pull request, main should be the base branch and feature-a should be the compare branch.

This setup ensures that the changes from feature-a are compared against the main branch, and once the pull request is merged, the changes will be incorporated into the main branch.

## How can you enforce status checks passing before merging a pull request to the main branch?

By running tests locally prior to pushing to the remote repository

By using GitHub Actions

**By creating a branch protection rule**

By making the repository private

[💡Hint](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches#about-branch-protection-settings)

## Which of these is true regarding custom fields for items in GitHub Projects?

Custom fields are limited to predefined options and cannot include user-defined metadata.

**Custom fields enable the addition of metadata beyond the built-in options, such as target dates and iteration fields.**

Custom fields are limited to textual information and cannot include numeric or date-related metadata.

Custom fields are exclusively for aesthetic modifications and do not add any meaningful metadata.

[💡Hint](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects#adding-metadata-to-your-items)

## In GitHub a proposal to merge a set of changes from one branch into another branch is called a:

**Pull Request**

A merge branch

Issue

Gist

Commit

[💡Hint](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

## Can you change a gist from public to secret after creating it?

**No**

Yes

[💡Hint](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)

## Where can you find publicly available GitHub Actions?

GitHub Public Action Storage

GitHub Actions Project Boards

GitHub private repositories

**GitHub Marketplace**

[💡](https://docs.github.com/en/actions/creating-actions/publishing-actions-in-github-marketplace)

## What is one of the main benefits for using a Personal Access Token (PAT) instead of a standard username and password for GitHub authentication?

**PAT can be used for authentication to GitHub when using the GitHub API or the command line. Users generate a token via the GitHub's settings option, and tie the token permissions to a repository or organization.**

PAT lets you authenticate GitHub Enterprise Server against your existing accounts and centrally manage repository access.

PATs can be managed by the organization and enterprise.

PAT is an extra layer of security used when logging into websites or apps. With PAT, users have to sign in with their username and password and provide another form of authentication that only they have access to.

[💡](https://learn.microsoft.com/en-us/training/modules/github-introduction-administration/3-how-github-authentication-works)

## How does the synchronization between GitHub projects, issues and pull requests work?

Information synchronization only works in one direction - from issues and pull requests to projects. Updates to Project items won't be automatically mirrored in issues and pull requests.

Information synchronization only works in one direction - from project to issues and pull requests. Updates to issues and pull requests won't be automatically mirrored in GitHub Project items.

Updates to the issues and pull requests will not be automatically reflected in GitHub Projects, it has to be triggered manually by the user.

**Updates to the issues and pull requests will be automatically reflected in GitHub Projects. This integration works both ways, so that when you change information about a pull request or issue in your project, the pull request or issue reflects that information.**

[💡](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects#staying-up-to-date)

## Which of these layouts are available in GitHub Projects? (Choose three.)

**Roadmap layout**

Scrum layout

Project layout

**Table layout**

**Board layout**

Agile layout

[💡](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/changing-the-layout-of-a-view)

## Which of these workflows are built-in automations in GitHub Projects? (Choose two.)

**When issues or pull requests in your project are closed, their status is set to Done**

When a new contributor is added to a repository, the unassigned issues are assigned to him.

## What are the different options that allow you to automate operations in your GitHub Project? (Choose three.)

**Project workflows**

GitHub Dependabot

GitHub Copilot

**GitHub GraphQL API**

GitHub Charts

Project items

**GitHub Actions**

[💡](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/)


When issues or pull requests are opened in your project, their status is set to Done.

When a GitHub Action is triggered, create a new item in your GitHub Project.

**When pull requests in your project are merged, their status is set to Done.**

[💡](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)

## If you face yourself often writing the same set of comments on issues or pull requests, what GitHub feature would you use to save time?

Comment templates

Labels

**Saved replies**

Repository templates
[💡](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/using-saved-replies)

## Which of these statements about saved replies are true? (Choose two.)

**You can create, edit and delete them in your GitHub account settings in the Saved replies section.**

Saved replies are only available to repository owners which can setup automated replies to issues and pull requests.

**Saved replies are comments that you can reuse in issues and pull requests.**

When someone comments on your issue or pull request, you can save their reply and set a notification to remind yourself about responding to it later.

[💡](https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/using-saved-replies)

## Which of these statements about GitHub Enterprise deployment options are true? (Select two.)

GitHub Enterprise Cloud is a self-hosted platform that runs on the company's infrastructure

**GitHub Enterprise Cloud is a cloud hosted platform that runs on the company's cloud infrastructure**

GitHub Enterprise Server is a set of advanced functionality on GitHub.com

**GitHub Enterprise Server is a self-hosted platform that runs on the company's infrastructure**

GitHub Enterprise Cloud is a set of advanced functionality on GitHub.com

[💡](https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises#about-deployment-options)












